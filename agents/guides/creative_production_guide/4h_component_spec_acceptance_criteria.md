# Part 4h — Component Spec for Each Shot: Acceptance Tests & Review Checklist

Now that assets, tools, and pipelines are defined, we need to establish **how to test each shot** before it’s integrated into the trailer.  
This is like **unit testing + code review** for a service.

---

## 🎯 Goal of This Part
- Define **acceptance tests** that verify shot quality.  
- Create a **review checklist** that ensures consistency.  
- Formalize sign-off so shots can be integrated with confidence.

---

## 🧩 Acceptance Tests (Shot-Level QA)

Tests should cover:
1. **Timing**
   - Shot duration within defined window (e.g., 2–5s).
   - VO within pacing target (120–150 WPM).
2. **Clarity**
   - Viewer can describe what happened in <1 sentence.
   - Subtitles are accurate and readable (<40 chars per line).
3. **Emotion**
   - Reviewer/AI confirms target emotion is evoked (e.g., “delight”).
   - No tonal mismatch with beat.
4. **Visual Quality**
   - UI clear, no overlapping text/icons.
   - B-roll looks authentic (not staged/stocky).
5. **Audio Quality**
   - VO clean, consistent tone.
   - Music ducked -6 dB under VO.
   - LUFS loudness -14 to -16.
6. **Legal/IP**
   - No logos, celebrity likenesses, or protected marks.

---

## 🧾 Review Checklist (For Humans + AI Agents)

- [ ] Purpose of shot documented and aligned to beat.  
- [ ] Success criteria defined and met.  
- [ ] Inputs logged (script, visuals, audio).  
- [ ] Outputs produced (render, captions, telemetry).  
- [ ] Constraints respected (time, tone, style).  
- [ ] Failure modes reviewed, no unresolved risks.  
- [ ] Asset manifest complete and versioned.  
- [ ] Toolchain + MCP hooks executed without errors.  
- [ ] Acceptance tests passed (timing, clarity, emotion, quality, legal).  
- [ ] Reviewer sign-off recorded (name, date, version).  

---

## 📋 Example Shot Spec QA

**Shot ID:** Shopping-2 (Avatar Guidance)  
- **Acceptance Tests:**  
  - Duration = 2.8s ✅  
  - VO = 10 words, 135 WPM ✅  
  - Viewer feedback: “Felt like a friend helping” ✅  
  - Subtitles accurate, 32 chars max ✅  
  - LUFS = -15 ✅  
  - No brand logos ✅  

- **Review Checklist:**  
  - Purpose: Deliver personal recommendation ✅  
  - Inputs: b-roll, product UI, avatar VO ✅  
  - Outputs: final render + captions ✅  
  - Constraints: all met ✅  
  - Reviewer: MTorres, v1.0, 2025-09-04 ✅  

---

## ✅ Output of This Step
- Each shot now has **unit tests + review process**.  
- QA is structured, measurable, and automatable.  
- Shots that pass are integration-ready for the full trailer.  

---

# ✅ Summary of Part 4 (a–h)
We’ve now defined a **complete shot spec system**:
- Schema & Template  
- Purpose & Success Criteria  
- Inputs (Script, Visuals, Audio)  
- Outputs (Deliverables & Telemetry)  
- Constraints & Style Guides  
- Failure Modes & Mitigations  
- Assets, Toolchain & MCP Hooks  
- Acceptance Tests & Review Checklist  

This is your **PRD equivalent for creative direction** at the shot level.

Next, in **Part 5 — Emotional & Narrative Arc (System Behavior)**, we’ll zoom back out and treat the whole trailer as a system-in-motion, ensuring the emotional pacing works like a well-orchestrated service.
