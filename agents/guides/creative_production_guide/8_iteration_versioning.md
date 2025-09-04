# Part 8 — Iteration & Versioning

Just like a codebase, a trailer evolves through drafts.  
This part defines how to **version, iterate, and track changes** to the storyboard and assets.

---

## 🎯 Goal of This Part
- Treat the storyboard as a **living document** with versions.  
- Establish a workflow for **iteration** (drafts, feedback, refinements).  
- Ensure changes are tracked, reversible, and comparable.

---

## 🧩 Versioning Principles

### 1. Semantic Versioning for Drafts
- **v0.x** = Rough storyboard (no assets yet).  
- **v1.x** = First animatic (timed storyboard with temp audio).  
- **v2.x** = Beta trailer (real assets, still rough).  
- **v3.x** = Release candidate (final polish pass).  
- **v3.0** = Final cut.  

### 2. Change Tracking
- Log changes at shot-level: what script/asset/timing was adjusted.  
- Keep notes in Markdown or YAML alongside the shot spec.  
- Example:  
  ```yaml
  shot_id: Sports-2
  version: v1.1
  change: trimmed VO from 14 → 10 words for pacing
  reviewer: MTorres
  date: 2025-09-04
  ```

### 3. File Organization
- Use a consistent folder structure:  
  ```
  /trailer_project/
    /storyboard_specs/
    /shots/
      /sports/
        /sports-1/
        /sports-2/
      /shopping/
      /gaming/
    /renders/
      /drafts/
      /final/
  ```

---

## 🔁 Iteration Workflow

1. **Storyboard Draft (Paper/Markdown):** v0.x  
2. **Animatic (timed storyboard with placeholder audio):** v1.x  
3. **Beta Cut (b-roll + placeholder VO):** v2.x  
4. **Polish Pass (real VO, transitions, music):** v2.5+  
5. **Final Review + Export:** v3.0  

At each stage:  
- Run acceptance tests.  
- Review emotional arc.  
- Collect feedback.  
- Log changes.  

---

## ⚡ Automation Aids
- Use **Git/GitHub** for versioning shot specs and Markdown docs.  
- Store renders in cloud (Google Drive, Dropbox, or Git LFS for binaries).  
- Have AI agents auto-generate changelogs from diffs (e.g., “VO trimmed, duration shortened by 1.2s”).  

---

## ✅ Output of This Step
- Trailer development is now **version-controlled and iterative.**  
- Each cut is traceable, reversible, and reviewable.  
- Ensures structured progress from v0.x → v3.0.  

Next: in **Part 9 — Evaluation & Testing**, we’ll formalize the QA process at the trailer level (not just shot level), including emotional arc validation and conversion goals.
