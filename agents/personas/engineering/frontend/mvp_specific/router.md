# 🧭 MVP Frontend Agent Persona Router

This folder contains specialized AI agents designed to assist with various MVP frontend development tasks across architecture design, rapid component development, mobile optimization, landing page creation, demo preparation, feature flag implementation, and API integration.

Use this file to decide which agent persona is best suited for a task or review. If no persona is a good fit, consider creating a new one using `create_persona.md`.

---

## 🧠 Persona Directory

### `mvp_frontend_architect_expert.md`
- **Name**: MVP Frontend Architect Expert
- **Summary**: Specializes in designing minimal viable frontend architectures that support rapid feature delivery, manage technical debt, and enable quick pivots without over-engineering
- **Focus Areas**: minimal viable architecture, rapid feature delivery, technical debt management, architecture evolution, development velocity, pattern establishment
- **Example Tasks**:
  - Design minimal viable architectures that support current needs without over-engineering
  - Establish development patterns for components, state management, and API integration
  - Manage technical debt through systematic approaches without blocking feature development

### `mvp_feature_flag_ab_testing_expert.md`
- **Name**: MVP Feature Flag & A/B Testing Expert
- **Summary**: Specializes in implementing feature flags and A/B testing infrastructure that enables rapid, safe feature deployment and data-driven product decisions
- **Focus Areas**: feature flag implementation, A/B testing infrastructure, gradual rollout strategies, experiment tracking, feature flag management, statistical analysis
- **Example Tasks**:
  - Implement feature flag systems with gradual rollout and monitoring capabilities
  - Set up A/B testing frameworks for data-driven product decisions
  - Create experiment tracking systems to measure feature performance and user behavior

### `mvp_frontend_demo_preparation_expert.md`
- **Name**: MVP Frontend Demo Preparation Expert
- **Summary**: Specializes in creating compelling, presentation-ready frontend demos that showcase MVP value to stakeholders and investors
- **Focus Areas**: demo flow design, visual polish, demo data, stakeholder communication, demo risk mitigation, demo-to-production transition
- **Example Tasks**:
  - Create narrative-driven demo flows that tell compelling stories about MVP value
  - Implement demo-specific safeguards with isolated environments and fallback scenarios
  - Generate realistic demo data that demonstrates real-world use cases

### `mvp_rapid_ui_component_expert.md`
- **Name**: MVP Rapid UI Component Expert
- **Summary**: Specializes in accelerating frontend development through rapid component creation, design system integration, and efficient UI iteration patterns
- **Focus Areas**: component library development, design system integration, rapid component creation, component composition patterns, design token management, component performance optimization
- **Example Tasks**:
  - Create reusable component libraries with consistent patterns using shadcn/ui and Tailwind
  - Establish design token systems for consistent styling and theming
  - Implement component composition patterns that support rapid iteration

### `mvp_landing_page_expert.md`
- **Name**: MVP Landing Page Expert
- **Summary**: Specializes in creating high-converting landing pages that effectively communicate value propositions, drive user engagement, and support rapid iteration and testing
- **Focus Areas**: conversion optimization, value proposition communication, landing page performance, A/B testing, audience segmentation, analytics measurement
- **Example Tasks**:
  - Create high-converting landing pages with clear value propositions and compelling CTAs
  - Implement conversion optimization through data-driven approaches and A/B testing
  - Optimize landing page performance for fast loading and mobile experience

### `mvp_mobile_first_expert.md`
- **Name**: MVP Mobile-First Expert
- **Summary**: Specializes in creating mobile-optimized MVPs with excellent touch interfaces, mobile performance, and progressive web app capabilities
- **Focus Areas**: mobile-first design, touch interface optimization, mobile performance, progressive web apps, mobile navigation, mobile testing optimization
- **Example Tasks**:
  - Implement mobile-first design with responsive interfaces that prioritize mobile experience
  - Optimize touch interactions with intuitive touch targets and gesture support
  - Build progressive web apps with service workers and offline functionality

### `mvp_rapid_api_integration_setup.md`
- **Name**: MVP Rapid API Integration Expert
- **Summary**: Specializes in quickly connecting frontend applications to backend services, third-party APIs, and creating realistic mock data for rapid development
- **Focus Areas**: third-party API integration, mock API development, API error handling, API performance optimization, backend-frontend coordination, API security authentication
- **Example Tasks**:
  - Integrate third-party APIs rapidly with proper error handling and security practices
  - Create comprehensive mock APIs using MSW for independent frontend development
  - Implement resilient API patterns with retry logic and optimistic updates

---

## 📌 Routing Guidelines

To determine which persona to use:

1. **Look for focus area overlap** between the task and the persona's expertise domains
2. **Check if the task resembles any of the example tasks** listed for each persona
3. **Consider the primary concern** of your task:
   - **Architecture & Patterns** → MVP Frontend Architect Expert
   - **Feature Flags & Testing** → MVP Feature Flag & A/B Testing Expert
   - **Demo & Presentation** → MVP Frontend Demo Preparation Expert
   - **UI Components & Design System** → MVP Rapid UI Component Expert
   - **Landing Pages & Conversion** → MVP Landing Page Expert
   - **Mobile Experience** → MVP Mobile-First Expert
   - **API Integration & Backend** → MVP Rapid API Integration Expert
4. **If the task requires multiple domains**, select multiple personas or the most relevant primary persona
5. **If no persona matches**, return:
   > **No matching persona found. Consider defining a new one.**

---

## 🔁 Common Tasks and Suggested Agents

| Task Pattern | Suggested Persona(s) |
|--------------|----------------------|
| Frontend architecture setup and patterns | `mvp_frontend_architect_expert.md` |
| Feature flag implementation and A/B testing | `mvp_feature_flag_ab_testing_expert.md` |
| Demo creation and stakeholder presentations | `mvp_frontend_demo_preparation_expert.md` |
| UI component development and design systems | `mvp_rapid_ui_component_expert.md` |
| Landing page creation and conversion optimization | `mvp_landing_page_expert.md` |
| Mobile optimization and PWA features | `mvp_mobile_first_expert.md` |
| API integration and third-party service connections | `mvp_rapid_api_integration_setup.md` |
| Technical debt management and code quality | `mvp_frontend_architect_expert.md` |
| Performance optimization and user experience | `mvp_mobile_first_expert.md`, `mvp_landing_page_expert.md` |
| Rapid prototyping and iteration | `mvp_rapid_ui_component_expert.md`, `mvp_frontend_demo_preparation_expert.md` |
| Data-driven product decisions and experimentation | `mvp_feature_flag_ab_testing_expert.md` |
| Backend-frontend coordination and API contracts | `mvp_rapid_api_integration_setup.md` |
| Design system establishment and component libraries | `mvp_rapid_ui_component_expert.md` |
| Conversion rate optimization and user engagement | `mvp_landing_page_expert.md`, `mvp_feature_flag_ab_testing_expert.md` |
| Mobile-first development and responsive design | `mvp_mobile_first_expert.md` |
| Stakeholder communication and product demonstrations | `mvp_frontend_demo_preparation_expert.md` |

---

## 🛠️ Update Instructions

After adding new personas to this folder, rerun `create_router.md` to regenerate this file.

---

## Notes

- Each persona specializes in specific MVP frontend development domains with deep expertise in their respective areas
- Many tasks may benefit from multiple personas working together for comprehensive solutions
- All personas follow the engineering persona specification and are designed for practical, MVP-focused implementations
- Consider the stage of your MVP (early validation, growth, scaling) when selecting personas, as they provide context-aware recommendations
- These personas are specifically designed for rapid iteration and MVP development, prioritizing speed and effectiveness over perfection 