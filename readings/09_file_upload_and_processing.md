# 09 — File Upload, Validation & Processing

> **📖 Reading · Module 06 · Intermediate**
> *Turn uploaded files into actionable insights — safely.*

---

## Learning Objectives

After completing this reading you will be able to:

- Use `st.file_uploader` to accept CSV, Excel, JSON, and other file types.
- Validate uploaded files by type, size, and content before processing.
- Read and parse uploaded files with Pandas.
- Detect and handle missing values, duplicates, and data type issues.
- Clean and transform raw data into analysis-ready DataFrames.
- Provide download buttons for processed data with `st.download_button`.
- Apply safe file handling practices to protect against untrusted uploads.

---

## 1. The Upload → Process → Download Pipeline

Every file-handling app follows the same flow:

```
UPLOAD → VALIDATE → READ → CLEAN → ANALYZE → VISUALIZE → DOWNLOAD
   │          │        │       │         │            │          │
   ▼          ▼        ▼       ▼         ▼            ▼          ▼
Widget   Check type  Parse   Handle    Charts,     Charts     CSV,
& size   & content   to DF   nulls,    tables,     & tables   Excel,
                      │     dtypes     metrics               JSON
                      ▼
                  Analysis-
                   ready DF
```

**The key insight:** Validation is not optional. Never trust uploaded data — always check before processing.

---

## 2. st.file_uploader — The Upload Widget

### Basic Single-File Upload

```python
import streamlit as st
import pandas as pd

uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df.head())
```

### Multi-File Upload

```python
uploaded_files = st.file_uploader(
    "Choose files",
    type=["csv", "xlsx", "json"],
    accept_multiple_files=True,
)

for file in uploaded_files:
    st.write(f"📄 **{file.name}** — {file.size:,} bytes")
```

### Per-Widget Size Limit (Streamlit ≥ 1.44)

```python
# Limit this specific uploader to 50 MB
uploaded = st.file_uploader(
    "Upload large file",
    type=["csv"],
    max_upload_size=50,  # MB
)
```

### Key Parameters

| Parameter | Purpose | Default |
|---|---|---|
| `label` | Text shown above the widget | Required |
| `type` | Allowed extensions (list or single) | `None` (all types) |
| `accept_multiple_files` | Accept one or many files | `False` |
| `max_upload_size` | Per-widget size limit in MB | `None` (uses global config) |
| `key` | Unique widget identifier | Auto-generated |
| `help` | Tooltip text | `None` |
| `disabled` | Disable the widget | `False` |
| `label_visibility` | Show, hide, or collapse label | `"visible"` |

### The UploadedFile Object

The returned object is a **BytesIO subclass** — it behaves like a file:

```python
uploaded = st.file_uploader("Upload", type=["csv"])
if uploaded:
    # uploaded.name    → "sales_data.csv"
    # uploaded.size    → 102400 (bytes)
    # uploaded.type    → "text/csv"
    # uploaded.seek(0) → reset read position
    # pd.read_csv(uploaded) → works directly
```

---

## 3. File Type Handling

### CSV Files

```python
uploaded = st.file_uploader("Upload CSV", type=["csv"])

if uploaded is not None:
    try:
        df = pd.read_csv(uploaded)
        st.success(f"Loaded {len(df):,} rows × {len(df.columns)} columns")
    except pd.errors.EmptyDataError:
        st.error("The CSV file is empty.")
    except pd.errors.ParserError:
        st.error("Could not parse the CSV file. Check the format.")
```

### Excel Files

```python
# Requires: pip install openpyxl
uploaded = st.file_uploader("Upload Excel", type=["xlsx", "xls"])

if uploaded is not None:
    try:
        # Let user choose a sheet
        xl = pd.ExcelFile(uploaded)
        sheet = st.selectbox("Select sheet", xl.sheet_names)
        df = pd.read_excel(xl, sheet_name=sheet)
        st.success(f"Loaded sheet '{sheet}': {len(df):,} rows")
    except Exception as e:
        st.error(f"Error reading Excel file: {e}")
```

### JSON Files

```python
uploaded = st.file_uploader("Upload JSON", type=["json"])

if uploaded is not None:
    try:
        import json
        data = json.load(uploaded)

        # Handle both list-of-records and nested JSON
        if isinstance(data, list):
            df = pd.json_normalize(data)
        elif isinstance(data, dict):
            # Try common structures
            if "data" in data:
                df = pd.json_normalize(data["data"])
            elif "results" in data:
                df = pd.json_normalize(data["results"])
            else:
                df = pd.json_normalize(data)

        st.dataframe(df.head())
    except json.JSONDecodeError:
        st.error("Invalid JSON format.")
```

### Multiple Formats in One Uploader

```python
uploaded = st.file_uploader(
    "Upload data file",
    type=["csv", "xlsx", "json"],
    help="Supported formats: CSV, Excel (.xlsx), JSON",
)

if uploaded is not None:
    suffix = uploaded.name.split(".")[-1].lower()

    if suffix == "csv":
        df = pd.read_csv(uploaded)
    elif suffix in ("xlsx", "xls"):
        df = pd.read_excel(uploaded)
    elif suffix == "json":
        import json
        data = json.load(uploaded)
        df = pd.json_normalize(data if isinstance(data, list) else [data])
    else:
        st.error(f"Unsupported file type: {suffix}")
        st.stop()

    st.dataframe(df.head())
```

---

## 4. File Validation

Never trust uploaded data. Validate at three levels:

### Level 1: Type & Size Validation

```python
MAX_SIZE_MB = 100

uploaded = st.file_uploader("Upload", type=["csv"])

if uploaded is not None:
    # Check file size
    size_mb = uploaded.size / (1024 * 1024)
    if size_mb > MAX_SIZE_MB:
        st.error(f"File too large: {size_mb:.1f} MB (max: {MAX_SIZE_MB} MB)")
        st.stop()

    st.info(f"File size: {size_mb:.1f} MB")
```

### Level 2: Content Validation

```python
if uploaded is not None:
    df = pd.read_csv(uploaded)

    # Check minimum rows
    if len(df) < 2:
        st.error("File must have at least 2 rows of data.")
        st.stop()

    # Check minimum columns
    if len(df.columns) < 1:
        st.error("File must have at least 1 column.")
        st.stop()

    # Check for required columns
    required_cols = ["date", "revenue", "product"]
    missing = [c for c in required_cols if c not in df.columns]
    if missing:
        st.error(f"Missing required columns: {', '.join(missing)}")
        st.info(f"Available columns: {', '.join(df.columns)}")
        st.stop()
```

### Level 3: Data Quality Validation

```python
if uploaded is not None:
    df = pd.read_csv(uploaded)

    # Report data quality issues
    issues = []

    # Check for all-null columns
    null_cols = [c for c in df.columns if df[c].isnull().all()]
    if null_cols:
        issues.append(f"All-null columns: {', '.join(null_cols)}")

    # Check for high-null columns (>50%)
    high_null = [c for c in df.columns if df[c].isnull().mean() > 0.5]
    if high_null:
        issues.append(f"High null columns (>50%): {', '.join(high_null)}")

    # Check for duplicate rows
    n_dupes = df.duplicated().sum()
    if n_dupes > 0:
        issues.append(f"{n_dupes:,} duplicate rows ({n_dupes/len(df)*100:.1f}%)")

    if issues:
        st.warning("**Data Quality Issues:**\n" + "\n".join(f"- {i}" for i in issues))
    else:
        st.success("Data quality check passed ✓")
```

---

## 5. Missing Values — Detection & Handling

### Detecting Missing Values

```python
df = pd.read_csv(uploaded)

# Summary of nulls
null_summary = pd.DataFrame({
    "Column": df.columns,
    "Null Count": df.isnull().sum().values,
    "Null %": (df.isnull().mean() * 100).round(1).values,
    "Dtype": df.dtypes.values,
}).sort_values("Null Count", ascending=False)

st.dataframe(null_summary, hide_index=True)
```

### Handling Strategies

```python
strategy = st.selectbox(
    "Missing value strategy",
    ["Drop rows with any null", "Drop columns >50% null", "Fill with mean", "Fill with median", "Fill with mode", "Fill with custom value"]
)

if strategy == "Drop rows with any null":
    df_clean = df.dropna()
elif strategy == "Drop columns >50% null":
    threshold = len(df) * 0.5
    df_clean = df.dropna(axis=1, thresh=threshold)
elif strategy == "Fill with mean":
    numeric_cols = df.select_dtypes(include="number").columns
    df_clean = df.copy()
    df_clean[numeric_cols] = df_clean[numeric_cols].fillna(df[numeric_cols].mean())
elif strategy == "Fill with median":
    numeric_cols = df.select_dtypes(include="number").columns
    df_clean = df.copy()
    df_clean[numeric_cols] = df_clean[numeric_cols].fillna(df[numeric_cols].median())
elif strategy == "Fill with mode":
    df_clean = df.fillna(df.mode().iloc[0])
elif strategy == "Fill with custom value":
    fill_val = st.text_input("Fill value", "0")
    df_clean = df.fillna(fill_val)

st.write(f"Rows before: {len(df):,} → After: {len(df_clean):,}")
```

---

## 6. Data Cleaning & Transformation

### Rename Columns

```python
# Standardize column names
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
```

### Fix Data Types

```python
# Auto-detect and convert dates
for col in df.columns:
    if df[col].dtype == "object":
        try:
            df[col] = pd.to_datetime(df[col])
        except (ValueError, TypeError):
            pass

# Convert numeric strings
for col in df.select_dtypes(include="object").columns:
    try:
        df[col] = pd.to_numeric(df[col].str.replace(",", "").str.replace("$", ""))
    except (ValueError, TypeError):
        pass
```

### Remove Duplicates

```python
n_before = len(df)
df = df.drop_duplicates()
n_removed = n_before - len(df)
if n_removed > 0:
    st.info(f"Removed {n_removed:,} duplicate rows")
```

### Filter Outliers

```python
numeric_cols = df.select_dtypes(include="number").columns
for col in numeric_cols:
    q1 = df[col].quantile(0.01)
    q99 = df[col].quantile(0.99)
    df = df[(df[col] >= q1) & (df[col] <= q99)]
```

---

## 7. Download — Exporting Processed Data

### Basic CSV Download

```python
st.download_button(
    label="📥 Download CSV",
    data=df.to_csv(index=False),
    file_name="processed_data.csv",
    mime="text/csv",
)
```

### Excel Download

```python
# Requires: pip install openpyxl
import io

buffer = io.BytesIO()
with pd.ExcelWriter(buffer, engine="openpyxl") as writer:
    df.to_excel(writer, index=False, sheet_name="Cleaned Data")

st.download_button(
    label="📥 Download Excel",
    data=buffer.getvalue(),
    file_name="processed_data.xlsx",
    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
)
```

### JSON Download

```python
st.download_button(
    label="📥 Download JSON",
    data=df.to_json(orient="records", indent=2),
    file_name="processed_data.json",
    mime="application/json",
)
```

### Download with Metadata

```python
import io
from datetime import datetime

# Create a multi-sheet workbook with metadata
buffer = io.BytesIO()
with pd.ExcelWriter(buffer, engine="openpyxl") as writer:
    df.to_excel(writer, index=False, sheet_name="Data")
    pd.DataFrame({
        "Property": ["Source File", "Rows", "Columns", "Generated", "Null Strategy"],
        "Value": [uploaded.name, len(df), len(df.columns), datetime.now().isoformat(), strategy],
    }).to_excel(writer, index=False, sheet_name="Metadata")

st.download_button(
    "📥 Download Report",
    data=buffer.getvalue(),
    file_name=f"report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx",
    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
)
```

---

## 8. Safe File Handling — Security

### The Threat Model

Uploaded files are **untrusted input**. Attackers can:

- Upload files with misleading extensions (e.g., `malware.exe` renamed to `data.csv`)
- Submit extremely large files to cause memory exhaustion (DoS)
- Include malicious content in cell values (XSS if rendered as HTML)
- Upload files with encoding tricks to bypass type checks

### Security Rules

#### Rule 1: Never Trust the File Extension

```python
# ❌ Bad — only checks extension
if uploaded.name.endswith(".csv"):
    df = pd.read_csv(uploaded)

# ✅ Better — checks type AND tries to parse
if uploaded.type == "text/csv" or uploaded.name.endswith(".csv"):
    try:
        df = pd.read_csv(uploaded)
    except pd.errors.ParserError:
        st.error("File is not a valid CSV.")
```

#### Rule 2: Enforce Size Limits

```python
# Global limit in .streamlit/config.toml:
# [server]
# maxUploadSize = 200  # MB

# Per-widget limit:
uploaded = st.file_uploader("Upload", max_upload_size=10)  # 10 MB
```

#### Rule 3: Never Write Uploaded Files to Disk Without Sanitization

```python
# ❌ Bad — path traversal vulnerability
import os
path = os.path.join("uploads", uploaded.name)
with open(path, "wb") as f:
    f.write(uploaded.getbuffer())

# ✅ Better — sanitize filename
import re
safe_name = re.sub(r"[^a-zA-Z0-9._-]", "_", uploaded.name)
path = os.path.join("uploads", safe_name)
```

#### Rule 4: Don't Render Raw Cell Values as HTML

```python
# ❌ Dangerous — user could inject <script> tags
st.markdown(df.to_html(), unsafe_allow_html=True)

# ✅ Safe — use st.dataframe or st.table
st.dataframe(df)
```

#### Rule 5: Validate Data Types After Parsing

```python
# After reading, verify expected types
expected_types = {"date": "datetime64", "revenue": "float64", "product": "object"}
for col, expected in expected_types.items():
    if col in df.columns and str(df[col].dtype) != expected:
        st.warning(f"Column '{col}' has unexpected type: {df[col].dtype} (expected {expected})")
```

#### Rule 6: Limit Rows Processed

```python
MAX_ROWS = 1_000_000
if len(df) > MAX_ROWS:
    st.warning(f"File has {len(df):,} rows. Processing first {MAX_ROWS:,}.")
    df = df.head(MAX_ROWS)
```

### Security Checklist

| Check | Why | How |
|---|---|---|
| Validate file type | Prevent executable uploads | `type=["csv", "xlsx"]` + content check |
| Enforce size limits | Prevent memory exhaustion | `max_upload_size` parameter |
| Sanitize filenames | Prevent path traversal | `re.sub(r"[^a-zA-Z0-9._-]", "_", name)` |
| Don't render raw HTML | Prevent XSS | Use `st.dataframe`, not `st.markdown(df.to_html())` |
| Validate data types | Catch malformed data | Check dtypes after parsing |
| Limit row count | Prevent processing overhead | `df.head(MAX_ROWS)` |
| Log uploads | Audit trail | `st.write(f"Uploaded: {name} ({size} bytes)")` |

---

## 9. Common Mistakes

### Mistake 1: Not Handling None (No Upload)

```python
# ❌ Crashes if no file uploaded
df = pd.read_csv(uploaded)  # TypeError if uploaded is None

# ✅ Always check first
if uploaded is not None:
    df = pd.read_csv(uploaded)
```

### Mistake 2: Reading File Multiple Times

```python
# ❌ File position advances on each read
if uploaded:
    pd.read_csv(uploaded)   # Reads OK
    pd.read_csv(uploaded)   # Returns empty — file position is at end

# ✅ Reset position or read once
if uploaded:
    uploaded.seek(0)
    df = pd.read_csv(uploaded)
    # Use `df` everywhere — don't re-read the file
```

### Mistake 3: No Error Handling

```python
# ❌ Crashes on bad files
df = pd.read_csv(uploaded)

# ✅ Graceful error handling
try:
    df = pd.read_csv(uploaded)
except pd.errors.EmptyDataError:
    st.error("The file is empty.")
except pd.errors.ParserError:
    st.error("Could not parse the file. Is it a valid CSV?")
except UnicodeDecodeError:
    st.error("File encoding issue. Try saving as UTF-8.")
```

### Mistake 4: Ignoring Encoding Issues

```python
# ✅ Try multiple encodings
for encoding in ["utf-8", "latin-1", "cp1252"]:
    try:
        df = pd.read_csv(uploaded, encoding=encoding)
        break
    except UnicodeDecodeError:
        uploaded.seek(0)
        continue
else:
    st.error("Could not read file with any supported encoding.")
    st.stop()
```

---

## Key Takeaways

- **`st.file_uploader`** returns a BytesIO-like object — pass it directly to `pd.read_csv()`, `pd.read_excel()`, etc.
- **Always validate** before processing: check type, size, columns, and data quality.
- **Handle missing values explicitly** — let the user choose the strategy.
- **`st.download_button`** accepts strings, bytes, or file-like objects — use `io.BytesIO()` for Excel.
- **Security is not optional** — never trust file extensions, sanitize filenames, enforce size limits, and never render raw HTML from uploaded data.
- **Reset file position** with `seek(0)` if you need to read the file twice.
- **Graceful errors** — always wrap parsing in try/except and provide clear feedback.

---

## Further Reading

- [st.file_uploader API Reference](https://docs.streamlit.io/develop/api-reference/widgets/st.file_uploader)
- [st.download_button API Reference](https://docs.streamlit.io/develop/api-reference/widgets/st.download_button)
- [Streamlit File Uploader Guide](https://docs.streamlit.io/develop/concepts/design/files-and-uploads)
- [OWASP File Upload Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html)

---

## Related Materials

- 📓 Notebook: [09 — File Upload & Processing](../notebooks/09_file_upload_and_processing.ipynb)
- ✏️ Exercise: [09 — File Upload Workshop](../exercises/09_file_upload_workshop.py)
- 🖥️ Demo App: [09 — File Upload Demo](../apps/09_file_upload_demo.py)
- 📝 Quiz: [06 — File Upload & Processing](../quizzes/06_file_upload.md)
