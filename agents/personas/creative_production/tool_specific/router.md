# 🧭 Creative Production Tool-Specific Agent Router

This folder contains specialized AI agents designed to assist with specific AI video generation tools, audio production, and creative technology optimization for professional video content creation.

Use this file to decide which agent persona is best suited for a tool-specific creative production task. If no persona is a good fit, consider creating a new one using the persona creation templates.

---

## 🧠 Persona Directory

### `ai_video_generation_expert.md`

- **Name**: AI Video Generation Expert
- **Summary**: Senior specialist who excels at leveraging AI video generation tools like Runway Gen-3, Luma Dream Machine, and Pika to create compelling visual content that meets creative briefs and production requirements
- **Focus Areas**: AI video tools, prompt engineering, workflow optimization, quality control, creative technology integration
- **Example Tasks**:
  - Setting up comprehensive AI video workflows for product launches
  - Creating brand-consistent AI video strategies across multiple tools
  - Optimizing AI video production for speed and cost-effectiveness

### `veo3_optimization_expert.md`

- **Name**: Veo3 Optimization Expert
- **Summary**: Expert in maximizing Veo3's unique capabilities including native audio generation, character consistency, and physics simulation for professional video production
- **Focus Areas**: Veo3 optimization, native audio generation, character consistency, physics simulation, professional video production
- **Example Tasks**:
  - Leveraging Veo3's native audio generation for product demonstration videos
  - Creating consistent character presentations across multiple video shots
  - Optimizing for realistic physics-based movements and interactions

### `runway_gen4_optimization_expert.md`

- **Name**: Runway Gen-4 Optimization Expert
- **Summary**: Expert in maximizing Runway Gen-4's keyframe functionality, visual reference integration, and simplicity-focused prompting for high-quality video generation
- **Focus Areas**: Runway Gen-4 optimization, keyframe functionality, visual reference integration, simplicity-focused prompting
- **Example Tasks**:
  - Using keyframes for consistent character generation across multiple shots
  - Simplifying complex prompts for optimal Runway Gen-4 performance
  - Integrating visual references effectively with text prompts

### `pika_optimization_expert.md`

- **Name**: Pika Optimization Expert
- **Summary**: Expert in maximizing Pika 1.5's motion effects, lip sync capabilities, and video-to-video transformations for dynamic video content
- **Focus Areas**: Pika 1.5 optimization, motion effects, lip sync capabilities, video-to-video transformations
- **Example Tasks**:
  - Adding dynamic motion effects to product videos for enhanced engagement
  - Creating videos with synchronized character speech and natural dialogue
  - Transforming existing videos with new styles using video-to-video features

### `luma_dream_machine_expert.md`

- **Name**: Luma Dream Machine Expert
- **Summary**: Expert in optimizing Luma Dream Machine's natural language processing, character reference system, and cinematic movement capabilities for professional video production
- **Focus Areas**: Luma Dream Machine optimization, natural language processing, character reference system, cinematic movement
- **Example Tasks**:
  - Creating cinematic videos using natural language prompts instead of technical jargon
  - Leveraging Luma's character reference system for consistent character generation
  - Creating smooth, cinematic movements that feel natural and organic

### `audio_production_specialist.md`

- **Name**: Audio Production Specialist
- **Summary**: Expert in AI audio generation, synchronization, and post-production for video content, ensuring seamless audio-visual integration
- **Focus Areas**: AI audio generation, audio synchronization, post-production, audio-visual integration
- **Example Tasks**:
  - Creating synchronized audio for AI-generated video content with professional quality
  - Optimizing audio integration across different AI video models and platforms
  - Creating immersive audio experiences that enhance brand video content

---

## 📌 Routing Guidelines

To determine which persona to use:

1. **Identify the specific AI tool or technology** you're working with:
   - **Veo3** → `veo3_optimization_expert.md`
   - **Runway Gen-4** → `runway_gen4_optimization_expert.md`
   - **Pika 1.5** → `pika_optimization_expert.md`
   - **Luma Dream Machine** → `luma_dream_machine_expert.md`
   - **General AI video tools** → `ai_video_generation_expert.md`
   - **Audio production** → `audio_production_specialist.md`

2. **Check the task requirements** against the persona's focus areas and capabilities

3. **Consider the specific features** you need to leverage (e.g., character consistency, motion effects, audio generation)

4. **For multi-tool workflows**, use the general `ai_video_generation_expert.md` for overall strategy and specific tool experts for optimization

5. If no persona matches, return:
   > **No matching persona found. Consider defining a new one.**

---

## 🔁 Common Tasks and Suggested Agents

| Task Pattern | Suggested Persona(s) |
|--------------|----------------------|
| Need character consistency across multiple shots | `veo3_optimization_expert.md`, `runway_gen4_optimization_expert.md`, `luma_dream_machine_expert.md` |
| Want to add motion effects and dynamic movement | `pika_optimization_expert.md` |
| Need synchronized audio with video content | `veo3_optimization_expert.md`, `audio_production_specialist.md` |
| Creating cinematic, smooth camera movements | `luma_dream_machine_expert.md` |
| Optimizing prompts for specific AI tools | Tool-specific expert (e.g., `runway_gen4_optimization_expert.md`) |
| Building comprehensive AI video workflows | `ai_video_generation_expert.md` |
| Video-to-video style transformations | `pika_optimization_expert.md` |
| Using visual references with text prompts | `runway_gen4_optimization_expert.md` |
| Natural language prompt optimization | `luma_dream_machine_expert.md` |
| Physics-based realistic movements | `veo3_optimization_expert.md` |
| Audio post-production and synchronization | `audio_production_specialist.md` |
| Multi-tool AI video strategy and coordination | `ai_video_generation_expert.md` |

---

## 🛠️ Update Instructions

After adding new tool-specific personas to this folder, rerun the router generation process to update this file and maintain accurate routing guidance.

---

## Notes

- Each persona specializes in specific AI video tools and their unique capabilities
- Tool-specific experts provide deep optimization knowledge for maximum results
- The general AI video generation expert handles multi-tool workflows and overall strategy
- Audio production specialist works across all video tools for seamless integration
- Focus on the specific tool features you need to leverage for optimal routing decisions

---
