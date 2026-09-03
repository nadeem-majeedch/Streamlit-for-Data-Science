# 07 — Data Display: DataFrames, Tables & Pandas Integration

> **📖 Reading · Module 04 · Intermediate**
> *The bridge between raw data and human understanding.*

---

## Learning Objectives

After completing this reading you will be able to:

- Use `st.dataframe` with `column_config`, `column_order`, and `hide_index` to display interactive tables.
- Choose between `st.dataframe`, `st.table`, `st.write`, and `st.data_editor` for different use cases.
- Format numbers, currency, and dates using `st.column_config` types.
- Apply Pandas `Styler` formatting within `st.dataframe`.
- Filter and transform DataFrames before displaying them in Streamlit.
- Select the right display method based on data size, interactivity needs, and audience.

---

## 1. The Display Spectrum

Streamlit offers multiple ways to show tabular data. Each sits at a different point on the interactivity spectrum:

```
Static                                              Interactive
─────────────────────────────────────────────────────────────────
st.table()    st.write()    st.dataframe()    st.data_editor()
   │              │               │                   │
   ▼              ▼               ▼                   ▼
 HTML table   Auto-detect   Sortable, scrollable   Editable cells
 No scroll    No control    Column resize           Add/delete rows
 Fixed        Simple        Row selection           Download CSV
```

### When to Use Each

| Method | Best For | Limitations |
|---|---|---|
| `st.table(df)` | Small datasets (< 20 rows), static display | No scrolling, no interaction |
| `st.write(df)` | Quick debugging, simple output | No formatting control |
| `st.dataframe(df)` | **Primary choice** for displaying data | Read-only |
| `st.data_editor(df)` | Editable tables, data entry | Adds complexity, user modifies data |
| `st.json(obj)` | Nested dicts, API responses, config | Not tabular |

> **Rule of thumb:** Start with `st.dataframe()`. Switch to `st.table()` only for very small, static tables. Use `st.data_editor()` only when the user needs to modify data.

---

## 2. st.dataframe — The Primary Display Tool

`st.dataframe` renders an interactive table with sorting, scrolling, column resizing, and optional row selection.

### Basic Usage

```python
import streamlit as st
import pandas as pd

df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie", "Diana"],
    "Score": [92, 87, 78, 95],
    "Grade": ["A", "B+", "C+", "A+"]
})

st.dataframe(df)
```

### Width Control

```python
# Match parent container width (default)
st.dataframe(df, width="stretch")

# Fit to content width
st.dataframe(df, width="content")

# Fixed pixel width
st.dataframe(df, width=600)
```

### Height Control

```python
# Show ~10 rows with scrolling (default)
st.dataframe(df, height="auto")

# Show all content (capped at 10,000px)
st.dataframe(df, height="content")

# Fill available vertical space
st.dataframe(df, height="stretch")

# Fixed height in pixels
st.dataframe(df, height=400)
```

### Hide the Index

```python
# Let Streamlit decide (default — hides numeric index)
st.dataframe(df, hide_index=True)
```

### Column Order

```python
# Show only specific columns in a specific order
st.dataframe(df, column_order=["Name", "Grade", "Score"])
```

---

## 3. Column Configuration — Formatting & Types

`column_config` is how you control **how each column looks and behaves**. It's the most powerful feature of `st.dataframe`.

### Available Column Types

| Type | Use For | Example |
|---|---|---|
| `TextColumn` | Strings, names, descriptions | `"Alice"` |
| `NumberColumn` | Numeric values with formatting | `"$1,234.56"` |
| `PercentColumn` | Percentage values | `"45.2%"` |
| `CurrencyColumn` | Currency with symbol | `"$1,234.56"` |
| `DateColumn` | Date values | `"Jan 15, 2026"` |
| `DatetimeColumn` | Date + time | `"2026-01-15 14:30"` |
| `TimeColumn` | Time only | `"14:30:00"` |
| `CheckboxColumn` | Boolean checkboxes | `☑️` |
| `ProgressColumn` | Progress bars | `████████░░ 80%` |
| `ImageColumn` | Thumbnail images | `<img>` |
| `LinkColumn` | Clickable URLs | `<a href>` |
| `ListColumn` | Comma-separated lists | `"a, b, c"` |
| `JsonColumn` | JSON display | `{"key": "val"}` |
| `BarChartColumn` | Inline bar charts | `▁▃▅▇` |

### Formatting Numbers

```python
st.dataframe(
    df,
    column_config={
        "Score": st.column_config.NumberColumn(
            "Student Score",
            help="Score out of 100",
            format="%d",
            min_value=0,
            max_value=100,
        ),
    }
)
```

### Currency Formatting

```python
st.dataframe(
    df,
    column_config={
        "Revenue": st.column_config.NumberColumn(
            "Revenue",
            format="$ %d",
        ),
    }
)
```

### Percentage Formatting

```python
st.dataframe(
    df,
    column_config={
        "Conversion": st.column_config.PercentColumn(
            "Conversion Rate",
            format="%.1f%%",
        ),
    }
)
```

### Date Formatting

```python
st.dataframe(
    df,
    column_config={
        "Date": st.column_config.DateColumn(
            "Report Date",
            format="MMM D, YYYY",
        ),
    }
)
```

### Hiding Columns

```python
st.dataframe(
    df,
    column_config={
        "internal_id": None,  # Hide this column
        "Name": st.column_config.TextColumn("Student Name"),
    }
)
```

---

## 4. Row Selection — Making DataFrames Interactive

`st.dataframe` can return **selected rows** when users click on them.

```python
selected = st.dataframe(
    df,
    on_select="rerun",
    selection_mode="multi-row",
)

# selected is a dict with "selection" key
if selected and selected["selection"]["rows"]:
    selected_rows = df.iloc[selected["selection"]["rows"]]
    st.write("Selected:", selected_rows)
```

### Selection Modes

| Mode | Behavior |
|---|---|
| `"multi-row"` | Click multiple rows (default) |
| `"single-row"` | Click one row at a time |
| `"single-row-required"` | Always one row selected (radio-like) |
| `"multi-column"` | Select entire columns |
| `"single-column"` | Select one column |
| `"multi-cell"` | Select rectangular cell ranges |

---

## 5. st.table — Static Display

`st.table` renders a fixed HTML table. No scrolling, no interaction — just a clean snapshot.

```python
# Good for small summaries
summary = df.describe()
st.table(summary)
```

**When to use:** Summary statistics, small reference tables (< 20 rows), data that doesn't need scrolling.

---

## 6. Pandas Styler Integration

`st.dataframe` can display `pandas.Styler` objects for rich formatting:

```python
# Color-code scores
def color_scores(val):
    if val >= 90:
        return "background-color: #c6efce; color: #006100"
    elif val >= 80:
        return "background-color: #ffeb9c; color: #9c6500"
    else:
        return "background-color: #ffc7ce; color: #9c0006"

styled = df.style.applymap(color_scores, subset=["Score"])
st.dataframe(styled)
```

### Bar Charts in Styler

```python
styled = df.style.bar(subset=["Score"], color="#4ecdc4", vmin=0, vmax=100)
st.dataframe(styled)
```

### Gradient Coloring

```python
styled = df.style.background_gradient(cmap="RdYlGn", subset=["Score"])
st.dataframe(styled)
```

> **Note:** `st.dataframe` with Styler supports custom cell values, colors, and font weights. It does NOT support hovering, captions, or some exotic styling options. For those, use `column_config` instead.

---

## 7. Filtering Data Before Display

The most common pattern in a Streamlit app: **filter data → display results**.

### Pattern 1: Sidebar Filters

```python
# Sidebar controls
category = st.sidebar.selectbox("Category", ["All"] + df["Category"].unique().tolist())
min_value = st.sidebar.slider("Min Value", 0, 100, 0)

# Apply filters
filtered = df.copy()
if category != "All":
    filtered = filtered[filtered["Category"] == category]
filtered = filtered[filtered["Value"] >= min_value]

# Display
st.dataframe(filtered)
```

### Pattern 2: Multi-Select Filters

```python
categories = st.sidebar.multiselect(
    "Categories",
    options=df["Category"].unique(),
    default=df["Category"].unique().tolist()
)

# Filter
filtered = df[df["Category"].isin(categories)]
```

### Pattern 3: Date Range Filters

```python
date_range = st.sidebar.date_input(
    "Date range",
    value=(df["Date"].min(), df["Date"].max())
)

if isinstance(date_range, tuple) and len(date_range) == 2:
    filtered = df[
        (df["Date"] >= pd.Timestamp(date_range[0]))
        & (df["Date"] <= pd.Timestamp(date_range[1]))
    ]
```

### Pattern 4: Text Search

```python
search = st.sidebar.text_input("Search names")
if search:
    filtered = df[df["Name"].str.contains(search, case=False, na=False)]
```

---

## 8. Transforming Data Before Display

### Aggregation

```python
# Group and aggregate
region_summary = df.groupby("Region").agg({
    "Revenue": "sum",
    "Orders": "count",
    "Rating": "mean"
}).reset_index()

st.dataframe(region_summary)
```

### Sorting

```python
sort_by = st.selectbox("Sort by", ["Revenue", "Orders", "Rating"])
ascending = st.checkbox("Ascending")
st.dataframe(df.sort_values(sort_by, ascending=ascending))
```

### Computed Columns

```python
# Add derived columns before display
display_df = df.copy()
display_df["Profit Margin"] = (display_df["Revenue"] - display_df["Cost"]) / display_df["Revenue"]
display_df["Revenue per Order"] = display_df["Revenue"] / display_df["Orders"]

st.dataframe(display_df[["Name", "Revenue", "Profit Margin", "Revenue per Order"]])
```

### Pivot Tables

```python
pivot = df.pivot_table(
    values="Revenue",
    index="Region",
    columns="Product",
    aggfunc="sum",
    fill_value=0
)
st.dataframe(pivot)
```

---

## 9. Displaying Data Science Datasets

### The Titanic Dataset Pattern

```python
@st.cache_data
def load_titanic():
    return pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")

df = load_titanic()

# Select columns of interest
display_cols = ["Name", "Age", "Sex", "Pclass", "Survived", "Fare"]
st.dataframe(
    df[display_cols],
    column_config={
        "Fare": st.column_config.NumberColumn("Fare (£)", format="$%.2f"),
        "Age": st.column_config.NumberColumn("Age", format="%.0f"),
        "Survived": st.column_config.CheckboxColumn("Survived"),
    },
    hide_index=True,
    height=400,
)
```

### The Iris Dataset Pattern

```python
from sklearn.datasets import load_iris

iris = load_iris(as_frame=True)
df = iris.frame
df["species"] = df["target"].map({0: "setosa", 1: "versicolor", 2: "virginica"})

st.dataframe(
    df,
    column_config={
        "sepal length (cm)": st.column_config.NumberColumn("Sepal Length", format="%.1f cm"),
        "petal length (cm)": st.column_config.NumberColumn("Petal Length", format="%.1f cm"),
    },
    hide_index=True,
)
```

---

## 10. Common Mistakes

### Mistake 1: Using st.write for Tables

```python
# ❌ No formatting control
st.write(df)

# ✅ Interactive table with formatting
st.dataframe(df, column_config={...})
```

### Mistake 2: Not Using hide_index for Clean Tables

```python
# ❌ Clunky numeric index
st.dataframe(df)

# ✅ Clean display
st.dataframe(df, hide_index=True)
```

### Mistake 3: Displaying Raw Large DataFrames

```python
# ❌ 100,000 rows — overwhelming
st.dataframe(huge_df)

# ✅ Filter, aggregate, or paginate
filtered = huge_df[huge_df["Year"] == 2026]
st.dataframe(filtered)
```

### Mistake 4: Ignoring Column Config

```python
# ❌ Ugly number formatting
st.dataframe(df)  # Shows: 1234567.891234

# ✅ Formatted display
st.dataframe(df, column_config={
    "Revenue": st.column_config.NumberColumn("Revenue", format="$%,.2f")
})
```

---

## Key Takeaways

- **`st.dataframe()` is the primary tool** for displaying tabular data — interactive, sortable, scrollable.
- **`column_config`** gives you full control over formatting, types, and visibility.
- **Always `hide_index=True`** for clean presentation.
- **Filter before display** — sidebar controls → filtered DataFrame → `st.dataframe()`.
- **Transform for clarity** — aggregate, sort, add computed columns.
- **`st.table()` is for tiny static tables only** — use `st.dataframe()` by default.
- **Pandas Styler works** with `st.dataframe` for conditional formatting.
- **Row selection** makes DataFrames interactive — use `on_select="rerun"`.

---

## Further Reading

- [st.dataframe API Reference](https://docs.streamlit.io/develop/api-reference/data/st.dataframe)
- [st.column_config API Reference](https://docs.streamlit.io/develop/api-reference/data/st.column_config)
- [Dataframes Guide](https://docs.streamlit.io/develop/concepts/design/dataframes)
- [Pandas Styler Documentation](https://pandas.pydata.org/docs/user_guide/style.html)

---

## Related Materials

- 📖 Reading: [08 — Visualization with Streamlit, Matplotlib & Plotly](08_visualization_matplotlib_plotly.md)
- 📓 Notebook: [07 — DataFrames, Tables & Pandas Integration](../notebooks/07_dataframes_tables_pandas.ipynb)
- 📓 Notebook: [08 — Interactive Visualization & Chart Selection](../notebooks/08_interactive_visualization.ipynb)
- ✏️ Exercise: [07 — Data Display Challenges](../exercises/07_data_display_challenges.py)
- 🖥️ Demo App: [07 — Data Display Demo](../apps/07_data_display_demo.py)
- 📝 Quiz: [04 — DataFrames & Visualization](../quizzes/04_dataframes_visualization.md)
