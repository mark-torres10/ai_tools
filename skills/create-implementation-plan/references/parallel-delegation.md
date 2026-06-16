# Parallel Delegation Reference

Apply in Phase 3 when splitting work into serial vs parallel tasks.

## Parallel-first delegation (mandatory)

Plans must be optimized for maximum safely delegable parallel execution.

This is a hard requirement:

- Minimize the serial coordination path.
- Maximize the amount of work split into safe parallel tasks.
- Do not delegate any task that could plausibly be misunderstood by a small, weak, distilled coding agent.
- If a task cannot be specified unambiguously enough to survive delegation without clarifying questions, it must remain in the serial coordination spine.

Prefer decomposition by stable ownership boundaries such as:

- schema or contract work
- backend handler or service work
- frontend rendering work
- tests or fixtures
- docs or migration follow-up
- runbook updates under `docs/runbooks/` (one file per parallel task when possible)

Do not split work across parallel tasks if they would share ownership of the same file unless the plan explicitly keeps that file in the serial coordinator track.

## Parallel task packet format (mandatory)

Each delegated task must include all of the following:

- **Task ID**
- **One-sentence objective**
- **Why this task is parallelizable**
- **Exact files to inspect**
- **Exact files allowed to change**
- **Exact files forbidden to change**
- **Preconditions**
- **Dependency tasks**
- **Required contracts and invariants**
- **Step-by-step implementation instructions**
- **Exact verification commands**
- **Expected outputs from verification**
- **Done-when checklist**
- **Coordinator review checklist**

If any one of these fields is missing, the task is not safe to delegate and must not appear under Parallel Task Packets.

## Delegation validity test (mandatory)

Before finalizing the plan, apply this test to every delegated task:

1. Could a weak coding agent execute this task without asking a question?
2. Could another agent execute a sibling task in parallel without file ownership conflict?
3. Could the coordinator verify this task in isolation?
4. Would two different agents likely make the same change from this description?

If the answer to any question is "no", rewrite the task or move it out of parallel execution.

## Anti-patterns to avoid

- Vague task descriptions
- Missing file paths
- Incomplete code snippets
- Implementation before tests
- No verification steps
- Assuming context
- Delegated tasks with ambiguous scope or ownership
- Shared ownership of the same file across parallel tasks
- "As needed", "etc.", or "follow the existing pattern" without naming the exact reference file or symbol
- Verification steps that rely on unfinished parallel work
- Any delegated step that requires hidden intent or unstated judgment

## Phase 3 gate

Do not proceed to Phase 4 until:

- [ ] Serial Coordination Spine, Interface or Contract Freeze, Parallel Task Packets, Integration Order, and Final Verification are present.
- [ ] Every delegated task includes all packet fields.
- [ ] Every delegated task passes the validity test.
- [ ] Runbook parallel tasks (if any) have exclusive `docs/runbooks/` file ownership and land after contract freeze in Integration Order.
