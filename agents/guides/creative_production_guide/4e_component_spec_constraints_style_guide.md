# Part 4e — Component Spec for Each Shot: Constraints & Style Guides

Now that we’ve defined outputs, we need to establish the **rules and boundaries** each shot must operate within.  
Think of this as the **non-functional requirements** or **style guide contracts** for a component.

---

## 🎯 Goal of This Part
- Document the **constraints** that bound each shot (time, tone, technical).  
- Provide a **style guide** for consistency across all shots.  
- Prevent failure modes by making implicit creative rules explicit.

---

## 🧩 Categories of Constraints

### 1. **Duration Constraints**
- Each shot must fall within a defined time window.  
- Example: 2–5s per shot, max 60s total trailer.  
- Rule: *“If >5s, cut or split into two shots.”*  

### 2. **Tone & Emotional Constraints**
- Must match global brand tone (e.g., Apple-polished + creator-energy).  
- Avoid tonal whiplash (e.g., don’t switch from hype to somber).  
- Every shot has an emotional target that cannot be missed (e.g., “curiosity” for hook).  

### 3. **Visual Constraints**
- Typography: bold sans-serif, max 40 chars per line.  
- Color palette: neutral backgrounds + neon accent for avatars.  
- Safe areas: captions/subtitles must not overlap avatar icons.  
- UI: logo-free, generic but instantly recognizable.  

### 4. **Audio Constraints**
- VO pacing: 120–150 words per minute.  
- Music: duck -6 dB under VO.  
- SFX: subtle, no more than 1 per shot.  
- LUFS loudness target: -14 to -16.  

### 5. **Legal & IP Constraints**
- No real ESPN/Amazon logos.  
- No celebrity likenesses without rights.  
- Avatars = stylized symbolic personas only.  

---

## 📋 Example Shot Spec

**Shot ID:** Shopping-2 (Avatar Guidance)  
- **Constraints:**  
  - Duration: <= 3s  
  - Tone: Relatable + delightful, not salesy  
  - Typography: Bold sans-serif, max 36 chars/line  
  - Color palette: White/teal background, avatar glow accent  
  - VO: <= 12 words, ~135 WPM  
  - Audio: LUFS -15 ±1  
  - Legal: Avatar must be generic beauty icon, no real influencer likeness  

---

## ✅ Output of This Step
- Each shot now has **clear operational boundaries**.  
- Creative choices are now **systemized** into enforceable rules.  
- Ensures consistency across shots, prevents “off-brand” moments, and avoids legal/IP issues.  

Next: in **Part 4f — Failure Modes & Mitigations**, we’ll anticipate how shots can break and prescribe fallback strategies.
