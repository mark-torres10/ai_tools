# Create PR — Final Checklist

Read this in Phase 3 before delivering the PR title and body. **Invalid until every applicable box is checked.**

## Always required (Layer 0)

- [ ] Title is verb + what, specific, reasonably short
- [ ] Problem explains why (error text included when relevant)
- [ ] Solution is one or two sentences
- [ ] Manual Verification has concrete steps/commands and expected outcomes
- [ ] Prose is terse, present tense; no run-ons; minimal bold; no filler
- [ ] Plan content (if any) was condensed, not pasted
- [ ] No empty sections or "N/A" placeholders
- [ ] No Overview / Happy Flow as required PR headings

## Multi-step path (if gate fired)

- [ ] Read `references/layer-1-details.md`
- [ ] `## Details` includes end-to-end steps
- [ ] Existing flow changed → Before and After mermaid both present
- [ ] New multi-step path → After mermaid present
- [ ] Diagrams match the real jobs/steps in the diff

## Data (if gate fired)

- [ ] Read `references/data-flow.md`
- [ ] Data flow narrative (source → transform → sink)
- [ ] After (and Before if existing path changed) mermaid present
- [ ] Nodes match real stores/jobs/tables in the diff

## Backend (if gate fired)

- [ ] Read `references/backend-flow.md`
- [ ] Request / I/O flow narrative for the primary path
- [ ] After (and Before if existing path changed) mermaid present
- [ ] Names match real endpoints/modules in the diff

## Experimental (if gate fired)

- [ ] Diff is primarily under `experiments/` (or repo experiment root)
- [ ] Read `references/experimental.md`
- [ ] Terse executive results summary present
- [ ] Results table uses Dimension / Finding / Evidence / Implication
- [ ] No invented metrics; missing results → user prompted

## UI (if gate fired)

- [ ] Read `references/ui-screenshots.md`
- [ ] Screenshots linked/referenced, or user prompted if missing

## Simple PRs (no gates)

- [ ] No `## Details` section
- [ ] No mermaid, results tables, or invented depth

## Deliverable rule

If any applicable box is unchecked, fix the body and re-check. Do not deliver a padded template.
