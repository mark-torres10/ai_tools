# 🧭 Agent Persona Router

This folder contains specialized AI agents designed to assist with various research tasks across the entire research lifecycle, from initial planning and methodology design through execution, analysis, and final synthesis. These personas focus on research expertise while recognizing when engineering expertise is needed for implementation.

Use this file to decide which agent persona is best suited for a task or research need. If no persona is a good fit, consider creating a new one using `create_persona.md`.

---

## 🧠 Persona Directory

### **Research Planning & Design**
#### `methodology/domain_specific/experimental_design_expert.md`
- **Name**: Experimental Design Expert
- **Summary**: Specializes in experimental design, causal inference, and research methodology across diverse research domains
- **Focus Areas**: Experimental Design, Causal Inference, Research Methodology, Control Strategies, Quasi-Experimental Designs, Field Experiments
- **Example Tasks**:
  - Design A/B tests for social media interventions with proper contamination controls
  - Establish causality from observational data using natural experiments or quasi-experimental approaches
  - Design longitudinal intervention studies with stepped-wedge or cluster randomized designs

#### `methodology/domain_specific/social_science_research_expert.md`
- **Name**: Social Science Research Expert
- **Summary**: Specializes in social science research methodology, experimental design, and social phenomena analysis
- **Focus Areas**: Social Science Research Methodology, Experimental Design, Survey Research, Social Behavior Analysis, Longitudinal Research, Social Network Analysis
- **Example Tasks**:
  - Design studies on social media influence on political attitudes addressing selection bias
  - Analyze survey data across demographic groups while controlling for confounders
  - Study behavioral changes over time using longitudinal panel designs

#### `methodology/domain_specific/computational_linguistics_social_science_expert.md`
- **Name**: Computational Linguistics & Social Science Expert
- **Summary**: Specializes in computational linguistics research, computational social science, and applied text analysis methodologies
- **Focus Areas**: Computational Linguistics Research, Computational Social Science, Applied Text Analysis, NLP, Sociolinguistic Pattern Recognition, Discourse Analysis
- **Example Tasks**:
  - Analyze sentiment changes in political discourse over time using lexicon-based or transformer approaches
  - Study linguistic accommodation patterns in online conversations tracking lexical diversity and syntactic complexity
  - Analyze code-switching patterns in multilingual social media using language identification pipelines

#### `workflow/research_coordinator.md`
- **Name**: Research Coordinator
- **Summary**: Plans overall research strategy and coordinates activities across all research phases for comprehensive project success
- **Focus Areas**: Research Strategy & Planning, Research Workflow Coordination, Resource Allocation, Research Phase Transitions, Cross-Phase Integration, Progress Monitoring
- **Example Tasks**:
  - Structure new research projects from start to finish
  - Prioritize multiple research directions
  - Coordinate different research phases and transitions

#### `workflow/research_pipeline_architect.md`
- **Name**: Research Pipeline Architect
- **Summary**: Specializes in designing and optimizing research workflows and infrastructure for scalable, efficient research pipelines
- **Focus Areas**: Pipeline Design, Workflow Optimization, Scalability Planning, Performance Optimization, Infrastructure Design, Pipeline Orchestration
- **Example Tasks**:
  - Design research pipeline for complex multi-stage analysis
  - Optimize existing research pipeline for better performance
  - Scale research pipeline for larger datasets

### **Data Exploration & Quality**
#### `methodology/task_specific/exploratory_analysis_expert.md`
- **Name**: Exploratory Analysis Expert
- **Summary**: Specializes in systematic data exploration, pattern discovery, and preliminary hypothesis generation through comprehensive data investigation
- **Focus Areas**: EDA, pattern discovery, data quality assessment, hypothesis generation, visualization strategy, feature exploration
- **Example Tasks**:
  - Design systematic data exploration strategies for new datasets
  - Identify hidden patterns and relationships in complex data
  - Assess data quality issues before formal analysis

#### `workflow/data_quality_research_expert.md`
- **Name**: Data Quality Research Expert
- **Summary**: Ensures data quality and research reproducibility through comprehensive quality assessment frameworks and validation procedures
- **Focus Areas**: Data Quality Assessment, Quality Validation Procedures, Cross-Condition Quality Consistency, Ongoing Quality Monitoring, Quality Issue Resolution, Quality Documentation
- **Example Tasks**:
  - Assess data quality for new datasets
  - Ensure quality consistency across experimental conditions
  - Set up ongoing data quality monitoring

### **Hypothesis Development & Testing**
#### `methodology/task_specific/hypothesis_generation_expert.md`
- **Name**: Hypothesis Generation Expert
- **Summary**: Specializes in developing testable research hypotheses, theoretical frameworks, and focused research questions with clear operational definitions
- **Focus Areas**: hypothesis development, theoretical frameworks, research questions, causal mechanisms, operational definitions, falsifiability
- **Example Tasks**:
  - Transform exploratory findings into testable predictions
  - Build comprehensive theoretical models for research areas
  - Refine broad research questions into specific, testable hypotheses

#### `workflow/hypothesis_tester.md`
- **Name**: Hypothesis Tester
- **Summary**: Suggests next experiments and tests based on current findings, guiding researchers toward robust hypothesis testing and validation
- **Focus Areas**: Hypothesis Testing Strategy, Experimental Design Suggestion, Validation Strategy Development, Testing Priority Assessment, Causal Inference Testing, Replication Planning
- **Example Tasks**:
  - Plan next tests to validate initial findings
  - Validate unexpected findings with appropriate experiments
  - Prioritize hypotheses for testing with limited resources

### **Analysis & Processing**
#### `methodology/task_specific/statistical_analysis_expert.md`
- **Name**: Statistical Analysis Expert
- **Summary**: Specializes in statistical methodology, test selection, and statistical inference with focus on rigor and appropriate test choice
- **Focus Areas**: statistical test selection, assumption testing, power analysis, statistical inference, multivariate analysis, robust statistics
- **Example Tasks**:
  - Choose appropriate statistical tests for research questions
  - Design comprehensive statistical analysis plans
  - Conduct power analysis and sample size planning

#### `methodology/tool_specific/text_preprocessing_expert.md`
- **Name**: Text Preprocessing Expert
- **Summary**: Specializes in text preprocessing, cleaning, and feature extraction for computational analysis
- **Focus Areas**: Text cleaning, feature extraction, preprocessing pipeline design, cross-condition consistency, text quality assessment, preprocessing validation
- **Example Tasks**:
  - Preprocessing messy social media text with emojis and URLs
  - Ensuring consistent preprocessing across experimental groups
  - Extracting linguistic features like POS tags and named entities

#### `methodology/tool_specific/bert_topic_modeling_expert.md`
- **Name**: BERT Topic Modeling Expert
- **Summary**: Specializes in BERT-based topic modeling, dynamic topic modeling, and advanced topic analysis techniques
- **Focus Areas**: BERT-based topic modeling, dynamic topic modeling, topic quality optimization, cross-condition topic analysis, topic evolution, topic coherence
- **Example Tasks**:
  - Implementing BERTopic models for social media analysis
  - Comparing topics across different experimental conditions
  - Optimizing topic quality and clustering parameters

#### `methodology/tool_specific/temporal_analysis_expert.md`
- **Name**: Temporal Analysis Expert
- **Summary**: Specializes in temporal data analysis, time-series modeling, and longitudinal pattern detection
- **Focus Areas**: Time series analysis, temporal pattern detection, change point detection, longitudinal data analysis, seasonal analysis, temporal relationships
- **Example Tasks**:
  - Analyzing temporal patterns in social media activity
  - Comparing temporal patterns across different groups
  - Identifying critical time points and change points

### **Result Interpretation & Communication**
#### `methodology/task_specific/result_interpretation_expert.md`
- **Name**: Result Interpretation Expert
- **Summary**: Specializes in interpreting research findings, assessing practical significance, and translating results into actionable insights for different audiences
- **Focus Areas**: result interpretation, practical significance, statistical vs clinical significance, effect size interpretation, limitation analysis, communication strategy
- **Example Tasks**:
  - Interpret statistical results and assess practical implications
  - Communicate findings effectively to different audiences
  - Analyze study limitations and alternative explanations

#### `methodology/tool_specific/visualization_interpretation_expert.md`
- **Name**: Visualization Interpretation Expert
- **Summary**: Specializes in data visualization design, chart interpretation, and visual communication for research
- **Focus Areas**: Data visualization design, chart type selection, visual pattern interpretation, publication-quality visualization, interactive visualization, visual communication
- **Example Tasks**:
  - Choosing appropriate visualizations for multi-group temporal data
  - Creating publication-ready visualizations with design principles
  - Interpreting complex visualizations like correlation heatmaps

### **Research Workflow & Iteration**
#### `workflow/iteration_coach.md`
- **Name**: Iteration Coach
- **Summary**: Guides iterative improvement cycles and research refinement through systematic enhancement approaches and progress measurement
- **Focus Areas**: Iterative Improvement Cycles, Research Refinement Strategies, Improvement Opportunity Identification, Iteration Planning, Progress Assessment, Iteration Breakout Strategies
- **Example Tasks**:
  - Plan next iteration based on current results
  - Break out of research iteration loops
  - Design systematic improvement cycles

#### `workflow/research_synthesizer.md`
- **Name**: Research Synthesizer
- **Summary**: Combines findings across analyses and research phases into coherent narratives and comprehensive conclusions
- **Focus Areas**: Research Finding Integration, Cross-Analysis Synthesis, Research Narrative Development, Pattern Identification, Gap Analysis, Comprehensive Conclusion Formation
- **Example Tasks**:
  - Synthesize multiple analyses into coherent story
  - Integrate findings from different research phases
  - Identify gaps in research synthesis

#### `workflow/result_reviewer.md`
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

1. **Identify the primary research stage**:
   - **Planning & Design**: `experimental_design_expert.md`, `social_science_research_expert.md`, `research_coordinator.md`, `research_pipeline_architect.md`
   - **Data Exploration**: `exploratory_analysis_expert.md`, `text_preprocessing_expert.md`, `data_quality_research_expert.md`
   - **Hypothesis Development**: `hypothesis_generation_expert.md`, `hypothesis_tester.md`
   - **Analysis**: `statistical_analysis_expert.md`, `bert_topic_modeling_expert.md`, `temporal_analysis_expert.md`
   - **Interpretation**: `result_interpretation_expert.md`, `visualization_interpretation_expert.md`
   - **Workflow & Iteration**: `iteration_coach.md`, `research_synthesizer.md`, `result_reviewer.md`

2. **Look for focus area overlap** between the task and the persona's expertise

3. **Check if the task resembles any of the example tasks** listed above

4. **Consider the research domain**:
   - **Social Science**: `social_science_research_expert.md`, `computational_linguistics_social_science_expert.md`
   - **Experimental**: `experimental_design_expert.md`
   - **Text Analysis**: `text_preprocessing_expert.md`, `bert_topic_modeling_expert.md`
   - **Temporal**: `temporal_analysis_expert.md`
   - **Workflow**: `research_coordinator.md`, `research_pipeline_architect.md`

5. **If the task requires multiple domains**, select multiple personas for collaboration

6. **If no persona matches**, return:
   > **No matching persona found. Consider defining a new one.**

---

## 🔁 Common Tasks and Suggested Agents

| Task Pattern | Suggested Persona(s) |
|--------------|----------------------|
| Starting a new research project | `workflow/research_coordinator.md` |
| Designing research methodology | `methodology/domain_specific/experimental_design_expert.md`, `workflow/research_coordinator.md` |
| Ensuring data quality | `workflow/data_quality_research_expert.md` |
| Planning experiments and tests | `workflow/hypothesis_tester.md`, `workflow/research_coordinator.md` |
| Iterating on research approach | `workflow/iteration_coach.md`, `workflow/result_reviewer.md` |
| Coordinating research phases | `workflow/research_coordinator.md`, `workflow/research_pipeline_architect.md` |
| Synthesizing multiple findings | `workflow/research_synthesizer.md` |
| Reviewing research quality | `workflow/result_reviewer.md`, `workflow/data_quality_research_expert.md` |
| Optimizing research pipeline | `workflow/research_pipeline_architect.md`, `workflow/iteration_coach.md` |
| Preparing for peer review | `workflow/result_reviewer.md`, `workflow/research_synthesizer.md` |
| Scaling research infrastructure | `workflow/research_pipeline_architect.md`, `workflow/data_quality_research_expert.md` |
| Validating research findings | `workflow/hypothesis_tester.md`, `workflow/result_reviewer.md` |
| "I need to design an experiment" | `methodology/domain_specific/experimental_design_expert.md` |
| "I have new data and need to understand what's in it" | `methodology/task_specific/exploratory_analysis_expert.md` |
| "I found patterns but need to develop testable hypotheses" | `methodology/task_specific/hypothesis_generation_expert.md` |
| "What statistical test should I use for my data?" | `methodology/task_specific/statistical_analysis_expert.md` |
| "What do my results actually mean?" | `methodology/task_specific/result_interpretation_expert.md` |
| "I need to analyze text data" | `methodology/tool_specific/text_preprocessing_expert.md` + `methodology/tool_specific/bert_topic_modeling_expert.md` |
| "I need to analyze time series data" | `methodology/tool_specific/temporal_analysis_expert.md` |
| "I need to create visualizations" | `methodology/tool_specific/visualization_interpretation_expert.md` |
| "I need to plan my research approach" | `methodology/task_specific/exploratory_analysis_expert.md` + `methodology/task_specific/hypothesis_generation_expert.md` |
| "I have results but need to communicate them" | `methodology/task_specific/result_interpretation_expert.md` |
| "My hypothesis wasn't supported - how should I interpret this?" | `methodology/task_specific/result_interpretation_expert.md` + `methodology/task_specific/statistical_analysis_expert.md` |
| "I need to build a theoretical framework" | `methodology/task_specific/hypothesis_generation_expert.md` |
| "How should I check my data quality?" | `methodology/task_specific/exploratory_analysis_expert.md` |
| "What's the practical significance of my findings?" | `methodology/task_specific/result_interpretation_expert.md` |
| "I need to design a social science study" | `methodology/domain_specific/social_science_research_expert.md` |
| "I need to analyze linguistic patterns" | `methodology/domain_specific/computational_linguistics_social_science_expert.md` |
| "Cross-condition text analysis" | `methodology/tool_specific/text_preprocessing_expert.md` + `methodology/tool_specific/bert_topic_modeling_expert.md` |
| "Temporal text analysis" | `methodology/tool_specific/temporal_analysis_expert.md` + `methodology/tool_specific/bert_topic_modeling_expert.md` |
| "Visualization of temporal data" | `methodology/tool_specific/temporal_analysis_expert.md` + `methodology/tool_specific/visualization_interpretation_expert.md` |

---

## 🎯 Research Stage-Based Routing

### **Planning Stage**
- **Research Coordinator** - Overall strategy and resource planning
- **Research Pipeline Architect** - Pipeline and infrastructure design
- **Experimental Design Expert** - Methodology and experimental design
- **Social Science Research Expert** - Domain-specific research design
- **Data Quality Research Expert** - Quality framework planning

### **Data Exploration Stage**
- **Exploratory Analysis Expert** - Systematic data investigation
- **Text Preprocessing Expert** - Text data preparation
- **Data Quality Research Expert** - Quality assessment and monitoring

### **Hypothesis Development Stage**
- **Hypothesis Generation Expert** - Theory and hypothesis development
- **Hypothesis Tester** - Testing strategy and validation planning

### **Analysis Stage**
- **Statistical Analysis Expert** - Statistical methodology and testing
- **BERT Topic Modeling Expert** - Text analysis and topic modeling
- **Temporal Analysis Expert** - Time series and longitudinal analysis
- **Hypothesis Tester** - Next testing and validation planning

### **Interpretation Stage**
- **Result Interpretation Expert** - Finding interpretation and communication
- **Visualization Interpretation Expert** - Visual communication and chart design
- **Result Reviewer** - Quality assessment and improvement

### **Synthesis & Review Stage**
- **Research Synthesizer** - Finding integration and narrative development
- **Research Coordinator** - Cross-phase integration coordination
- **Result Reviewer** - Final quality review and peer review preparation

### **Workflow & Iteration Stage**
- **Iteration Coach** - Improvement cycles and refinement
- **Research Pipeline Architect** - Pipeline optimization and scaling
- **Research Coordinator** - Overall project success evaluation

---

## 🛠️ Update Instructions

After adding new personas to this folder, rerun `create_router.md` to regenerate this file.

---

## Notes

- These personas focus on **research expertise** rather than technical implementation
- They collaborate with engineering personas when technical infrastructure is needed
- Each persona specializes in a specific research stage while maintaining awareness of the broader research process
- Consider using multiple personas for complex research planning that spans multiple stages
- All personas emphasize reproducibility, validation, and methodological rigor
- The personas are designed to collaborate effectively on multidisciplinary research tasks
- Focus areas are complementary, allowing for comprehensive coverage of research needs
- Workflow personas focus on process and coordination, while methodology personas focus on specific research techniques
- The combined router provides a complete view of the research lifecycle from planning through final synthesis
