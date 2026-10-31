# The second-pass trick

Source: Youssef Hosni, 30 October 2026. [Post](https://x.com/YoussefHosni951/status/2116250056747782343). Infographic title: "The second-pass trick". Header: "Claude Code + Codex. Rewrite after learning."

## Post

- One of the most useful prompts is to throw away the solution just built.
- The first solution often records uncertainty from the way there: unnecessary abstractions, temporary helpers, duplicated logic, and extra layers that are no longer needed.
- By the time it works, the agent knows more about the problem.
- Hosni attributes this prompt to engineers on the Claude Code team:

  > Knowing everything you know now, scrap this and implement the elegant solution.

- The second pass uses what the first pass learned. It can show simpler data flows, existing functions worth reusing, and abstractions to remove.
- The first implementation learns the problem. The second pass simplifies the solution.
- For a safe demonstration, preserve the original with git, ask for the simplification, and compare the diff and the test results. A second pass is not automatically better.

## Infographic

After the first working implementation, ask the agent to rebuild it more elegantly using what it learned.

First pass (`~/first-pass`), prompt "Build the feature":

- `temp_helper.ts`
- `adapter_v2.ts`
- duplicate validation
- works, but noisy
- It learned the problem.

Second pass (`~/second-pass`), prompt "Rebuild it elegantly":

- shared validator
- remove temp layer
- simpler flow
- same behavior, less code
- It simplifies the solution.

| Pass | What it does |
|------|----------------|
| Learn | The first implementation helps the agent understand the real shape of the problem. |
| Simplify | Use what it learned to remove extra layers, duplicated logic, and temporary structure. |
| Compare | Keep the tests, inspect the diff, and choose the cleaner version only if it still holds up. |

`rewrite-prompt.txt`, for after the first version works:

> Knowing everything you know now, scrap this and implement the elegant solution.

- Ask for a cleaner implementation, not just more fixes.
- Run the same tests and compare the diff before keeping it.

The first pass learns. The second pass can make it elegant.
