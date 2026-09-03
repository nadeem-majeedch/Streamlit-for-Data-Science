# Assignment 01 — Personal Dashboard

> **📋 Assignment · Level 1 (Beginner) — Modules 01–03**
> *Build your first interactive Streamlit application.*

---

## Course Information

| Field | Detail |
|-------|--------|
| **Course** | Streamlit for Data Science |
| **Assignment** | A01 — Personal Dashboard |
| **Due Date** | End of Week 3 |
| **Weight** | 4% of course grade |
| **Difficulty** | ★☆☆☆☆ Beginner |
| **Collaboration** | Individual |

---

## Learning Outcomes

After completing this assignment you will be able to:

1. **LO1** — Create and run a Streamlit application from scratch (Remember)
2. **LO2** — Use text elements, markdown, and code display (Understand)
3. **LO3** — Implement sidebar navigation and widgets (Apply)
4. **LO4** — Display data using DataFrames and metrics (Apply)
5. **LO5** — Structure a multi-section application with layouts (Apply)

---

## Prerequisites

- Completed Modules 01, 02, 03
- Python 3.10+ installed with Streamlit
- Basic Pandas knowledge

---

## Overview

Build a **Personal Dashboard** — a single-page Streamlit app that serves as your
personal profile and productivity hub. This is your first substantial Streamlit
application.

The dashboard must include:
- A profile section with your information
- An interactive calculator or converter
- A data display section with at least one DataFrame
- Sidebar navigation

---

## Tasks

### Task 1: Profile Section (15 marks)

Create a profile page that displays:

| Requirement | Marks |
|-------------|-------|
| Title with your name using `st.title()` | 2 |
| A brief bio using `st.markdown()` with bold and italic text | 2 |
| Your photo or avatar placeholder using `st.image()` or emoji | 2 |
| A code block showing your favorite Python snippet using `st.code()` | 2 |
| Contact information using `st.write()` or columns | 2 |
| A LaTeX formula (any valid LaTeX) using `st.latex()` | 2 |
| A caption with the current date using `st.caption()` | 1 |
| Creative use of at least 2 other text elements | 2 |

### Task 2: Interactive Widgets (15 marks)

Build an interactive section in the sidebar with at least 5 different widget types:

| Requirement | Marks |
|-------------|-------|
| `st.sidebar.selectbox()` for a category choice | 2 |
| `st.sidebar.slider()` for a numeric range | 2 |
| `st.sidebar.text_input()` for user text | 2 |
| `st.sidebar.checkbox()` to toggle a feature | 2 |
| `st.sidebar.radio()` for exclusive options | 2 |
| Each widget connected to visible app behavior | 3 |
| Clear labels and helpful defaults | 2 |

### Task 3: Data Display (20 marks)

Display data using at least 2 methods:

| Requirement | Marks |
|-------------|-------|
| Create a DataFrame with at least 5 rows and 4 columns | 3 |
| Display it using `st.dataframe()` with `use_container_width=True` | 2 |
| Display a summary using `st.table()` | 2 |
| Use `st.metric()` to show at least 3 KPIs | 4 |
| Data changes based on a sidebar widget selection | 4 |
| Data is meaningful (not random numbers with no context) | 3 |
| Column names are descriptive | 2 |

### Task 4: Layout & Structure (20 marks)

| Requirement | Marks |
|-------------|-------|
| Uses `st.columns()` for side-by-side content | 4 |
| Uses `st.tabs()` or `st.expander()` for sections | 4 |
| Sidebar separates controls from content | 3 |
| Visual separators (`st.divider()`) between sections | 2 |
| Logical flow: profile → widgets → data → about | 3 |
| Consistent styling throughout | 2 |
| Page config set correctly (`st.set_page_config()` as first call) | 2 |

### Task 5: Code Quality & Documentation (10 marks)

| Requirement | Marks |
|-------------|-------|
| No hardcoded magic numbers — use variables or constants | 2 |
| Functions used to organize repeated logic | 3 |
| Comments explaining non-obvious sections | 2 |
| Clean indentation and PEP 8 style | 2 |
| File runs without errors: `streamlit run A01_yourname.py` | 1 |

### Task 6: Creativity & Polish (10 marks)

| Requirement | Marks |
|-------------|-------|
| App has a cohesive theme (not just default) | 3 |
| At least one element that surprised or delighted | 3 |
| Overall professional appearance | 2 |
| Thoughtful use of emojis and visual elements | 2 |

### Task 7: Documentation (10 marks)

Create a `README.md` for your assignment:

| Requirement | Marks |
|-------------|-------|
| Title and description of your dashboard | 2 |
| Screenshot or description of the app | 2 |
| List of features implemented | 2 |
| How to run the app | 2 |
| What you learned | 2 |

**Total: 100 marks**

---

## Deliverables

1. **`A01_yourname.py`** — Your Streamlit application
2. **`README.md`** — Documentation with screenshots
3. **Screenshot(s)** of your running app (PNG in repo or linked)

### Submission

Push to your course repository under `assignments/A01/`:

```
assignments/A01/
├── A01_yourname.py
├── README.md
└── screenshots/
    ├── dashboard_1.png
    └── dashboard_2.png
```

---

## Starter Template

```python
import streamlit as st
import pandas as pd

st.set_page_config(page_title="My Dashboard", layout="wide")

st.title("My Personal Dashboard")

# TODO: Add your profile section
# TODO: Add sidebar widgets
# TODO: Add data display
# TODO: Add layout elements
```

---

## Grading Rubric Summary

| Category | Marks | Bloom's Level |
|----------|-------|---------------|
| Profile Section | 15 | Remember, Understand |
| Interactive Widgets | 15 | Apply |
| Data Display | 20 | Apply |
| Layout & Structure | 20 | Apply |
| Code Quality | 10 | Apply |
| Creativity | 10 | Create |
| Documentation | 10 | Understand |
| **Total** | **100** | |

---

## Common Mistakes to Avoid

1. **❌ Forgetting `st.set_page_config()`** — Must be the first Streamlit call
2. **❌ Using absolute file paths** — Use relative paths or generated data
3. **❌ No error handling** — Widgets should have sensible defaults
4. **❌ Copying notebook code verbatim** — Write your own implementation
5. **❌ Ignoring the sidebar** — The assignment requires sidebar navigation

---

## Related Materials

- 📖 Reading: [Streamlit Introduction](../readings/01_streamlit_introduction.md)
- 📖 Reading: [First Streamlit App](../readings/02_first_streamlit_app.md)
- 📓 Notebook: [01 — Introduction](../notebooks/01_Streamlit_Introduction.ipynb)
- 📓 Notebook: [02 — First App](../notebooks/02_First_Streamlit_App.ipynb)
- ✏️ Exercise: [01 — Hello Streamlit](../exercises/01_hello_streamlit.py)
- ✏️ Exercise: [03 — Widget Mastery](../exercises/03_widget_mastery.py)
- ✏️ Exercise: [05 — Layout Basics](../exercises/05_layout_basics.py)
- 🖥️ Demo: [01 — Introduction](../apps/01_introduction_demo.py)
