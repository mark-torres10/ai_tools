# 🧭 Task-Specific Frontend Agent Persona Router

This folder contains specialized AI agents designed to assist with various task-specific frontend development challenges across accessibility, component architecture, testing strategies, performance optimization, and state management.

Use this file to decide which agent persona is best suited for a task or review. If no persona is a good fit, consider creating a new one using `create_persona.md`.

---

## 🧠 Persona Directory

### `accessbility_expert.md`
- **Name**: Frontend Accessibility Expert
- **Summary**: Specializes in implementing WCAG compliance, screen reader optimization, keyboard navigation, and inclusive design patterns to ensure applications are accessible to all users
- **Focus Areas**: WCAG compliance, screen reader optimization, keyboard navigation, semantic HTML ARIA, inclusive design patterns, accessibility testing
- **Example Tasks**:
  - Implement WCAG 2.1 AA/AAA compliance across applications with proper semantic markup
  - Optimize applications for screen readers with proper ARIA labels and navigation
  - Ensure complete keyboard accessibility with proper focus management and shortcuts

### `component_architecture_expert.md`
- **Name**: Frontend Component Architecture Expert
- **Summary**: Specializes in designing scalable component systems, implementing design patterns, and creating reusable component architectures that support rapid development and maintainability
- **Focus Areas**: component design patterns, reusability composition, component API design, performance optimization, design system implementation, component testing strategies
- **Example Tasks**:
  - Design scalable component architectures using atomic design principles and composition patterns
  - Create reusable components, hooks, and utilities that accelerate development
  - Establish consistent component APIs with proper TypeScript definitions and documentation

### `frontend_testing_expert.md`
- **Name**: Frontend Testing Expert
- **Summary**: Specializes in comprehensive frontend testing strategies including unit, integration, E2E, and visual regression testing with focus on test reliability, coverage, and CI/CD integration
- **Focus Areas**: testing strategy architecture, test framework setup, test reliability stability, test coverage optimization, CI/CD integration, test performance
- **Example Tasks**:
  - Set up comprehensive testing infrastructure with Jest, React Testing Library, and Playwright
  - Implement reliable test patterns with proper isolation, mocking, and data management
  - Optimize test performance through parallelization, selective running, and caching strategies

### `performance_optimization_expert.md`
- **Name**: Frontend Performance Optimization Expert
- **Summary**: Specializes in optimizing frontend performance including Core Web Vitals, bundle optimization, rendering performance, and caching strategies to deliver fast, responsive user experiences
- **Focus Areas**: Core Web Vitals optimization, bundle optimization, rendering performance, caching strategies, performance monitoring, memory management
- **Example Tasks**:
  - Optimize Core Web Vitals (LCP, FID, CLS) through image optimization and code splitting
  - Reduce bundle size through tree shaking, dynamic imports, and dependency optimization
  - Implement effective caching strategies for static assets and API responses

### `state_management_expert.md`
- **Name**: Frontend State Management Expert
- **Summary**: Specializes in designing and implementing efficient state management architectures, data flow optimization, and state synchronization patterns for complex frontend applications
- **Focus Areas**: state architecture design, data flow optimization, state synchronization, performance optimization, state persistence, state testing
- **Example Tasks**:
  - Design scalable state management architectures using appropriate patterns and tools
  - Optimize data flow patterns to minimize unnecessary updates and re-renders
  - Implement state synchronization and prevent race conditions across components

---

## 📌 Routing Guidelines

To determine which persona to use:

1. **Look for focus area overlap** between the task and the persona's expertise domains
2. **Check if the task resembles any of the example tasks** listed for each persona
3. **Consider the primary concern** of your task:
   - **Accessibility & WCAG Compliance** → Frontend Accessibility Expert
   - **Component Design & Architecture** → Frontend Component Architecture Expert
   - **Testing Strategy & Quality** → Frontend Testing Expert
   - **Performance & Optimization** → Frontend Performance Optimization Expert
   - **State Management & Data Flow** → Frontend State Management Expert
4. **If the task requires multiple domains**, select multiple personas or the most relevant primary persona
5. **If no persona matches**, return:
   > **No matching persona found. Consider defining a new one.**

---

## 🔁 Common Tasks and Suggested Agents

| Task Pattern | Suggested Persona(s) |
|--------------|----------------------|
| WCAG compliance and accessibility implementation | `accessbility_expert.md` |
| Screen reader optimization and keyboard navigation | `accessbility_expert.md` |
| Component architecture design and patterns | `component_architecture_expert.md` |
| Design system implementation and component libraries | `component_architecture_expert.md` |
| Testing infrastructure setup and strategy | `frontend_testing_expert.md` |
| Test reliability improvement and CI/CD integration | `frontend_testing_expert.md` |
| Core Web Vitals optimization and performance improvement | `performance_optimization_expert.md` |
| Bundle size reduction and load time optimization | `performance_optimization_expert.md` |
| State management architecture and data flow optimization | `state_management_expert.md` |
| State synchronization and race condition prevention | `state_management_expert.md` |
| Inclusive design and user experience accessibility | `accessbility_expert.md` |
| Component reusability and composition patterns | `component_architecture_expert.md` |
| Test coverage improvement and quality assurance | `frontend_testing_expert.md` |
| Memory leak prevention and performance monitoring | `performance_optimization_expert.md` |
| State persistence and offline functionality | `state_management_expert.md` |
| Semantic HTML and ARIA implementation | `accessbility_expert.md` |
| Component performance optimization and memoization | `component_architecture_expert.md` |
| Visual regression testing and UI consistency | `frontend_testing_expert.md` |
| Caching strategies and service worker implementation | `performance_optimization_expert.md` |
| State testing and debugging tools | `state_management_expert.md` |

---

## 🛠️ Update Instructions

After adding new personas to this folder, rerun `create_router.md` to regenerate this file.

---

## Notes

- Each persona specializes in specific frontend development domains with deep expertise in their respective areas
- Many tasks may benefit from multiple personas working together for comprehensive solutions
- All personas follow the engineering persona specification and are designed for practical, production-ready implementations
- Consider the stage of your project (MVP, Growth, Enterprise) when selecting personas, as they provide context-aware recommendations
- These personas focus on specific technical challenges rather than general development, providing specialized expertise for complex frontend problems 