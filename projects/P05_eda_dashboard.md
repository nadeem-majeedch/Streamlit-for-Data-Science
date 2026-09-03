# P05 — Exploratory Data Analysis Dashboard

> **🚀 Project · Intermediate · M04–M06**
> *Build an automated EDA dashboard that generates insights from any dataset.*
> Difficulty: ★★☆☆☆ · Duration: 1.5 weeks · Weight: Part of 15% project grade

---

## Problem Statement

Before building models, data scientists must understand their data. Build a Streamlit app that automatically performs Exploratory Data Analysis (EDA): showing distributions, correlations, missing values, outliers, and summary statistics for any uploaded dataset.

---

## Learning Objectives

1. Implement multi-tab data exploration (CLO2)
2. Create multiple visualization types (CLO3)
3. Compute statistical summaries programmatically (CLO2)
4. Handle different data types dynamically (CLO4)
5. Design a clean, organized dashboard layout (CLO6)

---

## Prerequisites

- Completed Modules 04–06
- Pandas describe(), corr(), value_counts()
- Plotly or Matplotlib basics

---

## Functional Requirements

| # | Requirement | Marks |
|---|-------------|-------|
| F1 | File upload with automatic column type detection (numeric vs categorical) | 5 |
| F2 | "Overview" tab: shape, dtypes, head, describe() | 8 |
| F3 | "Distributions" tab: histograms for numeric, bar charts for categorical | 10 |
| F4 | "Correlations" tab: correlation matrix heatmap | 8 |
| F5 | "Missing Values" tab: null count, percentage, pattern visualization | 8 |
| F6 | "Outliers" tab: box plots for numeric columns | 6 |
| F7 | Sidebar: column selector, number of bins slider | 5 |
| F8 | Export EDA report as downloadable summary | 5 |

**Total: 55 marks**

---

## Architecture

```
eda_dashboard/
├── app.py
├── eda_functions.py    # Pure analysis functions
├── requirements.txt
└── README.md
```

---

## Evaluation Criteria

| Criteria | Marks |
|----------|-------|
| Functionality (all 8 tabs/features) | 35 |
| Visualization quality | 10 |
| Code organization | 5 |
| Documentation | 5 |
| **Total** | **55** |

---

## Extensions

- Add interactive filtering before EDA
- Add time-series specific analysis (trends, seasonality)
- Add text column analysis (word frequency)
- Generate a PDF report

---

## Related Materials

- 📖 Reading: [Visualization](../readings/08_visualization_matplotlib_plotly.md)
- 📖 Reading: [Data Display](../readings/07_data_display_dataframes.md)
- 📓 Notebook: [08 — Visualization](../notebooks/08_interactive_visualization.ipynb)
- ✏️ Exercise: [08 — Visualization](../exercises/08_visualization_workshop.py)
