# 06 — Dashboard Design & UI/UX for Data Science

> **📖 Reading · Module 03 · Beginner**
> *A Data Science application is not simply a notebook placed inside a web page.*

---

## Learning Objectives

After completing this reading you will be able to:

- Explain why Streamlit apps differ from Jupyter notebooks.
- Apply Data Science dashboard design principles to build readable, usable applications.
- Use status, progress, and feedback elements appropriately.
- Apply basic accessibility principles to Streamlit apps.
- Avoid common UI complexity traps that hurt usability.

---

## 1. A Data Science App Is Not a Notebook in a Browser

This is the most important concept in this module.

A Jupyter notebook is designed for **one person doing analysis**. A Streamlit app is designed for **many people consuming results**.

| Aspect | Jupyter Notebook | Streamlit App |
|---|---|---|
| **Audience** | Analyst (self) | Stakeholders, clients, public |
| **Flow** | Linear cells, top-to-bottom | Interactive, non-linear |
| **State** | Cell order matters, execution history | Every rerun is fresh |
| **Output** | Code + output interleaved | Only results visible |
| **Narrative** | Markdown cells between code | Written prose, no code shown |
| **Interaction** | Kernel restarts | Real-time reruns |
| **Distribution** | `.ipnb` file, NBViewer | Deployed URL, shareable link |

### What This Means in Practice

A notebook can say: "Run this cell, then this cell, then look at the output."

A Streamlit app must say: "Here is the answer. Want to explore? Click these controls."

**The app hides complexity from the user.** The notebook exposes complexity to the analyst.

---

## 2. Design Principles for Data Science Dashboards

### Principle 1: Lead with Insights, Not Data

```
❌ Wrong approach:
1. Show raw data table
2. Show statistics
3. Show charts
4. User must interpret

✅ Right approach:
1. Show KPIs ("Revenue is up 8%")
2. Show key chart ("Trend is increasing")
3. Let user drill into details
4. Offer raw data for those who want it
```

### Principle 2: Progressive Disclosure

Show the most important information first. Let users choose to see more.

```
Level 1: KPI metrics (always visible)        → 5-second understanding
Level 2: Summary charts (main area)          → 30-second understanding
Level 3: Detailed breakdowns (tabs/expander) → 2-minute deep-dive
Level 4: Raw data & export (bottom section)  → Full analysis
```

### Principle 3: Consistent Spatial Layout

Users build a **mental map** of your app. Don't move things around.

```
Sidebar:    Always controls/filters
Top row:    Always KPI metrics
Middle:     Always main visualization
Bottom:     Always details or data table
```

### Principle 4: Minimal Cognitive Load

Every element on screen has a cost — attention. Make each element earn its place.

**Questions to ask about every element:**
- Does this help the user answer a question?
- Could this be combined with another element?
- Is this the right widget type for this interaction?
- Does the user need to see this immediately, or on demand?

---

## 3. The Status & Feedback Layer

Streamlit provides several elements that communicate **what's happening**. Using them well is the difference between a polished app and a confusing one.

### Progress Bar

Show completion of a known-duration task:

```python
import streamlit as st
import time

progress = st.progress(0, text="Processing...")
for i in range(100):
    time.sleep(0.01)  # Simulate work
    progress.progress(i + 1, text=f"Processing... {i + 1}%")
progress.empty()  # Clean up when done
```

**When to use:** Loading data, training models, batch processing — anything with a measurable percentage.

### Spinner

Show a message during an uncertain-duration task:

```python
with st.spinner("Loading dataset..."):
    df = load_large_dataset()
```

**When to use:** Quick operations (1-5 seconds) where you can't estimate progress.

### Status Container

For multi-step workflows with checkpoints:

```python
with st.status("Running analysis...", expanded=True) as status:
    st.write("Step 1: Loading data...")
    df = load_data()

    st.write("Step 2: Cleaning data...")
    df = clean_data(df)

    st.write("Step 3: Computing metrics...")
    results = compute_metrics(df)

    status.update(label="Analysis complete!", state="complete")
```

**When to use:** Multi-step pipelines where you want to show progress of each step.

### Toast Notifications

Brief, non-blocking messages:

```python
st.toast("Data refreshed!", icon="✅")
```

**When to use:** Confirmations, quick notifications that don't need user action.

### Callout Messages

Status boxes for important information:

```python
st.success("Report generated successfully!")    # Green
st.info("Last updated: 2 minutes ago")          # Blue
st.warning("Data is 30 days old")               # Yellow
st.error("API connection failed")               # Red
```

**When to use:** Persistent messages that explain the current state.

### Celebration Effects

```python
st.balloons()   # After successful submission
st.snow()       # Seasonal or milestone celebration
```

**When to use:** Sparingly — only for genuine milestones.

### Status Feedback Decision Matrix

| Situation | Element | Why |
|---|---|---|
| Loading data (known %) | `st.progress()` | User knows how long to wait |
| Quick computation | `st.spinner()` | Simple "wait a moment" |
| Multi-step pipeline | `st.status()` | Shows step-by-step progress |
| Action confirmed | `st.toast()` | Non-blocking acknowledgment |
| Error occurred | `st.error()` | Persistent, visible state |
| Warning condition | `st.warning()` | Needs attention but not blocking |
| Data is stale | `st.info()` | Context without urgency |
| Task completed | `st.success()` | Positive confirmation |

---

## 4. Metrics — The KPI Language

`st.metric` is the primary element for showing key performance indicators.

### Basic Usage

```python
col1, col2, col3 = st.columns(3)
col1.metric("Revenue", "$1.2M", "+8.3%")
col2.metric("Users", "45,231", "+1,205")
col3.metric("Bounce Rate", "32.1%", "-2.4%")
```

### Metric with Delta Color

```python
# For metrics where lower is better (e.g., error rate)
st.metric("Error Rate", "0.3%", "-0.1%", delta_color="inverse")
```

### Metric with Border

```python
st.metric("Revenue", "$1.2M", border=True)
```

### Metric with Icon (New in Streamlit 1.61)

```python
st.metric("Revenue", "$1.2M", "+8.3%", icon="💰")
st.metric("Users", "45K", "+1.2K", icon="👥")
```

### KPI Design Rules

1. **4 metrics per row** is the standard — 3 is comfortable, 5 is crowded
2. **Label should be short** — "Revenue" not "Total Revenue This Quarter"
3. **Delta tells the story** — users scan deltas to find problems
4. **Format numbers** — "$1.2M" not "1200000"
5. **Group related metrics** — revenue metrics together, user metrics together

---

## 5. Labels and Usability

### Widget Labels

Every widget needs a clear, concise label:

```python
# ❌ Bad labels
st.selectbox("Select one", [...])
st.text_input("Enter")
st.slider("Value", 0, 100)

# ✅ Good labels
st.selectbox("Product category", [...])
st.text_input("Customer name")
st.slider("Confidence threshold", 0.0, 1.0, 0.5)
```

### The `help` Parameter

Add tooltips for non-obvious controls:

```python
st.slider(
    "Smoothing factor",
    0.0, 1.0, 0.5,
    help="Higher values produce smoother trends but may hide important variations."
)
```

### Labels as Section Headers

Use `st.subheader()` or `st.markdown("**Bold text**")` to group related controls:

```python
st.sidebar.header("Data Filters")
product = st.sidebar.selectbox("Product", [...])

st.sidebar.header("Display Options")
chart_type = st.sidebar.radio("Chart type", ["Line", "Bar"])
```

### `label_visibility`

Hide labels when the context is obvious:

```python
# The metric above makes the label redundant
st.metric("Revenue", "$1.2M")

# Hidden label for tight layouts
st.selectbox("Sort", ["A", "B"], label_visibility="collapsed")
```

---

## 6. Basic Accessibility

Streamlit apps should be usable by everyone. Here are practical accessibility guidelines:

### Color Is Not the Only Signal

```python
# ❌ Bad: color alone indicates status
st.metric("Error Rate", "0.3%", delta_color="normal")

# ✅ Good: color + text + icon
st.metric("Error Rate", "0.3%", "-0.1%", icon="✅",
          delta_color="normal")
# The arrow and text provide the signal; color reinforces it.
```

### Alt Text for Images

```python
# Always provide alt_text
st.image("chart.png", alt_text="Revenue trend showing 8% growth over 12 months")
```

### Logical Heading Structure

Streamlit renders headings as HTML `<h1>` through `<h6>`. Use them in order:

```python
st.title("Dashboard")           # <h1> — one per page
st.header("Revenue Analysis")   # <h2> — major sections
st.subheader("Monthly Trend")   # <h3> — subsections
```

### Sufficient Color Contrast

Streamlit's default themes have good contrast. If you customize CSS:

```python
# Streamlit's default text on white background: #262730
# This meets WCAG AA contrast requirements
```

### Keyboard Navigation

All Streamlit widgets are keyboard-navigable by default. Don't override this with custom HTML.

### Semantic Structure

```python
# Use sidebar for controls, main for content
# This helps screen readers distinguish control from content
with st.sidebar:
    st.header("Filters")
    # ... controls

st.header("Results")
# ... content
```

---

## 7. Avoiding Unnecessary UI Complexity

### The Simplicity Rule

If you can remove an element and the app still makes sense, remove it.

### Common Complexity Traps

**Trap 1: Too Many Widgets**

```python
# ❌ 12 widgets in the sidebar — overwhelming
st.sidebar.slider("A", ...)
st.sidebar.slider("B", ...)
st.sidebar.slider("C", ...)
st.sidebar.slider("D", ...)
# ... 8 more

# ✅ Group into a form, or use expanders
with st.sidebar.expander("Advanced Settings"):
    st.slider("A", ...)
    st.slider("B", ...)
```

**Trap 2: Too Much Information at Once**

```python
# ❌ 6 charts on one page — visual overload
col1, col2, col3 = st.columns(3)
with col1: st.line_chart(data1)
with col2: st.bar_chart(data2)
with col3: st.scatter_chart(data3)
# ... 3 more

# ✅ Use tabs for views
tab1, tab2, tab3 = st.tabs(["Revenue", "Users", "Performance"])
```

**Trap 3: Deep Nesting**

```python
# ❌ Container → Columns → Expander → Columns — hard to follow
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        with st.expander("Details"):
            a, b = st.columns(2)

# ✅ Flatten the hierarchy
st.header("Overview")
col1, col2 = st.columns(2)
with col1: st.metric(...)
with col2: st.metric(...)

with st.expander("Details"):
    st.dataframe(df)
```

**Trap 4: Redundant Elements**

```python
# ❌ Title, header, and subheader all say the same thing
st.title("Sales Dashboard")
st.header("Sales Dashboard Overview")
st.subheader("Sales Data Dashboard")

# ✅ One clear title
st.title("Sales Dashboard")
```

### The "5-Second Test"

A user should understand what your app does and how to use it within 5 seconds of loading. If they can't, simplify.

---

## 8. Real-World Dashboard Anatomy

Here's a complete layout for a typical Data Science dashboard:

```
┌─────────────────────────────────────────────────────────────┐
│ 📊 Sales Dashboard                              [Settings⚙️]│
├──────────┬──────────────────────────────────────────────────┤
│          │                                                  │
│ Sidebar  │  [KPI 1] [KPI 2] [KPI 3] [KPI 4]              │
│          │                                                  │
│ Filters: │  ┌──────────────────────┬──────────────────┐   │
│ Category │  │   Main Chart         │  Secondary View  │   │
│ Date     │  │   (60% width)        │  (40% width)     │   │
│ Region   │  │                      │                  │   │
│          │  └──────────────────────┴──────────────────┘   │
│ Options: │                                                  │
│ Chart    │  ┌─────────────────────────────────────────┐    │
│ Sort     │  │ Details Table / Data                     │    │
│          │  │ (inside expander)                        │    │
│ Export:  │  └─────────────────────────────────────────┘    │
│ [CSV]    │                                                  │
│ [Excel]  │  Last updated: 2 min ago · Source: Sales DB     │
├──────────┴──────────────────────────────────────────────────┤
```

### Layout Zones

| Zone | Purpose | Content |
|---|---|---|
| **Sidebar** | Controls | Filters, parameters, settings, export buttons |
| **KPI Row** | Key metrics | `st.metric` cards (4 columns max) |
| **Main Area** | Primary visualization | Charts, plots (60% width) |
| **Side Panel** | Supporting view | Table, secondary chart (40% width) |
| **Details** | Deep dive | Expandable data tables, raw data |
| **Footer** | Context | Last updated, data source, version |

---

## 9. Cross-References: Topic → Learning Path

Every concept in this reading maps to a full learning chain:

| Topic | Reading | Notebook | Exercise | Quiz | Assessment |
|---|---|---|---|---|---|
| Sidebar | This (§2) | 05 (§2) | 05 (Step 2) | 03 (Q1) | Midterm |
| Columns | This (§3) | 05 (§3) | 05 (Step 3) | 03 (Q2) | Midterm |
| Tabs | This (§6) | 05 (§6) | 05 (Step 5) | 03 (Q3) | Midterm |
| Expander | This (§7) | 05 (§7) | 06 (Step 2) | 03 (Q4) | Midterm |
| Status/Progress | This (§3) | 06 (§3) | 06 (Step 4) | 03 (Q5) | Final |
| Metrics | This (§4) | 06 (§2) | 06 (Step 1) | 03 (Q6) | Final |
| Dashboard design | This (§2,§8) | 06 (§5) | 06 (all) | 03 (Q7) | Capstone |
| Accessibility | This (§6) | 06 (§6) | 06 (Bonus) | 03 (Q8) | Capstone |

---

## Key Takeaways

- **A Streamlit app is not a notebook in a browser** — it's a purpose-built interface for sharing results.
- **Lead with insights** (KPIs), then charts, then data — progressive disclosure.
- **Sidebar for controls, main for content** — this separation is non-negotiable.
- **Use status/feedback elements** to communicate progress — spinners for short tasks, progress bars for measurable tasks, status containers for multi-step pipelines.
- **Metrics are the KPI language** — use them prominently at the top of dashboards.
- **Accessibility means contrast, labels, alt text, and keyboard navigation** — not just color.
- **Simplicity is a feature** — every element must earn its place on screen.

---

## Further Reading

- [Streamlit Layouts API](https://docs.streamlit.io/develop/api-reference/layout)
- [Streamlit Status Elements](https://docs.streamlit.io/develop/api-reference/status)
- [Streamlit Metrics API](https://docs.streamlit.io/develop/api-reference/data/st.metric)
- [Streamlit Theming](https://docs.streamlit.io/develop/concepts/theming)
- [WCAG 2.1 Guidelines](https://www.w3.org/WAI/WCAG21/quickref/)

---

## Related Materials

- 📖 Reading: [05 — Layouts, Containers & Page Structure](05_layouts_and_containers.md)
- 📓 Notebook: [05 — Layouts & Containers](../notebooks/05_layouts_and_containers.ipynb)
- 📓 Notebook: [06 — Data Science Dashboards](../notebooks/06_data_science_dashboards.ipynb)
- ✏️ Exercise: [05 — Layout Basics](../exercises/05_layout_basics.py)
- ✏️ Exercise: [06 — Dashboard Builder](../exercises/06_dashboard_builder.py)
- 🖥️ Demo: [05 — Layouts Demo](../apps/05_layouts_demo.py)
- 🖥️ Demo: [06 — Dashboard Demo](../apps/06_dashboard_demo.py)
- 📝 Quiz: [03 — Layouts & UI/UX](../quizzes/03_layouts_uiux.md)
