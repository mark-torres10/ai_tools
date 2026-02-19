---
name: suggest-rules-additions
description: At end of conversation, analyzes the exchange to infer user preferences and suggests additions to docs/RULES.md. Use when the user asks what preferences they could add to their rules, or wants to capture practices from the conversation.
disable-model-invocation: true
metadata:
  owner: mark
  scope: global
  category: rules
---

# Suggest Rules Additions

Analyze the conversation to infer the user's preferences, practices, and decisions, then suggest concrete additions they could add to `docs/RULES.md`.

## When to Use

- User runs this at the end of a conversation to capture preferences discovered during the session.
- User asks: "Based on our conversation, what preferences could I add to docs/RULES.md?"
- User wants to evolve their rules file with learnings from the current exchange.

## Assumptions

- `docs/RULES.md` exists and contains practices and preferences.
- The user is actively maintaining it and wants to add inferred preferences.

## Workflow

1. Read `docs/RULES.md` to understand its current structure and scope.
2. Review the conversation for:
   - Repeated choices or patterns (tools, formats, conventions)
   - Explicit preferences stated or implied
   - Corrections the user made (what they wanted differently)
   - Decisions with rationale (why X over Y)
   - Style, verbosity, or workflow preferences
3. Propose specific additions: rule text + rationale (what in the conversation suggested it).

## Output Format

For each suggested addition:

- **Proposed rule** – Exact or near-exact text to add (or a clear description).
- **Rationale** – What in the conversation suggested this preference.
- **Category** – Where it might fit in `docs/RULES.md` (if sections exist).

If nothing strong emerges, say so—do not invent preferences.

## Constraints

- Base suggestions on evidence from the conversation, not generic best practices.
- Do not modify `docs/RULES.md`; only suggest. The user adds what they want.
- Prefer concrete, actionable rules over vague guidance.
