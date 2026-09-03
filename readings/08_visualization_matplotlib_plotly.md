# 08 — Visualization: Native Charts, Matplotlib & Plotly

> **📖 Reading · Module 04 · Intermediate**
> *Choose the right chart for the right question — every time.*

---

## Learning Objectives

After completing this reading you will be able to:

- Use Streamlit's native chart types (`st.line_chart`, `st.bar_chart`, `st.area_chart`, `st.scatter_chart`).
- Embed Matplotlib figures with `st.pyplot()`.
- Embed Plotly figures with `st.plotly_chart()`.
- Select the appropriate chart type for a given data question.
- Apply visualization best practices for readability and clarity.
- Transform data before visualization for meaningful insights.

---

## 1. The Visualization Pipeline

Every visualization in Streamlit follows the same pipeline:

```
DATA → TRANSFORM → CHOOSE CHART → RENDER → INTERACT
 │         │            │            │          │
 ▼         ▼            ▼            ▼          ▼
Raw     Filter/       Select      Display    User
data    Aggregate     type        in app     explores
```

**The key insight:** Most of the work is in the **transform** step. A chart is only as good as the data shape you feed it.

---

## 2. Streamlit Native Charts

Streamlit provides four simple chart types that work with minimal setup. They accept DataFrames directly.

### st.line_chart — Trends Over Time

```python
import streamlit as st
import pandas as pd
import numpy as np

# Line charts show trends — ideal for time series
dates = pd.date_range("2026-01-01", periods=30, freq="D")
df = pd.DataFrame({
    "Date": dates,
    "Revenue": np.random.randint(30000, 60000, 30).cumsum(),
    "Users": np.random.randint(100, 500, 30).cumsum(),
})

# Simple — pass DataFrame with numeric columns
st.line_chart(df.set_index("Date")[["Revenue", "Users"]])
```

**When to use:** Time series, trends, comparisons over a continuous variable.

### st.bar_chart — Categories & Comparisons

```python
# Bar charts show discrete categories
product_sales = df.groupby("Product")["Revenue"].sum().sort_values(ascending=False)
st.bar_chart(product_sales)
```

**When to use:** Comparing values across categories, ranking, distribution of categorical data.

### st.area_chart — Volume & Proportion

```python
# Area charts show volume — like line charts but filled
st.area_chart(df.set_index("Date")[["Revenue", "Users"]])
```

**When to use:** Cumulative totals, stacked comparisons, volume over time.

### st.scatter_chart — Relationships

```python
# Scatter charts show relationships between two variables
np.random.seed(42)
scatter_df = pd.DataFrame({
    "Budget": np.random.randint(10000, 100000, 50),
    "Revenue": np.random.randint(15000, 120000, 50),
    "Rating": np.random.uniform(1, 5, 50),
})

st.scatter_chart(scatter_df, x="Budget", y="Revenue", color="Rating")
```

**When to use:** Correlations, distributions, identifying outliers, clustering.

### Native Charts — Limitations

| Feature | Native Charts | Matplotlib/Plotly |
|---|---|---|
| Setup complexity | Zero — just pass a DataFrame | Requires creating figure objects |
| Customization | Limited (no titles, axis labels) | Full control |
| Interactivity | Basic hover/zoom | Rich tooltips, animations |
| Multiple series | Automatic | Manual |
| Best for | Quick exploration | Polished presentations |

> **Rule of thumb:** Use native charts for **quick exploration** during development. Use Matplotlib/Plotly for **polished dashboards** where titles, labels, and styling matter.

---

## 3. Matplotlib Integration — st.pyplot

Matplotlib is the most widely used Python plotting library. Streamlit renders Matplotlib figures directly.

### Basic Usage

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.plot([1, 2, 3, 4], [10, 20, 25, 30])
ax.set_title("Simple Line Plot")
ax.set_xlabel("X")
ax.set_ylabel("Y")

st.pyplot(fig)
```

### With Pandas

```python
fig, ax = plt.subplots(figsize=(10, 5))
df.plot(x="Date", y="Revenue", ax=ax, title="Revenue Over Time")
st.pyplot(fig)
```

### Multiple Subplots

```python
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

axes[0].bar(["A", "B", "C"], [10, 20, 15])
axes[0].set_title("Bar Chart")

axes[1].hist(np.random.randn(100), bins=20)
axes[1].set_title("Histogram")

plt.tight_layout()
st.pyplot(fig)
```

### Histograms & Distributions

```python
fig, ax = plt.subplots()
ax.hist(df["Revenue"], bins=30, edgecolor="black", alpha=0.7)
ax.set_title("Revenue Distribution")
ax.set_xlabel("Revenue ($)")
ax.set_ylabel("Frequency")
st.pyplot(fig)
```

### Seaborn Integration

```python
import seaborn as sns

fig, ax = plt.subplots(figsize=(8, 6))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm", ax=ax)
ax.set_title("Correlation Matrix")
st.pyplot(fig)
```

---

## 4. Plotly Integration — st.plotly_chart

Plotly creates **interactive** charts with tooltips, zoom, pan, and export. It's the go-to for polished dashboards.

### Basic Usage

```python
import plotly.express as px

fig = px.line(df, x="Date", y="Revenue", title="Revenue Trend")
st.plotly_chart(fig, use_container_width=True)
```

> **Always use `use_container_width=True`** — it makes the chart fill the available width.

### Bar Chart with Plotly

```python
fig = px.bar(
    df, x="Region", y="Revenue", color="Product",
    title="Revenue by Region and Product",
    barmode="group"
)
st.plotly_chart(fig, use_container_width=True)
```

### Scatter Plot with Trendline

```python
fig = px.scatter(
    df, x="Budget", y="Revenue",
    color="Rating", size="Rating",
    trendline="ols",
    title="Budget vs Revenue"
)
st.plotly_chart(fig, use_container_width=True)
```

### Histogram

```python
fig = px.histogram(df, x="Revenue", nbins=30, title="Revenue Distribution")
st.plotly_chart(fig, use_container_width=True)
```

### Box Plot

```python
fig = px.box(df, x="Region", y="Revenue", color="Region", title="Revenue by Region")
st.plotly_chart(fig, use_container_width=True)
```

### Sunburst / Treemap

```python
fig = px.sunburst(df, path=["Region", "Product"], values="Revenue",
                  title="Revenue Hierarchy")
st.plotly_chart(fig, use_container_width=True)
```

### Plotly vs Matplotlib

| Feature | Matplotlib | Plotly |
|---|---|---|
| Interactivity | Static (PNG) | Hover, zoom, pan, export |
| Setup | `fig, ax = plt.subplots()` | `px.figure()` or `go.Figure()` |
| Learning curve | Steeper | gentler with `plotly.express` |
| File size | Small (raster) | Larger (JavaScript) |
| Best for | Quick analysis, publications | Interactive dashboards, web |

---

## 5. Choosing the Right Chart

### The Chart Selection Matrix

| Question | Chart Type | Streamlit Call |
|---|---|---|
| How does X change over time? | Line | `st.line_chart()` or `px.line()` |
| How do categories compare? | Bar | `st.bar_chart()` or `px.bar()` |
| What is the distribution of X? | Histogram | `px.histogram()` or `plt.hist()` |
| Is there a relationship between X and Y? | Scatter | `st.scatter_chart()` or `px.scatter()` |
| How do parts relate to a whole? | Pie / Treemap | `px.pie()` or `px.treemap()` |
| What are the outliers? | Box plot | `px.box()` |
| How does X vary by group? | Grouped bar / Box | `px.bar(barmode="group")` or `px.box()` |
| What is the correlation? | Heatmap | `sns.heatmap()` |

### The Decision Flowchart

```
What are you showing?
│
├── Time series → Line chart
│
├── Categories
│   ├── Compare values → Bar chart
│   ├── Parts of whole → Pie / Treemap
│   └── Distribution → Histogram
│
├── Relationships
│   ├── Two numeric → Scatter
│   └── Many numeric → Heatmap
│
├── Distributions
│   ├── Single variable → Histogram
│   └── By group → Box plot / Violin
│
└── Geographic → Map (st.map / px.scatter_mapbox)
```

---

## 6. Interactive Visualization Patterns

### Pattern 1: User-Selected Chart Type

```python
chart_type = st.selectbox("Chart type", ["Line", "Bar", "Scatter", "Area"])

if chart_type == "Line":
    st.line_chart(data)
elif chart_type == "Bar":
    st.bar_chart(data)
elif chart_type == "Scatter":
    st.scatter_chart(data)
else:
    st.area_chart(data)
```

### Pattern 2: Plotly with Sidebar Controls

```python
with st.sidebar:
    chart_title = st.text_input("Chart title", "Revenue Analysis")
    color_by = st.selectbox("Color by", ["Region", "Product"])
    show_trend = st.checkbox("Show trendline")

fig = px.bar(df, x="Region", y="Revenue", color=color_by, title=chart_title)
if show_trend:
    fig = px.scatter(df, x="Region", y="Revenue", color=color_by,
                     trendline="ols", title=chart_title)
st.plotly_chart(fig, use_container_width=True)
```

### Pattern 3: Side-by-Side Comparison

```python
col1, col2 = st.columns(2)

with col1:
    st.subheader("This Year")
    fig1 = px.bar(this_year, x="Month", y="Revenue")
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    st.subheader("Last Year")
    fig2 = px.bar(last_year, x="Month", y="Revenue")
    st.plotly_chart(fig2, use_container_width=True)
```

### Pattern 4: Dynamic Data Transformations

```python
# Let user choose aggregation
agg_func = st.selectbox("Aggregation", ["Sum", "Mean", "Median", "Count"])

agg_map = {"Sum": "sum", "Mean": "mean", "Median": "median", "Count": "count"}
result = df.groupby("Region")["Revenue"].agg(agg_map[agg_func]).reset_index()

st.bar_chart(result.set_index("Region")["Revenue"])
```

---

## 7. Readable Dashboard Visualization

### Labels and Titles

```python
# ❌ No title, no labels
st.line_chart(df[["Revenue"]])

# ✅ Clear context
st.subheader("Monthly Revenue Trend")
st.line_chart(df.set_index("Date")[["Revenue"]])
```

### Color and Contrast

```python
# Use consistent, accessible colors
fig = px.bar(df, x="Region", y="Revenue",
             color_discrete_sequence=["#4ecdc4", "#ff6b6b", "#45b7d1", "#96ceb4"])
```

### Avoid Chart Junk

```python
# ❌ Too many elements
fig = px.scatter(df, x="a", y="b", text="label", size="c", color="d",
                 symbol="e", trendline="ols", marginal_x="histogram",
                 marginal_y="box")  # Overwhelming

# ✅ Focused
fig = px.scatter(df, x="budget", y="revenue", color="region",
                 title="Budget vs Revenue by Region")
```

### Consistent Scales

```python
# When comparing charts, keep the same scale
fig1 = px.bar(data1, x="Category", y="Revenue")
fig2 = px.bar(data2, x="Category", y="Revenue")
fig1.update_yaxes(range=[0, 100000])
fig2.update_yaxes(range=[0, 100000])
```

---

## 8. Common Visualization Mistakes

### Mistake 1: Pie Charts for Too Many Categories

```python
# ❌ 15 slices — unreadable
fig = px.pie(df, names="Category", values="Revenue")

# ✅ Group small categories into "Other"
top_n = df.nlargest(5, "Revenue")
other = pd.DataFrame({"Category": ["Other"], "Revenue": [df[~df.index.isin(top_n.index)]["Revenue"].sum()]})
chart_df = pd.concat([top_n, other])
fig = px.pie(chart_df, names="Category", values="Revenue")
```

### Mistake 2: Line Charts for Non-Sequential Data

```python
# ❌ Line chart for categorical data
st.line_chart(region_sales)  # Implies continuity between categories

# ✅ Bar chart for categories
st.bar_chart(region_sales)
```

### Mistake 3: No Axis Labels

```python
# ❌ Generic
fig = px.scatter(df, x="x", y="y")

# ✅ Descriptive
fig = px.scatter(df, x="Marketing Budget ($)", y="Revenue ($)",
                 title="Marketing ROI Analysis")
```

### Mistake 4: Misleading Y-Axis

```python
# ❌ Y-axis starting at non-zero makes differences look bigger
fig = px.bar(df, x="Category", y="Revenue")
fig.update_yaxes(range=[50000, 70000])  # Misleading

# ✅ Start from zero for bar charts
fig = px.bar(df, x="Category", y="Revenue")
fig.update_yaxes(range=[0, None])  # Honest
```

---

## 9. The Visualization Workflow

Here's the complete workflow for turning raw data into a meaningful visualization:

```
1. ASK: What question am I answering?
2. SHAPE: Filter, aggregate, transform data for that question
3. CHOOSE: Pick the chart type that best shows the answer
4. RENDER: Use the appropriate Streamlit call
5. LABEL: Add titles, axis labels, context
6. INTERACT: Add filters for user exploration
```

### Example: "Which region has the highest revenue?"

```python
# 1. Question: Regional revenue comparison
# 2. Shape: Aggregate by region
region_revenue = df.groupby("Region")["Revenue"].sum().reset_index()

# 3. Choose: Bar chart (categorical comparison)
# 4. Render
fig = px.bar(region_revenue, x="Region", y="Revenue", color="Region",
             title="Revenue by Region")

# 5. Label
fig.update_layout(xaxis_title="Region", yaxis_title="Total Revenue ($)")

# 6. Interact
st.plotly_chart(fig, use_container_width=True)
```

---

## Key Takeaways

- **Native charts** (`st.line_chart`, `st.bar_chart`, etc.) are for **quick exploration** — zero setup.
- **Matplotlib** (`st.pyplot`) is for **static, publication-quality** figures.
- **Plotly** (`st.plotly_chart`) is for **interactive dashboards** — always use `use_container_width=True`.
- **Choose the chart type** based on the question: trends→line, categories→bar, distribution→histogram, relationships→scatter.
- **Transform before you visualize** — the data shape determines the chart's effectiveness.
- **Label everything** — titles, axis labels, context. Never assume the user knows what they're looking at.
- **Avoid chart junk** — fewer elements, cleaner insight.

---

## Further Reading

- [Streamlit Chart Elements](https://docs.streamlit.io/develop/api-reference/charts)
- [st.plotly_chart Reference](https://docs.streamlit.io/develop/api-reference/charts/st.plotly_chart)
- [st.pyplot Reference](https://docs.streamlit.io/develop/api-reference/charts/st.pyplot)
- [Plotly Express Documentation](https://plotly.com/python/plotly-express/)
- [Matplotlib Tutorials](https://matplotlib.org/stable/tutorials/index.html)

---

## Related Materials

- 📖 Reading: [07 — Data Display: DataFrames, Tables & Pandas Integration](07_data_display_dataframes.md)
- 📓 Notebook: [07 — DataFrames, Tables & Pandas Integration](../notebooks/07_dataframes_tables_pandas.ipynb)
- 📓 Notebook: [08 — Interactive Visualization & Chart Selection](../notebooks/08_interactive_visualization.ipynb)
- ✏️ Exercise: [07 — Data Display Challenges](../exercises/07_data_display_challenges.py)
- ✏️ Exercise: [08 — Visualization Workshop](../exercises/08_visualization_workshop.py)
- 🖥️ Demo App: [07 — Data Display Demo](../apps/07_data_display_demo.py)
- 📝 Quiz: [04 — DataFrames & Visualization](../quizzes/04_dataframes_visualization.md)
