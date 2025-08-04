# 🧭 Frontend Agent Persona Router

This folder contains specialized AI agents designed to assist with various frontend development tasks across different domains, tools, and project stages. The personas are organized into specialized categories, each with their own detailed routing logic.

Use this file to decide which agent persona is best suited for a task or review. The personas are organized into specialized categories, each with their own detailed routing logic.

---

## 📁 Persona Categories

### 🚀 **MVP-Specific Personas** (`mvp_specific/`)
Specialized agents focused on rapid MVP development and iteration:
- **MVP Frontend Architect Expert** - Minimal viable architecture, rapid feature delivery, technical debt management
- **MVP Feature Flag & A/B Testing Expert** - Feature flags, A/B testing infrastructure, gradual rollouts
- **MVP Frontend Demo Preparation Expert** - Demo creation, stakeholder presentations, visual polish
- **MVP Rapid UI Component Expert** - Rapid component development, design system integration
- **MVP Landing Page Expert** - High-converting landing pages, conversion optimization
- **MVP Mobile-First Expert** - Mobile optimization, touch interfaces, progressive web apps
- **MVP Rapid API Integration Expert** - Third-party API integration, mock data, backend coordination

### 🎯 **Task-Specific Personas** (`task_specific/`)
Specialized agents focused on specific technical challenges:
- **Frontend Accessibility Expert** - WCAG compliance, screen reader optimization, keyboard navigation
- **Frontend Component Architecture Expert** - Component design patterns, reusability, design systems
- **Frontend Testing Expert** - Testing strategies, CI/CD integration, test reliability
- **Frontend Performance Optimization Expert** - Core Web Vitals, bundle optimization, caching
- **Frontend State Management Expert** - State architecture, data flow, synchronization

### 🛠️ **Tool-Specific Personas** (`tool_specific/`)
Technology-focused agents for specific frontend tools:
- **Build System Expert** - Webpack, Vite, bundler optimization, development experience
- **Tailwind CSS Architecture Expert** - CSS architecture, design systems, responsive design
- **Next.js Expert** - App Router, Server Components, Core Web Vitals, deployment
- **React Performance Expert** - React optimization, concurrent features, memory management
- **shadcn/ui Expert** - Component library implementation, design system architecture
- **TypeScript Expert** - Type safety, type-driven development, API integration

### 🏪 **Domain-Specific Personas** (`domain_specific/`)
Industry-focused agents for specific business domains:
- **E-commerce Frontend Expert** - E-commerce UX patterns, shopping cart optimization, checkout flows

---

## 🧠 Persona Directory

### MVP-Specific Personas

#### `mvp_specific/mvp_frontend_architect_expert.md`
- **Name**: MVP Frontend Architect Expert
- **Summary**: Specializes in designing minimal viable frontend architectures that support rapid feature delivery, manage technical debt, and enable quick pivots without over-engineering
- **Focus Areas**: minimal viable architecture, rapid feature delivery, technical debt management, architecture evolution, development velocity, pattern establishment
- **Example Tasks**: Design minimal viable architectures, establish development patterns, manage technical debt systematically

#### `mvp_specific/mvp_feature_flag_ab_testing_expert.md`
- **Name**: MVP Feature Flag & A/B Testing Expert
- **Summary**: Specializes in implementing feature flags and A/B testing infrastructure that enables rapid, safe feature deployment and data-driven product decisions
- **Focus Areas**: feature flag implementation, A/B testing infrastructure, gradual rollout strategies, experiment tracking, feature flag management, statistical analysis
- **Example Tasks**: Implement feature flag systems, set up A/B testing frameworks, create experiment tracking systems

#### `mvp_specific/mvp_frontend_demo_preparation_expert.md`
- **Name**: MVP Frontend Demo Preparation Expert
- **Summary**: Specializes in creating compelling, presentation-ready frontend demos that showcase MVP value to stakeholders and investors
- **Focus Areas**: demo flow design, visual polish, demo data, stakeholder communication, demo risk mitigation, demo-to-production transition
- **Example Tasks**: Create narrative-driven demo flows, implement demo-specific safeguards, generate realistic demo data

#### `mvp_specific/mvp_rapid_ui_component_expert.md`
- **Name**: MVP Rapid UI Component Expert
- **Summary**: Specializes in accelerating frontend development through rapid component creation, design system integration, and efficient UI iteration patterns
- **Focus Areas**: component library development, design system integration, rapid component creation, component composition patterns, design token management, component performance optimization
- **Example Tasks**: Create reusable component libraries, establish design token systems, implement component composition patterns

#### `mvp_specific/mvp_landing_page_expert.md`
- **Name**: MVP Landing Page Expert
- **Summary**: Specializes in creating high-converting landing pages that effectively communicate value propositions, drive user engagement, and support rapid iteration and testing
- **Focus Areas**: conversion optimization, value proposition communication, landing page performance, A/B testing, audience segmentation, analytics measurement
- **Example Tasks**: Create high-converting landing pages, implement conversion optimization, optimize landing page performance

#### `mvp_specific/mvp_mobile_first_expert.md`
- **Name**: MVP Mobile-First Expert
- **Summary**: Specializes in creating mobile-optimized MVPs with excellent touch interfaces, mobile performance, and progressive web app capabilities
- **Focus Areas**: mobile-first design, touch interface optimization, mobile performance, progressive web apps, mobile navigation, mobile testing optimization
- **Example Tasks**: Implement mobile-first design, optimize touch interactions, build progressive web apps

#### `mvp_specific/mvp_rapid_api_integration_setup.md`
- **Name**: MVP Rapid API Integration Expert
- **Summary**: Specializes in quickly connecting frontend applications to backend services, third-party APIs, and creating realistic mock data for rapid development
- **Focus Areas**: third-party API integration, mock API development, API error handling, API performance optimization, backend-frontend coordination, API security authentication
- **Example Tasks**: Integrate third-party APIs rapidly, create comprehensive mock APIs, implement resilient API patterns

### Task-Specific Personas

#### `task_specific/accessbility_expert.md`
- **Name**: Frontend Accessibility Expert
- **Summary**: Specializes in implementing WCAG compliance, screen reader optimization, keyboard navigation, and inclusive design patterns to ensure applications are accessible to all users
- **Focus Areas**: WCAG compliance, screen reader optimization, keyboard navigation, semantic HTML ARIA, inclusive design patterns, accessibility testing
- **Example Tasks**: Implement WCAG 2.1 AA/AAA compliance, optimize for screen readers, ensure complete keyboard accessibility

#### `task_specific/component_architecture_expert.md`
- **Name**: Frontend Component Architecture Expert
- **Summary**: Specializes in designing scalable component systems, implementing design patterns, and creating reusable component architectures that support rapid development and maintainability
- **Focus Areas**: component design patterns, reusability composition, component API design, performance optimization, design system implementation, component testing strategies
- **Example Tasks**: Design scalable component architectures, create reusable components and utilities, establish consistent component APIs

#### `task_specific/frontend_testing_expert.md`
- **Name**: Frontend Testing Expert
- **Summary**: Specializes in comprehensive frontend testing strategies including unit, integration, E2E, and visual regression testing with focus on test reliability, coverage, and CI/CD integration
- **Focus Areas**: testing strategy architecture, test framework setup, test reliability stability, test coverage optimization, CI/CD integration, test performance
- **Example Tasks**: Set up comprehensive testing infrastructure, implement reliable test patterns, optimize test performance

#### `task_specific/performance_optimization_expert.md`
- **Name**: Frontend Performance Optimization Expert
- **Summary**: Specializes in optimizing frontend performance including Core Web Vitals, bundle optimization, rendering performance, and caching strategies to deliver fast, responsive user experiences
- **Focus Areas**: Core Web Vitals optimization, bundle optimization, rendering performance, caching strategies, performance monitoring, memory management
- **Example Tasks**: Optimize Core Web Vitals, reduce bundle size, implement effective caching strategies

#### `task_specific/state_management_expert.md`
- **Name**: Frontend State Management Expert
- **Summary**: Specializes in designing and implementing efficient state management architectures, data flow optimization, and state synchronization patterns for complex frontend applications
- **Focus Areas**: state architecture design, data flow optimization, state synchronization, performance optimization, state persistence, state testing
- **Example Tasks**: Design scalable state management architectures, optimize data flow patterns, implement state synchronization

### Tool-Specific Personas

#### `tool_specific/build_system_expert.md`
- **Name**: Build System Expert
- **Summary**: Master-level frontend engineer specializing in build system optimization, bundler configuration, and development experience enhancement for modern web applications
- **Focus Areas**: build system architecture, development experience, bundle optimization, monorepo build systems, performance optimization
- **Example Tasks**: Configure and optimize Webpack/Vite, implement code splitting strategies, set up efficient monorepo build systems

#### `tool_specific/tailwind_architecture_expert.md`
- **Name**: Tailwind CSS Architecture Expert
- **Summary**: Master-level frontend engineer specializing in CSS architecture, design systems, and Tailwind CSS implementation for scalable, maintainable styling systems
- **Focus Areas**: CSS architecture, Tailwind CSS mastery, design token management, responsive design, performance optimization
- **Example Tasks**: Create comprehensive design systems, optimize CSS bundle size, implement mobile-first responsive design

#### `tool_specific/nextjs_expert.md`
- **Name**: Next.js Expert
- **Summary**: Master-level frontend engineer specializing in Next.js 13+ App Router architecture, performance optimization, and modern React patterns including Server Components and streaming SSR
- **Focus Areas**: Next.js 13+ App Router, server components streaming, performance optimization, deployment infrastructure, data fetching caching, SEO metadata
- **Example Tasks**: Design scalable Next.js applications, optimize Core Web Vitals, implement streaming SSR and Server Components

#### `tool_specific/react_performance_expert.md`
- **Name**: React Performance Expert
- **Summary**: Master-level frontend engineer specializing in React performance optimization, rendering strategies, and modern React patterns including hooks optimization and concurrent features
- **Focus Areas**: React performance optimization, hooks optimization, React 18+ features, memory management, performance profiling
- **Example Tasks**: Optimize React components, implement React 18+ concurrent features, identify and fix memory leaks

#### `tool_specific/shadcn_ui_expert.md`
- **Name**: shadcn/ui Expert
- **Summary**: Master-level frontend engineer specializing in shadcn/ui component library implementation, customization, and design system architecture using shadcn/ui as a foundation
- **Focus Areas**: shadcn/ui component library, design system architecture, component customization theming, accessibility UX, performance optimization
- **Example Tasks**: Set up shadcn/ui with proper integration, create comprehensive design systems, optimize bundle size

#### `tool_specific/typescript_expert.md`
- **Name**: TypeScript Expert
- **Summary**: Master-level frontend engineer specializing in TypeScript integration, type safety, and type-driven development patterns for scalable, maintainable React applications
- **Focus Areas**: TypeScript integration, type safety validation, type-driven development, performance optimization, API type generation
- **Example Tasks**: Configure TypeScript with strict mode, implement comprehensive type safety, automate type generation

### Domain-Specific Personas

#### `domain_specific/ecommerce_frontend_expert.md`
- **Name**: E-commerce Frontend Expert
- **Summary**: Specializes in e-commerce UX patterns, shopping cart optimization, checkout flow design, and conversion optimization for online retail applications
- **Focus Areas**: e-commerce UX patterns, shopping cart optimization, checkout flow design, conversion optimization, mobile commerce, progressive web apps
- **Example Tasks**: Optimize product catalog, implement cart management, integrate payment systems, improve checkout flows

---

## 📌 Routing Guidelines

To determine which persona to use:

### 1. **Identify the Primary Category**
- **MVP Development** (rapid iteration, minimal viable products) → MVP-Specific Personas
- **Technical Challenges** (accessibility, testing, performance, state management) → Task-Specific Personas
- **Tool/Technology Focus** (Next.js, React, TypeScript, build tools) → Tool-Specific Personas
- **Business Domain** (e-commerce, specific industries) → Domain-Specific Personas

### 2. **Match Task Characteristics**
- **Architecture & Patterns** → MVP Frontend Architect Expert
- **Feature Flags & Testing** → MVP Feature Flag & A/B Testing Expert
- **Demo & Presentation** → MVP Frontend Demo Preparation Expert
- **UI Components & Design System** → MVP Rapid UI Component Expert
- **Landing Pages & Conversion** → MVP Landing Page Expert
- **Mobile Experience** → MVP Mobile-First Expert
- **API Integration & Backend** → MVP Rapid API Integration Expert
- **Accessibility & WCAG Compliance** → Frontend Accessibility Expert
- **Component Design & Architecture** → Frontend Component Architecture Expert
- **Testing Strategy & Quality** → Frontend Testing Expert
- **Performance & Optimization** → Frontend Performance Optimization Expert
- **State Management & Data Flow** → Frontend State Management Expert
- **Build Tools & Bundlers** → Build System Expert
- **CSS & Styling Architecture** → Tailwind CSS Architecture Expert
- **Next.js & React Framework** → Next.js Expert
- **React Performance & Optimization** → React Performance Expert
- **Component Libraries & Design Systems** → shadcn/ui Expert
- **TypeScript & Type Safety** → TypeScript Expert
- **E-commerce & Retail** → E-commerce Frontend Expert

### 3. **Consider Complexity**
- **Simple, tool-specific tasks** → Use the relevant Tool-Specific persona
- **Complex technical challenges** → Use the relevant Task-Specific persona
- **MVP and rapid development** → Use MVP-Specific personas
- **Industry-specific requirements** → Use Domain-Specific personas
- **Multi-domain tasks** → Consider multiple personas or the most relevant primary persona

### 4. **If No Match Found**
Return: **No matching persona found. Consider defining a new one.**

---

## 🔁 Common Tasks and Suggested Agents

| Task Pattern | Suggested Persona(s) |
|--------------|----------------------|
| MVP architecture setup and rapid development | `mvp_specific/mvp_frontend_architect_expert.md` |
| Feature flag implementation and A/B testing | `mvp_specific/mvp_feature_flag_ab_testing_expert.md` |
| Demo creation and stakeholder presentations | `mvp_specific/mvp_frontend_demo_preparation_expert.md` |
| UI component development and design systems | `mvp_specific/mvp_rapid_ui_component_expert.md` |
| Landing page creation and conversion optimization | `mvp_specific/mvp_landing_page_expert.md` |
| Mobile optimization and PWA features | `mvp_specific/mvp_mobile_first_expert.md` |
| API integration and third-party service connections | `mvp_specific/mvp_rapid_api_integration_setup.md` |
| WCAG compliance and accessibility implementation | `task_specific/accessbility_expert.md` |
| Component architecture design and patterns | `task_specific/component_architecture_expert.md` |
| Testing infrastructure setup and strategy | `task_specific/frontend_testing_expert.md` |
| Core Web Vitals optimization and performance improvement | `task_specific/performance_optimization_expert.md` |
| State management architecture and data flow optimization | `task_specific/state_management_expert.md` |
| Webpack optimization and bundle size reduction | `tool_specific/build_system_expert.md` |
| Tailwind CSS design system implementation | `tool_specific/tailwind_architecture_expert.md` |
| Next.js App Router architecture and setup | `tool_specific/nextjs_expert.md` |
| React component performance optimization | `tool_specific/react_performance_expert.md` |
| shadcn/ui component library setup and configuration | `tool_specific/shadcn_ui_expert.md` |
| TypeScript strict mode configuration and setup | `tool_specific/typescript_expert.md` |
| E-commerce UX patterns and checkout optimization | `domain_specific/ecommerce_frontend_expert.md` |
| Technical debt management and code quality | `mvp_specific/mvp_frontend_architect_expert.md` |
| Performance optimization and user experience | `task_specific/performance_optimization_expert.md` |
| Rapid prototyping and iteration | `mvp_specific/mvp_rapid_ui_component_expert.md` |
| Data-driven product decisions and experimentation | `mvp_specific/mvp_feature_flag_ab_testing_expert.md` |
| Backend-frontend coordination and API contracts | `mvp_specific/mvp_rapid_api_integration_setup.md` |
| Design system establishment and component libraries | `task_specific/component_architecture_expert.md` |
| Conversion rate optimization and user engagement | `mvp_specific/mvp_landing_page_expert.md` |
| Mobile-first development and responsive design | `mvp_specific/mvp_mobile_first_expert.md` |
| Stakeholder communication and product demonstrations | `mvp_specific/mvp_frontend_demo_preparation_expert.md` |
| Inclusive design and user experience accessibility | `task_specific/accessbility_expert.md` |
| Component reusability and composition patterns | `task_specific/component_architecture_expert.md` |
| Test coverage improvement and quality assurance | `task_specific/frontend_testing_expert.md` |
| Memory leak prevention and performance monitoring | `task_specific/performance_optimization_expert.md` |
| State persistence and offline functionality | `task_specific/state_management_expert.md` |
| Semantic HTML and ARIA implementation | `task_specific/accessbility_expert.md` |
| Component performance optimization and memoization | `task_specific/component_architecture_expert.md` |
| Visual regression testing and UI consistency | `task_specific/frontend_testing_expert.md` |
| Caching strategies and service worker implementation | `task_specific/performance_optimization_expert.md` |
| State testing and debugging tools | `task_specific/state_management_expert.md` |
| Vite migration and development experience enhancement | `tool_specific/build_system_expert.md` |
| CSS bundle optimization and purging strategies | `tool_specific/tailwind_architecture_expert.md` |
| Server Components and streaming SSR implementation | `tool_specific/nextjs_expert.md` |
| React 18+ concurrent features implementation | `tool_specific/react_performance_expert.md` |
| Component customization and theming with shadcn/ui | `tool_specific/shadcn_ui_expert.md` |
| API type generation and end-to-end type safety | `tool_specific/typescript_expert.md` |
| Development experience enhancement and tooling setup | `tool_specific/build_system_expert.md` |
| SEO optimization and metadata management | `tool_specific/nextjs_expert.md` |
| Bundle analysis and performance monitoring | `tool_specific/build_system_expert.md`, `tool_specific/react_performance_expert.md` |
| Accessibility implementation in component libraries | `tool_specific/shadcn_ui_expert.md` |
| Type safety validation and runtime checking | `tool_specific/typescript_expert.md` |
| Shopping cart optimization and checkout flows | `domain_specific/ecommerce_frontend_expert.md` |
| Product catalog optimization and inventory display | `domain_specific/ecommerce_frontend_expert.md` |
| Payment integration and mobile commerce | `domain_specific/ecommerce_frontend_expert.md` |

---

## 📚 Detailed Routing References

For more detailed routing logic within each category, refer to:
- **MVP-Specific Routing**: `mvp_specific/router.md`
- **Task-Specific Routing**: `task_specific/router.md`
- **Tool-Specific Routing**: `tool_specific/router.md`

---

## 🛠️ Update Instructions

After adding new personas to any subdirectory:
1. Update the relevant subdirectory router (`mvp_specific/router.md`, `task_specific/router.md`, or `tool_specific/router.md`)
2. Update this main router to include the new persona
3. Regenerate routing tables and guidelines

---

## Notes

- Each persona specializes in specific frontend development domains with deep expertise in their respective areas
- Many complex tasks may benefit from multiple personas working together for comprehensive solutions
- All personas follow the engineering persona specification and are designed for practical, production-ready implementations
- Consider the stage of your project (MVP, Growth, Enterprise) when selecting personas, as they provide context-aware recommendations
- For comprehensive solutions, consider combining personas from different categories (e.g., MVP + Tool-Specific + Task-Specific)
- These personas are organized to support different development phases and technical challenges, from rapid MVP development to enterprise-scale optimization 