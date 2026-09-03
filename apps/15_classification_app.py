"""
Streamlit Classification App Demo
==================================

Module 11 · ML

A complete classification application demonstrating:
- Model loading with caching
- Preprocessing consistency
- Feature input UI
- Prediction with confidence
- Invalid input handling
- Batch prediction

Run: streamlit run apps/15_classification_app.py
"""

import streamlit as st
import numpy as np
import pandas as pd
import joblib
from pathlib import Path

st.set_page_config(
    page_title="Classification App",
    page_icon="🎯",
    layout="wide"
)

st.title("🎯 Classification App Demo")
st.caption("Module 11 · Machine Learning with Streamlit")

# ============================================================================
# Model Training (runs once, saves artifacts)
# ============================================================================

def train_and_save_model():
    """Train iris classifier and save artifacts."""
    from sklearn.datasets import load_iris
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import StandardScaler
    from sklearn.ensemble import RandomForestClassifier
    
    # Load data
    iris = load_iris()
    X = pd.DataFrame(iris.data, columns=iris.feature_names)
    y = iris.target
    
    # Split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    
    # Preprocess
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # Train
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train_scaled, y_train)
    
    # Evaluate
    train_acc = model.score(X_train_scaled, y_train)
    test_acc = model.score(X_test_scaled, y_test)
    
    # Save
    joblib.dump(model, "classification_model.joblib")
    joblib.dump(scaler, "classification_scaler.joblib")
    joblib.dump({
        "feature_names": iris.feature_names,
        "class_names": iris.target_names.tolist(),
        "train_accuracy": train_acc,
        "test_accuracy": test_acc
    }, "classification_meta.joblib")
    
    return train_acc, test_acc

# ============================================================================
# Load Model
# ============================================================================

@st.cache_resource
def load_model():
    """Load model and artifacts."""
    model_path = Path("classification_model.joblib")
    
    if not model_path.exists():
        # Train if not exists
        train_and_save_model()
    
    model = joblib.load("classification_model.joblib")
    scaler = joblib.load("classification_scaler.joblib")
    meta = joblib.load("classification_meta.joblib")
    
    return model, scaler, meta

# ============================================================================
# Validation
# ============================================================================

def validate_inputs(sl, sw, pl, pw):
    """Validate Iris feature inputs."""
    errors = []
    
    if not (4.0 <= sl <= 8.0):
        errors.append("Sepal Length must be 4.0-8.0 cm")
    if not (2.0 <= sw <= 4.5):
        errors.append("Sepal Width must be 2.0-4.5 cm")
    if not (1.0 <= pl <= 7.0):
        errors.append("Petal Length must be 1.0-7.0 cm")
    if not (0.1 <= pw <= 2.5):
        errors.append("Petal Width must be 0.1-2.5 cm")
    
    return errors

# ============================================================================
# Sidebar
# ============================================================================

st.sidebar.title("📚 Module 11 Demo")
st.sidebar.markdown("---")

tab = st.sidebar.radio(
    "Navigate:",
    ["🎯 Single Prediction", "📊 Batch Prediction", "📈 Model Info"]
)

st.sidebar.markdown("---")
st.sidebar.markdown("""
**Key Concepts:**
- Cache models with `@st.cache_resource`
- Match preprocessing exactly
- Validate all inputs
- Show confidence scores
""")

# ============================================================================
# Tab 1: Single Prediction
# ============================================================================
if tab.startswith("🎯"):
    st.header("🎯 Single Prediction")
    
    # Load model
    model, scaler, meta = load_model()
    
    # Display model info
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Model Type", type(model).__name__)
    with col2:
        st.metric("Test Accuracy", f"{meta['test_accuracy']:.2%}")
    
    st.divider()
    
    # Input form
    with st.form("prediction_form"):
        st.subheader("📝 Enter Features")
        
        col1, col2 = st.columns(2)
        
        with col1:
            sepal_length = st.slider(
                "Sepal Length (cm)", 4.0, 8.0, 5.4, 0.1,
                help="Length of the sepal in centimeters"
            )
            sepal_width = st.slider(
                "Sepal Width (cm)", 2.0, 4.5, 3.4, 0.1,
                help="Width of the sepal in centimeters"
            )
        
        with col2:
            petal_length = st.slider(
                "Petal Length (cm)", 1.0, 7.0, 1.5, 0.1,
                help="Length of the petal in centimeters"
            )
            petal_width = st.slider(
                "Petal Width (cm)", 0.1, 2.5, 0.2, 0.1,
                help="Width of the petal in centimeters"
            )
        
        submitted = st.form_submit_button("🔮 Predict", type="primary")
    
    if submitted:
        # Validate
        errors = validate_inputs(sepal_length, sepal_width, petal_length, petal_width)
        
        if errors:
            for error in errors:
                st.error(f"❌ {error}")
        else:
            # Create features
            features = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
            
            # Preprocess (transform, not fit!)
            features_scaled = scaler.transform(features)
            
            # Predict
            prediction = model.predict(features_scaled)[0]
            probabilities = model.predict_proba(features_scaled)[0]
            
            # Display results
            st.divider()
            st.subheader("📊 Prediction Results")
            
            # Main prediction
            class_name = meta["class_names"][prediction]
            confidence = probabilities[prediction]
            
            col1, col2, col3 = st.columns(3)
            with col1:
                st.success(f"**Predicted Species:** {class_name}")
            with col2:
                st.metric("Confidence", f"{confidence:.1%}")
            with col3:
                st.metric("Certainty", "High" if confidence > 0.8 else "Medium" if confidence > 0.6 else "Low")
            
            # Probability breakdown
            st.subheader("📈 Probability Breakdown")
            prob_df = pd.DataFrame({
                "Species": meta["class_names"],
                "Probability": probabilities
            }).sort_values("Probability", ascending=False)
            
            st.bar_chart(prob_df.set_index("Species")["Probability"])
            
            # All probabilities
            for name, prob in zip(meta["class_names"], probabilities):
                st.progress(prob, text=f"{name}: {prob:.1%}")

# ============================================================================
# Tab 2: Batch Prediction
# ============================================================================
elif tab.startswith("📊"):
    st.header("📊 Batch Prediction")
    
    # Load model
    model, scaler, meta = load_model()
    
    # Sample data for download
    st.subheader("📥 Sample Data")
    sample = pd.DataFrame({
        "sepal_length": [5.1, 4.9, 7.0, 6.4, 5.5],
        "sepal_width": [3.5, 3.0, 3.2, 3.2, 2.5],
        "petal_length": [1.4, 1.4, 4.7, 4.5, 4.0],
        "petal_width": [0.2, 0.2, 1.4, 1.5, 1.3]
    })
    csv = sample.to_csv(index=False)
    st.download_button("📥 Download Sample CSV", csv, "sample_iris.csv", "text/csv")
    
    st.divider()
    
    # Upload file
    st.subheader("📤 Upload Your Data")
    uploaded = st.file_uploader("Upload CSV for batch prediction", type=["csv"])
    
    if uploaded:
        df = pd.read_csv(uploaded)
        st.write("**Preview:**")
        st.dataframe(df.head())
        
        # Validate columns
        required = ["sepal_length", "sepal_width", "petal_length", "petal_width"]
        missing = [col for col in required if col not in df.columns]
        
        if missing:
            st.error(f"❌ Missing required columns: {', '.join(missing)}")
            st.info(f"Required columns: {', '.join(required)}")
        else:
            # Check for missing values
            if df[required].isnull().any().any():
                st.warning("⚠️ Found missing values. Filling with median.")
                df[required] = df[required].fillna(df[required].median())
            
            # Preprocess
            X = df[required].values
            X_scaled = scaler.transform(X)
            
            # Predict
            predictions = model.predict(X_scaled)
            probabilities = model.predict_proba(X_scaled)
            
            # Add results
            df["predicted_species"] = [meta["class_names"][p] for p in predictions]
            df["confidence"] = probabilities.max(axis=1)
            
            st.divider()
            st.subheader("📊 Results")
            st.success(f"✅ Generated {len(predictions)} predictions")
            st.dataframe(df, use_container_width=True)
            
            # Statistics
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Total Predictions", len(predictions))
            with col2:
                st.metric("Avg Confidence", f"{df['confidence'].mean():.1%}")
            with col3:
                st.metric("Species Found", df["predicted_species"].nunique())
            
            # Download
            csv = df.to_csv(index=False)
            st.download_button("📥 Download Predictions", csv, "predictions.csv", "text/csv")

# ============================================================================
# Tab 3: Model Info
# ============================================================================
else:
    st.header("📈 Model Information")
    
    model, scaler, meta = load_model()
    
    # Model details
    st.subheader("Model Details")
    col1, col2 = st.columns(2)
    
    with col1:
        st.write(f"**Type:** {type(model).__name__}")
        st.write(f"**Features:** {len(meta['feature_names'])}")
        st.write(f"**Classes:** {len(meta['class_names'])}")
        st.write(f"**Class Names:** {', '.join(meta['class_names'])}")
    
    with col2:
        st.metric("Training Accuracy", f"{meta['train_accuracy']:.2%}")
        st.metric("Test Accuracy", f"{meta['test_accuracy']:.2%}")
    
    # Feature importance
    if hasattr(model, "feature_importances_"):
        st.subheader("📊 Feature Importance")
        importance_df = pd.DataFrame({
            "Feature": meta["feature_names"],
            "Importance": model.feature_importances_
        }).sort_values("Importance", ascending=False)
        
        st.bar_chart(importance_df.set_index("Feature")["Importance"])
    
    # Scaler info
    st.subheader("🔧 Preprocessor Info")
    st.write(f"**Scaler Type:** {type(scaler).__name__}")
    st.write(f"**Scaler Mean:** {scaler.mean_.tolist()}")
    st.write(f"**Scaler Scale:** {scaler.scale_.tolist()}")
    
    # How to retrain
    st.divider()
    st.subheader("🔄 Retrain Model")
    if st.button("Retrain with New Data"):
        train_acc, test_acc = train_and_save_model()
        st.success(f"✅ Model retrained! Train: {train_acc:.2%}, Test: {test_acc:.2%}")
        st.rerun()
    
    # Deployment info
    st.divider()
    st.subheader("🚀 Deployment Notes")
    st.markdown("""
    **For production deployment:**
    
    1. **Model artifacts:** Save `model.joblib`, `scaler.joblib`, and `meta.joblib`
    2. **Preprocessing:** Must match training exactly (transform, not fit)
    3. **Caching:** Use `@st.cache_resource` for model loading
    4. **Validation:** Validate all inputs before prediction
    5. **Error handling:** Graceful failure for invalid inputs
    6. **Secrets:** Never hard-code credentials
    """)
    
    # Download model artifacts
    st.divider()
    st.subheader("📥 Download Model Artifacts")
    
    with open("classification_model.joblib", "rb") as f:
        st.download_button("📥 Download Model", f, "model.joblib", "application/octet-stream")
    
    with open("classification_scaler.joblib", "rb") as f:
        st.download_button("📥 Download Scaler", f, "scaler.joblib", "application/octet-stream")

# ============================================================================
# Footer
# ============================================================================
st.divider()
st.caption("""
**🎓 Module 11: Machine Learning with Streamlit**
- Train offline, load in app
- Cache models with `@st.cache_resource`
- Match preprocessing exactly
- Validate inputs and show confidence
""")

# Run verification
if __name__ == "__main__":
    st.write("✅ App is running correctly!")
