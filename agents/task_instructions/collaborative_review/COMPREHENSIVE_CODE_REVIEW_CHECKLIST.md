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
  - [ ] Dependencies or external assumptions.  
    - *Example:* “Assumes Redis always available — no retry logic.”

- [ ] **Cross-Cutting Concerns**  
  - Highlight design patterns, abstractions, or conventions that span files.  
  - Call out areas needing consistency (e.g., error handling, logging, API contracts).  
  - *Example:* “Ensure `api.py` and `tasks.py` return errors in the same JSON format.”

- [ ] **Testing & Validation**  
  - [ ] Which files contain tests and what’s covered.  
  - [ ] What scenarios or edge cases are missing.  
  - [ ] Suggested manual or integration checks.  
  - *Example:* “`test_models.py` covers user creation, but missing duplicate email case.”  
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
