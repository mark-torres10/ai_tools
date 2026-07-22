# Layer 1 — Details (gated)

Read this only when a Phase 2 depth gate fires. Put gated content under `## Details`. Omit everything that does not apply.

## Multi-step path gate

**Fires when:** the PR changes a multi-step path — e.g. CI/CD or release workflow, deploy pipeline, multi-stage job chain, request path across services, or any ordered flow with multiple handoffs.

**Does not fire for:** single-function fixes, copy/typo, isolated config typos, pure docs, one-shot helpers with no pipeline.

### Required under Details

1. **End-to-end** — Numbered steps of the path as it works after this PR. Short clauses. No bold spam.
2. **Mermaid**
   - If the path **already existed** and this PR changes it: include **Before** and **After** diagrams.
   - If this PR **introduces** a new multi-step path: include **After** only (label it clearly; no fake Before).

### Mermaid guidance

- Prefer `flowchart LR` or `flowchart TD` for pipelines.
- Name nodes after real jobs/services/steps from the diff.
- Show failure stops when the change adds gates (e.g. smoke fail → stop).
- Keep diagrams scannable; avoid decorative subgraphs.

### Example (existing release path changed)

Under `## Details`, include end-to-end steps, then:

Before:

~~~mermaid
flowchart LR
  tag[Push v* tag] --> build[Build and push images]
  build --> stg[Deploy staging app + migrations]
  stg --> approve[Manual approve]
  approve --> prod[Deploy prod app + migrations]
~~~

After:

~~~mermaid
flowchart LR
  tag[Push v* tag] --> build[Build and push images]
  build --> stgMig[Staging migrations]
  stgMig --> stgApp[Staging app deploy]
  stgApp --> smoke[Staging smoke]
  smoke -->|pass| approve[Manual approve]
  smoke -->|fail| stop[Stop workflow]
  approve --> prodMig[Prod migrations]
  prodMig --> prodApp[Prod app deploy]
~~~

## Optional: Changes

Add a short bullet list (one line per file or logical group) when it helps review. Skip for tiny one-file fixes already clear from Solution.

Example:

- `simulation/api/dependencies/auth.py`: when `DISABLE_AUTH=1`, return mock payload instead of validating JWT
- `ui/contexts/AuthContext.tsx`: when `NEXT_PUBLIC_DISABLE_AUTH=true`, treat as authenticated with mock user

## Optional: Target structure

For large layout refactors only. Show the new tree in a fenced `text` block. Skip otherwise.

```text
feeds/
├── algorithms/
│   ├── registry.py
│   └── implementations/chronological.py
└── feed_generator.py
```

## Phase 2 checklist (multi-step)

- [ ] `## Details` present only because a gate fired
- [ ] End-to-end steps match the post-change path
- [ ] Existing flow changed → Before and After mermaid both present
- [ ] New multi-step path → After mermaid present; no invented Before
- [ ] No Overview / Happy Flow / Data Flow headings
- [ ] Prose stays terse; minimal bold
