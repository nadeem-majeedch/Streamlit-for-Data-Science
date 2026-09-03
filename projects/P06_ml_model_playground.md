# P06 — ML Model Playground

> **🚀 Project · Module 11 · ML**  
> *Build an interactive machine learning model training and prediction application.*

---

## Project Overview

Create a Streamlit application that allows users to:
1. Upload or select datasets
2. Configure and train ML models
3. Evaluate model performance
4. Make predictions on new data
5. Download trained models

This project demonstrates the complete ML deployment pipeline.

---

## Learning Objectives

By completing this project, you will be able to:

- Build end-to-end ML applications with Streamlit
- Implement proper train/test separation
- Create intuitive ML configuration UIs
- Visualize model performance metrics
- Deploy trained models for inference
- Handle file uploads for batch prediction

---

## Functional Requirements

### 1. Dataset Selection
- [ ] Option to use built-in datasets (Iris, Wine, Breast Cancer)
- [ ] Option to upload custom CSV files
- [ ] Display dataset overview (shape, columns, types, statistics)
- [ ] Preview first 10 rows

### 2. Model Configuration
- [ ] Select algorithm (Random Forest, SVM, KNN, Decision Tree)
- [ ] Configure hyperparameters (with sensible defaults)
- [ ] Option for train/test split ratio
- [ ] Option for cross-validation

### 3. Training
- [ ] Train model with selected configuration
- [ ] Display training progress/status
- [ ] Save trained model artifacts

### 4. Evaluation
- [ ] Display accuracy metrics (accuracy, precision, recall, F1)
- [ ] Show confusion matrix
- [ ] Display feature importance (if applicable)
- [ ] Visualize predictions vs actual

### 5. Prediction
- [ ] Single prediction with input form
- [ ] Batch prediction from uploaded CSV
- [ ] Download predictions as CSV
- [ ] Download trained model

---

## UI Requirements

### Layout
```
┌─────────────────────────────────────────────────────┐
│  Sidebar                           │  Main Content  │
│  ─────────                         │  ───────────── │
│  • Dataset selection               │  • Overview    │
│  • Model configuration             │  • Training    │
│  • Training controls               │  • Evaluation  │
│  • Navigation                      │  • Prediction  │
└─────────────────────────────────────────────────────┘
```

### Pages/Tabs
1. **Data** — Dataset selection and overview
2. **Train** — Model configuration and training
3. **Evaluate** — Model performance metrics
4. **Predict** — Single and batch prediction

---

## Technical Requirements

### Models
- Use scikit-learn algorithms
- Support at least 4 classifiers
- Proper train/test split
- Cross-validation option

### Caching
- Cache dataset loading
- Cache trained models
- Cache evaluation results

### Validation
- Validate uploaded files
- Validate inputs before prediction
- Handle missing values
- Display meaningful error messages

### Preprocessing
- Handle categorical encoding
- Scale numerical features
- Match preprocessing between train/inference

---

## Implementation Guide

### Step 1: Project Structure

```
P06_ml_playground/
├── app.py                 # Main entry point
├── pages/
│   ├── data.py           # Data loading and overview
│   ├── train.py          # Model training
│   ├── evaluate.py       # Model evaluation
│   └── predict.py        # Predictions
├── utils/
│   ├── __init__.py
│   ├── data_loader.py    # Dataset functions
│   ├── model.py          # Model training functions
│   └── preprocessing.py  # Preprocessing functions
├── requirements.txt
└── README.md
```

### Step 2: Data Module

```python
# utils/data_loader.py
import streamlit as st
import pandas as pd
from sklearn.datasets import load_iris, load_wine, load_breast_cancer

@st.cache_data
def load_builtin_dataset(name):
    """Load a built-in sklearn dataset."""
    datasets = {
        "iris": load_iris,
        "wine": load_wine,
        "breast_cancer": load_breast_cancer
    }
    data = datasets[name]()
    df = pd.DataFrame(data.data, columns=data.feature_names)
    df["target"] = data.target
    return df, data.target_names

def load_uploaded_dataset(file):
    """Load dataset from uploaded CSV."""
    return pd.read_csv(file)
```

### Step 3: Training Module

```python
# utils/model.py
import streamlit as st
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split, cross_val_score
import joblib

def get_model(algorithm, params):
    """Get model instance with parameters."""
    models = {
        "Random Forest": RandomForestClassifier,
        "Gradient Boosting": GradientBoostingClassifier,
        "SVM": SVC,
        "KNN": KNeighborsClassifier
    }
    return models[algorithm](**params)

@st.cache_resource
def train_model(X_train, y_train, model):
    """Train and return model."""
    model.fit(X_train, y_train)
    return model

def save_artifacts(model, scaler, feature_names, path):
    """Save model artifacts."""
    joblib.dump(model, f"{path}/model.joblib")
    joblib.dump(scaler, f"{path}/scaler.joblib")
    joblib.dump({"feature_names": feature_names}, f"{path}/meta.joblib")
```

### Step 4: Prediction Module

```python
# pages/predict.py
import streamlit as st
import joblib
import numpy as np
import pandas as pd

def single_prediction(model, scaler, feature_names):
    """Single prediction interface."""
    st.subheader("Single Prediction")
    
    with st.form("predict"):
        features = {}
        for name in feature_names:
            features[name] = st.number_input(name, value=0.0)
        
        if st.form_submit_button("Predict"):
            X = np.array([[features[name] for name in feature_names]])
            X_scaled = scaler.transform(X)
            prediction = model.predict(X_scaled)[0]
            st.success(f"Prediction: {prediction}")

def batch_prediction(model, scaler, feature_names):
    """Batch prediction from file upload."""
    st.subheader("Batch Prediction")
    
    uploaded = st.file_uploader("Upload CSV", type=["csv"])
    if uploaded:
        df = pd.read_csv(uploaded)
        # Validate, preprocess, predict, download
        ...
```

---

## Experiments to Try

1. **Algorithm Comparison** — Train multiple algorithms and compare performance
2. **Hyperparameter Tuning** — Adjust parameters and observe impact
3. **Feature Selection** — Try different feature subsets
4. **Cross-Validation** — Compare simple split vs. k-fold CV
5. **Custom Datasets** — Test with your own data

---

## Common Mistakes to Avoid

1. ❌ Training on every rerun (use caching)
2. ❌ Preprocessing mismatch (save and reuse scaler)
3. ❌ Not validating inputs
4. ❌ Showing raw model internals to users
5. ❌ Not handling missing values

---

## Testing Checklist

- [ ] Dataset loads correctly (built-in and uploaded)
- [ ] Model trains without errors
- [ ] Metrics display correctly
- [ ] Single prediction works with valid inputs
- [ ] Single prediction handles invalid inputs gracefully
- [ ] Batch prediction processes CSV correctly
- [ ] Downloads work (predictions, model)
- [ ] No training on every rerun
- [ ] Preprocessing matches between train/inference

---

## Extension Ideas

1. **Regression mode** — Support regression datasets
2. **Model comparison** — Side-by-side algorithm comparison
3. **SHAP explanations** — Add model interpretability
4. **AutoML** — Automatic algorithm selection
5. **API endpoint** — Expose prediction as REST API
6. **Database logging** — Log predictions to database

---

## Grading Rubric

| Component | Points | Criteria |
|-----------|--------|----------|
| **Functionality** | 40 | All features work correctly |
| **UI/UX** | 20 | Intuitive interface, good feedback |
| **Code Quality** | 20 | Clean, modular, well-documented |
| **ML Best Practices** | 15 | Proper train/test, caching, validation |
| **Error Handling** | 5 | Graceful failure for edge cases |

---

## Submission

1. Push code to GitHub repository
2. Deploy to Streamlit Community Cloud (if applicable)
3. Submit repository URL
4. Include README with:
   - Setup instructions
   - Feature list
   - Screenshots
   - Known limitations

---

## Related Materials

- 📖 Reading: [15 — ML with Streamlit](../readings/15_machine_learning_streamlit.md)
- 📓 Notebook: [15 — ML with Streamlit](../notebooks/15_ml_streamlit.ipynb)
- 🖥️ Demo App: [15 — Classification App](../apps/15_classification_app.py)
- 🖥️ Demo App: [15 — Regression App](../apps/15_regression_app.py)
- 📝 Quiz: [11 — Machine Learning](../quizzes/11_machine_learning.md)
