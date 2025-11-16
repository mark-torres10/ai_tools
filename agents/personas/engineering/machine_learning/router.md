# 🧭 Machine Learning Agent Persona Router

This folder contains specialized AI agents designed to assist with machine learning tasks, focusing on model development, evaluation, and optimization.

Use this file to decide which agent persona is best suited for a machine learning task or review. If no persona is a good fit, consider creating a new one using the persona creation templates.

---

## 🧠 Persona Directory

### `domain_specific/classification_modeling_expert.md`
- **Name**: Classification Modeling Expert
- **Summary**: Specializes in developing, evaluating, and optimizing classification models with expertise in algorithm selection, feature engineering, and model interpretation for business applications.
- **Focus Areas**: algorithm selection, model evaluation, feature engineering, imbalanced data handling, model interpretability, validation strategy
- **Example Tasks**:
  - Building customer churn prediction models with proper handling of class imbalance
  - Implementing SHAP and LIME for model interpretability and stakeholder communication
  - Designing comprehensive validation strategies including temporal splits and drift detection
  - Optimizing feature engineering pipelines for improved model performance

### `domain_specific/mechanistic_interpretability_expert.md`
- **Name**: Mechanistic Interpretability Expert
- **Summary**: Reverse-engineers transformer LMs via causal interventions to identify minimal, faithful circuits and interpretable features in the residual stream.
- **Focus Areas**: activation/OV patching, path patching, causal scrubbing, attribution patching, SAEs/dictionary learning, effect-size reporting, minimality/completeness checks
- **Example Tasks**:
  - Running activation/OV patching to validate induction or IOI circuit hypotheses
  - Discovering and validating SAE features with selectivity/causality/robustness checks
  - Building minimal faithful circuits with quantitative necessity/sufficiency tests
  - Designing reproducible MI experiment harnesses (seeds, prompts, metrics)

### `domain_specific/transformer_architecture_expert.md`
- **Name**: Transformer Architecture Expert
- **Summary**: Explains behaviors via architectural decomposition (QK selection vs. OV/MLP content, residual composition, layernorm scaling) and validates with targeted interventions.
- **Focus Areas**: residual stream reasoning, attention decomposition (QK/OV), MLP key–value memories, logit lens/attribution diagnostics, SoLU tradeoffs, causal localization
- **Example Tasks**:
  - Localizing decisive layers/heads/MLPs and quantifying their causal impact
  - Decomposing QK vs. OV contributions and normalizing comparisons across runs
  - Documenting architecture-grounded mechanisms and side-effect surfaces

### `domain_specific/circuit_discovery_expert.md`
- **Name**: Circuit Discovery Expert
- **Summary**: Discovers, validates, and documents computational circuits; prunes to minimal sets that causally explain behaviors with effect sizes and controls.
- **Focus Areas**: circuit assembly, path patching, causal scrubbing, minimality/completeness, robustness/OOD evaluation, CLT-based circuit tracing, safe edits (ROME/MEMIT)
- **Example Tasks**:
  - Triage → intervene → assemble candidate circuit; prune to minimal faithful set
  - Run causal scrubbing to test behavior-preserving resampling implied by the hypothesis
  - Produce attribution graphs (CLTs) and validate edges with targeted interventions
  - Apply targeted edits (ROME/MEMIT) with specificity/generalization/regression batteries

---

## 📌 Routing Guidelines

To determine which persona to use:

1. **Classification Modeling Expert** - Choose when the task involves:
   - Building and optimizing classification models for business applications
   - Handling imbalanced data with techniques like SMOTE and class weighting
   - Implementing model interpretability with SHAP and LIME
   - Designing validation strategies including temporal splits and drift detection
   - Feature engineering and selection for improved model performance
   - Algorithm selection from simple to complex (logistic regression → XGBoost → Neural Networks)

2. **Mechanistic Interpretability Expert** - Choose when the task involves:
   - Causal, circuit-level explanations of transformer behaviors
   - Activation/OV/path patching, causal scrubbing, attribution patching
   - SAE feature discovery and faithfulness validation (selectivity, causality, robustness)
   - Minimality/completeness testing and effect-size reporting

3. **Transformer Architecture Expert** - Choose when the task involves:
   - Decomposing behaviors via QK (selection) vs. OV/MLP (content) and residual composition
   - Localizing decisive layers/heads/MLPs and normalizing comparisons across runs
   - Explaining MLP key–value memories and architecture tradeoffs (e.g., SoLU)

4. **Circuit Discovery Expert** - Choose when the task involves:
   - End-to-end circuit discovery, pruning to minimal faithful sets
   - Causal scrubbing, path patching, and attribution graphs (CLTs)
   - Targeted editing (ROME/MEMIT) with post-edit regression/safety batteries

5. **Multiple Personas** - If the task requires multiple specialized skills (e.g., architecture analysis plus circuit pruning), consider using multiple personas for comprehensive coverage.

6. **No Match** - If no persona matches, return:
   > **No matching persona found. Consider defining a new one.**

---

## 🔁 Common Tasks and Suggested Agents

| Task Pattern | Suggested Persona(s) |
|--------------|----------------------|
| Binary/multi-class classification model development | `domain_specific/classification_modeling_expert.md` |
| Handling imbalanced datasets | `domain_specific/classification_modeling_expert.md` |
| Model interpretability implementation | `domain_specific/classification_modeling_expert.md` |
| Feature engineering and selection | `domain_specific/classification_modeling_expert.md` |
| Validation strategy design | `domain_specific/classification_modeling_expert.md` |
| Model performance optimization | `domain_specific/classification_modeling_expert.md` |
| Business metric optimization | `domain_specific/classification_modeling_expert.md` |
| Production model monitoring setup | `domain_specific/classification_modeling_expert.md` |
| Mechanistic interpretability of transformer behaviors | `domain_specific/mechanistic_interpretability_expert.md` |
| Attention QK/OV and MLP KV memory analysis | `domain_specific/transformer_architecture_expert.md` |
| Circuit discovery and minimal faithful circuits | `domain_specific/circuit_discovery_expert.md` |
| Activation/OV/path patching and causal scrubbing | `domain_specific/mechanistic_interpretability_expert.md`, `domain_specific/circuit_discovery_expert.md` |
| SAE feature discovery and validation (selectivity/causality/robustness) | `domain_specific/mechanistic_interpretability_expert.md` |
| Attribution graphs (CLTs) and targeted edits (ROME/MEMIT) | `domain_specific/circuit_discovery_expert.md`, `domain_specific/transformer_architecture_expert.md` |

---

## 🛠️ Update Instructions

After adding new personas to this folder, update this router to include them with appropriate routing guidelines.

---

## Notes

- The Classification Modeling Expert is designed for senior-level machine learning expertise
- Focuses on the research and development side of ML, not deployment (which is covered by other engineering personas)
- Emphasizes business-relevant metrics and stakeholder communication
- Prioritizes systematic approaches and best practices for model development
