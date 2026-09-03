# 15 — Machine Learning with Streamlit

> **📖 Reading · Module 11 · ML**  
> *Deploy trained ML models as interactive Streamlit applications.*

---

## Learning Objectives

After completing this reading you will be able to:

- Save and load trained ML models using joblib
- Build preprocessing pipelines that match training and inference
- Create feature input UIs for different data types
- Implement classification and regression prediction apps
- Handle invalid inputs gracefully
- Display prediction confidence and model performance
- Cache models for performance
- Implement batch and file-based predictions

---

## 1. The ML Deployment Pipeline

```
┌─────────────┐    ┌──────────────┐    ┌─────────────┐
│  Training   │ →  │  Save Model  │ →  │  Load Model │
│  (Offline)  │    │  (joblib)    │    │  (Streamlit)│
└─────────────┘    └──────────────┘    └─────────────┘
                                              │
                                              ▼
┌─────────────┐    ┌──────────────┐    ┌─────────────┐
│  Display    │ ←  │  Predict     │ ←  │  Get Input  │
│  Results    │    │  (Inference) │    │  (Widgets)  │
└─────────────┘    └──────────────┘    └─────────────┘
```

### Key Principle: Train Once, Predict Many

```python
# ❌ WRONG: Retrain on every rerun
if st.button("Predict"):
    model = train_model(data)  # Slow!
    prediction = model.predict(X)

# ✅ CORRECT: Load pre-trained model
@st.cache_resource
def load_model():
    return joblib.load("model.joblib")

model = load_model()  # Fast!
prediction = model.predict(X)
```

---

## 2. Model Persistence with joblib

### Saving a Trained Model

```python
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

# Train model
X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save model
joblib.dump(model, "iris_classifier.joblib")
print(f"Model saved! Accuracy: {model.score(X_test, y_test):.2%}")
```

### Loading in Streamlit

```python
import streamlit as st
import joblib

@st.cache_resource
def load_model():
    """Load pre-trained model (cached as singleton)."""
    return joblib.load("iris_classifier.joblib")

model = load_model()
st.write(f"Model type: {type(model).__name__}")
```

---

## 3. Preprocessing Consistency

### The Critical Rule

**The preprocessing during inference MUST match training exactly.**

```python
# Training script (train_model.py)
from sklearn.preprocessing import StandardScaler
import joblib
import pandas as pd

# Load data
df = pd.read_csv("data.csv")
X = df[["age", "income", "hours"]]
y = df["purchased"]

# Fit scaler on TRAINING data only
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)  # fit_transform on train

# Save both model AND scaler
model.fit(X_scaled, y)
joblib.dump(model, "model.joblib")
joblib.dump(scaler, "scaler.joblib")  # Save scaler too!
```

```python
# Streamlit app (app.py)
import streamlit as st
import joblib
import numpy as np

@st.cache_resource
def load_artifacts():
    """Load model AND scaler together."""
    model = joblib.load("model.joblib")
    scaler = joblib.load("scaler.joblib")
    return model, scaler

model, scaler = load_artifacts()

# Get user input
age = st.number_input("Age", 18, 100, 30)
income = st.number_input("Income", 0, 200000, 50000)
hours = st.number_input("Hours per week", 0, 80, 40)

# Preprocess EXACTLY like training
X = np.array([[age, income, hours]])
X_scaled = scaler.transform(X)  # transform only (not fit!)

# Predict
prediction = model.predict(X_scaled)
```

---

## 4. Feature Input UI Patterns

### Numeric Features

```python
# Single numeric input
age = st.number_input("Age", min_value=0, max_value=120, value=30)

# Slider for bounded range
income = st.slider("Annual Income", 0, 200000, 50000, step=5000)

# With validation
if age < 0 or age > 120:
    st.error("Please enter a valid age (0-120)")
    st.stop()
```

### Categorical Features

```python
# Selectbox for few options
gender = st.selectbox("Gender", ["Male", "Female", "Other"])

# Radio for binary
smoker = st.radio("Smoker?", ["Yes", "No"])

# Multiselect for multiple selections
hobbies = st.multiselect("Hobbies", ["Sports", "Reading", "Gaming", "Cooking"])
```

### Derived Features

```python
# Create features from inputs
age = st.number_input("Age", 18, 100, 30)
income = st.number_input("Income", 0, 200000, 50000)

# Derived feature
income_per_age = income / max(age, 1)  # Avoid division by zero

# Feature engineering matching training
features = {
    "age": age,
    "income": income,
    "income_per_age": income_per_age,
    "is_young": 1 if age < 30 else 0,
}
```

---

## 5. Classification App Pattern

```python
import streamlit as st
import joblib
import numpy as np
import pandas as pd

st.title("🎯 Customer Churn Predictor")

# Load artifacts
@st.cache_resource
def load_model():
    return joblib.load("churn_model.joblib"), joblib.load("churn_scaler.joblib")

model, scaler = load_model()

# Input form
with st.form("prediction_form"):
    col1, col2 = st.columns(2)
    
    with col1:
        age = st.number_input("Age", 18, 100, 35)
        tenure = st.number_input("Tenure (months)", 0, 72, 12)
    
    with col2:
        monthly_charges = st.number_input("Monthly Charges", 0, 200, 50)
        contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
    
    submitted = st.form_submit_button("Predict Churn")

if submitted:
    # Encode categorical
    contract_map = {"Month-to-month": 0, "One year": 1, "Two year": 2}
    
    # Create feature array
    features = np.array([[age, tenure, monthly_charges, contract_map[contract]]])
    
    # Preprocess
    features_scaled = scaler.transform(features)
    
    # Predict
    prediction = model.predict(features_scaled)[0]
    probability = model.predict_proba(features_scaled)[0]
    
    # Display results
    if prediction == 1:
        st.error(f"⚠️ High churn risk: {probability[1]:.1%} probability")
    else:
        st.success(f"✅ Low churn risk: {probability[0]:.1%} probability")
    
    # Confidence metrics
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Churn Probability", f"{probability[1]:.1%}")
    with col2:
        st.metric("Retention Probability", f"{probability[0]:.1%}")
```

---

## 6. Regression App Pattern

```python
import streamlit as st
import joblib
import numpy as np

st.title("🏠 House Price Predictor")

@st.cache_resource
def load_model():
    return joblib.load("house_price_model.joblib"), joblib.load("house_scaler.joblib")

model, scaler = load_model()

# Input
col1, col2, col3 = st.columns(3)
with col1:
    sqft = st.number_input("Square Feet", 500, 5000, 1500)
with col2:
    bedrooms = st.number_input("Bedrooms", 1, 10, 3)
with col3:
    bathrooms = st.number_input("Bathrooms", 1, 5, 2)

age = st.slider("House Age (years)", 0, 100, 10)

if st.button("Predict Price"):
    features = np.array([[sqft, bedrooms, bathrooms, age]])
    features_scaled = scaler.transform(features)
    
    prediction = model.predict(features_scaled)[0]
    
    st.success(f"💰 Predicted Price: ${prediction:,.0f}")
    
    # Confidence interval (if model supports it)
    st.info("💡 This is a point estimate. Actual prices may vary based on location, condition, and market factors.")
```

---

## 7. Handling Invalid Inputs

```python
import streamlit as st
import numpy as np

def validate_inputs(**kwargs):
    """Validate all inputs before prediction."""
    errors = []
    
    if kwargs.get("age", 0) < 0 or kwargs.get("age", 0) > 120:
        errors.append("Age must be between 0 and 120")
    
    if kwargs.get("income", 0) < 0:
        errors.append("Income cannot be negative")
    
    if kwargs.get("hours", 0) < 0 or kwargs.get("hours", 0) > 24:
        errors.append("Hours must be between 0 and 24")
    
    return errors

# Usage
age = st.number_input("Age", 0, 100, 30)
income = st.number_input("Income", 0, 200000, 50000)

if st.button("Predict"):
    errors = validate_inputs(age=age, income=income)
    
    if errors:
        for error in errors:
            st.error(error)
        st.stop()
    
    # Proceed with prediction
    features = np.array([[age, income]])
    prediction = model.predict(features)
```

---

## 8. Batch Prediction

### From Uploaded File

```python
import streamlit as st
import pandas as pd
import joblib

st.title("📊 Batch Prediction")

# Load model
@st.cache_resource
def load_model():
    return joblib.load("model.joblib")

model = load_model()

# Upload file
uploaded = st.file_uploader("Upload CSV for prediction", type=["csv"])

if uploaded:
    df = pd.read_csv(uploaded)
    st.write("Preview:")
    st.dataframe(df.head())
    
    # Validate required columns
    required_cols = ["age", "income", "hours"]
    missing = [col for col in required_cols if col not in df.columns]
    
    if missing:
        st.error(f"Missing columns: {', '.join(missing)}")
    else:
        # Preprocess
        X = df[required_cols].values
        
        # Handle missing values
        if df[required_cols].isnull().any().any():
            st.warning("Found missing values. Filling with median.")
            X = pd.DataFrame(X, columns=required_cols).fillna(pd.DataFrame(X).median()).values
        
        # Predict
        predictions = model.predict(X)
        
        # Add predictions to dataframe
        df["prediction"] = predictions
        
        st.success(f"Generated {len(predictions)} predictions")
        st.dataframe(df)
        
        # Download results
        csv = df.to_csv(index=False)
        st.download_button("Download Predictions", csv, "predictions.csv", "text/csv")
```

---

## 9. Model Performance Display

```python
import streamlit as st
import pandas as pd

def show_classification_metrics(y_true, y_pred, class_names=None):
    """Display classification metrics."""
    from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
    
    accuracy = accuracy_score(y_true, y_pred)
    precision = precision_score(y_true, y_pred, average="weighted")
    recall = recall_score(y_true, y_pred, average="weighted")
    f1 = f1_score(y_true, y_pred, average="weighted")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Accuracy", f"{accuracy:.2%}")
    with col2:
        st.metric("Precision", f"{precision:.2%}")
    with col3:
        st.metric("Recall", f"{recall:.2%}")
    with col4:
        st.metric("F1 Score", f"{f1:.2%}")

def show_regression_metrics(y_true, y_pred):
    """Display regression metrics."""
    from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
    
    mae = mean_absolute_error(y_true, y_pred)
    rmse = mean_squared_error(y_true, y_pred, squared=False)
    r2 = r2_score(y_true, y_pred)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("MAE", f"${mae:,.0f}")
    with col2:
        st.metric("RMSE", f"${rmse:,.0f}")
    with col3:
        st.metric("R²", f"{r2:.3f}")
```

---

## 10. Model Versioning Concepts

```python
import streamlit as st
import joblib
from pathlib import Path

def load_model_version(version="latest"):
    """Load specific model version."""
    model_dir = Path("models")
    
    if version == "latest":
        # Find most recent model
        models = sorted(model_dir.glob("model_v*.joblib"))
        if not models:
            st.error("No models found!")
            return None
        model_path = models[-1]
    else:
        model_path = model_dir / f"model_v{version}.joblib"
    
    if not model_path.exists():
        st.error(f"Model {model_path} not found!")
        return None
    
    return joblib.load(model_path)

# Version selector
version = st.selectbox("Model Version", ["latest", "1.0", "1.1", "2.0"])
model = load_model_version(version)
```

---

## 11. Best Practices

### Do's

1. **Cache models** — use `@st.cache_resource`
2. **Save preprocessors** — scaler, encoder, feature names
3. **Validate inputs** — check ranges, types, required fields
4. **Show confidence** — probabilities, metrics
5. **Handle errors** — invalid inputs, missing data
6. **Document assumptions** — what the model expects

### Don'ts

1. **Don't train on every rerun** — train offline, load in app
2. **Don't skip preprocessing** — must match training exactly
3. **Don't ignore edge cases** — empty inputs, outliers
4. **Don't hide model limitations** — be transparent

---

## 12. Learning vs Production

### Learning Environment

```python
# Simple loading — fine for learning
model = joblib.load("model.joblib")
prediction = model.predict(X)
```

### Production Considerations

```python
# Production-ready pattern
@st.cache_resource(ttl=3600)  # Refresh hourly
def load_model():
    """Load with versioning and validation."""
    model_path = Path("models") / "production" / "model.joblib"
    
    if not model_path.exists():
        raise FileNotFoundError(f"Model not found: {model_path}")
    
    model = joblib.load(model_path)
    
    # Validate model
    if not hasattr(model, "predict"):
        raise ValueError("Invalid model: missing predict method")
    
    return model

def predict_with_logging(model, features):
    """Predict with logging for monitoring."""
    prediction = model.predict(features)
    
    # In production: log to monitoring system
    # log_prediction(features, prediction)
    
    return prediction
```

---

## Key Takeaways

- **Train offline, load in app** — never train on every rerun
- **Cache models with `@st.cache_resource`** — singletons for performance
- **Save preprocessors alongside models** — scaler, encoder, feature names
- **Preprocessing must match exactly** — transform, don't fit_transform at inference
- **Validate all inputs** — ranges, types, required fields
- **Show confidence** — probabilities for classification, intervals for regression
- **Handle edge cases** — missing data, invalid inputs, model failures
- **Batch predictions** — upload CSV, process, download results

---

## Further Reading

- [Scikit-learn Model Persistence](https://scikit-learn.org/stable/model_persistence.html)
- [Joblib Documentation](https://joblib.readthedocs.io/)
- [Streamlit Caching](https://docs.streamlit.io/develop/concepts/architecture/caching)

---

## Related Materials

- 📓 Notebook: [15 — ML with Streamlit](../notebooks/15_ml_streamlit.ipynb)
- ✏️ Exercise: [15 — ML Workshop](../exercises/15_ml_workshop.py)
- 🖥️ Demo App: [15 — Classification App](../apps/15_classification_app.py)
- 🖥️ Demo App: [15 — Regression App](../apps/15_regression_app.py)
- 📝 Quiz: [11 — Machine Learning](../quizzes/11_machine_learning.md)
- 🚀 Project: [P06 — ML Model Playground](../projects/P06_ml_model_playground.md)
