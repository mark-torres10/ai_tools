# UI Screenshots Reference

Apply in Phase 4 when the plan touches UI code (anything under `ui/` or equivalent frontend paths in the target project).

## Agent responsibility (mandatory)

**The agent MUST capture before/after screenshots itself.** Do NOT:

- Write a README or instructions for the user to take screenshots.
- Add a to-do for "someone" to capture screenshots later.
- Delegate screenshot capture to the user.

**The agent MUST:** Use the browser (e.g. Cursor's browser tools or MCP) to:

1. Capture the current UI state **before** implementation and save to the plan asset folder under `images/before/`.
2. Capture the new UI state **after** implementation and save to `images/after/`.

If the plan involves UI changes, the plan is **not complete** until these screenshots exist in the plan asset folder. No exceptions.

## Paths

Use the plan asset path from `plan-structure.md`:

```text
docs/plans/<YYYY-MM-DD>_<descriptor>_<hash>/images/before/
docs/plans/<YYYY-MM-DD>_<descriptor>_<hash>/images/after/
```

## To-do ordering (MUST)

For UI changes:

- **First to-do:** agent captures before screenshots (happy path).
- **Last to-do:** agent captures after screenshots (happy path).

The agent performs these steps; it does not document them for the user.

## Phase 4 gate

Skip this phase entirely if the plan has no UI changes.

When UI changes are in scope, do not deliver the plan until:

- [ ] Before-screenshot to-do is first in the plan.
- [ ] After-screenshot to-do is last in the plan.
- [ ] Plan does not ask the user to take screenshots.
- [ ] (During execution) Before screenshots exist in `.../images/before/`.
- [ ] (During execution) After screenshots exist in `.../images/after/`.
