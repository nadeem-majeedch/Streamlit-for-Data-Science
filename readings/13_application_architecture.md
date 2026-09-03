# 13 — Application Architecture & Multipage Apps

> **📖 Reading · Module 09 · Advanced**  
> *Structure your Streamlit applications for maintainability, scalability, and team collaboration.*

---

## Learning Objectives

After completing this reading you will be able to:

- Structure Streamlit applications from single-file to modular projects
- Separate UI, data processing, and business logic
- Create multipage applications using `st.navigation` and `st.Page`
- Implement shared configuration and utilities
- Follow naming conventions and project structure best practices
- Avoid common architectural mistakes

---

## 1. The Evolution of Application Structure

### Level 1: Single File (Beginner)

Every Streamlit app starts as a single file:

```python
# app.py — Simple, but doesn't scale
import streamlit as st
import pandas as pd

st.title("My Dashboard")

# Data loading
df = pd.read_csv("data.csv")

# UI
st.dataframe(df)

# Charts
st.line_chart(df)

# Analysis
st.write(df.describe())
```

**When to use:** Prototypes, scripts, learning exercises (< 100 lines)

---

### Level 2: Functions (Intermediate)

Extract logic into functions:

```python
# app.py — Better separation, still one file
import streamlit as st
import pandas as pd

# --- Data Functions ---
@st.cache_data
def load_data(url):
    return pd.read_csv(url)

def filter_data(df, category):
    if category == "All":
        return df
    return df[df["category"] == category]

def compute_summary(df):
    return df.describe()

# --- UI Functions ---
def render_header():
    st.title("My Dashboard")
    st.markdown("Interactive data analysis tool")

def render_sidebar():
    category = st.sidebar.selectbox("Category", ["All", "A", "B", "C"])
    return category

def render_metrics(df):
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Rows", len(df))
    with col2:
        st.metric("Columns", len(df.columns))
    with col3:
        st.metric("Categories", df["category"].nunique())

# --- Main ---
render_header()
category = render_sidebar()
df = load_data("data.csv")
filtered = filter_data(df, category)
render_metrics(filtered)
st.dataframe(filtered)
st.write(compute_summary(filtered))
```

**When to use:** Medium apps (100-500 lines), solo developers

---

### Level 3: Modules (Advanced)

Split into multiple files and directories:

```
my_app/
├── app.py                    # Entry point
├── config.py                 # Configuration
├── data/
│   ├── __init__.py
│   ├── loader.py            # Data loading
│   └── processor.py         # Data processing
├── ui/
│   ├── __init__.py
│   ├── components.py        # Reusable UI components
│   ├── charts.py            # Chart functions
│   └── layout.py            # Layout helpers
├── pages/
│   ├── home.py              # Home page
│   ├── explore.py           # Data exploration
│   └── analysis.py          # Analysis page
├── utils/
│   ├── __init__.py
│   └── helpers.py           # Utility functions
└── tests/
    ├── test_loader.py
    └── test_processor.py
```

**When to use:** Large apps (500+ lines), team projects, production apps

---

## 2. Separation of Concerns

### Three Layers

| Layer | Responsibility | Example |
|-------|---------------|---------|
| **UI Layer** | Display elements, user interaction | `st.write()`, `st.button()`, layouts |
| **Data Layer** | Loading, processing, transformation | Pandas operations, API calls |
| **Business Logic** | Rules, calculations, validation | Domain-specific computations |

### Example: Separated Code

```python
# ui/components.py
def render_metric_card(label, value, delta=None):
    """Reusable metric card component."""
    st.metric(label=label, value=value, delta=delta)

def render_data_table(df, height=400):
    """Standard data table with consistent styling."""
    st.dataframe(df, height=height, use_container_width=True)

# data/loader.py
@st.cache_data(ttl=3600)
def load_sales_data(region):
    """Load sales data for a region."""
    return pd.read_csv(f"data/sales_{region}.csv")

@st.cache_data
def aggregate_sales(df, group_by):
    """Aggregate sales by category."""
    return df.groupby(group_by).agg({
        "revenue": "sum",
        "units": "sum",
        "date": "count"
    }).rename(columns={"date": "orders"})

# app.py (entry point)
import streamlit as st
from ui.components import render_metric_card, render_data_table
from data.loader import load_sales_data, aggregate_sales

st.title("Sales Dashboard")
region = st.sidebar.selectbox("Region", ["north", "south", "east", "west"])

df = load_sales_data(region)
summary = aggregate_sales(df, "product_category")

render_metric_card("Total Revenue", f"${summary['revenue'].sum():,.0f}")
render_data_table(summary)
```

---

## 3. Multipage Applications

### Method 1: `pages/` Directory (Simple)

Create a `pages/` directory next to your entry point:

```
my_app/
├── app.py           # Entry point
└── pages/
    ├── 1_Explore.py
    ├── 2_Analyze.py
    └── 3_Settings.py
```

Streamlit automatically creates navigation from filenames. Numbers control order.

### Method 2: `st.navigation` + `st.Page` (Preferred)

More flexible and recommended for production:

```python
# app.py — Entry point
import streamlit as st

# Configure pages
pg = st.navigation([
    st.Page("pages/home.py", title="Home", icon="🏠"),
    st.Page("pages/explore.py", title="Explore Data", icon="📊"),
    st.Page("pages/analysis.py", title="Analysis", icon="🔬"),
    st.Page("pages/settings.py", title="Settings", icon="⚙️", default=False),
])

# Shared sidebar elements
st.sidebar.title("My App")
st.sidebar.selectbox("Region", ["Global", "US", "EU"], key="region")

# Run selected page
pg.run()
```

### Grouped Navigation

```python
# app.py
import streamlit as st

pg = st.navigation({
    "Data": [
        st.Page("pages/home.py", title="Home", icon="🏠"),
        st.Page("pages/explore.py", title="Explore", icon="📊"),
    ],
    "Analysis": [
        st.Page("pages/analysis.py", title="Analysis", icon="🔬"),
        st.Page("pages/reports.py", title="Reports", icon="📄"),
    ],
    "Admin": [
        st.Page("pages/settings.py", title="Settings", icon="⚙️"),
    ]
})

pg.run()
```

### Top Navigation

```python
pg = st.navigation(pages, position="top")  # Navigation at top instead of sidebar
```

---

## 4. Shared Components

### Common Sidebar

```python
# app.py — Shared elements before page
import streamlit as st

# These widgets persist across page navigation
st.sidebar.title("My App")
user = st.sidebar.text_input("Username")
theme = st.sidebar.selectbox("Theme", ["Light", "Dark"])

# Store in session state for pages to access
st.session_state.user = user
st.session_state.theme = theme

pg = st.navigation([...])
pg.run()
```

### Reusable UI Components

```python
# ui/components.py
import streamlit as st

def card(title, content):
    """Render a styled card."""
    with st.container(border=True):
        st.subheader(title)
        st.write(content)

def metric_row(metrics: dict):
    """Render a row of metrics."""
    cols = st.columns(len(metrics))
    for col, (label, value) in zip(cols, metrics.items()):
        with col:
            st.metric(label, value)

def data_preview(df, max_rows=5):
    """Show data preview with shape info."""
    st.info(f"📊 {df.shape[0]} rows × {df.shape[1]} columns")
    st.dataframe(df.head(max_rows), use_container_width=True)
```

### Configuration Module

```python
# config.py
import os

# App settings
APP_TITLE = "My Data App"
APP_ICON = "📊"
MAX_ROWS = 10000

# Data paths
DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
RAW_DATA_PATH = os.path.join(DATA_DIR, "raw")
PROCESSED_DATA_PATH = os.path.join(DATA_DIR, "processed")

# Cache settings
CACHE_TTL = 3600  # 1 hour
MAX_CACHE_ENTRIES = 100
```

---

## 5. Naming Conventions

### Files

| Type | Convention | Example |
|------|-----------|---------|
| Entry point | `app.py` | `app.py` |
| Pages | `NN_name.py` or `name.py` | `01_home.py`, `explore.py` |
| Modules | `snake_case.py` | `data_loader.py` |
| Tests | `test_*.py` | `test_loader.py` |
| Config | `config.py` or `.env` | `config.py` |

### Functions

| Type | Convention | Example |
|------|-----------|---------|
| UI rendering | `render_*()` | `render_header()`, `render_chart()` |
| Data loading | `load_*()` | `load_data()`, `load_config()` |
| Processing | `process_*()` or `compute_*()` | `process_data()`, `compute_stats()` |
| Validation | `validate_*()` | `validate_input()` |
| Utilities | `get_*()` or descriptive | `get_session_user()` |

### Variables

| Type | Convention | Example |
|------|-----------|---------|
| DataFrames | Descriptive noun | `sales_data`, `user_profiles` |
| Config | UPPER_SNAKE | `MAX_ROWS`, `API_KEY` |
| Session state | snake_case | `st.session_state.user` |
| Widget keys | snake_case, descriptive | `key="selected_category"` |

---

## 6. Project Structure Templates

### Small App (< 300 lines)

```
my_app/
├── app.py
├── requirements.txt
└── data/
    └── data.csv
```

### Medium App (300-1000 lines)

```
my_app/
├── app.py
├── config.py
├── requirements.txt
├── pages/
│   ├── home.py
│   ├── explore.py
│   └── settings.py
├── utils/
│   ├── __init__.py
│   └── helpers.py
└── data/
    └── data.csv
```

### Large App (1000+ lines)

```
my_app/
├── app.py
├── config.py
├── requirements.txt
├── pages/
│   ├── home.py
│   ├── explore.py
│   ├── analysis.py
│   └── settings.py
├── components/
│   ├── __init__.py
│   ├── charts.py
│   ├── forms.py
│   └── layout.py
├── data/
│   ├── __init__.py
│   ├── loader.py
│   └── processor.py
├── utils/
│   ├── __init__.py
│   └── helpers.py
├── tests/
│   ├── __init__.py
│   ├── test_loader.py
│   └── test_processor.py
└── data/
    └── raw/
```

---

## 7. Common Architectural Mistakes

### Mistake 1: Giant app.py

```python
# ❌ BAD: 2000+ line monolith
# Everything in one file — hard to navigate, test, maintain

# ✅ GOOD: Split into modules
from data.loader import load_data
from ui.components import render_chart
from utils.helpers import format_currency
```

### Mistake 2: Business Logic in UI

```python
# ❌ BAD: Logic mixed with UI
if st.button("Calculate"):
    result = price * quantity * (1 - discount)  # Business logic!
    tax = result * 0.1  # More logic!
    st.write(f"Total: ${result + tax}")

# ✅ GOOD: Separate concerns
def calculate_total(price, quantity, discount, tax_rate=0.1):
    """Business logic in its own function."""
    subtotal = price * quantity * (1 - discount)
    tax = subtotal * tax_rate
    return subtotal + tax

if st.button("Calculate"):
    total = calculate_total(price, quantity, discount)
    st.write(f"Total: ${total:.2f}")
```

### Mistake 3: No Shared Configuration

```python
# ❌ BAD: Hardcoded values scattered throughout
df = pd.read_csv("data/sales_2024.csv")  # In file1.py
df = pd.read_csv("data/sales_2024.csv")  # In file2.py (same path!)

# ✅ GOOD: Single source of truth
# config.py
DATA_PATH = "data/sales_2024.csv"

# file1.py
from config import DATA_PATH
df = pd.read_csv(DATA_PATH)
```

### Mistake 4: Importing Everything

```python
# ❌ BAD: Star imports pollute namespace
from utils.helpers import *

# ✅ GOOD: Explicit imports
from utils.helpers import format_currency, validate_email
```

---

## 8. Testing Streamlit Apps

### Testing Data Logic (No Streamlit)

```python
# tests/test_processor.py
import pytest
import pandas as pd
from data.processor import aggregate_sales, filter_by_date

def test_aggregate_sales():
    df = pd.DataFrame({
        "category": ["A", "A", "B", "B"],
        "revenue": [100, 200, 150, 250]
    })
    result = aggregate_sales(df, "category")
    assert len(result) == 2
    assert result.loc["A", "revenue"] == 300

def test_filter_by_date():
    df = pd.DataFrame({
        "date": pd.to_datetime(["2024-01-01", "2024-06-15", "2024-12-31"]),
        "value": [1, 2, 3]
    })
    result = filter_by_date(df, "2024-01-01", "2024-06-30")
    assert len(result) == 2
```

### Testing Streamlit UI (AppTest)

```python
# tests/test_app.py
from streamlit.testing.v1 import AppTest

def test_home_page():
    at = AppTest.from_file("app.py")
    at.run()
    assert at.title[0].value == "My Dashboard"
    assert not at.exception

def test_sidebar_navigation():
    at = AppTest.from_file("app.py")
    at.run()
    at.sidebar.selectbox[0].set_value("Explore")
    at.run()
    assert "Explore" in at.title[0].value
```

---

## 9. Best Practices

### Do's

1. **Start simple, refactor when needed** — don't over-engineer early
2. **Separate UI from logic** — UI functions render, logic functions compute
3. **Use configuration modules** — single source of truth for settings
4. **Create reusable components** — DRY (Don't Repeat Yourself)
5. **Test business logic separately** — unit tests without Streamlit
6. **Use explicit imports** — no star imports
7. **Follow naming conventions** — consistent, predictable

### Don'ts

1. **Don't create giant app.py** — split at 300-500 lines
2. **Don't put business logic in UI callbacks** — extract to functions
3. **Don't hardcode paths, URLs, or secrets** — use config
4. **Don't import everything everywhere** — explicit imports only
5. **Don't skip `__init__.py`** — proper Python packages
6. **Don't over-abstract** — keep it understandable

---

## 10. Learning vs Production

### Learning/Teaching

```python
# Simple single file — fine for teaching
import streamlit as st
import pandas as pd

st.title("Lesson Demo")
data = pd.read_csv("sample.csv")
st.dataframe(data)
st.line_chart(data)
```

### Production

```python
# app.py — Production entry point
import streamlit as st
from config import APP_TITLE, APP_ICON
from pages import home, explore, analysis

st.set_page_config(page_title=APP_TITLE, page_icon=APP_ICON)

pg = st.navigation([
    st.Page(home, title="Home", icon="🏠"),
    st.Page(explore, title="Explore", icon="📊"),
    st.Page(analysis, title="Analysis", icon="🔬"),
])

pg.run()
```

---

## Key Takeaways

- **Evolution:** Single file → Functions → Modules → Multipage
- **Separation of concerns:** UI, Data, Business Logic
- **`st.navigation` + `st.Page`** is the preferred multipage approach
- **Shared components** go in the entry point or shared modules
- **Configuration** centralizes settings and constants
- **Testing** — test logic separately, use AppTest for UI
- **Naming conventions** make code predictable and navigable

---

## Further Reading

- [Multipage Apps Overview](https://docs.streamlit.io/develop/concepts/multipage-apps/overview)
- [st.navigation](https://docs.streamlit.io/develop/api-reference/navigation/st.navigation)
- [st.Page](https://docs.streamlit.io/develop/api-reference/navigation/st.Page)
- [AppTest](https://docs.streamlit.io/develop/api-reference/app-testing/st.testing.v1.apptest)

---

## Related Materials

- 📓 Notebook: [13 — Application Architecture](../notebooks/13_application_architecture.ipynb)
- ✏️ Exercise: [13 — Architecture Workshop](../exercises/13_architecture_workshop.py)
- 🖥️ Demo App: [13 — Modular App](../apps/13_modular_app/app.py)
- 📝 Quiz: [09 — Architecture & Multipage](../quizzes/09_architecture_multipage.md)
