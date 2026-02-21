Scan all markdown files in the repo, extract references to code paths and implementations, verify them against the actual codebase, and report when the markdown content is no longer true (documentation drift).

## Scope

- **Markdown files:** `**/*.md` under the repo root
- **Exclude:** `node_modules/`, `.venv/`, `docs/feature_ideas/`, `docs/weekly_updates/`, and any generated or vendored content
- **Priority areas:** `docs/`, and any `README.md` or rules files

## What to verify

For each markdown file, identify and verify:

1. **File and path references**
   - Paths in backticks, e.g. `agents/task_instructions/rules/CODING_RULES.md`
   - Paths in code blocks or "see `path/to/file`"
   - Check: Does the file exist? Has it moved or been renamed?

2. **Code references**
   - Function, class, or variable names mentioned in prose or examples
   - Check: Does the symbol exist in the referenced file? Same signature or behavior?

3. **API and endpoint references**
   - URLs, routes, e.g. `GET /v1/simulations/feed-algorithms`
   - Check: Does the endpoint exist in the codebase? Same method and path?

4. **Command references**
   - Shell commands, e.g. `uv run pytest`, `gh pr create`
   - Check: Is the command still valid? Does the script/target exist?

5. **Structural claims**
   - "The file X contains...", "We use Y for Z"
   - Folder structure diagrams, e.g. `feeds/algorithms/registry.py`
   - Check: Does the described structure match the repo?

6. **Cross-doc references**
   - Links to other markdown files, e.g. `[HOW_TO_WRITE_PR](rules/HOW_TO_WRITE_PR.md)`
   - Check: Does the target file exist? Is the link path correct?

## Output: edit markdown directly

Do NOT create a separate report file. When drift is found:

1. **Edit the affected markdown files in place** — fix broken links, update stale paths, correct claims to match the codebase.
2. **Make minimal changes** — only correct factual errors; preserve style and tone.
3. **One commit per file** (or group logically) — keep changes reviewable.

If no drift is found, no edits are needed and no report file is created.

## Grounding rules

- Use ONLY concrete repo evidence. Quote exact paths, symbols, and text.
- Do NOT invent drift; if a reference is ambiguous or unreachable, note it and skip.
- Be conservative: flag only clear factual errors (markdown says X, code does Y).
- Ignore stylistic or subjective "could be better" suggestions.
- When markdown references external repos or URLs, note them but do not fail on unreachable externals.

## PR setup

When opening a PR with direct edits:

- **PR Title:** `[YYYY-MM-DD] Codex repo automation - Markdown scan`
- **PR Description:** Automated scan of markdown vs. codebase. Drift fixed in-place in affected markdown files.

---

## Related automations & tools

This design draws from:

| Source | Description |
|--------|-------------|
| [driftcheck](https://github.com/deichrenner/driftcheck) | Pre-push hook that detects doc drift using LLMs; finds related docs from code changes and checks consistency. Conservative—flags only factual errors. |
| [awesome-codex-automations: README Freshness Check](https://github.com/onurkanbakirci/awesome-codex-automations) | Verify README and core docs are still accurate. |
| [awesome-codex-automations: API Documentation Drift](https://github.com/onurkanbakirci/awesome-codex-automations) | Detect mismatches between API docs and implementations. |
| [readme-update-check](https://github.com/mkotsollaris/readme-update-check) | CI tool to find stale documentation. |
| [stale-md](https://github.com/mkotsollaris/stale-md) | CircleCI orb to find stale markdown in CI. |
| [pystaleds](https://github.com/AloizioMacedo/pystaleds) | Checks for stale Python docstrings vs. function signatures. |

**Inclusion:** Adapted for Codex automation—full-repo scan of all markdown, verification of file paths, code references, API endpoints, commands, and structure, with PR output in this project's convention.
