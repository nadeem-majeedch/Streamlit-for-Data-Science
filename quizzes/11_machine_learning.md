# Quiz 11: Machine Learning with Streamlit

> **📝 Quiz · Module 11 · ML**  
> *Test your understanding of ML deployment with Streamlit.*

---

## Multiple Choice

### Q1. Why should you NOT train a model on every Streamlit rerun?

a) It's not possible in Streamlit  
b) It wastes resources and is slow  
c) Models can't be trained in Python  
d) Streamlit doesn't support ML libraries

---

### Q2. Which decorator should you use to load a trained model?

a) `@st.cache_data`  
b) `@st.cache_resource`  
c) `@st.cache`  
d) `@st.memo`

---

### Q3. What is the correct way to preprocess data at inference time?

```python
# Option A
X_scaled = scaler.fit_transform(X)

# Option B
X_scaled = scaler.transform(X)
```

---

### Q4. Why must you save the scaler/encoder alongside the model?

a) To make the model file smaller  
b) To ensure preprocessing matches training  
c) Scikit-learn requires it  
d) To improve prediction accuracy

---

### Q5. What is a parameterized query in the context of ML deployment?

a) A query with many parameters  
b) User input that's validated before prediction  
c) A query to a database  
d) A SQL injection technique

---

### Q6. How do you handle missing values during batch prediction?

a) Ignore them  
b) Drop rows with missing values  
c) Fill with training statistics (median/mean)  
d) Raise an error

---

### Q7. What should you display for classification predictions?

a) Only the predicted class  
b) The predicted class AND probability/confidence  
c) Only the probability  
d) The raw model output

---

### Q8. Why use `joblib` instead of `pickle` for scikit-learn models?

a) `joblib` is faster for large NumPy arrays  
b) `joblib` is more secure  
c) `pickle` doesn't work with scikit-learn  
d) `joblib` is required by Streamlit

---

### Q9. What is the purpose of input validation?

a) To make the app look better  
b) To prevent errors and invalid predictions  
c) To improve model accuracy  
d) To speed up predictions

---

### Q10. How should you handle a file upload with missing required columns?

a) Predict anyway with defaults  
b) Show error with list of missing columns  
c) Drop the file silently  
d) Create dummy columns

---

### Q11. What is batch prediction?

a) Predicting one sample at a time  
b) Predicting on multiple samples from a file  
c) Training multiple models  
d) Running predictions overnight

---

### Q12. Why is model versioning important?

a) To keep models organized  
b) To track model performance over time  
c) To allow rollback if new model performs poorly  
d) All of the above

---

## Short Answer

### Q13. Explain the complete ML deployment pipeline for a Streamlit app. What are the key steps and why is each important?

---

### Q14. A developer's predictions are completely wrong in production, even though the model performed well during training. What is the most likely cause and how do you fix it?

---

### Q15. Describe three best practices for deploying ML models in Streamlit applications.

---

## Code Completion

### Q16. Complete the model loading function:

```python
import streamlit as st
import joblib

# TODO: Add caching decorator
def load_model_artifacts():
    """Load model, scaler, and metadata."""
    # TODO: Load the three artifacts
    pass

# Usage
model, scaler, meta = load_model_artifacts()
```

---

### Q17. Complete the batch prediction function:

```python
import streamlit as st
import pandas as pd
import numpy as np

def batch_predict(model, scaler, df, feature_names):
    """
    Make predictions on a DataFrame.
    
    Args:
        model: Trained model
        scaler: Fitted scaler
        df: Input DataFrame
        feature_names: List of required feature columns
    
    Returns:
        DataFrame with predictions added
    """
    # TODO: Validate required columns
    missing = [col for col in feature_names if col not in df.columns]
    if missing:
        raise ValueError(f"Missing columns: {missing}")
    
    # TODO: Handle missing values
    # TODO: Preprocess (transform, not fit)
    # TODO: Make predictions
    # TODO: Add predictions to DataFrame
    
    return df
```

---

## Answer Key

### Multiple Choice

1. **B** — Training on every rerun wastes resources and makes the app slow
2. **B** — `@st.cache_resource` returns the same object (singleton) for shared resources
3. **B** — Use `transform()` only, not `fit_transform()`, to match training
4. **B** — Preprocessing must match training exactly to get valid predictions
5. **B** — Validated user input that's safe to use in prediction
6. **C** — Fill with training statistics (median/mean) to maintain distribution
7. **B** — Show both predicted class AND probability for transparency
8. **A** — `joblib` is optimized for large NumPy arrays in scikit-learn
9. **B** — Validation prevents errors and ensures valid predictions
10. **B** — Show clear error with list of missing columns
11. **B** — Batch prediction processes multiple samples from a file
12. **D** — Versioning helps organization, tracking, and rollback

### Short Answer

**Q13.** ML Deployment Pipeline:
1. **Train offline** — Train model on historical data, save artifacts
2. **Save artifacts** — Model, scaler, metadata (feature names, class names)
3. **Load in app** — Use `@st.cache_resource` for fast loading
4. **Get input** — Widgets for single prediction or file upload for batch
5. **Validate** — Check inputs for validity before prediction
6. **Preprocess** — Apply same transformations as training (transform only)
7. **Predict** — Generate predictions with confidence scores
8. **Display** — Show results clearly with context and interpretation

**Q14.** Most likely cause: **Preprocessing mismatch**. The scaler/encoder used during inference was fit on different data than training.

**Fix:** Save the fitted scaler during training and load it for inference. Use `transform()` only, never `fit_transform()` at inference time.

**Q15.** Best practices:
1. **Cache models** — Use `@st.cache_resource` to load once, predict many
2. **Match preprocessing** — Save and reuse the same scaler/encoder
3. **Validate inputs** — Check ranges, types, required fields
4. **Show confidence** — Display probabilities or uncertainty
5. **Handle errors** — Graceful failure for invalid inputs

### Code Completion

**Q16.**
```python
@st.cache_resource
def load_model_artifacts():
    """Load model, scaler, and metadata."""
    model = joblib.load("model.joblib")
    scaler = joblib.load("scaler.joblib")
    meta = joblib.load("meta.joblib")
    return model, scaler, meta
```

**Q17.**
```python
def batch_predict(model, scaler, df, feature_names):
    """Make predictions on a DataFrame."""
    # Validate required columns
    missing = [col for col in feature_names if col not in df.columns]
    if missing:
        raise ValueError(f"Missing columns: {missing}")
    
    # Handle missing values
    if df[feature_names].isnull().any().any():
        df[feature_names] = df[feature_names].fillna(df[feature_names].median())
    
    # Preprocess (transform, not fit)
    X = df[feature_names].values
    X_scaled = scaler.transform(X)
    
    # Make predictions
    predictions = model.predict(X_scaled)
    probabilities = model.predict_proba(X_scaled)
    
    # Add to DataFrame
    df["prediction"] = predictions
    df["confidence"] = probabilities.max(axis=1)
    
    return df
```

---

## Related Materials

- 📖 Reading: [15 — ML with Streamlit](../readings/15_machine_learning_streamlit.md)
- 📓 Notebook: [15 — ML with Streamlit](../notebooks/15_ml_streamlit.ipynb)
- ✏️ Exercise: [15 — ML Workshop](../exercises/15_ml_workshop.py)
- 🖥️ Demo App: [15 — Classification App](../apps/15_classification_app.py)
- 🖥️ Demo App: [15 — Regression App](../apps/15_regression_app.py)
- 🚀 Project: [P06 — ML Model Playground](../projects/P06_ml_model_playground.md)
