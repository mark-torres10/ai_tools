# 🧭 Agent Persona Router

This folder contains specialized AI agents designed to assist with various research methodology tasks across experimental design, statistical analysis, text analysis, temporal analysis, and result interpretation. These personas focus on methodological expertise while recognizing when engineering expertise is needed for implementation.

Use this file to decide which agent persona is best suited for a task or review. If no persona is a good fit, consider creating a new one using `create_persona.md`.

---

## 🧠 Persona Directory

### **Experimental Design & Social Science**
#### `domain_specific/experimental_design_expert.md`
- **Name**: Experimental Design Expert
- **Summary**: Specializes in experimental design, causal inference, and research methodology across diverse research domains
- **Focus Areas**: Experimental Design, Causal Inference, Research Methodology, Control Strategies, Quasi-Experimental Designs, Field Experiments
- **Example Tasks**:
  - Design A/B tests for social media interventions with proper contamination controls
  - Establish causality from observational data using natural experiments or quasi-experimental approaches
  - Design longitudinal intervention studies with stepped-wedge or cluster randomized designs

#### `domain_specific/social_science_research_expert.md`
- **Name**: Social Science Research Expert
- **Summary**: Specializes in social science research methodology, experimental design, and social phenomena analysis
- **Focus Areas**: Social Science Research Methodology, Experimental Design, Survey Research, Social Behavior Analysis, Longitudinal Research, Social Network Analysis
- **Example Tasks**:
  - Design studies on social media influence on political attitudes addressing selection bias
  - Analyze survey data across demographic groups while controlling for confounders
  - Study behavioral changes over time using longitudinal panel designs

#### `domain_specific/computational_linguistics_social_science_expert.md`
- **Name**: Computational Linguistics & Social Science Expert
- **Summary**: Specializes in computational linguistics research, computational social science, and applied text analysis methodologies
- **Focus Areas**: Computational Linguistics Research, Computational Social Science, Applied Text Analysis, NLP, Sociolinguistic Pattern Recognition, Discourse Analysis
- **Example Tasks**:
  - Analyze sentiment changes in political discourse over time using lexicon-based or transformer approaches
  - Study linguistic accommodation patterns in online conversations tracking lexical diversity and syntactic complexity
  - Analyze code-switching patterns in multilingual social media using language identification pipelines

### **Core Research Methodology**
#### `task_specific/exploratory_analysis_expert.md`
- **Name**: Exploratory Analysis Expert
- **Summary**: Specializes in systematic data exploration, pattern discovery, and preliminary hypothesis generation through comprehensive data investigation
- **Focus Areas**: EDA, pattern discovery, data quality assessment, hypothesis generation, visualization strategy, feature exploration
- **Example Tasks**:
  - Design systematic data exploration strategies for new datasets
  - Identify hidden patterns and relationships in complex data
  - Assess data quality issues before formal analysis

#### `task_specific/hypothesis_generation_expert.md`
- **Name**: Hypothesis Generation Expert
- **Summary**: Specializes in developing testable research hypotheses, theoretical frameworks, and focused research questions with clear operational definitions
- **Focus Areas**: hypothesis development, theoretical frameworks, research questions, causal mechanisms, operational definitions, falsifiability
- **Example Tasks**:
  - Transform exploratory findings into testable predictions
  - Build comprehensive theoretical models for research areas
  - Refine broad research questions into specific, testable hypotheses

#### `task_specific/statistical_analysis_expert.md`
- **Name**: Statistical Analysis Expert
- **Summary**: Specializes in statistical methodology, test selection, and statistical inference with focus on rigor and appropriate test choice
- **Focus Areas**: statistical test selection, assumption testing, power analysis, statistical inference, multivariate analysis, robust statistics
- **Example Tasks**:
  - Choose appropriate statistical tests for research questions
  - Design comprehensive statistical analysis plans
  - Conduct power analysis and sample size planning

#### `task_specific/result_interpretation_expert.md`
- **Name**: Result Interpretation Expert
- **Summary**: Specializes in interpreting research findings, assessing practical significance, and translating results into actionable insights for different audiences
- **Focus Areas**: result interpretation, practical significance, statistical vs clinical significance, effect size interpretation, limitation analysis, communication strategy
- **Example Tasks**:
  - Interpret statistical results and assess practical implications
  - Communicate findings effectively to different audiences
  - Analyze study limitations and alternative explanations

### **Specialized Analysis Tools**
#### `tool_specific/bert_topic_modeling_expert.md`
- **Name**: BERT Topic Modeling Expert
- **Summary**: Specializes in BERT-based topic modeling, dynamic topic modeling, and advanced topic analysis techniques
- **Focus Areas**: BERT-based topic modeling, dynamic topic modeling, topic quality optimization, cross-condition topic analysis, topic evolution, topic coherence
- **Example Tasks**:
  - Implementing BERTopic models for social media analysis
  - Comparing topics across different experimental conditions
  - Optimizing topic quality and clustering parameters

#### `tool_specific/temporal_analysis_expert.md`
- **Name**: Temporal Analysis Expert
- **Summary**: Specializes in temporal data analysis, time-series modeling, and longitudinal pattern detection
- **Focus Areas**: Time series analysis, temporal pattern detection, change point detection, longitudinal data analysis, seasonal analysis, temporal relationships
- **Example Tasks**:
  - Analyzing temporal patterns in social media activity
  - Comparing temporal patterns across different groups
  - Identifying critical time points and change points

#### `tool_specific/text_preprocessing_expert.md`
- **Name**: Text Preprocessing Expert
- **Summary**: Specializes in text preprocessing, cleaning, and feature extraction for computational analysis
- **Focus Areas**: Text cleaning, feature extraction, preprocessing pipeline design, cross-condition consistency, text quality assessment, preprocessing validation
- **Example Tasks**:
  - Preprocessing messy social media text with emojis and URLs
  - Ensuring consistent preprocessing across experimental groups
  - Extracting linguistic features like POS tags and named entities

#### `tool_specific/visualization_interpretation_expert.md`
- **Name**: Visualization Interpretation Expert
- **Summary**: Specializes in data visualization design, chart interpretation, and visual communication for research
- **Focus Areas**: Data visualization design, chart type selection, visual pattern interpretation, publication-quality visualization, interactive visualization, visual communication
- **Example Tasks**:
  - Choosing appropriate visualizations for multi-group temporal data
  - Creating publication-ready visualizations with design principles
  - Interpreting complex visualizations like correlation heatmaps

---

## 📌 Routing Guidelines

To determine which persona to use:

1. **Identify the primary research stage**:
   - **Planning & Design**: `experimental_design_expert.md`, `social_science_research_expert.md`
   - **Data Exploration**: `exploratory_analysis_expert.md`, `text_preprocessing_expert.md`
   - **Analysis**: `statistical_analysis_expert.md`, `bert_topic_modeling_expert.md`, `temporal_analysis_expert.md`
   - **Interpretation**: `result_interpretation_expert.md`, `visualization_interpretation_expert.md`

2. **Look for focus area overlap** between the task and the persona's expertise

3. **Check if the task resembles any of the example tasks** listed above

4. **Consider the research domain**:
   - **Social Science**: `social_science_research_expert.md`, `computational_linguistics_social_science_expert.md`
   - **Experimental**: `experimental_design_expert.md`
   - **Text Analysis**: `text_preprocessing_expert.md`, `bert_topic_modeling_expert.md`
   - **Temporal**: `temporal_analysis_expert.md`

5. **If the task requires multiple domains**, select multiple personas for collaboration

6. **If no persona matches**, return:
   > **No matching persona found. Consider defining a new one.**

---

## 🔁 Common Tasks and Suggested Agents

| Task Pattern | Suggested Persona(s) |
|--------------|----------------------|
| "I need to design an experiment" | `experimental_design_expert.md` |
| "I have new data and need to understand what's in it" | `exploratory_analysis_expert.md` |
| "I found patterns but need to develop testable hypotheses" | `hypothesis_generation_expert.md` |
| "What statistical test should I use for my data?" | `statistical_analysis_expert.md` |
| "What do my results actually mean?" | `result_interpretation_expert.md` |
| "I need to analyze text data" | `text_preprocessing_expert.md` + `bert_topic_modeling_expert.md` |
| "I need to analyze time series data" | `temporal_analysis_expert.md` |
| "I need to create visualizations" | `visualization_interpretation_expert.md` |
| "I need to plan my research approach" | `exploratory_analysis_expert.md` + `hypothesis_generation_expert.md` |
| "I have results but need to communicate them" | `result_interpretation_expert.md` |
| "My hypothesis wasn't supported - how should I interpret this?" | `result_interpretation_expert.md` + `statistical_analysis_expert.md` |
| "I need to build a theoretical framework" | `hypothesis_generation_expert.md` |
| "How should I check my data quality?" | `exploratory_analysis_expert.md` |
| "What's the practical significance of my findings?" | `result_interpretation_expert.md` |
| "I need to design a social science study" | `social_science_research_expert.md` |
| "I need to analyze linguistic patterns" | `computational_linguistics_social_science_expert.md` |
| "Cross-condition text analysis" | `text_preprocessing_expert.md` + `bert_topic_modeling_expert.md` |
| "Temporal text analysis" | `temporal_analysis_expert.md` + `bert_topic_modeling_expert.md` |
| "Visualization of temporal data" | `temporal_analysis_expert.md` + `visualization_interpretation_expert.md` |

---

## 🛠️ Update Instructions

After adding new personas to this folder, rerun `create_router.md` to regenerate this file.

---

## Notes

- These personas focus on **research methodology and design** rather than technical implementation
- They collaborate with engineering personas when technical infrastructure is needed
- Each persona specializes in a specific research stage while maintaining awareness of the broader research process
- Consider using multiple personas for complex research planning that spans multiple stages
- All personas emphasize reproducibility, validation, and methodological rigor
- The personas are designed to collaborate effectively on multidisciplinary research tasks
- Focus areas are complementary, allowing for comprehensive coverage of research methodology needs
