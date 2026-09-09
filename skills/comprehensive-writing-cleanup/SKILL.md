---
name: comprehensive-writing-cleanup
description: >-
  Cleans up prose by applying plain-writing, anti-slop-writing,
  humanizer-writing, the Addy Osmani clear writing principles, and the
  project's preferred vocabulary, then writing the edited text. Use when
  the user asks to clean up, rewrite, humanize, deslopify, or
  comprehensively edit writing, or when they run /comprehensive-writing-cleanup.
disable-model-invocation: true
metadata:
  owner: mark
  scope: global
  category: writing
---

# Comprehensive writing cleanup

Run a full prose cleanup as a sequence of passes. Each pass reads its source
and edits the text before the next pass starts. Do not apply a pass from
memory. Do not skip a pass.

## When to use

- The user runs `/comprehensive-writing-cleanup`.
- The user asks to clean up, rewrite, humanize, or comprehensively edit prose.
- The user names a markdown file, a document, or pasted text for a writing cleanup.

## Do not use

- Do not use on code, configs, tests, or data. Change surrounding prose only.
- Do not use as a substitute for a code review.

## Inputs

Resolve the target before editing:

- A file the user named
- Pasted text in the request
- The previous agent response, if they asked to clean that up and named no file

If none of those is clear, ask which file or text to edit and stop.

## Workflow

```markdown
Cleanup progress:
- [ ] 1. Resolve the target and the ai_tools root
- [ ] 2. Apply /plain-writing
- [ ] 3. Apply /anti-slop-writing
- [ ] 4. Apply /humanizer-writing
- [ ] 5. Review against the Addy Osmani clear writing principles
- [ ] 6. Review against conventions/vocabulary.md
- [ ] 7. Check hard constraints, then write the result
```

### 1. Resolve the target and the ai_tools root

Read the target text. Resolve the ai_tools root. Keep a copy of the original
so you can confirm you did not drop a supported claim or change code.

### 2. Apply /plain-writing

Read `plain-writing/SKILL.md` in full. Follow it and
edit the text. Skip the deslopify command unless the user asked for that
output shape.

### 3. Apply /anti-slop-writing

Read `anti-slop-writing/SKILL.md` in full. Follow its
own rules for when to read `references/`. For this full-document cleanup, also
read `references/anti-slop-writing-doctrine.md`. Read
`references/flow-by-relation.md` when paragraphs are locally clear but
list-like. Then edit the text.

### 4. Apply /humanizer-writing

Read `humanizer-writing/SKILL.md` in full. Follow it and edit the text. Keep every
supported claim. Do not add facts, names, numbers, dates, quotes, or citations
that are not already in the source or the user's request.

### 5. Review against the Addy Osmani clear writing principles

Read `https://github.com/mark-torres10/ai_tools/blob/main/conventions/clear_writing_principles_addy_osmani.md`.
Edit the text so it is useful, clear, and specific. On sentence shape, keep
the plain-writing style. Use the Osmani file for usefulness, specificity, named
actors, cutting padding, taking a position, and stopping when the thought
stops.

### 6. Review against conventions/vocabulary.md

Read `https://github.com/mark-torres10/ai_tools/blob/main/conventions/vocabulary.md`. Replace any listed term with the required substitute for that context. Then edit the text.

### 7. Check hard constraints, then write the result

After the last pass, confirm all of the following still hold:

- No em dashes or en dashes
- Vocabulary substitutions still in place
- Code blocks, inline code, commands, paths, YAML, data, and link targets
  unchanged
- No invented facts
- Meaning of the original prose preserved

**File mode.** When the user named a file, write only the final prose to that
file, then give a short summary of what each pass changed.

**Pasted text.** Return the final rewrite. A short summary of what each pass
changed is fine after the rewrite.

## Hard constraints later passes must not undo

- Follow plain-writing on dashes, invented jargon, analogies, filler, and
  sentence shape.
- Follow vocabulary.md on the listed terms. The vocabulary pass is last so
  earlier passes cannot put a banned term back.
- Do not change code or structured data.
