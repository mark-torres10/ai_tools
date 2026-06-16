# Runbooks Audit Reference

Apply in Phase 2 for every plan. Target workspace runbooks only—not the ai_tools repo unless that is where the change lands.

## Runbook path discovery

**Runbook root:** `<workspace_root>/docs/runbooks/`

Each project's runbook layout differs. Do not assume subfolder names beyond what you find in inventory.

- If `docs/runbooks/` is missing or empty, note that in **Update Runbooks** and still run gap analysis for anything the plan introduces.
- If the workspace has a runbook template under `docs/runbooks/`, prefer it when proposing new runbooks; otherwise use `runbook-template.md` in this skill's `references/` directory.

## When runbook updates are required

Audit runbooks whenever the plan changes any of:

- How to run, deploy, or roll back the system
- Env vars, secrets, auth, or local dev setup
- Service boundaries, pipelines, cron/workers, or on-call surfaces
- Failure modes, recovery steps, observability, or escalation
- Manual verification steps that operators would repeat outside the PR

If none of these apply, the section is still required — use **No runbook impact** (see output format below).

## Discovery workflow (mandatory order)

1. **Inventory** — List all files under `docs/runbooks/` recursively. Record exact paths only from the target workspace.
2. **Read frontmatter** — For each runbook with YAML frontmatter, use `name`, `description`, and `paths` globs to judge relevance to the plan.
3. **Classify each existing runbook**:
   - **No change** — plan does not touch topics covered by this runbook.
   - **Update required** — plan changes commands, env, behavior, failure modes, or verification that this runbook documents. Name template sections to edit (e.g. Prerequisites, Verify It Worked).
   - **Review recommended** — tangentially related; call out what to double-check after implementation.
4. **Gap analysis** — If the plan introduces new operational surfaces with no matching runbook, propose a new file under `docs/runbooks/`. Choose path and grouping to match patterns in the inventory when present.
5. **Cross-check Manual Verification** — Any manual verification step an operator would run in prod/staging should appear in a runbook update row or new runbook proposal.

## New runbook rules

When proposing new runbooks, follow `runbook-template.md` in this skill's `references/` directory.

**Naming:**

- Procedural guides → `HOW_TO_<TOPIC>.md`
- Conceptual overviews → `WHAT_IS_<TOPIC>.md`
- Group related runbooks in subfolders when the project's inventory already does (e.g. `docs/runbooks/<topic>/`)

**Frontmatter (required for new runbooks):**

```yaml
---
name: kebab-case-slug
description: >-
  When to load this runbook — symptoms, tasks, outcomes.
paths:
  - "glob/patterns/**"
---
```

**Section outline for proposals** — list which template sections apply; omit optional sections you do not need:

| Section | Include in proposal when |
|---------|--------------------------|
| Title + intro paragraph | Always |
| When to Use | Always |
| Prerequisites | Env vars, accounts, or running services apply |
| Primary procedure section(s) | Always for `HOW_TO_*` runbooks |
| Verify It Worked | Always |
| Reference | Defaults, formats, or layer-by-layer debugging matter |
| Troubleshooting | Failure modes or recovery change |
| Testing Checklist | Tests or lint commands are part of ops |
| Out of Scope | Boundaries need to be explicit |
| Related Runbooks | Link only to paths discovered in inventory |

## Output format (use in every plan)

```markdown
## Update Runbooks

**Runbook root:** `docs/runbooks/` — exists | missing | empty

### Existing runbooks

| Runbook | Status | Sections / changes needed | Why |
|---------|--------|-----------------------------|-----|
| `docs/runbooks/...` | no change \| update required \| review recommended | ... | ... |

### New runbooks to create

| Proposed path | `name` | `description` (draft) | `paths` globs | Section outline |
|---------------|--------|----------------------|---------------|-----------------|
| `docs/runbooks/...` | ... | ... | ... | When to Use, ..., Verify It Worked |

### No runbook impact

(Use only when truly none of the "when required" triggers apply.)

None — this change is limited to `<scope>` and does not alter operational procedures documented in runbooks.
```

## Delegation rules

- Runbook edits may appear as a **Parallel Task Packet** only when exact runbook file(s) are listed in **files allowed to change** and no other parallel task owns the same file.
- If a runbook must stay in sync with a frozen contract (API shape, env var names, CLI flags), place runbook tasks **after** **Interface or Contract Freeze** in **Integration Order**.

## Runbook anti-patterns

- Skipping runbook audit when the plan changes deploy, env, auth, or recovery paths
- Vague runbook notes ("update docs as needed") without file paths and section names
- Proposing new runbooks without `name`, `description`, `paths`, and section outline
- Citing runbook paths that were not found in the target workspace inventory (except **Related Runbooks** links between discovered files)

## Phase 2 gate

Do not proceed to Phase 3 until:

- [ ] `docs/runbooks/` was inventoried (or absence was noted).
- [ ] Every discovered runbook is classified (no change / update required / review recommended).
- [ ] New runbooks are proposed with template-aligned frontmatter and section outline, or **No runbook impact** is justified.
- [ ] No runbook paths appear in the plan except those found in inventory or proposed as new files.
