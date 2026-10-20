---
name: grade-agent-conversation
description: >-
  Grades a finished coding-agent conversation on verbosity, efficiency, test
  quality, and skill adherence, then proposes edits to skills and rules in
  this repo. Use when the user runs /grade-agent-conversation or asks to
  grade a Claude Code, Cursor, or Codex session.
disable-model-invocation: true
metadata:
  owner: mark
  scope: global
  category: review
---

# Grade agent conversation

Read one finished coding-agent session, write it as a `session-trace/0.1` JSONL file, grade it on the rubrics in this skill, group the failures, and propose edits to files in this repo. The design and the source notes are in `docs/plans/2026-10-19_agent_conversation_grading_8b4df5/proposal.md`. If this skill and that proposal disagree on a field name, follow the proposal until Mark says otherwise.

A session trace is the JSONL file defined below. A failure is a rubric score below 0.5. `not_applicable` is not a failure.

## When to use

- Mark runs `/grade-agent-conversation`.
- Mark asks to grade the current session, or a session he names, on verbosity, efficiency, test quality, or skill adherence.

## Do not use

- Do not use to score a controlled eval with hidden tests. That work is the skills evals proposal.
- Do not edit `skills/` or `agents/` while grading. Proposed diffs stay in the report until Mark asks to apply one.
- Do not commit the trace or the report. Tool results can contain secrets.

## Workflow

```markdown
Grade progress:
- [ ] 1. Choose the session
- [ ] 2. Write the session trace
- [ ] 3. Grade the four rubrics
- [ ] 4. Group failures and write the report
- [ ] 5. Show the scores and stop
```

### 1. Choose the session

If Mark gives a file path, use that file. If he does not, find the newest session whose working directory is this repo, in the store for the program that is running this skill.

| Program | Where the session is | What you can recover |
| --- | --- | --- |
| Claude Code | `~/.claude/projects/<encoded-cwd>/<session-id>.jsonl`. `CLAUDE_CONFIG_DIR` moves the root. Subagent JSONL sits in a directory named for the session id. | Messages, `thinking` blocks, tool calls, tool results, timestamps, `message.model`, `message.usage`. No documented dollar cost. |
| Cursor IDE | `~/.cursor/projects/<workspace-slug>/agent-transcripts/<session-id>/<session-id>.jsonl` | Messages and tool-call inputs. Tool results are omitted. Reasoning is often `[REDACTED]`. Do not read `state.vscdb`. |
| Cursor CLI | A `stream-json` capture if Mark has one. Else `~/.cursor/chats/<hash>/<session-id>/store.db` and `meta.json`. | `stream-json` has the model, tool args, tool results, and `duration_ms`. It has no documented token counts. `store.db` is best-effort. |
| Codex CLI | `$CODEX_HOME/sessions/YYYY/MM/DD/rollout-<timestamp>-<uuid>.jsonl`, default home `~/.codex`. Also read `.jsonl.zst`. `session_index.jsonl` maps an id to a file. | Messages, tool calls, tool results, timestamps, `token_count` events. Model slug is on `turn_context` when present. No documented dollar cost. |
| Cursor Cloud | Prefer `<TRACE_DIR>/<agentId>/<runId>.jsonl` from `tools/cursor_cloud_recorder/archive_cloud_runs.py`. The run file is `session-trace/0.1`, captured by replaying `GET /v1/agents/{id}/runs/{runId}/stream` within about 24 hours of the run. The user prompt, when the recorder saved it, is in `<agentId>/conversation.json` from `GET /v0/agents/{id}/conversation`. | The run file has assistant text, thinking, tool calls, and tool results. Large payloads are marked `truncated`. Token counts are on the usage line, and so is `cost.chargedCents` when the usage payload has it. v0 ids looked stable in SpecStory's spike (`turn-0:step:22:assistant`). Use the id in the file. Drop a user message whose text is `Reminder to commit and push if appropriate.` If the run file is missing because the stream expired, grade the v0 text and mark tool results `absent`. |

The encoded Claude directory replaces non-alphanumeric characters in the working directory with `-`. Codex files are grouped by the day the session started, not by the repo, so resolve them from `session_index.jsonl` or by scanning. IDE and CLI session ids are not interchangeable.

### 2. Write the session trace

Create a directory with `mktemp -d "${TMPDIR:-/tmp}/grade-agent-conversation-XXXXXXXX"` and write `session.jsonl` there. One JSON object per line. Write every key even when the value is null.

The first line is the session header.

```json
{"record_type":"session","schema":"session-trace/0.1","gen_ai.conversation.id":"<session id>","agent_trace.source":"claude_code","agent_trace.source_path":"<file or URL>","agent_trace.cwd":"<cwd>","agent_trace.git_branch":"<branch or null>","agent_trace.harness_version":"<version or null>","gen_ai.provider.name":"<provider or null>","gen_ai.request.model":"<model or null>","agent_trace.started_at":"<ISO-8601 or null>","agent_trace.cost_usd":null}
```

`agent_trace.source` is `claude_code`, `cursor_ide`, `cursor_cli`, `codex_cli`, or `cursor_cloud`. Leave `cost_usd` null unless the source file contains a dollar amount. If a Cloud usage payload has `chargedCents`, set `cost_usd` to that number divided by 100. Do not multiply tokens by a price table.

Later lines use these types.

- `message`, with `gen_ai.operation.name` set to `chat`, plus `timestamp`, `role` (`user`, `assistant`, or `system`), and `content` as an array of `{ "type": "text" | "thinking", "text": "..." }`.
- `tool_call`, with `gen_ai.operation.name` set to `execute_tool`, plus `gen_ai.tool.name`, `gen_ai.tool.call.id`, `gen_ai.tool.call.arguments`, `gen_ai.tool.call.result`, `agent_trace.result_status` (`present`, `absent`, `truncated`, or `error`), `agent_trace.duration_ms`, and `agent_trace.file_edits`. Each file edit is `{ "path", "kind" }` where `kind` is `write`, `edit`, or `delete`.
- `usage`, with `agent_trace.usage_scope` set to `turn` or `session`, plus `gen_ai.usage.input_tokens`, `gen_ai.usage.output_tokens`, `agent_trace.usage.cache_read_input_tokens`, `agent_trace.usage.cache_creation_input_tokens`, `agent_trace.usage.reasoning_output_tokens`, and `agent_trace.cost_usd`. Codex `last_token_usage` is `turn`. Codex `total_token_usage` is `session`.

Keep tool results that you need as evidence. Do not paste those results into chat if they contain secrets, credentials, or large file bodies. Cite the call id and the path instead.

### 3. Grade the four rubrics

Read every file in `rubrics/`. For each rubric, pick one label from that file, copy its score, and write one to three sentences that cite a tool call id, a file path, or a short quote from the trace. If the rubric does not apply, store `not_applicable` and no score. A missing tool result is not evidence that the agent skipped a step. Say that the result was `absent`.

### 4. Group failures and write the report

A failure is a score below 0.5. Cluster failures that share a cause, and name the cluster as an area plus the missing instruction, for example `Routing: when to use end-to-end tests`. A group needs at least one cited moment. Write `report.md` in the temp directory with these sections.

- **Scores.** One row per rubric, with the label, the score or `not_applicable`, and the reason.
- **Failure groups.** The cause, the grades in the group, and the cited moment.
- **Skill and rule feedback.** For each group, the path under `skills/`, `agents/task_instructions/rules/`, `conventions/`, or `AGENTS.md` that should have covered it. Say whether the trace shows a read of that file. Say whether later actions match the file. Include a unified diff for an existing file, or a short outline for a new skill or rule. Change only the step the trace shows was missing. A suggestion with no failed grade does not belong in the report.

Use `skills/README.md` as the index of skills. The rule files are `CLEAN_CODE_PRINCIPLES.md`, `CODING_REPO_CONVENTIONS.md`, `RUN_SERVERS.md`, `UI_RULES.md`, and `router.md`.

### 5. Show the scores and stop

Tell Mark the four labels, the failure-group names, and the absolute path of `report.md`. Ask whether he wants any proposed diff applied. Do not apply it in this run.
