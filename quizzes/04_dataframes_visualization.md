# Quiz 04 — DataFrames & Visualization

> **📝 Quiz · Module 04 · Intermediate**
> *Test your understanding of data display, formatting, and visualization in Streamlit.*
> ⏱ Time: 20 minutes · 📊 Points: 24

---

## Instructions

Answer all questions. For multiple-choice questions, circle the correct answer. For code questions, write the complete code.

---

## Part A: Multiple Choice (2 points each)

### Q1. Which is the primary tool for displaying interactive tables in Streamlit?

(a) `st.write()`  \
(b) `st.table()`  \
(c) `st.dataframe()`  \
(d) `st.json()`

---

### Q2. What does `hide_index=True` do in `st.dataframe()`?

(a) Removes the DataFrame from the page  \
(b) Hides the index column for a cleaner display  \
(c) Hides the column headers  \
(d) Makes the table read-only

---

### Q3. How do you format a column as currency in `st.dataframe()`?

(a) `st.column_config.NumberColumn(format="$ %d")`  \
(b) `st.column_config.CurrencyColumn(format="$ %d")`  \
(c) `st.dataframe(df.style.format({"Revenue": "$%d"}))`  \
(d) Both (a) and (c) work

---

### Q4. When should you use `st.table()` instead of `st.dataframe()`?

(a) When you have more than 100 rows  \
(b) When you need interactive sorting  \
(c) When you have a small, static table (< 20 rows)  \
(d) When you need row selection

---

### Q5. What is the correct way to display a Matplotlib figure in Streamlit?

(a) `st.pyplot(fig)`  \
(b) `st.plot(fig)`  \
(c) `st.matplotlib(fig)`  \
(d) `st.show(fig)`

---

### Q6. What parameter should you always use with `st.plotly_chart()`?

(a) `width="stretch"`  \
(b) `use_container_width=True`  \
(c) `responsive=True`  \
(d) `full_width=True`

---

### Q7. Which chart type is best for showing trends over time?

(a) Bar chart  \
(b) Pie chart  \
(c) Line chart  \
(d) Scatter chart

---

### Q8. How do you make a DataFrame interactive so users can select rows?

(a) `st.dataframe(df, selectable=True)`  \
(b) `st.dataframe(df, on_select="rerun")`  \
(c) `st.dataframe(df, interactive=True)`  \
(d) `st.selectable(df)`

---

## Part B: Short Answer (3 points each)

### Q9. Explain the difference between `st.dataframe()` and `st.data_editor()`. When would you use each?

---

### Q10. A user says "My Plotly chart doesn't fill the available width." What parameter fixes this, and where does it go?

---

### Q11. Describe the complete workflow for creating a filtered, formatted table in Streamlit. List each step in order.

---

### Q12. Explain when you would choose Matplotlib over Plotly for a visualization. Give a specific use case.

---

## Part C: Code Completion (4 points)

### Q13. Complete this code to display a formatted, filtered DataFrame:

```python
import streamlit as st
import pandas as pd

# Assume df has columns: Name, Revenue, Date, Rating

# Sidebar filter
min_rating = st.sidebar.slider("Min Rating", 1.0, 5.0, 3.0)

# Filter data
filtered = df[df["______"] >= min_rating]

# Display with formatting
st.dataframe(
    filtered,
    hide_index=______,
    column_config={
        "Revenue": st.column_config.______(
            "Revenue",
            format="______",
        ),
        "Date": st.column_config.______(
            "Sale Date",
            format="MMM D, YYYY",
        ),
    },
)
```

---

### Q14. Complete this code to create a Plotly scatter plot with a trendline:

```python
import plotly.express as px

fig = px.______(
    df,
    x="Marketing",
    y="______",
    color="Region",
    ______="ols",
    title="Marketing vs Revenue",
)
st.______(fig, use_container_width=True)
```

---

## Answer Key (Instructor Only)

> **A1:** (c) `st.dataframe()`
>
> **A2:** (b) Hides the index column for a cleaner display
>
> **A3:** (d) Both (a) and (c) work
>
> **A4:** (c) When you have a small, static table (< 20 rows)
>
> **A5:** (a) `st.pyplot(fig)`
>
> **A6:** (b) `use_container_width=True`
>
> **A7:** (c) Line chart
>
> **A8:** (b) `st.dataframe(df, on_select="rerun")`
>
> **A9:** `st.dataframe()` displays read-only interactive tables. `st.data_editor()` allows users to edit cells, add/delete rows, and modify data. Use `st.dataframe()` for displaying results; use `st.data_editor()` when the user needs to input or modify data.
>
> **A10:** The parameter is `use_container_width=True`, passed to `st.plotly_chart()`. Example: `st.plotly_chart(fig, use_container_width=True)`.
>
> **A11:** (1) Create sidebar filter widgets, (2) Apply filter logic to DataFrame, (3) Transform data if needed (aggregate, sort, compute columns), (4) Call `st.dataframe()` with `column_config` for formatting, (5) Set `hide_index=True` and appropriate `height`.
>
> **A12:** Use Matplotlib when you need static, publication-quality figures with precise control over every element (axis ticks, annotations, subplots). Example: generating a figure for a PDF report or academic paper where interactivity is not needed.
>
> **A13:** `Rating`, `True`, `NumberColumn`, `$ %d`, `DateColumn`
>
> **A14:** `scatter`, `Revenue`, `trendline`, `plotly_chart`

---

## Related Materials

- 📖 Reading: [07 — Data Display: DataFrames, Tables & Pandas Integration](../readings/07_data_display_dataframes.md)
- 📖 Reading: [08 — Visualization with Streamlit, Matplotlib & Plotly](../readings/08_visualization_matplotlib_plotly.md)
- 📓 Notebook: [07 — DataFrames, Tables & Pandas Integration](../notebooks/07_dataframes_tables_pandas.ipynb)
- 📓 Notebook: [08 — Interactive Visualization & Chart Selection](../notebooks/08_interactive_visualization.ipynb)
- ✏️ Exercise: [07 — Data Display Challenges](../exercises/07_data_display_challenges.py)
- ✏️ Exercise: [08 — Visualization Workshop](../exercises/08_visualization_workshop.py)
- 🖥️ Demo: [07 — Data Display & Visualization Demo](../apps/07_data_display_demo.py)
