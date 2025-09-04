# Part 6 — Transitions & Stitching (APIs & Integration)

Now that we’ve defined shots and emotional flow, the next layer is **transitions** — the “glue” between shots.  
This is like defining **APIs and integration contracts** between microservices.

---

## 🎯 Goal of This Part
- Treat transitions as **interfaces** that carry emotion and clarity between shots.  
- Define types of transitions and when to use them.  
- Prevent breaks in immersion (the equivalent of broken API calls).

---

## 🧩 Transitions as Contracts
- Each shot “hands off” to the next.  
- The **transition** defines how that handoff feels.  
- If the handoff is broken, the audience feels jarred (like a 500 error).

---

## 🔀 Types of Transitions

### 1. **Hard Cut (Direct API Call)**
- Instant switch from one shot to the next.  
- Best for: high-energy beats (gaming, montage).  
- Risk: feels abrupt if tone shifts too much.

### 2. **Match Cut (Schema-Aligned API)**
- Cut between two visually similar actions (scroll → scroll, click → click).  
- Best for: smooth logical progression.  
- Builds continuity without slowing pacing.

### 3. **Motion/Graphic Transition (Middleware)**
- Abstract animation, whoosh, fade, or overlay bridges shots.  
- Best for: tone shifts (sports → beauty, beauty → gaming).  
- Adds breathing space and visual polish.

### 4. **Audio Bridge (Async API Call)**
- Music or VO line carries across shots.  
- Best for: maintaining emotional continuity even with visual change.  
- Prevents tonal whiplash.

---

## 🧾 Transition Guidelines
- **Consistency:** Use the same type within a beat for rhythm.  
- **Variety:** Change type between beats to avoid monotony.  
- **Purpose:** Every transition must serve clarity or emotion, not just decoration.  
- **Duration:** Keep most transitions under 1s unless intentional pause.  

---

## 📋 Example Beat Transitions
- **Hook → Reveal:** Hard cut (problem → solution) with VO bridge.  
- **Sports → Shopping:** Motion graphic overlay (avatar glow expands, contracts into next shot).  
- **Shopping → Gaming:** Match cut (phone swipe → mouse click).  
- **Marketplace Montage:** Rapid hard cuts synced to beat.  
- **Closing → CTA:** Slow fade with music swell (gives gravitas).  

---

## ✅ Output of This Step
You now have a framework for **transitions as APIs**:  
- Types: hard cut, match cut, graphic, audio bridge.  
- Rules for consistency, variety, purpose, and duration.  
- Example mappings for your trailer.  

Next: in **Part 7 — Implementation Planning (Resourcing)**, we’ll map each beat/shot to required assets, tools, and roles — the equivalent of infra + resourcing in system design.
