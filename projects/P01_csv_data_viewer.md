# P01 — CSV Data Viewer

> **🚀 Project · Beginner · M01–M02**
> *Your first Streamlit app: upload, view, and explore CSV data.*
> Difficulty: ★☆☆☆☆ · Duration: 1 week · Weight: Part of 15% project grade

---

## Problem Statement

A small business owner has sales data in CSV files but no technical skills. Build a simple Streamlit app that lets them upload a CSV, preview the data, and see basic statistics — no coding required on their part.

---

## Learning Objectives

By completing this project you will be able to:

1. Create and run a Streamlit application from scratch (CLO1)
2. Use `st.file_uploader` to accept CSV files (CLO2)
3. Display data with `st.dataframe()` and `st.table()` (CLO2)
4. Compute and display basic statistics with `st.metric()` (CLO2)
5. Handle errors gracefully when files are missing or malformed (CLO10)

---

## Prerequisites

- Completed Modules 01–02
- Python basics, Pandas DataFrame basics
- `pip install streamlit pandas`

---

## Dataset

Students must generate a sample dataset OR use one provided:

```python
import pandas as pd
import numpy as np

np.random.seed(42)
df = pd.DataFrame({
    "Product": np.random.choice(["Widget A", "Widget B", "Widget C"], 100),
    "Region": np.random.choice(["North", "South", "East", "West"], 100),
    "Sales": np.random.randint(50, 500, 100),
    "Quantity": np.random.randint(1, 20, 100),
    "Rating": np.random.uniform(1, 5, 100).round(1),
})
df.to_csv("sample_sales.csv", index=False)
```

---

## Functional Requirements

| # | Requirement | Marks |
|---|-------------|-------|
| F1 | `st.file_uploader` accepts CSV files | 5 |
| F2 | Display file name, size, and row/column count after upload | 5 |
| F3 | Show first 10 rows with `st.dataframe()` | 5 |
| F4 | Display column names and data types | 5 |
| F5 | Show 3 summary statistics (total rows, mean sales, unique products) | 5 |
| F6 | Handle empty files and non-CSV uploads with error messages | 5 |
| F7 | Show a helpful message when no file is uploaded | 5 |

**Total: 35 marks**

---

## UI Requirements

1. Page title: "CSV Data Viewer"
2. Sidebar with app description
3. Main area: upload → preview → statistics
4. Clear visual separation between sections (`st.divider()`)
5. Professional appearance with consistent styling

---

## Architecture

```
csv_viewer/
├── app.py              # Main application (single file OK for beginner)
├── requirements.txt    # streamlit, pandas
├── README.md           # Documentation
└── sample_sales.csv    # Sample data for testing
```

---

## Milestones

| Day | Milestone | Deliverable |
|-----|-----------|-------------|
| 1 | App setup | File uploader working, data displays |
| 2 | Statistics | Summary metrics displayed |
| 3 | Error handling | Graceful failure for edge cases |
| 4 | Polish & submit | README, screenshots, final testing |

---

## Testing Requirements

- App runs without errors: `streamlit run app.py`
- Upload a valid CSV → data displays correctly
- Upload an empty CSV → shows warning, no crash
- Upload a non-CSV file → shows error message
- No file uploaded → shows helpful instructions

---

## Evaluation Criteria

| Criteria | Marks | Description |
|----------|-------|-------------|
| Functionality | 20 | All 7 requirements met |
| Error handling | 5 | Graceful failure for edge cases |
| Code quality | 5 | Clean code, comments, structure |
| Documentation | 5 | README with description and screenshots |
| **Total** | **35** | |

---

## Security Requirements

- No hardcoded file paths
- No `exec()` or `eval()` calls
- Validate file type before processing

---

## Deliverables

1. `app.py` — Running Streamlit application
2. `requirements.txt` — Dependencies
3. `README.md` — Description, how to run, screenshots
4. `sample_sales.csv` — Test data

---

## Extensions (Bonus)

- Add a download button for the displayed data
- Allow multiple file upload
- Add basic chart (bar chart of a column)
- Store upload history in session state

---

## Related Materials

- 📖 Reading: [Streamlit Introduction](../readings/01_streamlit_introduction.md)
- 📖 Reading: [First Streamlit App](../readings/02_first_streamlit_app.md)
- 📓 Notebook: [01 — Introduction](../notebooks/01_Streamlit_Introduction.ipynb)
- ✏️ Exercise: [01 — Hello Streamlit](../exercises/01_hello_streamlit.py)
- 🖥️ Demo: [01 — Introduction](../apps/01_introduction_demo.py)
