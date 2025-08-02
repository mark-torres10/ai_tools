You are helping define engineering personas for an AI agent system.

You will be given a **role description** that describes a specific software engineering persona, including their focus areas, key skills, and what types of issues they are meant to catch or optimize.

Your task is to generate the **`examples`** section for this persona’s spec file, using the following YAML-compatible format:

---
examples:
  - context: <Short 1-line description of the situation or problem the user is facing>
    user: "<User request in natural language>"
    assistant: "<How the persona agent would respond to the user, demonstrating its expertise>"
    commentary: "<What this example illustrates about the persona’s priorities, skill, or judgment>"
  - context: ...
---

You must generate at least **3 examples**, ideally covering different scenarios that show the range of the agent’s skills. The tone should reflect a senior engineer giving a pragmatic, reliable answer.

Do **not** include the full spec — only output the `examples` block.

Ready? Here's the role description to generate examples for:
"""
<insert role description here>
"""
