# 🧭 Analytics Agent Persona Router

This folder contains specialized AI agents for product analytics, experimentation, and growth engineering tasks.

Use this file to decide which agent persona is best suited for analytics-related tasks. If no persona is a good fit, consider creating a new one using the persona creation templates.

---

## 🧠 Persona Directory

### `growth_engineer.md`
- **Name**: Growth Engineer
- **Summary**: Drives measurable product growth through rigorous A/B testing, feature flags, and statistical experimentation
- **Focus Areas**: A/B testing, experimentation methodology, feature flags, statistical rigor, sample size calculation, randomization, SRM detection, experiment analysis
- **Key Expertise**:
  - Design trustworthy online controlled experiments (A/B tests, multivariate tests)
  - Implement proper randomization and variant assignment
  - Detect and debug Sample Ratio Mismatches (SRM)
  - Calculate statistical power, sample sizes, and minimum detectable effects
  - Build experimentation platforms with PostHog, Optimizely, LaunchDarkly
- **Example Tasks**:
  - Setting up A/B test for 3 homepage variants with proper statistical power
  - Implementing feature flag system with consistent user assignment
  - Debugging Sample Ratio Mismatch in running experiment
  - Calculating required sample size for 2% minimum detectable effect
  - Building automated SRM detection and alerting
  - Implementing hash-based randomization for user assignment

### `product_analyst.md`
- **Name**: Product Analyst
- **Summary**: Translates business questions into measurable metrics, designs event taxonomies, and extracts actionable insights from user behavior data
- **Focus Areas**: metric definition, event taxonomy, dashboard design, cohort analysis, retention analysis, funnel optimization, data visualization, tracking plans
- **Key Expertise**:
  - Define metrics using HEART, AARRR, and North Star frameworks
  - Design scalable event taxonomies and tracking plans
  - Build decision-oriented dashboards in PostHog/Amplitude
  - Perform cohort analysis and segmentation
  - Distinguish correlation from causation
  - Communicate insights through data storytelling
- **Example Tasks**:
  - Defining what "engagement" means with specific, measurable metrics
  - Designing event taxonomy with consistent naming convention
  - Building product health dashboard tracking DAU, activation, retention
  - Analyzing funnel drop-off to identify friction points
  - Creating cohorts to compare activated vs non-activated users
  - Setting up automated alerts for metric anomalies

---

## 📌 Routing Guidelines

To determine which persona to use:

### Use **Growth Engineer** when:
- ✅ Designing or implementing A/B tests or experiments
- ✅ Setting up feature flag infrastructure
- ✅ Calculating statistical power or sample sizes
- ✅ Debugging experiment data quality (SRM, instrumentation bugs)
- ✅ Implementing randomization or variant assignment
- ✅ Building experimentation platforms
- ✅ Analyzing experiment results with statistical rigor
- ✅ Technical implementation of tracking for experiments

### Use **Product Analyst** when:
- ✅ Defining product metrics (engagement, retention, activation)
- ✅ Choosing which metrics to track and why
- ✅ Designing event tracking schemas and naming conventions
- ✅ Building dashboards for product health monitoring
- ✅ Analyzing user behavior patterns (funnels, cohorts, paths)
- ✅ Extracting insights from analytics data
- ✅ Communicating data-driven recommendations to stakeholders
- ✅ Setting up product analytics infrastructure (PostHog, Amplitude)

### Use **Both** when:
- ✅ Launching new features with tracking + experimentation
- ✅ Setting up complete analytics + experimentation stack
- ✅ Product Analyst defines metrics → Growth Engineer implements experiment
- ✅ Growth Engineer runs experiment → Product Analyst analyzes broader impact

---

## 🔁 Common Tasks and Suggested Agents

| Task Pattern | Suggested Agent(s) |
|--------------|-------------------|
| "Set up A/B test for 3 variants" | `growth_engineer.md` |
| "Calculate sample size needed for experiment" | `growth_engineer.md` |
| "Implement feature flags with PostHog" | `growth_engineer.md` |
| "Debug Sample Ratio Mismatch in experiment" | `growth_engineer.md` |
| "Define what 'engagement' means for our product" | `product_analyst.md` |
| "Create event taxonomy and naming convention" | `product_analyst.md` |
| "Build dashboard showing retention cohorts" | `product_analyst.md` |
| "Analyze where users drop off in signup funnel" | `product_analyst.md` |
| "Track clicks, comments, likes, and dwell time" | `product_analyst.md` → then `growth_engineer.md` for experiments |
| "Set up product analytics from scratch" | Both: `product_analyst.md` (metrics) + `growth_engineer.md` (infrastructure) |
| "Analyze experiment results by user segment" | Both: `growth_engineer.md` (statistical analysis) + `product_analyst.md` (cohort insights) |

---

## 🎯 Workflow: Analytics + Experimentation

For comprehensive analytics and experimentation setup:

**Phase 1: Metric Definition** (Product Analyst)
- Define North Star metric and key metrics
- Choose framework (HEART, AARRR)
- Define success criteria and guardrails

**Phase 2: Event Tracking** (Product Analyst)
- Design event taxonomy and naming convention
- Create tracking plan
- Implement schema validation

**Phase 3: Dashboard Setup** (Product Analyst)
- Build product health dashboards
- Set up funnels, retention, cohorts
- Configure automated alerts

**Phase 4: Experimentation** (Growth Engineer)
- Design A/B test methodology
- Calculate sample sizes and power
- Implement feature flags and randomization
- Set up SRM detection

**Phase 5: Analysis & Iteration** (Both)
- Product Analyst: Extract insights, segment analysis, storytelling
- Growth Engineer: Statistical analysis, experiment conclusions
- Both: Communicate findings, drive product decisions

---

## 🛠️ Tool Specialization

### PostHog Coverage:
- **Product Analyst**: Insights, dashboards, funnels, retention, cohorts, user paths
- **Growth Engineer**: Feature flags, experiments, exposure tracking, statistical testing

### Other Tools:
- **Amplitude/Mixpanel**: Product Analyst (analytics focus)
- **Optimizely/LaunchDarkly**: Growth Engineer (experimentation focus)
- **SQL Analysis**: Both (custom queries and analysis)

---

## 🛠️ Update Instructions

After adding new analytics personas to this folder, rerun the router generation to update this file.

---

## Notes

- Growth Engineer focuses on **technical implementation** and **statistical rigor** of experiments
- Product Analyst focuses on **metric definition** and **insight extraction**
- They work together: Product Analyst defines what to measure, Growth Engineer ensures it's measured trustworthily
- Both are essential for data-driven product development

