# Verbosity

Whether the agent's messages, code comments, and final summary stayed short enough to review, or repeated work the diff already shows.

A score below 0.5 is a failure. `not_applicable` is not a failure.

| Label | Score | When to use it |
| --- | --- | --- |
| `concise` | 1 | Messages and comments say what changed and why. The agent did not narrate each tool call. |
| `mostly_concise` | 0.8 | One message or a few comments repeat a point the diff already shows, and the rest is direct. |
| `padded` | 0.4 | Several messages, comments, or the final summary restate the same change, or the agent narrates routine tool calls. |
| `verbosity_dominates` | 0.2 | The length of the messages or the comments is the main thing a reviewer would have to skip. |

Holmes marked verbosity as a pass when the agent used a model setting that did not fill the change with comments, and when the pull request was easy to read. Use that case as `concise` or `mostly_concise`.
