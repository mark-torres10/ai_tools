# Planning rules

In addition to the plan that you make for a certain goal, please do the following:

- Start each plan with a "Overview" section. This is a brief, 1-paragraph description of what we're building and why.
- Add a "Happy Flow" section at the top, with information on how data or logic should flow, end-to-end, in the unit of work. This should be done in enumerated plain English, with references to files.
- Add a "Manual Verification" section with specific, step-by-step instructions for manual verification. This includes (1) running the test suite (e.g., "uv run pytest ..."), running servers, etc. For UI changes, specify the series of clicks to perform or screens to toggle or components to highlight during review. This should be in the form of a checklist.
- Alternative approaches – Short note on options considered and why the chosen approach was selected (e.g. “We chose Y over X because…”)
- Specificity: Avoid vague steps like “Add auth” or “Fix the bug”. Prefer exact commands, file paths, and component names where possible.

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
