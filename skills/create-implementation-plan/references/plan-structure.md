# Plan Structure Reference

Apply when drafting the core sections of an implementation plan (Phase 1).

## Required sections

Every plan must include all of the following:

1. **Overview** – Brief 1-paragraph description of what we're building and why.
2. **Happy Flow** – How data/logic flows end-to-end in this unit of work. Enumerated plain English with file references.
3. **Manual Verification** – Checklist with step-by-step instructions:
   - Test commands (e.g. `uv run pytest ...`)
   - Server startup and checks
   - For UI: clicks, screens, components to review
4. **Alternative approaches** – Short note on options considered and why the chosen approach was selected.
5. **Specificity** – Exact commands, file paths, and component names. No vague steps like "Add auth" or "Fix the bug".
6. **Serial Coordination Spine** – The minimum set of tasks that must stay sequential because they define contracts, unblock dependencies, or integrate parallel work.
7. **Interface or Contract Freeze** – Exact shared interfaces, schemas, types, endpoints, props, DB contracts, or invariants that must be fixed before parallel work starts.
8. **Parallel Task Packets** – As many safely delegable tasks as possible (see `parallel-delegation.md`).
9. **Integration Order** – Exact order for merging or landing completed parallel tasks.
10. **Final Verification** – The end-to-end checks that prove the fully integrated change works.
11. **Update Runbooks** – See `runbooks-audit.md`.

## Remember block (include at top of every plan)

```markdown
## Remember
- Exact file paths always
- Exact commands with expected output
- DRY, YAGNI, TDD, frequent commits
- Maximum safely delegable parallelism
- Delegated tasks must be impossible to misread
- Operational changes: inventory `docs/runbooks/`; list updates and new runbooks from the runbook template
- UI changes: agent captures before/after screenshots itself (no README or instructions for the user)
```

## Plan asset storage

Save all assets related to this workflow in:

```text
docs/plans/<YYYY-MM-DD>_<descriptor of change>_<6-digit hash>/
```

Example: `docs/plans/2026-01-30_change_selector_panels_123456/`

## Phase 1 gate

Do not proceed to Phase 2 until:

- [ ] Overview, Happy Flow, and Manual Verification are present and specific.
- [ ] Remember block is at the top of the plan draft.
- [ ] Plan asset path is chosen if the plan will store artifacts.
