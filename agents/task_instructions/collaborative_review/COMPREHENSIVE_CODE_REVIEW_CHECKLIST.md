# 🔍 Comprehensive Code Review Agent Checklist

Please provide the following so I can perform a thorough review:

- [ ] **Key Files & Review Order**  
  - List the key files to examine.  
  - Specify the order and why it matters.  
  - *Example:* “Start with `config.py` (sets constants), then `database.py` (schema), then `api.py` (uses both).”

- [ ] **Per-File Notes**  
  For each file, provide:  
  - [ ] Purpose and role in the system.  
    - *Example:* “`handlers.py` manages HTTP routes → business logic.”  
  - [ ] Critical sections to inspect (functions, classes, blocks).  
    - *Example:* “Check `UserManager.create_user()` — touches DB, hashing, validation.”  
  - [ ] Pitfalls or tricky logic.  
    - *Example:* “Pagination in `query_posts()` — check for off-by-one errors.”  
  - [ ] Defensive checks for cases the call sites or types already rule out: extra null or type checks, `try`/`except` that swallows errors, fallbacks, and retries. Validate at boundaries, trust internal invariants, and fail loudly.  
    - *Example:* “`save_user()` catches `TypeError` and returns `None`, but every caller already passes a `User`.”  
  - [ ] Dead paths: unreachable branches, unused parameters, options, or flags, commented-out code, and leftover helpers.  
    - *Example:* “`use_v1` is never passed, and `_format_v1()` is only referenced from a comment.”  
  - [ ] Single-use temporaries that only rename an expression, leftover debug variables, and accumulate-then-return that can be inlined. Keep a name when it adds clarity.  
    - *Example:* “`result = build_row(user)` is returned on the next line — return `build_row(user)`. Keep `cents` when the name explains the conversion.”  
  - [ ] Dependencies or external assumptions.  
    - *Example:* “Assumes Redis always available — no retry logic.”

- [ ] **Cross-Cutting Concerns**  
  - Highlight design patterns, abstractions, or conventions that span files.  
  - Flag an interface, wrapper, factory, base class, or config layer with one caller or one implementation when it has no concrete purpose, such as a public API boundary, dependency-injection or test seam, framework contract, or invariant. Prefer the direct version only when the abstraction adds no such value.  
  - *Example:* “`Storage` only forwards to `S3Storage`, has no boundary or seam purpose, and has one caller — call the client directly.”  
  - Call out areas needing consistency (e.g., error handling, logging, API contracts).  
  - *Example:* “Ensure `api.py` and `tasks.py` return errors in the same JSON format.”

- [ ] **Testing & Validation**  
  - [ ] Which files contain tests and what’s covered.  
  - [ ] What scenarios or edge cases are missing.  
  - [ ] Tests that cannot fail or only restate the implementation: a mock returning what it was told, an expected value recomputed with the same code, or a constant asserted equal to itself.  
  - [ ] Suggested manual or integration checks.  
  - *Example:* “`test_models.py` covers user creation, but missing duplicate email case.”  
  - *Example:* “`test_get_user` sets `mock.return_value = user`, then asserts only that same `user`, without checking the dependency call.”  
  - *Example:* “Manually test concurrent writes to `update_balance()` for race conditions.”

- [ ] **Risks & Tradeoffs**  
  - [ ] Known fragile areas or compromises.  
  - [ ] Potential security, performance, scalability, or maintainability issues.  
  - *Example:* “Blocking DB calls may cause performance issues under load.”  
  - *Example:* “Password hashing with SHA256 instead of bcrypt — security risk.”

- [ ] **Context**  
  - [ ] Background assumptions, constraints, or design decisions.  
  - [ ] Style/architectural conventions to keep in mind.  
  - *Example:* “Using SQLite now, but schema designed for Postgres compatibility.”  
  - *Example:* “PEP8 + Google docstrings are expected.”
