---
name: review-for-simplicity
description: Reviews plans, proposals, and code changes for unnecessary complexity, unverified assumptions, and premature abstraction. Use when the user asks to simplify a plan, challenge a proposal, narrow scope before implementation, pressure-test whether a design is overengineered, or review a diff for avoidable complexity. Slash-only.
disable-model-invocation: true
metadata:
  owner: mark
  scope: project
  category: review
---

# Review For Simplicity

Run a skeptical but fair review that pushes toward the smallest solution that can ship safely now.

## When to Use

- User asks to simplify a plan, proposal, architecture, or implementation approach.
- User wants pushback on complexity before coding starts.
- User wants a generated plan reviewed before execution.
- User wants a diff or PR reviewed for avoidable abstraction, extra layers, or speculative design.
- User asks questions like:
  - "Is this overengineered?"
  - "What can we cut?"
  - "What's the simplest version of this?"
  - "Challenge this plan."
  - "Pressure-test this proposal."

## Do Not Use

- Do not use for broad brainstorming where the user wants many options rather than narrowing.
- Do not use as a generic code review when correctness, bugs, or security are the main concern.
- Do not default to this skill automatically for all planning or design tasks.
- Do not turn the review into a combative takedown. The goal is simplification, not rhetoric.

## Inputs

- A plan, proposal, design note, markdown file, diff, PR, or code change.
- Optional constraints from the user:
  - timeline
  - staffing
  - risk tolerance
  - explicit non-functional requirements

## Review Goal

Determine whether the proposed solution is justified by the actual need, and recommend the narrowest version that can be shipped safely now.

Default bias:

- Prefer fewer moving parts.
- Prefer fewer files and concepts.
- Prefer concrete present requirements over future possibilities.
- Prefer deleting, collapsing, or deferring abstractions unless they protect a real current invariant.
- Prefer a narrower first version when it preserves the core user value.

## Review Workflow

1. Identify the actual goal.
   - Separate the user's real outcome from the proposed solution.
   - Restate the problem in plain language before judging the design.
2. Check evidence vs. assumption.
   - Mark which requirements are explicit.
   - Mark which claims are inferred, speculative, or unsupported.
3. Inventory the complexity being introduced.
   - Extra models
   - Extra classes or services
   - Extra layers or abstractions
   - Extra coordination or orchestration
   - Extra configuration, schema, or rollout machinery
4. Ask whether each piece is needed now.
   - What concrete present requirement does it satisfy?
   - What breaks if it is removed?
   - Is it solving a real second use case, or a hypothetical one?
5. Look for a smaller shape.
   - Can multiple concepts collapse into one?
   - Can a generic interface become one concrete implementation?
   - Can a new subsystem become a helper in an existing module?
   - Can the first version support one narrow path instead of a generalized framework?
6. Recommend the simplest viable approach.
   - If the current proposal is fine, say so.
   - If it is too broad, explain exactly what to cut, defer, or merge.

## Follow-Up Question Policy

- Ask follow-up questions only when the answer would materially change the recommendation.
- Prefer 1-3 questions, not a long interview.
- Ask before giving a strong verdict if any of these are unclear:
  - the actual user need
  - hard constraints
  - whether an extra abstraction protects a real invariant
  - whether a future-facing requirement is already committed

## What to Look For

Flag these as potential complexity tax unless justified:

- abstractions without a concrete second use case
- interfaces with only one implementation
- multiple data models where one would do
- coordination layers for single-path flows
- configuration systems for one or two values
- plugin or strategy frameworks without active variation
- premature caching, queuing, retries, or distribution
- splitting work across too many components when a local change would suffice
- implementation detail elevated into architecture

## Output Format

Return a compact memo with these sections:

1. **Bottom line**
   - Short paragraph with overall assessment.
   - Use one of:
     - `acceptable`
     - `simplify first`
     - `not justified yet`
2. **What seems solid**
   - Brief bullets for the parts that are actually grounded.
3. **What seems unproven or overbuilt**
   - Brief bullets naming specific complexity and why it is not yet justified.
4. **Simpler version I would ship**
   - Concrete narrower alternative.
   - Name what to cut, merge, defer, or keep.
5. **Follow-up questions**
   - Include only if needed.

## Response Rules

- Be skeptical but fair.
- Do not praise complexity for being "robust" unless the constraints clearly require it.
- Do not hide behind generic advice like "apply YAGNI" without naming the exact excess.
- Always point to the specific abstraction, model, layer, or mechanism that seems unnecessary.
- Always propose a simpler concrete alternative when criticizing.
- Keep the response moderately concise.
- If the proposal is already appropriately small, say so plainly and name the constraints that justify it.

## Integration Guidance

- After `create-implementation-plan`: use this to challenge the plan before implementation starts.
- Before `implement-plan-and-open-pr`: use this if the plan seems broad, assumption-heavy, or future-proofed.
- On a diff or PR: use this to identify avoidable abstractions or machinery that slipped into implementation.

## Example

**User input:**

```text
/review-for-simplicity Review this plan. We need to enable one internal-only feature.
My plan is to add a FeatureFlag model, a FeatureFlagAssignment model, a
FeatureFlagResolver service, a cache, an admin abstraction for future
multi-tenant support, and a rollout strategy interface.
```

**Good response shape:**

```markdown
## Bottom line

`simplify first`

The requirement appears narrow: enable one feature for a known internal cohort.
The current plan introduces several domain objects and extension points that may
be reasonable later, but are not yet justified by the stated need.

## What seems solid

- A central feature check is likely useful.
- Default-off behavior and targeted enablement are real requirements.

## What seems unproven or overbuilt

- Separate assignment and resolver layers are not yet justified for a single rollout path.
- Caching looks premature for a tiny flag set with no demonstrated performance issue.
- Multi-tenant support is described as future-facing, not current.
- A rollout strategy interface adds abstraction before there are multiple real strategies.

## Simpler version I would ship

Start with one persisted flag store plus one concrete helper such as
`is_feature_enabled(user, feature_name)`. Skip caching, strategy interfaces, and
extra domain layers until a second real use case forces them.

## Follow-up questions

- Do non-engineers need to edit flags immediately?
- Is there already a second rollout mode beyond internal users?
```

## Constraints

- Favor present-tense evidence over hypothetical future needs.
- Prefer recommending a narrow first slice over a general framework.
- Do not expand into a long architecture essay unless the user asks for depth.
