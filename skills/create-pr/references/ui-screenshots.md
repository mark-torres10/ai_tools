# UI screenshots (gated)

Read this when the PR changes UI / frontend paths (`ui/` or equivalent).

## Required

Include before and after screenshots from the plan asset folder when they exist:

`docs/plans/<folder>/images/before/` and `docs/plans/<folder>/images/after/`

Place under `## Details` (or as sibling sections if Details already exists for multi-step):

```markdown
### State (Before)

![Sign-in required](docs/plans/2026-02-20_auth_phase1_gate_app_382915/images/before/sign_in_prompt.png)

### State (After)

![Authenticated sidebar](docs/plans/2026-02-20_auth_phase1_gate_app_382915/images/after/sidebar_user.png)
```

Or reference the folder:

`Screenshots: docs/plans/<folder>/`

## If screenshots are missing

Prompt the user for instruction. Do not invent image paths or skip silently when UI changed.

## Phase 2 checklist (UI)

- [ ] UI change detected
- [ ] Before/after images linked, folder referenced, or user prompted
- [ ] No fabricated screenshot paths
