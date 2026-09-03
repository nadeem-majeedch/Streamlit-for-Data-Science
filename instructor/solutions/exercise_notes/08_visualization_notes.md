# Exercise 08 — Visualization Workshop: Solution Notes

> **👩‍🏫 Instructor Reference**
> *Expected approach, key code, and grading guidance.*

---

## Challenge 1: Chart Selection

### Expected Approach
| Question | Correct Chart | Library |
|----------|---------------|---------|
| Q1: Revenue over time | Line chart | st.line_chart or px.line |
| Q2: Units per product | Bar chart | st.bar_chart or px.bar |
| Q3: Revenue distribution | Histogram | px.histogram |
| Q4: Marketing vs Revenue | Scatter plot | px.scatter or st.scatter_chart |
| Q5: Revenue by region | Box plot | px.box |

### Key Code for Q1 (Line Chart)
```python
monthly = sales_df.set_index("Date").resample("M")["Revenue"].sum()
st.line_chart(monthly)
```

### Key Code for Q3 (Histogram)
```python
import plotly.express as px
fig = px.histogram(sales_df, x="Revenue", nbins=40, title="Revenue Distribution")
st.plotly_chart(fig, use_container_width=True)
```

### Key Code for Q5 (Box Plot)
```python
fig = px.box(sales_df, x="Region", y="Revenue", color="Region")
st.plotly_chart(fig, use_container_width=True)
```

### Common Mistakes
- Using line chart for categorical data (Q2)
- Using bar chart for distributions (Q3)
- Forgetting `use_container_width=True` with Plotly

### Grading Notes (20 marks — 4 per chart)
- Full marks: Correct chart type AND appropriate library choice
- 3 marks: Correct chart type but wrong library for context
- 2 marks: Chart renders but wrong type
- 0 marks: Missing or broken

---

## Challenge 2: Matplotlib Subplots

### Expected Approach
Create a 2x2 figure with `plt.subplots(2, 2, figsize=(12, 10))` containing:
1. Revenue histogram with mean line
2. Revenue by Region bar chart
3. Rating distribution histogram
4. Marketing vs Revenue scatter

### Key Code
```python
import matplotlib.pyplot as plt

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

axes[0, 0].hist(sales_df["Revenue"], bins=30, edgecolor="black", alpha=0.7)
axes[0, 0].axvline(sales_df["Revenue"].mean(), color="red", linestyle="--", label="Mean")
axes[0, 0].set_title("Revenue Distribution")
axes[0, 0].legend()

axes[0, 1].bar(
    sales_df.groupby("Region")["Revenue"].sum().index,
    sales_df.groupby("Region")["Revenue"].sum().values
)
axes[0, 1].set_title("Revenue by Region")

axes[1, 0].hist(sales_df["Rating"], bins=20, edgecolor="black", alpha=0.7, color="green")
axes[1, 0].set_title("Rating Distribution")

axes[1, 1].scatter(sales_df["Marketing"], sales_df["Revenue"], alpha=0.5)
axes[1, 1].set_title("Marketing vs Revenue")
axes[1, 1].set_xlabel("Marketing Spend")
axes[1, 1].set_ylabel("Revenue")

plt.tight_layout()
st.pyplot(fig)
```

### Common Mistakes
- Forgetting `plt.tight_layout()`
- Not setting `alpha` on scatter (overplotting)
- Missing axis labels or titles
- Forgetting `st.pyplot(fig)` instead of `plt.show()`

### Grading Notes (20 marks)
- Full marks: All 4 subplots with titles, mean line, proper labels
- 15 marks: 3-4 subplots with titles
- 10 marks: 2 subplots working
- 5 marks: 1 subplot working

---

## Challenge 3: Interactive Plotly Dashboard

### Expected Approach
Build sidebar controls that dynamically select chart type, axes, and color encoding.

### Key Code
```python
with st.sidebar:
    chart_type = st.selectbox("Chart type", ["Bar", "Line", "Scatter"])
    x_col = st.selectbox("X axis", ["Region", "Product"])
    y_col = st.selectbox("Y axis", ["Revenue", "Units"])
    color_by = st.selectbox("Color", ["None", "Region", "Product"])

color = color_by if color_by != "None" else None

if chart_type == "Bar":
    fig = px.bar(sales_df, x=x_col, y=y_col, color=color, title=f"{y_col} by {x_col}")
elif chart_type == "Line":
    fig = px.line(sales_df, x=x_col, y=y_col, color=color, title=f"{y_col} by {x_col}")
elif chart_type == "Scatter":
    fig = px.scatter(sales_df, x=x_col, y=y_col, color=color, title=f"{y_col} by {x_col}")

st.plotly_chart(fig, use_container_width=True)
```

### Grading Notes (15 marks)
- Full marks: All controls work, chart updates dynamically
- 10 marks: Chart updates but missing some controls
- 5 marks: Static chart only

---

## Challenge 4: Side-by-Side Comparison

### Expected Approach
Two columns with horizontal bar charts, different colors, with insight caption.

### Key Code
```python
col1, col2 = st.columns(2)

with col1:
    st.subheader("Revenue by Product")
    fig1 = px.bar(
        sales_df.groupby("Product")["Revenue"].sum().sort_values(),
        orientation="h", title="Total Revenue",
        color_discrete_sequence=["#636EFA"]
    )
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    st.subheader("Units by Product")
    fig2 = px.bar(
        sales_df.groupby("Product")["Units"].sum().sort_values(),
        orientation="h", title="Total Units",
        color_discrete_sequence=["#EF553B"]
    )
    st.plotly_chart(fig2, use_container_width=True)

st.caption("Insight: Laptops generate the most revenue but Phones sell the most units.")
```

### Grading Notes (10 marks)
- Full marks: Both charts render with different colors and insight caption
- 6 marks: Charts render but missing colors or caption
