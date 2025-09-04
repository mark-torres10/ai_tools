# Part 3c — Storyboard as Spec Architecture: Scenes (Groupings)

We’ve defined beats (subsystems) and shots (components).  
Now we step up one layer: **scenes**, which group shots into coherent sequences.

---

## 🎯 Goal of This Part
To understand **scenes** as the mid-level unit of design:  
- A scene groups multiple shots that share a location, context, or use case.  
- Scenes ensure consistency and flow within a beat.  
- Scenes make it easier to reason about pacing and narrative rhythm.

---

## 🧩 What Are Scenes?
- **Analogy:** A *scene* = a *service cluster or module*.  
- It bundles multiple components (shots) into a deployable unit.  
- Scenes can be swapped, reordered, or trimmed while maintaining internal integrity.  
- Each scene has:  
  - **Purpose** (role in the larger arc).  
  - **Contained Shots** (the components).  
  - **Total Duration Budget.**  
  - **Emotional Arc.**

---

## 📊 Example Scenes in Your Trailer

### **Scene 1: Sports Use Case**
- **Purpose:** Show immediate value in a familiar context.  
- **Shots:**  
  - Shot 1: Fan scrolling, frustrated question.  
  - Shot 2: Avatar delivers instant context.  
- **Duration Budget:** 6–8s total.  
- **Emotional Arc:** Curiosity → Surprise/Delight → Trust.  
- **Failure Mode:** If too long, audience loses attention before payoff.

---

### **Scene 2: Shopping/Beauty Use Case**
- **Purpose:** Show utility in everyday lifestyle.  
- **Shots:**  
  - Shot 1: User browsing skincare.  
  - Shot 2: Avatar gives tip + discount.  
- **Duration Budget:** 6–8s.  
- **Emotional Arc:** Relatability → Delight.  
- **Failure Mode:** If avatar line feels like an ad, trust breaks.

---

### **Scene 3: Gaming/News Use Case**
- **Purpose:** Demonstrate adaptability in another domain.  
- **Shots:**  
  - Shot 1: Gamer asks about patch.  
  - Shot 2: Avatar gives insider tip.  
- **Duration Budget:** 6–8s.  
- **Emotional Arc:** Curiosity → Excitement/Playfulness.  
- **Failure Mode:** If line isn’t specific/credible, gamer audience disengages.

---

### **Scene 4: Marketplace Montage**
- **Purpose:** Show scale + creator empowerment.  
- **Shots:**  
  - Multiple quick cuts (cooking, jogging, creator editing).  
  - Multiple avatars responding.  
- **Duration Budget:** 8–10s.  
- **Emotional Arc:** Breadth → Possibility → Empowerment.  
- **Failure Mode:** If too cluttered, loses clarity.

---

## ✅ Output of This Step
Scenes provide a **middle layer of abstraction**:  
- **Beats** = high-level subsystems (Hook, Use Cases, Marketplace, Closing).  
- **Shots** = components (the smallest units).  
- **Scenes** = groupings (packages of shots delivering a complete mini-arc).  

You now have the **full hierarchy**:  
**Beats → Scenes → Shots.**

Next we’ll go deeper in **Part 4 — Component Spec for Each Shot**, expanding the shot structure with detailed inputs, outputs, and acceptance criteria.
