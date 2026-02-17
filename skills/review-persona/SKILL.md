---
name: review-persona
description: Reviews current work using a selected persona from agents/personas. Use when the user asks for persona-based review, expert-lens critique, or domain-specific code assessment.
disable-model-invocation: true
metadata:
  owner: mark
  scope: global
  category: review
---

# Review Persona

Run a structured review of the user's current work using a specific persona from `agents/personas/`.

## When to Use

- User asks for a review "as" a persona.
- User wants domain-specific critique of code, architecture, or experiments.
- User asks to route to the best persona and review with that lens.

## Inputs

- Optional explicit persona path or persona name from the user.
- Current workspace context (open files, staged/unstaged changes, relevant artifacts).

## Path Discovery

Personas live inside an `ai_tools` tree. Resolve the **ai_tools root** first, then use `agents/personas/` under it.

**Resolve ai_tools root in this order:**

1. **Submodule in workspace**  
   Check for an `ai_tools` directory in the workspace root (e.g. `./ai_tools/`). If it exists and contains `agents/personas/`, use it. Paths are always relative to this ai_tools root (e.g. `./ai_tools/agents/personas/` from workspace).
2. **Fallback canonical path**  
   If there is no such submodule, use: `/Users/mark/Documents/projects/ai_tools/`.

**Personas directory:** `<ai_tools_root>/agents/personas/`

If neither location yields a valid `agents/personas/` directory, ask the user for the personas directory and stop.

## Persona Selection

1. If the user explicitly names a persona file, use it.
2. Otherwise, check for `router.md` files under the personas tree and route by task intent.
3. If multiple personas fit, choose up to 2 and state why.
4. If no match, report "no strong persona match" and ask whether to proceed with closest candidate.

## Review Workflow

1. Read selected persona file(s) completely.
2. Collect current work context:
   - prioritized changed files or active files
   - tests, docs, and config touched
3. Evaluate using persona-specific standards:
   - correctness and failure modes
   - architecture and maintainability tradeoffs
   - performance/scalability concerns
   - observability/testing gaps
4. Produce findings ordered by severity.

## Output Format

Return:

1. **Persona Used**
   - Persona file path(s)
   - Why selected
2. **Findings (highest severity first)**
   - Issue
   - Impact
   - Recommended fix
3. **Open Questions / Assumptions**
4. **Suggested Next Actions**

If no material issues are found, say that explicitly and list residual risks/testing gaps.

## Constraints

- Do not invent persona capabilities not present in the persona file.
- Prefer concrete, evidence-based findings over generic advice.
- Keep findings scoped to the user's current work and stated goal.
