# Runbooks Audit Reference (Approach A)

Apply in Phase 2 **only when the ops / runbooks gate fires**.

**Gate fires when** the plan changes any of:

- How to run, deploy, or roll back the system
- Env vars, secrets, auth, or local dev setup
- Service boundaries, pipelines, cron/workers, or on-call surfaces
- Failure modes, recovery steps, observability, or escalation
- Manual verification steps that operators would repeat outside the PR

**If none apply:** do **not** create `runbooks.md`, do **not** add an Update Runbooks section to `plan.md`, and do **not** write "No runbook impact" filler files. Skip this reference entirely.

When the gate fires: inventory target-workspace runbooks, write full audit to **`runbooks.md`**, and add a short **index** in `plan.md` (touch/no-touch + link).

## Runbook path discovery

**Runbook root:** `<workspace_root>/docs/runbooks/`

Each project's layout differs. Do not assume subfolder names beyond inventory.

- If `docs/runbooks/` is missing or empty, note that in `runbooks.md` and still run gap analysis for new operational surfaces.
- If the workspace has a runbook template under `docs/runbooks/`, prefer it for new runbooks; otherwise use [runbook-template.md](runbook-template.md).

## Discovery workflow (mandatory order)

1. **Inventory** — List all files under `docs/runbooks/` recursively. Exact paths only from the target workspace.
2. **Read frontmatter** — Use `name`, `description`, and `paths` globs to judge relevance.
3. **Classify each existing runbook**:
   - **No change** — plan does not touch this runbook's topics.
   - **Update required** — plan changes commands, env, behavior, failure modes, or verification. Name sections to edit.
   - **Review recommended** — tangential; note what to double-check after implementation.
4. **Gap analysis** — New operational surfaces without a matching runbook → propose a new file under `docs/runbooks/`.
5. **Cross-check `verification.md`** — Operator-facing manual checks should appear in an update row or new runbook proposal.

## New runbook rules

Follow [runbook-template.md](runbook-template.md) when proposing new runbooks.

**Naming:**

- Procedural → `HOW_TO_<TOPIC>.md`
- Conceptual → `WHAT_IS_<TOPIC>.md`
- Group in subfolders when inventory already does

**Frontmatter (required for proposals):**

```yaml
---
name: kebab-case-slug
description: >-
  When to load this runbook — symptoms, tasks, outcomes.
paths:
  - "glob/patterns/**"
---
```

**Section outline** — list which template sections apply; omit unused optionals:

| Section | Include when |
|---------|----------------|
| Title + intro | Always |
| When to Use | Always |
| Prerequisites | Env vars, accounts, or services apply |
| Primary procedure section(s) | Always for `HOW_TO_*` |
| Verify It Worked | Always |
| Reference | Defaults, formats, layer debugging matter |
| Troubleshooting | Failure modes / recovery change |
| Testing Checklist | Tests/lint are part of ops |
| Out of Scope | Boundaries need to be explicit |
| Related Runbooks | Link only to inventory paths |

## Output: `runbooks.md` (full leaf)

```markdown
# Update Runbooks

**Runbook root:** `docs/runbooks/` — exists | missing | empty

## Existing runbooks

| Runbook | Status | Sections / changes needed | Why |
|---------|--------|-----------------------------|-----|
| `docs/runbooks/...` | no change \| update required \| review recommended | ... | ... |

## New runbooks to create

| Proposed path | `name` | `description` (draft) | `paths` globs | Section outline |
|---------------|--------|----------------------|---------------|-----------------|
| `docs/runbooks/...` | ... | ... | ... | When to Use, ..., Verify It Worked |
```

## Output: `plan.md` index only

When `runbooks.md` exists, Layer 0 includes a short index, for example:

```markdown
## Runbooks

- Updates: `docs/runbooks/HOW_TO_DEPLOY.md` (Verify It Worked)
- No change: `docs/runbooks/WHAT_IS_PIPELINE.md`
- Full audit: [runbooks.md](runbooks.md)
```

Omit the entire Runbooks section from `plan.md` when the ops gate did not fire.

## Delegation rules

- Runbook edits may be a **parallel packet** only when exact runbook file(s) are listed in **files allowed to change** and no sibling packet owns the same file.
- If a runbook must stay in sync with a frozen contract, place that packet **after** contract freeze in the Tasks (in order) table (`plan.md`).

## Anti-patterns

- Creating `runbooks.md` when ops gate did not fire
- "No runbook impact" N/A files or empty stubs
- Vague notes ("update docs as needed") without paths and section names
- Proposing new runbooks without frontmatter + section outline
- Citing paths not in inventory (except Related links between discovered files)
- Dumping the full audit table into `plan.md` instead of `runbooks.md`

## Phase gate (ops)

When the ops gate fired, do not proceed to Phase 3 until:

- [ ] `docs/runbooks/` inventoried (or absence noted) in `runbooks.md`
- [ ] Every discovered runbook classified
- [ ] New runbooks proposed with template-aligned frontmatter and section outline
- [ ] No runbook paths except inventory + new proposals
- [ ] `plan.md` will only index (not duplicate) this leaf
