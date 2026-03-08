# Weekly Changelog Update

Create the weekly work update (including rollouts, incidents, and reviews) and weekly changelog entry for the most recently completed Monday-to-Sunday window, then open a PR with the results.

## Scope

- Work only for the week that just ended.
- If the last completed week already has both a weekly update file and a changelog block, stop and do not create duplicates.
- Use only concrete repo evidence: merged PRs, commit history, release notes, and existing docs.

## Week window

1. Determine the most recently completed Monday-to-Sunday date range.
2. Use `YYYY-MM-DD` formatting everywhere.
3. Name the weekly update file `docs/weekly_updates/<start_date>_<end_date>.md`.

## Step 1: Build the weekly update file

Collect the merged PRs for that week and write:

`docs/weekly_updates/<start_date>_<end_date>.md`

Use this exact structure:

```markdown
# Weekly work progress

Dates: <start_date> to <end_date>
Total PRs merged: <count>

## Scope of PRs

- Backend/API & simulation plumbing: <comma-separated markdown links to PRs>
- UI/Frontend: <comma-separated markdown links to PRs>
- Platform, documentation, and quality: <comma-separated markdown links to PRs>
- Automation, CI, and scans: <comma-separated markdown links to PRs>

## Rollouts

- None this period.

## Incidents

- None this period.

## Reviews

- None this period.
```

Notes:

- Match the formatting style above.
- Each PR link should include the title and PR number, for example:
  `[Add example feature (#123)](https://github.com/<org>/<repo>/pull/123)`
- If a category has no PRs, write `- <Category>: None this period.`
- If there were incidents, keep it concise and factual: impact, duration, and link(s) to any relevant PRs or issue threads.
- Keep the list factual and grouped by area.

## Step 2: Update `CHANGELOG.md`

Add a new weekly block near the top of `CHANGELOG.md` for the same date range.

Use this exact section hierarchy for every week:

- `Backend/API`
- `UI/frontend`
- `ML`
- `Platform`
- `Docs/Quality`
- `Automation/CI`
- `Bug Fixes`

For each section:

1. Add a bullet beginning with `- High-level summary:` followed by 2-3 short, factual sentences summarizing that area for the week.
1. Add `- PRs:` and then list the PRs in this exact format:

```markdown
- [https://github.com/<org>/<repo>/pull/<number>](https://github.com/<org>/<repo>/pull/<number>): <PR title>. <1-2 sentence factual description.>
```

1. If a section has no PRs, write:

```markdown
- PRs:
 - _None this week._
```

Classification guidance:

- Backend/API: backend services, persistence, schemas, contracts, simulation plumbing.
- UI/frontend: UI flows, components, typed frontend contracts, UX wiring.
- ML: model, evaluation, ranking, inference, training, simulation intelligence changes.
- Platform: developer environment, infrastructure, deployment, runtime platform support.
- Docs/Quality: docs, linting, tests, architecture rules, maintainability improvements.
- Automation/CI: bots, automation prompts, cron jobs, CI workflows, codegen automation.
- Bug Fixes: regressions or fixes that do not fit better elsewhere.

Required checks:

- Keep the newest week first.
- Ensure links use the full GitHub PR URL.
- Use the weekly update file as a cross-check so the changelog and weekly update stay aligned.
- Be concise, neutral, and specific. Do not speculate.

## Grounding rules

- Use ONLY concrete repo evidence.
- Do NOT invent PR descriptions; confirm them from the PR title, diff, or release notes when needed.
- Prefer the smallest set of edits needed for the new week.
- If evidence is incomplete for a section summary, say less rather than guessing.

## PR setup

When the weekly update file and changelog entry are ready, open a PR using GitHub CLI.

- PR Title: `[YYYY-MM-DD] Codex repo automation - Weekly changelog update`
- PR Description:
  `Automated weekly work update and changelog refresh for the most recently completed week.`
- Add a GitHub tag `codex` so it is clearly marked as automation output.
