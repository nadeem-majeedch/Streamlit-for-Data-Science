# Exercise 07 — Data Display Challenges: Solution Notes

> **👩‍🏫 Instructor Reference**
> *Expected approach, key code, and grading guidance.*

---

## Challenge 1: Formatted Employee Table

### Expected Approach
- Create 50-row DataFrame with random names, departments, salaries, dates, ratings
- Use `st.column_config` for currency, date, and rating formatting
- Sort by salary descending, display top 25

### Key Code
```python
st.dataframe(
    df.sort_values("Salary", ascending=False).head(25),
    hide_index=True,
    column_config={
        "Salary": st.column_config.NumberColumn(format="$%d"),
        "Start Date": st.column_config.DateColumn(format="MMM D, YYYY"),
        "Performance Rating": st.column_config.NumberColumn(format="%.1f ⭐"),
    },
)
```

### Alternative Approaches
- Using Pandas Styler for custom formatting
- Using `st.table()` with pre-formatted strings
- Adding conditional coloring with `background_gradient`

### Common Mistakes
- Using `"$%f"` format string incorrectly
- Not rounding ratings before display
- Forgetting `hide_index=True`

### Grading Notes (10 marks)
- Full marks: All 5 formatting requirements met
- 7 marks: 3-4 requirements met
- 4 marks: 2 requirements met
- Deduction: -1 for each missing format specification

---

## Challenge 2: Filtered Customer Dashboard

### Expected Approach
- Create 200-row customer dataset
- Build sidebar filters with multiselect and slider
- Apply filters sequentially
- Display with formatted columns and metric card

### Key Code
```python
filtered = df[
    (df["City"].isin(cities)) &
    (df["Purchase Amount"].between(*purchase_range)) &
    (df["Category"].isin(cats))
]
st.metric("Total Purchase Amount", f"${filtered['Purchase Amount'].sum():,.2f}")
st.dataframe(filtered, hide_index=True, column_config={
    "Purchase Amount": st.column_config.NumberColumn(format="$%.2f"),
})
```

### Common Mistakes
- Not using `.between()` for the range slider
- Displaying unfiltered data
- Missing metric card

### Grading Notes (10 marks)
- Full marks: All filters work, data updates, metric card present
- 7 marks: Filters work but no metric card
- 4 marks: Some filters missing or broken

---

## Challenge 3: Conditional Formatting Report

### Expected Approach
- Create product performance dataset
- Use Pandas Styler with `.applymap()` for conditional colors
- Add summary table with groupby

### Key Code
```python
def color_revenue(val):
    if val >= 15000:
        return "background-color: #90EE90"
    elif val >= 8000:
        return "background-color: #FFD700"
    else:
        return "background-color: #FFB6C1"

styled = df.style.applymap(color_revenue, subset=["Revenue"])
st.dataframe(styled, use_container_width=True)
```

### Alternative Approaches
- Using `st.column_config` with conditional coloring
- Using Altair for heatmap-style visualization
- Using `df.style.background_gradient()`

### Grading Notes (10 marks)
- Full marks: Both color functions work, summary table present
- 7 marks: Revenue coloring works, summary partial
- 4 marks: One coloring function works

---

## Challenge 4: Pivot Table Explorer

### Expected Approach
- Create pivot table with `pd.pivot_table()`
- Add Total row and column
- Apply heatmap-style coloring

### Key Code
```python
pivot = df.pivot_table(
    values="Revenue", index="Region",
    columns="Product", aggfunc="sum"
)
pivot["Total"] = pivot.sum(axis=1)
pivot.loc["Total"] = pivot.sum()

styled_pivot = pivot.style.background_gradient(cmap="YlOrRd", axis=None)
st.dataframe(styled_pivot, use_container_width=True)
```

### Grading Notes (10 marks)
- Full marks: Pivot table with both totals and styling
- 6 marks: Pivot table works but missing totals or styling

---

## Challenge 5: Row Selection (Bonus)

### Expected Approach
- Use `on_select="rerun"` with `selection_mode="multi-row"`
- Extract selected rows from selection state
- Display metrics and detail table for selection

### Key Code
```python
selection = st.dataframe(
    df, on_select="rerun",
    selection_mode="multi-row",
    use_container_width=True,
)
if selection and selection["selection"]["rows"]:
    selected = df.iloc[selection["selection"]["rows"]]
    c1, c2, c3 = st.columns(3)
    c1.metric("Total Revenue", f"${selected['Revenue'].sum():,.0f}")
```

### Grading Notes (10 marks bonus)
- Full marks: Selection works, metrics update, download button present
