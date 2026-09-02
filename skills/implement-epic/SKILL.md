---
name: implement-epic
description: >-
  Implements an existing GitHub epic as a stacked PR: one PR per child issue, via gh stack. The current agent is the epic manager and spawns one fresh orchestrator per child. Use when the user runs /implement-epic, or asks to take a container issue to stacked PRs.
disable-model-invocation: true
metadata:
  owner: mark
  scope: global
  category: execution
---

# Implement Epic

Take an existing GitHub epic to a **stacked implementation**. One **child issue** is one **PR**. You are the **epic manager**. You do not write product code. You do not file issues. You do not merge. You do not open the docs-only plan PR from `create-epic`.

You do not run `/implement-from-spec`. Per child, the orchestrator writes a one-PR plan with `/create-implementation-plan`, then ships it with `/implement-plan-and-open-pr`. That skill uses `/implement-from-spec` for coding.

Do not use this skill unless the user explicitly rund `/implement-epic` or named it.

## When to Use

- The user runs `/implement-epic`.
- The user wants a GitHub container issue (with children) implemented as stacked PRs.

## Do Not Use

- Filing the epic or children — use `create-epic`.
- One plan, one PR, no stack — use `implement-plan-and-open-pr`.
- Per-step approval before commit — use `interactive-implementation`.

## Using `delegate-work-to-subagents`

Follow `/delegate-work-to-subagents`, with these notes:

- You (epic manager) spawn **one fresh orchestrator per child** (`generalPurpose`, `model: inherit`). No prior chat. Sequential. Never two children at once.
- Each per-PR orchestrator then follows `delegate-work-to-subagents` for research, implementation, QA, verification, and synthesis. Leaf subagents stay Composer 2.5 (`model: composer-2.5`).
- Only those per-PR orchestrators spawn leaf subagents. Leaves must not spawn anyone.
- You are the only agent that talks to the user. You keep the user updated on each step of the process and manager agents report up to you.

## Notes when using `/create-implementation-plan`

When the per-PR orchestrator runs `/create-implementation-plan`:

- Kickoff `go` is the plan confirm. Do not wait for a per-child draft accept.
- Still write the plan, then run `plain-writing`, then `review-for-simplicity`. Apply obvious cuts.
- The plan must be independently mergeable as one PR.
- Stop and ask (manager reports to the user) if research finds an open design choice, or if simplicity review wants to drop something the GitHub issue requires.

## Notes when using `/implement-plan-and-open-pr`

When the per-PR orchestrator runs `/implement-plan-and-open-pr`:

- Stay on the current `gh stack` branch. Do not create a new branch off the default branch (skip that skill's "if on main, create a feature branch").
- Do not `gh pr create`. Open the PR with `gh stack submit --open`.
- `write-pr-description`, `write-docstring`, `write-changelog`, and the post-PR review subagents already run inside `/implement-plan-and-open-pr`. Do not run them again after it returns.
- Do not run `/implement-from-spec` here. `/implement-plan-and-open-pr` does that.

## Workflow

```
Epic progress:
- [ ] 1. Resolve repo and parent
- [ ] 2. Ensure gh stack
- [ ] 3. Propose (wait)
- [ ] 4. For each child: layer, orchestrate, CI, checkpoint
- [ ] 5. Print the table and stop
```

### 1. Resolve repo and parent

Need a parent issue URL with **children already filed** (create-epic output, or equivalent). List children: sub-issues of the parent; if that API fails, parse `## Children` in the parent body. Order: `## Children` list order when present.

If there are no children, stop. Tell the user to run `create-epic`. Do not skip or adopt existing PRs.

Do not edit the parent issue body. Local plan files are optional context. You may read temp files (including ones the user will delete). Never cite them.

If the worktree is dirty in a way that would mix unrelated edits into the stack, stop.

### 2. Ensure gh stack

If `gh stack` is missing: `gh extension install github/gh-stack`.

Default branch: `gh repo view` (trunk for the stack).

### 3. Propose, then wait

Orchestrator only. Do not `gh stack init` yet.

Branch name: `epic-{parent}-{child}-{slug}`. Slug from the child title: lowercase, hyphens, no punctuation, cap length.

```markdown
| Issue | Title | Branch | Base | Status |
| --- | --- | --- | --- | --- |
| {parent URL} | {parent title} | — | — | tracking only |
| {child URL} | {child title} | `epic-{parent}-{child}-{slug}` | {default branch or previous branch} | todo |
```

Parent is row 1. Children in implementation order. No extra proposal file.

**Approval:** `yes` / `lgtm` / `go` means start. Apply title/order edits from that reply. Show a second proposal only if the **set** of children changed.

### 4. Each child

One child at a time, in approved order.

**Manager, before the orchestrator:**

- First child: `gh stack init --base {default} {branch}` (names so it never prompts).
- Later child: `gh stack add {branch}` from the current stack top.

Then spawn **one** per-PR orchestrator. It does not talk to the user. Give it: owner/repo, parent number, child number/URL/title/body, branch name, cited step file if any, the notes in this skill, and what to return.

**Per-PR orchestrator must:**

1. Read `create-implementation-plan` and run it for this child. Input: child issue body and any cited step file. New plan files ship **in this branch**. Notes above apply.
2. Edit that plan with `plain-writing`, then `review-for-simplicity`. Notes above apply.
3. Read `implement-plan-and-open-pr` and run it. Notes above apply. That includes `/implement-from-spec`, `write-docstring`, verification, `write-pr-description`, `write-changelog`, `gh stack submit --open`, and the post-PR review subagents.
4. `gh pr edit` so the body includes `Fixes #{child}` and `Part of #{parent}`. Never a closing keyword on the parent.
5. Return to the manager only: PR URL, branch, title, verification, review notes worth reading, blockers.

**Manager, after it returns:**

Wait until GitHub checks finish (`gh pr checks --watch` when checks exist). No checks → continue. Any failing check → **stop** (do not start the next child). Green → next child.

Do not skip a failed child. Leave already-opened PRs as they are.

**Checkpoint** (short, after each child):

```markdown
{child issue URL} → {PR URL}
CI: green | none | red (stopped)
Next: {next child title} | done | stopped
```

### 5. Print the table and stop

```markdown
| PR or issue | Title | What's accomplished |
| --- | --- | --- |
| {parent issue URL} | {parent title} | tracking only |
| {child PR URL} | {PR title} | {what that PR ships} |
```

Parent first, then children in stack order. Under the table: `gh stack view` order if available, review notes worth reading, remaining children if you stopped.

Stop. Do not merge. Do not edit the parent issue.
