# Skill adherence

Whether the agent read and followed the skill or rule in this repo that the task called for.

A score below 0.5 is a failure. Use `not_applicable` when no file under `skills/`, `agents/task_instructions/rules/`, `conventions/`, or `AGENTS.md` applies to the task. `not_applicable` is not a failure. If tool results are missing, do not treat a missing read as a skip. Say the read cannot be confirmed, and score only the actions that are visible.

| Label | Score | When to use it |
| --- | --- | --- |
| `followed` | 1 | The trace shows a read of the applicable file, and the later edits match it. |
| `one_miss` | 0.8 | The agent followed the file and missed one step that did not change the outcome. |
| `repeated_miss` | 0.4 | The agent missed the same instruction more than once, or it skipped a step the file orders before the edit, such as a failing test before the fix. |
| `ignored` | 0.2 | The applicable file was available, and the session does not follow its main instruction. |

Name the file in the reason. A reason that says "the agent ignored skills" without a path is not a grade.
