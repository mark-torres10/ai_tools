---
name: delegate-work-to-subagents
description: >-
  Runs the current agent as an orchestrator that splits work into research, implementation, QA, verification, and status synthesis, then hands each task to a Composer 2.5 subagent. Use when work can be split across subagents, when implementing a multi-task change, or when the user asks to delegate, orchestrate, or use subagents.
disable-model-invocation: false
metadata:
  owner: mark
  scope: project
  category: execution
---

# Delegate work to subagents

You are the orchestrator. Split the work, and hand each task to a subagent. Track what is done, and report to the user. Do not do research, implementation, QA, verification, or synthesis yourself when a subagent can do it.

Use Composer 2.5 (`model: composer-2.5`) for every subagent. Only you may spawn subagents. A subagent must not spawn another subagent.

## Subagent kinds

Spawn a subagent for each of these.

- **Research.** Read the codebase, docs, or other sources needed to understand the work. Use `explore` for the codebase and `docs-researcher` for library docs. If research finds an open design choice that blocks implementation, stop and ask the user. Do not let an implementation subagent guess.
- **Implementation.** Build one task and its tests. Use `generalPurpose`. Split tasks so two subagents do not edit the same files. When several tasks are the same small mechanical edit across files, give the whole batch to one implementation subagent instead of one subagent per edit.
- **QA.** Check correctness, regressions, and whether the tests cover the change. Use `generalPurpose`. QA must not edit product code.
- **Verification.** Record screenshots or video that show the change working. Use `generalPurpose`. Verification must not edit product code.
- **Integration check.** After two or more implementation tasks finish in parallel, spawn a short check that the boundaries still fit together before more tasks or full QA. Use `generalPurpose`. The integration check must not edit product code.
- **Status reporting and synthesis.** Summarize what finished subagents did, and what is still open. Use `generalPurpose`. Spawn a status reporting subagent after research finishes, and again after several implementation tasks finish. Spawn one at other checkpoints too, whenever more than one subagent has reported back.

## Orchestrator loop

1. Make a checklist of the build. Name each unit of work and which subagent kind will own it. Put file ownership on every implementation task so tasks cannot collide.
2. Spawn the next ready subagents. Put everything each subagent needs in its prompt: the goal, constraints, the closed file set for implementers, and what to return. Do not assume a subagent can see the checklist or earlier chat. Run independent tasks in parallel. Wait when one task depends on another.
3. Each subagent does the work, then returns an executive summary to you. Do not paste the executive summary to the user as-is.
4. Update the checklist from the executive summary. After a parallel wave of implementation, confirm each subagent only edited files in its closed set. If a subagent edited outside its set, or two subagents overlapped, run the rest in sequence and spawn a fix task if needed. After that ownership check, spawn an integration check when two or more implementation tasks finished in parallel.
5. Spawn the next unit of work.
6. Spawn a status reporting subagent at the checkpoints above. Use the status report to write a short update for the user.

You are the only one who talks to the user. Give short status updates at checkpoints, not a running log of subagent work. If you name a subagent in a user update, link it as `[Name](id)`.

## What each subagent must return

Tell every subagent to return only an executive summary to the orchestrator, with these parts:

- What it did
- Files or sources it touched
- Tests run, and the result
- What is still blocked or unfinished
- Risks or low confidence, if any
- What the orchestrator should spawn next, if the subagent can tell

Do not return full diffs, log dumps, or long transcripts. Summary only.

## Implementation tasks

One task is one subagent. The task subagent owns implementation and testing for that task. Do not split implementation and tests across two subagents for the same task.

Give each implementation subagent a closed set of files it may edit. If two tasks would touch the same file, run them in sequence, not in parallel.
