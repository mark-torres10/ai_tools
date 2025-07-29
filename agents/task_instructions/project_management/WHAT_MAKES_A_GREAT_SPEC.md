# ✅ Spec Evaluation Criteria by Stakeholder Persona

Each stakeholder evaluates a spec based on their unique goals and concerns. Use these criteria to assess and refine specs before work begins.

---

## 🧭 Product Manager (PM)

1. **Clarity of Problem Statement**
   - **1** – Vague, jargon-filled, or missing entirely.
   - **3** – Reasonably clear, but lacks context or business framing.
   - **5** – Clearly states the problem, affected users, and why it matters.
   - **Success:** Any stakeholder can understand the “why” within 30 seconds.

2. **User & Business Impact**
   - **1** – No measurable impact or user value identified.
   - **3** – High-level impact noted but lacks detail or evidence.
   - **5** – Specific, measurable outcomes tied to product or business goals.
   - **Success:** Spec includes hypotheses, OKRs, or KPIs to track.

3. **Prioritization Justification**
   - **1** – No rationale for why this is being prioritized now.
   - **3** – Mentions timing or urgency but lacks comparison to alternatives.
   - **5** – Explicit reasoning about trade-offs, urgency, and opportunity cost.
   - **Success:** PM can defend this priority choice in roadmap reviews.

4. **Scope Definition**
   - **1** – Scope creep risk: unclear boundaries or adjacent features mentioned.
   - **3** – Rough scoping with known unknowns but lacks clarity on exclusions.
   - **5** – Clear in-scope, out-of-scope, and future work demarcation.
   - **Success:** Engineering can estimate confidently with minimal follow-ups.

5. **Alignment with Strategy**
   - **1** – No connection to company, team, or user strategy.
   - **3** – Loosely references strategic pillars or themes.
   - **5** – Explicitly maps to strategic goals with links or references.
   - **Success:** PM can point to a strategic document that justifies the spec.

---

## ⚙️ Engineering Lead / Staff Engineer

1. **Technical Feasibility**
   - **1** – Mentions features without considering existing systems.
   - **3** – Assumes feasibility but lacks validation or constraints.
   - **5** – Includes engineering feedback, feasibility notes, or spike results.
   - **Success:** No major re-scoping needed during implementation.

2. **Defined Interfaces and Dependencies**
   - **1** – No mention of systems, APIs, or dependencies.
   - **3** – High-level references to integration points, but unclear ownership.
   - **5** – Precise definitions of dependencies, contracts, and teams involved.
   - **Success:** Engineers know exactly what needs to be built and where it plugs in.

3. **Risk Assessment**
   - **1** – No risks listed or hand-waved as low.
   - **3** – Generic risks listed with no mitigations.
   - **5** – Realistic, project-specific risks with mitigation plans.
   - **Success:** Known risks are proactively flagged and de-risked.

4. **Edge Cases & Failure Modes**
   - **1** – No mention of edge cases or system failures.
   - **3** – Mentions some cases but lacks completeness.
   - **5** – Clearly thought through “what ifs,” failure handling, and fallback behavior.
   - **Success:** Reviewers can’t easily surface missing cases.

5. **Estimability**
   - **1** – Ambiguous requirements prevent effort estimates.
   - **3** – Partial clarity; engineers need follow-up to size tasks.
   - **5** – Well-scoped with story-level clarity for ticketing.
   - **Success:** Tasks can be broken down and assigned with confidence.

---

## 🎨 Design Lead / UX Researcher

1. **User Journey Coverage**
   - **1** – No mention of user flow or interaction context.
   - **3** – Touches on UX but missing key flows or entry points.
   - **5** – End-to-end user flows and edge scenarios described.
   - **Success:** Designers know what screens or components are needed.

2. **Design System Integration**
   - **1** – Introduces new UI elements without justification.
   - **3** – Mentions design system but lacks references or specs.
   - **5** – Uses existing components or justifies new additions.
   - **Success:** Designs can reuse components with minimal custom styling.

3. **Accessibility Considerations**
   - **1** – Ignores accessibility altogether.
   - **3** – Mentions it, but with no specific concerns addressed.
   - **5** – Identifies potential accessibility challenges and guidelines.
   - **Success:** Designers can confidently apply WCAG or internal standards.

4. **User Validation Evidence**
   - **1** – No user research or signal cited.
   - **3** – Anecdotal feedback or outdated studies referenced.
   - **5** – Synthesizes recent user interviews, surveys, or behavioral data.
   - **Success:** Decisions are grounded in real user pain.

5. **Design/Engineering Handoff Readiness**
   - **1** – Ambiguous descriptions; leaves major UX gaps.
   - **3** – Provides general design intent.
   - **5** – Clear specs, links to wireframes/prototypes, responsive behavior defined.
   - **Success:** Engineers can build without needing to guess interactions.

---

## 📊 Data / Analytics Partner

1. **Success Metrics Defined**
   - **1** – No metrics or unclear definitions.
   - **3** – Mentions metrics without formulas or context.
   - **5** – Defines primary/secondary metrics, formulas, and thresholds.
   - **Success:** Everyone can tell if the project is successful post-launch.

2. **Instrumentation Plan**
   - **1** – No mention of events or data tracking.
   - **3** – Mentions logging but lacks detail.
   - **5** – Specific events, properties, and tagging outlined.
   - **Success:** Instrumentation tickets can be written directly from the spec.

3. **Experimentation Strategy**
   - **1** – No A/B plan or control group identified.
   - **3** – Generic mention of an experiment but lacks design.
   - **5** – Clear test/control groups, sample size needs, and hypotheses.
   - **Success:** The team can launch and interpret an A/B test with confidence.

4. **Data Dependencies**
   - **1** – No mention of upstream or downstream data impacts.
   - **3** – Lists some dependencies but unclear source or freshness.
   - **5** – Describes exact data sources, latency, ownership.
   - **Success:** Data flows are known and reliable for analysis.

5. **Dashboard / Reporting Plan**
   - **1** – No dashboard or plan to review performance.
   - **3** – Mentions reporting but unclear metrics or audience.
   - **5** – Lists metrics, audience, cadence, and owner.
   - **Success:** Team knows where and how performance will be monitored.

---

## 🧑‍💼 Cross-Functional Stakeholder (e.g., Legal, Marketing, Executive)

1. **Compliance & Regulatory Checks**
   - **1** – No mention of legal/privacy implications.
   - **3** – Mentions "check with legal" but no specifics.
   - **5** – Flags data usage, consent flows, TOS implications.
   - **Success:** Legal partner can review and sign off in <1 day.

2. **Brand Voice & Positioning**
   - **1** – Conflicts with brand guidelines or market messaging.
   - **3** – Brand-conscious but lacks review from comms or marketing.
   - **5** – Aligned with tone, value prop, and visual identity.
   - **Success:** Stakeholders feel confident putting it in front of customers.

3. **Go-To-Market Dependencies**
   - **1** – No mention of comms, support, or training needs.
   - **3** – Mentions launch timing but no downstream coordination.
   - **5** – Lists GTM tasks, owners, and timing implications.
   - **Success:** GTM teams know when and how to support launch.

4. **Cost & Resource Awareness**
   - **1** – Assumes free or unbounded resources.
   - **3** – Mentions cost but no estimate or trade-offs.
   - **5** – Flags infra, headcount, or tooling needs with impact.
   - **Success:** Leadership can assess ROI or trade-offs.

5. **Stakeholder Visibility**
   - **1** – No stakeholders or reviewers mentioned.
   - **3** – Vague list of "to check with" roles.
   - **5** – Named stakeholders with clear sign-off expectations.
   - **Success:** Everyone knows who owns approval and feedback.

---
