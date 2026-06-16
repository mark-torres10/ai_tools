# Runbook Template

Copy this structure when proposing or creating a runbook under `docs/runbooks/`. Replace bracketed placeholders and delete optional sections you do not need.

```markdown
---
name: template-runbook-slug
description: >-
  One or two sentences describing what this runbook covers and when an agent
  or developer should load it. Be specific about symptoms, tasks, or outcomes.
paths:
  - "path/to/relevant/code/**"
  - "another/path/**"
  - ".env"
---

# Runbook Template

Copy this file when adding a runbook under `docs/runbooks/`. Replace bracketed placeholders and delete optional sections you do not need.

**Naming:** procedural guides → `HOW_TO_<TOPIC>.md`; conceptual overviews → `WHAT_IS_<TOPIC>.md`. Group related runbooks in subfolders (e.g. `docs/runbooks/chat/`).

**Frontmatter:** `name` is kebab-case for agent discovery. `description` should state *when* to use the runbook. `paths` lists globs for code the runbook touches.

## Title (replace with your runbook title)

Example: `# How to Run Example Service Locally`

One short paragraph: what system or workflow this runbook covers, where the code lives, and any critical context (e.g. run from repo root with `uv`).

## When to Use

- Bullet describing a symptom or task that maps to this runbook
- Another scenario — keep these concrete and scannable
- Optional: link to a related runbook if the boundary is fuzzy

## Prerequisites

List env vars, accounts, running services, or prior steps. Omit this section if none apply.

```bash
# Example env vars in repo-root .env
EXAMPLE_API_KEY=...
```

Note any startup behavior (e.g. restart the server after changing `.env`).

## [Primary Procedure Section]

Use imperative headings for each major step. Include copy-pasteable commands from the **repo root**:

```bash
uv run ...
```

Expected output or log line:

```text
Application startup complete.
```

### Sub-step or Variant (Optional)

Break complex steps into subsections. Show before/after code or config when editing files.

## Verify It Worked

Show how to confirm success — curl, pytest, UI check, or expected response fields:

| Field | Expected |
|-------|----------|
| `example_id` | non-empty string |
| `status` | `"ok"` |

```bash
curl -s http://127.0.0.1:8000/health | python -m json.tool
```

## Reference

Tables work well for defaults, id formats, or layer-by-layer debugging:

| Concept | Value | Source |
|---------|-------|--------|
| Default setting | `example` | `app/example/constants.py` |

```text
Optional ASCII diagram of flow or package layout
app/example/
├── module_a.py
└── module_b.py
```

## Troubleshooting (Optional)

| Layer / Symptom | Where to look |
|-----------------|---------------|
| Validation error | `app/example/schemas.py` |
| Runtime failure | server logs, `.env` keys |

Common fix:

```bash
rm -f path/to/cache-or-state
```

## Testing Checklist (Optional)

```bash
uv run pytest tests/app/example/ -v
uv run ruff check app/example tests/app/example
uv run pyright app/example
```

- [ ] Step-by-step checkbox for manual verification after a change
- [ ] Another checkbox if the change has multiple blast radii

## Out of Scope (Optional)

- Features or environments this runbook deliberately does not cover
- Pointers to future work or separate runbooks

## Related Runbooks

- [OTHER_RUNBOOK.md](OTHER_RUNBOOK.md) — short note on why it is related
```
