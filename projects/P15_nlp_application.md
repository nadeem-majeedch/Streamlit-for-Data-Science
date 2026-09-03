# P15 — NLP Application: Text Analysis Dashboard

> **🚀 Project · AI/LLM · M13**
> *Build a text analysis application with sentiment analysis and text classification.*
> Difficulty: ★★★★☆ · Duration: 2 weeks · Weight: Part of 15% project grade

---

## Problem Statement

A customer support team receives thousands of reviews daily. Build a Streamlit app that analyzes text sentiment, classifies reviews by topic, extracts key phrases, and provides batch processing capabilities.

---

## Learning Objectives

1. Implement text preprocessing pipelines (CLO9)
2. Build text classification models (CLO9)
3. Create NLP-specific visualizations (CLO3)
4. Handle batch text processing (CLO5)
5. Validate and sanitize text inputs (CLO10)

---

## Prerequisites

- Completed Module 13
- TF-IDF vectorization
- Text preprocessing (lowercase, remove stopwords, stem)
- Scikit-learn classifiers

---

## Functional Requirements

| # | Requirement | Marks |
|---|-------------|-------|
| F1 | Text input: text_area for single text analysis | 4 |
| F2 | Sentiment analysis: show positive/negative/neutral with confidence | 8 |
| F3 | Text classification: assign topic/category label | 8 |
| F4 | Text preprocessing display: show cleaned text | 5 |
| F5 | Key phrase extraction: show top N important words | 6 |
| F6 | Batch processing: upload CSV with text column, process all rows | 8 |
| F7 | Results visualization: sentiment distribution, topic breakdown | 8 |
| F8 | Download batch results | 4 |
| F9 | Input validation: check for empty text, length limits | 5 |
| F10 | Model info: show model type, accuracy, feature count | 4 |

**Total: 60 marks**

---

## Architecture

```
nlp_analyzer/
├── app.py
├── text_processing.py  # Preprocessing functions
├── models.py           # Model training and loading
├── visualizations.py   # NLP-specific charts
├── models/
├── requirements.txt
└── README.md
```

---

## Evaluation Criteria

| Criteria | Marks |
|----------|-------|
| NLP pipeline quality | 25 |
| Visualization | 15 |
| Batch processing | 10 |
| Input validation | 5 |
| Documentation | 5 |
| **Total** | **60** |

---

## Extensions

- Add word cloud visualization
- Add named entity recognition
- Add text summarization
- Add language detection

---

## Related Materials

- 📖 Reading: [NLP Applications](../readings/17_nlp_ai_applications.md)
- 📓 Notebook: [17 — NLP](../notebooks/17_nlp_applications.ipynb)
- ✏️ Exercise: [17 — NLP](../exercises/17_nlp_workshop.py)
- 🖥️ Demo: [17 — Sentiment](../apps/17_sentiment_app.py)
