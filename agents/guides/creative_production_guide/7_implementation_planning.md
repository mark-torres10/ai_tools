# Part 7 — Implementation Planning (Resourcing)

Now that we’ve designed beats, shots, emotions, and transitions, it’s time to plan **implementation**.  
This is the equivalent of **infra + resourcing** in a system design doc.

---

## 🎯 Goal of This Part
- Map each shot to the **assets** it requires.  
- Assign **tools** and **roles** responsible for generating those assets.  
- Define where automation (MCP hooks) can reduce effort.

---

## 🧩 Resource Planning Dimensions

### 1. **Assets Required**
- UI mockups (Figma exports).  
- Persona icons (stylized SVGs).  
- Stock b-roll (Pexels, Artgrid).  
- Talking head clips (HeyGen/D-ID).  
- VO files (ElevenLabs).  
- Music + SFX (Epidemic Sound, Soundstripe).  
- Subtitles/captions.  

### 2. **Tool Assignments**
- **Figma** → UI, captions, persona icons.  
- **Pexels/Artgrid** → human b-roll.  
- **Runway/Luma** → AI transitions.  
- **HeyGen/D-ID** → avatar shots.  
- **ElevenLabs** → VO (scripted + variants).  
- **CapCut/Premiere** → assembly, text animation.  

### 3. **Roles**
- **Creative Engineer (you):** Owns pipeline, specs, assembly.  
- **Designer (optional):** Polishes icons, typography.  
- **VO Editor (optional/AI):** QA pacing and clarity.  
- **Reviewer:** Signs off on acceptance tests.  

### 4. **Automation (MCP Hooks)**
- **Figma MCP:** Auto-export frames/icons.  
- **Pexels MCP:** Search + fetch b-roll candidates.  
- **Runway MCP:** Generate 2–3 transition variants.  
- **HeyGen MCP:** Render talking head clips.  
- **ElevenLabs MCP:** Generate VO, enforce WPM.  
- **CapCut MCP:** Auto-assemble timeline skeleton.  

---

## 📋 Example Resource Table

| Beat | Shot ID | Assets | Tools | Role | MCP Hooks |
|------|---------|--------|-------|------|-----------|
| Sports | Sports-1 | UI mock, fan b-roll, user VO | Figma, Pexels, ElevenLabs | You | Figma MCP, Pexels MCP |
| Sports | Sports-2 | Avatar icon, avatar VO, overlay | Figma, ElevenLabs | You | Figma MCP, ElevenLabs MCP |
| Shopping | Shop-1 | B-roll (mirror), UI frame, VO | Pexels, Figma | You | Pexels MCP |
| Gaming | Game-2 | Gamer avatar, VO, patch UI | Figma, ElevenLabs | You | Figma MCP, ElevenLabs MCP |
| Marketplace | Market-1 | Multiple b-rolls, avatar icons | Pexels, Runway | You | Pexels MCP, Runway MCP |
| CTA | CTA-1 | Logo lockup, music stem | Figma, CapCut | You | Figma MCP |

---

## ✅ Output of This Step
- Every shot is now mapped to **assets, tools, roles, and automation points.**  
- This is the equivalent of your **infra + resourcing plan**.  
- Gives clarity on what needs to be built, who/what builds it, and how.  

Next: in **Part 8 — Iteration & Versioning**, we’ll treat the storyboard like a codebase, define versions, and set up workflows for revision and improvement.
