# Merge Danger (required on every PR)

Adapted from [mattpocock/skills — engineering/pr](https://github.com/mattpocock/skills/blob/main/skills/engineering/pr/SKILL.md).

Every PR description **ends** with **Merge Danger**. Do not omit it. A two-way door with a narrow blast radius is still worth stating.

## Door

**Two-way:** Revert is cheap and complete—typical cases are code-only behavior, a feature flag, docs, a prompt change, or an eval config.

**One-way:** Revert is expensive or incomplete—migrations, deleted or rewritten stored data, a breaking public contract, or an external side effect that already happened.

The type guide may spell out what one-way usually means for that kind of PR (for example schema changes on features, or data backfills on bugs).

## Blast radius

One short phrase for the scope of harm, then one or two sentences on what actually breaks if this is wrong. Skip the sentences when the phrase is already specific (for example “staging-only export queue”).

## Output shape

```markdown
## Merge Danger

**Door:** one-way | two-way

<optional: why this can or cannot be reverted cleanly>

**Blast radius:** <short phrase>

<optional: who or what is affected if this is wrong>
```

Omit optional lines when they only repeat the label.
