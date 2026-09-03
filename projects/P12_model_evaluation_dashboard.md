# P12 — Model Evaluation Dashboard

> **🚀 Project · Advanced · M10–M12**
> *Build a dashboard for comparing and evaluating multiple ML models.*
> Difficulty: ★★★★☆ · Duration: 2 weeks · Weight: Part of 15% project grade

---

## Problem Statement

A data science team has trained several models and needs a dashboard to compare their performance side-by-side. Build an app that loads pre-trained models, evaluates them on test data, and displays comprehensive metrics, confusion matrices, and ROC curves.

---

## Learning Objectives

1. Load and compare multiple trained models (CLO8)
2. Implement comprehensive model evaluation (CLO5)
3. Create advanced visualizations (confusion matrix, ROC, PR curves) (CLO3)
4. Design a model comparison interface (CLO6)
5. Handle model versioning concepts (CLO8)

---

## Prerequisites

- Completed Modules 10–12
- Scikit-learn metrics (accuracy, precision, recall, F1, confusion_matrix)
- Plotly for interactive charts
- joblib for model loading

---

## Functional Requirements

| # | Requirement | Marks |
|---|-------------|-------|
| F1 | Load 3+ pre-trained models from files | 5 |
| F2 | Model selector: choose which models to compare | 5 |
| F3 | Metrics comparison table: accuracy, precision, recall, F1, AUC | 10 |
| F4 | Confusion matrix for selected model (Plotly heatmap) | 8 |
| F5 | ROC curve comparison (multiple models on same plot) | 8 |
| F6 | Precision-Recall curve | 6 |
| F7 | Feature importance comparison across models | 6 |
| F8 | Model training time and size info | 4 |
| F9 | Download comparison report as CSV | 4 |
| F10 | Recommendation: highlight best model per metric | 4 |

**Total: 60 marks**

---

## Architecture

```
model_evaluator/
├── app.py
├── evaluation.py       # Metrics computation functions
├── visualizations.py   # Chart creation functions
├── models/             # Pre-trained model files
├── requirements.txt
└── README.md
```

---

## Evaluation Criteria

| Criteria | Marks |
|----------|-------|
| Evaluation comprehensiveness | 25 |
| Visualization quality | 15 |
| Comparison interface | 10 |
| Code quality | 5 |
| Documentation | 5 |
| **Total** | **60** |

---

## Extensions

- Add statistical significance tests between models
- Add learning curves
- Add model fairness metrics
- Add interactive threshold adjustment

---

## Related Materials

- 📖 Reading: [ML Streamlit](../readings/15_machine_learning_streamlit.md)
- 📓 Notebook: [15 — ML](../notebooks/15_ml_streamlit.ipynb)
- ✏️ Exercise: [15 — ML Workshop](../exercises/15_ml_workshop.py)
