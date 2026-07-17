# Implement from Spec — Final Checklist

Read this file in Phase 5 before declaring the slice done. **The slice is invalid until every applicable box is checked.**

## Always required

- [ ] Design/spec/plan input was identified (path or conversation paste).
- [ ] Phase 0–4 reference files were read for phases executed.
- [ ] Main caller is named and wired end-to-end for this slice.
- [ ] Scaffold landed before contracts; contracts before test design; tests before fleshing UoWs.
- [ ] Phase 2 contracts were approved (or user explicitly waived with full auto / unattended).
- [ ] Designed tests exist (pseudocode then real); they failed for the right reasons before implementation.
- [ ] Units of work were fleshed in **dependency order of the caller path**, one at a time.
- [ ] All designed tests for this slice are green.
- [ ] Out-of-scope and sibling plan packets were not expanded into.
- [ ] Pattern matches [examples/pipeline-memory-repo.md](examples/pipeline-memory-repo.md) (caller → scaffold → contracts → tests → incremental UoWs).

## If working from a plan with packets

- [ ] Exactly one packet / slice was implemented.
- [ ] Interface or Contract Freeze from the plan was honored.

## Test seams

- [ ] Tests prefer public APIs / fixtures; any private-field seeding is documented as a demo exception.

## Deliverable rule

If any unchecked item applies, fix and re-run Phase 5. Do not declare a partial slice done.
