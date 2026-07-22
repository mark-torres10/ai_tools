# Backend gate (Layer 1)

Read when the PR is a **backend** change whose review needs the request or input/output path through the change — APIs, services, workers, handlers, or internal call chains.

## Fires when

Diff changes how a request, message, or job input moves through backend code (route → service → store, consumer → handler → emit, CLI/command → core → side effect). Skip for pure renames, comment-only, or isolated helpers with no I/O boundary change.

## Required under Details

1. **Request / I/O flow (narrative)** — Numbered steps for one primary happy path through the change. Name real modules, endpoints, queues, and stores.
2. **Flow diagram** — Mermaid of that path after this PR.
   - If an existing request/I/O path changed: **Before** and **After** diagrams.
   - If this PR introduces a new path: **After** only.

Call out auth, validation, or error branches only when the PR changes them.

## Mermaid guidance

- Prefer `sequenceDiagram` for request/response, or `flowchart TD` for linear pipelines.
- Show actor → API → service → DB/queue (or equivalent).
- Keep one primary path; do not diagram every branch.

## Example shape

```markdown
### Request flow

1. `POST /v1/runs` hits `api/routes/runs.py`.
2. `RunService.create` validates payload and writes `runs`.
3. Enqueues `run.started` on the worker queue.
4. Returns `201` with `run_id`.

### Before
(mermaid — if existing)

### After
(mermaid — proposed)
```

## Checklist

- [ ] Narrative is one clear input → processing → output path
- [ ] After (and Before if existing path changed) mermaid present
- [ ] Names match real endpoints/modules in the diff
- [ ] Terse; no OpenAPI dump
