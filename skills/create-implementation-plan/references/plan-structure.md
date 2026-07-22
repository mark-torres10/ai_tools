# Plan Structure Reference (Approach A)

Apply in Phase 1 (core) and Phase 3 (`plan.md` assembly). Planning produces a **package**; `plan.md` is Layer 0 only.

## Completeness model

| Always | When gate fires |
|--------|-----------------|
| `plan.md` (Layer 0) | `contracts.md` — parallel and/or heavy-contracts |
| `verification.md` (full Manual + Final Verification) | `spine.md`, `packets/*.md` — parallel / multi-agent |
| | `runbooks.md` — ops |
| | `alternatives.md` — non-trivial alternatives |
| | `images/` + screenshot todos — UI |

**Invalid:** requiring all historical "11 sections" inlined in `plan.md`.  
**Valid:** Layer 0 indexes + every fired gate's leaf exists with real content (no N/A files).

## Package layout

```text
docs/plans/<YYYY-MM-DD>_<descriptor>_<6-digit hash>/
  plan.md
  verification.md
  contracts.md            # gated
  spine.md                # gated (with parallel)
  packets/T<n>_<slug>.md  # gated
  runbooks.md             # gated
  alternatives.md         # gated
  images/before/          # gated (UI); filled at execution
  images/after/
```

Example: `docs/plans/2026-01-30_change_selector_panels_123456/`

## Remember block (top of `plan.md`)

```markdown
## Remember
- Exact file paths always
- Exact commands with expected output
- DRY, YAGNI, TDD, frequent commits
- Maximum safely delegable parallelism
- Detail lives in sibling files; plan.md is the router
- Delegated packets must be impossible to misread (see packets/)
- Operational changes: write runbooks.md from docs/runbooks/ inventory
- UI changes: agent captures before/after screenshots itself
```

## Layer 0 — what belongs in `plan.md`

Keep skim-friendly (~150–250 lines). Include only:

### 1. Remember
Short block above.

### 2. Overview
One paragraph: what and why.

### 3. Happy Flow
Enumerated end-to-end flow with **file references**. Stays in `plan.md` (not only in a leaf).

### 4. Chosen approach
1–3 sentences. If `alternatives.md` exists, link it; do not paste the full options writeup here.

### 5. Contracts pointer (omit if no `contracts.md`)
Short pointer only — no frozen-symbol lists. Example: `See details in [contracts.md](contracts.md).`

### 6. Spine pointer (omit if no `spine.md`)
Short pointer only — no ordered task lines. Example: `See details in [spine.md](spine.md).`

### 7. Tasks (in order) (omit if no packets and no spine)

Markdown table with **exactly three columns**:

| ID | Task description | File |
|----|------------------|------|
| S0 | … | [spine.md](spine.md) |
| T1 | One-sentence human-readable description | [packets/T1_slug.md](packets/T1_slug.md) |

- **ID** — spine or packet ID (`S0`, `T1`, …)
- **Task description** — one sentence, human-readable
- **File** — link/path to the packet or other detail file (`spine.md`, `packets/T*.md`, etc.)

Rows are in **execution/integration order** (serial spine steps and parallel packets interleaved as they should land). Do **not** add a separate Integration order section. Do **not** paste the 14 packet fields here.

For parallel-only waves, still list each task with clear IDs; row order = recommended execution/integration order.

### 8. Verification pointer (always)
Short pointer only — no top-checks list. Example: `See [verification.md](verification.md).`

### 9. Runbooks pointer (omit if no `runbooks.md`)
Touch / no-touch summary + link to `[runbooks.md](runbooks.md)`.

### 10. UI notes (omit if UI gate did not fire)
Brief before/after screenshot paths if useful; detail stays in `spine.md` / `verification.md`.

## Always-on leaf: `verification.md`

Write full detail here (not in `plan.md`):

```markdown
# Verification

## Manual Verification
- [ ] Exact command / step — expected outcome
- …

## Final Verification
- [ ] End-to-end integrated checks after all packets land
- …
```

Use exact commands (e.g. `uv run pytest ...`), startup steps, and UI clicks when relevant.

## Gated leaf sketches

### `contracts.md` (when freeze needed)

Full Interface / Contract Freeze: exact shared interfaces, schemas, types, endpoints, props, DB contracts, invariants. Enough that parallel agents cannot invent conflicting shapes.

### `spine.md` (when parallel gate fires)

Short ordered list of serial coordination tasks (contract freeze, integration, shared-file work). One section per spine step; keep tighter than packets—packets hold the bulk of implementation steps.

### `packets/T<n>_<slug>.md`

Full **14-field** parallel task packet. See [parallel-delegation.md](parallel-delegation.md).

### `runbooks.md`

Full audit output from [runbooks-audit.md](runbooks-audit.md). **Do not create this file** when there is no ops impact.

### `alternatives.md`

Short note: options considered, why chosen. **Only if** the tradeoff is non-trivial.

## Depth gates (evaluate in Phase 2)

| Gate | When | Create |
|------|------|--------|
| Parallel / multi-agent | Work can safely split across agents/files | `contracts.md`, `spine.md`, `packets/*.md`; Tasks (in order) table in `plan.md` |
| Heavy contracts | Shared contracts must freeze even with little parallelism | `contracts.md` |
| Ops / runbooks | Deploy, env, incident, operator procedure changes | `runbooks.md` |
| UI | `ui/` or equivalent frontend paths | Screenshot todos + `images/` dirs per [ui-screenshots.md](ui-screenshots.md) |
| Non-trivial alternatives | Real design tradeoff | `alternatives.md` |

## Specificity

- Leaves: exact paths, commands, component names, expected output.
- `plan.md`: Happy Flow narrative + thin pointers + Tasks (in order)—not vague "add auth" steps, and not full packet dumps.
- Never: empty sections, "N/A", or stub files for unfired gates.

## Phase 1 gate

Do not proceed to Phase 2 until:

- [ ] Plan asset path chosen under `docs/plans/.../`
- [ ] Remember, Overview, Happy Flow, and chosen approach drafted (for `plan.md`)
- [ ] `verification.md` drafted with specific Manual + Final Verification
- [ ] Tentative gate signals recorded (which leaves will exist)

## Phase 3 gate

Do not proceed to Phase 4 until:

- [ ] `plan.md` contains only Layer 0 sections (plus gated pointers/tables that have leaves)
- [ ] Every existing leaf is linked from `plan.md`
- [ ] No 14-field packet bodies inlined in `plan.md`
- [ ] No frozen-symbol lists, spine task lines, verification check lists, or Integration order section in `plan.md`
- [ ] Soft length: `plan.md` remains skim-friendly (~150–250 lines guidance)
- [ ] Unfired gates produced neither files nor N/A sections
