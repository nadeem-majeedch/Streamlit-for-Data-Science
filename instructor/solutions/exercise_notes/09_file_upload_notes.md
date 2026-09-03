# Exercise 09 — File Upload Workshop: Solution Notes

> **👩‍🏫 Instructor Reference**
> *Expected approach, key code, and grading guidance.*

---

## Challenge 1: Multi-Format Uploader

### Expected Approach
- `st.file_uploader` with `type=["csv", "xlsx", "json"]`
- Detect type from filename extension
- Branch reading logic per format
- Display file info and preview

### Key Code
```python
uploaded = st.file_uploader("Upload data file", type=["csv", "xlsx", "json"])

if uploaded:
    suffix = uploaded.name.split(".")[-1].lower()
    st.write(f"**File:** {uploaded.name} · **Size:** {uploaded.size / 1024:.1f} KB")

    if suffix == "csv":
        df = pd.read_csv(uploaded)
    elif suffix in ("xlsx", "xls"):
        df = pd.read_excel(uploaded)
    elif suffix == "json":
        import json
        data = json.load(uploaded)
        df = pd.json_normalize(data if isinstance(data, list) else [data])

    st.success(f"Loaded: {len(df)} rows × {len(df.columns)} columns")
    st.dataframe(df.head(10), use_container_width=True)
```

### Common Mistakes
- Not handling JSON nested data (needs `json_normalize`)
- Not checking file extension before reading
- No try/except around file reading

### Grading Notes (15 marks)
- Full marks: All 3 formats work, file info displayed, preview shown
- 10 marks: 2 formats work
- 5 marks: 1 format works

---

## Challenge 2: Data Quality Reporter

### Expected Approach
- CSV-only uploader
- 3 tabs: Overview (KPIs), Nulls (column analysis), Types (schema info)

### Key Code
```python
tab1, tab2, tab3 = st.tabs(["Overview", "Nulls", "Types"])

with tab1:
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Rows", f"{len(df):,}")
    c2.metric("Columns", len(df.columns))
    c3.metric("Null Cells", f"{df.isnull().sum().sum():,}")
    c4.metric("Duplicates", f"{df.duplicated().sum():,}")

with tab2:
    null_df = pd.DataFrame({
        "Column": df.columns,
        "Null Count": df.isnull().sum().values,
        "Null %": (df.isnull().mean() * 100).round(1).values,
    }).sort_values("Null %", ascending=False)
    st.dataframe(null_df, hide_index=True)

with tab3:
    type_df = pd.DataFrame({
        "Column": df.columns,
        "Dtype": df.dtypes.values,
        "Non-Null": df.notnull().sum().values,
    })
    st.dataframe(type_df, hide_index=True)
```

### Grading Notes (15 marks)
- Full marks: All 3 tabs with correct computations
- 10 marks: 2 tabs working correctly
- 5 marks: 1 tab working

---

## Challenge 3: Custom Cleaning Pipeline

### Expected Approach
- File uploader + checkboxes for cleaning options
- Apply steps in order, track changes
- Before/after comparison with download

### Key Code (cleaning logic)
```python
df_cleaned = df_original.copy()
changes = []

if remove_dupes:
    n = len(df_cleaned)
    df_cleaned = df_cleaned.drop_duplicates()
    changes.append(f"Removed {n - len(df_cleaned)} duplicates")

if fix_names:
    df_cleaned.columns = df_cleaned.columns.str.strip().str.lower().str.replace(" ", "_")
    changes.append("Standardized column names")

if drop_null_cols:
    thresh = len(df_cleaned) * 0.5
    before = len(df_cleaned.columns)
    df_cleaned = df_cleaned.dropna(axis=1, thresh=thresh)
    changes.append(f"Dropped {before - len(df_cleaned)} high-null columns")

if fill_nulls:
    numeric_cols = df_cleaned.select_dtypes(include="number").columns
    for col in numeric_cols:
        median = df_cleaned[col].median()
        filled = df_cleaned[col].isnull().sum()
        df_cleaned[col] = df_cleaned[col].fillna(median)
        if filled > 0:
            changes.append(f"Filled {filled} nulls in '{col}' with median ({median:.2f})")
```

### Common Mistakes
- Not creating a copy before modifying
- Not tracking changes for the summary
- Applying fill before drop (should drop first)

### Grading Notes (15 marks)
- Full marks: All 4 options work, before/after comparison, download
- 10 marks: 3 options work, summary present
- 5 marks: 1-2 options work

---

## Challenge 4: Encoding & Validation (if present)

### Key Points
- Check for UTF-8 encoding with `encoding` parameter
- Validate expected columns before processing
- Handle edge cases: empty files, single-row files
