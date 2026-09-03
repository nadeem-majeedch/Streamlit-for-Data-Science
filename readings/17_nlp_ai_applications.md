# 17 — NLP & AI Applications

> **📖 Reading · Module 13 · AI/LLM**  
> *Build practical Natural Language Processing applications with Streamlit.*

---

## Learning Objectives

After completing this reading you will be able to:

- Understand NLP workflow: text → preprocessing → features → model → prediction
- Build text classification applications
- Implement sentiment analysis
- Create document processing pipelines
- Visualize NLP results effectively
- Handle text input validation and security
- Use scikit-learn for NLP without external APIs

---

## 1. The NLP Workflow

```
┌─────────────┐    ┌──────────────┐    ┌─────────────┐
│  Text Input │ →  │ Preprocessing│ →  │  Feature    │
│  (User/API) │    │ (Clean/Token)│    │  Extraction │
└─────────────┘    └──────────────┘    └─────────────┘
                                              │
                                              ▼
┌─────────────┐    ┌──────────────┐    ┌─────────────┐
│  Display    │ ←  │  Prediction  │ ←  │    Model    │
│  Results    │    │  (Inference) │    │  (Trained)  │
└─────────────┘    └──────────────┘    └─────────────┘
```

### Key Principle: Same as ML

NLP deployment follows the same pattern as general ML:
1. **Train offline** — Train model on labeled text data
2. **Save artifacts** — Model, vectorizer, metadata
3. **Load in app** — Cache with `@st.cache_resource`
4. **Process input** — Preprocess text exactly like training
5. **Predict** — Generate predictions with confidence

---

## 2. Text Preprocessing

### Basic Cleaning

```python
import re

def clean_text(text):
    """Basic text cleaning."""
    # Lowercase
    text = text.lower()
    
    # Remove HTML tags
    text = re.sub(r'<[^>]+>', '', text)
    
    # Remove URLs
    text = re.sub(r'http\S+|www\S+', '', text)
    
    # Remove special characters (keep letters and spaces)
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text
```

### Tokenization (Optional)

```python
# Using NLTK (optional dependency)
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

def tokenize_text(text):
    """Tokenize and remove stopwords."""
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    return [t for t in tokens if t not in stop_words]

# Using spaCy (optional dependency)
import spacy
nlp = spacy.load("en_core_web_sm")

def spacy_preprocess(text):
    """Advanced preprocessing with spaCy."""
    doc = nlp(text)
    return [token.lemma_ for token in doc if not token.is_stop]
```

---

## 3. Feature Extraction: TF-IDF

### What is TF-IDF?

**Term Frequency-Inverse Document Frequency** converts text to numerical features:

- **TF:** How often a word appears in a document
- **IDF:** How rare a word is across all documents
- **TF-IDF:** High score = frequent in this document, rare overall

```python
from sklearn.feature_extraction.text import TfidfVectorizer

# Training
vectorizer = TfidfVectorizer(max_features=1000, ngram_range=(1, 2))
X_train_tfidf = vectorizer.fit_transform(train_texts)

# Inference (transform only!)
X_test_tfidf = vectorizer.transform(test_texts)
```

### Why TF-IDF Works

- Captures word importance
- Handles different document lengths
- Simple and fast
- No external dependencies

---

## 4. Text Classification Pattern

```python
import streamlit as st
import joblib
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

# --- Training (offline) ---
def train_text_classifier(texts, labels):
    """Train a text classification pipeline."""
    pipeline = Pipeline([
        ('tfidf', TfidfVectorizer(max_features=5000, ngram_range=(1, 2))),
        ('classifier', LogisticRegression(max_iter=1000))
    ])
    pipeline.fit(texts, labels)
    return pipeline

# --- Inference (Streamlit) ---
@st.cache_resource
def load_model():
    """Load trained pipeline."""
    return joblib.load("text_classifier.joblib")

def predict_text(pipeline, text):
    """Predict with confidence."""
    # Preprocess
    cleaned = clean_text(text)
    
    # Predict
    prediction = pipeline.predict([cleaned])[0]
    probabilities = pipeline.predict_proba([cleaned])[0]
    
    return prediction, probabilities
```

---

## 5. Sentiment Analysis

### Using Pre-trained Models

```python
from transformers import pipeline  # Optional dependency

@st.cache_resource
def load_sentiment_model():
    """Load pre-trained sentiment model."""
    return pipeline("sentiment-analysis")

def analyze_sentiment(text):
    """Analyze sentiment of text."""
    model = load_sentiment_model()
    result = model(text[:512])  # Limit to 512 tokens
    return result[0]
```

### Using scikit-learn (No External APIs)

```python
# Train on movie reviews or similar dataset
from sklearn.datasets import load_files
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC

# Example: Simple sentiment classifier
def train_sentiment_model():
    """Train sentiment classifier on sample data."""
    # In practice, use a real dataset like IMDB, Yelp, etc.
    texts = [
        "This movie was great!", "Excellent product!",
        "Terrible experience.", "Worst service ever.",
        "I love this!", "Highly recommend!",
        "Awful quality.", "Complete waste of money."
    ]
    labels = [1, 1, 0, 0, 1, 1, 0, 0]  # 1=positive, 0=negative
    
    vectorizer = TfidfVectorizer(max_features=1000)
    X = vectorizer.fit_transform(texts)
    
    model = LinearSVC()
    model.fit(X, labels)
    
    return model, vectorizer
```

---

## 6. Streamlit UI for NLP

### Text Input

```python
# Single text input
text = st.text_area("Enter text to analyze", height=150)

# File upload
uploaded = st.file_uploader("Upload text file", type=["txt", "csv"])

# Text with examples
text = st.text_area(
    "Enter your review",
    value="This product is amazing!",
    placeholder="Type or paste your text here..."
)
```

### Results Display

```python
# Prediction result
if st.button("Analyze"):
    prediction, confidence = predict(text)
    
    # Main result
    if prediction == "positive":
        st.success(f"😊 Positive Sentiment ({confidence:.1%})")
    else:
        st.error(f"😞 Negative Sentiment ({confidence:.1%})")
    
    # Confidence breakdown
    st.write("**Confidence Scores:**")
    for label, score in zip(["Negative", "Positive"], confidence):
        st.progress(score, text=f"{label}: {score:.1%}")
```

### Visualization

```python
import pandas as pd

# Word frequency
from collections import Counter

def show_word_frequency(text, top_n=10):
    """Display word frequency chart."""
    words = text.lower().split()
    word_counts = Counter(words).most_common(top_n)
    
    df = pd.DataFrame(word_counts, columns=["Word", "Count"])
    st.bar_chart(df.set_index("Word")["Count"])

# Word cloud (optional)
from wordcloud import WordCloud  # Optional dependency

def show_wordcloud(text):
    """Display word cloud."""
    wc = WordCloud(width=800, height=400).generate(text)
    st.image(wc.to_array())
```

---

## 7. Document Processing

### Multiple Documents

```python
import streamlit as st
import pandas as pd

st.header("📄 Batch Document Processing")

uploaded = st.file_uploader("Upload CSV with text column", type=["csv"])

if uploaded:
    df = pd.read_csv(uploaded)
    
    # Select text column
    text_col = st.selectbox("Select text column", df.columns)
    
    if st.button("Process All"):
        # Process each document
        results = []
        for text in df[text_col]:
            pred, conf = predict(text)
            results.append({"prediction": pred, "confidence": conf})
        
        results_df = pd.DataFrame(results)
        df = pd.concat([df, results_df], axis=1)
        
        st.dataframe(df)
        
        # Summary
        st.write(f"**Summary:** {len(df)} documents processed")
        st.write(df["prediction"].value_counts())
```

---

## 8. Input Validation & Security

### Text Validation

```python
def validate_text_input(text, max_length=10000):
    """Validate text input."""
    errors = []
    
    if not text or not text.strip():
        errors.append("Text cannot be empty")
    
    if len(text) > max_length:
        errors.append(f"Text exceeds maximum length ({max_length} characters)")
    
    # Check for suspicious patterns
    suspicious = ['<script>', 'javascript:', 'onerror=']
    for pattern in suspicious:
        if pattern.lower() in text.lower():
            errors.append("Text contains suspicious content")
    
    return errors
```

### Security Considerations

1. **Sanitize input** — Remove HTML, scripts, dangerous patterns
2. **Limit length** — Prevent abuse with very long texts
3. **Rate limiting** — Consider limiting requests per user
4. **No eval/exec** — Never execute user-provided code
5. **Output encoding** — Encode outputs to prevent XSS

---

## 9. Learning vs Production

### Learning Environment

```python
# Simple classification — fine for learning
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texts)
model = MultinomialNB()
model.fit(X, labels)
```

### Production Considerations

```python
# Production-ready pattern
import joblib
from sklearn.pipeline import Pipeline

@st.cache_resource(ttl=3600)
def load_nlp_model():
    """Load with validation and error handling."""
    try:
        pipeline = joblib.load("nlp_pipeline.joblib")
        # Validate model
        if not hasattr(pipeline, 'predict'):
            raise ValueError("Invalid model")
        return pipeline
    except Exception as e:
        st.error(f"Failed to load model: {e}")
        return None

def safe_predict(pipeline, text):
    """Predict with error handling."""
    try:
        cleaned = clean_text(text)
        prediction = pipeline.predict([cleaned])[0]
        probabilities = pipeline.predict_proba([cleaned])[0]
        return prediction, probabilities, None
    except Exception as e:
        return None, None, str(e)
```

---

## 10. Model Interpretation

### Top Features

```python
def show_top_features(pipeline, class_names, top_n=10):
    """Display top features for each class."""
    feature_names = pipeline.named_steps['tfidf'].get_feature_names_out()
    coefficients = pipeline.named_steps['classifier'].coef_
    
    for i, class_name in enumerate(class_names):
        st.write(f"**{class_name}:**")
        top_indices = coefficients[i].argsort()[-top_n:][::-1]
        top_features = [(feature_names[j], coefficients[i][j]) for j in top_indices]
        
        for feat, coef in top_features:
            st.write(f"  - {feat}: {coef:.3f}")
```

---

## Key Takeaways

- **NLP workflow:** Text → Preprocess → Vectorize → Predict → Display
- **TF-IDF** is a simple, effective feature extraction method
- **Same ML patterns** apply: train offline, cache models, validate inputs
- **Preprocessing consistency** is critical (same cleaning as training)
- **Input validation** prevents abuse and errors
- **Confidence scores** help users understand predictions
- **Optional dependencies** (spaCy, NLTK, transformers) enhance capabilities

---

## Further Reading

- [Scikit-learn Text Features](https://scikit-learn.org/stable/modules/feature_extraction.html#text-feature-extraction)
- [NLTK Documentation](https://www.nltk.org/)
- [spaCy Documentation](https://spacy.io/)

---

## Related Materials

- 📓 Notebook: [17 — NLP with Streamlit](../notebooks/17_nlp_applications.ipynb)
- ✏️ Exercise: [17 — NLP Workshop](../exercises/17_nlp_workshop.py)
- 🖥️ Demo App: [17 — Sentiment Analyzer](../apps/17_sentiment_app.py)
- 📝 Quiz: [13 — NLP & AI](../quizzes/13_nlp_ai.md)
- 🚀 Project: [P07 — RAG Document Chat](../projects/P07_rag_document_chat.md)
