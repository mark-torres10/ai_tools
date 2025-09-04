# Part 4g — Component Spec for Each Shot: Assets, Toolchain & MCP Hooks

Every shot needs **assets** to exist, **tools** to create them, and optionally **MCP hooks** to automate generation and QA.  
This is like the **infra + pipeline plan** for a microservice.

---

## 🎯 Goal of This Part
- Define the full **asset manifest** for each shot.  
- Map assets to **tools** in your production stack.  
- Identify **MCP servers** that can automate parts of the pipeline.  

---

## 🧩 Asset Categories

### 1. **Visual Assets**
- **UI mockups** (Figma frames, e.g., `sports_mock_v1.png`).  
- **Persona icons** (SVG/PNG, e.g., `commentator_icon.svg`).  
- **Stock b-roll** (Pexels, Artgrid, e.g., `fan_react_01.mp4`).  
- **Talking head clips** (HeyGen/D-ID neutral avatar renders).  

### 2. **Audio Assets**
- **VO lines** (ElevenLabs-generated, `shopping_avatar_tip.wav`).  
- **Music stems** (licensed, `creator_energy_intro.wav`).  
- **SFX** (subtle UI clicks, `scroll_click.wav`).  

### 3. **Text Assets**
- **Subtitles/captions** (auto-generated `.srt`).  
- **On-screen text overlays** (Figma/CapCut templates).  
- **Acceptance criteria notes** (YAML/Markdown shot spec).  

---

## 🛠️ Toolchain Mapping

- **Figma** → UI mockups, captions, icon design.  
- **Pexels/Artgrid** → authentic b-roll.  
- **Runway/Luma** → AI-generated abstract transitions.  
- **HeyGen/D-ID** → talking head clips.  
- **ElevenLabs** → VO generation (multiple takes).  
- **CapCut/Premiere** → assembly, kinetic text, final export.  
- **Audition/DAW** → optional fine audio mixing.  

---

## 🔌 MCP Hook Opportunities

- **Figma MCP** → auto-export frames & icons from design file.  
- **Pexels MCP** → search & download stock b-roll programmatically.  
- **Runway MCP** → generate N transition variants, pick top-scoring.  
- **HeyGen MCP** → render neutral avatars from scripts.  
- **ElevenLabs MCP** → batch-generate VO, enforce WPM constraint.  
- **CapCut MCP** (community) → script project assembly & export.  

---

## 📋 Example Shot Spec

**Shot ID:** Sports-1 (Fan scrolling)  
- **Assets Required:**  
  - UI mock: `sports_page_v1.png` (Figma)  
  - Persona icon: `commentator_icon.svg` (Figma)  
  - B-roll: `fan_scroll_stock01.mp4` (Pexels)  
  - User VO: `sports_user_q.wav` (ElevenLabs)  
  - Subtitles: `sports_user_q.srt`  

- **Toolchain:**  
  - Figma → export mock  
  - Pexels MCP → fetch b-roll  
  - ElevenLabs MCP → generate VO  
  - CapCut → composite assets  

- **MCP Hooks:**  
  - Auto-check VO length <12 words.  
  - Auto-check shot <3s runtime.  
  - Auto-export all files to `/shots/sports/scene1/sports-1/`.  

---

## ✅ Output of This Step
- Every shot now has an **asset manifest** + **toolchain mapping.**  
- MCP hooks enable automation for asset gen, QA, and assembly.  
- You’ve designed the creative equivalent of a **CI/CD pipeline** for shots.  

Next: in **Part 4h — Acceptance Tests & Review Checklist**, we’ll define how to test each shot’s quality and sign off for integration.
