# Research-Grounded Persona Creation Process

## Overview

This guide documents the process for creating deeply knowledgeable, practical AI agent personas that are grounded in real-world expertise rather than generic knowledge. The goal is to create personas that provide actionable, field-tested guidance based on actual best practices from domain experts. You ground all of your results with the Exa MCP.

**Core Principle**: AI agent personas should embody the accumulated wisdom of top practitioners in their field, not just theoretical knowledge. This requires deep research, synthesis, and structured knowledge organization.

## Gold Standard Examples to Study

Before creating a new persona, review these exemplar personas that demonstrate the research-grounded approach:

1. **AI Evals Methodology Expert**: `agents/personas/ai_engineering/domain_specific/ai_evals_methodology_expert.md`
   - Demonstrates deep research synthesis from expert practitioners (Hamel Husain and others)
   - Shows comprehensive phase-based rubric with detailed checklists
   - Rich with concrete examples, pitfalls, and pro tips

2. **LLM Evaluation Platform Architect**: `agents/personas/ai_engineering/domain_specific/llm_evaluation_platform_architect.md`
   - Demonstrates platform/architecture expertise grounded in real-world patterns
   - Shows decision frameworks and implementation guidance
   - Includes detailed technical patterns and code examples

These personas serve as templates for the structure, depth, and practical value that research-grounded personas should achieve.

## The Problem with Generic Personas

**❌ Generic Persona Approach:**
- Relies only on LLM's training data
- Provides surface-level, theoretical advice
- Missing practical insights, common pitfalls, and pro tips
- No structured methodology or checklists
- Limited real-world examples

**✅ Research-Grounded Persona Approach:**
- Deep dive into expert resources (blogs, talks, documentation, papers)
- Captures practitioner wisdom and battle-tested insights
- Includes detailed rubric checklists with phases
- Rich with concrete examples (good vs. bad)
- Documents common pitfalls and pro tips from experts

## The Research Process

### Phase 1: Source Discovery & Collection

**CRITICAL**: You must research deeply before creating the persona. Minimum 10 high-quality sources.

#### Step 1.1: Identify Research Targets

- [ ] **Define the domain**: What specific expertise does this persona need?
- [ ] **Identify key practitioners**: Who are the recognized experts in this field?
- [ ] **Find authoritative sources**: Where do experts share knowledge?

**Source Categories to Search:**
1. **Expert Blogs & Articles**: Practitioner blog posts, technical deep-dives
2. **Conference Talks & Videos**: KubeCon, PyData, industry conferences
3. **Official Documentation**: Framework docs, best practice guides
4. **Academic Papers**: Research papers on methodology, evaluation
5. **Open Source Code**: Real implementations from successful projects
6. **Community Forums**: Reddit, HN, specialized forums with expert discussions
7. **Books & Guides**: Authoritative books on the subject
8. **Podcasts & Interviews**: Expert interviews revealing insights
9. **Case Studies**: Real-world implementation examples
10. **Tool Documentation**: Specific tools used in the domain

**Search Strategy:**
```
Example for "AI Evals Methodology Expert":
- Search: "LLM evaluation best practices"
- Search: "how to build AI evals" + expert names
- Search: "evaluation methodology" + conference talks
- Search: "[Expert Name] evals" (e.g., "Hamel Husain evals")
- Search: "LLM benchmarking mistakes"
- Search: "evaluation dataset design"
- Search: GitHub repos for eval frameworks
- Search: Recent papers on LLM evaluation
```

#### Step 1.2: Deep Source Analysis

For EACH source (minimum 10 sources):

- [ ] **Read/Watch Thoroughly**: Don't skim - deep understanding required
- [ ] **Extract Key Insights**: What are the core learnings?
- [ ] **Identify Patterns**: Do multiple sources emphasize the same points?
- [ ] **Note Contrarian Views**: Where do experts disagree?
- [ ] **Capture Examples**: Concrete examples of good/bad practices
- [ ] **Document Pitfalls**: What mistakes do experts warn against?
- [ ] **Extract Pro Tips**: What shortcuts or advanced techniques do they share?

**Create a Research Log:**
```markdown
## Source 1: [Title/Author/URL]
**Key Insights:**
- Insight 1
- Insight 2

**Notable Quotes:**
- "Direct quote that captures important principle"

**Examples Shared:**
- ✅ GOOD: Example of doing it right
- ❌ BAD: Example of common mistake

**Pitfalls Mentioned:**
- Pitfall 1
- Pitfall 2

**Pro Tips:**
- Tip 1
- Tip 2
```

#### Step 1.3: Iterative Learning Documentation

**CRITICAL**: Create and continuously update `temp_learnings.md` during research.

**Template Structure:**
```markdown
# [Domain] Expert Learnings

## Core Principles Discovered
1. Principle 1 (Source: [link])
2. Principle 2 (Sources: [link1], [link2])

## Common Themes Across Sources
- Theme 1: [Description] (Mentioned in: 7/10 sources)
- Theme 2: [Description] (Mentioned in: 5/10 sources)

## Key Insights by Category

### [Category 1: e.g., "Methodology"]
- Insight 1 (Source: [expert name])
- Insight 2 (Source: [expert name])

### [Category 2: e.g., "Implementation"]
- Insight 1
- Insight 2

## Contrarian Views / Debates
- **View A**: [Description] (Proponent: [expert])
- **View B**: [Description] (Proponent: [expert])
- **Synthesis**: [Your understanding of when each applies]

## Practical Examples Collected

### Good Practices ✅
1. Example 1 (Source: [link])
2. Example 2 (Source: [link])

### Bad Practices / Anti-patterns ❌
1. Anti-pattern 1 (Source: [link])
2. Anti-pattern 2 (Source: [link])

## Common Pitfalls (Frequency-Sorted)
1. Most common pitfall (Mentioned: 8/10 sources)
2. Second most common (Mentioned: 6/10 sources)

## Pro Tips from Experts
- Tip 1 (Expert: [name])
- Tip 2 (Expert: [name])

## Tools & Frameworks Mentioned
- Tool 1: [Use case] (Recommended by: [expert])
- Tool 2: [Use case] (Recommended by: [expert])

## Open Questions / Areas for Further Research
- Question 1
- Question 2

## Sources Consulted
1. [Source 1 - Title, Author, URL]
2. [Source 2 - Title, Author, URL]
...
10. [Source 10 - Title, Author, URL]
```

**Iteration Process:**
1. Read source #1 → Update temp_learnings.md
2. Read source #2 → Update temp_learnings.md (add new insights, reinforce existing)
3. Read source #3 → Update temp_learnings.md (patterns emerging?)
4. Continue until 10+ sources
5. Review temp_learnings.md for patterns and themes

### Phase 2: Knowledge Synthesis

#### Step 2.1: Identify Core Expertise Areas

From your research, extract:
- [ ] **Key domains of knowledge**: What are the main areas this expert covers?
- [ ] **Methodologies**: What processes/frameworks do they use?
- [ ] **Tools & Technologies**: What tech stack do they work with?
- [ ] **Problem-solving approaches**: How do they tackle challenges?

**Example from AI Evals Methodology Expert:**
```
Core Expertise Areas identified from research:
- Evaluation Design (task classification, paradigms, rubric design)
- Metric Selection & Analysis (choosing right metrics, statistical testing)
- Evaluation Best Practices (dataset design, version control, reproducibility)
```

#### Step 2.2: Extract Structured Methodology

From research, identify if experts follow a **structured process** or **methodology**.

**Look for:**
- Sequential steps (Phase 0 → 1 → 2)
- Prerequisites (must do X before Y)
- Decision points (when to use approach A vs. B)
- Quality gates (don't proceed until X is complete)

**Example Pattern Found:**
```
Hamel's Evals Methodology:
1. START with error analysis (foundation)
2. THEN design evals based on real failures
3. THEN implement with right approach
4. THEN integrate into workflow
5. CONTINUOUSLY iterate
```

#### Step 2.3: Organize by Phases

Structure knowledge into logical phases:

- [ ] **Phase 0: Foundation** - What must be done first?
- [ ] **Phase 1: Core Implementation** - What's the MVP?
- [ ] **Phase 2: Integration** - How does it fit into workflows?
- [ ] **Phase 3: Optimization** - How to make it better?
- [ ] **Phase 4: Advanced** - What are advanced techniques?

Each phase should have:
1. **Purpose**: Why this phase matters
2. **Key Insight**: Core principle (often from expert quote)
3. **Checklist Items**: Specific actions to take
4. **Examples**: Concrete good/bad examples
5. **Common Pitfalls**: Mistakes to avoid
6. **Pro Tips**: Expert shortcuts and techniques
7. **Red Flags**: Warning signs you're doing it wrong

## The Rubric Creation Process

### Phase 3: Building the Rubric Checklist

The rubric checklist is the **core value** of a research-grounded persona. It transforms abstract knowledge into actionable steps.

#### Step 3.1: Create Checklist Items

For each phase, create specific, actionable checklist items.

**Checklist Item Format:**
```markdown
- [ ] **Action Item Title**
  - Specific description of what to do
  - Why it matters
  - How to do it
  
  **Examples:**
  - ✅ GOOD: [Concrete example of doing it right]
  - ✅ GOOD: [Another good example]
  - ❌ BAD: [Example of common mistake]
  - ❌ BAD: [Another anti-pattern]
  
  **Common Pitfalls:**
  - **Pitfall Name**: Description (consequence)
  - **Pitfall Name**: Description (consequence)
  
  **Pro Tips:**
  - Tip 1 from expert
  - Tip 2 from expert
```

**Example from Research:**
```markdown
- [ ] **Conduct Manual Error Review**
  - Review a representative sample of model outputs (minimum 50-100 examples)
  - Examine both successful and failed outputs
  - Look at real production data, not synthetic examples
  - Document specific instances where the model fails
  
  **Examples:**
  - ✅ GOOD: Review 100 actual customer support conversations where the AI responded
  - ✅ GOOD: Examine real code generation outputs from your IDE assistant
  - ❌ BAD: Create 20 hypothetical scenarios you think might happen
  - ❌ BAD: Only review outputs that users reported as failures (misses silent failures)
  
  **Common Pitfalls:**
  - **Confirmation bias**: Only looking for errors you expect to find
  - **Sample size too small**: 10-20 examples won't reveal patterns
  
  **Pro Tips:**
  - Use stratified sampling: include easy, medium, hard examples
  - Review outputs chronologically to catch temporal patterns
```

#### Step 3.2: Include Rich Examples

**CRITICAL**: Every major point needs concrete examples.

**Example Categories:**
1. **Good vs. Bad Examples**
   ```markdown
   - ✅ GOOD: "Model correctly extracts due dates from lease agreements in MM/DD/YYYY format"
   - ❌ BAD: "Model produces good outputs" (too vague)
   ```

2. **Code Examples**
   ```python
   # BAD: Same model judges itself
   model = "gpt-4"
   judge = "gpt-4"  # ❌ Circular, biased
   
   # GOOD: Different model as judge
   model = "gpt-4"
   judge = "claude-3-opus"  # ✅ Independent
   ```

3. **Real-World Scenarios**
   ```markdown
   SYNTHETIC (BAD):
   "What is the capital of France?"
   
   REAL (GOOD):
   "hey i need to know the capital city for france im writing 
   a travel blog post and want to make sure i get it right..."
   ```

#### Step 3.3: Document Common Pitfalls

Extract from research all the mistakes experts warn about.

**Pitfall Documentation Format:**
```markdown
**Common Pitfalls:**
- **Pitfall Name**: Clear description (what goes wrong as a result)
- **Pitfall Name**: Clear description (what goes wrong as a result)
```

**Frequency Matters**: If 7/10 sources mention same pitfall → it's critical.

**Example:**
```markdown
**Common Pitfalls:**
- **Synthetic data bias**: GPT-generated questions are too clean, miss real complexity
- **Confirmation bias**: Only looking for errors you expect to find
- **No versioning**: Can't reproduce results from last month
```

#### Step 3.4: Extract Pro Tips

Capture expert shortcuts, advanced techniques, and hard-won wisdom.

**Pro Tip Criteria:**
- ✅ Actionable advice
- ✅ Not obvious to beginners
- ✅ From experienced practitioners
- ✅ Provides shortcut or efficiency gain

**Format:**
```markdown
**Pro Tips:**
- Tip that saves time/money/effort
- Tip that improves quality
- Tip that avoids common mistake
```

**Example:**
```markdown
**Pro Tips:**
- Start with code assertions where possible (faster, cheaper, more reliable)
- Use "tiered" approach: code assertions filter, then LLM-judge on subset
- Sample check: periodically audit ground truth quality
- Red team your evals: try to game them with synthetic data, then fix
```

#### Step 3.5: Define Red Flags

Create "stop and reassess" warnings for critical mistakes.

**Red Flag Format:**
```markdown
**Red Flags in Phase X:**
- 🚨 Critical mistake 1 (consequence)
- 🚨 Critical mistake 2 (consequence)
- 🚨 Critical mistake 3 (consequence)
```

**Example:**
```markdown
**Red Flags in Phase 0:**
- 🚨 You spent <2 hours on error analysis (not enough)
- 🚨 You haven't looked at production data (flying blind)
- 🚨 You're categorizing errors alone (need diverse perspectives)
```

### Phase 4: Persona Structure Assembly

#### Step 4.1: Standard Persona Sections

Every persona should start with these standard sections (brief, 1-2 pages):

```markdown
# [Persona Name]

## Core Identity
[2-3 sentence description of the persona and their expertise]

## Key Expertise Areas
[3-5 main domains, with 3-4 bullet points each]

## Problem-Solving Approach
[How they think about and tackle problems]

## Communication Style
[How they interact and communicate]

## Key Questions You Ask
[5-7 questions they commonly ask]

## Common Challenges You Help Solve
[5-7 typical problems they address]

## Tools & Frameworks You're Familiar With
[Organized by category, sourced from research]

## Success Criteria
[How they measure success]
```

#### Step 4.2: The Detailed Rubric Checklist

**CRITICAL**: This is where the research pays off. The rubric should be 3-10x longer than the standard sections.

**Structure:**
```markdown
---

## [Domain] Rubric Checklist

**CRITICAL**: This rubric MUST be consulted for EVERY [domain]-related task. Work through each section systematically.

[Include key quote or insight from expert research]

### Phase 0: [Phase Name] - [Short Description]
**Purpose**: [Why this phase matters]

[Expert's Key Insight]: "[Powerful quote from research]"

- [ ] **Checklist Item 1**
  - Details
  - Examples (✅/❌)
  - Common Pitfalls
  - Pro Tips

- [ ] **Checklist Item 2**
  - Details
  - Examples (✅/❌)
  - Common Pitfalls
  - Pro Tips

**Red Flags in Phase 0:**
- 🚨 Critical warning 1
- 🚨 Critical warning 2

### Phase 1: [Next Phase]
[Repeat structure]

### Phase 2: [Next Phase]
[Repeat structure]

### Meta-Checklist: How to Use This Rubric
- **For New Projects**: Work through Phases 0→1→2→3 in order
- **For Existing Projects**: Use Phase X continuously
- **Frequency**: [How often to review]

**Remember**: [Final wisdom/principle]
```

#### Step 4.3: Quality Checklist

Before finalizing the persona, verify:

**Research Quality:**
- [ ] Consulted 10+ high-quality sources
- [ ] Captured insights from recognized experts
- [ ] Documented contrarian views and synthesized them
- [ ] Identified consistent patterns across multiple sources
- [ ] Collected concrete examples from research

**Rubric Quality:**
- [ ] Each phase has clear purpose and expert insight
- [ ] Checklist items are specific and actionable
- [ ] Rich examples (✅ GOOD / ❌ BAD) for each major point
- [ ] Common pitfalls documented with consequences
- [ ] Pro tips from experts included
- [ ] Red flags warn about critical mistakes
- [ ] Meta-checklist explains how to use the rubric

**Practical Value:**
- [ ] Persona provides actionable guidance, not just theory
- [ ] Examples are concrete and relatable
- [ ] Pitfalls are realistic and common
- [ ] Pro tips provide real efficiency gains
- [ ] Rubric can be followed step-by-step

## Detailed Breakdown of Gold Standard Examples

### Example 1: AI Evals Methodology Expert

**Reference**: `agents/personas/ai_engineering/domain_specific/ai_evals_methodology_expert.md`

**Research Sources Used:**
- Hamel Husain's blog posts and talks on LLM evals
- HELM evaluation framework documentation
- Papers on LLM evaluation methodology
- Eugene Yan's blog on evaluation best practices
- Conference talks on production LLM evaluation
- Case studies from companies building eval systems

**Key Research Insights Captured:**
1. **"Error analysis is the foundation"** (Hamel - mentioned in 5 sources)
   - Became Phase 0 of rubric
   - Detailed checklist for conducting error analysis
   
2. **"Use real data, not synthetic"** (Hamel - critical principle)
   - Integrated throughout rubric
   - Multiple examples of real vs. synthetic data

3. **"Don't use LLM-as-judge for everything"** (Multiple sources)
   - Became decision matrix in Phase 2
   - Examples of when to use code vs. LLM judges

**Rubric Structure:**
- Phase 0: Foundation (Start With Error Analysis)
- Phase 1: Eval Design (Ground Everything in Truth)
- Phase 2: Eval Implementation (Choose the Right Approach)
- Phase 3: Eval Integration (Make Evals Actionable)
- Phase 4: Continuous Improvement
- Phase 5: Advanced Practices

**Examples of Research → Rubric:**
```
RESEARCH FINDING:
"Biggest mistake is using synthetic data" - Hamel

RUBRIC IMPLEMENTATION:
- [ ] **Use Real Data, Not Synthetic Data**
  - Source evaluation examples from actual production data
  - Examples of real vs. synthetic with explanations
  - Common pitfall: "Synthetic data bias"
  - Pro tip: "For new products without production data: user test with real users"
```

### Example 2: LLM Evaluation Platform Architect

**Reference**: `agents/personas/ai_engineering/domain_specific/llm_evaluation_platform_architect.md`

**Research Sources Used:**
- Hamel's "Keep evals close to code" philosophy
- OpenAI Evals framework architecture
- Braintrust platform design patterns
- LangSmith architecture documentation
- FastAPI/async patterns for LLM orchestration
- Cost optimization strategies from production blogs

**Key Research Insights Captured:**
1. **"Keep prompts in code, not database"** (Hamel - critical insight)
   - Became core principle in Phase 1
   - Detailed rationale and implementation examples

2. **"Start simple, add complexity when needed"** (Multiple sources)
   - Shaped entire rubric philosophy
   - Decision matrix for architecture based on team size

3. **"Evals must run in CI or they won't run at all"** (Common theme)
   - Became Phase 2 focus
   - Detailed CI/CD integration patterns

**Rubric Structure:**
- Phase 0: Foundation (Requirements & Constraints)
- Phase 1: Core Platform (Build Minimum Viable System)
- Phase 2: Integration (Connect to Development Workflow)
- Phase 3: Optimization (Make It Fast and Cheap)
- Phase 4: Reliability (Production-Grade Infrastructure)

## Templates & Checklists

### Research Phase Template

```markdown
# Research Log: [Domain] Expert Persona

## Research Plan
**Domain**: [Specific expertise area]
**Key Questions to Answer**:
1. What are core methodologies?
2. What are common pitfalls?
3. What tools do experts use?
4. What are best practices?

## Sources (Minimum 10)

### Source 1: [Title]
**Author/Creator**: [Name]
**URL**: [Link]
**Type**: [Blog/Video/Paper/Docs]

**Key Insights**:
- 
- 

**Quotes**:
- 

**Examples Captured**:
- ✅ GOOD: 
- ❌ BAD: 

**Pitfalls Mentioned**:
- 

**Pro Tips**:
- 

**Tools/Frameworks**:
- 

---

[Repeat for 10+ sources]

## Synthesis

### Recurring Themes
1. [Theme 1] (Mentioned in X/10 sources)
2. [Theme 2] (Mentioned in Y/10 sources)

### Core Methodology Identified
[If experts follow specific process]

### Key Principles Extracted
1. Principle 1
2. Principle 2

### Phase Structure Identified
- Phase 0: [Name]
- Phase 1: [Name]
- Phase 2: [Name]
```

### Rubric Creation Template

```markdown
### Phase X: [Phase Name] - [One-line Description]
**Purpose**: [Why this phase exists and what it accomplishes]

**[Expert Name]'s Key Insight**: "[Powerful quote from research]"

- [ ] **Action Item Name**
  - Specific guidance on what to do
  - Why it matters
  - How to implement
  
  **Examples:**
  - ✅ GOOD: [Concrete positive example]
  - ✅ GOOD: [Another positive example]
  - ❌ BAD: [Concrete negative example]
  - ❌ BAD: [Another negative example]
  
  **Common Pitfalls:**
  - **Pitfall Name**: Description (consequence)
  - **Pitfall Name**: Description (consequence)
  
  **Pro Tips:**
  - Tip from expert
  - Tip from expert

[Repeat for 3-7 action items per phase]

**⚠️ WARNING**: [If there's a critical prerequisite or common mistake]

**Red Flags in Phase X:**
- 🚨 Critical mistake to avoid
- 🚨 Another critical mistake
- 🚨 Another critical mistake
```

## Success Criteria for Research-Grounded Personas

A well-crafted research-grounded persona should:

**Research Depth:**
- ✅ 10+ high-quality sources consulted
- ✅ Includes insights from recognized domain experts
- ✅ Captures both consensus views and contrarian perspectives
- ✅ Documents sources and attributions
- ✅ Iteratively built knowledge in temp_learnings.md

**Practical Value:**
- ✅ Provides step-by-step actionable guidance
- ✅ Rich with concrete examples (not abstract)
- ✅ Documents real-world pitfalls from experience
- ✅ Includes expert shortcuts and pro tips
- ✅ Has clear red flags for critical mistakes

**Structural Quality:**
- ✅ Organized into logical phases
- ✅ Each phase has clear purpose and expert insight
- ✅ Detailed rubric checklist (3-10x longer than basic persona)
- ✅ Examples for every major point (✅ GOOD / ❌ BAD)
- ✅ Meta-checklist explaining how to use the rubric

**Usability:**
- ✅ Can be followed step-by-step by someone new to domain
- ✅ Balances theory with practical implementation
- ✅ Provides decision frameworks (when to use X vs. Y)
- ✅ Includes tools, frameworks, and resources
- ✅ Measurable success criteria

## Common Mistakes to Avoid

**❌ Insufficient Research:**
- Only consulting 2-3 sources (need 10+)
- Relying solely on LLM knowledge without external research
- Not capturing expert names and attributions
- Skipping temp_learnings.md iteration

**❌ Weak Rubric:**
- Vague checklist items ("make it good")
- Missing examples (no ✅ GOOD / ❌ BAD)
- No common pitfalls documented
- Missing pro tips from experts
- No red flags for critical mistakes

**❌ Poor Structure:**
- No clear phases or progression
- Rubric is just a list without organization
- Missing "how to use this rubric" guidance
- No connection between research and rubric

**❌ Lack of Practicality:**
- Too theoretical, not actionable
- Examples are abstract, not concrete
- Pitfalls are generic, not domain-specific
- No tools or frameworks mentioned

## Final Workflow Summary

**Step-by-Step Process:**

1. **Research Phase**
   - [ ] Define domain and research questions
   - [ ] Find 10+ high-quality sources
   - [ ] Deep read each source
   - [ ] Iteratively update temp_learnings.md
   - [ ] Identify patterns and themes

2. **Synthesis Phase**
   - [ ] Review temp_learnings.md
   - [ ] Extract core expertise areas
   - [ ] Identify methodology/process
   - [ ] Organize into logical phases
   - [ ] Create phase structure

3. **Rubric Creation Phase**
   - [ ] For each phase, create checklist items
   - [ ] Add concrete examples (✅/❌)
   - [ ] Document common pitfalls
   - [ ] Include pro tips from experts
   - [ ] Define red flags
   - [ ] Write meta-checklist

4. **Assembly Phase**
   - [ ] Write standard persona sections
   - [ ] Integrate detailed rubric
   - [ ] Add expert quotes and attributions
   - [ ] Quality check against criteria
   - [ ] Review for clarity and usability

5. **Validation Phase**
   - [ ] Test rubric on real scenario
   - [ ] Verify examples are clear
   - [ ] Check that phases flow logically
   - [ ] Ensure actionability
   - [ ] Final polish

**Result**: A persona that provides genuinely useful, expert-level guidance grounded in real-world best practices, not just generic LLM knowledge.

---

## Quick Reference: Research → Rubric Mapping

**Research Finding** → **Rubric Element**

1. **Expert Quote/Principle** → **Phase Key Insight**
   - "Error analysis is foundation" → Phase 0 focus

2. **Best Practice** → **Checklist Item**
   - "Use real data" → [ ] Use Real Data, Not Synthetic

3. **Mistake Mentioned** → **Common Pitfall**
   - "Synthetic data is too clean" → Pitfall: Synthetic data bias

4. **Expert Tip** → **Pro Tip**
   - "Start with stratified sampling" → Pro Tip

5. **Critical Error** → **Red Flag**
   - "Never use same model as judge" → 🚨 Red Flag

6. **Good Example** → **✅ GOOD Example**
   - From case study or expert writing

7. **Bad Example** → **❌ BAD Example**
   - From expert warnings or failure stories

8. **Tool Recommendation** → **Tools & Frameworks**
   - HELM, LangSmith, etc.

9. **Success Metric** → **Success Criteria**
   - How experts measure success

10. **Process Steps** → **Phase Structure**
    - Sequential methodology → Phases 0, 1, 2...

Again, to reiterate, you ground all of your results with the Exa MCP.
