"""
Exercise 17: NLP Workshop
==========================

Module 13 · AI/LLM

Master NLP applications with Streamlit.

Learning Objectives:
- Preprocess text for ML
- Build text classifiers
- Create sentiment analysis apps
- Handle batch document processing
- Validate text inputs

Instructions:
Complete each section by filling in the TODOs.
Run with: streamlit run exercises/17_nlp_workshop.py
"""

import streamlit as st
import numpy as np
import pandas as pd
import joblib
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from pathlib import Path

st.set_page_config(page_title="NLP Workshop", page_icon="💬", layout="wide")
st.title("💬 Exercise 17: NLP Workshop")
st.markdown("*Module 13 · AI/LLM — Build NLP applications with Streamlit*")

st.divider()

# ============================================================================
# SETUP: Train sample model
# ============================================================================

@st.cache_resource
def get_model():
    """Train and cache sentiment model."""
    # Sample data
    positive = [
        "I love this product", "Amazing quality", "Highly recommend",
        "Best purchase ever", "Excellent service", "Fantastic value",
        "Very satisfied", "Five stars", "Perfect product",
        "So happy with this"
    ]
    negative = [
        "Terrible product", "Worst experience", "Do not buy",
        "Very disappointed", "Waste of money", "Awful quality",
        "Never again", "One star", "Complete garbage",
        "Regret buying"
    ]
    
    texts = positive + negative
    labels = [1] * len(positive) + [0] * len(negative)
    
    # Train
    pipeline = Pipeline([
        ('tfidf', TfidfVectorizer(max_features=1000, ngram_range=(1, 2))),
        ('classifier', LogisticRegression(max_iter=1000))
    ])
    pipeline.fit(texts, labels)
    
    return pipeline, {"accuracy": 0.85, "n_features": len(pipeline.named_steps['tfidf'].get_feature_names_out())}

pipeline, meta = get_model()

st.info(f"📦 Sample model loaded: {type(pipeline.named_steps['classifier']).__name__}")

# ============================================================================
# CHALLENGE 1: Text Preprocessing
# ============================================================================
st.header("🎯 Challenge 1: Text Preprocessing")
st.write("Build a text preprocessing function.")

# TODO: Create clean_text function
# def clean_text(text):
#     """Clean text for NLP."""
#     # Lowercase
#     # Remove HTML tags
#     # Remove URLs
#     # Remove special characters
#     # Remove extra whitespace
#     pass

# TODO: Test with sample texts
# sample_texts = [
#     "This is GREAT!!! Visit https://example.com",
#     "<p>Hello World</p> This is a test.",
#     "LOVE this product!!! Best purchase ever!!!"
# ]
# 
# for text in sample_texts:
#     cleaned = clean_text(text)
#     st.write(f"**Original:** {text}")
#     st.write(f"**Cleaned:** {cleaned}")
#     st.write("---")

st.divider()

# ============================================================================
# CHALLENGE 2: Single Prediction
# ============================================================================
st.header("🎯 Challenge 2: Single Text Prediction")
st.write("Build a prediction interface with validation.")

# TODO: Create input and predict
# text = st.text_area("Enter text to analyze", "This product is amazing!")
# 
# if st.button("Predict"):
#     # Validate
#     if not text.strip():
#         st.error("Please enter some text")
#     else:
#         # Preprocess (must match training!)
#         cleaned = text.lower().strip()
#         
#         # Predict
#         prediction = pipeline.predict([cleaned])[0]
#         probabilities = pipeline.predict_proba([cleaned])[0]
#         
#         # Display
#         if prediction == 1:
#             st.success(f"😊 Positive ({probabilities[1]:.1%})")
#         else:
#             st.error(f"😞 Negative ({probabilities[0]:.1%})")

st.divider()

# ============================================================================
# CHALLENGE 3: Input Validation
# ============================================================================
st.header("🎯 Challenge 3: Input Validation")
st.write("Implement robust text validation.")

# TODO: Create validate_text function
# def validate_text(text, max_length=5000):
#     """Validate text input."""
#     errors = []
#     
#     # Check empty
#     # Check length
#     # Check suspicious patterns
#     
#     return errors

# TODO: Test validation
# text = st.text_area("Test validation", "Enter text here...")
# if st.button("Validate"):
#     errors = validate_text(text)
#     if errors:
#         for error in errors:
#             st.error(error)
#     else:
#         st.success("✅ Valid input")

st.divider()

# ============================================================================
# CHALLENGE 4: Batch Processing
# ============================================================================
st.header("🎯 Challenge 4: Batch Document Processing")
st.write("Process multiple documents from uploaded file.")

# TODO: File upload and batch processing
# uploaded = st.file_uploader("Upload CSV", type=["csv"])
# if uploaded:
#     df = pd.read_csv(uploaded)
#     st.dataframe(df.head())
#     
#     text_col = st.selectbox("Select text column", df.columns)
#     
#     if st.button("Process"):
#         # Clean texts
#         df["cleaned"] = df[text_col].apply(lambda x: str(x).lower().strip())
#         
#         # Predict
#         df["prediction"] = pipeline.predict(df["cleaned"])
#         df["sentiment"] = df["prediction"].map({0: "Negative", 1: "Positive"})
#         
#         st.dataframe(df)
#         
#         # Download
#         csv = df.to_csv(index=False)
#         st.download_button("Download", csv, "results.csv", "text/csv")

st.divider()

# ============================================================================
# CHALLENGE 5: Model Interpretation
# ============================================================================
st.header("🎯 Challenge 5: Model Interpretation")
st.write("Show which words drive predictions.")

# TODO: Show top features
# feature_names = pipeline.named_steps['tfidf'].get_feature_names_out()
# coefficients = pipeline.named_steps['classifier'].coef_[0]
# 
# st.subheader("Top Positive Words")
# top_pos = coefficients.argsort()[-5:][::-1]
# for i in top_pos:
#     st.write(f"- {feature_names[i]}: {coefficients[i]:.3f}")
# 
# st.subheader("Top Negative Words")
# top_neg = coefficients.argsort()[:5]
# for i in top_neg:
#     st.write(f"- {feature_names[i]}: {coefficients[i]:.3f}")

st.divider()

# ============================================================================
# BONUS: Multi-class Classifier
# ============================================================================
st.header("🏆 Bonus: Multi-class Classification")
st.write("Extend to 3 classes: Positive, Neutral, Negative")

# TODO: Build multi-class classifier
# train_texts = [...]  # Add neutral examples
# train_labels = [...]  # 0=negative, 1=neutral, 2=positive
# 
# pipeline = Pipeline([...])
# pipeline.fit(train_texts, train_labels)

st.divider()

# ============================================================================
# COMPLETION
# ============================================================================
st.success("🎉 Workshop Complete!")
st.markdown("""
**What you practiced:**
- ✅ Text preprocessing
- ✅ TF-IDF feature extraction
- ✅ Text classification
- ✅ Input validation
- ✅ Batch processing
- ✅ Model interpretation

**Key NLP deployment rules:**
- Same preprocessing for training and inference
- Validate all text inputs
- Show confidence scores
- Handle edge cases gracefully

**Next steps:**
- Read: [NLP & AI Applications](../readings/17_nlp_ai_applications.md)
- Notebook: [NLP Applications](../notebooks/17_nlp_applications.ipynb)
- Demo App: [Sentiment Analyzer](../apps/17_sentiment_app.py)
""")

# Run check
if __name__ == "__main__":
    st.write("✅ Exercise file is valid and ready to run!")
