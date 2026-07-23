---
name: create-implementation-plan
description: >-
  Use when the user asks for an implementation plan.
disable-model-invocation: false
metadata:
  owner: mark
  scope: global
  category: planning
---

# Create Implementation Plan

Produce a complete plan package up front for how to implement work.

- `plan.md` (router + executive summary). Full detail lives in sibling files under the plan asset directory. Planning still runs every applicable phase.
- Intended audience: humans skim the plan.md to get an overview of the implementation plan. Keep it high-level. Appropriate for a senior or staff engineer reviewing a project without context.
- Tone: terse, direct, clear, executive-summary style updates. Sufficient clear detail to provide context to stakeholders without much context. However, avoids excessive verbosity and practices progressive disclosure.

Anti-patterns:

- `plan.md` should not have code or names of variables or interfaces.
- `plan.md` should not dump full implementation details.
- Avoid vague task descriptions. Better to not mention it than to use vague descriptions.
- Avoid vague modifiers and dangling modifiers, such as "as needed", "etc.", or "follow the existing pattern", without naming the exact reference file or symbol
- Avoid verification steps that rely on unfinished parallel work. Assume that the work in `plan.md` is self-encompassed.
- Avoid delegated steps that requires hidden intent or unstated judgment.

Include at the top of every plan:

```markdown
## Remember
- Exact file paths always
- Exact commands with expected output
- DRY, YAGNI, TDD, frequent commits
- Delegated tasks must be impossible to misread.
```

Relevant filepaths:

- `<workspace_root>/docs/plans`: where to put the work when generating a plan.
- `<workspace_root>/docs/runbooks/`: runbooks for that repo.

Target file layout:

```text
docs/plans/<YYYY-MM-DD>_<descriptor>_<6-digit hash>/
  plan.md                 # router + executive summary
  steps/
    step1.md
    step2.md
    ...
  images/...              # UI before/after — only if UI change
```

Omit files that are unnecessary. Never write empty N/A stubs.

Start with a draft version of `plan.md`. It should have this setup:

```markdown
# (Name of Plan. Focus on 1-sentence, leading with an action verb)

## Remember
- Exact file paths always
- Exact commands with expected output
- DRY, YAGNI, TDD, frequent commits
- Delegated tasks must be impossible to misread.

## Overview

## Happy flow

1-2 sentence description of intended user journey. Then include a mermaid diagram of the intended change.

## Approach

1-2 sentence of the approach. Focus on philosophy and intention and design of approach.

## Steps

### Step 1: (title)

(1-2 sentences of how to do this, at a high level)

### Step 2: (title)

(1-2 sentences of how to do this, at a high level)

## What "done" looks like

(enumerated list of what will be the end state of things when done)

```

Ask the user for confirmation here and ask for possible revisions. Once this is confirmed by the user, expand the plan to now create a separate markdown file for each step.

Store these in `{workspace root}/docs/plans/{doc plan folder}/steps/{step1,step2,etc.}.md`.

The setup of each step should look something like:

```markdown
# Step {n}: {name of step}

{details of steps}
```

For writing each step, use the `/implement-from-spec` skill to design implementation details.

Some additional rules while writing each step:

- Include a list of files to inspect, files allowed to change, and files forbidden to change.
- Include what must pass/fail for each step.
- For ui changes, require screenshots before and after. Put these in `{workspace root}/docs/plans/{doc plan folder}/images/{before/after}/`.
