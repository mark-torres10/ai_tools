# Implement from Spec — Final Checklist

Read this file in Phase 6 before declaring the slice done. The slice is invalid until every applicable box is checked.

## Always required

- [ ] Design/spec/plan input was identified (path or conversation paste).
- [ ] Phase 1–5 reference files were read for phases executed.
- [ ] Main caller is named and wired end-to-end for this slice.
- [ ] Scaffold landed before contracts. When tests belong, test design landed after contracts and before the units of work.
- [ ] Each step was a separate Git commit (scaffold, contracts, test design when tests belong, and each unit of work).
- [ ] Phase 3 contracts were approved (or user explicitly waived with full auto / unattended).
- [ ] When tests belong, the designed tests existed before implementation and failed for the right reasons.
- [ ] When tests belong, those tests are green.
- [ ] When tests do not belong, you added no test file, and the task summary says why.
- [ ] Units of work were implemented in dependency order of the caller path, one at a time.
- [ ] You asked what you can remove from the diff, and you deleted the leftover code.
- [ ] Out-of-scope and sibling plan packets were not expanded into.
- [ ] The order matches [examples/pipeline-memory-repo.md](examples/pipeline-memory-repo.md). Skip the test-design step when tests do not belong.

## If working from a plan with packets

- [ ] Exactly one packet / slice was implemented.
- [ ] Contracts agreed upon in the plan were honored.

## Test seams

- [ ] Tests prefer public APIs / fixtures; any private-field seeding is documented as a demo exception.

## Deliverable rule

If any unchecked item applies, fix and re-run Phase 6. Do not declare a partial slice done.
