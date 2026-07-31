---
name: write-docstring
description: >-
  Writes Python docstrings for functions, classes, or modules using numpy-style
  conventions. Routes to the matching guide for criteria and good/bad examples.
  Use when the user asks to write, rewrite, improve, or review a docstring, or
  when adding documentation to a function, class, or file.
disable-model-invocation: true
metadata:
  owner: mark
  scope: project
  category: writing
---

# Write Docstring

Write accurate, behavior-focused Python docstrings. Prefer numpy-style sections.
This skill is the source of truth—read the matching guide and follow it.

## Shared principles

| Do | Avoid |
| ---- | ----- |
| Describe **what** the code does | Restating the implementation |
| Explain **why** when non-obvious | Describing every line |
| Mention behavior, side effects, assumptions | Repeating names or types |
| Stay accurate as code evolves | Stale version/format detail |
| Lead with a one-line summary | Long introductory paragraphs |
| Keep the highest useful abstraction | Hot-path / infra / runbook detail |

## Workflow

1. **Classify** the target: function, class, or file/module.
2. **Read** the matching guide below (required).
3. **Inspect** the code (signature, body, callers) enough to name behavior—not to narrate it.
4. **Draft** a docstring that passes that guide's criteria.
5. **Strip** anything that will rot (version numbers, cron paths, provisioning notes, file digests).
6. **Return** the docstring ready to paste (or edit the file if asked).

## Route by target

Resolve paths relative to this `SKILL.md`.

| Target | When | Guide |
|--------|------|-------|
| Function | `def` / method docstring | [function-docstrings.md](function-docstrings.md) |
| Class | `class` docstring | [class-docstrings.md](class-docstrings.md) |
| File | Module / package docstring at top of file | [file-docstrings.md](file-docstrings.md) |

If the user asks for several targets, handle each with its own guide. If unclear which target, ask once.
