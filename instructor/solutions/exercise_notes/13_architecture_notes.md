# Exercise 13 — Architecture Workshop: Solution Notes

> **👩‍🏫 Instructor Reference**
> *Expected approach, key code, and grading guidance.*

---

## Challenge 1: Refactor to Functions

### Expected Approach
Separate the monolithic code into: data loading, filtering, metrics computation, and rendering functions.

### Key Code Structure
```python
@st.cache_data
def load_data(n_rows=100):
    np.random.seed(42)
    return pd.DataFrame({
        "category": np.random.choice(["A", "B", "C"], n_rows),
        "value": np.random.randn(n_rows) * 10 + 50,
        "quantity": np.random.randint(1, 50, n_rows),
    })

def filter_data(df, category):
    if category == "All":
        return df
    return df[df["category"] == category]

def compute_metrics(df):
    return {
        "total_rows": len(df),
        "avg_value": df["value"].mean(),
        "total_quantity": df["quantity"].sum(),
    }

def render_metrics(metrics):
    c1, c2, c3 = st.columns(3)
    c1.metric("Total Rows", metrics["total_rows"])
    c2.metric("Avg Value", f"{metrics['avg_value']:.1f}")
    c3.metric("Total Quantity", f"{metrics['total_quantity']:,}")

# Main flow
df = load_data()
category = st.selectbox("Filter", ["All", "A", "B", "C"])
filtered = filter_data(df, category)
metrics = compute_metrics(filtered)
render_metrics(metrics)
st.dataframe(filtered)
st.line_chart(filtered[["value", "quantity"]])
```

### Common Mistakes
- Not using `@st.cache_data` on data loading
- Putting `st.*` calls inside data functions
- Not separating concerns (data vs UI)

### Grading Notes (25 marks)
- Full marks: Clean separation, all functions work, cached loading
- 18 marks: Functions exist but some mixing of concerns
- 10 marks: Partial refactoring

---

## Challenge 2: Reusable Components

### Expected Approach
Create wrapper functions around Streamlit primitives for consistent UI.

### Key Code
```python
def metric_card(label, value, delta=None, delta_color="normal"):
    """Render a consistent metric card."""
    st.metric(label=label, value=value, delta=delta, delta_color=delta_color)

def data_preview(df, max_rows=5, show_shape=True):
    """Show data with consistent formatting."""
    if show_shape:
        st.write(f"Shape: {df.shape[0]} rows × {df.shape[1]} columns")
    st.dataframe(df.head(max_rows), use_container_width=True, hide_index=True)

def section_header(title, description=None, divider=True):
    """Render section header with optional description."""
    st.header(title)
    if description:
        st.caption(description)
    if divider:
        st.divider()

def status_badge(status):
    """Render status with appropriate color/icon."""
    colors = {"active": "🟢", "pending": "🟡", "error": "🔴"}
    icons = {"active": "✅", "pending": "⏳", "error": "❌"}
    icon = icons.get(status.lower(), "❓")
    color = colors.get(status.lower(), "⚪")
    st.write(f"{icon} **{status}**")
```

### Grading Notes (25 marks)
- Full marks: All 4 components work and are used in a demo dashboard
- 18 marks: 3 components work
- 10 marks: 1-2 components work

---

## Challenge 3: Configuration Pattern

### Expected Approach
Centralize settings in a dict or config module. Reference throughout the app.

### Key Code
```python
APP_CONFIG = {
    "title": "My Data Dashboard",
    "icon": "📊",
    "max_rows": 10000,
    "cache_ttl": 3600,
    "categories": ["Electronics", "Clothing", "Food", "Books"],
    "regions": ["North", "South", "East", "West"],
}

st.set_page_config(page_title=APP_CONFIG["title"], page_icon=APP_CONFIG["icon"])

st.title(f"{APP_CONFIG['icon']} {APP_CONFIG['title']}")

category = st.selectbox("Category", APP_CONFIG["categories"])
region = st.selectbox("Region", APP_CONFIG["regions"])
```

### Grading Notes (25 marks)
- Full marks: Config dict used for all settings, no hardcoded values in UI code
- 18 marks: Config exists but some hardcoded values remain
- 10 marks: Config exists but barely used

---

## Challenge 4: Multipage Design

### Expected Approach
Use `st.navigation` with `st.Page` to create a multipage app from a single file (or with page files).

### Key Pattern
```python
# At top of app.py
def home_page():
    st.title("Home")
    st.write("Welcome to the dashboard")

def data_page():
    st.title("Data Explorer")
    # data exploration code

def about_page():
    st.title("About")
    st.write("Built with Streamlit")

# Navigation
home = st.Page(home_page, title="Home", icon="🏠")
data = st.Page(data_page, title="Data", icon="📊")
about = st.Page(about_page, title="About", icon="ℹ️")

pg = st.navigation({"Main": [home, data, about]})
pg.run()
```

### Grading Notes (25 marks)
- Full marks: 3+ pages with navigation, shared state, clean routing
- 18 marks: Pages work but navigation basic
- 10 marks: Basic page switching without st.navigation
