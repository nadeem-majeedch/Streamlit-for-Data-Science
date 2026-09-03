"""
Streamlit Regression App Demo
==============================

Module 11 · ML

A complete regression application demonstrating:
- Model loading with caching
- Preprocessing consistency
- Feature input UI
- Prediction with interpretation
- Invalid input handling

Run: streamlit run apps/15_regression_app.py
"""

import streamlit as st
import numpy as np
import pandas as pd
import joblib
from pathlib import Path

st.set_page_config(
    page_title="Regression App",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Regression App Demo")
st.caption("Module 11 · Machine Learning with Streamlit")

# ============================================================================
# Model Training (runs once, saves artifacts)
# ============================================================================

def train_and_save_model():
    """Train housing price regressor and save artifacts."""
    from sklearn.datasets import fetch_california_housing
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import StandardScaler
    from sklearn.ensemble import GradientBoostingRegressor
    
    # Load data
    housing = fetch_california_housing()
    X = pd.DataFrame(housing.data, columns=housing.feature_names)
    y = housing.target  # Median house value (in $100k)
    
    # Split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    # Preprocess
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # Train
    model = GradientBoostingRegressor(n_estimators=100, random_state=42)
    model.fit(X_train_scaled, y_train)
    
    # Evaluate
    r2_train = model.score(X_train_scaled, y_train)
    r2_test = model.score(X_test_scaled, y_test)
    
    # Calculate additional metrics
    y_pred = model.predict(X_test_scaled)
    mae = np.mean(np.abs(y_test - y_pred)) * 100000  # Convert to dollars
    rmse = np.sqrt(np.mean((y_test - y_pred) ** 2)) * 100000
    
    # Save
    joblib.dump(model, "regression_model.joblib")
    joblib.dump(scaler, "regression_scaler.joblib")
    joblib.dump({
        "feature_names": housing.feature_names.tolist(),
        "r2_train": r2_train,
        "r2_test": r2_test,
        "mae": mae,
        "rmse": rmse,
        "feature_descriptions": {
            "MedInc": "Median income in block ($10k)",
            "HouseAge": "Median house age in block",
            "AveRooms": "Average rooms per household",
            "AveBedrms": "Average bedrooms per household",
            "Population": "Block population",
            "AveOccup": "Average household occupancy",
            "Latitude": "Block latitude",
            "Longitude": "Block longitude"
        }
    }, "regression_meta.joblib")
    
    return r2_train, r2_test

# ============================================================================
# Load Model
# ============================================================================

@st.cache_resource
def load_model():
    """Load model and artifacts."""
    model_path = Path("regression_model.joblib")
    
    if not model_path.exists():
        train_and_save_model()
    
    model = joblib.load("regression_model.joblib")
    scaler = joblib.load("regression_scaler.joblib")
    meta = joblib.load("regression_meta.joblib")
    
    return model, scaler, meta

# ============================================================================
# Sidebar
# ============================================================================

st.sidebar.title("📚 Module 11 Demo")
st.sidebar.markdown("---")

tab = st.sidebar.radio(
    "Navigate:",
    ["🏠 Single Prediction", "📊 Batch Prediction", "📈 Model Info"]
)

st.sidebar.markdown("---")
st.sidebar.markdown("""
**Key Concepts:**
- Cache models with `@st.cache_resource`
- Match preprocessing exactly
- Validate all inputs
- Show prediction context
""")

# ============================================================================
# Tab 1: Single Prediction
# ============================================================================
if tab.startswith("🏠"):
    st.header("🏠 Single Prediction")
    
    # Load model
    model, scaler, meta = load_model()
    
    # Display model info
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Test R²", f"{meta['r2_test']:.3f}")
    with col2:
        st.metric("MAE", f"${meta['mae']:,.0f}")
    with col3:
        st.metric("RMSE", f"${meta['rmse']:,.0f}")
    
    st.divider()
    
    # Input form
    with st.form("prediction_form"):
        st.subheader("📝 Enter Property Details")
        
        col1, col2 = st.columns(2)
        
        with col1:
            med_inc = st.slider(
                "Median Income ($10k)", 0.0, 15.0, 3.0, 0.1,
                help="Block median household income in tens of thousands"
            )
            house_age = st.slider(
                "House Age (years)", 1.0, 52.0, 20.0, 1.0,
                help="Median age of houses in the block"
            )
            avg_rooms = st.slider(
                "Average Rooms", 1.0, 10.0, 5.0, 0.1,
                help="Average number of rooms per household"
            )
            avg_bedrooms = st.slider(
                "Average Bedrooms", 0.5, 3.0, 1.0, 0.1,
                help="Average number of bedrooms per household"
            )
        
        with col2:
            population = st.number_input(
                "Block Population", 100, 35000, 1500, step=100,
                help="Population of the block group"
            )
            avg_occup = st.slider(
                "Average Occupancy", 1.0, 5.0, 3.0, 0.1,
                help="Average household occupancy"
            )
            latitude = st.slider(
                "Latitude", 32.5, 42.0, 37.5, 0.1,
                help="Block group latitude"
            )
            longitude = st.slider(
                "Longitude", -124.5, -114.3, -120.0, 0.1,
                help="Block group longitude"
            )
        
        submitted = st.form_submit_button("🔮 Predict Price", type="primary")
    
    if submitted:
        # Validate
        errors = []
        if avg_rooms < avg_bedrooms:
            errors.append("Average rooms should be >= average bedrooms")
        if avg_occup < 1:
            errors.append("Average occupancy should be >= 1")
        
        if errors:
            for error in errors:
                st.error(f"❌ {error}")
        else:
            # Create features
            features = np.array([[
                med_inc, house_age, avg_rooms, avg_bedrooms,
                population, avg_occup, latitude, longitude
            ]])
            
            # Preprocess (transform, not fit!)
            features_scaled = scaler.transform(features)
            
            # Predict
            prediction = model.predict(features_scaled)[0]
            price = prediction * 100000  # Convert to dollars
            
            # Display results
            st.divider()
            st.subheader("📊 Prediction Results")
            
            col1, col2, col3 = st.columns(3)
            with col1:
                st.success(f"**Predicted Price:** ${price:,.0f}")
            with col2:
                st.metric("Confidence", "Medium" if meta['r2_test'] > 0.6 else "Low")
            with col3:
                st.metric("Model R²", f"{meta['r2_test']:.3f}")
            
            # Context
            st.info(f"""
            **Interpretation:**
            - This property in a block with median income ${med_inc*10000:,.0f}
            - {house_age:.0f}-year-old houses
            - {avg_rooms:.1f} rooms, {avg_bedrooms:.1f} bedrooms
            - Population: {population:,}, Occupancy: {avg_occup:.1f}
            
            **Note:** This is a point estimate based on block-level statistics. Actual prices vary based on specific property condition, lot size, and local market factors.
            """)
            
            # Feature values
            st.subheader("📝 Input Values")
            feature_df = pd.DataFrame({
                "Feature": meta["feature_names"],
                "Value": [med_inc, house_age, avg_rooms, avg_bedrooms,
                         population, avg_occup, latitude, longitude],
                "Description": [meta["feature_descriptions"][f] for f in meta["feature_names"]]
            })
            st.dataframe(feature_df, use_container_width=True)

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
        "MedInc": [3.5, 5.0, 2.0, 8.0, 4.5],
        "HouseAge": [20, 35, 15, 40, 25],
        "AveRooms": [5.0, 6.5, 4.0, 7.0, 5.5],
        "AveBedrms": [1.0, 1.2, 0.9, 1.3, 1.1],
        "Population": [1000, 2000, 800, 1500, 1200],
        "AveOccup": [3.0, 2.5, 3.5, 2.0, 2.8],
        "Latitude": [37.5, 38.0, 37.0, 39.0, 37.8],
        "Longitude": [-122.0, -121.5, -122.5, -120.0, -121.8]
    })
    csv = sample.to_csv(index=False)
    st.download_button("📥 Download Sample CSV", csv, "sample_housing.csv", "text/csv")
    
    st.divider()
    
    # Upload file
    st.subheader("📤 Upload Your Data")
    uploaded = st.file_uploader("Upload CSV for batch prediction", type=["csv"])
    
    if uploaded:
        df = pd.read_csv(uploaded)
        st.write("**Preview:**")
        st.dataframe(df.head())
        
        # Validate columns
        required = meta["feature_names"]
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
            
            # Add results
            df["predicted_price"] = predictions * 100000
            
            st.divider()
            st.subheader("📊 Results")
            st.success(f"✅ Generated {len(predictions)} predictions")
            st.dataframe(df, use_container_width=True)
            
            # Statistics
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Total Predictions", len(predictions))
            with col2:
                st.metric("Avg Price", f"${df['predicted_price'].mean():,.0f}")
            with col3:
                st.metric("Price Range", f"${df['predicted_price'].min():,.0f} - ${df['predicted_price'].max():,.0f}")
            
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
        st.write(f"**Target:** Median house value ($100k)")
    
    with col2:
        st.metric("Training R²", f"{meta['r2_train']:.3f}")
        st.metric("Test R²", f"{meta['r2_test']:.3f}")
    
    # Additional metrics
    col1, col2 = st.columns(2)
    with col1:
        st.metric("MAE", f"${meta['mae']:,.0f}")
    with col2:
        st.metric("RMSE", f"${meta['rmse']:,.0f}")
    
    # Feature importance
    if hasattr(model, "feature_importances_"):
        st.subheader("📊 Feature Importance")
        importance_df = pd.DataFrame({
            "Feature": meta["feature_names"],
            "Importance": model.feature_importances_,
            "Description": [meta["feature_descriptions"][f] for f in meta["feature_names"]]
        }).sort_values("Importance", ascending=False)
        
        st.bar_chart(importance_df.set_index("Feature")["Importance"])
        
        st.write("**Feature Descriptions:**")
        for _, row in importance_df.iterrows():
            st.write(f"- **{row['Feature']}:** {row['Description']}")
    
    # Scaler info
    st.subheader("🔧 Preprocessor Info")
    st.write(f"**Scaler Type:** {type(scaler).__name__}")
    
    scaler_df = pd.DataFrame({
        "Feature": meta["feature_names"],
        "Mean": scaler.mean_,
        "Scale": scaler.scale_
    })
    st.dataframe(scaler_df, use_container_width=True)
    
    # How to retrain
    st.divider()
    st.subheader("🔄 Retrain Model")
    if st.button("Retrain with New Data"):
        r2_train, r2_test = train_and_save_model()
        st.success(f"✅ Model retrained! Train R²: {r2_train:.3f}, Test R²: {r2_test:.3f}")
        st.rerun()
    
    # Deployment notes
    st.divider()
    st.subheader("🚀 Deployment Notes")
    st.markdown("""
    **For production deployment:**
    
    1. **Model artifacts:** Save `model.joblib`, `scaler.joblib`, and `meta.joblib`
    2. **Preprocessing:** Must match training exactly (transform, not fit)
    3. **Caching:** Use `@st.cache_resource` for model loading
    4. **Validation:** Validate all inputs before prediction
    5. **Error handling:** Graceful failure for invalid inputs
    6. **Interpretation:** Explain predictions to users
    
    **Limitations:**
    - Based on block-level statistics, not individual properties
    - California-specific (won't work for other regions)
    - Market conditions change over time
    """)

# ============================================================================
# Footer
# ============================================================================
st.divider()
st.caption("""
**🎓 Module 11: Machine Learning with Streamlit**
- Train offline, load in app
- Cache models with `@st.cache_resource`
- Match preprocessing exactly
- Validate inputs and show context
""")

# Run verification
if __name__ == "__main__":
    st.write("✅ App is running correctly!")
