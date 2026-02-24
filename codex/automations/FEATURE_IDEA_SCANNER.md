Scan the codebase for feature ideas, improvement opportunities, and technical-debt markers embedded in code and docs.

## What to find

### 1. Markers and phrases

- **Markers**: `TODO`, `FIXME`, `HACK`, `XXX`, `NOTE`, `OPTIMIZE`, `REFACTOR`
- **Phrases**: "nice to have", "future improvement", "could add", "consider adding", "eventually", "later", "we should", "would be useful", "idea:", "missing:", "needs:", "wish:", "support for"

Include file path, line number, and the full comment or context for each item.

### 2. Proposed features by area

Scan the following code paths and propose **3 UI features**, **3 ML features**, and **3 backend features**:

| Area   | Paths                     | Count |
|--------|---------------------------|-------|
| UI     | `ui/`                     | 3     |
| ML     | `simulation/core/`, `ml_tooling/` | 3     |
| Backend| `simulation/api/`         | 3     |

For each proposed feature:

- **Title**: Short, action-oriented (e.g., "Add feed algorithm selection to ConfigForm")
- **Rationale**: What gap or opportunity the code suggests (cite file paths, patterns, or adjacent capabilities)
- **Scope**: Large (multiple PRs/tickets, e.g. 2+ backend PRs + 1 frontend PR) or small (1–2 PRs; common for UI)
- **Evidence**: Code or structure that supports the idea (e.g., existing endpoints without UI, config surfaces that could be extended)

Features may be:

- **Larger**: Multiple parts/PRs/tickets (e.g., exposing feed ranking algorithms required backend registry + typing PRs and a frontend+backend ConfigForm PR)
- **Smaller**: 1–2 PRs (especially for UI—e.g., add a select, wire an existing API to a form)

If a path does not exist, note it and propose from available paths instead.

## Output format

Write results to `docs/feature_ideas/(YYYY-MM-DD)_feature_ideas.md`:

```markdown
# Feature Ideas and Technical Debt Scan

**Scan date:** YYYY-MM-DD  
**Scope:** Full repo (or: last 7 days of commits, if scoped)

## Summary

- Total markers/phrases found: N
- By category: TODO (n), FIXME (n), feature ideas (n), etc.
- Proposed features: 2 UI, 1 ML, 1 backend

## Proposed features by area

### UI (3 features)

#### Feature 1: [Title]
- **Rationale:** ...
- **Scope:** Large | Small
- **Evidence:** `path/to/file`, patterns, etc.

#### Feature 2: [Title]
- **Rationale:** ...
- **Scope:** Large | Small
- **Evidence:** ...

...

### ML (3 features)

#### Feature: [Title]
- **Rationale:** ...
- **Scope:** Large | Small
- **Evidence:** ...

...

### Backend (3 features)

#### Feature: [Title]
- **Rationale:** ...
- **Scope:** Large | Small
- **Evidence:** ...

...

## Markers and phrases

### File: `path/to/file.ext` (line N)

**Type:** TODO | FIXME | Feature idea | Technical debt  
**Context:** (surrounding code or comment)

> Original text

---

(repeat for each item)
```

## Grounding rules

- Use ONLY concrete evidence from the repo. Quote the exact text.
- Do NOT invent items; if a match is ambiguous, note it and skip.
- Proposed features must be grounded in the scanned code paths: cite files, endpoints, patterns, or adjacent capabilities that support each idea.
- Exclude generated files, `node_modules`, `.venv`, and similar.
- For large codebases, optionally scope to files changed in the last 7 days, or to specific dirs.

## PR setup

When opening a PR with the new report:

- **PR Title:** `[YYYY-MM-DD] Codex repo automation - Feature ideas scan`
- **PR Description:** Automated scan of feature ideas and technical debt markers. Attach the report file.
- Add a Github tag "codex" so that I know that it was from the Codex agent.
