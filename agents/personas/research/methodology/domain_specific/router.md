# 🧭 Agent Persona Router

This folder contains specialized AI agents designed to assist with various research methodology tasks across experimental design, social science research, and computational linguistics. These personas focus on domain-specific research approaches and methodologies.

Use this file to decide which agent persona is best suited for a task or review. If no persona is a good fit, consider creating a new one using `create_persona.md`.

---

## 🧠 Persona Directory

### `experimental_design_expert.md`
- **Name**: Experimental Design Expert
- **Summary**: Specializes in experimental design, causal inference, and research methodology across diverse research domains
- **Focus Areas**: Experimental Design, Causal Inference, Research Methodology, Control Strategies, Quasi-Experimental Designs, Field Experiments
- **Example Tasks**:
  - Design A/B tests for social media interventions with proper contamination controls
  - Establish causality from observational data using natural experiments or quasi-experimental approaches
  - Design longitudinal intervention studies with stepped-wedge or cluster randomized designs

### `social_science_research_expert.md`
- **Name**: Social Science Research Expert
- **Summary**: Specializes in social science research methodology, experimental design, and social phenomena analysis
- **Focus Areas**: Social Science Research Methodology, Experimental Design, Survey Research, Social Behavior Analysis, Longitudinal Research, Social Network Analysis
- **Example Tasks**:
  - Design studies on social media influence on political attitudes addressing selection bias
  - Analyze survey data across demographic groups while controlling for confounders
  - Study behavioral changes over time using longitudinal panel designs

### `computational_linguistics_social_science_expert.md`
- **Name**: Computational Linguistics & Social Science Expert
- **Summary**: Specializes in computational linguistics research, computational social science, and applied text analysis methodologies
- **Focus Areas**: Computational Linguistics Research, Computational Social Science, Applied Text Analysis, NLP, Sociolinguistic Pattern Recognition, Discourse Analysis
- **Example Tasks**:
  - Analyze sentiment changes in political discourse over time using lexicon-based or transformer approaches
  - Study linguistic accommodation patterns in online conversations tracking lexical diversity and syntactic complexity
  - Analyze code-switching patterns in multilingual social media using language identification pipelines

---

## 📌 Routing Guidelines

To determine which persona to use:

1. **Look for focus area overlap** between the task and the persona's expertise
2. **Check if the task resembles any of the example tasks** listed for each persona
3. **Consider the primary research domain**:
   - **Experimental Design Expert**: For causal inference, A/B testing, intervention studies, and methodological rigor
   - **Social Science Research Expert**: For social behavior studies, survey research, group comparisons, and social phenomena
   - **Computational Linguistics Expert**: For text analysis, language patterns, computational social science, and NLP applications
4. **If the task requires multiple domains**, select multiple personas or the most relevant primary persona
5. **If no persona matches**, return:
   > **No matching persona found. Consider defining a new one.**

---

## 🔁 Common Tasks and Suggested Agents

| Task Pattern | Suggested Persona(s) |
|--------------|----------------------|
| A/B testing, intervention studies, causal inference | `experimental_design_expert.md` |
| Survey research, social behavior analysis, group comparisons | `social_science_research_expert.md` |
| Text analysis, sentiment analysis, linguistic patterns | `computational_linguistics_social_science_expert.md` |
| Social media research with experimental design | `experimental_design_expert.md` + `social_science_research_expert.md` |
| Longitudinal studies with computational analysis | `social_science_research_expert.md` + `computational_linguistics_social_science_expert.md` |
| Experimental design for language-based studies | `experimental_design_expert.md` + `computational_linguistics_social_science_expert.md` |
| Survey design with computational analysis | `social_science_research_expert.md` + `computational_linguistics_social_science_expert.md` |

---

## 🛠️ Update Instructions

After adding new personas to this folder, rerun `create_router.md` to regenerate this file.

---

## Notes

- All personas follow the expected schema and focus on research methodology and design
- Each persona recognizes when engineering expertise is needed for implementation
- The personas are designed to collaborate effectively on multidisciplinary research tasks
- Focus areas are complementary, allowing for comprehensive coverage of research methodology needs
