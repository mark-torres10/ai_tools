#!/usr/bin/env python3
"""Archive Cursor Cloud runs before the stream expires.

Mark ran this script against api.cursor.com on 20 October 2026. That run
saved 5 streams. One file had 8823 lines. The same run returned HTTP 429
on about 10 runs after a burst, and HTTP 410 on about 20 older runs of
agents that were still inside the agent list window. This file now stays
under 20 requests per minute, retries a 429, and skips a run whose own
updatedAt is outside retention. Those two guards were not in the 20
October run. ``--self-check`` does not open a socket.

A scheduled run (hourly or daily) lists recent agents, replays each
finished run's SSE stream, and writes two files per run:

  <TRACE_DIR>/<agentId>/<runId>.events.jsonl   raw SSE, then usage and the run
  <TRACE_DIR>/<agentId>/<runId>.jsonl          session-trace/0.1

It also writes ``<TRACE_DIR>/<agentId>/conversation.json`` from the v0
conversation endpoint when that call succeeds. v0 is the whole agent, not one
run, so those messages are not copied into the run's session-trace file.

Requires CURSOR_API_KEY (Cursor Dashboard, API Keys). Standard library only.
TRACE_DIR defaults to ./cursor-cloud-traces.
"""

from __future__ import annotations

import base64
import email.utils
import json
import os
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timedelta, timezone

API = "https://api.cursor.com"
OUT = os.environ.get("TRACE_DIR", "cursor-cloud-traces")
SCHEMA = "session-trace/0.1"
SKIP_STATUS = {"CREATING", "RUNNING"}
# SpecStory measured this header at 86400. A live response can replace it.
DEFAULT_RETENTION_SECONDS = 86400
# Documented limit is 20 requests per minute. Stay under that cap.
MAX_REQUESTS_PER_MINUTE = 19
WINDOW_SECONDS = 60.0
MAX_429_ATTEMPTS = 6


def _auth_header(key: str) -> str:
    return "Basic " + base64.b64encode(f"{key}:".encode()).decode()


def header_value(headers, name: str) -> str | None:
    if not headers:
        return None
    getter = getattr(headers, "get", None)
    if getter is not None:
        direct = getter(name)
        if direct not in (None, ""):
            return str(direct)
    items = getattr(headers, "items", None)
    if items is None:
        return None
    wanted = name.lower()
    for key, value in items():
        if str(key).lower() == wanted and value not in (None, ""):
            return str(value)
    return None


def parse_retry_after(value: str | None, now: datetime | None = None) -> float | None:
    """Return seconds to wait, or None when the header is missing or invalid."""
    if value is None:
        return None
    text = str(value).strip()
    if not text:
        return None
    try:
        return max(0.0, float(text))
    except ValueError:
        pass
    parsed = email.utils.parsedate_to_datetime(text)
    if parsed is None:
        return None
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    current = now or datetime.now(timezone.utc)
    return max(0.0, (parsed - current).total_seconds())


def retry_delay(headers, attempt: int) -> float:
    parsed = parse_retry_after(header_value(headers, "Retry-After"))
    if parsed is not None:
        return parsed
    return min(60.0, 2.0 ** (attempt + 1))


def parse_retention_seconds(headers) -> int | None:
    raw = header_value(headers, "X-Cursor-Stream-Retention-Seconds")
    if raw is None:
        return None
    try:
        value = int(str(raw).strip())
    except ValueError:
        return None
    if value <= 0:
        return None
    return value


def parse_timestamp(value) -> datetime | None:
    if not isinstance(value, str) or not value:
        return None
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed


def run_within_retention(run: dict, now: datetime, retention_seconds: int) -> bool:
    """True when the run's own updatedAt is still inside the stream window.

    A missing timestamp is kept, so the caller can try the stream and log a
    410 if Cursor has already expired it.
    """
    updated = parse_timestamp(run.get("updatedAt")) or parse_timestamp(run.get("createdAt"))
    if updated is None:
        return True
    return updated >= now - timedelta(seconds=retention_seconds)


def wait_seconds(
    stamps: list[float],
    now: float,
    not_before: float,
    max_requests: int = MAX_REQUESTS_PER_MINUTE,
    window: float = WINDOW_SECONDS,
) -> float:
    """How long to sleep before the next request stays under the cap."""
    if now < not_before:
        return not_before - now
    live = [stamp for stamp in stamps if now - stamp < window]
    if len(live) < max_requests:
        return 0.0
    oldest = min(live)
    return max(0.0, oldest + window - now)


class Retention:
    def __init__(self, seconds: int = DEFAULT_RETENTION_SECONDS) -> None:
        self.seconds = seconds

    def observe(self, headers) -> int | None:
        parsed = parse_retention_seconds(headers)
        if parsed is None or parsed == self.seconds:
            return None
        self.seconds = parsed
        return parsed


class RateLimiter:
    """Keep one process under 20 requests in any 60 second window."""

    def __init__(self) -> None:
        self.stamps: list[float] = []
        self.not_before = 0.0

    def wait(self) -> None:
        while True:
            now = time.monotonic()
            delay = wait_seconds(self.stamps, now, self.not_before)
            if delay <= 0:
                break
            time.sleep(delay)
        now = time.monotonic()
        self.stamps = [stamp for stamp in self.stamps if now - stamp < WINDOW_SECONDS]
        self.stamps.append(now)

    def penalize(self, seconds: float) -> None:
        self.not_before = max(self.not_before, time.monotonic() + max(0.0, seconds))


def get(path: str, key: str, limiter: RateLimiter, accept: str = "application/json"):
    req = urllib.request.Request(
        API + path,
        headers={"Authorization": _auth_header(key), "Accept": accept},
    )
    for attempt in range(MAX_429_ATTEMPTS):
        limiter.wait()
        try:
            return urllib.request.urlopen(req, timeout=300)
        except urllib.error.HTTPError as exc:
            if exc.code != 429 or attempt + 1 >= MAX_429_ATTEMPTS:
                raise
            delay = retry_delay(exc.headers, attempt)
            print(f"429 {path}, retry in {delay:.0f}s", file=sys.stderr)
            exc.close()
            limiter.penalize(delay)
    raise RuntimeError(f"429 retries exhausted for {path}")


def parse_sse_lines(lines):
    """Yield one dict per SSE event. Stop after ``done``."""
    event: dict = {}
    data_parts: list[str] = []

    def flush():
        nonlocal event, data_parts
        if data_parts:
            blob = "\n".join(data_parts)
            try:
                event["data"] = json.loads(blob)
            except ValueError:
                event["data"] = blob
        finished = None
        if event.get("event"):
            finished = dict(event)
        event = {}
        data_parts = []
        return finished

    for line in lines:
        if isinstance(line, bytes):
            line = line.decode("utf-8", errors="replace")
        line = line.rstrip("\r\n")
        if line == "":
            finished = flush()
            if finished:
                yield finished
                if finished["event"] == "done":
                    return
            continue
        if line.startswith(":"):
            continue
        field, _, value = line.partition(":")
        if value.startswith(" "):
            value = value[1:]
        if field == "id":
            event["id"] = value
        elif field == "event":
            event["event"] = value
        elif field == "data":
            data_parts.append(value)
    finished = flush()
    if finished:
        yield finished


def find_charged_cents(obj):
    """Return the first chargedCents number, or None.

    The published usage example lists token fields only. SpecStory's live
    spike saw cost.chargedCents on this payload. The key may sit on the
    top-level object or under a run.
    """
    if isinstance(obj, dict):
        cents = obj.get("chargedCents")
        if isinstance(cents, (int, float)):
            return cents
        for value in obj.values():
            found = find_charged_cents(value)
            if found is not None:
                return found
    elif isinstance(obj, list):
        for value in obj:
            found = find_charged_cents(value)
            if found is not None:
                return found
    return None


def usage_for_run(usage_body: dict | None, run_id: str) -> dict:
    runs = (usage_body or {}).get("runs") or []
    for row in runs:
        if row.get("id") == run_id:
            return row.get("usage") or {}
    if len(runs) == 1:
        return runs[0].get("usage") or {}
    return {}


def file_edits(name: str | None, args) -> list[dict]:
    if not isinstance(args, dict):
        return []
    path = args.get("path") or args.get("file_path") or args.get("target_file")
    if not path or not isinstance(path, str):
        return []
    label = (name or "").lower()
    if "delete" in label:
        kind = "delete"
    elif "write" in label:
        kind = "write"
    elif "edit" in label or label in {"strreplace", "search_replace"}:
        kind = "edit"
    else:
        return []
    return [{"path": path, "kind": kind}]


def _tool_record(data: dict) -> dict:
    truncated = data.get("truncated") or {}
    if not isinstance(truncated, dict):
        truncated = {}
    if data.get("result") is not None and not truncated.get("result"):
        result_status = "present"
    elif truncated.get("result") or truncated.get("args"):
        result_status = "truncated"
    else:
        result_status = "absent"
    args = data.get("args")
    return {
        "record_type": "tool_call",
        "gen_ai.operation.name": "execute_tool",
        "timestamp": None,
        "gen_ai.tool.name": data.get("name"),
        "gen_ai.tool.call.id": data.get("callId"),
        "gen_ai.tool.call.arguments": args if isinstance(args, dict) else args,
        "gen_ai.tool.call.result": data.get("result"),
        "agent_trace.result_status": result_status,
        "agent_trace.duration_ms": None,
        "agent_trace.file_edits": file_edits(data.get("name"), args),
    }


def map_run(agent_id: str, run: dict, events: list[dict], usage_body: dict | None) -> list[dict]:
    """Map one replayed stream plus the usage payload to session-trace/0.1."""
    run_id = run["id"]
    branches = ((run.get("git") or {}).get("branches")) or []
    git = branches[0] if branches else {}
    cents = find_charged_cents(usage_body)
    cost = None if cents is None else cents / 100.0
    tokens = usage_for_run(usage_body, run_id)
    records: list[dict] = [
        {
            "record_type": "session",
            "schema": SCHEMA,
            "gen_ai.conversation.id": run_id,
            "agent_trace.agent_id": agent_id,
            "agent_trace.source": "cursor_cloud",
            "agent_trace.source_path": (
                f"{API}/v1/agents/{agent_id}/runs/{run_id}/stream"
            ),
            "agent_trace.cwd": None,
            "agent_trace.git_branch": git.get("branch"),
            "agent_trace.pr_url": git.get("prUrl"),
            "agent_trace.harness_version": None,
            "gen_ai.provider.name": None,
            "gen_ai.request.model": None,
            "agent_trace.started_at": run.get("createdAt"),
            "agent_trace.duration_ms": run.get("durationMs"),
            "agent_trace.cost_usd": cost,
        }
    ]
    assistant: list[str] = []
    thinking: list[str] = []
    call_index: dict[str, int] = {}

    def flush() -> None:
        if not assistant and not thinking:
            return
        content = []
        if thinking:
            content.append({"type": "thinking", "text": "".join(thinking)})
        if assistant:
            content.append({"type": "text", "text": "".join(assistant)})
        records.append(
            {
                "record_type": "message",
                "gen_ai.operation.name": "chat",
                "timestamp": None,
                "role": "assistant",
                "gen_ai.response.model": None,
                "content": content,
            }
        )
        assistant.clear()
        thinking.clear()

    for ev in events:
        kind = ev.get("event")
        data = ev.get("data") if isinstance(ev.get("data"), dict) else {}
        if kind == "assistant":
            assistant.append(data.get("text") or "")
        elif kind == "thinking":
            thinking.append(data.get("text") or "")
        elif kind == "tool_call":
            flush()
            call_id = data.get("callId") or ""
            record = _tool_record(data)
            if call_id in call_index and data.get("status") == "completed":
                records[call_index[call_id]] = record
            elif call_id not in call_index:
                call_index[call_id] = len(records)
                records.append(record)
        elif kind == "result":
            flush()
    flush()
    records.append(
        {
            "record_type": "usage",
            "timestamp": run.get("updatedAt"),
            "agent_trace.usage_scope": "session",
            "gen_ai.response.model": None,
            "gen_ai.usage.input_tokens": tokens.get("inputTokens"),
            "gen_ai.usage.output_tokens": tokens.get("outputTokens"),
            "agent_trace.usage.cache_read_input_tokens": tokens.get("cacheReadTokens"),
            "agent_trace.usage.cache_creation_input_tokens": tokens.get("cacheWriteTokens"),
            "agent_trace.usage.reasoning_output_tokens": None,
            "agent_trace.cost_usd": cost,
        }
    )
    return records


def recent_agents(key: str, limiter: RateLimiter, retention: Retention):
    cursor = ""
    while True:
        path = "/v1/agents?limit=100" + (f"&cursor={cursor}" if cursor else "")
        page = json.load(get(path, key, limiter))
        cutoff = datetime.now(timezone.utc) - timedelta(seconds=retention.seconds)
        for agent in page.get("items") or []:
            updated = parse_timestamp(agent.get("updatedAt"))
            if updated is not None and updated < cutoff:
                return
            yield agent
        cursor = page.get("nextCursor") or ""
        if not cursor:
            return


def list_runs(
    key: str, agent_id: str, limiter: RateLimiter, retention: Retention
) -> list[dict]:
    """Return runs still inside the retention window.

    The runs endpoint is newest first, so the first run outside the window
    ends the scan.
    """
    cursor = ""
    rows: list[dict] = []
    while True:
        path = f"/v1/agents/{agent_id}/runs?limit=100" + (
            f"&cursor={cursor}" if cursor else ""
        )
        page = json.load(get(path, key, limiter))
        now = datetime.now(timezone.utc)
        for run in page.get("items") or []:
            if not run_within_retention(run, now, retention.seconds):
                return rows
            rows.append(run)
        cursor = page.get("nextCursor") or ""
        if not cursor:
            return rows


def _write_jsonl(path: str, rows: list[dict]) -> None:
    with open(path, "w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")


def archive_run(
    key: str,
    agent_id: str,
    run: dict,
    limiter: RateLimiter,
    retention: Retention,
) -> None:
    run_id = run["id"]
    if run.get("status") in SKIP_STATUS:
        return
    directory = os.path.join(OUT, agent_id)
    trace_path = os.path.join(directory, f"{run_id}.jsonl")
    if os.path.exists(trace_path):
        return
    if not run_within_retention(run, datetime.now(timezone.utc), retention.seconds):
        print(f"expired {agent_id}/{run_id}")
        return
    os.makedirs(directory, exist_ok=True)
    try:
        resp = get(
            f"/v1/agents/{agent_id}/runs/{run_id}/stream",
            key,
            limiter,
            "text/event-stream",
        )
    except urllib.error.HTTPError as exc:
        updated = retention.observe(exc.headers)
        if updated is not None:
            print(f"retention {updated}s")
        if exc.code == 410:
            print(f"expired {agent_id}/{run_id}")
            return
        # stream_unavailable is common on the first connection right after
        # launch. A later scheduled pass retries a run that has no trace file.
        print(f"skip {agent_id}/{run_id}: HTTP {exc.code}", file=sys.stderr)
        return
    updated = retention.observe(resp.headers)
    if updated is not None:
        print(f"retention {updated}s")
    events = list(parse_sse_lines(resp))
    events_path = os.path.join(directory, f"{run_id}.events.jsonl")
    _write_jsonl(events_path, events)
    try:
        usage = json.load(
            get(f"/v1/agents/{agent_id}/usage?runId={run_id}", key, limiter)
        )
    except urllib.error.HTTPError as exc:
        print(f"usage {agent_id}/{run_id}: HTTP {exc.code}", file=sys.stderr)
        usage = None
    with open(events_path, "a", encoding="utf-8") as handle:
        handle.write(json.dumps({"event": "usage", "data": usage}) + "\n")
        handle.write(json.dumps({"event": "run", "data": run}) + "\n")
    _write_jsonl(trace_path, map_run(agent_id, run, events, usage))
    print(f"archived {trace_path}")


def save_conversation(key: str, agent_id: str, limiter: RateLimiter) -> None:
    path = os.path.join(OUT, agent_id, "conversation.json")
    if os.path.exists(path):
        return
    try:
        payload = json.load(get(f"/v0/agents/{agent_id}/conversation", key, limiter))
    except urllib.error.HTTPError as exc:
        print(f"conversation {agent_id}: HTTP {exc.code}", file=sys.stderr)
        return
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        json.dump(payload, handle)
        handle.write("\n")


def archive_all(key: str) -> None:
    limiter = RateLimiter()
    retention = Retention()
    for agent in recent_agents(key, limiter, retention):
        agent_id = agent["id"]
        save_conversation(key, agent_id, limiter)
        for run in list_runs(key, agent_id, limiter, retention):
            archive_run(key, agent_id, run, limiter, retention)


def self_check() -> None:
    raw = "\n".join(
        [
            'event: assistant',
            'data: {"text":"I will "}',
            "",
            'event: assistant',
            'data: {"text":"edit the test."}',
            "",
            "event: thinking",
            'data: {"text":"Read the skill first."}',
            "",
            "event: tool_call",
            'data: {"callId":"c1","name":"edit_file","status":"running","args":{"path":"tests/test_notes.py"}}',
            "",
            "event: tool_call",
            'data: {"callId":"c1","name":"edit_file","status":"completed","args":{"path":"tests/test_notes.py"},"result":{"ok":true},"truncated":{"args":true}}',
            "",
            "event: done",
            "data: {}",
            "",
        ]
    )
    events = list(parse_sse_lines(raw.splitlines(keepends=True)))
    assert [ev["event"] for ev in events] == [
        "assistant",
        "assistant",
        "thinking",
        "tool_call",
        "tool_call",
        "done",
    ]
    run = {
        "id": "run-1",
        "status": "FINISHED",
        "createdAt": "2026-10-20T00:00:00.000Z",
        "updatedAt": "2026-10-20T00:05:00.000Z",
        "durationMs": 5000,
        "git": {"branches": [{"branch": "cursor/example", "prUrl": "https://example.com/1"}]},
    }
    usage = {
        "runs": [
            {
                "id": "run-1",
                "usage": {
                    "inputTokens": 10,
                    "outputTokens": 2,
                    "cacheWriteTokens": 3,
                    "cacheReadTokens": 4,
                    "totalTokens": 19,
                },
                "cost": {"chargedCents": 43},
            }
        ]
    }
    rows = map_run("bc-1", run, events, usage)
    assert rows[0]["schema"] == SCHEMA
    assert rows[0]["agent_trace.source"] == "cursor_cloud"
    assert rows[0]["agent_trace.cost_usd"] == 0.43
    assert rows[0]["agent_trace.git_branch"] == "cursor/example"
    message = rows[1]
    assert message["content"][0]["type"] == "thinking"
    assert message["content"][1]["text"] == "I will edit the test."
    tool = rows[2]
    assert tool["gen_ai.tool.call.id"] == "c1"
    # The result body is present. truncated.args does not hide it.
    assert tool["agent_trace.result_status"] == "present"
    assert tool["agent_trace.file_edits"] == [{"path": "tests/test_notes.py", "kind": "edit"}]
    omitted = _tool_record(
        {
            "callId": "c2",
            "name": "read_file",
            "status": "completed",
            "truncated": {"result": True},
        }
    )
    assert omitted["agent_trace.result_status"] == "truncated"
    assert omitted["gen_ai.tool.call.result"] is None
    usage_row = rows[3]
    assert usage_row["gen_ai.usage.input_tokens"] == 10
    assert usage_row["agent_trace.usage.cache_creation_input_tokens"] == 3
    assert usage_row["agent_trace.cost_usd"] == 0.43
    assert find_charged_cents({}) is None
    moment = datetime(2026, 10, 20, 12, 0, tzinfo=timezone.utc)
    assert run_within_retention({"updatedAt": "2026-10-20T11:00:00Z"}, moment, 86400)
    assert not run_within_retention({"updatedAt": "2026-10-19T11:00:00Z"}, moment, 86400)
    assert run_within_retention({"createdAt": "2026-10-20T11:30:00Z"}, moment, 86400)
    assert run_within_retention({}, moment, 86400)
    assert parse_retention_seconds({"X-Cursor-Stream-Retention-Seconds": "86400"}) == 86400
    assert parse_retention_seconds({}) is None
    holder = Retention()
    assert holder.observe({"x-cursor-stream-retention-seconds": "1000"}) == 1000
    assert holder.seconds == 1000
    assert holder.observe({"X-Cursor-Stream-Retention-Seconds": "1000"}) is None
    assert parse_retry_after("12") == 12.0
    assert parse_retry_after(None) is None
    assert parse_retry_after("Wed, 21 Oct 2026 12:00:00 GMT", now=moment) == 86400.0
    assert retry_delay({}, 0) == 2.0
    assert retry_delay({"Retry-After": "9"}, 0) == 9.0
    burst = [1_000.0 - 50.0 + index for index in range(MAX_REQUESTS_PER_MINUTE)]
    assert wait_seconds(burst, 1_000.0, 0.0) > 0
    assert wait_seconds(burst[:-1], 1_000.0, 0.0) == 0.0
    assert wait_seconds([], 1_000.0, 1_005.0) == 5.0
    print("self-check ok")


def main(argv: list[str]) -> int:
    if "--self-check" in argv:
        self_check()
        return 0
    key = os.environ.get("CURSOR_API_KEY", "").strip()
    if not key:
        print("CURSOR_API_KEY is not set", file=sys.stderr)
        return 2
    archive_all(key)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
