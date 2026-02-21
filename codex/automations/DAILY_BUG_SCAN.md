Scan recent commits (since the last run, or last 24h) for likely bugs and propose minimal fixes.

Grounding rules:
- Use ONLY concrete repo evidence (commit SHAs, PRs, file paths, diffs, failing tests, CI signals).
- Do NOT invent bugs; if evidence is weak, say so and skip.
- Prefer the smallest safe fix; avoid refactors and unrelated cleanup.

When you find them, please open a PR (using the Github CLI tools). When you open a PR, please set it up in this way:

PR Title: "[YYYY-MM-DD] Codex repo automation - conventions"
PR Description: Itemized list of improvements. Note that it is from Codex automation.
Add a tag "codex" so that I know that it was from the Codex agent.
