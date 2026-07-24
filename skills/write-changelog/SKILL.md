---
name: write-changelog
description: >-
  Writes CHANGELOG entries for merged or ready PRs.
  Use when the user asks to update CHANGELOG.md, draft a changelog line for a
  PR, or summarize shipped work as a changelog entry.
disable-model-invocation: true
metadata:
  owner: mark
  scope: project
  category: writing
---

# Write Changelog

Write CHANGELOG entries as a terse executive summary of shipped PRs.

PRs carry the verbose implementation detail, rationale, and tradeoffs. The CHANGELOG is the readable history of outcomes and what each PR delivered for the system or user, not a digest of how it was built.

Format and layout: [examples/example1.md](examples/example1.md).

## When to Use

- The user asks to add or update a CHANGELOG entry for a PR.
- The user asks to draft changelog lines from a PR, diff, or merge.
- The user wants a shipped-work summary in CHANGELOG form.

## Do Not Use

- Do not use for PR descriptions (use `write-pr-description`).
- Do not use for weekly status writeups unless the user explicitly wants CHANGELOG format.
- Do not invent entries for work that was not actually shipped.

## Entry Rules

- 1–2 sentences per entry.
- Executive-summary style. Terse. Minimal bolding.
- Lead with the system or user impact.
- Focus on outcome, not logistics.
- Always end with the PR link: `[PR #N](PR link)`. Add this once the PR is generated.
- Name the problem solved and the key intervention. Mention libraries or tools only when they are central to the change.
- Cut implementation rationale, file digests, and design narration.
- Avoid versioning labels (e.g. "V1 of graph").
- Avoid "what this completes / what it doesn’t do yet." State what is implemented.

## Format

Mirror [examples/example1.md](examples/example1.md):

```markdown
# CHANGELOG

## YYYY-MM-DD

1. <1-2 outcome-focused sentences>. [PR #N](https://github.com/<org>/<repo>/pull/N)
```

- Group under `## YYYY-MM-DD` (merge or ship date).
- Number entries under that date.
- Newest dates at the top; append new entries under today’s (or the PR’s) date.
- One PR = one entry unless the user asks otherwise.

## Workflow

1. Identify the PR(s): number, URL, title, and what actually merged.
2. Read enough context (PR body, diff summary, or user notes) to name the outcome—not every file touched.
3. Draft 1–2 sentences that lead with system/user impact and the key intervention.
4. Strip rationale, version labels, and “not yet” narration.
5. Append under the correct date heading in `CHANGELOG.md` (create the file or heading if missing).
6. Return the entry (and file path if edited).
