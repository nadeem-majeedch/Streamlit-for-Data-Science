# P10 — Student Performance Analytics Dashboard

> **🚀 Project · Intermediate · M04–M06**
> *Build an analytics dashboard for tracking and visualizing student performance.*
> Difficulty: ★★★☆☆ · Duration: 2 weeks · Weight: Part of 15% project grade

---

## Problem Statement

A university department needs a dashboard to analyze student performance across courses, semesters, and demographics. The dashboard should help faculty identify at-risk students, track grade trends, and generate reports.

---

## Learning Objectives

1. Build a domain-specific analytics dashboard (CLO2, CLO3)
2. Implement complex filtering across multiple dimensions (CLO4)
3. Calculate derived metrics (GPA, pass rates, trends) (CLO2)
4. Create comparative visualizations (CLO3)
5. Design a professional, accessible dashboard (CLO6)

---

## Prerequisites

- Completed Modules 04–06
- Pandas groupby, pivot_table
- Session state for filter persistence

---

## Dataset

```python
import pandas as pd
import numpy as np

np.random.seed(42)
n = 500
courses = ["CS101", "CS201", "MATH101", "MATH201", "STAT101"]
semesters = ["Fall 2023", "Spring 2024", "Fall 2024"]

df = pd.DataFrame({
    "student_id": [f"S{i:04d}" for i in np.random.choice(range(1, 201), n)],
    "course": np.random.choice(courses, n),
    "semester": np.random.choice(semesters, n),
    "midterm": np.random.randint(40, 100, n),
    "final": np.random.randint(30, 100, n),
    "assignments": np.random.randint(50, 100, n),
    "participation": np.random.randint(60, 100, n),
    "department": np.random.choice(["CS", "Math", "Statistics"], n),
    "year": np.random.choice(["Freshman", "Sophomore", "Junior", "Senior"], n),
})
df["grade"] = ((df["midterm"] * 0.3 + df["final"] * 0.4 + df["assignments"] * 0.2 + df["participation"] * 0.1)).round(1)
```

---

## Functional Requirements

| # | Requirement | Marks |
|---|-------------|-------|
| F1 | Sidebar filters: course, semester, department, year, grade range | 8 |
| F2 | KPI metrics: avg grade, pass rate, at-risk count, total students | 8 |
| F3 | Grade distribution histogram | 6 |
| F4 | Performance by course bar chart | 6 |
| F5 | Trend chart: avg grade by semester | 6 |
| F6 | At-risk student table (grade < 60) | 6 |
| F7 | Student detail view: select a student, see all their grades | 8 |
| F8 | Export filtered data and summary report | 6 |
| F9 | Session state for filter persistence | 4 |

**Total: 58 marks**

---

## Architecture

```
student_analytics/
├── app.py
├── data_functions.py
├── components.py
├── requirements.txt
└── README.md
```

---

## Evaluation Criteria

| Criteria | Marks |
|----------|-------|
| Functionality | 35 |
| Visualization quality | 10 |
| Domain relevance (useful for faculty) | 5 |
| Code quality | 5 |
| Documentation | 3 |
| **Total** | **58** |

---

## Extensions

- Add GPA calculation per student
- Add cohort analysis (compare entering classes)
- Add predictive analytics (predict at-risk students)
- Add PDF report generation

---

## Related Materials

- 📖 Reading: [Interactive Dashboard](../readings/10_interactive_dashboard.md)
- 📓 Notebook: [10 — Dashboard](../notebooks/10_interactive_dashboard.ipynb)
- ✏️ Exercise: [10 — Dashboard](../exercises/10_dashboard_workshop.py)
- 🖥️ Demo: [10 — Data Explorer](../apps/10_interactive_data_explorer.py)
