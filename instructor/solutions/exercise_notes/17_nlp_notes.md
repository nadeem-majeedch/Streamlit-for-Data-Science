# Exercise 17 — NLP Workshop: Solution Notes

> **👩‍🏫 Instructor Reference**
> *Expected approach, key code, and grading guidance.*

---

## Challenge 1: Text Preprocessing

### Expected Approach
Create a `clean_text()` function that normalizes text for ML: lowercase, remove HTML/URLs/special chars, strip whitespace.

### Key Code
```python
import re

def clean_text(text):
    """Clean text for NLP."""
    text = text.lower()                    # Lowercase
    text = re.sub(r"<[^>]+>", "", text)    # Remove HTML tags
    text = re.sub(r"http\S+|www\S+", "", text)  # Remove URLs
    text = re.sub(r"[^a-zA-Z\s]", "", text)     # Remove special chars
    text = re.sub(r"\s+", " ", text).strip()      # Remove extra whitespace
    return text

# Test
sample_texts = [
    "This is GREAT!!! Visit https://example.com",
    "<p>Hello World</p> This is a test.",
    "LOVE this product!!! Best purchase ever!!!"
]
for text in sample_texts:
    st.write(f"**Original:** {text}")
    st.write(f"**Cleaned:** {clean_text(text)}")
```

### Common Mistakes
- Forgetting to lowercase
- Not removing HTML tags (breaks TF-IDF)
- Removing ALL non-alpha characters (should keep spaces)
- Using `re.sub` without raw strings

### Grading Notes (20 marks)
- Full marks: All 5 cleaning steps work correctly
- 14 marks: 3-4 steps work
- 7 marks: 1-2 steps work

---

## Challenge 2: Single Text Prediction

### Key Code
```python
text = st.text_area("Enter text to analyze", "This product is amazing!")

if st.button("Predict"):
    if not text.strip():
        st.error("Please enter some text")
    else:
        cleaned = clean_text(text)
        prediction = pipeline.predict([cleaned])[0]
        probabilities = pipeline.predict_proba([cleaned])[0]

        label = "Positive 😊" if prediction == 1 else "Negative 😞"
        st.success(f"Sentiment: **{label}**")
        st.write(f"Confidence: **{probabilities[prediction]:.1%}**")
```

### Common Mistakes
- Not applying `clean_text()` before prediction (must match training)
- Using raw text instead of preprocessed text
- Forgetting to show confidence/probabilities

---

## Challenge 3: Batch Processing

### Key Code
```python
uploaded = st.file_uploader("Upload text file (CSV with 'text' column)", type=["csv"])

if uploaded:
    df = pd.read_csv(uploaded)
    if "text" not in df.columns:
        st.error("CSV must have a 'text' column")
    else:
        df["cleaned"] = df["text"].apply(clean_text)
        df["sentiment"] = pipeline.predict(df["cleaned"])
        df["confidence"] = pipeline.predict_proba(df["cleaned"]).max(axis=1)
        df["label"] = df["sentiment"].map({1: "Positive", 0: "Negative"})

        st.dataframe(df[["text", "label", "confidence"]], use_container_width=True)

        # Summary
        st.write(f"Positive: {(df['sentiment'] == 1).sum()} · Negative: {(df['sentiment'] == 0).sum()}")

        csv = df.to_csv(index=False)
        st.download_button("Download Results", csv, "sentiment_results.csv")
```

---

## Challenge 4: Model Interpretation

### Key Code
```python
# Get feature names and coefficients from the trained pipeline
tfidf = pipeline.named_steps["tfidf"]
classifier = pipeline.named_steps["classifier"]
feature_names = tfidf.get_feature_names_out()
coefficients = classifier.coef_[0]

# Top positive and negative features
top_n = 10
top_positive = pd.DataFrame({
    "Feature": feature_names[coefficients.argsort()[-top_n:]],
    "Coefficient": coefficients[coefficients.argsort()[-top_n:]],
}).sort_values("Coefficient")

st.subheader("Top Features Driving Predictions")
fig_col1, fig_col2 = st.columns(2)
with fig_col1:
    st.write("**Positive indicators:**")
    st.dataframe(top_positive.tail(top_n), hide_index=True)
with fig_col2:
    st.write("**Negative indicators:**")
    st.dataframe(top_positive.head(top_n), hide_index=True)
```

### Grading Notes (25 marks)
- Full marks: All 4 challenges work, preprocessing consistent, batch processing works
- 18 marks: Single and batch work, interpretation partial
- 10 marks: Basic prediction works

---

## Security Notes
- Input validation: check for empty text, excessive length
- Sanitize text before display (prevent XSS if rendering user text)
- File upload validation: check CSV has "text" column
