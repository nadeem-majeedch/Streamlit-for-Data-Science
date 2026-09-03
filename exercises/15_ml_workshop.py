"""
Exercise 15: Machine Learning Workshop
=======================================

Module 11 · ML

Master ML deployment with Streamlit.

Learning Objectives:
- Save and load models with joblib
- Build preprocessing pipelines
- Create prediction UIs
- Handle invalid inputs
- Implement batch prediction

Instructions:
Complete each section by filling in the TODOs.
Run with: streamlit run exercises/15_ml_workshop.py
"""

import streamlit as st
import numpy as np
import pandas as pd
import joblib
from pathlib import Path

st.set_page_config(page_title="ML Workshop", page_icon="🤖", layout="wide")
st.title("🤖 Exercise 15: Machine Learning Workshop")
st.markdown("*Module 11 · ML — Deploy models with Streamlit*")

st.divider()

# ============================================================================
# SETUP: Train a sample model
# ============================================================================

@st.cache_resource
def get_model():
    """Train and cache a sample model."""
    from sklearn.datasets import make_classification
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import StandardScaler
    from sklearn.ensemble import RandomForestClassifier
    
    # Generate synthetic data
    X, y = make_classification(
        n_samples=1000, n_features=5, n_informative=3,
        n_redundant=1, random_state=42
    )
    feature_names = ["feature_1", "feature_2", "feature_3", "feature_4", "feature_5"]
    
    # Split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Preprocess
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # Train
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train_scaled, y_train)
    
    # Save
    joblib.dump(model, "workshop_model.joblib")
    joblib.dump(scaler, "workshop_scaler.joblib")
    joblib.dump({
        "feature_names": feature_names,
        "accuracy": model.score(X_test_scaled, y_test)
    }, "workshop_meta.joblib")
    
    return model, scaler, {"feature_names": feature_names, "accuracy": model.score(X_test_scaled, y_test)}

model, scaler, meta = get_model()

st.info(f"📦 Sample model loaded: {type(model).__name__}, Accuracy: {meta['accuracy']:.2%}")

# ============================================================================
# CHALLENGE 1: Single Prediction
# ============================================================================
st.header("🎯 Challenge 1: Single Prediction")
st.write("Build a prediction form with validation.")

# TODO: Create input widgets for 5 features
# st.subheader("📝 Enter Features")
# col1, col2 = st.columns(2)
# with col1:
#     f1 = st.slider("Feature 1", -3.0, 3.0, 0.0, 0.1)
#     f2 = st.slider("Feature 2", -3.0, 3.0, 0.0, 0.1)
# with col2:
#     f3 = st.slider("Feature 3", -3.0, 3.0, 0.0, 0.1)
#     f4 = st.slider("Feature 4", -3.0, 3.0, 0.0, 0.1)
# f5 = st.slider("Feature 5", -3.0, 3.0, 0.0, 0.1)

# TODO: Validate inputs
# def validate_features(f1, f2, f3, f4, f5):
#     errors = []
#     # Add validation logic
#     return errors

# TODO: Make prediction
# if st.button("Predict"):
#     errors = validate_features(f1, f2, f3, f4, f5)
#     if errors:
#         for error in errors:
#             st.error(error)
#     else:
#         features = np.array([[f1, f2, f3, f4, f5]])
#         features_scaled = scaler.transform(features)
#         prediction = model.predict(features_scaled)[0]
#         probabilities = model.predict_proba(features_scaled)[0]
#         
#         st.success(f"Prediction: Class {prediction}")
#         st.write(f"Confidence: {probabilities[prediction]:.1%}")

st.divider()

# ============================================================================
# CHALLENGE 2: Batch Prediction
# ============================================================================
st.header("🎯 Challenge 2: Batch Prediction")
st.write("Implement batch prediction from uploaded file.")

# TODO: Create sample data for download
# sample = pd.DataFrame({
#     "feature_1": np.random.randn(5),
#     "feature_2": np.random.randn(5),
#     ...
# })
# csv = sample.to_csv(index=False)
# st.download_button("Download Sample", csv, "sample.csv", "text/csv")

# TODO: File uploader
# uploaded = st.file_uploader("Upload CSV", type=["csv"])
# if uploaded:
#     df = pd.read_csv(uploaded)
#     st.dataframe(df.head())
#     
#     # Validate columns
#     required = meta["feature_names"]
#     missing = [col for col in required if col not in df.columns]
#     if missing:
#         st.error(f"Missing: {missing}")
#     else:
#         # Preprocess
#         X = df[required].values
#         X_scaled = scaler.transform(X)
#         
#         # Predict
#         predictions = model.predict(X_scaled)
#         df["prediction"] = predictions
#         
#         st.dataframe(df)
#         
#         # Download
#         csv = df.to_csv(index=False)
#         st.download_button("Download Results", csv, "predictions.csv", "text/csv")

st.divider()

# ============================================================================
# CHALLENGE 3: Model Info Display
# ============================================================================
st.header("🎯 Challenge 3: Model Information")
st.write("Display model details and feature importance.")

# TODO: Show model info
# st.write(f"**Model Type:** {type(model).__name__}")
# st.write(f"**Accuracy:** {meta['accuracy']:.2%}")
# st.write(f"**Features:** {', '.join(meta['feature_names'])}")

# TODO: Show feature importance
# if hasattr(model, "feature_importances_"):
#     importance_df = pd.DataFrame({
#         "Feature": meta["feature_names"],
#         "Importance": model.feature_importances_
#     }).sort_values("Importance", ascending=False)
#     
#     st.bar_chart(importance_df.set_index("Feature")["Importance"])

st.divider()

# ============================================================================
# CHALLENGE 4: Error Handling
# ============================================================================
st.header("🎯 Challenge 4: Error Handling")
st.write("Implement robust error handling.")

# TODO: Create safe prediction function
# def safe_predict(features):
#     try:
#         features_scaled = scaler.transform(features)
#         prediction = model.predict(features_scaled)[0]
#         probabilities = model.predict_proba(features_scaled)[0]
#         return prediction, probabilities, None
#     except Exception as e:
#         return None, None, str(e)

# TODO: Test with edge cases
# st.subheader("🧪 Test Edge Cases")
# test_cases = [
#     ("Normal", [0.5, 0.5, 0.5, 0.5, 0.5]),
#     ("Extreme", [10.0, 10.0, 10.0, 10.0, 10.0]),
#     ("Negative", [-5.0, -5.0, -5.0, -5.0, -5.0]),
# ]
# 
# for name, features in test_cases:
#     st.write(f"**{name}:** {features}")
#     pred, probs, error = safe_predict(np.array([features]))
#     if error:
#         st.error(f"Error: {error}")
#     else:
#         st.success(f"Prediction: {pred}, Confidence: {probs[pred]:.1%}")

st.divider()

# ============================================================================
# BONUS: Custom Model Upload
# ============================================================================
st.header("🏆 Bonus: Custom Model Upload")
st.write("Upload your own trained model.")

# TODO: Model file upload
# model_file = st.file_uploader("Upload Model (.joblib)", type=["joblib"])
# scaler_file = st.file_uploader("Upload Scaler (.joblib)", type=["joblib"])
# 
# if model_file and scaler_file:
#     custom_model = joblib.load(model_file)
#     custom_scaler = joblib.load(scaler_file)
#     
#     st.write(f"**Model Type:** {type(custom_model).__name__}")
#     
#     # Use custom model for predictions
#     ...

st.divider()

# ============================================================================
# COMPLETION
# ============================================================================
st.success("🎉 Workshop Complete!")
st.markdown("""
**What you practiced:**
- ✅ Model loading with caching
- ✅ Preprocessing consistency
- ✅ Single and batch prediction
- ✅ Input validation
- ✅ Error handling
- ✅ Model information display

**Key ML deployment rules:**
- Train offline, load in app
- Cache models with `@st.cache_resource`
- Match preprocessing exactly (transform, not fit)
- Validate all inputs
- Show confidence and context

**Next steps:**
- Read: [ML with Streamlit](../readings/15_machine_learning_streamlit.md)
- Notebook: [ML with Streamlit](../notebooks/15_ml_streamlit.ipynb)
- Demo Apps: [Classification](../apps/15_classification_app.py), [Regression](../apps/15_regression_app.py)
""")

# Run check
if __name__ == "__main__":
    st.write("✅ Exercise file is valid and ready to run!")
