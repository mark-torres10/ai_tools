# Creative Direction PRD — AI Avatar Trailer

This document treats the creative direction process like a **system design spec**.  
It structures beats, shots, emotional arcs, assets, and QA into a reproducible framework.

---

# Part 1 — Mental Reframes (Foundations)

## 🎯 Goal
Reframe creative direction as a system with components, constraints, and outputs.

## 🔄 Core Reframes
- **Storyboard = Architecture Diagram**
- **Shot = Component/Service**
- **Narrative Arc = System Behavior**
- **Transitions = API Contracts**
- **Emotion = SLO**
- **Constraints = NFRs**

## ⚙️ Mental Model Shift
- Engineering: throughput, latency, failure modes.  
- Creative: pacing, emotional timing, immersion breaks.

---

# Part 2 — Mental Reframes (Workflow & Questions)

## 🎯 Goal
Turn creative review into structured design review.

## 📝 Checklist
1. Storyboard level: purpose, arc, redundancy, time.  
2. Shot level: purpose, inputs, outputs, constraints, failure modes.  
3. Transition level: handoffs, pacing.  
4. System level: emotional SLOs, bottlenecks, overloads.

## ✅ Output
Refined spec with acceptance criteria.

---

# Part 3a — Storyboard as Spec Architecture: Beats (Subsystems)

## 🎯 Goal
Define beats as subsystems delivering emotional payloads.

## Example Beats
- Hook → Curiosity, recognition.  
- Reveal → Surprise, delight.  
- Sports → Trust, excitement.  
- Shopping → Relatability, delight.  
- Gaming → Playfulness, credibility.  
- Marketplace → Possibility, empowerment.  
- Closing → Inspiration, trust.

---

# Part 3b — Storyboard as Spec Architecture: Shots (Components)

## 🎯 Goal
Shots as smallest designable units with inputs/outputs.

## Shot Schema
- Purpose  
- Inputs (visuals, audio)  
- Outputs (emotion, narrative)  
- Constraints (duration, tone, style)  
- Failure modes  

---

# Part 3c — Storyboard as Spec Architecture: Scenes (Groupings)

## 🎯 Goal
Scenes group shots into coherent sequences.

## Example Scenes
- Sports Scene: Fan scrolling → Avatar reply.  
- Shopping Scene: Browsing skincare → Avatar tip.  
- Gaming Scene: Gamer Q → Avatar insight.  
- Marketplace: Montage of avatars/creators.

---

# Part 4a — Component Spec: Schema & Template

```yaml
id: Sports-1
beat: Sports Use Case
scene: Sports Scene
name: Fan scrolling
purpose: Show relatable pain point
inputs:
  visuals: [actor, sports UI mock]
  audio: [user VO]
outputs:
  emotional: Curiosity
  narrative: Viewer recognizes problem
constraints:
  duration: 3s
  style: Apple-polished
  tone: Relatable
failure_modes:
  - Feels staged → no empathy
acceptance_criteria:
  - Shot <=3s
  - Viewer recognizes problem
assets_required:
  - sports_mock_v1.png
  - commentator_icon.svg
tools_pipeline:
  - Figma MCP
  - ElevenLabs MCP
  - CapCut
```

---

# Part 4b — Purpose & Success Criteria

- **Purpose:** Why does shot exist? (narrative role)  
- **Success Criteria:** Observable, measurable, aligned.  
  - Clarity (audience recalls message)  
  - Emotion (viewer feels intended)  
  - Timing (within budget)

---

# Part 4c — Inputs (Script, Visuals, Audio)

- **Script:** user VO, avatar VO, narrator VO.  
- **Visuals:** b-roll, UI, avatars, props.  
- **Audio:** VO, SFX, music stems.  

---

# Part 4d — Outputs (Deliverables & Telemetry)

- **Deliverables:** final renders, VO files, captions.  
- **Telemetry:** duration, WPM, LUFS, readability, emotion tags.  

---

# Part 4e — Constraints & Style Guides

- **Duration:** 2–5s per shot.  
- **Tone:** Apple-polished + creator-energy.  
- **Visuals:** bold sans-serif, safe areas, no logos.  
- **Audio:** 120–150 WPM, LUFS -14 to -16.  

---

# Part 4f — Failure Modes & Mitigations

- **Narrative failure:** unclear → trim VO.  
- **Emotional failure:** flat → re-record VO.  
- **Timing failure:** too long → split.  
- **Visual failure:** clutter → clean UI.  
- **Audio failure:** too loud music → rebalance.  
- **Legal failure:** logos → replace assets.

---

# Part 4g — Assets, Toolchain & MCP Hooks

- **Assets:** UI mockups, icons, b-roll, VO, music, captions.  
- **Tools:** Figma, Pexels, Runway, HeyGen, ElevenLabs, CapCut.  
- **MCP Hooks:** export, fetch, generate VO, assemble.  

---

# Part 4h — Acceptance Tests & Review Checklist

- **Tests:** duration, clarity, emotion, visual, audio, legal.  
- **Checklist:** purpose, criteria, inputs, outputs, constraints, failure modes, assets, pipeline.  
- **Sign-off:** reviewer/date/version.

---

# Part 5a — Emotional Arc Fundamentals (Principles)

- **Emotions = SLOs**  
- **Narrative logic vs. emotional logic**  
- Core beats: curiosity → surprise → trust → relatability → playfulness → possibility → inspiration.  

---

# Part 5b — Emotional Arc Fundamentals (Beat Mapping)

- Hook → Curiosity + Recognition.  
- Reveal → Surprise + Delight.  
- Sports → Trust + Excitement.  
- Shopping → Relatability + Delight.  
- Gaming → Playfulness + Credibility.  
- Marketplace → Possibility + Empowerment.  
- Closing → Inspiration + Trust.  

---

# Part 5c — Narrative Flow & Pacing (Timing Principles)

- **Time budgets:** 5–10s per beat, <60s total.  
- **Shot durations:** 2–4s typical, montage = 1–2s.  
- **Rhythm:** punchy start, alternating setups/payoffs, rapid montage, slow inspirational CTA.  

---

# Part 5d — Narrative Flow & Pacing (Flow Management)

- **Bottlenecks:** too long → trim.  
- **Overloads:** too much info → split.  
- **Jarring transitions:** tone mismatch → bridge.  
- **Fixes:** compression, expansion, reordering, bridging.  

---

# Part 5e — Testing the Emotional System

- **Human review:** screenings, interviews.  
- **AI review:** sentiment tagging, comprehension checks.  
- **Telemetry checks:** WPM, LUFS, caption length.  
- **Iteration:** tighten, trim, reorder, rescript.  

---

# Part 6 — Transitions & Stitching (APIs & Integration)

- **Hard cuts:** high energy.  
- **Match cuts:** smooth logical link.  
- **Motion graphics:** tone shifts.  
- **Audio bridges:** continuity.  
- **Guidelines:** consistency, variety, purpose, <1s duration.

---

# Part 7 — Implementation Planning (Resourcing)

- **Assets:** UI, icons, b-roll, VO, music.  
- **Tools:** Figma, Pexels, Runway, HeyGen, ElevenLabs, CapCut.  
- **Roles:** creative engineer, designer, reviewer.  
- **Automation:** MCP hooks for export, VO gen, assembly.

---

# Part 8 — Iteration & Versioning

- **Semantic versions:** v0.x draft, v1.x animatic, v2.x beta, v3.0 final.  
- **Tracking:** YAML/Markdown logs per shot.  
- **Workflow:** storyboard → animatic → beta cut → polish → final.  
- **Automation:** Git, cloud storage, AI-generated changelogs.

---

# Part 9 — Evaluation & Testing

- **Technical QA:** integration, sync, exports.  
- **Narrative QA:** coherence, arc validation.  
- **Audience QA:** comprehension, emotion, conversion intent.  
- **AI QA:** transcript analysis, pacing.  
- **Metrics:** retention, comprehension, emotional accuracy, conversion.

---

# Part 10 — Final Assembly & Delivery

- **Assembly:** timeline lock, edit, polish (color/audio).  
- **Exports:** master (16:9), social (9:16), investor loop.  
- **Accessibility:** captions, transcripts, alt audio.  
- **Metrics:** retention curve, A/B test CTA variants.  
- **Deployment:** website hero, social distribution, deck embeds.

---

# ✅ End of Document
This PRD-equivalent covers:  
- Reframes (Parts 1–2)  
- Architecture (Parts 3a–c)  
- Shot specs (Parts 4a–h)  
- Emotional arc (Parts 5a–e)  
- Integration (Part 6)  
- Implementation planning (Part 7)  
- Iteration & versioning (Part 8)  
- Evaluation & testing (Part 9)  
- Final delivery (Part 10)  

It turns creative direction into a **structured, testable, system-like workflow**.
