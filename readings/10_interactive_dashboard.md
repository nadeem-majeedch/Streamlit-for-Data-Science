# 10 — Building Interactive Data Science Dashboards

> **📖 Reading · Module 06 · Intermediate**
> *Transform a Jupyter notebook into a production-quality interactive application.*

---

## Learning Objectives

After completing this reading you will be able to:

- Design a dashboard architecture that separates data processing from presentation.
- Build filter panels that update all dashboard components reactively.
- Create KPI metric rows that communicate insights at a glance.
- Combine charts, tables, and controls into a cohesive layout.
- Apply progressive disclosure to manage information density.
- Implement user feedback for loading states, errors, and empty results.
- Avoid the most common dashboard design mistakes.

---

## 1. From Notebook to Dashboard — The Architecture Shift

A Jupyter notebook is a **linear narrative** for one analyst. A Streamlit dashboard is an **interactive application** for many users.

### The Core Principle: Separate Processing from Presentation

```
┌─────────────────────────────────────────────────────┐
│                   DATA LAYER                         │
│  Load → Clean → Transform → Aggregate → Cache       │
│  (Pure Python — no Streamlit calls here)             │
└─────────────────────────┬───────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────┐
│                 PRESENTATION LAYER                   │
│  Sidebar controls → KPIs → Charts → Tables → Export  │
│  (Streamlit widgets + display calls)                 │
└─────────────────────────────────────────────────────┘
```

**Why this matters:**
- The data layer can be tested independently.
- The presentation layer can be redesigned without touching data logic.
- Multiple presentation layers can share the same data functions.

### The Dashboard Flow

```
USER ACTION (filter, sort, click)
        │
        ▼
SIDEBAR WIDGETS produce filter values
        │
        ▼
DATA LAYER: load_data() → filter_data() → aggregate()
        │
        ▼
SESSION STATE: cache filtered results
        │
        ▼
PRESENTATION: KPIs → Charts → Tables → Download
```

---

## 2. Dashboard Architecture — A Practical Blueprint

### Folder Structure

For a project larger than a single file:

```
dashboard/
├── app.py                 # Entry point — only Streamlit UI calls
├── data.py                # Data loading, cleaning, transformation
├── charts.py              # Chart-building functions (Plotly/Matplotlib)
├── utils.py               # Formatting helpers, constants
└── requirements.txt       # Dependencies
```

### The Single-File Pattern (For Smaller Dashboards)

When everything fits in one file, organize with clear sections:

```python
# ═══════════════════════════════════════════════════════
# SECTION 1: Imports & Configuration
# ═══════════════════════════════════════════════════════
import streamlit as st
import pandas as pd

# ═══════════════════════════════════════════════════════
# SECTION 2: Data Functions (no Streamlit calls!)
# ═══════════════════════════════════════════════════════
@st.cache_data
def load_data():
    ...

def filter_data(df, region, category, date_range):
    ...

def compute_kpis(df):
    ...

# ═══════════════════════════════════════════════════════
# SECTION 3: Page Layout
# ═══════════════════════════════════════════════════════
st.set_page_config(...)

# ═══════════════════════════════════════════════════════
# SECTION 4: Sidebar Controls
# ═══════════════════════════════════════════════════════
with st.sidebar:
    ...

# ═══════════════════════════════════════════════════════
# SECTION 5: Main Content
# ═══════════════════════════════════════════════════════
# KPI Row
# Charts
# Tables
# Footer
```

---

## 3. Filters — The User's Control Panel

### Filter Placement

Filters **always** go in the sidebar. Never in the main content area.

```python
with st.sidebar:
    st.header("🔍 Filters")

    # Date range
    date_range = st.date_input(
        "Date range",
        value=(df["date"].min(), df["date"].max()),
    )

    # Categorical
    region = st.multiselect(
        "Region",
        options=df["region"].unique(),
        default=df["region"].unique(),
    )

    # Numeric
    min_revenue = st.slider(
        "Minimum revenue",
        min_value=0,
        max_value=int(df["revenue"].max()),
        value=0,
        step=1000,
    )
```

### Filter Types and When to Use Them

| Widget | Best For | Example |
|---|---|---|
| `st.selectbox` | Single selection from small list | Country, Status |
| `st.multiselect` | Multiple selections | Regions, Categories |
| `st.slider` | Numeric range | Revenue, Age |
| `st.date_input` | Date range | Order date, Report date |
| `st.radio` | Binary or few options | View mode, Sort order |
| `st.checkbox` | Toggle features | Show outliers, Raw data |
| `st.text_input` | Free text search | Product name, Customer ID |

### Applying Filters Safely

```python
# Start with full data
filtered = df.copy()

# Apply each filter only if it has a value
if selected_regions:
    filtered = filtered[filtered["region"].isin(selected_regions)]

if min_revenue > 0:
    filtered = filtered[filtered["revenue"] >= min_revenue]

if date_range and len(date_range) == 2:
    start, end = pd.Timestamp(date_range[0]), pd.Timestamp(date_range[1])
    filtered = filtered[(filtered["date"] >= start) & (filtered["date"] <= end)]
```

### Handling Empty Results

```python
if filtered.empty:
    st.warning("No data matches your filters. Try adjusting the criteria.")
    st.stop()  # Don't render the rest of the dashboard
```

---

## 4. KPI Metrics — Lead with Insights

### The 4-Card Pattern

```python
total_revenue = filtered["revenue"].sum()
total_orders = filtered["orders"].sum()
avg_order_value = total_revenue / total_orders if total_orders > 0 else 0
unique_customers = filtered["customer_id"].nunique()

c1, c2, c3, c4 = st.columns(4)
c1.metric("Total Revenue", f"${total_revenue:,.0f}", icon="💰")
c2.metric("Total Orders", f"{total_orders:,}", icon="📦")
c3.metric("Avg Order Value", f"${avg_order_value:,.2f}", icon="🛒")
c4.metric("Unique Customers", f"{unique_customers:,}", icon="👥")
```

### Delta Values

```python
# Compare current vs previous period
current = filtered["revenue"].sum()
previous = previous_period_df["revenue"].sum()
delta = current - previous
delta_pct = (delta / previous * 100) if previous > 0 else 0

c1.metric(
    "Total Revenue",
    f"${current:,.0f}",
    f"{delta_pct:+.1f}%",
    delta_color="normal",  # Green if positive
)
```

### KPI Design Rules

1. **4 metrics per row** — this is the standard layout
2. **Short labels** — "Revenue" not "Total Revenue This Quarter"
3. **Deltas tell the story** — users scan deltas to find problems
4. **Format numbers** — "$1.2M" not "1200000"
5. **Group related metrics** — revenue together, user metrics together

---

## 5. Charts — Visual Storytelling

### Chart Selection Guide

| Question | Chart Type | Streamlit Call |
|---|---|---|
| How does X change over time? | Line | `st.line_chart()` or Plotly |
| How do categories compare? | Bar | `st.bar_chart()` or Plotly |
| What is the distribution? | Histogram | Plotly `px.histogram()` |
| Is there a relationship? | Scatter | `st.scatter_chart()` or Plotly |
| How does X vary by group? | Box/Violin | Plotly `px.box()` |

### Plotly for Rich Charts

```python
import plotly.express as px

# Revenue trend
fig = px.line(
    daily_revenue,
    x="date",
    y="revenue",
    color="region",
    title="Daily Revenue by Region",
    labels={"revenue": "Revenue ($)", "date": "Date"},
)
fig.update_layout(height=400)
st.plotly_chart(fig, use_container_width=True)
```

### Consistent Styling

Define a color palette once and reuse it:

```python
COLORS = {
    "primary": "#FF4B4B",
    "secondary": "#4ECDC4",
    "accent": "#45B7D1",
    "warning": "#F7DC6F",
    "danger": "#E74C3C",
}

# Use in Plotly
fig = px.bar(data, color_discrete_map=COLORS)
```

---

## 6. Tables — Structured Data Display

### st.dataframe for Interactive Tables

```python
st.dataframe(
    filtered.sort_values("revenue", ascending=False),
    use_container_width=True,
    hide_index=True,
    column_config={
        "revenue": st.column_config.NumberColumn("Revenue", format="$%,.0f"),
        "date": st.column_config.DateColumn("Date", format="MMM DD, YYYY"),
        "region": st.column_config.TextColumn("Region"),
    },
    height=400,
)
```

### Conditional Formatting

```python
def highlight_revenue(val):
    """Color-code revenue values."""
    if val >= 10000:
        return "background-color: #d4edda; color: #155724"
    elif val >= 5000:
        return "background-color: #fff3cd; color: #856404"
    else:
        return "background-color: #f8d7da; color: #721c24"

styled = filtered[["product", "revenue", "orders"]].style.applymap(
    highlight_revenue, subset=["revenue"]
)
st.dataframe(styled, use_container_width=True)
```

---

## 7. Layout — Spatial Organization

### The Standard Dashboard Layout

```
┌──────────────────────────────────────────────────┐
│ Sidebar              │  Main Content              │
│                      │                             │
│ Filters              │  Title + Subtitle           │
│   - Date range       │                             │
│   - Category         │  [KPI] [KPI] [KPI] [KPI]   │
│   - Region           │                             │
│                      │  ┌──────────┬──────────┐   │
│ Settings             │  │ Chart 1  │ Chart 2  │   │
│   - Chart type       │  │ (60%)    │ (40%)    │   │
│   - Sort by          │  └──────────┴──────────┘   │
│                      │                             │
│ Export               │  ┌─────────────────────┐   │
│   - CSV button       │  │ Data Table (expander)│   │
│                      │  └─────────────────────┘   │
│                      │                             │
│                      │  Footer: Source, timestamp  │
└──────────────────────────────────────────────────┘
```

### Column Ratios

```python
# Unequal split — main chart + side panel
main_col, side_col = st.columns([2, 1])

# Equal split
left, right = st.columns(2)

# Three columns for KPIs
c1, c2, c3, c4 = st.columns(4)
```

### Tabs for Views

```python
tab_overview, tab_details, tab_export = st.tabs(
    ["📊 Overview", "🔍 Details", "📥 Export"]
)

with tab_overview:
    # Main charts and KPIs
    ...

with tab_details:
    # Data table with sorting
    ...

with tab_export:
    # Download buttons
    ...
```

### Expanders for Progressive Disclosure

```python
with st.expander("📈 Summary Statistics", expanded=False):
    st.dataframe(filtered.describe(), use_container_width=True)

with st.expander("📋 Raw Data", expanded=False):
    st.dataframe(filtered, use_container_width=True)
```

---

## 8. User Feedback — Communicating State

### Loading States

```python
# For known-duration tasks
progress = st.progress(0, text="Processing...")
for i in range(100):
    time.sleep(0.01)
    progress.progress(i + 1, text=f"Processing... {i+1}%")
progress.empty()

# For quick tasks
with st.spinner("Loading data..."):
    df = load_data()
```

### Status Messages

```python
# Success
st.success("Dashboard loaded successfully!")

# Info
st.info("Showing data from Jan 2025 to Dec 2025")

# Warning
st.warning("No data matches current filters")

# Error
st.error("Failed to load data. Please try again.")
```

### Empty States

```python
if filtered.empty:
    st.info(
        "🔍 **No results found**\n\n"
        "Try adjusting your filters or date range."
    )
    # Optionally show what filters are active
    with st.expander("Active Filters"):
        st.write(f"- Regions: {selected_regions}")
        st.write(f"- Min Revenue: ${min_revenue:,}")
    st.stop()
```

---

## 9. Data Transformation — Separation of Concerns

### Pure Functions (No Streamlit Calls)

```python
def load_data() -> pd.DataFrame:
    """Load raw data. Cache with @st.cache_data."""
    return pd.read_csv("data/sales.csv")

def filter_data(
    df: pd.DataFrame,
    regions: list[str],
    categories: list[str],
    min_revenue: float,
) -> pd.DataFrame:
    """Apply filters. Pure function — no st.* calls."""
    result = df.copy()

    if regions:
        result = result[result["region"].isin(regions)]
    if categories:
        result = result[result["category"].isin(categories)]
    if min_revenue > 0:
        result = result[result["revenue"] >= min_revenue]

    return result

def compute_kpis(df: pd.DataFrame) -> dict:
    """Compute KPI values. Returns a dict."""
    return {
        "total_revenue": df["revenue"].sum(),
        "total_orders": df["orders"].sum(),
        "avg_order_value": (
            df["revenue"].sum() / df["orders"].sum()
            if df["orders"].sum() > 0
            else 0
        ),
        "unique_customers": df["customer_id"].nunique(),
    }
```

### Why This Matters

1. **Testability** — You can unit test `filter_data()` and `compute_kpis()` without Streamlit.
2. **Reusability** — The same data functions work in notebooks, scripts, or APIs.
3. **Clarity** — The `app.py` file is just layout; the logic lives in data functions.

---

## 10. Common Dashboard Mistakes

### Mistake 1: Putting Filters in the Main Area

```python
# ❌ Filters clutter the main content
st.selectbox("Region", options)  # In main area
st.slider("Revenue", 0, 100000)  # In main area
st.line_chart(data)

# ✅ Filters belong in the sidebar
with st.sidebar:
    st.selectbox("Region", options)
    st.slider("Revenue", 0, 100000)
st.line_chart(data)
```

### Mistake 2: No Empty State Handling

```python
# ❌ Crashes or shows confusing output when filtered data is empty
st.dataframe(filtered)  # Shows empty table
st.bar_chart(filtered)  # Shows blank chart

# ✅ Always handle empty results
if filtered.empty:
    st.warning("No data matches your filters.")
    st.stop()
```

### Mistake 3: Too Many Charts on One Page

```python
# ❌ Visual overload — user doesn't know where to look
col1, col2, col3 = st.columns(3)
with col1: st.line_chart(data1)
with col2: st.bar_chart(data2)
with col3: st.scatter_chart(data3)
# ... 3 more charts below

# ✅ Use tabs or expanders for secondary views
tab1, tab2, tab3 = st.tabs(["Trends", "Breakdown", "Details"])
with tab1:
    st.line_chart(data1)
with tab2:
    st.bar_chart(data2)
```

### Mistake 4: Not Caching Expensive Operations

```python
# ❌ Reloads data on every interaction
def load_data():
    return pd.read_csv("large_file.csv")

# ✅ Cache the result
@st.cache_data
def load_data():
    return pd.read_csv("large_file.csv")
```

### Mistake 5: Mixing Data Logic with UI Code

```python
# ❌ Data transformation mixed with Streamlit calls
region = st.selectbox("Region", options)
filtered = df[df["region"] == region]
total = filtered["revenue"].sum()
st.metric("Revenue", f"${total:,.0f}")

# ✅ Separate concerns
with st.sidebar:
    region = st.selectbox("Region", options)

filtered = apply_filter(df, region)
kpis = compute_kpis(filtered)
st.metric("Revenue", f"${kpis['total_revenue']:,.0f}")
```

---

## 11. The Complete Dashboard Pattern

Here's the full blueprint, putting everything together:

```python
import streamlit as st
import pandas as pd
import plotly.express as px

# ── 1. Page Config ──────────────────────────────────────
st.set_page_config(page_title="Sales Dashboard", layout="wide")

# ── 2. Data Loading (cached) ────────────────────────────
@st.cache_data
def load_data():
    return pd.read_csv("data/sales.csv")

# ── 3. Data Functions ───────────────────────────────────
def filter_data(df, regions, min_rev, date_range):
    result = df.copy()
    if regions:
        result = result[result["region"].isin(regions)]
    if min_rev > 0:
        result = result[result["revenue"] >= min_rev]
    if date_range and len(date_range) == 2:
        result = result[
            (result["date"] >= pd.Timestamp(date_range[0])) &
            (result["date"] <= pd.Timestamp(date_range[1]))
        ]
    return result

# ── 4. Load Data ────────────────────────────────────────
df = load_data()

# ── 5. Sidebar Controls ─────────────────────────────────
with st.sidebar:
    st.header("🔍 Filters")
    regions = st.multiselect("Region", df["region"].unique(), default=df["region"].unique())
    min_rev = st.slider("Min Revenue", 0, int(df["revenue"].max()), 0)
    date_range = st.date_input("Date Range", value=(df["date"].min(), df["date"].max()))

# ── 6. Apply Filters ────────────────────────────────────
filtered = filter_data(df, regions, min_rev, date_range)

if filtered.empty:
    st.warning("No data matches your filters.")
    st.stop()

# ── 7. Page Title ───────────────────────────────────────
st.title("📊 Sales Dashboard")
st.caption(f"Showing {len(filtered):,} of {len(df):,} records")

# ── 8. KPI Row ──────────────────────────────────────────
c1, c2, c3, c4 = st.columns(4)
c1.metric("Revenue", f"${filtered['revenue'].sum():,.0f}", icon="💰")
c2.metric("Orders", f"{filtered['orders'].sum():,}", icon="📦")
c3.metric("Avg Order", f"${filtered['revenue'].sum() / filtered['orders'].sum():,.2f}", icon="🛒")
c4.metric("Customers", f"{filtered['customer_id'].nunique():,}", icon="👥")

# ── 9. Charts ───────────────────────────────────────────
col_main, col_side = st.columns([2, 1])
with col_main:
    fig = px.line(filtered.groupby("date")["revenue"].sum().reset_index(),
                  x="date", y="revenue", title="Revenue Trend")
    st.plotly_chart(fig, use_container_width=True)
with col_side:
    st.subheader("By Region")
    st.bar_chart(filtered.groupby("region")["revenue"].sum().sort_values())

# ── 10. Data Table ──────────────────────────────────────
with st.expander("📋 View Data"):
    st.dataframe(filtered, use_container_width=True, hide_index=True)

# ── 11. Export ──────────────────────────────────────────
st.download_button("📥 Download CSV", filtered.to_csv(index=False), "filtered_data.csv")

# ── 12. Footer ──────────────────────────────────────────
st.divider()
st.caption("Built with Streamlit · Data Source: Synthetic Sales Data")
```

---

## 12. Testing Checklist

Before releasing a dashboard:

- [ ] **Filters work independently** — each filter can be toggled without error
- [ ] **Empty state handled** — no crash when all data is filtered out
- [ ] **Numbers formatted** — currencies show $, percentages show %, large numbers use commas
- [ ] **Charts resize** — `use_container_width=True` on all Plotly charts
- [ ] **Responsive layout** — sidebar doesn't overlap main content
- [ ] **Loading feedback** — spinner or progress bar for slow operations
- [ ] **Export works** — CSV download produces valid file
- [ ] **Session state** — widget values persist across reruns
- [ ] **Error handling** — try/except around file loading and data parsing
- [ ] **Performance** — `@st.cache_data` on data loading functions
- [ ] **Accessibility** — meaningful widget labels, no color-only indicators
- [ ] **Mobile friendly** — columns collapse gracefully on narrow screens

---

## Key Takeaways

- **Separate data processing from presentation** — pure functions for data, Streamlit calls only in the UI layer.
- **Filters go in the sidebar** — main content is for results, not controls.
- **Lead with KPIs** — users scan metrics before charts.
- **Handle empty states** — always check `filtered.empty` before rendering.
- **Cache expensive operations** — `@st.cache_data` prevents redundant computation.
- **Progressive disclosure** — KPIs first, charts second, raw data in expanders.
- **Consistent formatting** — format numbers, use the same color palette, align metrics.

---

## Further Reading

- [Streamlit Layouts API](https://docs.streamlit.io/develop/api-reference/layout)
- [Streamlit Metrics API](https://docs.streamlit.io/develop/api-reference/data/st.metric)
- [Streamlit Caching](https://docs.streamlit.io/develop/concepts/architecture/caching)
- [Plotly Express](https://plotly.com/python/plotly-express/)
- [Dashboard Design Best Practices](https://www.nngroup.com/articles/dashboards/)

---

## Related Materials

- 📖 Reading: [09 — File Upload & Processing](09_file_upload_and_processing.md)
- 📓 Notebook: [10 — Interactive Data Explorer](../notebooks/10_interactive_dashboard.ipynb)
- ✏️ Exercise: [10 — Dashboard Workshop](../exercises/10_dashboard_workshop.py)
- 🖥️ Demo App: [Interactive Data Explorer](../apps/10_interactive_data_explorer.py)
- 🚀 Project: [P02 — Data Explorer](../projects/P02_data_explorer.md)
