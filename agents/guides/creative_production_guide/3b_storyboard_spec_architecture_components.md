# Part 3b — Storyboard as Spec Architecture: Shots (Components)

With beats defined as subsystems, we now drill down into **shots** as the smallest units of design.  
Each shot is a **component** within a beat.

---

## 🎯 Goal of This Part
To define shots with the same rigor as services/components in a system design:  
- Each shot has a **purpose**.  
- Each shot has **inputs** and **outputs**.  
- Each shot operates within **constraints** (time, tone, visual style).  
- Together, shots execute the beat’s purpose.

---

## 🧩 What Are Shots?
- **Analogy:** A *shot* = a *microservice or component*.  
- It handles one discrete job (e.g., “fan scrolling with frustration” or “avatar delivers line”).  
- Shots are composable. You can swap one without breaking the whole beat, as long as inputs/outputs remain valid.  
- Shots must be efficient — just like services, they have a “budget” (seconds instead of CPU cycles).

---

## 📊 Shot Structure (Component Spec Format)

Each shot should be documented like this:

- **Name/ID**: Short handle (e.g., “Sports-1: Fan Scroll”).  
- **Purpose**: Why this shot exists (what problem it solves in the arc).  
- **Inputs**:  
  - Visuals (actors, UI mockups, props, setting).  
  - Audio (script line, sound effect, music cue).  
- **Outputs**:  
  - Emotional response (what the audience should feel).  
  - Narrative takeaway (what info they now have).  
- **Constraints**:  
  - Duration (e.g., 3–5s).  
  - Style (Apple-polished, upbeat creator-energy).  
  - Tone (relatable, delightful, trustworthy).  
- **Failure Modes**:  
  - Emotion doesn’t land.  
  - Visuals confuse or distract.  
  - Timing drags or cuts too abruptly.  

---

## 📋 Example Shots from Your Trailer

**Beat: Sports Use Case**  
- *Shot 1: Fan scrolling*  
  - Purpose: Show relatable frustration.  
  - Inputs: Actor scrolling generic sports page. User VO: “Who even played well in this game?”  
  - Outputs: Audience recognizes problem → curiosity.  
  - Constraints: 3s max, clear UI.  
  - Failure Mode: If unclear, audience doesn’t empathize.  

- *Shot 2: Avatar reply*  
  - Purpose: Deliver instant context.  
  - Inputs: Avatar icon overlay; Avatar VO line.  
  - Outputs: Surprise + delight.  
  - Constraints: 2s, short punchy VO.  
  - Failure Mode: Too long or too vague → payoff lost.  

**Beat: Shopping Use Case**  
- *Shot 1: User browsing skincare*  
  - Purpose: Everyday relatability.  
  - Inputs: B-roll of person at mirror; product card on phone.  
  - Outputs: Connection to lifestyle.  
  - Constraints: 3s max, natural feel.  
  - Failure Mode: Feels staged → breaks relatability.  

- *Shot 2: Avatar guidance*  
  - Purpose: Personal recommendation.  
  - Inputs: Avatar icon overlay; Avatar VO with tip + discount.  
  - Outputs: Delight + utility.  
  - Constraints: 2–3s, clear line.  
  - Failure Mode: Feels like an ad, not a friend.  

---

## ✅ Output of This Step
Shots are now defined like components:  
- Each has **purpose, inputs, outputs, constraints, failure modes.**  
- This makes it easy to expand, substitute, or refine without breaking the whole arc.  

Next: we’ll zoom out one layer up to **Part 3c — Storyboard as Spec Architecture: Scenes (Groupings)**.
