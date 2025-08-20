# 🧭 Agent Persona Router

This folder contains specialized AI agents designed to assist with various research methodology tasks across exploratory analysis, hypothesis development, statistical analysis, and result interpretation workflows.

Use this file to decide which agent persona is best suited for a task or review. If no persona is a good fit, consider creating a new one using `create_persona.md`.

---

## 🧠 Persona Directory

### `exploratory_analysis_expert.md`
- **Name**: Exploratory Analysis Expert
- **Summary**: Specializes in systematic data exploration, pattern discovery, and preliminary hypothesis generation through comprehensive data investigation
- **Focus Areas**: EDA, pattern discovery, data quality assessment, hypothesis generation, visualization strategy, feature exploration
- **Example Tasks**:
  - Design systematic data exploration strategies for new datasets
  - Identify hidden patterns and relationships in complex data
  - Assess data quality issues before formal analysis

### `hypothesis_generation_expert.md`
- **Name**: Hypothesis Generation Expert
- **Summary**: Specializes in developing testable research hypotheses, theoretical frameworks, and focused research questions with clear operational definitions
- **Focus Areas**: hypothesis development, theoretical frameworks, research questions, causal mechanisms, operational definitions, falsifiability
- **Example Tasks**:
  - Transform exploratory findings into testable predictions
  - Build comprehensive theoretical models for research areas
  - Refine broad research questions into specific, testable hypotheses

### `statistical_analysis_expert.md`
- **Name**: Statistical Analysis Expert
- **Summary**: Specializes in statistical methodology, test selection, and statistical inference with focus on rigor and appropriate test choice
- **Focus Areas**: statistical test selection, assumption testing, power analysis, statistical inference, multivariate analysis, robust statistics
- **Example Tasks**:
  - Choose appropriate statistical tests for research questions
  - Design comprehensive statistical analysis plans
  - Conduct power analysis and sample size planning

### `topic_modeling_expert.md`
- **Name**: Topic Modeling Expert
- **Summary**: Specializes in topic modeling methodologies, from classical LDA to modern neural approaches, with deep expertise in model selection, evaluation, and interpretation
- **Focus Areas**: Topic Model Selection & Architecture, Model Evaluation & Validation, Hyperparameter Optimization, Domain-Specific Adaptation, Interpretability & Human Evaluation
- **Example Tasks**:
  - Choose between LDA and BERTopic for different text types
  - Troubleshoot topic model quality and coherence issues
  - Evaluate topic models for publication with proper metrics

### `scientific_visualization_specialist.md`
- **Name**: Scientific Visualization Specialist
- **Summary**: Specializes in scientific data visualization, with deep expertise in creating publication-ready figures, interactive dashboards, and effective visual communication
- **Focus Areas**: Scientific Figure Design & Publication Standards, Interactive Visualization & Dashboard Creation, Data-Ink Ratio & Visual Clarity, Color Theory & Accessibility
- **Example Tasks**:
  - Create publication-ready visualizations for complex research findings
  - Design interactive dashboards for exploratory data analysis
  - Optimize visualizations for clarity and accessibility

### `result_interpretation_expert.md`
- **Name**: Result Interpretation Expert
- **Summary**: Specializes in interpreting research findings, assessing practical significance, and translating results into actionable insights for different audiences
- **Focus Areas**: result interpretation, practical significance, statistical vs clinical significance, effect size interpretation, limitation analysis, communication strategy
- **Example Tasks**:
  - Interpret statistical results and assess practical implications
  - Communicate findings effectively to different audiences
  - Analyze study limitations and alternative explanations

---

## 📌 Routing Guidelines

To determine which persona to use:

1. **Look for focus area overlap** between the task and the persona's expertise
2. **Check if the task resembles any of the example tasks** listed above
3. **Consider the research stage** - exploratory, hypothesis development, analysis, or interpretation
4. **If the task requires multiple domains**, select multiple personas for collaboration
5. **If no persona matches**, return:
   > **No matching persona found. Consider defining a new one.**

---

## 🔁 Common Tasks and Suggested Agents

| Task Pattern | Suggested Persona(s) |
|--------------|----------------------|
| "I have new data and need to understand what's in it" | `exploratory_analysis_expert.md` |
| "I found patterns but need to develop testable hypotheses" | `hypothesis_generation_expert.md` |
| "What statistical test should I use for my data?" | `statistical_analysis_expert.md` |
| "What do my results actually mean?" | `result_interpretation_expert.md` |
| "I need to plan my research approach" | `exploratory_analysis_expert.md` + `hypothesis_generation_expert.md` |
| "I have results but need to communicate them" | `result_interpretation_expert.md` |
| "My hypothesis wasn't supported - how should I interpret this?" | `result_interpretation_expert.md` + `statistical_analysis_expert.md` |
| "I need to build a theoretical framework" | `hypothesis_generation_expert.md` |
| "How should I check my data quality?" | `exploratory_analysis_expert.md` |
| "What's the practical significance of my findings?" | `result_interpretation_expert.md` |
| "I need to choose a topic modeling approach" | `topic_modeling_expert.md` |
| "My topic model isn't working well" | `topic_modeling_expert.md` |
| "I need to create publication figures" | `scientific_visualization_specialist.md` |
| "I need an interactive dashboard" | `scientific_visualization_specialist.md` |
| "I need to visualize complex data" | `scientific_visualization_specialist.md` |

---

## 🛠️ Update Instructions

After adding new personas to this folder, rerun `create_router.md` to regenerate this file.

---

## Notes

- These personas focus on research methodology and design rather than technical implementation
- They collaborate with engineering personas when technical infrastructure is needed
- Each persona specializes in a specific research stage while maintaining awareness of the broader research process
- Consider using multiple personas for complex research planning that spans multiple stages
- New specialized personas (Topic Modeling Expert, Scientific Visualization Specialist) provide deep expertise in specific research methodologies
