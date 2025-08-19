# 🧭 Agent Persona Router

This folder contains specialized AI agents designed to assist with domain-specific data engineering tasks, focusing on real-time analytics and social media data processing.

Use this file to decide which agent persona is best suited for a task or review. If no persona is a good fit, consider creating a new one using `create_persona.md`.

---

## 🧠 Persona Directory

### `real_time_analytics_expert.md`
- **Name**: Real-time Analytics Expert
- **Summary**: Specializes in designing and optimizing real-time analytics systems, streaming data pipelines, and interactive dashboards that provide immediate insights from live data streams.
- **Focus Areas**: streaming data processing, real-time analytics dashboards, time-series data management, real-time data quality, low-latency data pipelines
- **Example Tasks**:
  - Building real-time dashboards with sub-second latency for user engagement metrics
  - Diagnosing and fixing performance issues in real-time inventory tracking systems
  - Migrating from batch to real-time processing for customer behavior analytics

### `social_media_data_expert.md`
- **Name**: Social Media Data Expert
- **Summary**: Specializes in integrating, processing, and analyzing social media data from multiple platforms, handling API rate limits, data normalization, and platform-specific optimizations.
- **Focus Areas**: multi-platform API integration, social media data patterns, data normalization, rate limiting, social media analytics
- **Example Tasks**:
  - Integrating data from Twitter, Instagram, LinkedIn, and TikTok for unified analytics
  - Resolving data inconsistencies and API errors in social media management tools
  - Building real-time sentiment analysis and trend detection for millions of social media posts

---

## 📌 Routing Guidelines

To determine which persona to use:

1. **Real-time Analytics Expert** - Choose when the task involves:
   - Streaming data processing or real-time data pipelines
   - Building interactive dashboards with live data updates
   - Optimizing for sub-second latency in data processing
   - Time-series data management and analytics
   - Performance optimization of real-time systems

2. **Social Media Data Expert** - Choose when the task involves:
   - Integrating multiple social media platform APIs
   - Handling API rate limits and quota management
   - Normalizing data across different social media platforms
   - Social media sentiment analysis and trend detection
   - Ensuring data quality and compliance for social media data

3. **Machine Learning Classification Expert** - Choose when the task involves:
   - Building and optimizing classification models for business applications
   - Handling imbalanced data with techniques like SMOTE and class weighting
   - Implementing model interpretability with SHAP and LIME
   - Designing validation strategies including temporal splits and drift detection
   - Feature engineering and selection for improved model performance

4. **Multiple Personas** - If the task requires multiple specialized skills (e.g., real-time processing AND social media data integration, or real-time analytics AND machine learning), consider using multiple personas for comprehensive coverage.

4. **No Match** - If no persona matches, return:
   > **No matching persona found. Consider defining a new one.**

---

## 🔁 Common Tasks and Suggested Agents

| Task Pattern | Suggested Persona(s) |
|--------------|----------------------|
| Real-time dashboard development | `real_time_analytics_expert.md` |
| Streaming data pipeline design | `real_time_analytics_expert.md` |
| Social media API integration | `social_media_data_expert.md` |
| Multi-platform data normalization | `social_media_data_expert.md` |
| Performance optimization for real-time systems | `real_time_analytics_expert.md` |
| Social media sentiment analysis | `social_media_data_expert.md` |
| Time-series data management | `real_time_analytics_expert.md` |
| API rate limiting and error handling | `social_media_data_expert.md` |
| Real-time data quality monitoring | `real_time_analytics_expert.md` |
| Social media compliance and GDPR | `social_media_data_expert.md` |

---

## 🛠️ Update Instructions

After adding new personas to this folder, rerun `create_router.md` to regenerate this file.

---

## Notes

- Both personas are designed for senior-level data engineering expertise
- Real-time Analytics Expert focuses on technical architecture and performance
- Social Media Data Expert emphasizes API integration and data quality
- Consider combining both personas for complex projects involving real-time social media analytics 