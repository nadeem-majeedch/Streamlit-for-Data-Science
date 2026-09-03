# P11 — Machine Learning Prediction App

> **🚀 Project · Advanced · M10–M12**
> *Build an end-to-end ML prediction application with preprocessing, training, and inference.*
> Difficulty: ★★★☆☆ · Duration: 2 weeks · Weight: Part of 15% project grade

---

## Problem Statement

A hospital wants to predict patient readmission risk. Build a Streamlit app that trains a classification model on historical patient data, provides single-patient prediction, batch prediction from CSV, and explains model decisions.

---

## Learning Objectives

1. Train, save, and load ML models with joblib (CLO8)
2. Build preprocessing pipelines that match training/inference (CLO8)
3. Create prediction UIs with input validation (CLO2, CLO8)
4. Display model explainability (feature importance) (CLO3)
5. Implement batch prediction with file upload (CLO2)

---

## Prerequisites

- Completed Modules 10–12
- Scikit-learn basics (train/test split, fit/predict)
- joblib for model persistence
- `@st.cache_resource` for model loading

---

## Dataset

```python
from sklearn.datasets import make_classification
import pandas as pd
import numpy as np

np.random.seed(42)
X, y = make_classification(n_samples=1000, n_features=8, n_informative=5, random_state=42)
df = pd.DataFrame(X, columns=[f"feature_{i}" for i in range(8)])
df["readmitted"] = y
df["age"] = np.random.randint(18, 85, 1000)
df["length_of_stay"] = np.random.randint(1, 14, 1000)
```

---

## Functional Requirements

| # | Requirement | Marks |
|---|-------------|-------|
| F1 | Train model on dataset with train/test split | 6 |
| F2 | Save model + scaler with joblib | 4 |
| F3 | Load model with `@st.cache_resource` | 4 |
| F4 | Single prediction: input widgets for all features, predict button | 8 |
| F5 | Display predicted class and probability for each class | 6 |
| F6 | Batch prediction: upload CSV, validate columns, predict all rows | 8 |
| F7 | Download batch results as CSV | 4 |
| F8 | Feature importance chart (bar chart) | 6 |
| F9 | Model info panel: accuracy, feature count, model type | 4 |
| F10 | Input validation: reject out-of-range values | 5 |
| F11 | Error handling for missing model files | 5 |

**Total: 60 marks**

---

## Architecture

```
ml_predictor/
├── app.py
├── model_utils.py      # Train, load, predict functions
├── preprocessing.py    # Feature processing
├── config.py           # Feature names, model paths
├── models/             # Saved artifacts (gitignored)
├── tests/
│   ├── test_model.py
│   └── test_preprocessing.py
├── requirements.txt
└── README.md
```

---

## Evaluation Criteria

| Criteria | Marks |
|----------|-------|
| ML pipeline (train → save → load → predict) | 25 |
| UI quality (prediction interface, batch upload) | 15 |
| Preprocessing consistency | 10 |
| Testing | 5 |
| Documentation | 5 |
| **Total** | **60** |

---

## Extensions

- Add SHAP values for prediction explanation
- Add model comparison (train 2+ algorithms)
- Add cross-validation scores
- Add real-time model retraining

---

## Related Materials

- 📖 Reading: [ML Streamlit](../readings/15_machine_learning_streamlit.md)
- 📓 Notebook: [15 — ML](../notebooks/15_ml_streamlit.ipynb)
- ✏️ Exercise: [15 — ML Workshop](../exercises/15_ml_workshop.py)
- 🖥️ Demo: [15 — Classification](../apps/15_classification_app.py)
- 🚀 Project: [P06 — ML Playground](P06_ml_model_playground.md)
