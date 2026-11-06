# Cursor Cloud recorder

`archive_cloud_runs.py` saves a Cursor Cloud run before the stream expires. Mark ran it against `api.cursor.com` on 20 October 2026, and that run saved 5 streams. One file had 8823 lines: 5813 `interaction_update`, 1804 `thinking`, 932 `assistant`, and 268 `tool_call`, plus `status`, `result`, `done`, `usage`, and `run` records. The same run returned HTTP 429 on about 10 runs after a burst, and HTTP 410 on about 20 older runs. The script now stays under 20 requests per minute. It retries a 429. When the response has `Retry-After`, the script waits that long. Otherwise the waits are 2, 4, 8, 16, 32, and 60 seconds. It also skips a run whose own `updatedAt` is outside retention, and it logs a 410 as `expired` on stdout. Other HTTP failures still go to stderr. The throttle and the `updatedAt` filter came after that run, so the live test does not cover them. `--self-check` maps a fake stream and checks the throttle math. It does not open a socket:

```bash
python3 tools/cursor_cloud_recorder/archive_cloud_runs.py --self-check
```

A real run needs `CURSOR_API_KEY` from Cursor Dashboard, API Keys. The script sends it as Basic auth (`-u KEY:`). It does not read the key from a file.

```bash
export CURSOR_API_KEY=...
python3 tools/cursor_cloud_recorder/archive_cloud_runs.py
```

`TRACE_DIR` overrides the output directory. The default is `./cursor-cloud-traces`, which is gitignored. Run the script hourly or daily. The script lists `GET /v1/agents` newest first, and it stops when an agent's `updatedAt` is outside retention. It replays `GET /v1/agents/{id}/runs/{runId}/stream` when the run is not `CREATING` or `RUNNING`. The run's own `updatedAt` also has to be inside the window. The runs list is newest first, so the scan stops at the first run outside the window. Retention starts at 86400 seconds, which is the `X-Cursor-Stream-Retention-Seconds` value SpecStory measured. When a stream response includes that header, later requests use the new value. After the window, Cursor returns `410 stream_expired`. The script prints `expired <agentId>/<runId>` and continues.

The first connection right after launch often fails with `stream_unavailable`. Pulling after the run has left `RUNNING` is the reliable case. A skipped run is retried on the next pass, because the script only skips a run whose session-trace file already exists.

## Files

For each run the script writes:

- `<agentId>/<runId>.events.jsonl`, one JSON object per SSE event, then one `usage` line and one `run` line.
- `<agentId>/<runId>.jsonl`, the same run in `session-trace/0.1`.
- `<agentId>/conversation.json`, the v0 conversation for the whole agent, when that call succeeds.

v0 messages cover every run on the agent. The script does not copy the v0 messages into a single run's session-trace file, because the v0 payload has no `runId`. SpecStory fetched the v0 payload twice on 6 October 2026, and the message ids stayed stable (`turn-0:step:22:assistant`). The skill uses those ids. A March 2026 forum report said the ids changed on every read. The March 2026 report did not reproduce in the SpecStory spike.

## Mapping into session-trace/0.1

| Stream or usage field | Session-trace field |
| --- | --- |
| Run id | `gen_ai.conversation.id` |
| Agent id | `agent_trace.agent_id` |
| `git.branches[0].branch` and `prUrl` | `agent_trace.git_branch`, `agent_trace.pr_url` |
| `createdAt`, `durationMs` | `agent_trace.started_at`, `agent_trace.duration_ms` |
| `assistant` text deltas, joined until a tool call or `result` | `message` role `assistant`, content type `text` |
| `thinking` deltas in that same stretch | the same message, content type `thinking` |
| `tool_call` `callId`, `name`, `args`, `result` | `gen_ai.tool.call.id`, `gen_ai.tool.name`, `gen_ai.tool.call.arguments`, `gen_ai.tool.call.result` |
| A later `completed` event for the same `callId` | replaces the `running` row |
| A result body is present, and `truncated.result` is not set | `agent_trace.result_status` `present` |
| `truncated.result`, or `truncated.args` with no result body | `agent_trace.result_status` `truncated` |
| No result body and no `truncated` flag | `agent_trace.result_status` `absent` |
| `edit_file` or a write or delete tool with `args.path` | `agent_trace.file_edits` |
| Usage `inputTokens`, `outputTokens`, `cacheReadTokens`, `cacheWriteTokens` | the `usage` line, scope `session` |
| `chargedCents`, when present | `agent_trace.cost_usd` as cents divided by 100 |

`status`, `heartbeat`, `interaction_update`, `error`, and `done` stay in the events file. The published usage example has token counts and no dollar field. SpecStory's spike saw `cost.chargedCents` on the live object, so the mapper copies it when the key is present and otherwise writes null.

The documented stream events do not include the user prompt. The prompt text is on the v0 conversation. The documented run object does not include the model id.

SDK `run.conversation()` is not used. Nobody has checked, for this proposal, whether that call returns a structured transcript. Nobody has checked how long the SDK keeps one. The proposal treats the call as unverified, and the proposal assumes the same retention as the stream until a check says otherwise.
