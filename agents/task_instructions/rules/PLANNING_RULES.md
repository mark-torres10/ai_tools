# Planning rules

In addition to the plan that you make for a certain goal, please do the following:

- Start each plan with a "Overview" section. This is a brief, 1-paragraph description of what we're building and why.
- Add a "Happy Flow" section at the top, with information on how data or logic should flow, end-to-end, in the unit of work. This should be done in enumerated plain English, with references to files.
- Add a "Manual Verification" section with specific, step-by-step instructions for manual verification. This includes (1) running the test suite (e.g., "uv run pytest ..."), running servers, etc. For UI changes, specify the series of clicks to perform or screens to toggle or components to highlight during review. This should be in the form of a checklist.
- Alternative approaches – Short note on options considered and why the chosen approach was selected (e.g. “We chose Y over X because…”)
- Specificity: Avoid vague steps like “Add auth” or “Fix the bug”. Prefer exact commands, file paths, and component names where possible.
- Save all assets related to this workflow in docs/plans/<YYYY-MM-DD>_<descriptor of change>_<6-digit hash> (e.g., docs/plans/2026-01-30_change_selector_panels_123456/).
- For UI-related changes, before starting work, get a current state of the UI by using the browser tool to take screenshots as needed of the state when doing the intended happy flow. Store this in `docs/plans/<YYYY-MM-DD>_<descriptor of change>_<6-digit hash>/images/before/`. This'll give us a baseline of what it looks like in the beginning, before any changes.
- Once done with UI-related changes, use the browser tool to take screenshots as needed of the state when doing the intended happy flow. Store this in `docs/plans/<YYYY-MM-DD>_<descriptor of change>_<6-digit hash>/images/after/`. This'll let us compare against the images in the `before/` path so we can see the change.
- YOUR FIRST TO-DO item in any UI change MUST BE taking the screenshots of the current UI state. This is a MUST. Your LAST TO-DO item in any UI change must be taking the screenshots of the correct updated UI state.

## DRY, YAGNI, TDD Reminders

Include at top of every plan:

```markdown
## Remember
- Exact file paths always
- Exact commands with expected output
- DRY, YAGNI, TDD, frequent commits
```

## Anti-Patterns

### Don't Do This

- Vague task descriptions
- Missing file paths
- Incomplete code snippets
- Implementation before tests
- No verification steps
- Assuming context
