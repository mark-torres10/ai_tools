---
name: implement-plan-and-open-pr
description: Implements an existing implementation plan to completion, verifies the result, creates a pull request using the local create-pr skill, and returns the PR URL. Use only when the user explicitly asks to execute a plan end-to-end, open a PR, and provide the link.
disable-model-invocation: true
metadata:
  owner: mark
  scope: project
  category: execution
---

# Implement Plan And Open PR

Execute a previously written implementation plan end-to-end.

This skill is for high-side-effect work:
- code edits
- test and build execution
- branch creation
- commits
- push
- PR creation

Do not use this skill unless the user explicitly asked for the full implementation + PR workflow.

## When to Use

- The user provides a plan and asks to implement it to completion.
- The user asks to execute a plan created earlier in `docs/plans/...`.
- The user wants the final deliverable to be an open PR and a returned PR URL.
- The user expects the existing `create-pr` skill to be used for the PR title/body.

## Do Not Use

- Do not use for planning only.
- Do not use when the user only wants code edits without git/PR actions.
- Do not use when the plan is ambiguous or incomplete.
- Do not use when the repo is in a conflicting dirty state and the relevant files already contain unrelated user changes that would be risky to touch.

## Path Discovery

Resolve the `ai_tools` root in this order:

1. Check for `./ai_tools/` in the workspace root.
2. Otherwise use `/Users/mark/Documents/projects/ai_tools/`.

Required files:

- Plan source: user-provided path, or an explicitly referenced file in `docs/plans/...`
- PR skill: `<ai_tools_root>/skills/create-pr/SKILL.md`
- Planning skill: `<ai_tools_root>/skills/create-implementation-plan/SKILL.md`

If the plan path is ambiguous, stop and ask the user to identify the exact plan file.

If `create-pr` is missing, stop and ask the user how to proceed. Do not improvise a different PR format when this skill is expected.

## Preconditions

Before making changes, confirm all of the following:

- The user explicitly asked for implementation plus PR creation.
- The exact plan file is known.
- The plan contains enough specificity to implement safely:
  - Overview
  - Happy Flow
  - Manual Verification
  - exact file paths or exact components to inspect
  - exact verification commands or exact manual checks
- Any required credentials or local tooling needed for verification are available.
- If the plan includes UI work and before screenshots are required, they already exist or can be captured before the first code edit.

If any precondition fails, stop and ask instead of guessing.

## Execution Rules

- Follow the plan. Do not silently redesign it.
- Preserve the plan's contract and invariants.
- Prefer the plan's serial coordination spine for shared-contract work.
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
3. Read `skills/create-pr/SKILL.md` so the PR description uses the project's required format.
4. Inspect the current git state.
5. If currently on `main` or `master`, create a feature branch named from the plan descriptor.
6. If the plan includes UI work and before screenshots are missing, capture them before editing.
7. Implement the plan in the required order.
8. Run the plan's verification steps.
9. If verification fails, iterate until:
   - all required checks pass, or
   - you are blocked by an external dependency, missing credential, or pre-existing unrelated failure
10. Review the final diff to ensure the implemented changes match the plan.
11. Stage only the relevant files.
12. Create the commit.
13. Draft the PR title and body by applying `create-pr`:
   - copy `Overview`, `Happy Flow`, `Data Flow`, and `Manual Verification` from the plan when required by that skill
   - fill in `Problem / motivation`, `Solution`, and `Changes` from the actual implementation
14. Push the branch.
15. Open the PR.
16. Return:
   - PR URL
   - branch name
   - verification summary
   - any known follow-ups or residual risks

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

Use the repository's existing PR-writing workflow from `skills/create-pr/SKILL.md`.

Do not invent a new PR structure if that file is available.

If the plan has a matching asset folder in `docs/plans/...`, include screenshot paths or references exactly as required by `create-pr`.

## Stop Conditions

Stop and ask the user if any of the following occurs:

- Multiple plausible plan files exist.
- The plan is missing exact verification steps.
- Required local services or credentials are unavailable.
- The git worktree contains conflicting unrelated edits in files the plan requires changing.
- The PR cannot be opened because authentication, remote permissions, or branch protection prevent it.
- The `create-pr` skill is missing or clearly incompatible with the current repo workflow.

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

