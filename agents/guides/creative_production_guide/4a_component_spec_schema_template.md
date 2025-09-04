# Part 4a — Component Spec for Each Shot: Schema & Template

Now that we’ve defined beats, scenes, and shots, we need a **consistent schema** to spec each shot.  
Think of this as the **YAML/JSON contract** for a shot, similar to how you’d define a service in a PRD.

---

## 🎯 Goal of This Part
- Create a reusable **template** for defining every shot.  
- Ensure each shot has clear **purpose, inputs, outputs, constraints, failure modes, and acceptance criteria.**  
- Make the spec structured enough for both **humans and AI agents** to process and evaluate.

---

## 🧩 Schema Structure

Here’s the recommended schema for a shot:

```yaml
id: Unique identifier (e.g., Sports-1)
beat: Which beat this shot belongs to (e.g., Sports Use Case)
scene: Scene grouping (e.g., Sports Scene)
name: Descriptive label (e.g., Fan scrolling, frustrated)
purpose: Why this shot exists (role in narrative arc)
inputs:
  visuals: [actors, props, setting, UI mockups, avatars, icons]
  audio: [user VO lines, avatar VO lines, SFX, music cues]
outputs:
  emotional: What the audience should feel (e.g., curiosity, delight)
  narrative: What the audience should understand (e.g., “team bench outperformed”)
constraints:
  duration: time budget in seconds
  style: Apple-polished, creator-energy, etc.
  tone: relatable, inspirational, playful
failure_modes:
  - How the shot could fail (e.g., VO too long, emotion doesn’t land)
  - How failure impacts flow (e.g., loss of trust, pacing breaks)
acceptance_criteria:
  - Measurable check #1 (e.g., “viewer can retell the info in one sentence”)
  - Measurable check #2 (e.g., “shot <5s duration”)
assets_required:
  - Figma UI frame name
  - Persona icon (SVG)
  - B-roll filename
  - VO file (ElevenLabs ID)
tools_pipeline:
  - Figma → export frame
  - Pexels → fetch b-roll
  - ElevenLabs MCP → generate VO
  - CapCut/Premiere → edit & composite
```

---

## 📋 Example (Filled Out)

```yaml
id: Sports-1
beat: Sports Use Case
scene: Sports Scene
name: Fan scrolling, frustrated
purpose: Show relatable pain point and set up avatar solution
inputs:
  visuals:
    - Actor scrolling laptop with generic sports score mockup
    - UI frame: sports_page_v1.png
  audio:
    - User VO: "Who even played well in this game?"
outputs:
  emotional: Curiosity, recognition
  narrative: Viewer understands the “problem” (stats are confusing)
constraints:
  duration: 3s max
  style: Clean, Apple-esque
  tone: Relatable, authentic
failure_modes:
  - Actor feels staged → no empathy from viewer
  - VO unclear → problem not understood
acceptance_criteria:
  - Audience recognizes confusion/problem in <3s
  - Shot duration <= 3s
assets_required:
  - Figma frame: sports_mock_v1
  - Persona icon: commentator_icon.svg
  - VO clip: sports_user_q.wav
tools_pipeline:
  - Figma MCP → export frame
  - ElevenLabs MCP → generate VO
  - CapCut → composite actor + UI overlay
```

---

## ✅ Output of This Step
You now have a **standardized schema** for every shot.  
This lets you:
- Treat shots like services with contracts.  
- Automate asset tracking and generation with MCP-enabled tools.  
- Build a full PRD for the trailer with consistent structure.  

Next, we’ll move into **Part 4b — Purpose & Success Criteria**, where we’ll detail how to define the role and measurable outcomes of each shot.
