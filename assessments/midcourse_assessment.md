# Mid-Course Assessment

> **🎯 Assessment · Modules 01–08 · Week 9**
> *Covers Streamlit fundamentals through architecture and multipage apps.*
> ⏱ Duration: 2 hours · 📊 Total: 100 marks · Difficulty: ★★★☆☆

---

## Course Information

| Field | Detail |
|-------|--------|
| **Course** | Streamlit for Data Science |
| **Assessment** | Mid-Course Examination |
| **Weight** | 10% of course grade |
| **Duration** | 2 hours (120 minutes) |
| **Type** | Closed-book, individual |
| **Materials Allowed** | Python documentation, Streamlit documentation (offline) |

---

## Learning Outcomes Assessed

| CLO | Outcome | Bloom's | Marks |
|-----|---------|---------|-------|
| CLO1 | Explain Streamlit's execution model, architecture, and widget lifecycle | Understand | 15 |
| CLO2 | Build interactive data applications using widgets, layouts, and state | Apply | 25 |
| CLO3 | Implement data visualization strategies | Apply | 15 |
| CLO4 | Design and manage application state across reruns | Apply, Analyze | 20 |
| CLO5 | Optimize performance through caching and fragments | Analyze | 10 |
| CLO6 | Design well-structured applications using architecture patterns | Analyze | 15 |

---

## Prerequisites

- Completed Modules 01–08
- All exercises and notebooks up to Week 8
- Python 3.10+, Streamlit ≥ 1.44.0 installed

---

## Part A: Conceptual Knowledge (20 marks)

### A1. Execution Model (5 marks)

**Q1.1** (2 marks) Explain what happens when a user interacts with a widget in a Streamlit app. Include the concept of "reruns" in your answer.

**Q1.2** (3 marks) A student writes:

```python
import streamlit as st
st.set_page_config(page_title="App")
st.title("My App")
import pandas as pd
```

Explain why this code might behave unexpectedly and how to fix it.

---

### A2. Widget Lifecycle (5 marks)

**Q2.1** (2 marks) What is the difference between a widget's **return value** and its value in **`st.session_state`**?

**Q2.2** (3 marks) Explain how `st.form()` changes widget behavior. Why would you use a form instead of individual widgets?

---

### A3. Caching Concepts (5 marks)

**Q3.1** (3 marks) Compare `@st.cache_data` and `@st.cache_resource`. For each, give:
- What it returns (copy vs. singleton)
- A suitable use case
- When NOT to use it

**Q3.2** (2 marks) Explain what cache invalidation means and why it matters after database writes.

---

### A4. Architecture (5 marks)

**Q4.1** (3 marks) Explain the principle of "separation of concerns" in the context of a Streamlit application. Give an example of good separation.

**Q4.2** (2 marks) Compare the `pages/` directory convention with `st.navigation()` for multipage apps. When would you prefer each?

---

## Part B: Coding (40 marks)

### B1. Widget & Layout Implementation (15 marks)

**Task:** Build a sidebar filter panel for a sales dataset.

Write complete Streamlit code that:

1. (3 marks) Creates a sidebar with:
   - A header "Data Filters"
   - A multiselect for "Region" with options ["North", "South", "East", "West"]
   - A slider for "Min Revenue" (0 to 100000, default 0)
   - A checkbox "Show only top performers (Rating ≥ 4.0)"

2. (3 marks) Generates a sample DataFrame with columns: Region, Revenue, Units, Rating (100 rows, seeded with `np.random.seed(42)`)

3. (4 marks) Applies all sidebar filters to the DataFrame and displays the filtered row count

4. (5 marks) Displays:
   - 4 metric cards (Total Revenue, Total Units, Avg Rating, Record Count) using `st.columns(4)`
   - The filtered DataFrame using `st.dataframe()` with `use_container_width=True`
   - A download button for the filtered data as CSV

---

### B2. Session State & Forms (15 marks)

**Task:** Build a multi-step survey form with session state.

Write complete Streamlit code that:

1. (3 marks) Initializes session state for:
   - `current_step` (1, 2, or 3)
   - `form_data` dict with keys: name, email, satisfaction, comments

2. (4 marks) Step 1 — Personal Information:
   - Text input for name
   - Text input for email
   - "Next" button (only enabled if name and email are filled)
   - Stores values in session_state.form_data

3. (4 marks) Step 2 — Feedback:
   - Slider for satisfaction (1–10)
   - Text area for comments
   - "Back" and "Next" buttons
   - Progress bar showing current step

4. (4 marks) Step 3 — Review & Submit:
   - Display all collected information in a formatted card
   - "Back" and "Submit" buttons
   - On submit: save to a list in session_state, show success, reset form

---

### B3. Visualization & Data Display (10 marks)

**Task:** Create a multi-view data visualization dashboard.

Given this DataFrame:

```python
import pandas as pd
import numpy as np
np.random.seed(42)
df = pd.DataFrame({
    "date": pd.date_range("2024-01-01", periods=365),
    "category": np.random.choice(["A", "B", "C"], 365),
    "value": np.random.randn(365).cumsum() + 100,
    "volume": np.random.randint(100, 1000, 365),
})
```

Write code to:

1. (2 marks) Display the DataFrame with salary-like formatting for the value column and hidden index

2. (3 marks) Create 3 tabs: "Trend", "Distribution", "Comparison"
   - Trend tab: line chart of value over date
   - Distribution tab: histogram of value
   - Comparison tab: bar chart of total volume by category

3. (3 marks) Add sidebar controls to filter by category and date range

4. (2 marks) Show summary statistics in a styled table

---

## Part C: Debugging (20 marks)

### C1. State Bug (5 marks)

**Q:** This counter app shows "Count: 0" even after clicking. Find the bug, explain why it occurs, and provide the corrected code.

```python
import streamlit as st

count = 0
if st.button("Increment"):
    count += 1
st.metric("Count", count)
```

---

### C2. Cache Bug (5 marks)

**Q:** After adding a record to the database, the displayed data is stale. Find and fix the caching issue:

```python
@st.cache_resource
def get_db():
    return sqlite3.connect("app.db")

def add_record(name, value):
    conn = get_db()
    conn.execute("INSERT INTO records VALUES (?, ?)", (name, value))
    conn.commit()

conn = get_db()
df = pd.read_sql("SELECT * FROM records", conn)
st.dataframe(df)
```

---

### C3. Layout Bug (5 marks)

**Q:** The app below shows the title AFTER the data. Also, the metrics don't display because `st.columns` is called incorrectly. Fix ALL issues:

```python
import streamlit as st
import pandas as pd

df = pd.DataFrame({"Revenue": [100, 200, 300]})
st.dataframe(df)
st.title("Sales Dashboard")

c1, c2 = st.columns(2)
c1.metric("Total", df["Revenue"].sum())
c2.metric("Average", df["Revenue"].mean())
st.metric("Count", len(df))
```

---

### C4. Form Bug (5 marks)

**Q:** This form should collect feedback and display it. It crashes with a TypeError. Find and fix the bug:

```python
import streamlit as st

with st.form("feedback"):
    rating = st.slider("Rating", 1, 5)
    comment = st.text_area("Comment")
    submitted = st.form_submit_button("Submit")

if submitted:
    st.write(f"Rating: {rating}")
    st.write(f"Comment: {comment}")
    st.balloons()
```

---

## Part D: Design & Architecture (20 marks)

### D1. App Architecture (10 marks)

**Task:** Design a "Student Grade Tracker" app architecture.

**Requirements:**
1. Upload a CSV of student grades
2. Filter by course and semester
3. Calculate GPA per student
4. Visualize grade distributions
5. Export a summary report

**Deliverables:**

1. (3 marks) **File structure:** Draw the directory layout with descriptions for each file

2. (3 marks) **Function signatures:** Write the signatures (not implementations) for:
   - Data loading function
   - GPA calculation function
   - Report generation function

3. (2 marks) **Caching strategy:** Which functions should be cached and why?

4. (2 marks) **Error handling:** List 3 error scenarios and how you'd handle each

---

### D2. Performance Analysis (10 marks)

**Task:** A Streamlit app has the following performance issues:

```python
import streamlit as st
import pandas as pd
import plotly.express as px

# Issue 1: Data loaded on every rerun
df = pd.read_csv("large_dataset.csv")  # 500MB file, takes 8 seconds

# Issue 2: Chart recomputed on every interaction
fig = px.scatter(df, x="x", y="y", color="category")  # Takes 3 seconds

# Issue 3: No caching anywhere
def process_data():
    return df.groupby("category").agg({"value": "mean", "count": "sum"})

# Issue 4: Heavy import at top level
import torch
model = torch.load("model.pt")
```

**Questions:**

1. (3 marks) For each issue, explain WHY it's a problem in Streamlit's execution model

2. (4 marks) Rewrite the code with appropriate caching decorators and explain your choices

3. (3 marks) Identify one additional performance optimization not shown in the code and explain how to implement it

---

## Marking Guide

| Part | Topic | Marks | Bloom's |
|------|-------|-------|---------|
| A | Conceptual Knowledge | 20 | Understand, Analyze |
| B | Coding | 40 | Apply |
| C | Debugging | 20 | Analyze |
| D | Design & Architecture | 20 | Analyze, Evaluate |
| **Total** | | **100** | |

---

## Grade Boundaries

| Grade | Score | Description |
|-------|-------|-------------|
| A | 85–100 | Exceptional understanding and application |
| B | 70–84 | Strong grasp of core concepts |
| C | 55–69 | Adequate understanding, some gaps |
| D | 40–54 | Below expectations, needs improvement |
| F | < 40 | Insufficient mastery |

---

## Answer Key

> ⚠️ **Instructor copy — do not distribute to students**
> Available in `assessments/rubrics/midcourse_rubric.md`

---

## Related Materials

- 📋 Curriculum: [docs/curriculum.md](../docs/curriculum.md)
- 📋 Learning Outcomes: [docs/learning_outcomes.md](../docs/learning_outcomes.md)
- 📝 Question Bank: [quizzes/question_bank.md](../quizzes/question_bank.md)
