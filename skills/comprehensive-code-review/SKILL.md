---
name: comprehensive-code-review
description: Performs thorough code reviews using the collaborative review checklist. Use when the user asks for a comprehensive code review, collaborative review, thorough review, or structured review with per-file analysis, cross-cutting concerns, and risk assessment.
disable-model-invocation: false
metadata:
  owner: mark
  scope: global
  category: review
---

# Comprehensive Code Review

Conduct thorough code reviews following the structured checklist in `agents/task_instructions/collaborative_review/COMPREHENSIVE_CODE_REVIEW_CHECKLIST.md`.

## When to Use

- User asks for a comprehensive, thorough, or collaborative code review.
- User wants structured per-file analysis with cross-cutting concerns.
- User requests review covering testing, risks, and context.

## Path Discovery

The checklist lives inside an `ai_tools` tree. Resolve the **ai_tools root** first.

**Resolve ai_tools root in this order:**

1. **Submodule in workspace**  
   Check for an `ai_tools` directory in the workspace root (e.g. `./ai_tools/`). If it exists and contains `agents/task_instructions/collaborative_review/COMPREHENSIVE_CODE_REVIEW_CHECKLIST.md`, use it.
2. **Fallback canonical path**  
   If there is no such submodule, use: `/Users/mark/Documents/projects/ai_tools/`.

**Checklist file:** `<ai_tools_root>/agents/task_instructions/collaborative_review/COMPREHENSIVE_CODE_REVIEW_CHECKLIST.md`

Read the checklist file and apply it. If not found, ask the user for the checklist path and stop.

## Workflow

1. Resolve ai_tools root and read `COMPREHENSIVE_CODE_REVIEW_CHECKLIST.md`.
2. Use the checklist as the structure for the review:
   - Gather or infer the required inputs (key files, per-file notes, cross-cutting concerns, etc.).
   - If the user has not provided sufficient context, solicit it using the checklist items as a guide.
   - Conduct the review covering each section in the checklist.
3. Produce findings organized by the checklist sections.

## Constraints

- Do not skip checklist sections; address each or state why it does not apply.
- Prefer evidence-based findings over generic advice.
- Keep findings scoped to the user's current work and stated goal.
