---
name: be-more-ambitious
description: >-
  Rewrites a basic problem setup or prompt into the deeper request a
  field-leading expert would make, and returns that prompt with a short
  rationale. Does not run the task. Use when the user runs
  /be-more-ambitious. Sourced from
  https://felixrieseberg.com/how-to-be-more-ambitious-a-tutorial-for-humans-with-models/
disable-model-invocation: true
metadata:
  owner: mark
  scope: global
  category: coaching
---

# Be more ambitious

The user gives a basic problem or prompt. Rewrite it into the request a field-leading expert would make, then stop. Do not do the task.

Source: Felix Rieseberg, [How to be more ambitious: A tutorial for humans with models](https://felixrieseberg.com/how-to-be-more-ambitious-a-tutorial-for-humans-with-models/) (13 October 2026).

## When to use

The user runs `/be-more-ambitious` on a problem, prompt, or task they have not asked you to carry out.

## Do not use

- They want the task done.
- They want the same work done faster. This skill skips speed.
- They want a longer version of the same request.

## How to raise the request

Apply each part that would change the work. If one would not, say so in one clause.

**Altitude.** Name the goal beyond the goal: the outcome after this task, and what should happen next. Prefer a durable way to keep getting that outcome, including the access and data that let it run again, when the user will act on the result. Leave a creative piece whose point is the piece itself at the level they asked for. Stop before a slogan such as "go make money".

**Depth.** Ask for the work the way the best people in that field do it. Felix's prompt:

> I want a deeper version of this task, not a bigger one. Before rewriting it: (1) say what a top professional in this field would do here that I'm not asking for; (2) name the rawest material they would start from instead of what has already been digested for me; (3) name the specific methods and tools they would use; (4) say what, other than you or me, would show the result is right. Then rewrite my prompt to ask for exactly that.

Also set a harder target than the user named and treat it as solvable. Where the task depends on a belief about data, ask to check that belief on the raw record and to look for a signal the user does not already have.

**Range.** Replace the noun of the deliverable with the verb of the job. A quarterly deck is getting busy people to believe a cause-and-effect story and to decide under uncertainty. From those verbs, name other fields whose techniques would change the result, including an adversarial field when someone will trust the result or spend money on it. Skip fields that would only decorate it.

## Rules

- Name the tools and methods. Expert wording on the user's original method is the same task.
- Name the field and the technique. Ask for the work, such as the checks a short seller runs before a position. Do not ask the model to play the person.
- The rewritten prompt requires an outside judge: a tool, a held-out set, a reproduction, or another system. The model does not grade itself.
- Stay on the user's intent. Keep their constraints. If altitude would replace the task, keep the original task reachable and say what changed.
- Name the data and tools the next run needs.
- Stop after the rewrite.

## Output

### Rationale

One or two sentences each:

1. Goal beyond the goal
2. What an expert would do differently
3. Rawest inputs
4. Expert methods and tools
5. Other fields
6. Outside check

### Rewritten request

One fenced markdown block, ready to hand to an agent. It asks for the expert work, the raw inputs, the questions the user did not ask that serve their goal, and the outside check. No commentary inside the fence.

If you cannot name the field, ask one question and stop.

## Anti-patterns

- Expert vocabulary on the original method.
- A longer outline of the same task.
- "Act as a world-class X", or a cast of personas.
- "Check your own work" as the only correctness check.
- Dropping a constraint the user set.
- Starting the research, the code, or the draft.
