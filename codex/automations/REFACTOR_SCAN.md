You are a coding agent working in this repository. Your task is to scan the codebase and report 10 refactoring opportunities that improve clean code, correctness, testability, and maintainability, explicitly following the repo’s standards in docs/RULES.md.

Requirements:

1) Read docs/RULES.md first and treat it as the source of truth (DI, thin FastAPI routes, absolute imports, domain purity for simulation.core.models, avoid hidden globals, avoid Any, etc.).
2) Scan at least simulation/ and ml_tooling/ (you may include other folders if relevant).
3) Output exactly 10 refactoring opportunities, each with:
   - Title (short)
   - Rationale (tie to docs/RULES.md and/or clean code)
   - Exact anchor: file path + line number (file:line)
   - Proposed change (1–3 concrete steps)
   - Risk/verification notes (what to test, what could break)
4) Prefer small-to-medium refactors with clear boundaries. Avoid “rewrite the system” suggestions.
5) Be empirical: support each opportunity by pointing to real code (don’t guess).
6) Do not modify code unless explicitly asked; this run is discovery-only.

Suggested workflow (use fast tooling):

- Use ripgrep to find: relative imports, Any usage, global caches/singletons, broad exception handling, duplicated patterns in routes/services, direct I/O inside business logic, and cross-layer imports.
- Identify hot spots by file size (largest modules) and repetition.

Deliverable:

- Print the report in Markdown to stdout under the heading “Refactor Opportunities (YYYY-MM-DD)”.

Some refactors to avoid:

- Imports of lib/ to simulation/core/models: we are OK with this.
