# P03 — Simple Calculator & Statistics App

> **🚀 Project · Beginner · M01–M02**
> *Build an interactive calculator and basic statistics tool.*
> Difficulty: ★☆☆☆☆ · Duration: 1 week · Weight: Part of 15% project grade

---

## Problem Statement

A math teacher needs a simple tool for students to:
1. Perform basic calculations (add, subtract, multiply, divide)
2. Enter a list of numbers and see statistics (mean, median, mode, range)
3. Visualize the distribution with a simple chart

Build a Streamlit app that replaces a basic calculator and stats tool.

---

## Learning Objectives

1. Use Streamlit widgets for user input (CLO2)
2. Implement conditional logic based on widget values (CLO2)
3. Compute basic statistics with Pandas/NumPy (CLO2)
4. Display results with `st.metric()` and `st.write()` (CLO2)
5. Create a simple chart with `st.bar_chart()` (CLO3)

---

## Prerequisites

- Completed Modules 01–02
- Basic Python arithmetic and lists
- Pandas basics (mean, median)

---

## Functional Requirements

| # | Requirement | Marks |
|---|-------------|-------|
| F1 | Calculator mode: two number inputs + operation selectbox (Add, Subtract, Multiply, Divide) | 8 |
| F2 | Display calculation result with `st.success()` or `st.error()` for division by zero | 5 |
| F3 | Statistics mode: text_area for entering numbers (comma-separated) | 5 |
| F4 | Compute and display: count, sum, mean, median, min, max, range | 10 |
| F5 | Display a bar chart of the entered numbers | 5 |
| F6 | Handle invalid inputs (non-numeric text, empty input) | 5 |
| F7 | Sidebar to switch between Calculator and Statistics modes | 5 |

**Total: 43 marks**

---

## Architecture

```
calculator_app/
├── app.py
├── requirements.txt
└── README.md
```

Single-file app is acceptable for beginner level.

---

## Milestones

| Day | Milestone |
|-----|-----------|
| 1 | Calculator mode working with all 4 operations |
| 2 | Statistics mode: number entry and computation |
| 3 | Chart display and error handling |
| 4 | Polish, mode switching, README |

---

## Evaluation Criteria

| Criteria | Marks |
|----------|-------|
| Calculator functionality | 13 |
| Statistics functionality | 20 |
| Error handling | 5 |
| UI/UX | 5 |
| **Total** | **43** |

---

## Extensions

- Add a history of calculations in session state
- Add scientific functions (sqrt, power, log)
- Add a histogram chart alongside the bar chart
- Allow file upload of numbers

---

## Related Materials

- 📖 Reading: [Widgets & Input](../readings/03_streamlit_widgets_and_input.md)
- 📓 Notebook: [03 — Widgets](../notebooks/03_streamlit_widgets.ipynb)
- ✏️ Exercise: [03 — Widget Mastery](../exercises/03_widget_mastery.py)
