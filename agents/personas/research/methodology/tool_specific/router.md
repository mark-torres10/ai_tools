# 🧭 Agent Persona Router

This folder contains specialized AI agents designed to assist with various research methodology tasks across text analysis, temporal analysis, visualization, and topic modeling. These personas focus on methodological expertise while recognizing when engineering expertise is needed for implementation.

Use this file to decide which agent persona is best suited for a task or review. If no persona is a good fit, consider creating a new one using `create_persona.md`.

---

## 🧠 Persona Directory

### `bert_topic_modeling_expert.md`
- **Name**: BERT Topic Modeling Expert
- **Summary**: Specializes in BERT-based topic modeling, dynamic topic modeling, and advanced topic analysis techniques
- **Focus Areas**: BERT-based topic modeling, dynamic topic modeling, topic quality optimization, cross-condition topic analysis, topic evolution, topic coherence
- **Example Tasks**:
  - Implementing BERTopic models for social media analysis
  - Comparing topics across different experimental conditions
  - Optimizing topic quality and clustering parameters

### `temporal_analysis_expert.md`
- **Name**: Temporal Analysis Expert
- **Summary**: Specializes in temporal data analysis, time-series modeling, and longitudinal pattern detection
- **Focus Areas**: Time series analysis, temporal pattern detection, change point detection, longitudinal data analysis, seasonal analysis, temporal relationships
- **Example Tasks**:
  - Analyzing temporal patterns in social media activity
  - Comparing temporal patterns across different groups
  - Identifying critical time points and change points

### `text_preprocessing_expert.md`
- **Name**: Text Preprocessing Expert
- **Summary**: Specializes in text preprocessing, cleaning, and feature extraction for computational analysis
- **Focus Areas**: Text cleaning, feature extraction, preprocessing pipeline design, cross-condition consistency, text quality assessment, preprocessing validation
- **Example Tasks**:
  - Preprocessing messy social media text with emojis and URLs
  - Ensuring consistent preprocessing across experimental groups
  - Extracting linguistic features like POS tags and named entities

### `visualization_interpretation_expert.md`
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

1. Look for **focus area overlap** between the task and the persona.
2. Check if the task resembles any of the **example tasks** listed.
3. If the task requires more than one domain, select multiple personas.
4. If no persona matches, return:
   > **No matching persona found. Consider defining a new one.**

---

## 🔁 Common Tasks and Suggested Agents

| Task Pattern | Suggested Persona(s) |
|--------------|----------------------|
| Text preprocessing and cleaning | `text_preprocessing_expert.md` |
| Topic modeling with BERT | `bert_topic_modeling_expert.md` |
| Time series analysis and patterns | `temporal_analysis_expert.md` |
| Data visualization design | `visualization_interpretation_expert.md` |
| Cross-condition text analysis | `text_preprocessing_expert.md` + `bert_topic_modeling_expert.md` |
| Temporal text analysis | `temporal_analysis_expert.md` + `bert_topic_modeling_expert.md` |
| Visualization of temporal data | `temporal_analysis_expert.md` + `visualization_interpretation_expert.md` |
| Text preprocessing for visualization | `text_preprocessing_expert.md` + `visualization_interpretation_expert.md` |

---

## 🛠️ Update Instructions

After adding new personas to this folder, rerun `create_router.md` to regenerate this file.

---

## Notes

- These personas focus on **methodological expertise** and **research design** rather than technical implementation
- They collaborate with engineering personas when computational infrastructure is needed
- All personas emphasize reproducibility, validation, and methodological rigor
- Consider combining multiple personas for complex tasks that span multiple domains
