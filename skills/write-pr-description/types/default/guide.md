# PR Descriptions (Default)

Use this outline when the change does not fit **experiment**, **feature**, or **bug**. It is a catch-all for refactors, chores, infra tweaks, docs, dependency bumps, and other PRs that still need a clear body.

A default PR description should let another engineer quickly understand:

1. What problem or need drove the change.
2. What was done about it.
3. Why that approach (and what is in/out of scope).
4. How to run or verify it.

Keep Purpose a bit fuller if needed. Keep every other section terse. Prefer behavior and outcomes over a file changelog.

## Outline

### 1. Problem

State the situation that made the change necessary.

It should answer:

- What was wrong, missing, painful, or unclear?
- Who or what is affected?

Guidelines:

- Max 2-3 sentences.
- Describe the observable gap, not the code you plan to touch.
- If there is no “broken” behavior (e.g. cleanup), say what friction or risk this reduces.

Common anti-patterns:

- Listing files or tickets without stating the need.
- Jumping to the solution before naming the problem.

An example:

```markdown
## Problem

CI installs every optional ML extra on every PR, so feedback takes 12–15 minutes
even for docs-only changes. Reviewers routinely wait on the critical path for
work that never exercises those extras.
```

### 2. Solution

State what this PR does to address the problem.

It should answer:

- What changed, from a caller/operator perspective?
- What is the new or restored behavior?

Guidelines:

- Max 2-3 sentences.
- Lead with the outcome, then the mechanism only if it clarifies the outcome.
- Omit stale implementation detail (variable names, one-off helper renames).

Common anti-patterns:

- A bullet dump of every file touched.
- Repeating the Problem without saying what changed.

An example:

```markdown
## Solution

Split the PR workflow into a fast default job and an optional `ml-extras` job.
Docs and non-ML paths run the default job only; the heavy install runs when
`paths` or a label indicate ML code changed.
```

### 3. Purpose

Explain why this solution (and its scope) is the right move.

It should answer:

- Why address this now?
- What tradeoff or constraint shaped the approach?
- What is explicitly in/out of scope?

Max 2-3 sentences.

An example:

```markdown
## Purpose

Faster PR feedback for the common path without dropping ML coverage where it
matters. Migrating other workflows (release, nightly) and changing local
`make` targets is out of scope.
```

### 4. How to run

Provide a terse list of commands or checks that exercise the change.

Guidelines:

- Prefer the happy path someone else can run today.
- Note expected results when they are not obvious.
- Mention required services or working directory only when needed.

An example:

````markdown
## How to run

```bash
# docs-only path (expect default job only)
git push origin HEAD

# ML path (expect default + ml-extras)
# touch a file under ml/ then push, or apply the `ml` label
```

Confirm the default job finishes in roughly the previous non-ML duration and
that `ml-extras` still installs and tests when triggered.
````

Verify that:

- Commands are current
- Required services are mentioned
- Paths assume a clear working directory
- Success criteria are explicit
