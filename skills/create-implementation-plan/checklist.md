# Implementation Plan Package — Final Checklist (Approach A)

Read this in Phase 4 before delivering the plan package. **Invalid until every applicable box is checked.**

Completeness = **Layer 0 + fired gates' leaves**. Do **not** require all historical sections inlined in `plan.md`.

## Always required (Layer 0 + verification leaf)

- [ ] ai_tools root and `PLANNING_RULES.md` were resolved (or GitHub fallback used).
- [ ] Plan asset dir exists: `docs/plans/<YYYY-MM-DD>_<descriptor>_<6-digit hash>/`
- [ ] `plan.md` is a router/exec summary only (Remember, Overview, Happy Flow, approach, verification pointer).
- [ ] `plan.md` stays skim-friendly (soft guidance ~150–250 lines; no inlined packet walls).
- [ ] Happy Flow is enumerated with file refs **in** `plan.md`.
- [ ] `verification.md` exists with specific Manual Verification + Final Verification (commands + expected outcomes).
- [ ] `plan.md` has a short verification pointer linking to `verification.md` (no top-checks list).
- [ ] No empty sections, "N/A" placeholders, or stub files for unfired gates.
- [ ] Specificity lives in leaves; `plan.md` indexes rather than dumping.

## Parallel / multi-agent (if gate fired)

- [ ] Read `references/parallel-delegation.md`.
- [ ] `contracts.md` exists with real freeze content.
- [ ] `spine.md` exists (short, ordered).
- [ ] Every packet is `packets/T<n>_<slug>.md` with **all 14 fields**.
- [ ] Every packet passes the delegation validity test.
- [ ] `plan.md` has short contracts/spine pointers (no symbol lists or spine task lines), plus a **Tasks (in order)** table (ID | Task description | File)—not full packet bodies.
- [ ] `plan.md` has **no** separate Integration order section (order lives in the Tasks table).
- [ ] No shared file ownership across parallel packets without serial coordination.
- [ ] Plan maximizes safely delegable parallel work.

## Heavy contracts only (if gate fired without parallel split)

- [ ] Read `references/parallel-delegation.md` (freeze section).
- [ ] `contracts.md` exists; `plan.md` has a short pointer to it (no frozen-symbol list).
- [ ] No empty `spine.md` / `packets/` created "just in case".

## Ops / runbooks (if gate fired)

- [ ] Read `references/runbooks-audit.md`.
- [ ] `runbooks.md` exists with inventory + classifications (and proposals if needed).
- [ ] `plan.md` has a short runbooks index + link (not the full audit dump).
- [ ] No invented runbook paths outside inventory + proposals.

## Ops / runbooks (if gate did **not** fire)

- [ ] No `runbooks.md` file.
- [ ] No Update Runbooks / N/A section in `plan.md`.

## Non-trivial alternatives (if gate fired)

- [ ] `alternatives.md` exists and is short.
- [ ] `plan.md` chosen approach is 1–3 sentences and links to `alternatives.md`.

## Non-trivial alternatives (if gate did **not** fire)

- [ ] No `alternatives.md` stub.

## UI (if gate fired)

- [ ] Read `references/ui-screenshots.md`.
- [ ] First to-do is before screenshots; last to-do is after screenshots.
- [ ] No README or instructions ask the user to take screenshots.
- [ ] Paths reserved: `images/before/`, `images/after/` under the plan asset dir.
- [ ] (At execution time) Screenshots land in those dirs.

## UI (if gate did **not** fire)

- [ ] No obligatory empty `images/` tree required for delivery of the plan text package.

## Anti-patterns check

- [ ] No anti-patterns from `references/parallel-delegation.md` or `references/runbooks-audit.md`.
- [ ] Did not treat "all 11 sections in one file" as the completeness bar.

## Deliverable rule

If any applicable box is unchecked, fix the package and re-run Phase 4. Do not deliver a monolithic `plan.md` dump or padded N/A artifacts.
