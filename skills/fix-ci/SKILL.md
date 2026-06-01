---
name: fix-ci
description: >-
  Investigates failing GitHub PR CI checks, reproduces failures locally, fixes
  scoped issues, commits and pushes, and summarizes changes. Use when CI is
  red, GitHub Actions or checks fail on a PR, or the user asks to fix CI/build/
  lint/test failures for a branch or pull request.
disable-model-invocation: true
metadata:
  owner: mark
  scope: project
  category: execution
---

# Fix CI

End-to-end workflow: identify the PR, read failing checks, reproduce locally, fix, push, and report.

Invoking this skill means the user wants commits and push unless they say otherwise (e.g. "investigate only").

## When to Use

- User passes a GitHub PR or Actions URL.
- User asks to fix CI, failing checks, or a red build on the current branch.
- User asks to find the PR for this branch and fix CI.

## Do Not Use

- Do not use for planning-only or "what failed?" without fixing (use `gh pr checks` briefly instead).
- Do not change workflow files, required checks, or CI config just to make red checks green.
- Do not make unrelated product changes to silence failures.
- Do not merge, force-push, or amend unless the user explicitly asks.

## Resolve the PR

**If the user gave a GitHub URL**, parse owner/repo and PR number or branch from it, then confirm with `gh`.

**If no URL**, resolve from the current branch:

```bash
git branch --show-current
gh pr list --head "$(git branch --show-current)" --json number,url,title,baseRefName --limit 1
```

If multiple PRs match, ask which one. If none match, ask for a PR URL or number.

Record: PR number, URL, head branch, base branch.

```bash
gh pr view <number> --json number,url,title,headRefName,baseRefName,statusCheckRollup
gh pr checks <number>
```

For failed GitHub Actions runs, pull logs (prefer summary first, then failing step):

```bash
gh run list --branch <headRefName> --limit 5
gh run view <run_id> --log-failed
```

Read only what you need from command output; do not dump full logs into the chat.

## Triage CI Failures

1. List failing checks from `gh pr checks` / `statusCheckRollup`.
2. Group by root cause (one fix may clear several checks).
3. Classify each failure:
   - **In scope** — caused by this PR's changes; fix in code/tests/docs the PR touches.
   - **Stale base** — failures on main or fixed elsewhere; merge or rebase base first (`git fetch origin && git merge origin/<base>`), re-run checks.
   - **Out of scope** — flaky infra, broken main, or unrelated service; stop and report; do not hack around.

Scope rules (same spirit as babysit):

- Fix failures this PR introduced or exposed.
- Never weaken or skip checks in YAML to pass.
- If the only fix would be disabling a job or unrelated refactors, report back with evidence.

## Reproduce Locally

1. Ensure you are on the PR head branch and reasonably up to date with its remote.
2. Find the command CI runs:
   - Read `.github/workflows/*.yml` for the failing job's `run:` steps.
   - Check repo docs: `README`, `Makefile`, `package.json` scripts, `pyproject.toml`, `tox.ini`, etc.
3. Run the **same** commands locally (same test paths, lint targets, build flags when practical).
4. If you cannot reproduce (missing secrets, GPU, paid service), say what is missing and use CI logs as the source of truth for the fix.

Iterate: fix → re-run local commands until the previously failing steps pass.

## Fix

- Minimal diff: only what CI requires and what the failure implies.
- Prefer fixing root cause over suppressing warnings or broad refactors.
- Do not commit secrets, `.env`, or credentials.
- Do not revert unrelated user changes; if the worktree has conflicting edits in files you need, stop and ask.

## Commit and Push

Only after local reproduction passes (or remaining gap is documented).

1. `git status` and `git diff` — stage only files for this CI fix.
2. Commit with a clear message focused on **why** (HEREDOC). Example types: `fix`, `test`, `ci` (code/test fixes only — not workflow gaming).
3. `git push` to the PR head branch (set upstream if needed).

Do not push if the user said investigate-only.

## Re-check CI

After push:

```bash
gh pr checks <number> --watch
```

If checks stay red, repeat triage. Stop after a reasonable loop if blocked (permissions, external service, flaky main).

## Final Summary

Return a short report:

### PR

- Link and branch

### What failed

- Check names and one-line cause each

### What you did

- Files touched and nature of fix

### Verification

- Commands run locally and outcomes

### CI after push

- Check status or link to the run

### Follow-ups

- Anything still red, out of scope, or needs user action (secrets, rebase, infra)

Keep the summary scannable; no raw log walls.

## Stop and Ask

- No PR found and user did not provide a URL.
- Ambiguous which PR or which failure to prioritize.
- Fix requires secrets, production access, or policy decisions.
- All failures appear pre-existing on main and rebase did not help.
- User rules conflict (e.g. "do not push") — honor the stricter instruction.

## Tooling

- Use `gh` for all GitHub operations.
- Shell is available: run installs, tests, and linters; do not guess failures without evidence.
