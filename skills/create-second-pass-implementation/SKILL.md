---
name: create-second-pass-implementation
description: >-
  After a first working implementation, harvest what the pass learned, rebuild
  a cleaner version from scratch, and keep it only if the same checks still
  hold. Use when the user runs /create-second-pass-implementation on a plan,
  design doc, diff, PR, or working code. Sourced from
  https://x.com/YoussefHosni951/status/2116250056747782343
disable-model-invocation: true
metadata:
  owner: mark
  scope: global
  category: implementation
---

# Create second-pass implementation

The first working version learns the problem. Rebuild a cleaner version from that learning, then keep it only if the same checks still hold.

Read [references/second-pass-trick-youssef-hosni.md](references/second-pass-trick-youssef-hosni.md) before you rewrite. Do not rebuild from memory of this file alone.

Source: Youssef Hosni, [The second-pass trick](https://x.com/YoussefHosni951/status/2116250056747782343) (30 October 2026).

## When to use

- The user runs `/create-second-pass-implementation`.
- A first pass already works: a plan, a design doc, a PR, a branch, a diff, or working code.
- The user wants a cleaner implementation, not another round of fixes on the same structure.

## Do not use

- Nothing works yet. Finish a first pass first.
- The user wants a review and no rebuild. Use `review-for-simplicity`.
- The user wants small bugfixes on the current structure.

## Inputs

Resolve one first pass before changing it:

1. A path or PR the user named.
2. The branch, diff, or doc already in the thread.
3. The working tree, if they said the current code is the first pass.

If two targets fit, ask which one and stop.

## Workflow

```markdown
Second pass:
- [ ] 1. Harvest learnings
- [ ] 2. Audit with the rubric
- [ ] 3. Split keep vs regenerate
- [ ] 4. Write v2 from that split
- [ ] 5. Compare, then keep v2 only if it holds
```

Leave v1 reachable until step 5 (the existing commit, branch, or a copy of the doc).

### 1. Harvest

Write this down before you delete or rewrite anything:

- The real shape of the problem, in a few sentences.
- Constraints and edge cases the first pass discovered.
- Dead ends: approaches tried and dropped, and why.
- Parts that exist only because the path there was uncertain.

If a learning is a requirement, it goes on the keep list. If it only explains a messy structure, it is residue.

### 2. Audit

Walk the rubric in order. For each item, mark `clear` or `residue` and name the file, symbol, or section. Code uses items 1-7. Docs and plans use items 1-8.

1. **Abstractions and indirection.** Residue: a base, interface, wrapper, or adapter with one implementation, or a layer that only forwards.
2. **Temporary or versioned layers.** Residue: `temp_`, `_v2`, `adapter`, `legacy`, `new_`, or a helper added to get unstuck.
3. **Duplicated logic or validation.** Residue: the same check or transform in more than one place.
4. **Workarounds.** Residue: a branch for a problem the harvest now states directly.
5. **Dead code and unused options.** Residue: a flag, parameter, or branch nothing calls.
6. **Flow vs. the problem.** Residue: steps, states, or files the harvested shape does not need.
7. **Names from the journey.** Residue: a name that records a discarded approach.
8. **Docs and plans.** Residue: a section that hedges, repeats a point already made, or plans a path the first pass ruled out.

### 3. Keep vs regenerate

| Carries over unchanged | Regenerated from scratch |
|------------------------|--------------------------|
| Behavioral contract and requirements | Internal structure |
| Tests and acceptance criteria | Abstractions |
| Public interfaces, unless the audit shows the interface is residue | Module layout |
| Discovered edge cases | Control flow |
| Domain knowledge | Temporary scaffolding |
| Verified data and facts | Doc structure and prose |

Gray areas:

- **Public interface.** Keep it. Change it only when a rubric item shows the interface itself is residue (a v2 surface, an adapter, a duplicated entry). Name that item, and update callers in the same rebuild.
- **Tests that lock in the journey.** Keep assertions about behavior. You may change a test that only exists to pin a temp helper, a file layout, or a private name, and only if behavior stays the same.
- **Shared modules.** Keep behavior other callers rely on. Internals may be rebuilt when those callers still pass.
- **Approved docs.** Keep confirmed decisions, requirements, and verified facts. Rebuild the explanation and the outline.

### 4. Write v2

Write v2 from the harvest and the keep list. Build the simpler structure the problem turned out to have.

Do not patch v1. A cleaner implementation, not just more fixes.

Do not add a test-first loop. The checks in step 5 are the checks v1 already has.

### 5. Compare

- Run the same tests or acceptance checks on v2. For a doc or plan, re-check the same acceptance criteria and the claims the doc makes.
- Read the diff: size, layers removed, behavior still the same.
- Score v1 and v2 on the rubric.

Keep v2 only when all of these hold:

- The same checks pass.
- The keep list still holds, including discovered edge cases.
- v2 has fewer residue items than v1.

Otherwise keep v1. Cherry-pick a single cut only when that cut, applied to v1, still passes the same checks.

End with this summary and nothing longer:

```markdown
## Second pass
- Kept: v1 | v2 | cherry-pick
- Checks: <what ran, pass or fail>
- Rubric: <v1 residue vs v2 residue, one line>
- Diff: <layers removed, size, behavior>
- Harvest kept: <requirements and edge cases still present>
- Left on v1: <what you did not take>
```

## Quick mode

If the user says "quick", harvest in a few bullets, skip the written per-item rubric, and rebuild with this sentence, then still run Compare:

> Knowing everything you know now, scrap this and implement the elegant solution.

If the user asks for the prompt and not a rebuild, return that sentence and stop.

## Rules

- Ask for a cleaner implementation, not just more fixes.
- A second pass is not automatically better. v1 stays until Compare says otherwise.
- Do not weaken or delete a behavioral check to make v2 pass.
- Do not invent requirements the first pass did not establish.
