---
name: write-pr-description
description: >-
  Writes type-specific PR descriptions for experiments, features, bug fixes, or
  a default catch-all using the matching guide, template, and examples under
  types/. Use when the user asks to write a PR description, draft
  experiment/feature/bug/default PR text, or refine a pull request body by PR
  kind.
disable-model-invocation: true
metadata:
  owner: mark
  scope: project
  category: planning
---

# Write PR Description

Draft a PR description. This skill is the single source of truth for PR bodies—read the matching type pack and follow it. Do not invent a hybrid outline.

## Workflow

1. **Classify** the PR as experiment, feature, or bug when clear. If none fit, use **default**. If unclear between two specific kinds, ask once.
2. **Read** that type's `guide.md` (required).
3. **Read** `template.md` when present (scaffold).
4. **Skim** 1–2 examples only if the shape or tone is unclear.
5. **Draft** from the diff / plan / experiment outputs. Omit empty or N/A sections.
6. **Return** the description as markdown ready to paste into the PR.

## Shared rules

- Summary and Purpose may be a bit fuller (for default: Problem / Purpose); keep every other section terse.
- Terse, professional, present tense. Short sentences. No filler. Minimal bolding. Executive-style McKinsey-style direct communication.
- Describe behavior and outcomes, not a file changelog or stale implementation detail.
- Audience: engineers (or researchers for experiments) who know the project broadly but not this change.

## Route by type

Resolve paths relative to this `SKILL.md`.

| Type | When | Guide | Template | Examples |
|------|------|-------|----------|----------|
| Experiment | Ablations, comparisons, evals, research trials | [types/experiments/guide.md](types/experiments/guide.md) | [types/experiments/template.md](types/experiments/template.md) | [types/experiments/examples/](types/experiments/examples/) |
| Feature | New capability or behavior | [types/feature/guide.md](types/feature/guide.md) | [types/feature/template.md](types/feature/template.md) | [types/feature/examples/](types/feature/examples/) |
| Bug | Defect fix; broken → corrected behavior | [types/bugs/guide.md](types/bugs/guide.md) | — | [types/bugs/examples/](types/bugs/examples/) |
| Default | Catch-all when no other type fits (refactors, chores, infra, docs, deps, …) | [types/default/guide.md](types/default/guide.md) | — | — |

Type index: [types/README.md](types/README.md)
