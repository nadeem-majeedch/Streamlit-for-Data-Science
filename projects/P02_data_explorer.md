# P02 — Interactive Data Explorer

> **🚀 Project · Intermediate**
> *Build a complete interactive dashboard that turns raw data into actionable insights.*

---

## Project Overview

You will build an **Interactive Data Explorer** — a Streamlit dashboard that allows users to upload or select datasets, apply filters, view KPIs, explore charts, and download results.

This project synthesizes everything from Modules 01–06: widgets, layout, session state, file upload, data processing, and dashboard design.

### Learning Outcomes

By completing this project, you will be able to:

- Design a dashboard architecture with separated data and presentation layers.
- Build reactive filter panels that update all components.
- Create KPI metric rows with proper formatting.
- Combine Plotly charts, data tables, and export into a cohesive app.
- Handle edge cases: empty states, large datasets, and user errors.

---

## Dataset Options

Choose **one** of the following datasets (or propose your own with instructor approval):

| Dataset | Source | Size | Key Columns |
|---|---|---|---|
| **E-Commerce Sales** | Generated (see below) | 2,000 rows | date, product, region, revenue, profit |
| **Titanic** | `seaborn.load_dataset("titanic")` | 891 rows | survived, class, age, fare, sex |
| **World Happiness** | Kaggle (CC0) | 1,500 rows | country, year, happiness_score, gdp |
| **COVID-19 Data** | Our World in Data | 10,000+ rows | date, location, cases, deaths, vaccination |
| **Your Choice** | Instructor-approved | Any | Must have ≥3 numeric + ≥2 categorical columns |

### E-Commerce Sales Generator

If you choose the generated dataset:

```python
import numpy as np
import pandas as pd

def generate_sales_data(n_rows=2000):
    np.random.seed(42)
    dates = pd.date_range("2024-01-01", periods=365, freq="D")
    products = ["Laptop", "Phone", "Tablet", "Headphones", "Monitor", "Keyboard"]
    regions = ["North America", "Europe", "Asia Pacific", "Latin America"]
    segments = ["Consumer", "Corporate", "Home Office"]
    base_prices = {"Laptop": 1200, "Phone": 800, "Tablet": 500, "Headphones": 150, "Monitor": 400, "Keyboard": 80}

    data = []
    for _ in range(n_rows):
        product = np.random.choice(products)
        unit_price = base_prices[product] * np.random.uniform(0.8, 1.2)
        quantity = np.random.randint(1, 10)
        revenue = round(unit_price * quantity, 2)
        cost = round(revenue * np.random.uniform(0.4, 0.7), 2)
        data.append({
            "date": np.random.choice(dates),
            "product": product,
            "region": np.random.choice(regions),
            "segment": np.random.choice(segments),
            "unit_price": round(unit_price, 2),
            "quantity": quantity,
            "revenue": revenue,
            "cost": cost,
            "profit": round(revenue - cost, 2),
        })
    return pd.DataFrame(data)
```

---

## Functional Requirements

### FR-1: Data Loading

- [ ] Load data using `@st.cache_data` for performance
- [ ] Display dataset shape (rows × columns) after loading
- [ ] Show first 5 rows in an expander

### FR-2: Filter Panel (Sidebar)

- [ ] Date range filter (st.date_input)
- [ ] At least 2 categorical filters (st.multiselect)
- [ ] At least 1 numeric filter (st.slider or st.number_input)
- [ ] Filters update all dashboard components reactively
- [ ] Filter state persists across reruns

### FR-3: KPI Metrics

- [ ] Display 4 KPI cards in a row using `st.metric`
- [ ] Metrics update when filters change
- [ ] Numbers formatted with appropriate units ($, %, commas)
- [ ] Each metric has a meaningful icon

### FR-4: Charts

- [ ] At least 3 different chart types (line, bar, scatter, pie, etc.)
- [ ] Charts are interactive (Plotly preferred)
- [ ] Charts use `use_container_width=True`
- [ ] Charts have titles and axis labels
- [ ] Charts update when filters change

### FR-5: Data Table

- [ ] Filtered data displayed in `st.dataframe`
- [ ] Sorted by a meaningful column (e.g., revenue descending)
- [ ] Formatted columns (currency, dates)
- [ ] Wrapped in `st.expander` for progressive disclosure

### FR-6: Export

- [ ] CSV download button for filtered data
- [ ] At least one additional format (Excel or JSON)
- [ ] Download includes only filtered data, not full dataset

### FR-7: Error Handling

- [ ] Empty state handled (st.warning + st.stop)
- [ ] No crashes on invalid filter combinations
- [ ] Graceful handling of missing data

---

## UI Requirements

### Layout

```
┌──────────────────────────────────────────────────┐
│ Sidebar              │  Main Content              │
│                      │                             │
│ 🔍 Filters           │  Title + Description        │
│   Date range         │                             │
│   Category           │  [KPI] [KPI] [KPI] [KPI]   │
│   Region             │                             │
│                      │  ┌──────────┬──────────┐   │
│ ⚙️ Display           │  │ Chart 1  │ Chart 2  │   │
│   Chart type         │  │ (60%)    │ (40%)    │   │
│   Options            │  └──────────┴──────────┘   │
│                      │                             │
│ 📥 Export             │  ┌─────────────────────┐   │
│   CSV button         │  │ Data Table (expander)│   │
│                      │  └─────────────────────┘   │
│                      │                             │
│                      │  Export buttons             │
│                      │  Footer                     │
└──────────────────────────────────────────────────┘
```

### Design Principles

- **Lead with KPIs** — metrics at the top, charts below
- **Progressive disclosure** — summary first, details on demand
- **Consistent formatting** — same color palette, number formats, spacing
- **Clear labels** — every widget has a descriptive label
- **Empty states** — always show a message when no data matches filters

---

## Technical Requirements

### Architecture

```
your_dashboard/
├── app.py           # Main Streamlit app (UI layer only)
├── data.py          # Data loading & transformation functions
├── charts.py        # Chart-building functions (optional)
├── utils.py         # Formatting helpers (optional)
└── requirements.txt # Dependencies
```

**Or** as a single file with clear section headers.

### Code Quality

- [ ] Data functions have no `st.*` calls inside
- [ ] Functions have docstrings
- [ ] No hardcoded file paths (use relative paths or data loading functions)
- [ ] No hardcoded secrets or API keys
- [ ] `@st.cache_data` on data loading functions
- [ ] Consistent naming (snake_case for functions/variables)

### Dependencies

```
streamlit>=1.44.0
pandas>=2.0.0
numpy>=1.24.0
plotly>=5.15.0
```

---

## Implementation Guide

### Step-by-Step Build Order

1. **Data Layer** — Write `load_data()`, `filter_data()`, `compute_kpis()`
2. **Page Config** — `st.set_page_config()` as the first Streamlit call
3. **Sidebar** — Build all filter widgets
4. **Apply Filters** — Call `filter_data()` and handle empty state
5. **KPI Row** — Display 4 metric cards
6. **Charts** — Add tabbed chart views with Plotly
7. **Data Table** — Add expandable data table with formatting
8. **Export** — Add download buttons
9. **Polish** — Add footer, help text, error handling
10. **Test** — Walk through the testing checklist below

### Session State Usage

```python
# Persist filter defaults
if "selected_regions" not in st.session_state:
    st.session_state.selected_regions = df["region"].unique().tolist()

# Use in sidebar
regions = st.multiselect(
    "Region",
    options=df["region"].unique().tolist(),
    default=st.session_state.selected_regions,
    key="region_filter",
)

# Update on change
st.session_state.selected_regions = regions
```

### Caching Strategy

```python
@st.cache_data  # Cache the raw data loading
def load_data():
    return pd.read_csv("data/sales.csv")

# Don't cache filtered data — it changes with every filter interaction
filtered = filter_data(df, regions, products, segments, date_range)
```

---

## Experiments

After building the basic dashboard, try these experiments:

### Experiment 1: Compare Chart Libraries

Replace Plotly charts with Streamlit native charts (`st.line_chart`, `st.bar_chart`). What do you gain/lose?

### Experiment 2: Add Real-Time Updates

Use `st.fragment` with `run_every` to auto-refresh data every 30 seconds. How does this change the user experience?

### Experiment 3: Multi-Page Layout

Convert the single-page dashboard into a multi-page app using `st.navigation`. How does the code organization change?

### Experiment 4: Add Authentication

Use `st.experimental_user` to show the logged-in user's name. How would you add role-based access?

### Experiment 5: Performance Testing

Load a dataset with 100,000 rows. Where does the dashboard become slow? Apply `@st.cache_data` and `st.fragment` to optimize.

---

## Common Mistakes

| Mistake | Why It's Bad | Fix |
|---|---|---|
| Filters in main area | Clutters the content | Move to sidebar |
| No empty state handling | Crashes on empty filters | Add `st.warning()` + `st.stop()` |
| Mixing data + UI code | Hard to test/reuse | Separate into functions |
| Not caching data | Slow on every rerun | Add `@st.cache_data` |
| Raw numbers displayed | Hard to read | Format: `$1,234,567` |
| No chart titles | User doesn't know what they're seeing | Always add titles + labels |
| 6+ charts on one page | Visual overload | Use tabs or expanders |
| Hardcoded file paths | Breaks on different machines | Use relative paths or config |

---

## Debugging Checklist

| Symptom | Likely Cause | Fix |
|---|---|---|
| Blank chart | Empty filtered data | Check `filtered.empty` before chart |
| Slow performance | No caching on data load | Add `@st.cache_data` |
| Filters don't update charts | State issue | Ensure filters are applied before charts |
| Numbers show as 1234567 | No formatting | Use f-strings: `f"${val:,.0f}"` |
| Chart too narrow | Missing `use_container_width` | Add `use_container_width=True` |
| Widget values reset | Wrong key usage | Use consistent `key` parameter |
| `st.stop()` not working | Placed before `st.stop()` call | Move empty check to right place |
| Excel download fails | Missing openpyxl | `pip install openpyxl` |

---

## Testing Checklist

### Before Submission

- [ ] **All filters work independently** — each can be toggled without error
- [ ] **Empty state handled** — no crash when all data is filtered out
- [ ] **Numbers formatted** — currencies show $, percentages show %, large numbers use commas
- [ ] **Charts resize** — `use_container_width=True` on all Plotly charts
- [ ] **Responsive layout** — sidebar doesn't overlap main content
- [ ] **Loading feedback** — spinner for slow operations
- [ ] **Export works** — CSV and Excel downloads produce valid files
- [ ] **Session state** — widget values persist across reruns
- [ ] **Error handling** — try/except around data loading
- [ ] **Performance** — `@st.cache_data` on data loading functions
- [ ] **Code quality** — no `st.*` calls in data functions
- [ ] **Documentation** — README with setup instructions

### Demo Walkthrough

Record a 2-minute screen recording showing:
1. Loading the dashboard
2. Applying filters
3. Exploring charts
4. Viewing data table
5. Downloading data

---

## Grading Rubric

| Criteria | Points | Description |
|---|---|---|
| **Data Layer** | 20 | Clean data functions, caching, no st.* in data code |
| **Filters & Interactivity** | 20 | Working filters, reactive updates, session state |
| **KPIs & Metrics** | 15 | 4+ formatted metrics, meaningful deltas |
| **Charts & Visualization** | 20 | 3+ chart types, Plotly, proper labels |
| **Layout & UX** | 15 | Sidebar/main separation, progressive disclosure, empty states |
| **Export & Polish** | 10 | Download buttons, error handling, footer |
| **Total** | **100** | |

### Bonus Points (+10)

- [ ] Multi-page layout with `st.navigation`
- [ ] File upload for custom datasets
- [ ] Auto-refresh with `st.fragment(run_every=...)`
- [ ] Authentication or user personalization
- [ ] Performance optimization for 100K+ rows

---

## Extension Ideas

Once the basic dashboard works, consider adding:

1. **File Upload** — Let users upload their own CSV/Excel/JSON files
2. **Custom Charts** — Let users choose which columns to plot
3. **Date Comparison** — Compare current period vs previous period
4. **Drill-Down** — Click on a bar to see details for that category
5. **Report Generation** — Generate a PDF or HTML report from the current view
6. **Database Connection** — Load data from SQLite instead of CSV
7. **API Integration** — Fetch real-time data from a REST API
8. **ML Integration** — Add a simple model (e.g., linear regression) that updates with filters

---

## Submission

1. **GitHub Repository** — Push your code to a public GitHub repo
2. **README.md** — Include:
   - Project description
   - Screenshot of the dashboard
   - Setup instructions (`pip install -r requirements.txt`)
   - How to run (`streamlit run app.py`)
3. **Live Demo** — Deploy to Streamlit Community Cloud (free)
4. **Screen Recording** — 2-minute walkthrough (upload to YouTube or Loom)

---

## Related Materials

- 📖 Reading: [10 — Building Interactive Data Science Dashboards](../readings/10_interactive_dashboard.md)
- 📓 Notebook: [10 — Interactive Data Explorer](../notebooks/10_interactive_dashboard.ipynb)
- ✏️ Exercise: [10 — Dashboard Workshop](../exercises/10_dashboard_workshop.py)
- 🖥️ Demo App: [Interactive Data Explorer](../apps/10_interactive_data_explorer.py)
