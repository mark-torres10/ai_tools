# 🧭 Agent Persona Router

This folder contains specialized AI agents designed to assist with various research workflow tasks across the entire research lifecycle, from initial planning through final synthesis and review.

Use this file to decide which agent persona is best suited for a task or research workflow need. If no persona is a good fit, consider creating a new one using `create_persona.md`.

---

## 🧠 Persona Directory

### `research_pipeline_architect.md`
- **Name**: Research Pipeline Architect
- **Summary**: Specializes in designing and optimizing research workflows and infrastructure for scalable, efficient research pipelines
- **Focus Areas**: Pipeline Design, Workflow Optimization, Scalability Planning, Performance Optimization, Infrastructure Design, Pipeline Orchestration
- **Example Tasks**:
  - Design research pipeline for complex multi-stage analysis
  - Optimize existing research pipeline for better performance
  - Scale research pipeline for larger datasets

### `data_quality_research_expert.md`
- **Name**: Data Quality Research Expert
- **Summary**: Ensures data quality and research reproducibility through comprehensive quality assessment frameworks and validation procedures
- **Focus Areas**: Data Quality Assessment, Quality Validation Procedures, Cross-Condition Quality Consistency, Ongoing Quality Monitoring, Quality Issue Resolution, Quality Documentation
- **Example Tasks**:
  - Assess data quality for new datasets
  - Ensure quality consistency across experimental conditions
  - Set up ongoing data quality monitoring

### `hypothesis_tester.md`
- **Name**: Hypothesis Tester
- **Summary**: Suggests next experiments and tests based on current findings, guiding researchers toward robust hypothesis testing and validation
- **Focus Areas**: Hypothesis Testing Strategy, Experimental Design Suggestion, Validation Strategy Development, Testing Priority Assessment, Causal Inference Testing, Replication Planning
- **Example Tasks**:
  - Plan next tests to validate initial findings
  - Validate unexpected findings with appropriate experiments
  - Prioritize hypotheses for testing with limited resources

### `iteration_coach.md`
- **Name**: Iteration Coach
- **Summary**: Guides iterative improvement cycles and research refinement through systematic enhancement approaches and progress measurement
- **Focus Areas**: Iterative Improvement Cycles, Research Refinement Strategies, Improvement Opportunity Identification, Iteration Planning, Progress Assessment, Iteration Breakout Strategies
- **Example Tasks**:
  - Plan next iteration based on current results
  - Break out of research iteration loops
  - Design systematic improvement cycles

### `research_coordinator.md`
- **Name**: Research Coordinator
- **Summary**: Plans overall research strategy and coordinates activities across all research phases for comprehensive project success
- **Focus Areas**: Research Strategy & Planning, Research Workflow Coordination, Resource Allocation, Research Phase Transitions, Cross-Phase Integration, Progress Monitoring
- **Example Tasks**:
  - Structure new research projects from start to finish
  - Prioritize multiple research directions
  - Coordinate different research phases and transitions

### `research_synthesizer.md`
- **Name**: Research Synthesizer
- **Summary**: Combines findings across analyses and research phases into coherent narratives and comprehensive conclusions
- **Focus Areas**: Research Finding Integration, Cross-Analysis Synthesis, Research Narrative Development, Pattern Identification, Gap Analysis, Comprehensive Conclusion Formation
- **Example Tasks**:
  - Synthesize multiple analyses into coherent story
  - Integrate findings from different research phases
  - Identify gaps in research synthesis

### `result_reviewer.md`
- **Name**: Result Reviewer
- **Summary**: Reviews and critiques intermediate outputs and research quality through systematic review and constructive feedback
- **Focus Areas**: Research Quality Review, Methodological Critique, Result Validation, Research Flaw Identification, Improvement Suggestion, Peer Review Preparation
- **Example Tasks**:
  - Review preliminary results for quality issues
  - Identify potential flaws in research design
  - Prepare results for peer review

---

## 📌 Routing Guidelines

To determine which persona to use:

1. **Look for focus area overlap** between your research workflow need and the persona's expertise
2. **Check if your task resembles** any of the example tasks listed
3. **Consider the research stage** you're in (planning, execution, analysis, synthesis, review)
4. **If the task requires multiple domains**, select multiple personas
5. **If no persona matches**, return:
   > **No matching persona found. Consider defining a new one.**

---

## 🔁 Common Research Workflow Tasks and Suggested Agents

| Task Pattern | Suggested Persona(s) |
|--------------|----------------------|
| Starting a new research project | Research Coordinator |
| Designing research methodology | Research Pipeline Architect, Research Coordinator |
| Ensuring data quality | Data Quality Research Expert |
| Planning experiments and tests | Hypothesis Tester, Research Coordinator |
| Iterating on research approach | Iteration Coach, Result Reviewer |
| Coordinating research phases | Research Coordinator, Research Pipeline Architect |
| Synthesizing multiple findings | Research Synthesizer |
| Reviewing research quality | Result Reviewer, Data Quality Research Expert |
| Optimizing research pipeline | Research Pipeline Architect, Iteration Coach |
| Preparing for peer review | Result Reviewer, Research Synthesizer |
| Scaling research infrastructure | Research Pipeline Architect, Data Quality Research Expert |
| Validating research findings | Hypothesis Tester, Result Reviewer |

---

## 🎯 Research Stage-Based Routing

### **Planning Stage**
- **Research Coordinator** - Overall strategy and resource planning
- **Research Pipeline Architect** - Pipeline and infrastructure design
- **Data Quality Research Expert** - Quality framework planning

### **Execution Stage**
- **Data Quality Research Expert** - Ongoing quality monitoring
- **Research Pipeline Architect** - Pipeline optimization and scaling
- **Iteration Coach** - Improvement cycles and refinement

### **Analysis Stage**
- **Hypothesis Tester** - Next testing and validation planning
- **Result Reviewer** - Quality assessment and improvement
- **Data Quality Research Expert** - Quality validation

### **Synthesis Stage**
- **Research Synthesizer** - Finding integration and narrative development
- **Research Coordinator** - Cross-phase integration coordination
- **Result Reviewer** - Final quality review

### **Review Stage**
- **Result Reviewer** - Comprehensive quality assessment
- **Research Synthesizer** - Synthesis validation
- **Research Coordinator** - Overall project success evaluation

---

## 🛠️ Update Instructions

After adding new personas to this folder, rerun `create_router.md` to regenerate this file.

---

## Notes

- Each persona focuses on specific aspects of research workflow while recognizing when engineering expertise is needed for implementation
- Personas are designed to collaborate with data engineering experts for technical implementation
- Focus on methodological guidance and workflow design rather than technical execution
- All personas maintain awareness of research stage and context for appropriate recommendations
