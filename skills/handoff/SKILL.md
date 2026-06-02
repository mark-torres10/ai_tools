---
name: handoff
description: >-
  Produces a concise end-of-session handoff in `handoff.md` summarizing what was
  done, what remains (with the last to-do you were working on), the PR link, and
  the key plan/notes files to read next. Use at the end of a work session or
  before switching agents.
disable-model-invocation: true
metadata:
  owner: mark
  scope: project
  category: project_management
---

# Handoff

Generate a single Markdown file `handoff.md` in the repo root so the next agent (or a human) can resume quickly.

Hard requirements:

- Prefer plan sources in `.cursor/plans/` first, then `docs/plans/`.
- Include the PR URL (or explicitly say no PR yet).
- Enumerate remaining to-dos and explicitly mark the last to-do you were working on when the session ended.
- Include the key files someone should open next to understand the implementation.
- `handoff.md` must have **max 3 sections** and **each section must be exactly 1 paragraph** (no bullet lists).

## When to Use

- End of a session where work was performed and someone else may continue.
- Before handing off to another agent.
- Before pausing work on an open PR/branch.

## Do Not Use

- Do not use mid-session as a running log (keep it end-of-session).
- Do not invent a plan or PR if none exists; instead ask for the file(s) / link(s).

## Inputs to Resolve

You need four things to write a correct handoff:

- **Plan / notes source(s)** (prefer `.cursor/plans/`, then `docs/plans/`)
- **PR URL** (or “no PR yet”)
- **What changed** (briefly: features/fixes + high-signal files)
- **Remaining work** (to-dos + last in-progress item)

## Plan / Notes Discovery (mandatory order)

1. **Primary**: find plan markdown in `.cursor/plans/`
   - If multiple exist, prefer the most recently modified plan file(s).
2. **Fallback**: find plan markdown in `docs/plans/`
   - Prefer the most recently modified plan folder/file(s).
3. **If still unclear**:
   - Stop and ask the user **which markdown file(s)** should be treated as the plan/notes source for this work.

## PR Discovery

If you already have a PR URL from the session, reuse it.

If you do not:

- Try to resolve it from the current branch using `gh` (preferred).
- If no PR exists for the branch, record “no PR yet” and include the branch name + latest commit SHA.

## What to Extract (do this before writing)

From the plan/notes:

- The planned scope and acceptance criteria (one sentence max in the handoff).
- The to-do list / remaining tasks (translate checklists into a short inline list).

From your actual work:

- What you completed (1–3 crisp clauses).
- Key files that capture the core changes (paths only; choose the smallest set that explains the change).
- Any known blockers, missing credentials, or required follow-ups.

From current state:

- What you were doing last when you stopped (a single “last to-do”).

## Output File: `handoff.md` (required format)

Create or overwrite `handoff.md` at the repo root with exactly **3** `##` sections:

1. `## Context`
2. `## What’s done`
3. `## Next`

Each section must be exactly **one paragraph** (no lists, no blank lines inside the section, no subheadings).

### Content requirements per section

`## Context` paragraph must include:

- PR URL (or “No PR yet”)
- Branch name (if known)
- Plan/notes file path(s) used (at least one path)

`## What’s done` paragraph must include:

- 1–3 clauses summarizing completed work
- Key file paths to read next (inline)

`## Next` paragraph must include:

- Inline list of remaining to-dos (comma/semicolon separated)
- Explicit “Last left off:” marker naming the last in-progress to-do
- Any blocker/user action needed (if any)

## Stop and Ask

Stop and ask the user if:

- You cannot find any plan/notes in `.cursor/plans/` or `docs/plans/`, and it’s unclear which markdown file(s) define the intended work.
- Multiple plausible plan/notes files exist and you cannot confidently pick the right one(s).
- You cannot determine whether a PR exists and `gh` access is unavailable or fails.
