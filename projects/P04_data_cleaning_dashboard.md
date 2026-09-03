# P04 — Data Cleaning Dashboard

> **🚀 Project · Intermediate · M04–M06**
> *Build an interactive data cleaning and preprocessing tool.*
> Difficulty: ★★☆☆☆ · Duration: 1.5 weeks · Weight: Part of 15% project grade

---

## Problem Statement

Data scientists spend 60–80% of their time cleaning data. Build a Streamlit app that automates common cleaning tasks: handling missing values, removing duplicates, standardizing columns, and exporting clean data. The app should let users choose cleaning options interactively and see before/after comparisons.

---

## Learning Objectives

1. Handle file uploads with validation (CLO2)
2. Use session state to persist cleaning choices (CLO4)
3. Implement data transformation functions (CLO2)
4. Display before/after comparisons (CLO3)
5. Provide data export functionality (CLO2)

---

## Prerequisites

- Completed Modules 04–06
- Pandas: dropna, fillna, drop_duplicates, rename
- Session state basics

---

## Dataset

Generate a messy dataset for testing:

```python
import pandas as pd
import numpy as np

np.random.seed(42)
n = 200
df = pd.DataFrame({
    "Name": np.random.choice(["Alice", "Bob", "Carol", "Dave", None], n),
    "Age": np.random.choice([25, 30, None, -5, 200, 35], n),
    "Salary": np.random.uniform(30000, 120000, n).round(2),
    "Department": np.random.choice(["eng", "ENG", "Sales", "sales", "HR", "  HR  "], n),
    "Start_Date": np.random.choice(["2024-01-15", "invalid-date", "", None], n),
    "Email": [f"user{i}@example.com" if np.random.random() > 0.1 else "invalid" for i in range(n)],
})
# Add some exact duplicates
dups = df.sample(20, random_state=42)
df = pd.concat([df, dups], ignore_index=True)
df.to_csv("messy_data.csv", index=False)
```

---

## Functional Requirements

| # | Requirement | Marks |
|---|-------------|-------|
| F1 | Upload CSV with file info display (name, size, rows, columns) | 5 |
| F2 | Data quality report: null counts, duplicates, column types | 8 |
| F3 | Cleaning options with checkboxes: remove duplicates, standardize names, drop high-null columns, fill numeric nulls | 10 |
| F4 | Before/after comparison: row count, null count, column count changes | 8 |
| F5 | Cleaning summary showing what was changed | 5 |
| F6 | Download cleaned data as CSV | 5 |
| F7 | Session state preserves cleaning choices across reruns | 5 |
| F8 | Error handling for empty files and bad uploads | 4 |

**Total: 50 marks**

---

## Architecture

```
data_cleaner/
├── app.py              # Main app with UI
├── cleaning.py         # Pure cleaning functions (no st.* calls)
├── requirements.txt
└── README.md
```

---

## Milestones

| Day | Milestone |
|-----|-----------|
| 1–2 | Upload + quality report working |
| 3–4 | Cleaning options + before/after comparison |
| 5–6 | Download + session state + error handling |
| 7 | Polish + README + screenshots |

---

## Evaluation Criteria

| Criteria | Marks |
|----------|-------|
| Functionality | 30 |
| Before/after comparison | 10 |
| Code quality (separated functions) | 5 |
| Error handling | 5 |
| **Total** | **50** |

---

## Extensions

- Add column renaming interface
- Add data type conversion options
- Add outlier detection and removal
- Show a data profile report (like pandas-profiling)

---

## Related Materials

- 📖 Reading: [File Upload & Processing](../readings/09_file_upload_and_processing.md)
- 📓 Notebook: [09 — File Upload](../notebooks/09_file_upload_and_processing.ipynb)
- ✏️ Exercise: [09 — File Upload](../exercises/09_file_upload_workshop.py)
