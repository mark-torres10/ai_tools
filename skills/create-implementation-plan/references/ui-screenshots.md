# UI Screenshots Reference (Approach A)

Apply in Phase 2 **only when the UI gate fires** (plan touches `ui/` or equivalent frontend paths in the target project).

**If no UI changes:** skip this file; do not require an empty `images/` tree for plan delivery.

## Agent responsibility (mandatory)

**The agent MUST capture before/after screenshots itself.** Do NOT:

- Write a README or instructions for the user to take screenshots.
- Add a to-do for "someone" to capture screenshots later.
- Delegate screenshot capture to the user.

**The agent MUST:** Use the browser (e.g. Cursor's browser tools or MCP) to:

1. Capture the current UI state **before** implementation → `images/before/` under the plan asset folder.
2. Capture the new UI state **after** implementation → `images/after/`.

If the plan involves UI changes, execution is **not complete** until these screenshots exist. No exceptions.

## Paths (plan package)

```text
docs/plans/<YYYY-MM-DD>_<descriptor>_<hash>/images/before/
docs/plans/<YYYY-MM-DD>_<descriptor>_<hash>/images/after/
```

Create the `images/before/` and `images/after/` directories as part of the package when the UI gate fires (placeholders OK until execution fills them).

## To-do ordering (MUST)

Surface screenshot todos in the package (typically in `spine.md` / Tasks (in order), or as first/last items called out from `plan.md` Happy Flow):

- **First to-do:** agent captures before screenshots (happy path).
- **Last to-do:** agent captures after screenshots (happy path).

The agent performs these steps; it does not document them for the user to do.

## `plan.md` / `verification.md`

- Layer 0 may briefly note "UI before/after screenshots required (agent)" with paths.
- Detailed screenshot acceptance criteria belong in `verification.md` when useful.
- Do not invent image filenames before capture; use clear descriptive names at capture time.

## Phase gate (UI)

Skip entirely if no UI changes.

When UI is in scope, do not finish Phase 2 until:

- [ ] Before-screenshot to-do is first among implementation todos.
- [ ] After-screenshot to-do is last.
- [ ] Plan does not ask the user to take screenshots.
- [ ] `images/before/` and `images/after/` paths are established under the plan asset dir.
- [ ] (During execution) Screenshots exist in those directories.
