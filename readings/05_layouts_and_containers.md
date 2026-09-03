# 05 — Layouts, Containers & Page Structure

> **📖 Reading · Module 03 · Beginner**
> *Learn how to structure your Streamlit app with sidebars, columns, tabs, expanders, and containers.*

---

## Learning Objectives

After completing this reading you will be able to:

- Organize content using `st.sidebar`, `st.columns`, `st.tabs`, `st.expander`, `st.container`, and `st.empty`.
- Choose the right layout element for a given Data Science use case.
- Apply vertical and horizontal alignment to create readable layouts.
- Use `st.popover` and `@st.dialog` for contextual UI.
- Understand the layout hierarchy: sidebar → main → columns → containers → widgets.

---

## 1. The Layout Mental Model

A Streamlit app is a **single scrollable page** divided into regions:

```
┌─────────────────────────────────────────────┐
│  Sidebar (fixed, left)  │   Main Area       │
│                          │                   │
│  ┌──────────────────┐   │  ┌──────────────┐ │
│  │  Controls here   │   │  │  Content     │ │
│  │  (filters, params)│   │  │  (charts,    │ │
│  └──────────────────┘   │  │   tables,    │ │
│                          │  │   metrics)   │ │
│                          │  └──────────────┘ │
│                          │                   │
│                          │  ┌────┐ ┌────┐   │
│                          │  │Col1│ │Col2│   │
│                          │  └────┘ └────┘   │
└─────────────────────────────────────────────┘
```

**Key principle:** The sidebar holds controls (filters, parameters, settings). The main area holds content (data, charts, insights). This separation creates a clean mental model for users.

---

## 2. Sidebar

The sidebar is a fixed panel on the left side of the page. It's the standard location for controls that affect the main content area.

### Basic Usage

```python
import streamlit as st

# Two equivalent syntaxes:
st.sidebar.write("Hello from the sidebar!")
st.sidebar.text_input("Search", key="search")

# Or using the object directly:
sidebar = st.sidebar
sidebar.header("Filters")
```

### Sidebar as a Control Panel

The sidebar is where users expect to find **controls that change what's displayed**:

```python
# Sidebar as a filter panel
st.sidebar.header("Data Filters")

# File upload
uploaded = st.sidebar.file_uploader("Upload CSV", type=["csv"])

# Category filter
category = st.sidebar.selectbox("Category", ["All", "Electronics", "Clothing", "Food"])

# Price range
price_range = st.sidebar.slider("Price Range", 0, 1000, (50, 500))

# Sort order
sort_by = st.sidebar.radio("Sort by", ["Name", "Price", "Rating"], horizontal=True)
```

### Sidebar Best Practices

1. **Filters and settings belong in the sidebar** — not in the main area
2. **Keep it concise** — a crowded sidebar is hard to scan
3. **Use headers to group controls** — `st.sidebar.header("Section Name")`
4. **Put the most important controls at the top** — users scan top-to-bottom
5. **Use `st.sidebar.form()` for complex filter sets** — batch submission prevents rerun churn

### Sidebar Gotcha: Reruns

Every sidebar widget change triggers a full script rerun. If you have expensive computations that depend on multiple filters, consider using `st.sidebar.form()` to batch them:

```python
# Without form: 3 reruns for 3 filter changes
# With form: 1 rerun when user clicks "Apply"
with st.sidebar.form("filters"):
    cat = st.selectbox("Category", ["All", "A", "B"])
    price = st.slider("Price", 0, 1000, (0, 1000))
    min_rating = st.slider("Min Rating", 0, 5, 3)
    submitted = st.form_submit_button("Apply Filters")
```

---

## 3. Columns

Columns let you place elements **side by side** — the most common layout pattern for dashboards.

### Basic Columns

```python
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Revenue", "$12,345", "+5.2%")

with col2:
    st.metric("Users", "1,234", "+12.1%")

with col3:
    st.metric("Conversion", "3.2%", "-0.4%")
```

### Unequal Columns

Pass a list of relative widths:

```python
# 70/30 split — chart on left, controls on right
main, sidebar = st.columns([0.7, 0.3])

with main:
    st.line_chart(data)

with sidebar:
    st.selectbox("Chart type", ["Line", "Bar", "Area"])
```

### Column Gap

Control the space between columns with the `gap` parameter:

```python
# Named gaps
st.columns(3, gap="small")    # 1rem (default)
st.columns(3, gap="medium")   # 2rem
st.columns(3, gap="large")    # 4rem

# Pixel-based gap (new in Streamlit 1.60)
st.columns(3, gap=20)         # 20px gap
```

### Vertical Alignment

Align content across columns of different heights:

```python
left, center, right = st.columns(3, vertical_alignment="center")

with left:
    st.button("Short")
with center:
    st.markdown("This is a\nmuch longer\ntext block")
with right:
    st.checkbox("Check me")
```

Options: `"top"` (default), `"center"`, `"bottom"`.

### Column Borders

Add borders around columns for visual separation:

```python
col1, col2, col3 = st.columns(3, border=True)
col1.write("Bordered column 1")
col2.write("Bordered column 2")
col3.write("Bordered column 3")
```

### Horizontal Scrolling (New in 1.62)

Disable vertical stacking for a scrollable row:

```python
# Columns stay horizontal, scroll instead of wrapping
cols = st.columns([1, 1, 1, 1, 1, 1, 1, 1], wrap=False)
for i, col in enumerate(cols):
    col.metric(f"Item {i}", f"{i * 100}")
```

### Anti-Pattern: Nesting Too Deep

```python
# ❌ Don't do this — readability collapses
col1, col2 = st.columns(2)
with col1:
    a, b = st.columns(2)
    with a:
        c, d = st.columns(2)
        # ... this is unreadable

# ✅ Better: use containers, tabs, or expanders for depth
with st.expander("Advanced Options"):
    col1, col2 = st.columns(2)
```

> **Rule of thumb:** Never nest columns more than one level deep.

---

## 4. Containers

A container is a **logical grouping** that doesn't add any visual chrome — it's just a section of your page that you can reference by name.

### Basic Container

```python
results = st.container()

# Later in the script, write into it:
results.write("This appears first in the container")
results.write("This appears second")

# Or using with:
with results:
    st.write("Inside the container")
```

### Why Use Containers?

1. **Write to them out of order** — useful when you compute results before you display them
2. **Conditional sections** — show/hide entire groups
3. **Pass to functions** — pass a container to a function so it writes into a specific area

```python
# Pass a container to a function
def render_chart(container, data, chart_type):
    with container:
        if chart_type == "line":
            container.line_chart(data)
        elif chart_type == "bar":
            container.bar_chart(data)

chart_area = st.container()
params = st.sidebar

chart_type = params.selectbox("Type", ["line", "bar"])
render_chart(chart_area, data, chart_type)
```

---

## 5. Empty

`st.empty()` is a container that **holds exactly one element** — writing a new element replaces the previous one.

```python
placeholder = st.empty()

# Initially shows "Loading..."
placeholder.write("Loading data...")

# After loading, replace the content
placeholder.dataframe(df)

# Or clear it entirely
placeholder.empty()
```

**Use cases:**
- Loading indicators that disappear when done
- Status messages that update in place
- Countdown timers or live counters

```python
import time

placeholder = st.empty()
for i in range(10, 0, -1):
    placeholder.metric("Countdown", i)
    time.sleep(1)
placeholder.empty()
st.success("Done!")
```

---

## 6. Tabs

Tabs let users switch between **views of related content** without leaving the page.

### Basic Tabs

```python
tab1, tab2, tab3 = st.tabs(["Overview", "Details", "Export"])

with tab1:
    st.line_chart(data)

with tab2:
    st.dataframe(data)

with tab3:
    st.download_button("Download CSV", data.to_csv(), "data.csv")
```

### Tab Height (New in Streamlit 1.60)

Control the height of the tab panel:

```python
tab1, tab2 = st.tabs(["Chart", "Data"])

with tab1:
    st.line_chart(data)    # Height matches content (default)

# Fixed-height tab panel
tab_a, tab_b = st.tabs(["Scrollable", "Fixed"])
with tab_a:
    for i in range(100):
        st.write(f"Row {i}")
```

### Lazy Tab Execution

By default, **all tabs execute** on every rerun. To only run the selected tab:

```python
tab1, tab2 = st.tabs(["Chart", "Expensive Analysis"])

with tab1:
    st.line_chart(data)

with tab2:
    # This code only runs when tab2 is selected
    if tab2.open:
        result = expensive_computation(data)
        st.write(result)
```

### When to Use Tabs vs. Other Elements

| Element | Best For | Tradeoff |
|---|---|---|
| **Tabs** | Switching between views of same data | All tabs execute by default |
| **Expander** | Optional details, toggling content | One at a time, users must click |
| **Sidebar** | Controls that affect the main view | Permanent, takes horizontal space |
| **Popover** | Contextual settings, quick actions | Floating, may be hidden |
| **Dialog** | Modal workflows (forms, confirmations) | Blocks main content |

---

## 7. Expander

Expanders are **collapsible sections** — show a preview, let users click to see more.

```python
# Basic expander
with st.expander("See detailed statistics"):
    st.write("Mean: 42.5")
    st.write("Std Dev: 12.3")
    st.write("Skewness: 0.45")

# Start expanded
with st.expander("Raw Data", expanded=True):
    st.dataframe(df)
```

### Expander for Progressive Disclosure

Show summaries first, details on demand:

```python
st.header("Sales Report")
st.metric("Total Revenue", "$1.2M", "+8.3%")

with st.expander("Revenue by Region"):
    st.bar_chart(region_revenue)

with st.expander("Revenue by Product"):
    st.dataframe(product_revenue)

with st.expander("Top 10 Customers"):
    st.dataframe(top_customers)
```

---

## 8. Popover

A popover is a **floating panel** attached to a button. Click the button to open; click outside to close.

```python
with st.popover("⚙️ Settings"):
    theme = st.selectbox("Theme", ["Light", "Dark"])
    density = st.radio("Density", ["Comfortable", "Compact"])
    font_size = st.slider("Font size", 12, 24, 14)
```

### Popover for Filter Panels

```python
with st.popover("🔍 Filters", icon="🔍"):
    category = st.selectbox("Category", ["All", "A", "B", "C"])
    min_val = st.number_input("Min value", value=0)
    max_val = st.number_input("Max value", value=100)
```

### Popover Best Practices

- Use for **lightweight settings** — not complex workflows
- Don't nest popovers
- The `icon` parameter adds visual context to the button

---

## 9. Dialog (Modal)

A dialog is a **modal window** that opens on top of the page. It's ideal for focused workflows that need the user's full attention.

```python
@st.dialog("Contact Form")
def contact_form():
    name = st.text_input("Name")
    email = st.text_input("Email", type="email")
    message = st.text_area("Message")
    if st.button("Send"):
        st.success("Message sent!")
        st.rerun()

if st.button("Contact Us"):
    contact_form()
```

### When to Use Dialogs

- **Confirmation workflows** — "Are you sure you want to delete?"
- **Input forms** — collecting data without cluttering the main page
- **Detail views** — click a row to see full details
- **Multi-step flows** — wizard-style input

### Dialog Best Practices

1. Keep dialogs focused — one task per dialog
2. Include a clear title (the decorator argument)
3. Provide a way to dismiss (button or X)
4. Don't block the entire app for simple tasks — use expanders instead

---

## 10. Bottom

`st.bottom()` places content at the **bottom of the browser window** — typically used for chat input.

```python
# Chat input pinned to the bottom
st.bottom.chat_input("Type a message")
```

This is primarily used for **chat-style interfaces** (covered in Module 13).

---

## 11. Space

`st.space()` adds vertical or horizontal whitespace:

```python
st.space("small")   # Small gap
st.space("medium")  # Medium gap
st.space("large")   # Large gap
```

Useful for visual breathing room between sections.

---

## 12. Layout Hierarchy

Understanding the hierarchy helps you choose the right tool:

```
Page (st.set_page_config)
├── Sidebar (st.sidebar)
│   ├── Header text
│   ├── Widgets (filters, params)
│   └── Form
│
└── Main Area
    ├── Headers & text
    ├── Tabs (st.tabs)
    │   ├── Tab 1
    │   │   ├── Columns (st.columns)
    │   │   │   ├── Container / Empty
    │   │   │   │   ├── Metrics
    │   │   │   │   ├── Charts
    │   │   │   │   └── DataFrames
    │   │   │   └── ...
    │   │   └── Expanders
    │   └── Tab 2
    │       └── ...
    │
    ├── Popovers (floating settings)
    ├── Dialogs (modal workflows)
    └── Status elements (progress, spinner, toast)
```

**Decision flowchart:**

1. **Where does the content live?** → Sidebar vs. Main
2. **How should it be organized?** → Tabs (views), Expanders (details), Columns (side-by-side)
3. **How much space does it need?** → Container (named section), Empty (replaceable)
4. **Is it contextual?** → Popover (settings), Dialog (workflow)
5. **Is it at the page level?** → Bottom (chat input)

---

## 13. Building Layouts for Data Science

### The Dashboard Pattern

Most Data Science dashboards follow a consistent structure:

```python
# 1. Page config
st.set_page_config(page_title="Sales Dashboard", layout="wide")

# 2. Sidebar: controls
st.sidebar.header("Filters")
date_range = st.sidebar.date_input("Date range", ...)
category = st.sidebar.selectbox("Category", [...])
min_revenue = st.sidebar.slider("Min Revenue", 0, 100000, 0)

# 3. Title
st.title("📊 Sales Dashboard")

# 4. KPI row (metrics)
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Revenue", f"${total:,.0f}", f"{delta:.1f}%")
col2.metric("Orders", f"{orders:,}")
col3.metric("Avg Order", f"${avg:.2f}")
col4.metric("Return Rate", f"{returns:.1f}%")

# 5. Charts row
chart_col, table_col = st.columns([2, 1])
with chart_col:
    st.subheader("Revenue Trend")
    st.line_chart(daily_revenue)
with table_col:
    st.subheader("Top Products")
    st.dataframe(top_products, hide_index=True)

# 6. Detailed sections
with st.expander("📊 Full Data"):
    st.dataframe(filtered_df)

with st.expander("📥 Export Options"):
    st.download_button("Export CSV", ...)
```

### Progressive Disclosure Pattern

Don't show everything at once — let users drill in:

```
Level 1: KPI metrics (always visible)
Level 2: Summary charts (tabs or main area)
Level 3: Detailed data (expanders)
Level 4: Raw export (download button)
```

---

## 14. Common Mistakes

### Mistake 1: Putting Controls in the Main Area

```python
# ❌ Filters in main area — cluttered
st.text_input("Search")
st.selectbox("Category", [...])
st.slider("Price range", ...)
st.line_chart(data)

# ✅ Filters in sidebar, charts in main
with st.sidebar:
    search = st.text_input("Search")
    category = st.selectbox("Category", [...])
st.line_chart(data)
```

### Mistake 2: Too Many Columns

```python
# ❌ 8 columns — unusable on any screen
c1, c2, c3, c4, c5, c6, c7, c8 = st.columns(8)

# ✅ 4 columns with scrollable row, or 2-3 columns with tabs
c1, c2, c3, c4 = st.columns(4)
```

### Mistake 3: Not Using Vertical Alignment

```python
# ❌ Columns look ragged
left, right = st.columns(2)
with left:
    st.button("Click")           # Short widget
with right:
    st.text_area("Notes", height=200)  # Tall widget

# ✅ Aligned columns
left, right = st.columns(2, vertical_alignment="bottom")
```

---

## 15. Best Practices

1. **Sidebar for controls, main for content** — always.
2. **Use `st.columns(3)` or `st.columns(4)` max** — fewer columns = more readable.
3. **Never nest columns more than one level deep.**
4. **Use `border=True` on columns** when visual separation helps.
5. **Use `gap` parameter** — `"small"` (default) works for most cases.
6. **Tabs for views, expanders for details, popovers for settings.**
7. **Use `st.empty()` for dynamic content** — loading states, live updates.
8. **Keep layout consistent across pages** — users build spatial memory.
9. **Test on mobile** — narrow screens collapse columns vertically.
10. **Use `layout="wide"` for dashboards** — more space for data.

---

## Key Takeaways

- `st.sidebar` is the standard location for filters and controls.
- `st.columns` places elements side by side — use proportional specs and `gap` for spacing.
- `st.tabs` switches between views; `st.expander` reveals details on demand.
- `st.container` groups elements logically; `st.empty` holds replaceable content.
- `st.popover` and `@st.dialog` provide floating and modal UI respectively.
- The layout hierarchy is: Page → Sidebar/Main → Tabs → Columns → Containers → Content.
- Data Science dashboards follow a standard pattern: Sidebar controls → KPIs → Charts → Details.

---

## Further Reading

- [Streamlit Layouts API Reference](https://docs.streamlit.io/develop/api-reference/layout)
- [Streamlit Columns Guide](https://docs.streamlit.io/develop/api-reference/layout/st.columns)
- [Streamlit Tabs Guide](https://docs.streamlit.io/develop/api-reference/layout/st.tabs)
- [Streamlit Status Elements](https://docs.streamlit.io/develop/api-reference/status)

---

## Related Materials

- 📖 Reading: [06 — Dashboard Design & UI/UX for Data Science](06_dashboard_design_ui_ux.md)
- 📓 Notebook: [05 — Layouts & Containers](../notebooks/05_layouts_and_containers.ipynb)
- 📓 Notebook: [06 — Data Science Dashboards](../notebooks/06_data_science_dashboards.ipynb)
- ✏️ Exercise: [05 — Layout Basics](../exercises/05_layout_basics.py)
- ✏️ Exercise: [06 — Dashboard Builder](../exercises/06_dashboard_builder.py)
- 🖥️ Demo: [05 — Layouts Demo](../apps/05_layouts_demo.py)
- 🖥️ Demo: [06 — Dashboard Demo](../apps/06_dashboard_demo.py)
- 📝 Quiz: [03 — Layouts & UI/UX](../quizzes/03_layouts_uiux.md)
