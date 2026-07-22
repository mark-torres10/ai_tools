---
name: create-pr
description: >-
  Drafts or refines PR descriptions for human reviewers: always-on skim core
  (Problem, Solution, Manual Verification), then optional Details when depth
  gates fire (multi-step, data, backend, experimental, UI). Use when creating
  a PR, writing a PR description, or refining a pull request.
disable-model-invocation: true
metadata:
  owner: mark
  scope: project
  category: planning
---

# Create PR

Draft PR descriptions for human reviewers. Skim first; add depth only when a gate fires.

**Audience:** mostly humans (~30s skim at the top).  
**Shape:** always-on Layer 0; optional Layer 1 under `## Details`.  
**Do not** paste plan sections wholesale. Condense. No empty N/A sections.

## When to Use

- User asks to create a PR, write a PR description, or draft a pull request.
- User wants help refining an existing PR description.
- User asks how to structure a PR for this project.

## Writing rules

- Terse, professional, present tense. Short sentences. No filler. Err on the side of being an executive summary, presentable to engineering audiences who are short on time and context.
- Provide sufficient context in the writeup that a human engineer without knowledge of this workstream can pick up the PR.
- Avoid run-on sentences. Avoid excessive bolding (prefer plain headings and lists).
- Simplify. Prefer fewer sections over a complete template.
- When a planning file exists: mine it for facts; rewrite into Layer 0 / Details. Do not copy Overview, Happy Flow, or Data Flow verbatim.

## PR title

Verb + what. Specific. Under ~60 chars when possible.

| Verb | Use |
|------|-----|
| Add | New feature or capability |
| Update | Change to existing behavior (including config/fixes) |
| Disable / Enable | Toggle behavior |
| Migrate | Refactor or move to a new pattern |
| Connect | Wire UI to backend, or integrate systems |
| Improve | Better error handling, UX, or implementation |
| Fix | Bug fix |

Examples: `Add OAuth with Supabase`, `Update release pipeline: migrations then smoke`, `Fix event time shown in UTC instead of local`.

## Workflow (mandatory)

Complete phases in order. Pass each gate before continuing. Read linked references only when that phase needs them.

| Phase | Read | Gate |
|-------|------|------|
| 0 — Context | — | Diff + plan understood; project-type signals noted |
| 1 — Layer 0 | (this file) | Title + Problem + Solution + Manual Verification drafted |
| 2 — Depth gates | Matching `references/*.md` only | Details added only if a gate fired; otherwise stop |
| 3 — Done | [checklist.md](checklist.md) | Checklist passes |

### Phase 0 — Gather context

Collect: changed files, planning file (if any), related docs. Record which signals apply (multiple may apply):

- Multi-step path (CI/CD/release, deploy, multi-stage job chain, etc.)
- Data (pipelines, ETL, warehouse, dataset movement)
- Backend (API/service/worker request or I/O path through the change)
- Experimental (primarily under `experiments/` or repo experiment root)
- UI (`ui/` or equivalent frontend)
- Large layout refactor / non-trivial file-level Changes (optional)

**Gate:** Signals recorded (yes/no per type; for path changes, existing vs new).

### Phase 1 — Layer 0 (always)

Draft only:

#### Problem

Why this change. For bugs or deploy failures, include the actual error when available. A few short sentences.

#### Solution

One or two sentences on what was done.

#### Manual Verification

Exact commands or steps and expected outcomes. Checkboxes OK.

For deploy-related PRs, add live URLs when available (e.g. health → expected JSON).

**Gate:** A reviewer can skim Problem → Solution → Manual Verification in ~30s and know what changed and how to check it.

### Phase 2 — Depth gates (optional Layer 1)

Evaluate gates. **If none fire, do not add `## Details`.** Do not invent filler sections. Multiple gates may fire; merge into one `## Details` with clear subheadings.

| Gate | When | Read | Add under `## Details` |
|------|------|------|-------------------------|
| Multi-step path | Diff changes a multi-step path | [references/layer-1-details.md](references/layer-1-details.md) | End-to-end steps; before/after mermaid |
| Data | Data movement / pipeline / ETL / warehouse path | [references/data-flow.md](references/data-flow.md) | Data flow narrative + how data moves (mermaid) |
| Backend | Request or I/O path through a backend change | [references/backend-flow.md](references/backend-flow.md) | Request/I/O flow narrative + mermaid |
| Experimental | Primarily under `experiments/` | [references/experimental.md](references/experimental.md) | Executive results summary + results table |
| UI screenshots | UI/frontend change | [references/ui-screenshots.md](references/ui-screenshots.md) | State (Before) / State (After) or prompt user |
| Target structure | Large refactor of layout | [references/layer-1-details.md](references/layer-1-details.md) | Optional tree block |
| File-level Changes | Helps review of a non-trivial diff | [references/layer-1-details.md](references/layer-1-details.md) | Optional short bullet list |

**Overlap:** If multi-step and backend/data all apply, prefer one coherent diagram set — do not duplicate the same flow three times. Use the most specific heading (Data flow vs Request flow vs End-to-end).

**Gate:** Either no Details section, or Details contains only gated content (no Happy Flow / Overview dumps).

### Phase 3 — Checklist

Read [checklist.md](checklist.md). Fix gaps before delivering the PR body.

## Output shape

**Simple PR (no gates):**

```markdown
## Problem
...

## Solution
...

## Manual Verification
...
```

**PR with depth (gates fired):**

```markdown
## Problem
...

## Solution
...

## Manual Verification
...

---

## Details

### End-to-end / Data flow / Request flow
(as gated)

### Before
(mermaid — existing path only)

### After
(mermaid — proposed path)

### Results summary
(experimental only)

### Results
(experimental table only)

### Changes
(optional)

### State (Before) / State (After)
(UI only)
```

## Constraints

- Always produce Layer 0. Never skip Problem, Solution, or Manual Verification.
- Never add empty sections or "N/A" placeholders.
- Never require Overview, Happy Flow, or Data Flow as always-on PR headings (data-flow *content* belongs under Details when the data gate fires).
- Path-changing gates (multi-step, data, backend) require narrative + mermaid(s) per their reference files; existing paths need Before and After.
- Experimental PRs under `experiments/` require the results summary + table per [references/experimental.md](references/experimental.md); do not invent metrics.
- If UI screenshots are required and missing, prompt the user; do not invent image paths.

## Additional resources

- Multi-step: [references/layer-1-details.md](references/layer-1-details.md)
- Data: [references/data-flow.md](references/data-flow.md)
- Backend: [references/backend-flow.md](references/backend-flow.md)
- Experimental: [references/experimental.md](references/experimental.md)
- UI screenshots: [references/ui-screenshots.md](references/ui-screenshots.md)
- Final checklist: [checklist.md](checklist.md)
- Canonical rules twin: `agents/task_instructions/rules/HOW_TO_WRITE_PR.md`
