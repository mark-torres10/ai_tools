---
name: review-security
description: Applies code-security (Semgrep) and security-best-practices (OpenAI) to the current task. Use when the user asks for a security review, secure code guidance, or vulnerability check. Instructs the agent to run both skills.
disable-model-invocation: true
metadata:
  owner: mark
  scope: global
  category: security
---

# Review Security

When this skill runs, apply **both** `code-security` (Semgrep) and `security-best-practices` (OpenAI). These skills are installed in your global Cursor skills directory.

## When to Use

- User asks for a security review of code.
- User wants secure coding guidance or to check for vulnerabilities.
- User asks to "run security skills" or "apply security review".
- Implementing auth, handling user input, or touching sensitive data.

## Required Skills (Must Be Installed)

You must have both of these installed (e.g. in `~/.cursor/skills/`):

1. **code-security** (Semgrep) – OWASP Top 10 rules, Semgrep patterns, infra and secure coding.
2. **security-best-practices** (OpenAI) – Language/framework-specific security guidance and OWASP references.

If either is missing, say so and skip this skill.

## Workflow

1. **Load both skills**  
   Read `~/.cursor/skills/code-security/SKILL.md` and `~/.cursor/skills/security-best-practices/SKILL.md` (or project-level `.cursor/skills/` if present).

2. **Apply code-security (Semgrep)**  
   Follow its workflow: run Semgrep rules, OWASP checks, and any infrastructure/code patterns it specifies.

3. **Apply security-best-practices (OpenAI)**  
   Follow its workflow: identify languages/frameworks, load relevant security references, and apply its guidance.

4. **Combine findings**  
   Merge results from both skills into a single report or set of recommendations. Deduplicate where they overlap.

## Output

- **Findings** – Vulnerabilities, misconfigurations, and risky patterns from both skills.
- **Remediations** – Concrete fixes with file/line references where possible.
- **References** – Links to OWASP or other docs that apply.

## Constraints

- Do not skip either skill; both must be applied.
- Prefer evidence (e.g. Semgrep output, concrete code) over generic advice.
- If a skill cannot be found or read, state that and continue with the one that is available.
