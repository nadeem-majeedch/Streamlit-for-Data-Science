# Quiz 03 — Layouts, Containers & UI/UX

> **📝 Quiz · Module 03 · Beginner**
> *Test your understanding of Streamlit layouts, status feedback, and dashboard design.*
> ⏱ Time: 20 minutes · 📊 Points: 20

---

## Instructions

Answer all questions. For multiple-choice questions, circle the correct answer. For code questions, write the complete code.

---

## Part A: Multiple Choice (2 points each)

### Q1. What is the primary purpose of `st.sidebar`?

(a) To display the app title  \
(b) To organize controls and filters separate from the main content area  \
(c) To add a footer to the app  \
(d) To create a navigation menu

---

### Q2. What does `st.columns([0.7, 0.3])` create?

(a) Two equal-width columns  \
(b) A 70/30 column split where the first column is wider  \
(c) Three columns with the first being 70%  \
(d) A column with 0.7 width and a sidebar with 0.3 width

---

### Q3. Which element should you use to let users switch between different views of the same data?

(a) `st.expander()`  \
(b) `st.container()`  \
(c) `st.tabs()`  \
(d) `st.empty()`

---

### Q4. What is the purpose of `st.empty()`?

(a) To create a collapsible section  \
(b) To hold a single element that can be replaced  \
(c) To add vertical space  \
(d) To create a floating panel

---

### Q5. When should you use `st.progress()` instead of `st.spinner()`?

(a) When the task takes less than 1 second  \
(b) When you can estimate the percentage completion  \
(c) When you want to show a success message  \
(d) When the task has uncertain duration

---

### Q6. What is the recommended maximum number of metric columns in a KPI row?

(a) 2  \
(b) 3  \
(c) 4  \
(d) 6

---

### Q7. Which layout element is best for floating settings panels?

(a) `st.expander()`  \
(b) `st.popover()`  \
(c) `st.container()`  \
(d) `st.sidebar`

---

### Q8. What does "progressive disclosure" mean in dashboard design?

(a) Showing all data at once for completeness  \
(b) Revealing details on demand — KPIs first, then charts, then raw data  \
(c) Using dark mode for better readability  \
(d) Adding more widgets to make the dashboard interactive

---

## Part B: Short Answer (3 points each)

### Q9. Explain the difference between `st.expander()` and `st.tabs()`. When would you use each?

---

### Q10. A user reports that your dashboard shows a spinner but the content never appears. List three possible causes and fixes.

---

### Q11. Describe the "5-second test" for dashboard design. Give an example of a dashboard that passes and one that fails.

---

## Part C: Code Completion (4 points)

### Q12. Complete this code to create a basic dashboard layout with sidebar controls, KPI row, and tabbed content:

```python
import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Dashboard", layout="wide")

# TODO: Sidebar with controls
with st.__________:
    st.header("Filters")
    category = st.___________("Category", ["All", "A", "B", "C"])
    show_raw = st.___________("Show raw data")

# TODO: KPI row — 4 metrics
c1, c2, c3, c4 = st.___________(4)
c1.___________("Revenue", "$45K", "+5.2%", icon="💰")
c2.___________("Users", "1,204", "+12.1%", icon="👥")
c3.___________("Orders", "347", "-3.2%", icon="📦")
c4.___________("Conversion", "3.2%", "+0.4%", icon="🎯")

# TODO: Tabbed content
tab1, tab2 = st.___________(["Chart", "Data"])

with tab1:
    st.line_chart(pd.DataFrame(np.random.randn(20, 2)))

with tab2:
    st.___________(pd.DataFrame(np.random.randn(20, 2)))
```

---

## Answer Key (Instructor Only)

> **A1:** (b) To organize controls and filters separate from the main content area
>
> **A2:** (b) A 70/30 column split where the first column is wider
>
> **A3:** (c) `st.tabs()`
>
> **A4:** (b) To hold a single element that can be replaced
>
> **A5:** (b) When you can estimate the percentage completion
>
> **A6:** (c) 4
>
> **A7:** (b) `st.popover()`
>
> **A8:** (b) Revealing details on demand — KPIs first, then charts, then raw data
>
> **A9:** Expanders collapse/expand a section of content (progressive disclosure for details). Tabs switch between different views of the same data (mutually exclusive panels). Use expanders for optional details; use tabs for different ways to view the same data.
>
> **A10:** (1) Task is too fast — spinner hides before user sees it. Fix: add a small `time.sleep()`. (2) Task raises an exception before completing — fix: add try/except. (3) Spinner is inside a conditional that doesn't execute — fix: ensure the code always runs.
>
> **A11:** A user should understand the dashboard purpose and key insights within 5 seconds. Passes: KPI row at top showing "Revenue: $1.2M (+8%)" with a clear chart below. Fails: Raw data table shown first with no summary or metrics.
>
> **A12:** `sidebar`, `selectbox`, `checkbox`, `columns`, `metric`, `tabs`, `dataframe`

---

## Related Materials

- 📖 Reading: [05 — Layouts, Containers & Page Structure](../readings/05_layouts_and_containers.md)
- 📖 Reading: [06 — Dashboard Design & UI/UX](../readings/06_dashboard_design_ui_ux.md)
- 📓 Notebook: [05 — Layouts & Containers](../notebooks/05_layouts_and_containers.ipynb)
- 📓 Notebook: [06 — Data Science Dashboards](../notebooks/06_data_science_dashboards.ipynb)
- ✏️ Exercise: [05 — Layout Basics](../exercises/05_layout_basics.py)
- ✏️ Exercise: [06 — Dashboard Builder](../exercises/06_dashboard_builder.py)
- 🖥️ Demo: [05 — Layouts Demo](../apps/05_layouts_demo.py)
- 🖥️ Demo: [06 — Dashboard Demo](../apps/06_dashboard_demo.py)
