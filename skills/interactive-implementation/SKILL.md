---
name: interactive-implementation
description: >-
  Runs an implementation plan step-by-step via implement-plan-and-open-pr,
  then at each step runs write-docstring and review-for-simplicity and awaits
  approval before committing. Use when implementing a plan interactively one
  step at a time with review gates. Slash-only.
disable-model-invocation: true
metadata:
  owner: mark
  scope: project
  category: execution
---

Given a plan and its step files, first run the `/implement-plan-and-open-pr` skill . Stop at each step. Once you think you're done with each step:

1. Run the `/write-docstring` skill to make sure that the docstrings are clean.
2. Run `/review-for-simplicity` to review the simplicity of the implementation.

Then await my approval at the end of each step (prior to committing). If I state that I want changes made, make those changes. Else, commit and move on to the next step.

At each step, start your report with the following format:

Here's an example, assuming you just finished Step 2 of 4

```markdown
# {Plan name}

✅ Step 1: {Step name}
✅ Step 2: {Step name}
⏳ Step 3: {Step name}
⏳ Step 4: {Step name}

## Latest step: Step 2: {Step name}

{What was implemented, 1-2 sentences}

## Key interfaces, data models, and seams

{enumerated list of key interfaces, data models, and seams}

## What does this accomplish?

{What does this accomplish? 1-2 sentences}

## How to verify

{How to manually verify}

## What comes next?

{2-3 sentence description of what comes next and how this leads into that work}

```
