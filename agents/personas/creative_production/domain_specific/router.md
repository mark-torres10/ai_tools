# 🧭 Agent Persona Router

This folder contains specialized AI agents designed to assist with various creative production tasks across audience research, brand storytelling, product marketing, and strategic leadership.

Use this file to decide which agent persona is best suited for a task or review. If no persona is a good fit, consider creating a new one using `create_persona.md`.

---

## 🧠 Persona Directory

### `audience_research_expert.md`
- **Name**: Audience Research Expert
- **Summary**: Senior audience research specialist who excels at understanding target audiences deeply and translating insights into actionable creative direction for video and multimedia content
- **Focus Areas**: User Research & Analysis, Audience Segmentation & Persona Development, Behavioral Analysis & Journey Mapping, Market Research & Competitive Analysis, Creative Direction & Content Strategy
- **Example Tasks**:
  - Conduct comprehensive audience research for product launch videos
  - Analyze audience engagement issues and provide data-driven solutions
  - Define and validate target audiences for investor presentations

### `brand_storytelling_expert.md`
- **Name**: Brand Storytelling Expert
- **Summary**: Senior brand strategist and storytelling specialist who excels at crafting compelling brand narratives that resonate emotionally with audiences and create lasting brand connections
- **Focus Areas**: Brand Narrative Development, Tone & Voice Strategy, Story Architecture & Structure, Visual Storytelling Integration, Emotional Resonance & Audience Connection
- **Example Tasks**:
  - Develop brand stories for product launch videos
  - Create comprehensive brand storytelling strategies for rebranding
  - Unify brand voice and story across all video content

### `creative_director.md`
- **Name**: Creative Director
- **Summary**: Senior creative leader who oversees AI video production strategy, brand alignment, and creative vision across all video content and campaigns
- **Focus Areas**: Creative Strategy & Vision Leadership, Brand Alignment & Consistency, Creative Excellence & Quality Standards, Business-Creative Alignment, Team Leadership & Creative Direction
- **Example Tasks**:
  - Establish creative strategy for AI video production across multiple campaigns
  - Elevate AI video content to compete with traditional production quality
  - Balance creative innovation with business objectives

### `executive_producer.md`
- **Name**: Executive Producer
- **Summary**: Senior production leader who oversees AI video production operations, resource allocation, timeline management, and stakeholder coordination across complex video projects
- **Focus Areas**: Production Operations Management, Resource Allocation & Optimization, Timeline & Project Coordination, Stakeholder Management & Communication, Scaling & Process Optimization
- **Example Tasks**:
  - Coordinate multiple AI video projects with competing deadlines
  - Build scalable production processes while maintaining quality
  - Manage stakeholder expectations and communication

### `product_marketing_expert.md`
- **Name**: Product Marketing Expert
- **Summary**: Senior product marketing specialist who excels at translating complex product features into compelling value propositions and creating messaging frameworks that resonate with target audiences
- **Focus Areas**: Audience Analysis & Positioning, Value Proposition Development, Messaging Framework Design, Video Marketing Strategy, Conversion Optimization
- **Example Tasks**:
  - Create high-converting product demo videos for complex B2B products
  - Develop competitive positioning strategies for crowded markets
  - Create unified messaging strategies across all video content

### `product_marketing_video_expert.md`
- **Name**: Product Marketing Video Expert
- **Summary**: Expert in creating AI-generated product demonstration videos, feature showcases, and marketing content that drives sales and customer engagement
- **Focus Areas**: Product Demonstration & Feature Showcases, Sales-Focused Content Strategy, Multi-Channel Marketing Optimization, Competitive Differentiation, Customer Journey Mapping
- **Example Tasks**:
  - Create product demonstration videos that drive sales and conversions
  - Develop multi-platform product marketing strategies
  - Create competitive product videos that differentiate from competitors

### `social_media_content_creator.md`
- **Name**: Social Media Content Creator
- **Summary**: Expert in creating AI-generated video content optimized for social media platforms, viral trends, and mobile-first viewing experiences
- **Focus Areas**: Platform-Specific Optimization, Viral Content Strategy, Mobile-First Design, Social Media Trends & Culture, Multi-Platform Content Strategy
- **Example Tasks**:
  - Create viral TikTok content using AI video generation
  - Develop Instagram Reels that drive engagement
  - Create content optimized for multiple social platforms

---

## 📌 Routing Guidelines

To determine which persona to use:

1. Look for **focus area overlap** between the task and the persona.
2. Check if the task resembles any of the **example tasks** listed.
3. If the task requires more than one domain, select multiple personas.
4. If no persona matches, return:
   > **No matching persona found. Consider defining a new one.**

---

## 🔁 Common Tasks and Suggested Agents

| Task Pattern | Suggested Persona(s) |
|--------------|----------------------|
| Understanding target audience for video content | `audience_research_expert.md` |
| Developing brand story and narrative | `brand_storytelling_expert.md` |
| Creating product demo videos | `product_marketing_video_expert.md` |
| Managing multiple video projects | `executive_producer.md` |
| Setting creative strategy and vision | `creative_director.md` |
| Creating social media video content | `social_media_content_creator.md` |
| Developing product messaging and positioning | `product_marketing_expert.md` |
| Coordinating stakeholder communication | `executive_producer.md` |
| Ensuring brand consistency across content | `creative_director.md`, `brand_storytelling_expert.md` |
| Optimizing content for conversion | `product_marketing_expert.md`, `product_marketing_video_expert.md` |
| Creating viral or trending content | `social_media_content_creator.md` |
| Researching audience behavior and preferences | `audience_research_expert.md` |
| Balancing creative vision with business goals | `creative_director.md` |
| Scaling video production operations | `executive_producer.md` |

---

## 🛠️ Update Instructions

After adding new personas to this folder, rerun `create_router.md` to regenerate this file.

---

## Notes

- Reword `description`, `examples`, and `focus areas` to be concise and readable.
- Do not copy entire persona content — just summarize and reference the file.
- Only include personas that follow the expected schema.

---
