---
name: explain-as-python
description: For Python-fluent developers. Explains code in other languages (especially TypeScript) through a Python lens—teaches concepts first (e.g. what is a hook?), then execution/model and idioms, then translation or line-by-line mapping to Python. Use when the user references a code chunk or asks about code in a non-Python language and wants to understand it, learn the language, or get an idiomatic Python equivalent.
disable-model-invocation: false
metadata:
  owner: mark
  scope: global
  category: learning
---

# Explain as Python

Help a Python-fluent developer understand code written in another language (TypeScript and JavaScript are the main examples; other languages on request) by teaching concepts first, then execution/model and idioms, then mapping or translating to Python. No refactoring of the user's codebase.

## Audience

- Fluent in Python.
- Working in or reading another language (often TypeScript/JavaScript) they know less well.
- Goals: understand the code, learn the other language, and optionally see an idiomatic Python equivalent and tradeoffs.

## When to Use

- User references a code chunk or file and asks to explain it "as a Python dev" or "like I know Python."
- User asks what a construct or concept means (e.g. "what's a hook?", "what's optional chaining?").
- User wants a snippet translated to Python and explained (idioms, execution model, pros/cons).
- User asks about execution or code model (compile vs runtime, type checking, module system) and how it differs from Python.

## Teaching Order

Always teach **concepts before implementation** when the code uses unfamiliar ideas:

1. **Concept** – What is it? (e.g. "A React hook is…"). One short paragraph, then how it maps to or differs from Python (e.g. "In Python you'd typically…").
2. **Execution / code model** – How does this run? (compiled vs interpreted, when types are checked, single-threaded vs event loop, module loading). Contrast with Python where it helps.
3. **Idioms and quirks** – Language-specific habits and gotchas (e.g. `null` vs `undefined`, `==` vs `===`, optional chaining). Brief, with Python analogues.
4. **Code** – Walk the actual snippet or give an idiomatic Python equivalent (or both). Tie each choice back to the concepts and idioms above.

If the user only asks one part (e.g. "what's a hook?"), answer that part in depth; don't force the full sequence.

## Output Shape

- **Flexible by request.** If the user wants only a concept explanation, only a translation, or only execution model, do that. If they don't specify, default to: concept (if needed) → execution/model → idioms → code/translation → short pros/cons (original vs Python) where relevant.
- When translating to Python: give idiomatic Python, then 2–4 bullets on "what changed and why" or "lost in translation" (what the original language does that Python doesn't mirror exactly).

## What to Include (as relevant)

- **Concept glossary** – For constructs (hooks, decorators in TS, promises, etc.): definition, then Python analogue or contrast.
- **Execution model** – Compilation, type checking (compile- vs runtime), module system, concurrency model. Compare to Python.
- **Idioms** – e.g. `null`/`undefined`, optional chaining, `===`, structural typing. One line each plus Python equivalent where it exists.
- **Translation** – Idiomatic Python equivalent; when something doesn't map cleanly, say so.
- **Pros/cons** – Short comparison: strengths/costs of the original vs the Python version (e.g. type safety at compile time vs runtime flexibility).

## Constraints

- **No refactoring.** Do not modify the user's repo or files. Explain, translate in the reply, and teach only.
- **Anchor in Python.** Assume Python is the mental model. Explain the other language by contrasting with or mapping to Python.
- **Don't over-explain Python.** Assume the user knows Python; focus on the other language and the mapping.
- **Prefer teaching.** Err on the side of teaching concepts and rationale, then the specific code.

## Example Triggers

- "Explain this TypeScript like I'm a Python dev."
- "What's a hook? [with or without code]"
- "Translate this to Python and tell me what's different about how TypeScript does it."
- "What's the execution model of this code (compile vs runtime) and how would it differ in Python?"
- "What are the idioms here (e.g. null/undefined) and how do they map to Python?"
