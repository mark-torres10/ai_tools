---
name: implement-plan-and-open-pr
description: Implements an existing implementation plan to completion, verifies the result, creates a pull request using write-pr-description for the PR body, and returns the PR URL. Use only when the user explicitly asks to execute a plan end-to-end, open a PR, and provide the link.
disable-model-invocation: true
metadata:
  owner: mark
  scope: project
  category: execution
---

# Implement Plan And Open PR

Execute a plan end-to-end.

Do not use this skill unless the user explicitly asked for the full implementation + PR workflow and explicitly cites it.

## When to Use

- The user provides a plan and asks to implement it to completion.
- The user asks to execute a plan created earlier in `docs/plans/...`.
- The user wants the final deliverable to be an open PR and a returned PR URL.
- The user expects `write-pr-description` to be used for the PR title/body.

## Do Not Use

- Do not use for planning only.
- Do not use when the user only wants code edits without git/PR actions.
- Do not use when the plan is ambiguous or incomplete.
- Do not use when the repo is in a conflicting dirty state and the relevant files already contain unrelated user changes that would be risky to touch.

## Setup

Before making changes, confirm all of the following:

- The user explicitly asked for implementation plus PR creation.
- The exact plan file is known.
- The plan contains enough specificity to implement.
- Any required credentials or local tooling needed for verification are available.

If any of these steps fail, stop and ask instead of guessing.

## Execution Rules

- Follow the plan. Do not silently redesign it. Do NOT make updates to plan.md or any step files.
- Review CODING_RULES.md and UNIT_TESTING_STANDARDS.md before any implementation. You must be in compliance with these standards.
- Preserve the plan's contract and invariants.
- Only parallelize tasks that are clearly independent and safe.
- Never revert unrelated user changes.
- If unexpected unrelated changes appear in files you need to edit, stop and ask the user how to proceed.
- Do not commit secrets or env files.
- Do not skip verification.
- Do not open a PR until verification is complete or the remaining failures are clearly identified as pre-existing and unrelated.

## Workflow

1. Read the plan fully.
2. Extract:
   - objective
   - exact files to inspect
   - exact files likely to change
   - contracts and invariants
   - verification commands
   - screenshot requirements
3. Read `skills/write-pr-description/SKILL.md` so the PR description uses the project's required format.
4. Review CODING_RULES.md and UNIT_TESTING_STANDARDS.md.
5. Inspect the current git state.. If currently on `main` or `master`, create a feature branch named from the plan descriptor.
6. If the plan includes UI work and before screenshots are missing, capture them before editing.
7. Implement the plan in the required order.
8. Run the plan's verification steps.
9. If verification fails, iterate until:
   - all required checks pass, or
   - you are blocked by an external dependency, missing credential, or pre-existing unrelated failure
10. Review the final diff to ensure the implemented changes match the plan. Ensure that your implementation complies with CODING_RULES.md and UNIT_TESTING_STANDARDS.md. For docstrings, apply the `write-docstring` skill.
11. Stage only the relevant files.
12. Create the commit.
13. Draft the PR title and body by applying `write-pr-description`.
14. Push the branch.
15. Open the PR.
16. Update the CHANGELOG.md, using the `write-changelog` skill. If the CHANGELOG.md file doesn't exist, create it. Then commit to the PR and push.
17. Return PR URL, executive summary of what was built,verification summary, and any known follow-ups.

## Required Verification Standard

The change is not complete until all of the following are true:

- The code implementing the plan exists.
- Required tests, linters, builds, or manual checks have been run.
- The actual result matches the plan's acceptance criteria.
- UI before/after screenshots exist when required by the plan.
- The branch is pushed.
- The PR is open.
- The PR URL is returned to the user.

## PR Creation Rules

Use the repository's PR-writing workflow from `skills/write-pr-description/SKILL.md`.

Do not invent a new PR structure if that file is available.

If the plan has a matching asset folder in `docs/plans/...`, include those paths in the PR body when the type guide or verification section calls for them.

## Stop Conditions

Stop and ask the user if any of the following occurs:

- Multiple plausible plan files exist.
- The plan is missing exact verification steps.
- Required local services or credentials are unavailable.
- The git worktree contains conflicting unrelated edits in files the plan requires changing.
- The PR cannot be opened because authentication, remote permissions, or branch protection prevent it.

## Final Response Format

Return a concise result with:

- PR URL
- branch name
- commit summary
- verification performed
- any blockers, caveats, or follow-up work

If blocked before PR creation, return:

- what was completed
- the exact blocking condition
- the next action required from the user
