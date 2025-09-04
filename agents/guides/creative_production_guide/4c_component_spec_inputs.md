# Part 4c — Component Spec for Each Shot: Inputs (Script, Visuals, Audio)

With purpose and success criteria defined, the next step is to capture the **inputs** required for each shot.  
Think of this like the **API dependencies** or **config values** needed for a service to run.

---

## 🎯 Goal of This Part
- Identify all inputs (script, visuals, audio) required for a shot.  
- Organize them clearly so they can be tracked, versioned, and generated.  
- Ensure no shot proceeds without its required building blocks.

---

## 🧩 Input Categories

### 1. **Script Inputs**
- **User VO line** (sets up problem or question).  
- **Avatar VO line** (delivers payoff/insight).  
- **Narrator VO line** (contextual framing, optional).  
- **Variants** (alt phrasing for A/B testing).  

**Tips:**  
- Keep user lines short, natural, conversational.  
- Keep avatar lines punchy (8–12 words).  
- Narrator lines should be clean and confident.

---

### 2. **Visual Inputs**
- **Actors or stock b-roll** (fans, creators, gamers).  
- **UI mockups** (sports page, shopping product card, patch notes).  
- **Avatar icons** (stylized persona, circular overlay).  
- **Props/Setting** (laptop, phone, mirror, gaming desk).  

**Tips:**  
- UI should be generic, logo-free, instantly recognizable.  
- Avatars should be distinct but neutral (not resembling real people).  
- B-roll should feel authentic (not staged stock footage).  

---

### 3. **Audio Inputs**
- **VO recordings** (user, avatar, narrator).  
- **SFX cues** (scroll clicks, UI pops, subtle whoosh).  
- **Music stem slices** (intro beat, mid build, CTA rise).  
- **Silence padding** (for rhythm).  

**Tips:**  
- Use ElevenLabs for VO (consistent tone + variants).  
- Keep SFX subtle (avoid gimmicky sounds).  
- Ensure music doesn’t overpower VO (duck under voice).  

---

## 📋 Example Shot Spec

**Shot ID:** Shopping-1 (User browsing skincare)  
- **Script Inputs:**  
  - User VO: “Would this cleanser even work for me?”  
  - Avatar VO: none (delivered in next shot).  

- **Visual Inputs:**  
  - B-roll: Woman at mirror with skincare.  
  - UI frame: skincare_product_v2.png.  
  - Avatar icon: beauty_icon.svg.  

- **Audio Inputs:**  
  - SFX: light scroll click.  
  - Music: upbeat bed (stem A).  

---

## ✅ Output of This Step
- Every shot now has a clear list of **script, visual, and audio inputs**.  
- These inputs can be **tracked, versioned, and generated** systematically.  
- No ambiguity about what assets need to exist before assembly.  

Next: in **Part 4d — Outputs (Deliverables & Telemetry)**, we’ll define what each shot should produce and how to measure it.
