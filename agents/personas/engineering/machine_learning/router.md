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

2. **Multiple Personas** - If the task requires multiple specialized skills (e.g., both classification modeling AND deployment considerations), consider using multiple personas for comprehensive coverage.

3. **No Match** - If no persona matches, return:
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

---

## 🛠️ Update Instructions

After adding new personas to this folder, update this router to include them with appropriate routing guidelines.

---

## Notes

- The Classification Modeling Expert is designed for senior-level machine learning expertise
- Focuses on the research and development side of ML, not deployment (which is covered by other engineering personas)
- Emphasizes business-relevant metrics and stakeholder communication
- Prioritizes systematic approaches and best practices for model development
