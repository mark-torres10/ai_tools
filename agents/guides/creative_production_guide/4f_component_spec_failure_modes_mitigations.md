# Part 4f — Component Spec for Each Shot: Failure Modes & Mitigations

Every system has failure cases. Shots do too.  
This section defines **how a shot can fail** and **how to mitigate** or recover — like documenting failure modes and fallback strategies for a service.

---

## 🎯 Goal of This Part
- Anticipate **common ways shots break** (creatively or technically).  
- Define **impact** of each failure on narrative arc.  
- Provide **mitigation strategies** (fixes, fallbacks, checks).  

---

## 🧩 Failure Mode Categories

### 1. **Narrative Failures**
- **Problem:** The shot doesn’t communicate its intended message.  
- **Impact:** Audience feels confused or bored.  
- **Mitigation:**  
  - Shorten VO.  
  - Simplify visuals.  
  - Add subtitle emphasis on key words.  

### 2. **Emotional Failures**
- **Problem:** Audience doesn’t feel intended emotion (e.g., no delight, no trust).  
- **Impact:** Breaks the emotional arc (like missing an SLA).  
- **Mitigation:**  
  - Revise VO tone (livelier, calmer).  
  - Swap b-roll for more relatable footage.  
  - Adjust pacing with tighter cuts.  

### 3. **Timing Failures**
- **Problem:** Shot runs too long or too short.  
- **Impact:** Trailer drags or feels rushed.  
- **Mitigation:**  
  - Enforce duration constraints.  
  - Use AI reviewer to auto-detect shot >5s.  
  - Split long shots into two.  

### 4. **Visual Failures**
- **Problem:** UI unclear, avatar overlaps text, shot looks staged.  
- **Impact:** Audience distracted, message lost.  
- **Mitigation:**  
  - Add safe-area checks.  
  - Re-export UI from Figma with cleaner layout.  
  - Choose more authentic b-roll.  

### 5. **Audio Failures**
- **Problem:** VO too fast, music too loud, subtitles desynced.  
- **Impact:** Comprehension drops, professionalism lost.  
- **Mitigation:**  
  - Run VO WPM check (target 120–150).  
  - Auto-duck music under voice.  
  - Auto-generate subtitles and review alignment.  

### 6. **Legal/IP Failures**
- **Problem:** Accidental logo, celebrity likeness, or copyrighted material.  
- **Impact:** Legal liability, brand damage.  
- **Mitigation:**  
  - QA check for logos/marks.  
  - Restrict avatar gen to symbolic icons.  
  - Use only licensed stock/AI media.  

---

## 📋 Example Shot Spec

**Shot ID:** Gaming-2 (Avatar Insight)  
- **Potential Failures & Mitigations:**  
  - VO too long → trim to <12 words.  
  - Gamer avatar feels generic → redesign with neon headset icon.  
  - Emotion flat → re-record VO with higher energy.  
  - Music overpowering → rebalance mix (-6 dB under VO).  
  - Patch notes UI too dense → simplify to 3 key bullets.  

---

## ✅ Output of This Step
- Every shot now has **failure modes mapped** with **mitigation strategies.**  
- You’ve created the equivalent of a **resilience plan** for creative work.  
- Ensures trailer can recover from weak spots without scrapping the whole cut.  

Next: in **Part 4g — Assets, Toolchain & MCP Hooks**, we’ll define what assets each shot needs, which tools generate them, and where MCP servers can automate the pipeline.
