---
name: create-epic
description: >-
  Turns a scoped multi-step implementation plan into a GitHub epic: one parent
  issue plus one child sub-issue per plan step (each child is one future PR).
  Use when the user invokes /create-epic, asks to file an epic, or wants a
  container issue with child issues for a plan.
disable-model-invocation: true
metadata:
  owner: mark
  scope: global
  category: planning
---

# Create Epic

File a GitHub epic from a complete implementation plan: one **parent** issue (tracking-only) and one **child** sub-issue per plan step. Each child is the unit of work for **one future PR**. This skill does not open PRs, write product code, or edit plan files.

Do not use this skill unless the user explicitly invoked `/create-epic` or named it.

## When to Use

- The user invokes `/create-epic`.
- The user wants a GitHub container issue plus child issues for a scoped, multi-step plan.

## Do Not Use

- Planning only with no intent to file GitHub issues — use `create-implementation-plan`.
- Implementing a plan or opening PRs — use `implement-plan-and-open-pr` (one child / one step at a time).
- Stacked PRs (`gh stack`) or `gh pr create`.
- Filing Linear tickets.

## Overlay on planning

When this skill runs `create-implementation-plan`, add these rules. Do **not** change that skill’s files.

- Every step is independently reviewable and mergeable as **one PR**.
- Do not emit a step that cannot ship alone.
- The parent issue covers the whole plan; children are the PRs.

## Workflow

```
Epic progress:
- [ ] 1. Resolve repo
- [ ] 2. Ensure full plan package
- [ ] 3. Search for an existing epic
- [ ] 4. Propose (wait)
- [ ] 5. Create via one subagent
- [ ] 6. Print the table and stop
```

### 1. Resolve repo

Use the current workspace’s `gh` remote (`gh repo view`). If there is no remote or issues are disabled, stop and ask.

Labels, assignees, projects, milestones: **none** unless the user named them in the invoke.

You may read temp files (including ones the user will delete). Never cite them.

### 2. Ensure a full plan package

Need `plan.md` **and** expanded `steps/*.md`.

Pick the plan in this order:

1. Path the user named.
2. Path clearly in-thread.
3. Newest `docs/plans/*/plan.md` that has a `steps/` directory.

If two complete packages look plausible, ask.

If the package is missing or `plan.md` has no expanded steps: read and follow the `create-implementation-plan` skill (including its draft → confirm → expand, and `implement-from-spec` inside steps), with the overlay above. Do not propose GitHub issues until that package exists.

### 3. Search for an existing epic

Search open issues for the plan `H1` as the parent title, or a parent that already holds those child titles.

If found: show the URL(s) and ask whether to add missing children or abort. Do not create duplicates. Do not silently edit an existing epic.

### 4. Propose, then wait

Orchestrator only. Do not `gh issue create` yet.

1:1 step → child unless the user accepts a split/merge. You may *recommend* a split/merge in the proposal; do not apply it unless they say yes.

**Titles:** parent = plan `H1`. Children = step titles as written.

**Table** (parent is row 1; children in implementation order):

```markdown
| Issue link | Title | What's accomplished |
| --- | --- | --- |
| pending | {parent title} | {epic done-state from plan.md} |
| pending | {step title} | {what this step/PR ships} |
```

Under the table:

- **Dependencies:** real `blocked-by` edges only (from the plan). No fake total chain. Parallel steps stay unblocked.
- **Recommended split/merge:** questions only, not applied.

No extra proposal file.

**Approval:** `yes` / `lgtm` / `create them` / `go` means file it. Apply title/order edits from that reply, then create. Show a second proposal only if the **set** of issues changed (add / drop / split), not for a title tweak.

### 5. Create (one subagent)

After approval, spawn **one** subagent to do all GitHub mutation. The orchestrator does not create issues. The subagent does not talk to the user.

Give it the approved list: titles, bodies, parent vs child, real `blocked-by` pairs, optional labels/assignees, owner/repo.

It must:

1. Create the parent, then the children as sub-issues of that parent.
2. Set `--blocked-by` only for approved real deps (child is blocked by the dependency).
3. Edit the parent body so it lists every child (checkbox + number + title).
4. Return parent/child numbers, URLs, titles, and whether types were skipped.

Do not edit `plan.md` or `steps/*.md`.

### 6. Print the table and stop

Same three columns as the proposal, with live issue links. Parent first.

Stop. Do not implement. Do not open PRs. One line is enough that later implementation is `implement-plan-and-open-pr` on one child/step at a time.

## Bodies

Thin. Plan files stay the source of truth.

**Parent** (tracking-only — do **not** say it ships as a PR):

```markdown
{Overview from plan.md}

{Approach from plan.md}

Done when:
{What "done" looks like from plan.md}

## Children

- [ ] #{n} {title}
```

Fill `## Children` after the children exist.

**Child:**

```markdown
{2–5 sentence summary of the step}

Plan step: `{path to steps/stepN.md}`

Done when:
- {acceptance lines from that step}

Ship as one PR. Do not bundle with sibling issues.
```

### 7. Once the issues are created, open a PR with the plan

Open a PR with the plan files (if they're not already merged into main) and reference the container and child issues in the PR description. That PR is plan and docs files only. It must not contain product code. Implementing the children as a stacked PR is `/implement-epic`, not this skill.
