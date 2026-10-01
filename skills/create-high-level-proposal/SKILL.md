---
name: create-high-level-proposal
description: >-
  Writes a high-level proposal for a unit of work before anyone writes an
  implementation plan. The proposal covers scope, cross-cutting concerns, file
  structure, schema models, high-level steps, expected results, and the
  decisions the user must confirm. Use when the user asks for a proposal, a
  high-level spec, or a design to review before /create-implementation-plan.
disable-model-invocation: false
metadata:
  owner: mark
  scope: global
  category: planning
---

# Create high-level proposal

Write a `proposal.md` that a reviewer can read in a few minutes, and then approve, redirect, or reject. You write the proposal after the user describes the work and before anyone writes an implementation plan. In the proposal, you decide what gets built, where the code and data live, which existing code you reuse, and what shape the data takes. You also list the choices that the user still has to make. Once the user confirms the proposal, `/create-implementation-plan` turns it into steps with exact commands, tests, and file changes.

- Audience: the user, and a senior or staff engineer who knows the codebase but not this task. They read the proposal to check the direction before any code exists.
- Tone: terse and direct. Each sentence names a file, a model, a number, or a choice. Put the overview first and the detail after it.

## When to use

- The user asks for a proposal, a high-level spec, or a design to review before an implementation plan.
- The user gives an issue or a rough description and wants to agree on the direction first.
- The file layout, the data shapes, or a major choice is still open, so an implementation plan would be premature.

## Do not use

- If the user already confirmed a direction and wants steps, use `/create-implementation-plan`.
- If the user wants to compare options with an outside AI that has no access to the repo, use `/create-advisory-brief`.
- If the user wants code, use `/implement-from-spec` or `/implement-plan-and-open-pr`.

## Inputs

Before you write, identify the following:

- The source of the request, which is an issue URL, pasted issue text, or a description in the chat. Read a GitHub issue with `gh issue view`, and read the issues, PRs, plans, and papers that it links.
- The scope. If the user limits the proposal to certain parts, e.g., "only the file structure, schemas, and Jev code", cover only those parts and link to where the rest is decided.
- The depth. By default, a proposal names files, models, fields, and function signatures, and it leaves out function bodies. Write full code only when the user asks for it.

If the source or the scope is unclear, ask one question and stop.

## Relevant file paths

- `<workspace_root>/docs/plans/<YYYY-MM-DD>_<descriptor>_<6-digit hash>/proposal.md` is where you write the proposal. When you later run `/create-implementation-plan`, point it at the same folder, so `plan.md` sits next to `proposal.md`.
- `<workspace_root>/docs/plans/` also holds earlier plans, which show how the repo lays out and names its work.
- `<workspace_root>/docs/runbooks/` holds the runbooks for the repo.

## Workflow

```markdown
Proposal progress:
- [ ] 1. Resolve the source, scope, and depth
- [ ] 2. Research what exists
- [ ] 3. Draft proposal.md
- [ ] 4. Clean up and simplify
- [ ] 5. Ask the user to confirm (wait)
- [ ] 6. Revise and stop
```

### 1. Resolve the source, scope, and depth

Follow the inputs section above. Write the scope as the first line of the proposal, so the reviewer knows what the proposal covers and what it leaves to other issues or plans.

### 2. Research what exists

Find the code, data, and docs that the work can reuse before you design anything new. Look for the following:

- Engines, clients, and helpers that already call the same service, e.g., an existing Bedrock or OpenAI engine.
- Schemas, prompts, constants, and storage helpers in sibling experiments or in a shared package.
- The layout of the most similar earlier work, such as an experiment folder or a plan in `docs/plans/`.
- Dependencies and their pinned versions in `pyproject.toml` or `package.json`.

Record each thing you reuse with its exact path and symbol. If you build a small prototype to check an assumption, such as the shape of a third-party response, say so in the proposal, and do not commit the prototype.

### 3. Draft `proposal.md`

Use the template below. Leave out any section that does not apply, and never write an empty "N/A" section.

```markdown
# Proposal: (what gets built, in one line)

Scope: (issue link). (The parts this proposal covers, and links to where the other parts are decided.)

## Overview

(Two to four sentences on the problem, what gets built, and what the user has at the end.)

## Cross-cutting concerns

### (Concern, e.g., data, models, storage, reuse, or dependencies)

## File structure

### Repository

### (Storage outside the repo, e.g., S3)

## Schema and key interfaces

| Model | Lives in | Role |
| --- | --- | --- |

## Steps

### Step 1: (title, leading with an action verb)

(One to three sentences on what the step reads and what it produces.)

## Expected results

## Decisions to confirm

1. **(Decision.)** (Recommendation, reason, and the main alternative.)
```

Write each section as follows:

- **Scope.** Link the issue. Name each part that the proposal covers, and link to where every other part is decided.
- **Cross-cutting concerns.** Cover the choices that affect more than one step, e.g., data sources and filters, model IDs, the storage location, reused code, and new dependencies. When you move code into a shared location, state the allowed import direction, e.g., "root `shared/` never imports from `experiments/`". Then say which side each piece goes on, and use a table when there are several pieces.
- **File structure.** Show a `text` tree of every new or changed file, with a few words on what each file holds. If the work stores artifacts outside the repo, such as in S3, show that tree too. Name the existing folders that stay unchanged.
- **Schema models.** For each model, give its location, whether it is new or reused, and its role. List the fields of each new model. Say which fields you store and which stay in memory.
- **Steps.** Write one to three sentences per step on what the step reads and what it produces. Leave commands, tests, and file-by-file changes for the implementation plan.
- **Expected results.** State what a successful run produces, e.g., row counts, runtime, token use, and cost. Label each number as measured or estimated, and say how you got it.
- **Decisions to confirm.** Number each decision, so the user can answer by number. Give the recommendation, the reason, and the main alternative for each one.

### 4. Clean up and simplify

Run `/comprehensive-writing-cleanup` on `proposal.md`, and then run `/review-for-simplicity`. Apply the cuts that are clearly right. If the simplicity review suggests cutting something that the issue requires, keep it and add the cut to "Decisions to confirm".

### 5. Ask the user to confirm, then wait

Give the user the path to `proposal.md`, a summary of two or three sentences, and the list of decisions to confirm. Ask the user to approve the proposal or to answer the decisions by number. Do not start `/create-implementation-plan` until the user approves.

### 6. Revise and stop

Apply the user's answers to `proposal.md`, and mark each decision as confirmed or changed. Show the proposal again only if the scope, the file structure, or a schema model changed. Then stop. The next step is `/create-implementation-plan`, with `proposal.md` as its input.

## Anti-patterns

- Do not include commands, test cases, verification steps, or per-file change lists. Leave them for the implementation plan.
- Do not write full function bodies unless the user asked for code.
- Do not describe reuse vaguely, e.g., "use the existing helpers" or "follow the existing pattern". Give the exact path and symbol.
- Do not leave a choice in the prose. Put every open choice under "Decisions to confirm".
- Do not state a number without its source. Label each number as measured or estimated.
- Do not restate the issue. Link to it, and spend the space on what the issue leaves open.

## Examples

Read the examples before your first draft.

- `examples/example1.md` is a proposal for issue 330. The user limited it to the file structure, the schema models, and the Jev code, so it includes full code. Go to that depth only when the user asks for code.
- `examples/example2.md` to `examples/example5.md` are issue descriptions that the user wrote. They show the kind of input you get, and the sections the user cares about, which are cross-cutting concerns, file structure, storage, steps, analysis, and what "done" means.
