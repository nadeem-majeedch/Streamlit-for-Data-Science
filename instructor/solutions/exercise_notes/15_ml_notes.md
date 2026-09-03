# Exercise 15 — ML Workshop: Solution Notes

> **👩‍🏫 Instructor Reference**
> *Expected approach, key code, and grading guidance.*

---

## Setup: Model Training

### Expected Approach
The exercise already provides a setup function that trains and caches a RandomForest model. Students must use the pre-trained model, not retrain.

### Key Verification Points
- Students should NOT add their own training code
- Model, scaler, and metadata are already loaded via `get_model()`
- Feature names are in `meta["feature_names"]`

---

## Challenge 1: Single Prediction

### Expected Approach
5 feature sliders, validation function, prediction with confidence display.

### Key Code
```python
st.subheader("Enter Features")
col1, col2 = st.columns(2)
with col1:
    f1 = st.slider("Feature 1", -3.0, 3.0, 0.0, 0.1)
    f2 = st.slider("Feature 2", -3.0, 3.0, 0.0, 0.1)
with col2:
    f3 = st.slider("Feature 3", -3.0, 3.0, 0.0, 0.1)
    f4 = st.slider("Feature 4", -3.0, 3.0, 0.0, 0.1)
f5 = st.slider("Feature 5", -3.0, 3.0, 0.0, 0.1)

if st.button("Predict", type="primary"):
    features = np.array([[f1, f2, f3, f4, f5]])
    features_scaled = scaler.transform(features)
    prediction = model.predict(features_scaled)[0]
    probabilities = model.predict_proba(features_scaled)[0]

    st.success(f"Prediction: **Class {prediction}**")
    st.write(f"Confidence: **{probabilities[prediction]:.1%}**")

    # Show probabilities for all classes
    prob_df = pd.DataFrame({
        "Class": model.classes_,
        "Probability": probabilities,
    })
    st.bar_chart(prob_df.set_index("Class"))
```

### Common Mistakes
- Forgetting to apply `scaler.transform()` before prediction
- Using raw features instead of scaled features
- Not displaying probabilities (only class label)

### Grading Notes (25 marks)
- Full marks: Sliders work, prediction correct, confidence displayed, probabilities shown
- 18 marks: Prediction works but missing probability display
- 10 marks: Basic prediction works

---

## Challenge 2: Batch Prediction

### Key Code
```python
uploaded = st.file_uploader("Upload CSV for batch prediction", type=["csv"])

if uploaded:
    df = pd.read_csv(uploaded)
    st.dataframe(df.head())

    required = meta["feature_names"]
    missing = [col for col in required if col not in df.columns]

    if missing:
        st.error(f"Missing columns: {missing}")
    else:
        X = df[required].values
        X_scaled = scaler.transform(X)
        predictions = model.predict(X_scaled)
        probabilities = model.predict_proba(X_scaled)

        df["prediction"] = predictions
        df["confidence"] = probabilities.max(axis=1).round(4)

        st.dataframe(df, use_container_width=True)

        # Download
        csv = df.to_csv(index=False)
        st.download_button("Download Results", csv, "predictions.csv")
```

### Common Mistakes
- Not validating columns before prediction
- Not applying scaler to batch data
- Missing download button

---

## Challenge 3: Model Info

### Key Code
```python
st.subheader("Model Information")
col1, col2 = st.columns(2)
with col1:
    st.write(f"**Type:** {type(model).__name__}")
    st.write(f"**Accuracy:** {meta['accuracy']:.2%}")
    st.write(f"**Features:** {len(meta['feature_names'])}")
with col2:
    st.write(f"**Feature Names:** {meta['feature_names']}")
    st.write(f"**Classes:** {list(model.classes_)}")
    st.write(f"**Estimators:** {model.n_estimators}")

# Feature importance
importances = model.feature_importances_
imp_df = pd.DataFrame({
    "Feature": meta["feature_names"],
    "Importance": importances,
}).sort_values("Importance", ascending=True)
st.bar_chart(imp_df.set_index("Feature"))
```

---

## Challenge 4: Error Handling

### Key Code
```python
def validate_features(features):
    errors = []
    for i, val in enumerate(features):
        if val < -3 or val > 3:
            errors.append(f"Feature {i+1} = {val} is outside range [-3, 3]")
    if len(features) != 5:
        errors.append(f"Expected 5 features, got {len(features)}")
    return errors

# Usage
features = [f1, f2, f3, f4, f5]
errors = validate_features(features)
if errors:
    for e in errors:
        st.error(e)
else:
    # Proceed with prediction
    pass
```

### Grading Notes (25 marks)
- Full marks: All 4 challenges work, preprocessing consistent, error handling
- 18 marks: Single and batch prediction work, info partial
- 10 marks: Basic prediction works

---

## Common Pattern: Preprocessing Consistency

**CRITICAL:** The scaler used during training must be used during inference.

```python
# WRONG: Training new scaler during inference
scaler = StandardScaler()
X_scaled = scaler.fit_transform(features)  # WRONG!

# RIGHT: Using the saved scaler
features_scaled = scaler.transform(features)  # Only transform, not fit!
```
