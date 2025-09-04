# Part 4d — Component Spec for Each Shot: Outputs (Deliverables & Telemetry)

After defining inputs, the next step is to specify the **outputs**.  
Think of this as the **artifacts and metrics** each shot must generate, similar to the return values and logs of a service.

---

## 🎯 Goal of This Part
- Define the **deliverables** each shot must produce (files, renders, text).  
- Define the **telemetry/metadata** that helps evaluate whether the shot met its criteria.  
- Ensure every shot is testable, reviewable, and measurable.

---

## 🧩 Types of Outputs

### 1. **Deliverables**
- **Composited shot render** (mp4, mov, or project snippet).  
- **VO + captions** (wav/mp3 + srt/vtt files).  
- **UI overlays** (clean export of frame with avatar icon).  
- **Scene package** (if grouped with other shots).  

**Tip:** Store deliverables in a structured directory (e.g., `/shots/beat/scene/shot_id/`).  

---

### 2. **Telemetry (Shot-Level Metadata)**
- **Duration actual** (seconds, compare vs. constraint).  
- **Word count / WPM** of VO.  
- **Audio levels** (LUFS, peak dB).  
- **Subtitle readability score** (e.g., text <= 40 chars per line).  
- **Playback review tags** (AI or human annotations: clarity, emotion hit/miss).  

**Tip:** Treat this like system logs → helps debug pacing, clarity, and flow.  

---

## 📋 Example Shot Spec

**Shot ID:** Sports-2 (Avatar Reply)  
- **Deliverables:**  
  - Final render: `sports_avatar_reply_v1.mp4`  
  - Avatar VO file: `sports_avatar_reply.wav`  
  - Subtitles: `sports_avatar_reply.srt`  
  - Overlay frame: `sports_page_avatar_overlay.png`  

- **Telemetry:**  
  - Duration actual: 2.4s (constraint <= 3s ✅)  
  - VO words: 11 (constraint <= 12 ✅)  
  - WPM: 137 (constraint <= 150 ✅)  
  - LUFS: -16 (within broadcast safe range)  
  - Subtitle readability: ✅ (line length 34 chars)  
  - Emotion tag: “delight” (reviewer feedback)  

---

## ✅ Output of This Step
- Each shot now has a clear **package of deliverables** (files to ship).  
- Each shot also has **telemetry** (metrics/logs) for QA and iteration.  
- This ensures shots are not just produced, but also **measurable against success criteria.**  

Next: in **Part 4e — Constraints & Style Guides**, we’ll define the rules that bound each shot (duration windows, typography, brand tone).
