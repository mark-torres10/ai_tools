# 🗂️ How to Write a Linear Project (Canonical Style Guide)

You are a senior product or engineering lead creating a Linear **Project**. A project defines a significant body of work (e.g., a feature, milestone, or research goal) that spans multiple tickets. It must provide strategic clarity, execution alignment, and clear scoping boundaries.

Use this document as your **source of truth** for authoring all Linear projects. Whether written by humans or AI, all projects must follow the structure and tone defined below.

---

## 🧱 Required Project Structure

### 1. **Title**
- Clear, concise, and scoped to the core deliverable
- Format: Noun + Outcome
- ✅ Example: `User Session Tracking for Study Participants`

---

### 2. **Problem Statement**
- Describe the high-level user, research, or business problem being solved.
- Include any known pain points, behavioral data, or hypotheses.
- Make this readable by both engineering and non-technical stakeholders.

✅ Example:
> Researchers currently cannot link session-level user behavior with post-level engagement in the app. This limits our ability to study engagement patterns, drop-off points, and response sequences in real time.

---

### 3. **Objective & Success Criteria**
- What is the goal of this project? Why now?
- List 2–4 measurable or observable outcomes that signal project success.

✅ Example:
- Users' session data is captured and queryable by research staff
- Session data is joined with post metadata for timeline analysis
- No performance degradation (>95% p95 latency preserved)
- Data coverage >98% of user sessions

---

### 4. **Scope & Deliverables**
- Define what **is in** and **out of scope**
- List major components or workstreams to be delivered
- Clarify boundaries: what this project explicitly does not include

✅ Example:
**In Scope:**
- API for session logging
- Client instrumentation (Web & Mobile)
- Postgres + Parquet storage layer
- Data joining pipeline

**Out of Scope:**
- Long-term user retention modeling (tracked in `USER-RETENTION-ML`)
- Public dashboards or visualizations

---

### 5. **Timeline & Milestones**
- Define key dates: start, milestones, internal/external deadlines
- Break work into **milestones** with clear themes and goals
- Use this for planning velocity and progress tracking

✅ Example:
- Week 1: Planning, instrumentation spec, schema design
- Week 2: Backend API + Parquet ingestion
- Week 3: Data validation + joining pipeline
- Week 4: CI coverage, performance testing, handoff to research

---

### 6. **Team & Stakeholders**
- Who’s working on this? Who owns what?
- Include eng leads, PMs, designers, researchers, and stakeholders
- Tag relevant Linear users if in-app

✅ Example:
- Eng: @marktorres (lead), @julia, @benson
- PM: @diana
- Research: @hannah, @owen
- Reviewers: @techlead, @qa-lead

---

### 7. **Risks & Mitigations**
- List known technical/product risks and how you’ll mitigate them
- Especially useful for research features or non-standard infrastructure

✅ Example:
- Risk: Too much client-side event volume → Mitigation: Add rate-limiting
- Risk: Joins with post metadata slow queries → Mitigation: Add async caching layer

---

### 8. **Related Tickets & Projects**
- Link all associated work: Linear issues, planning docs, past research, or design specs

✅ Example:
- Related Tickets: `MET-221`, `MET-234`, `RND-118`
- PRD: `/planning/b94_sessions/plan_tracking_sessions.md`
- Related Projects: `Outrage Detection MVP`, `Post Metadata Infra Upgrade`

---

## 🧠 Best Practices

- **Top-down clarity**: Your problem statement and objective should be understandable to non-engineers.
- **Execution-aware**: Your scope, timeline, and deliverables should be easily broken into tickets.
- **Traceable**: Reference specs, links, and previous projects/tickets.
- **Testable**: Even though this isn’t a ticket, your success criteria must be measurable.
- **Prioritized**: Projects should be aligned with a sprint, research milestone, or impact OKR.

---

## 📌 Example Linear Project Template
