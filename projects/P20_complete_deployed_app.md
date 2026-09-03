# P20 — Complete Deployed ML/AI Application

> **🚀 Project · Expert · Capstone-Level · M14–M16**
> *The ultimate course project: a fully tested, secured, deployed, and documented ML/AI application.*
> Difficulty: ★★★★★ · Duration: 4 weeks · Weight: Part of 15% project grade (or replaces P08 Capstone)

---

## Problem Statement

Build a complete, production-quality Streamlit application that solves a real-world problem using Machine Learning or AI. The application must demonstrate mastery of every course topic: from data loading to deployment, from UI design to security, from testing to monitoring.

This is the **capstone-level project** — it should represent the best work you can produce.

---

## Learning Outcomes

By completing this project you will demonstrate ALL course learning outcomes:

1. CLO1: Explain Streamlit's execution model
2. CLO2: Build interactive data applications
3. CLO3: Implement data visualization
4. CLO4: Manage application state
5. CLO5: Optimize performance
6. CLO6: Design well-structured applications
7. CLO7: Connect to data sources
8. CLO8: Deploy ML models
9. CLO9: Build AI-powered applications
10. CLO10: Apply testing and security
11. CLO11: Deploy to production
12. CLO12: Execute full development lifecycle

---

## Prerequisites

- Completed all 16 modules
- All assignments submitted
- Community Cloud account
- GitHub repository

---

## Project Categories

Choose ONE of these categories:

| Category | Example Projects | Key Technologies |
|----------|-----------------|------------------|
| **Analytics Dashboard** | Sales analytics, healthcare monitoring, financial tracking | Pandas, Plotly, SQLite, caching |
| **ML Deployment** | Churn prediction, fraud detection, recommendation system | Scikit-learn, joblib, preprocessing |
| **NLP/Text Analysis** | Sentiment analyzer, topic classifier, text summarizer | TF-IDF, classifiers, text processing |
| **AI Assistant** | Data science chatbot, document Q&A, code helper | LLM API, RAG, conversation state |
| **Full-Stack DS App** | End-to-end data pipeline with ML + AI insights | All technologies combined |

---

## Required Components (200 marks total)

### 1. Application Architecture (25 marks)

| Requirement | Marks |
|-------------|-------|
| Clean file structure with separation of concerns | 8 |
| `config.py` with centralized settings | 4 |
| Multipage navigation with `st.navigation()` | 5 |
| Reusable components in `components.py` | 4 |
| Data functions separated from UI (no `st.*` in data logic) | 4 |

### 2. Data Layer (20 marks)

| Requirement | Marks |
|-------------|-------|
| Data loading with `@st.cache_data` or `@st.cache_resource` | 5 |
| Database integration (SQLite) with CRUD operations | 8 |
| Parameterized SQL queries | 4 |
| Cache invalidation after writes | 3 |

### 3. Interactive Features (25 marks)

| Requirement | Marks |
|-------------|-------|
| Sidebar filters with session state persistence | 6 |
| KPI metrics with formatting and deltas | 5 |
| 4+ chart types using Plotly or Matplotlib | 8 |
| Charts update dynamically with filter changes | 4 |
| Data tables with sorting and formatting | 2 |

### 4. ML/AI Component (30 marks)

| Requirement | Marks |
|-------------|-------|
| Model training or loading with proper caching | 6 |
| Preprocessing consistency (same at train and inference) | 6 |
| Single prediction interface with input validation | 6 |
| Batch prediction from file upload | 6 |
| Model explanation (feature importance, probabilities) | 6 |

### 5. Testing & Security (25 marks)

| Requirement | Marks |
|-------------|-------|
| Unit tests (≥3) for data/logic functions | 6 |
| AppTest (≥2) for Streamlit app testing | 6 |
| All tests pass: `pytest tests/ -v` | 3 |
| No hardcoded secrets | 4 |
| Input validation on all user inputs | 3 |
| `.gitignore` properly configured | 3 |

### 6. Deployment (25 marks)

| Requirement | Marks |
|-------------|-------|
| Deployed on Community Cloud | 8 |
| `requirements.txt` correct and minimal | 4 |
| App loads within 15 seconds | 4 |
| All features work in deployed version | 5 |
| Deployment URL provided and accessible | 4 |

### 7. Documentation (25 marks)

| Requirement | Marks |
|-------------|-------|
| README: title, description, features, setup | 5 |
| README: screenshots (≥4) showing different views | 5 |
| README: architecture diagram and file descriptions | 5 |
| Code: docstrings on all functions | 5 |
| Code: type hints, consistent naming, no magic numbers | 5 |

### 8. Innovation & Polish (25 marks)

| Requirement | Marks |
|-------------|-------|
| At least one feature not taught in class | 8 |
| Professional UX: loading states, clear labels, consistent styling | 7 |
| Responsive design (works on different screen sizes) | 5 |
| Accessibility: good contrast, meaningful alt text, readable fonts | 5 |

---

## Architecture Template

```
capstone_project/
├── app.py                    # Entry point
├── config.py                 # Configuration
├── data_loader.py            # Data loading functions
├── data_processing.py        # Transformation functions
├── model_utils.py            # ML/AI functions
├── components.py             # Reusable UI components
├── pages/
│   ├── __init__.py
│   ├── home.py               # Overview/dashboard
│   ├── explore.py            # Data exploration
│   ├── predict.py            # ML/AI predictions
│   ├── chat.py               # Chat/AI interface (if applicable)
│   └── about.py              # About/methodology
├── tests/
│   ├── __init__.py
│   ├── test_data.py
│   ├── test_model.py
│   └── test_app.py
├── models/                   # Saved model artifacts (gitignored)
│   └── .gitkeep
├── data/                     # Data files (if applicable)
│   └── .gitkeep
├── requirements.txt
├── requirements-dev.txt      # Dev/test dependencies
├── .gitignore
├── README.md
└── screenshots/
    ├── dashboard.png
    ├── exploration.png
    ├── predictions.png
    └── deployed.png
```

---

## Milestones

| Week | Milestone | Deliverable |
|------|-----------|-------------|
| 1 | Planning + Architecture | Topic selection, file structure, data layer |
| 2 | Core Features | Dashboard, filters, visualizations |
| 3 | ML/AI + Testing | Model working, tests passing, security |
| 4 | Deployment + Polish | Deployed, documented, presented |

### Milestone 1: Project Plan (Due end of Week 1)
- Topic and problem statement
- Dataset description
- Feature list (prioritized)
- Architecture diagram
- Technology choices justified

### Milestone 2: Working Prototype (Due end of Week 2)
- Data loading and display
- Interactive filters working
- At least 2 visualizations
- Basic ML/AI component (can be simplified)

### Milestone 3: Complete Application (Due end of Week 3)
- All features implemented
- Tests passing
- Security measures applied
- Ready for deployment

### Milestone 4: Final Submission (Due end of Week 4)
- Deployed on Community Cloud
- Documentation complete
- Screenshots taken
- Presentation prepared

---

## Submission Checklist

```
✅ Application runs locally without errors
✅ All features functional
✅ Deployed on Community Cloud
✅ README complete with screenshots
✅ All tests passing
✅ No hardcoded secrets
✅ .gitignore configured
✅ requirements.txt present
✅ Code is clean and documented
✅ Presentation prepared
```

---

## Evaluation Rubric

| Grade | Score | Description |
|-------|-------|-------------|
| A+ | 185–200 | Exceptional: innovative, production-ready, well-presented |
| A | 170–184 | Excellent: complete, deployed, well-tested |
| A- | 160–169 | Very Good: strong app, minor gaps |
| B+ | 145–159 | Good: working app, some gaps in testing/polish |
| B | 130–144 | Satisfactory: functional but incomplete |
| B- | 115–129 | Adequate: basic functionality, significant gaps |
| C+ | 100–114 | Marginal: partial app, major features missing |
| C | 80–99 | Below expectations: minimal functionality |
| D | 60–79 | Poor: app doesn't work properly |
| F | < 60 | Failing: no submission or non-functional |

---

## Related Materials

- 📖 All readings: [readings/](../readings/)
- 📓 All notebooks: [notebooks/](../notebooks/)
- 📋 Deployment Checklist: [docs/deployment_checklist.md](../docs/deployment_checklist.md)
- 📋 Security Guide: [docs/security.md](../docs/security.md)
- 📋 Troubleshooting: [docs/deployment_troubleshooting.md](../docs/deployment_troubleshooting.md)
- 🚀 Existing Capstone: [P08 — Capstone](P08_capstone_project.md)
