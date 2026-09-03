# Assignment 02 — Data Explorer with File Upload

> **📋 Assignment · Level 2 (Intermediate) — Modules 04–06**
> *Build an interactive data exploration tool with file upload and processing.*

---

## Course Information

| Field | Detail |
|-------|--------|
| **Course** | Streamlit for Data Science |
| **Assignment** | A02 — Data Explorer with File Upload |
| **Due Date** | End of Week 6 |
| **Weight** | 4% of course grade |
| **Difficulty** | ★★☆☆☆ Intermediate |
| **Collaboration** | Individual |

---

## Learning Outcomes

After completing this assignment you will be able to:

1. **LO1** — Build interactive data filtering and visualization dashboards (Apply)
2. **LO2** — Handle file uploads with validation and error handling (Apply)
3. **LO3** — Use session state for persistent user interactions (Apply)
4. **LO4** — Select and apply appropriate chart types for different data (Analyze)
5. **LO5** — Process and transform uploaded data with Pandas (Apply)

---

## Prerequisites

- Completed Modules 04, 05, 06
- Pandas DataFrames, basic data analysis
- Matplotlib or Plotly basics
- Understanding of session state and forms

---

## Overview

Build a **Data Explorer** — a Streamlit application that lets users upload a
CSV or Excel file and interactively explore it through filters, charts, and
statistics. The app must also work with a built-in sample dataset when no
file is uploaded.

This assignment tests your ability to combine widgets, data display, file
handling, and visualization into a cohesive application.

---

## Tasks

### Task 1: Data Loading (15 marks)

| Requirement | Marks |
|-------------|-------|
| Implement `st.file_uploader` accepting CSV and Excel files | 3 |
| Validate file type and show clear error for invalid uploads | 2 |
| Validate file content (check for empty files, encoding errors) | 2 |
| Display file info: name, size, number of rows/columns after upload | 2 |
| Provide a built-in sample dataset (e.g., generate with NumPy) | 3 |
| Use the sample dataset when no file is uploaded | 2 |
| Handle large files gracefully (show warning if > 50MB) | 1 |

### Task 2: Interactive Filters (20 marks)

Build a sidebar with dynamic filters based on the loaded data:

| Requirement | Marks |
|-------------|-------|
| Auto-detect numeric vs categorical columns | 3 |
| Sidebar selectbox for categorical column filtering | 3 |
| Sidebar slider/range for numeric column filtering | 3 |
| Text search input for string columns | 2 |
| Filters update the displayed data in real time | 3 |
| Show active filter count: "Showing X of Y rows" | 2 |
| "Reset filters" button using session state | 2 |
| Filters are stored in session state so they persist | 2 |

### Task 3: Visualization (25 marks)

Create at least 3 different visualizations of the filtered data:

| Requirement | Marks |
|-------------|-------|
| Bar chart showing distribution of a categorical column | 4 |
| Histogram or density plot of a numeric column | 4 |
| Scatter plot of two numeric columns with color encoding | 4 |
| Line chart showing a time-series or trend | 3 |
| At least one Plotly chart with `use_container_width=True` | 3 |
| Chart titles and labels are descriptive | 2 |
| Charts update when filters change | 3 |
| Use `st.tabs()` to organize chart sections | 2 |

### Task 4: Statistics & Summary (15 marks)

| Requirement | Marks |
|-------------|-------|
| `st.metric()` KPIs: total rows, numeric columns count, mean/median | 4 |
| `st.dataframe()` showing `describe()` statistics | 3 |
| Correlation matrix display (for numeric columns) | 3 |
| Value counts for a selected categorical column | 2 |
| Missing values report (count and percentage per column) | 3 |

### Task 5: Data Export (10 marks)

| Requirement | Marks |
|-------------|-------|
| `st.download_button()` to download filtered data as CSV | 3 |
| Download button includes filtered state, not raw data | 2 |
| Filename includes a timestamp for versioning | 2 |
| Download button only appears when data is filtered | 1 |
| Export includes a summary sheet/text alongside data | 2 |

### Task 6: Session State & UX (10 marks)

| Requirement | Marks |
|-------------|-------|
| Filter selections persist across reruns via session state | 3 |
| App remembers the last uploaded file in the session | 2 |
| Loading spinner shown during data processing | 2 |
| Clear visual feedback when no data matches filters | 1 |
| Overall UX is intuitive (labels, descriptions, flow) | 2 |

### Task 7: Code Quality & Documentation (5 marks)

| Requirement | Marks |
|-------------|-------|
| Code organized into functions (not one giant script) | 2 |
| `st.set_page_config()` as first Streamlit call | 1 |
| README with screenshot and feature list | 2 |

**Total: 100 marks**

---

## Deliverables

1. **`A02_data_explorer.py`** — Your Streamlit application
2. **`README.md`** — Documentation with screenshots
3. **Screenshot(s)** of the running app

### Submission

```
assignments/A02/
├── A02_data_explorer.py
├── README.md
└── screenshots/
    ├── explorer_1_filters.png
    ├── explorer_2_charts.png
    └── explorer_3_stats.png
```

---

## Starter Template

```python
import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Data Explorer", layout="wide")
st.title("📊 Data Explorer")

# TODO: Add file uploader
# TODO: Add sample data fallback
# TODO: Build sidebar filters
# TODO: Create visualizations
# TODO: Show statistics
# TODO: Add download button
```

---

## Grading Rubric Summary

| Category | Marks | Bloom's Level |
|----------|-------|---------------|
| Data Loading | 15 | Apply |
| Interactive Filters | 20 | Apply, Analyze |
| Visualization | 25 | Apply, Analyze |
| Statistics & Summary | 15 | Analyze |
| Data Export | 10 | Apply |
| Session State & UX | 10 | Apply |
| Code Quality | 5 | Apply |
| **Total** | **100** | |

---

## Sample Datasets to Use

```python
# Option 1: Iris-like dataset
from sklearn.datasets import load_iris
iris = load_iris(as_frame=True).frame

# Option 2: Generated sales data
np.random.seed(42)
n = 500
sales = pd.DataFrame({
    "date": pd.date_range("2024-01-01", periods=n, freq="D"),
    "category": np.random.choice(["Electronics", "Clothing", "Food", "Books"], n),
    "region": np.random.choice(["North", "South", "East", "West"], n),
    "revenue": np.random.uniform(50, 500, n).round(2),
    "units": np.random.randint(1, 20, n),
    "rating": np.random.uniform(1, 5, n).round(1),
})
```

---

## Common Mistakes to Avoid

1. **❌ Hardcoded column names** — Filters must work with any uploaded data
2. **❌ No file validation** — Always check file type and content
3. **❌ Charts that don't update** — Use filtered data, not raw data
4. **❌ Missing session state** — Filter selections reset on every rerun
5. **❌ No download functionality** — Assignment requires export feature

---

## Related Materials

- 📖 Reading: [Data Display](../readings/07_data_display_dataframes.md)
- 📖 Reading: [Visualization](../readings/08_visualization_matplotlib_plotly.md)
- 📖 Reading: [File Upload](../readings/09_file_upload_and_processing.md)
- 📖 Reading: [Interactive Dashboard](../readings/10_interactive_dashboard.md)
- 📓 Notebook: [09 — File Upload](../notebooks/09_file_upload_and_processing.ipynb)
- 📓 Notebook: [10 — Dashboard](../notebooks/10_interactive_dashboard.ipynb)
- ✏️ Exercise: [09 — File Upload](../exercises/09_file_upload_workshop.py)
- ✏️ Exercise: [10 — Dashboard](../exercises/10_dashboard_workshop.py)
- 🖥️ Demo: [10 — Data Explorer](../apps/10_interactive_data_explorer.py)
- 🚀 Project: [P02 — Data Explorer](../projects/P02_data_explorer.md)
