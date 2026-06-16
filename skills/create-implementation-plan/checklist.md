# Implementation Plan — Final Checklist

Read this file in Phase 5 before delivering the plan. **The plan is invalid until every applicable box is checked.**

## Always required

- [ ] ai_tools root and `PLANNING_RULES.md` were resolved (or inline fallback from `plan-structure.md` was used).
- [ ] Remember block is at the top of the plan.
- [ ] All 11 required sections from `references/plan-structure.md` are present.
- [ ] Manual Verification has exact commands and expected outcomes.
- [ ] Update Runbooks section is complete (Phase 2 gate passed).
- [ ] Parallel delegation is complete (Phase 3 gate passed).
- [ ] No anti-patterns from `references/parallel-delegation.md` or `references/runbooks-audit.md`.
- [ ] Plan maximizes safely delegable parallel work where possible.
- [ ] Every delegated task has all packet fields and passes the validity test.

## UI changes (if any `ui/` or frontend work)

- [ ] Phase 4: read `references/ui-screenshots.md`.
- [ ] First to-do is before screenshots; last to-do is after screenshots.
- [ ] No README or instructions ask the user to take screenshots.
- [ ] (At execution time) Screenshots land in `docs/plans/.../images/before/` and `.../after/`.

## Runbooks

- [ ] `docs/runbooks/` inventoried in the target workspace (or absence noted).
- [ ] Every discovered runbook classified or new runbooks proposed with template frontmatter.
- [ ] No invented runbook paths outside inventory + proposals.

## Deliverable rule

If any unchecked item applies to this plan, fix the plan and re-run Phase 5. Do not deliver a partial plan.
