# Assignment 04 — Machine Learning Production Application

> **📋 Assignment · Level 4–6 (ML / AI / Production) — Modules 11–16**
> *Build, test, and deploy a complete ML application with security and monitoring.*

---

## Course Information

| Field | Detail |
|-------|--------|
| **Course** | Streamlit for Data Science |
| **Assignment** | A04 — Machine Learning Production Application |
| **Due Date** | End of Week 16 (or as capstone alternative) |
| **Weight** | 8% of course grade |
| **Difficulty** | ★★★★☆ Advanced |
| **Collaboration** | Individual |

---

## Learning Outcomes

After completing this assignment you will be able to:

1. **LO1** — Train, persist, and deploy an ML model in a Streamlit app (Apply)
2. **LO2** — Build a complete prediction pipeline with preprocessing consistency (Analyze)
3. **LO3** — Implement security best practices for a deployed application (Evaluate)
4. **LO4** — Deploy and verify a Streamlit app on Community Cloud (Apply)
5. **LO5** — Design and implement batch prediction workflows (Create)
6. **LO6** — Write tests for a Streamlit application using `st.testing.AppTest` (Evaluate)

---

## Prerequisites

- Completed Modules 11–16
- Scikit-learn basics (train/test, fit/predict)
- Model persistence with joblib
- Security concepts (secrets, input validation)
- Deployment on Streamlit Community Cloud
- `st.testing.AppTest` basics

---

## Overview

Build an **ML Model Playground** — a production-quality Streamlit application
that lets users interact with a trained machine learning model. The application
must include single prediction, batch prediction, model explanation, security
measures, tests, and successful deployment on Community Cloud.

This is the most comprehensive assignment in the course. It tests your ability
to bring together all skills from the entire curriculum.

---

## Architecture Requirements

```
assignments/A04/
├── app.py                    # Entry point with navigation
├── config.py                 # Model paths, feature names, constants
├── model_utils.py            # Training, loading, prediction functions
├── data_processing.py        # Preprocessing, validation, feature engineering
├── components.py             # Reusable UI components
├── security.py               # Input validation, sanitization
├── tests/
│   ├── __init__.py
│   ├── test_model_utils.py   # Unit tests for model functions
│   ├── test_processing.py    # Unit tests for preprocessing
│   └── test_app.py           # Streamlit AppTest integration tests
├── models/                   # Saved model artifacts (gitignored)
│   ├── .gitkeep
│   └── (model files generated at runtime)
├── requirements.txt
├── .gitignore
├── README.md
└── screenshots/
```

---

## Tasks

### Task 1: Model Training & Persistence (15 marks)

| Requirement | Marks |
|-------------|-------|
| Train a classification model on a real dataset (e.g., Wine, Breast Cancer) | 3 |
| Save model artifacts (model, scaler, feature names) with joblib | 3 |
| Separate training script or function that can be re-run | 2 |
| `@st.cache_resource` for model loading (singleton pattern) | 3 |
| Display model metadata: type, features, training date, accuracy | 2 |
| Handle missing model files gracefully (train if not found) | 2 |

### Task 2: Preprocessing & Input UI (15 marks)

| Requirement | Marks |
|-------------|-------|
| Feature input widgets match training feature types exactly | 4 |
| Numeric features: `st.number_input` with correct min/max/step | 3 |
| Categorical features: `st.selectbox` with correct options | 3 |
| Input validation: reject out-of-range values with clear messages | 3 |
| Preprocessing matches training pipeline exactly (same scaler/encoder) | 2 |

### Task 3: Prediction & Confidence (15 marks)

| Requirement | Marks |
|-------------|-------|
| Single prediction with clear result display | 3 |
| Classification: show predicted class and probability for each class | 4 |
| Regression: show predicted value with confidence interval | 3 |
| `st.metric()` or `st.success()` for prediction result | 2 |
| Prediction history stored in session state (last 10 predictions) | 3 |

### Task 4: Batch Prediction (10 marks)

| Requirement | Marks |
|-------------|-------|
| File upload for batch CSV prediction | 3 |
| Validate uploaded file columns match expected features | 3 |
| Display batch predictions in a DataFrame | 2 |
| Download button for results CSV with predictions column | 2 |

### Task 5: Model Explanation (10 marks)

| Requirement | Marks |
|-------------|-------|
| Feature importance display (bar chart or table) | 4 |
| For tree models: show top N features driving predictions | 3 |
| For single predictions: show which features contributed most | 3 |

### Task 6: Security (10 marks)

| Requirement | Marks |
|-------------|-------|
| No hardcoded secrets in source code | 2 |
| All user inputs validated before processing | 2 |
| SQL injection awareness (if using database) | 1 |
| `.gitignore` excludes secrets, model files, __pycache__ | 2 |
| README documents how to configure secrets | 1 |
| Input length/type limits enforced | 2 |

### Task 7: Testing (10 marks)

| Requirement | Marks |
|-------------|-------|
| Unit test for model loading (`test_model_utils.py`) | 2 |
| Unit test for preprocessing functions (`test_processing.py`) | 2 |
| `st.testing.AppTest` test for app loading without errors | 2 |
| `st.testing.AppTest` test for widget interactions | 2 |
| All tests pass: `pytest tests/ -v` | 2 |

### Task 8: Deployment (10 marks)

| Requirement | Marks |
|-------------|-------|
| App successfully deployed on Community Cloud | 3 |
| All features work in deployed version | 2 |
| No hardcoded paths or secrets | 2 |
| `requirements.txt` correct for deployment | 1 |
| Deployment URL provided in README | 2 |

### Task 9: Documentation (5 marks)

| Requirement | Marks |
|-------------|-------|
| README with title, description, features, screenshots | 2 |
| Setup instructions and deployment link | 1 |
| Model performance metrics documented | 1 |
| Architecture description | 1 |

**Total: 100 marks**

---

## Deliverables

1. **Complete application** with all files in architecture
2. **`tests/` directory** with passing tests
3. **`README.md`** with full documentation
4. **Deployed app URL** on Community Cloud
5. **Screenshot(s)** of local and deployed versions

### Submission

```
assignments/A04/
├── app.py
├── config.py
├── model_utils.py
├── data_processing.py
├── components.py
├── security.py
├── requirements.txt
├── .gitignore
├── README.md
├── screenshots/
│   ├── prediction.png
│   ├── batch.png
│   ├── model_info.png
│   └── deployed.png
├── tests/
│   ├── __init__.py
│   ├── test_model_utils.py
│   ├── test_processing.py
│   └── test_app.py
└── models/
    └── .gitkeep
```

---

## Starter Template

```python
# app.py
import streamlit as st
from model_utils import load_model
from data_processing import preprocess_input
from security import validate_input

st.set_page_config(page_title="ML Playground", layout="wide")
st.title("🤖 ML Model Playground")

# Load model
model = load_model()
if model is None:
    st.error("Model not found. Please run train_model.py first.")
    st.stop()

# Navigation
page = st.sidebar.radio("Navigate", ["Predict", "Batch", "Model Info"])

if page == "Predict":
    # TODO: Build single prediction UI
    pass
elif page == "Batch":
    # TODO: Build batch prediction UI
    pass
else:
    # TODO: Build model info page
    pass
```

---

## Grading Rubric Summary

| Category | Marks | Bloom's Level |
|----------|-------|---------------|
| Model Training & Persistence | 15 | Apply |
| Preprocessing & Input UI | 15 | Apply, Analyze |
| Prediction & Confidence | 15 | Apply, Create |
| Batch Prediction | 10 | Apply |
| Model Explanation | 10 | Analyze |
| Security | 10 | Evaluate |
| Testing | 10 | Evaluate |
| Deployment | 10 | Apply |
| Documentation | 5 | Evaluate |
| **Total** | **100** | |

---

## Recommended Datasets

| Dataset | Task | Features | Source |
|---------|------|----------|--------|
| Wine Quality | Classification | 11 numeric | `sklearn.datasets.load_wine()` |
| Breast Cancer | Classification | 30 numeric | `sklearn.datasets.load_breast_cancer()` |
| California Housing | Regression | 8 numeric | `sklearn.datasets.fetch_california_housing()` |
| Diabetes | Regression | 10 numeric | `sklearn.datasets.load_diabetes()` |

---

## Common Mistakes to Avoid

1. **❌ Training on every rerun** — Train once, save, load with caching
2. **❌ Preprocessing mismatch** — Save the exact scaler from training
3. **❌ No input validation** — Out-of-range values crash the model
4. **❌ Hardcoded paths** — Use `config.py` or `pathlib`
5. **❌ No tests** — Assignment requires `st.testing.AppTest`
6. **❌ Secrets in code** — Community Cloud scan will reject
7. **❌ Missing requirements.txt** — Deployment fails without it

---

## Related Materials

- 📖 Reading: [Machine Learning](../readings/15_machine_learning_streamlit.md)
- 📖 Reading: [Security](../readings/security_and_secrets.md)
- 📖 Reading: [Deployment](../readings/deployment_guide.md)
- 📖 Reading: [LLM/RAG](../readings/18_llm_rag_applications.md)
- 📓 Notebook: [15 — ML Streamlit](../notebooks/15_ml_streamlit.ipynb)
- 📓 Notebook: [Security Lab](../notebooks/security_practical_lab.ipynb)
- 📓 Notebook: [Deployment Tutorial](../notebooks/deployment_tutorial.ipynb)
- ✏️ Exercise: [15 — ML Workshop](../exercises/15_ml_workshop.py)
- ✏️ Exercise: [Security](../exercises/security_exercises.md)
- ✏️ Exercise: [Deployment](../exercises/deployment_exercises.py)
- 🖥️ Demo: [15 — Classification](../apps/15_classification_app.py)
- 🖥️ Demo: [15 — Regression](../apps/15_regression_app.py)
- 🚀 Project: [P06 — ML Playground](../projects/P06_ml_model_playground.md)
- 🚀 Project: [P08 — Capstone](../projects/P08_capstone_project.md)
- 📋 Checklist: [Deployment](../docs/deployment_checklist.md)
