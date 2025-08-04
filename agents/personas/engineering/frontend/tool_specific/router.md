# 🧭 Tool-Specific Frontend Agent Persona Router

This folder contains specialized AI agents designed to assist with various tool-specific frontend development challenges across build systems, CSS frameworks, React frameworks, performance optimization, component libraries, and TypeScript integration.

Use this file to decide which agent persona is best suited for a task or review. If no persona is a good fit, consider creating a new one using `create_persona.md`.

---

## 🧠 Persona Directory

### `build_system_expert.md`
- **Name**: Build System Expert
- **Summary**: Master-level frontend engineer specializing in build system optimization, bundler configuration, and development experience enhancement for modern web applications
- **Focus Areas**: build system architecture, development experience, bundle optimization, monorepo build systems, performance optimization
- **Example Tasks**:
  - Configure and optimize Webpack, Vite, and other bundlers for maximum performance
  - Implement code splitting, tree shaking, and bundle size reduction strategies
  - Set up efficient monorepo build systems with proper caching and dependency management

### `tailwind_architecture_expert.md`
- **Name**: Tailwind CSS Architecture Expert
- **Summary**: Master-level frontend engineer specializing in CSS architecture, design systems, and Tailwind CSS implementation for scalable, maintainable styling systems
- **Focus Areas**: CSS architecture, Tailwind CSS mastery, design token management, responsive design, performance optimization
- **Example Tasks**:
  - Create comprehensive design systems using Tailwind CSS with proper token management
  - Optimize CSS bundle size through purging, layering, and efficient utility usage
  - Implement mobile-first responsive design patterns with proper breakpoint strategies

### `nextjs_expert.md`
- **Name**: Next.js Expert
- **Summary**: Master-level frontend engineer specializing in Next.js 13+ App Router architecture, performance optimization, and modern React patterns including Server Components and streaming SSR
- **Focus Areas**: Next.js 13+ App Router, server components streaming, performance optimization, deployment infrastructure, data fetching caching, SEO metadata
- **Example Tasks**:
  - Design scalable Next.js applications using App Router patterns with proper route organization
  - Optimize Core Web Vitals through bundle analysis, image optimization, and caching strategies
  - Implement streaming SSR and Server Components for better perceived performance

### `react_performance_expert.md`
- **Name**: React Performance Expert
- **Summary**: Master-level frontend engineer specializing in React performance optimization, rendering strategies, and modern React patterns including hooks optimization and concurrent features
- **Focus Areas**: React performance optimization, hooks optimization, React 18+ features, memory management, performance profiling
- **Example Tasks**:
  - Optimize React components through memoization, code splitting, and rendering strategies
  - Implement React 18+ concurrent features for better user experience and performance
  - Identify and fix memory leaks through proper cleanup and resource management

### `shadcn_ui_expert.md`
- **Name**: shadcn/ui Expert
- **Summary**: Master-level frontend engineer specializing in shadcn/ui component library implementation, customization, and design system architecture using shadcn/ui as a foundation
- **Focus Areas**: shadcn/ui component library, design system architecture, component customization theming, accessibility UX, performance optimization
- **Example Tasks**:
  - Set up shadcn/ui with proper TypeScript integration and design token systems
  - Create comprehensive design systems using shadcn/ui as the foundation
  - Optimize bundle size through tree-shaking, lazy loading, and efficient component usage

### `typescript_expert.md`
- **Name**: TypeScript Expert
- **Summary**: Master-level frontend engineer specializing in TypeScript integration, type safety, and type-driven development patterns for scalable, maintainable React applications
- **Focus Areas**: TypeScript integration, type safety validation, type-driven development, performance optimization, API type generation
- **Example Tasks**:
  - Configure TypeScript with strict mode and optimal compiler options for robust type safety
  - Implement comprehensive type safety using advanced TypeScript features and validation libraries
  - Automate type generation from API specifications using OpenAPI, tRPC, or Zod schemas

---

## 📌 Routing Guidelines

To determine which persona to use:

1. **Look for focus area overlap** between the task and the persona's expertise domains
2. **Check if the task resembles any of the example tasks** listed for each persona
3. **Consider the primary concern** of your task:
   - **Build Tools & Bundlers** → Build System Expert
   - **CSS & Styling Architecture** → Tailwind CSS Architecture Expert
   - **Next.js & React Framework** → Next.js Expert
   - **React Performance & Optimization** → React Performance Expert
   - **Component Libraries & Design Systems** → shadcn/ui Expert
   - **TypeScript & Type Safety** → TypeScript Expert
4. **If the task requires multiple domains**, select multiple personas or the most relevant primary persona
5. **If no persona matches**, return:
   > **No matching persona found. Consider defining a new one.**

---

## 🔁 Common Tasks and Suggested Agents

| Task Pattern | Suggested Persona(s) |
|--------------|----------------------|
| Webpack optimization and bundle size reduction | `build_system_expert.md` |
| Vite migration and development experience enhancement | `build_system_expert.md` |
| Monorepo build system setup and optimization | `build_system_expert.md` |
| Tailwind CSS design system implementation | `tailwind_architecture_expert.md` |
| CSS bundle optimization and purging strategies | `tailwind_architecture_expert.md` |
| Responsive design patterns and mobile-first implementation | `tailwind_architecture_expert.md` |
| Next.js App Router architecture and setup | `nextjs_expert.md` |
| Core Web Vitals optimization in Next.js applications | `nextjs_expert.md` |
| Server Components and streaming SSR implementation | `nextjs_expert.md` |
| React component performance optimization and memoization | `react_performance_expert.md` |
| React 18+ concurrent features implementation | `react_performance_expert.md` |
| Memory leak prevention and debugging in React apps | `react_performance_expert.md` |
| shadcn/ui component library setup and configuration | `shadcn_ui_expert.md` |
| Design system architecture using shadcn/ui foundation | `shadcn_ui_expert.md` |
| Component customization and theming with shadcn/ui | `shadcn_ui_expert.md` |
| TypeScript strict mode configuration and setup | `typescript_expert.md` |
| API type generation and end-to-end type safety | `typescript_expert.md` |
| TypeScript compilation performance optimization | `typescript_expert.md` |
| Development experience enhancement and tooling setup | `build_system_expert.md` |
| CSS architecture and design token management | `tailwind_architecture_expert.md` |
| SEO optimization and metadata management | `nextjs_expert.md` |
| Bundle analysis and performance monitoring | `build_system_expert.md`, `react_performance_expert.md` |
| Accessibility implementation in component libraries | `shadcn_ui_expert.md` |
| Type safety validation and runtime checking | `typescript_expert.md` |

---

## 🛠️ Update Instructions

After adding new personas to this folder, rerun `create_router.md` to regenerate this file.

---

## Notes

- Each persona specializes in specific frontend development tools and technologies with deep expertise in their respective areas
- Many tasks may benefit from multiple personas working together for comprehensive solutions
- All personas follow the engineering persona specification and are designed for practical, production-ready implementations
- Consider the stage of your project (MVP, Growth, Enterprise) when selecting personas, as they provide context-aware recommendations
- These personas focus on specific tools and technologies rather than general development, providing specialized expertise for complex tool-specific challenges 