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

This skill ships one plan as one PR. For the actual coding, use the `/implement-from-spec` skill. That skill commits as it goes. This skill still owns verification, `write-docstring`, `write-pr-description`, opening the PR, `write-changelog`, and post-PR review.

Do not use this skill unless the user explicitly asked for the full implementation + PR workflow and explicitly cites it.

## When to Use

- The user provides a plan and asks to implement it to completion as one PR.
- The user asks to execute a plan created earlier in `docs/plans/...`.
- The user wants the final deliverable to be an open PR and a returned PR URL.
- The user expects `write-pr-description` to be used for the PR title/body.

If the plan has several `steps/*.md`, they all ship in this PR, in plan order.

## Do Not Use

- Do not use for planning only.
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
- For implementation, use the `/implement-from-spec` skill. Do not implement in a side pass that skips its phases.
- Review CODING_RULES.md and UNIT_TESTING_STANDARDS.md before any implementation. You must be in compliance with these standards.
- Preserve the plan's agreed contracts and invariants.
- Only parallelize tasks that are clearly independent and safe. Do not run `/implement-from-spec` in parallel for different plan steps.
- Never revert unrelated user changes.
- If unexpected unrelated changes appear in files you need to edit, stop and ask the user how to proceed.
- Do not commit secrets or env files.
- Do not skip verification.
- Do not open a PR until verification is complete or the remaining failures are clearly identified as pre-existing and unrelated.

### Notes when using `/implement-from-spec`

- This run is unattended. Do not stop for the Phase 3 approval in `/implement-from-spec`. Continue as if the user already said full auto.
- Phase 1 confirms the plan's caller, file tree, contracts, and out-of-scope. It does not reopen design.
- If the plan has multiple steps, run `/implement-from-spec` once per step, in plan order. After a step's Phase 6 / checklist passes, go to the next step. Do not open a PR until every required step is done.
- Read `CODING_RULES.md` and `UNIT_TESTING_STANDARDS.md` as usual. They constrain the code. They do not replace `/implement-from-spec`'s phase order.
- `/implement-from-spec` commits once per step (each phase that changes the repo, and each unit of work in its Phase 5 loop). Do not squash those commits into one commit. This skill opens the PR after implementation.

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
5. Inspect the current git state. If currently on `main` or `master`, create a feature branch named from the plan descriptor.
6. If the plan includes UI work and before screenshots are missing, capture them before editing.
7. For implementation, use the `/implement-from-spec` skill (notes above). One run per step, in plan order. Do not skip its phase reference reads. Do not treat a step as done until that run's Phase 6 / checklist passes.
8. Run the plan's verification steps.
9. If verification fails, iterate until:
   - all required checks pass, or
   - you are blocked by an external dependency, missing credential, or pre-existing unrelated failure
10. Review the final diff to ensure the implemented changes match the plan. Ensure that your implementation complies with CODING_RULES.md and UNIT_TESTING_STANDARDS.md. For docstrings, apply the `write-docstring` skill. If that leaves uncommitted changes, commit them separately (do not squash `/implement-from-spec` commits).
11. Draft the PR title and body by applying `write-pr-description`.
12. Push the branch.
13. Open the PR.
14. Update the CHANGELOG.md, using the `write-changelog` skill. If the CHANGELOG.md file doesn't exist, create it. Then commit to the PR and push.
15. Spawn three review subagents on the PR: `comprehensive-code-review`, `plain-writing`, `review-for-simplicity`. Not a merge gate. Fix clear correctness bugs (broken contract, failing tests) and address other feedback and push.
16. Return PR URL, executive summary of what was built, verification summary, review notes worth reading, and any known follow-ups.

## Required Verification Standard

The change is not complete until all of the following are true:

- The code implementing the plan exists.
- Required tests, linters, builds, or manual checks have been run.
- The actual result matches the plan's acceptance criteria.
- UI before/after screenshots exist when required by the plan and have been added to the PR.
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
- The git worktree contains conflicting unrelated edits in the files the plan requires changing.
- A step's `/implement-from-spec` Phase 6 checklist fails and you cannot get it green without going out of scope.
- The PR cannot be opened because authentication, remote permissions, or branch protection prevent it.

## Final Response Format

Return a concise result with:

- PR URL
- branch name
- commit summary
- verification performed
- review notes worth reading
- any blockers, caveats, or follow-up work

If blocked before PR creation, return:

- what was completed
- the exact blocking condition
- the next action required from the user
