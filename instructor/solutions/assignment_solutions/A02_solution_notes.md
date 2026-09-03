# A02 — Data Explorer: Solution Notes

> **👩‍🏫 Instructor Reference**
> *Architecture, key implementation, grading breakdown, and common errors.*

---

## Expected Architecture

```
A02_data_explorer.py     # Main application
README.md                # Documentation
screenshots/
  ├── explorer_1_filters.png
  ├── explorer_2_charts.png
  └── explorer_3_stats.png
```

Single-file is acceptable but must be well-organized with functions.

---

## Expected Approach

### Task 1: Data Loading (15 marks)

**Key implementation:**
```python
@st.cache_data
def load_sample_data():
    np.random.seed(42)
    return pd.DataFrame({
        "date": pd.date_range("2024-01-01", periods=500, freq="D"),
        "category": np.random.choice(["Electronics", "Clothing", "Food"], 500),
        "revenue": np.random.uniform(50, 500, 500).round(2),
    })

uploaded = st.file_uploader("Upload CSV/Excel", type=["csv", "xlsx"])

if uploaded:
    try:
        if uploaded.name.endswith(".csv"):
            df = pd.read_csv(uploaded)
        else:
            df = pd.read_excel(uploaded)
        st.write(f"**{uploaded.name}** — {len(df)} rows × {len(df.columns)} columns")
    except Exception as e:
        st.error(f"Error reading file: {e}")
        df = load_sample_data()
else:
    df = load_sample_data()
    st.info("Using sample data. Upload your own file above.")
```

**What to look for:**
- File type validation (csv/xlsx only)
- Graceful error handling for bad files
- Built-in sample data as fallback
- File info display (name, size, shape)

**Common deductions:**
- (-3) No file validation
- (-3) No error handling
- (-2) No sample data fallback
- (-1) No file info display

---

### Task 2: Interactive Filters (20 marks)

**Key implementation:**
```python
st.sidebar.header("Filters")

# Auto-detect column types
numeric_cols = df.select_dtypes(include="number").columns.tolist()
categorical_cols = df.select_dtypes(exclude="number").columns.tolist()

# Dynamic filters
if categorical_cols:
    cat_col = st.sidebar.selectbox("Filter column", categorical_cols)
    categories = df[cat_col].unique().tolist()
    selected = st.sidebar.multiselect(cat_col, categories, default=categories)
    df = df[df[cat_col].isin(selected)]

if numeric_cols:
    num_col = st.sidebar.selectbox("Range filter", numeric_cols)
    min_val, max_val = st.sidebar.slider(
        num_col, float(df[num_col].min()), float(df[num_col].max()),
        (float(df[num_col].min()), float(df[num_col].max()))
    )
    df = df[(df[num_col] >= min_val) & (df[num_col] <= max_val)]

st.write(f"Showing **{len(df)}** of **{original_len}** rows")
```

**Common deductions:**
- (-3) Hardcoded column names (won't work with different data)
- (-2) No reset/filter count
- (-2) Filters not in session state

---

### Task 3: Visualization (25 marks)

**Key charts expected:**
1. Bar chart for categorical distribution
2. Histogram for numeric distribution
3. Scatter plot for two numeric columns
4. Line chart for trends
5. At least one Plotly chart

**Common deductions:**
- (-3) Charts don't update with filters
- (-2) No chart titles
- (-2) Missing Plotly chart
- (-3) Wrong chart type for data

---

### Task 4: Statistics (15 marks)

**Expected:**
- KPI metrics (row count, column count, mean)
- `describe()` statistics
- Correlation matrix
- Missing values report

---

### Task 5: Export (10 marks)

**Expected:**
```python
csv = filtered_df.to_csv(index=False)
st.download_button(
    "📥 Download Filtered Data",
    csv,
    f"filtered_{datetime.now().strftime('%Y%m%d_%H%M')}.csv",
    "text/csv"
)
```

---

### Task 6: Session State (10 marks)

**Expected uses:**
- Filter selections persist across reruns
- Last uploaded file remembered
- Loading spinner during processing

---

## Grading Strategy

1. Run the app — does it start without errors?
2. Test with default sample data — do filters work?
3. Upload a real CSV — does it work with different data?
4. Test each chart — do they update?
5. Test download — does it work?
6. Check for session state usage

**Estimated grading time:** 10-15 minutes per student

---

## Common Class-Wide Issues

1. **Hardcoded column names** — Most common issue, prevents reuse
2. **Missing error handling for file upload** — Crashes on bad files
3. **Charts don't update** — Using raw df instead of filtered
4. **No session state** — Filters reset on every interaction
5. **Missing export** — 30% of students forget the download button
