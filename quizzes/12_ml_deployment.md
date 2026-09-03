# Quiz 12 — ML Model Deployment

> **📝 Post-Quiz · Module 12 · ML**
> *Test your understanding of deploying ML models with Streamlit.*
> ⏱ Time: 15 minutes · 📊 Points: 25 · Bloom's: Apply, Analyze

---

## Part A: Multiple Choice (2 points each)

### Q1. Why should you NOT train a model inside a Streamlit rerun?

(a) Streamlit doesn't support scikit-learn
(b) Training on every rerun wastes resources and is slow
(c) Models can only be trained in Jupyter notebooks
(d) Streamlit caches training automatically

**CLO:** CLO8

---

### Q2. Which decorator is correct for loading a trained ML model?

(a) `@st.cache_data`
(b) `@st.cache_resource`
(c) `@st.memo`
(d) `@st.cache`

**CLO:** CLO8, CLO5

---

### Q3. At inference time, you should:

(a) Call `scaler.fit_transform(X)` on the input
(b) Call `scaler.transform(X)` on the input
(c) Train a new scaler on the input
(d) Skip preprocessing

**CLO:** CLO8

---

### Q4. What is the PRIMARY reason to save the scaler alongside the model?

(a) To reduce file size
(b) To ensure preprocessing matches training exactly
(c) Scikit-learn requires it
(d) To improve accuracy

**CLO:** CLO8

---

### Q5. In a classification app, you should display:

(a) Only the predicted class label
(b) The predicted class AND probability for each class
(c) Only the raw model output
(d) The training accuracy

**CLO:** CLO8

---

## Part B: True/False (1 point each)

### Q6. `joblib.dump()` can save both the model and the scaler in one call.

**CLO:** CLO8

---

### Q7. Batch prediction means predicting on a single input at a time.

**CLO:** CLO8

---

### Q8. You should validate uploaded CSV columns before running batch prediction.

**CLO:** CLO8, CLO10

---

## Part C: Code Output (3 points each)

### Q9. What is wrong with this preprocessing code?

```python
# During training
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)

# During inference (in Streamlit app)
scaler = StandardScaler()
X_scaled = scaler.transform(X)
prediction = model.predict(X_scaled)
```

**CLO:** CLO8

---

### Q10. What does this code display?

```python
import numpy as np
model = ...  # trained classifier
scaler = ...  # fitted scaler

features = np.array([[5.1, 3.5, 1.4, 0.2]])
features_scaled = scaler.transform(features)
pred = model.predict(features_scaled)[0]
probs = model.predict_proba(features_scaled)[0]

st.success(f"Class: {pred}")
st.write(f"Confidence: {probs[pred]:.1%}")
```

Assuming the model predicts class 0 with 92% confidence.

**CLO:** CLO8

---

## Part D: Short Answer (3 points each)

### Q11. Explain the complete flow from training a model to deploying it in a Streamlit app. Include at least 5 steps.

**CLO:** CLO8

---

### A12. Your batch prediction app crashes when a user uploads a CSV with a column named "feature_1 " (note the trailing space). Explain why this happens and how to prevent it.

**CLO:** CLO8, CLO10

---

## Part E: Architecture (4 points)

### Q13. Design the file structure for an ML deployment app. Include what each file is responsible for and why separation matters.

**CLO:** CLO8, CLO6

---

## Answer Key

> ⚠️ **Instructor copy**

| Q | Answer | Explanation | Bloom's |
|---|--------|-------------|---------|
| Q1 | **(b)** | Training on every rerun is wasteful; train once, save, load with caching. | Apply |
| Q2 | **(b)** | `@st.cache_resource` for singletons (models, DB connections). | Apply |
| Q3 | **(b)** | Only `transform()` at inference — never `fit_transform()`. | Apply |
| Q4 | **(b)** | Preprocessing must match training exactly for valid predictions. | Analyze |
| Q5 | **(b)** | Probabilities help users understand prediction confidence. | Apply |
| Q6 | **False** | `joblib.dump()` saves one object. Use separate calls or a dict. | Apply |
| Q7 | **False** | Batch prediction processes multiple inputs at once (e.g., from a CSV). | Understand |
| Q8 | **True** | Column name mismatches cause KeyError crashes. | Apply |
| Q9 | A new `StandardScaler()` is created at inference, which is untrained. `transform()` on an untrained scaler produces incorrect values. The fix: save the trained scaler with `joblib.dump()` and load it with `joblib.load()`. | Analyze |
| Q10 | Displays: "Class: 0" and "Confidence: 92.0%" | Apply |
| Q11 | 1) Train model offline. 2) Save model + scaler + metadata with joblib. 3) Create Streamlit app. 4) Load model with `@st.cache_resource`. 5) Build input UI. 6) Apply saved preprocessing. 7) Predict and display results. 8) Handle errors gracefully. | Apply |
| Q12 | The trailing space in the column name doesn't match the expected feature name. Fix: strip whitespace from column names after upload (`df.columns = df.columns.str.strip()`). | Analyze |
| Q13 | `app.py` (entry point), `model_utils.py` (train/load/predict), `data_processing.py` (preprocessing), `config.py` (constants), `components.py` (UI). Separation enables testing, reuse, and maintenance. | Analyze |

---

## CLO Mapping

| CLO | Questions |
|-----|-----------|
| CLO5 — Optimize performance | Q2 |
| CLO6 — Design well-architected apps | Q13 |
| CLO8 — Deploy ML models | Q1–Q13 |
| CLO10 — Test and secure apps | Q8, Q12 |

---

## Related Materials

- 📖 Reading: [Machine Learning Streamlit](../readings/15_machine_learning_streamlit.md)
- 📓 Notebook: [15 — ML Streamlit](../notebooks/15_ml_streamlit.ipynb)
- ✏️ Exercise: [15 — ML Workshop](../exercises/15_ml_workshop.py)
- 🖥️ Demo: [15 — Classification](../apps/15_classification_app.py)
