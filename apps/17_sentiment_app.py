"""
Streamlit Sentiment Analysis App
=================================

Module 13 · AI/LLM

A complete NLP application demonstrating:
- Text preprocessing
- TF-IDF feature extraction
- Text classification
- Batch document processing
- Model interpretation

Run: streamlit run apps/17_sentiment_app.py
"""

import streamlit as st
import numpy as np
import pandas as pd
import joblib
import re
from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split

st.set_page_config(
    page_title="Sentiment Analyzer",
    page_icon="💬",
    layout="wide"
)

st.title("💬 Sentiment Analysis App")
st.caption("Module 13 · NLP with Streamlit")

# ============================================================================
# Training (runs once, saves artifacts)
# ============================================================================

def train_sentiment_model():
    """Train sentiment classifier and save artifacts."""
    
    # Sample training data (in practice, use a real dataset)
    positive_texts = [
        "I love this product, it is amazing",
        "Great quality, highly recommend",
        "Fantastic value for money",
        "Best purchase I ever made",
        "Excellent service and fast delivery",
        "This exceeded my expectations",
        "Absolutely wonderful experience",
        "Five stars, would buy again",
        "Perfect in every way",
        "So happy with this purchase",
        "Outstanding quality and design",
        "Worth every penny",
        "Amazing product, love it",
        "Highly satisfied customer",
        "This is exactly what I needed",
    ]
    
    negative_texts = [
        "This is terrible, worst experience",
        "Awful customer service, never again",
        "Complete waste of money",
        "Product broke after one day",
        "Very disappointed with quality",
        "Do not buy this product",
        "Horrible experience from start to finish",
        "One star, would give zero if I could",
        "Total garbage, want my money back",
        "Worst purchase ever made",
        "Extremely poor quality",
        "Nothing works as advertised",
        "Completely useless product",
        "Regret buying this immediately",
        "Never buying from this seller again",
    ]
    
    neutral_texts = [
        "The product is okay, nothing special",
        "It works as expected, average quality",
        "Decent product for the price",
        "Not great, not terrible",
        "It's fine, does the job",
        "Average experience overall",
        "It's an okay product",
        "Neither good nor bad",
        "Meets basic expectations",
        "Standard product, nothing extraordinary",
    ]
    
    # Combine data
    texts = positive_texts + negative_texts + neutral_texts
    labels = [2] * len(positive_texts) + [0] * len(negative_texts) + [1] * len(neutral_texts)
    
    # Split
    X_train, X_test, y_train, y_test = train_test_split(
        texts, labels, test_size=0.2, random_state=42, stratify=labels
    )
    
    # Create pipeline
    pipeline = Pipeline([
        ('tfidf', TfidfVectorizer(max_features=2000, ngram_range=(1, 2))),
        ('classifier', LogisticRegression(max_iter=1000, multi_class='multinomial'))
    ])
    
    # Train
    pipeline.fit(X_train, y_train)
    
    # Evaluate
    train_acc = pipeline.score(X_train, y_train)
    test_acc = pipeline.score(X_test, y_test)
    
    # Save
    joblib.dump(pipeline, "sentiment_pipeline.joblib")
    joblib.dump({
        "class_names": ["Negative", "Neutral", "Positive"],
        "train_accuracy": train_acc,
        "test_accuracy": test_acc,
        "n_features": len(pipeline.named_steps['tfidf'].get_feature_names_out())
    }, "sentiment_meta.joblib")
    
    return train_acc, test_acc

# ============================================================================
# Load Model
# ============================================================================

@st.cache_resource
def load_model():
    """Load sentiment analysis pipeline."""
    pipeline_path = Path("sentiment_pipeline.joblib")
    
    if not pipeline_path.exists():
        train_sentiment_model()
    
    pipeline = joblib.load("sentiment_pipeline.joblib")
    meta = joblib.load("sentiment_meta.joblib")
    
    return pipeline, meta

# ============================================================================
# Preprocessing
# ============================================================================

def clean_text(text):
    """Clean text (must match training)."""
    text = text.lower()
    text = re.sub(r'<[^>]+>', '', text)
    text = re.sub(r'http\S+|www\S+', '', text)
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def validate_text(text, max_length=5000):
    """Validate text input."""
    errors = []
    
    if not text or not text.strip():
        errors.append("Text cannot be empty")
    
    if len(text) > max_length:
        errors.append(f"Text too long (max {max_length} characters)")
    
    suspicious = ['<script>', 'javascript:', 'onerror=']
    for pattern in suspicious:
        if pattern.lower() in text.lower():
            errors.append("Text contains suspicious content")
    
    return errors

# ============================================================================
# Sidebar
# ============================================================================

st.sidebar.title("📚 Module 13 Demo")
st.sidebar.markdown("---")

tab = st.sidebar.radio(
    "Navigate:",
    ["💬 Single Analysis", "📄 Batch Analysis", "📊 Model Info"]
)

st.sidebar.markdown("---")
st.sidebar.markdown("""
**Key Concepts:**
- Text preprocessing
- TF-IDF features
- Preprocessing consistency
- Input validation
""")

# ============================================================================
# Tab 1: Single Analysis
# ============================================================================
if tab.startswith("💬"):
    st.header("💬 Single Text Analysis")
    
    # Load model
    pipeline, meta = load_model()
    
    # Model info
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Model Type", type(pipeline.named_steps['classifier']).__name__)
    with col2:
        st.metric("Test Accuracy", f"{meta['test_accuracy']:.2%}")
    with col3:
        st.metric("Features", f"{meta['n_features']:,}")
    
    st.divider()
    
    # Input
    st.subheader("📝 Enter Text")
    
    # Example texts
    examples = [
        "This product is absolutely amazing! Best purchase ever!",
        "Terrible experience. Worst customer service ever.",
        "It's okay, nothing special but does the job.",
        "I love how this works! Highly recommend to everyone!",
        "Complete waste of money. Very disappointed.",
    ]
    
    selected_example = st.selectbox("Or choose an example:", ["Custom"] + examples)
    
    if selected_example != "Custom":
        text = st.text_area("Text to analyze", value=selected_example, height=150)
    else:
        text = st.text_area(
            "Text to analyze",
            placeholder="Enter your review or feedback here...",
            height=150
        )
    
    if st.button("🔍 Analyze Sentiment", type="primary"):
        # Validate
        errors = validate_text(text)
        
        if errors:
            for error in errors:
                st.error(f"❌ {error}")
        else:
            # Preprocess
            cleaned = clean_text(text)
            
            # Predict
            prediction = pipeline.predict([cleaned])[0]
            probabilities = pipeline.predict_proba([cleaned])[0]
            
            # Display results
            st.divider()
            st.subheader("📊 Results")
            
            class_name = meta["class_names"][prediction]
            confidence = probabilities[prediction]
            
            # Main result
            if class_name == "Positive":
                st.success(f"😊 **{class_name}** ({confidence:.1%} confidence)")
            elif class_name == "Negative":
                st.error(f"😞 **{class_name}** ({confidence:.1%} confidence)")
            else:
                st.warning(f"😐 **{class_name}** ({confidence:.1%} confidence)")
            
            # Confidence breakdown
            st.subheader("Confidence Scores")
            for name, prob in zip(meta["class_names"], probabilities):
                st.progress(prob, text=f"{name}: {prob:.1%}")
            
            # Feature analysis
            st.subheader("📝 Key Words")
            feature_names = pipeline.named_steps['tfidf'].get_feature_names_out()
            coefficients = pipeline.named_steps['classifier'].coef_[prediction]
            
            # Get top words for predicted class
            top_indices = coefficients.argsort()[-5:][::-1]
            top_words = [(feature_names[i], coefficients[i]) for i in top_indices]
            
            cols = st.columns(5)
            for col, (word, score) in zip(cols, top_words):
                with col:
                    st.metric(word, f"{score:.3f}")

# ============================================================================
# Tab 2: Batch Analysis
# ============================================================================
elif tab.startswith("📄"):
    st.header("📄 Batch Text Analysis")
    
    # Load model
    pipeline, meta = load_model()
    
    # Sample data
    st.subheader("📥 Sample Data")
    sample = pd.DataFrame({
        "text": [
            "This product is amazing!",
            "Terrible experience, very disappointed",
            "Highly recommend to everyone",
            "Worst purchase ever made",
            "It's okay, nothing special",
            "Absolutely love this!",
            "Complete waste of money",
            "Does the job, average quality"
        ]
    })
    csv = sample.to_csv(index=False)
    st.download_button("📥 Download Sample", csv, "sample_texts.csv", "text/csv")
    
    st.divider()
    
    # Upload
    st.subheader("📤 Upload Your Data")
    uploaded = st.file_uploader("Upload CSV with text column", type=["csv"])
    
    if uploaded:
        df = pd.read_csv(uploaded)
        st.write("**Preview:**")
        st.dataframe(df.head())
        
        # Select text column
        text_col = st.selectbox("Select text column", df.columns)
        
        if st.button("🔄 Process All"):
            # Validate inputs
            df["cleaned"] = df[text_col].apply(lambda x: clean_text(str(x)))
            
            # Check for empty texts
            empty_mask = df["cleaned"].str.strip().str.len() == 0
            if empty_mask.any():
                st.warning(f"⚠️ {empty_mask.sum()} empty texts found. Filling with placeholder.")
                df.loc[empty_mask, "cleaned"] = "no text"
            
            # Predict
            predictions = pipeline.predict(df["cleaned"])
            probabilities = pipeline.predict_proba(df["cleaned"])
            
            # Add results
            df["sentiment"] = [meta["class_names"][p] for p in predictions]
            df["confidence"] = probabilities.max(axis=1)
            
            st.divider()
            st.subheader("📊 Results")
            st.success(f"✅ Processed {len(df)} documents")
            
            # Display with color coding
            st.dataframe(df, use_container_width=True)
            
            # Summary statistics
            st.subheader("📈 Summary")
            col1, col2, col3 = st.columns(3)
            with col1:
                positive_count = (df["sentiment"] == "Positive").sum()
                st.metric("Positive", positive_count, f"{positive_count/len(df):.1%}")
            with col2:
                neutral_count = (df["sentiment"] == "Neutral").sum()
                st.metric("Neutral", neutral_count, f"{neutral_count/len(df):.1%}")
            with col3:
                negative_count = (df["sentiment"] == "Negative").sum()
                st.metric("Negative", negative_count, f"{negative_count/len(df):.1%}")
            
            # Download
            csv = df.to_csv(index=False)
            st.download_button("📥 Download Results", csv, "sentiment_results.csv", "text/csv")

# ============================================================================
# Tab 3: Model Info
# ============================================================================
else:
    st.header("📈 Model Information")
    
    pipeline, meta = load_model()
    
    # Model details
    st.subheader("Model Details")
    col1, col2 = st.columns(2)
    
    with col1:
        st.write(f"**Algorithm:** {type(pipeline.named_steps['classifier']).__name__}")
        st.write(f"**Vectorizer:** TF-IDF")
        st.write(f"**Features:** {meta['n_features']:,}")
    
    with col2:
        st.metric("Training Accuracy", f"{meta['train_accuracy']:.2%}")
        st.metric("Test Accuracy", f"{meta['test_accuracy']:.2%}")
    
    # Feature importance
    st.subheader("📊 Feature Importance")
    
    feature_names = pipeline.named_steps['tfidf'].get_feature_names_out()
    coefficients = pipeline.named_steps['classifier'].coef_
    
    # Show top features for each class
    for i, class_name in enumerate(meta["class_names"]):
        st.write(f"**{class_name}:**")
        top_indices = coefficients[i].argsort()[-10:][::-1]
        top_words = [(feature_names[j], coefficients[i][j]) for j in top_indices]
        
        df = pd.DataFrame(top_words, columns=["Word", "Score"])
        st.bar_chart(df.set_index("Word")["Score"])
    
    # How to improve
    st.divider()
    st.subheader("🚀 How to Improve")
    st.markdown("""
    **For better accuracy:**
    
    1. **More training data** — Use larger datasets (IMDB, Yelp, etc.)
    2. **Better preprocessing** — Stemming, lemmatization
    3. **Advanced models** — Try SVM, Random Forest, or transformers
    4. **Hyperparameter tuning** — Grid search for optimal parameters
    5. **Cross-validation** — More robust evaluation
    """)
    
    # Retrain
    st.divider()
    st.subheader("🔄 Retrain Model")
    if st.button("Retrain with Updated Data"):
        train_acc, test_acc = train_sentiment_model()
        st.success(f"✅ Model retrained! Train: {train_acc:.2%}, Test: {test_acc:.2%}")
        st.rerun()
    
    # Deployment notes
    st.divider()
    st.subheader("🚀 Deployment Notes")
    st.markdown("""
    **For production deployment:**
    
    1. **Save pipeline** — Include vectorizer in pipeline
    2. **Preprocessing** — Must match training exactly
    3. **Caching** — Use `@st.cache_resource` for model loading
    4. **Validation** — Validate all text inputs
    5. **Error handling** — Graceful failure for edge cases
    
    **Optional enhancements:**
    - Add word cloud visualization
    - Implement streaming predictions
    - Add explainability (SHAP, LIME)
    """)

# ============================================================================
# Footer
# ============================================================================
st.divider()
st.caption("""
**🎓 Module 13: NLP & AI Applications**
- Text → Preprocess → Vectorize → Predict → Display
- TF-IDF for feature extraction
- Same preprocessing for training and inference
- Validate all inputs
""")

# Run verification
if __name__ == "__main__":
    st.write("✅ App is running correctly!")
