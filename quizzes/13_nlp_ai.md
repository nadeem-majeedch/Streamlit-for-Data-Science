# Quiz 13: NLP & AI Applications

> **📝 Quiz · Module 13 · AI/LLM**  
> *Test your understanding of NLP applications with Streamlit.*

---

## Multiple Choice

### Q1. What is the correct NLP deployment workflow?

a) Input → Model → Preprocess → Display  
b) Input → Preprocess → Vectorize → Model → Display  
c) Input → Vectorize → Preprocess → Display  
d) Input → Model → Display

---

### Q2. What does TF-IDF measure?

a) Text length  
b) Word importance based on frequency and rarity  
c) Sentiment polarity  
d) Document similarity

---

### Q3. Why must preprocessing at inference match training?

a) To make predictions faster  
b) To ensure the model receives expected input format  
c) To reduce memory usage  
d) It's not necessary

---

### Q4. What is the correct way to use a fitted vectorizer at inference?

```python
# Option A
X = vectorizer.fit_transform([text])

# Option B
X = vectorizer.transform([text])
```

---

### Q5. How should you handle empty text input?

a) Predict anyway with default class  
b) Show error message and don't predict  
c) Fill with dummy text silently  
d) Skip validation

---

### Q6. What is a sklearn Pipeline?

a) A sequence of data transformations  
b) A deployment tool  
c) A visualization library  
d) A database connector

---

### Q7. Why use `@st.cache_resource` for the NLP model?

a) To save memory  
b) To load the model once and reuse it  
c) To make predictions faster  
d) All of the above

---

### Q8. What is the purpose of `max_features` in TfidfVectorizer?

a) Maximum text length  
b) Limit vocabulary size  
c) Maximum prediction time  
d) Number of classes

---

### Q9. How do you display prediction confidence for classification?

a) Show only the predicted class  
b) Show class probabilities as progress bars  
c) Show raw model output  
d) Don't show confidence

---

### Q10. What is a common security concern with text input?

a) Text is too long  
b) User might enter HTML/scripts  
c) Text has too many words  
d) Text contains numbers

---

### Q11. Why use `predict_proba()` instead of just `predict()`?

a) It's faster  
b) It gives probability scores for each class  
c) It's required by Streamlit  
d) It handles missing values

---

### Q12. What is batch processing in NLP?

a) Processing one document at a time  
b) Processing multiple documents from a file  
c) Training multiple models  
d) Running predictions overnight

---

## Short Answer

### Q13. Explain the complete NLP deployment pipeline for a Streamlit sentiment analysis app. What are the key steps?

---

### Q14. A developer's sentiment classifier works well in testing but gives random predictions in production. What is the most likely cause and how do you fix it?

---

### Q15. Describe three best practices for building NLP applications with Streamlit.

---

## Code Completion

### Q16. Complete the text preprocessing function:

```python
import re

def clean_text(text):
    """Clean text for NLP processing."""
    # TODO: Lowercase
    # TODO: Remove HTML tags
    # TODO: Remove URLs
    # TODO: Remove special characters (keep letters and spaces)
    # TODO: Remove extra whitespace
    
    return cleaned_text
```

---

### Q17. Complete the batch prediction function:

```python
import streamlit as st
import pandas as pd

def batch_predict(pipeline, df, text_col):
    """
    Process multiple documents.
    
    Args:
        pipeline: Trained sklearn pipeline
        df: Input DataFrame
        text_col: Name of text column
    
    Returns:
        DataFrame with predictions added
    """
    # TODO: Validate text column exists
    # TODO: Handle missing values
    # TODO: Preprocess texts (same as training!)
    # TODO: Make predictions
    # TODO: Add predictions to DataFrame
    
    return df
```

---

## Answer Key

### Multiple Choice

1. **B** — Input → Preprocess → Vectorize → Model → Display
2. **B** — TF-IDF measures word importance based on frequency and rarity
3. **B** — Model expects specific input format from training
4. **B** — Use `transform()` only, not `fit_transform()`
5. **B** — Show error and don't predict on invalid input
6. **A** — Pipeline chains transformations and model together
7. **D** — Caching saves memory, loads once, and speeds up predictions
8. **B** — Limits vocabulary size to most important features
9. **B** — Show probabilities as progress bars or percentages
10. **B** — Users might enter malicious HTML/scripts
11. **B** — `predict_proba()` returns probability scores
12. **B** — Batch processing handles multiple documents from a file

### Short Answer

**Q13.** NLP Deployment Pipeline:
1. **Text Input** — User enters text or uploads file
2. **Validation** — Check for empty text, length, suspicious content
3. **Preprocessing** — Clean text (lowercase, remove HTML, etc.)
4. **Vectorization** — Convert text to TF-IDF features
5. **Prediction** — Use trained model to predict class
6. **Confidence** — Show probability scores
7. **Display** — Show results with visualization

**Q14.** Most likely cause: **Preprocessing mismatch**. The text isn't being cleaned the same way as training.

**Fix:** Use the exact same `clean_text()` function for both training and inference. Include it in the pipeline or save it alongside the model.

**Q15.** Best practices:
1. **Preprocessing consistency** — Same cleaning for training and inference
2. **Input validation** — Check empty text, length, suspicious content
3. **Confidence display** — Show probabilities, not just predictions
4. **Caching** — Use `@st.cache_resource` for model loading
5. **Error handling** — Graceful failure for edge cases

### Code Completion

**Q16.**
```python
def clean_text(text):
    """Clean text for NLP processing."""
    # Lowercase
    text = text.lower()
    
    # Remove HTML tags
    text = re.sub(r'<[^>]+>', '', text)
    
    # Remove URLs
    text = re.sub(r'http\S+|www\S+', '', text)
    
    # Remove special characters
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text
```

**Q17.**
```python
def batch_predict(pipeline, df, text_col):
    """Process multiple documents."""
    # Validate text column exists
    if text_col not in df.columns:
        raise ValueError(f"Column '{text_col}' not found")
    
    # Handle missing values
    df[text_col] = df[text_col].fillna("").astype(str)
    
    # Preprocess (same as training!)
    df["cleaned"] = df[text_col].apply(clean_text)
    
    # Make predictions
    predictions = pipeline.predict(df["cleaned"])
    probabilities = pipeline.predict_proba(df["cleaned"])
    
    # Add to DataFrame
    df["prediction"] = predictions
    df["confidence"] = probabilities.max(axis=1)
    
    return df
```

---

## Related Materials

- 📖 Reading: [17 — NLP & AI Applications](../readings/17_nlp_ai_applications.md)
- 📓 Notebook: [17 — NLP Applications](../notebooks/17_nlp_applications.ipynb)
- ✏️ Exercise: [17 — NLP Workshop](../exercises/17_nlp_workshop.py)
- 🖥️ Demo App: [17 — Sentiment Analyzer](../apps/17_sentiment_app.py)
- 🚀 Project: [P07 — RAG Document Chat](../projects/P07_rag_document_chat.md)
