# Parallel Delegation Reference (Approach A)

Apply when the **parallel / multi-agent** gate or **heavy contracts** gate fires (Phase 2).

**Artifact placement (mandatory):**

| Content | File |
|---------|------|
| Full Interface / Contract Freeze | `contracts.md` at plan asset root |
| Serial Coordination Spine | `spine.md` at plan asset root |
| Each parallel task packet (14 fields) | `packets/T<n>_<slug>.md` |
| Tasks (in order) table | **Index in `plan.md` only** (ID \| Task description \| File) |

`plan.md` must **not** contain full packet bodies, frozen-symbol lists, or spine task lines. It points at `contracts.md` / `spine.md` and lists tasks in execution order (ID → one-sentence description → detail file link).

## Parallel-first delegation (mandatory when gate fires)

Plans must maximize safely delegable parallel execution:

- Minimize the serial coordination path (`spine.md`).
- Maximize safe parallel tasks (`packets/`).
- Do not delegate any task a weak coding agent could misread.
- If a task cannot be specified unambiguously, keep it on the serial spine.

Prefer decomposition by stable ownership:

- schema or contract work
- backend handler or service work
- frontend rendering work
- tests or fixtures
- docs or migration follow-up
- runbook updates under `docs/runbooks/` (one file per parallel task when possible)

Do not share ownership of the same file across parallel packets unless that file stays on the serial spine.

## Heavy contracts only

If shared schemas/APIs must freeze but work does **not** safely split:

- Write `contracts.md` only.
- Skip `spine.md` and `packets/` unless the parallel gate also fires.
- `plan.md` includes a short pointer to `contracts.md` (no frozen-symbol list).

## Parallel task packet format (mandatory — 14 fields)

Each `packets/T<n>_<slug>.md` must include **all** of:

1. **Task ID**
2. **One-sentence objective**
3. **Why this task is parallelizable**
4. **Exact files to inspect**
5. **Exact files allowed to change**
6. **Exact files forbidden to change**
7. **Preconditions**
8. **Dependency tasks**
9. **Required contracts and invariants** (point at `contracts.md` symbols by name)
10. **Step-by-step implementation instructions**
11. **Exact verification commands**
12. **Expected outputs from verification**
13. **Done-when checklist**
14. **Coordinator review checklist**

If any field is missing, the packet is unsafe—rewrite or move the work to `spine.md`.

### Suggested packet file skeleton

```markdown
# T1 — <slug>

## Task ID
T1

## One-sentence objective
…

## Why this task is parallelizable
…

## Exact files to inspect
- `path/to/file.py`

## Exact files allowed to change
- `path/to/file.py`

## Exact files forbidden to change
- `path/to/other.py`

## Preconditions
- …

## Dependency tasks
- None | T0, …

## Required contracts and invariants
- See `contracts.md`: `SymbolName`, …

## Step-by-step implementation instructions
1. …

## Exact verification commands
```bash
uv run pytest path/to/test.py -q
```

## Expected outputs from verification
```text
…
```

## Done-when checklist
- [ ] …

## Coordinator review checklist
- [ ] …
```

## `spine.md` (short, ordered)

List only serial coordination work: freeze, shared-file edits, integration glue. Keep each spine item shorter than a full packet; if a spine item grows to 14-field rigor, consider whether it should be a packet after a prior freeze.

## `contracts.md`

Exact shared interfaces, schemas, types, endpoints, props, DB contracts, or invariants that must be fixed before parallel work. Name symbols agents can grep. Prefer examples or signature sketches over prose.

## Delegation validity test (mandatory)

Before finalizing, apply to every packet:

1. Could a weak coding agent execute this without asking a question?
2. Could another agent run a sibling packet in parallel without file ownership conflict?
3. Could the coordinator verify this packet in isolation?
4. Would two agents likely make the same change from this description?

If any answer is "no", rewrite the packet or move it to `spine.md`.

## `plan.md` index requirements (when parallel gate fires)

In Layer 0 only:

- Short **contracts** pointer → `[contracts.md](contracts.md)` (no symbol lists)
- Short **spine** pointer → `[spine.md](spine.md)` (no task lines)
- **Tasks (in order)** table: ID | Task description | File — covers spine steps and packets in execution/integration order (no separate Integration order section)

## Anti-patterns

- Inlining full packets into `plan.md`
- Vague task descriptions; missing file paths; incomplete snippets
- Implementation before tests in packet steps
- No verification steps; assuming context
- Shared file ownership across parallel packets
- "As needed", "etc.", or "follow the existing pattern" without naming the reference file/symbol
- Verification that depends on unfinished sibling packets
- Empty `contracts.md` / `spine.md` / packet stubs

## Phase gate (parallel / contracts)

Do not proceed to Phase 3 assembly until:

- [ ] If parallel gate: `contracts.md`, `spine.md`, and every `packets/T*.md` exist
- [ ] If heavy-contracts only: `contracts.md` exists
- [ ] Every packet includes all 14 fields and passes the validity test
- [ ] Runbook parallel packets (if any) have exclusive `docs/runbooks/` ownership and appear after contract freeze in the Tasks (in order) table
- [ ] Nothing required above was stuffed into `plan.md` as a full dump
