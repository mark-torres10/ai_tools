# Efficiency

Whether the agent worked toward the result, or spent the session on rereads, retries, and setup the repo already documents.

A score below 0.5 is a failure. `not_applicable` is not a failure, and it is only for a session that ended before any tool call.

| Label | Score | When to use it |
| --- | --- | --- |
| `highly_efficient` | 1 | The agent took a direct path. It did not reread a file it already had, and it did not redo work. |
| `mostly_efficient` | 0.8 | The agent slipped once or twice, such as one extra read or one early retry, and the slip did not add another round of edits. |
| `mostly_inefficient` | 0.4 | The agent wasted effort more than once, or a check it could have run earlier would have avoided a round of rework. |
| `highly_inefficient` | 0.2 | The waste dominated the session. The same defect was reworked across cycles, the user corrected the same mistake, or the agent looped. |

The labels and scores match the efficiency rubric Ben Holmes showed at AI Engineer New York on 10 October 2026. The descriptions are shortened from that slide.
