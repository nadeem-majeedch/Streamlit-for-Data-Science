# P13 — Batch Prediction Application

> **🚀 Project · Advanced · M10–M12**
> *Build a production-style batch prediction pipeline with Streamlit.*
> Difficulty: ★★★★☆ · Duration: 2 weeks · Weight: Part of 15% project grade

---

## Problem Statement

An insurance company needs to process thousands of policy applications through their risk model daily. Build a Streamlit app that accepts batch CSV uploads, runs predictions efficiently, validates results, and generates summary reports.

---

## Learning Objectives

1. Implement efficient batch processing (CLO5)
2. Handle large file uploads with validation (CLO2)
3. Create processing pipelines with status tracking (CLO6)
4. Generate summary reports from prediction results (CLO3)
5. Implement proper error handling for production use (CLO10)

---

## Prerequisites

- Completed Modules 10–12
- Pandas batch operations
- Joblib for model loading
- File upload with validation

---

## Functional Requirements

| # | Requirement | Marks |
|---|-------------|-------|
| F1 | File upload with size limit and type validation | 5 |
| F2 | Column validation: check expected features exist | 5 |
| F3 | Data validation: check for nulls, outliers, invalid values | 8 |
| F4 | Batch prediction with progress indicator | 8 |
| F5 | Results display: predictions + confidence scores | 6 |
| F6 | Summary report: distribution of predictions, confidence stats | 8 |
| F7 | Filter results by prediction class or confidence threshold | 6 |
| F8 | Download full results as CSV | 4 |
| F9 | Download summary report | 4 |
| F10 | Error handling: skip bad rows, report errors, continue processing | 6 |
| F11 | Session state for processing history | 4 |

**Total: 64 marks**

---

## Architecture

```
batch_predictor/
├── app.py
├── predictor.py        # Prediction pipeline
├── validator.py        # Input validation
├── reporter.py         # Summary report generation
├── models/
├── requirements.txt
└── README.md
```

---

## Evaluation Criteria

| Criteria | Marks |
|----------|-------|
| Batch processing pipeline | 25 |
| Validation and error handling | 15 |
| Reporting and summaries | 10 |
| Code quality | 7 |
| Documentation | 7 |
| **Total** | **64** |

---

## Extensions

- Add async processing for large files
- Add prediction caching (don't reprocess same file)
- Add email notification when processing completes
- Add API endpoint for programmatic access

---

## Related Materials

- 📖 Reading: [ML Streamlit](../readings/15_machine_learning_streamlit.md)
- 📓 Notebook: [15 — ML](../notebooks/15_ml_streamlit.ipynb)
- ✏️ Exercise: [15 — ML Workshop](../exercises/15_ml_workshop.py)
- 🖥️ Demo: [15 — Classification](../apps/15_classification_app.py)
