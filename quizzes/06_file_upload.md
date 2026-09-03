# Quiz 06 — File Upload & Processing

> **📝 Quiz · Module 06 · Intermediate**
> *Test your understanding of file upload, validation, processing, and download in Streamlit.*
> ⏱ Time: 20 minutes · 📊 Points: 24

---

## Instructions

Answer all questions. For multiple-choice questions, circle the correct answer. For code questions, write the complete code.

---

## Part A: Multiple Choice (2 points each)

### Q1. What does `st.file_uploader()` return when no file has been uploaded?

(a) An empty string `""`  \
(b) An empty list `[]`  \
(c) `None`  \
(d) `0`

---

### Q2. How do you restrict a file uploader to accept only CSV files?

(a) `st.file_uploader("Upload", type="csv")`  \
(b) `st.file_uploader("Upload", accept=".csv")`  \
(c) `st.file_uploader("Upload", extensions=["csv"])`  \
(d) Both (a) and a list `type=["csv"]` work

---

### Q3. What is the purpose of `max_upload_size` in `st.file_uploader()`?

(a) Limits the number of rows in the uploaded file  \
(b) Limits the file size in megabytes per widget  \
(c) Limits the number of columns  \
(d) Limits the total upload count per session

---

### Q4. Why should you call `uploaded.seek(0)` before reading a file a second time?

(a) To compress the file  \
(b) To reset the read position to the beginning  \
(c) To validate the file type  \
(d) To convert the file to UTF-8

---

### Q5. What happens if you try `pd.read_csv(uploaded)` without checking if `uploaded is not None`?

(a) It returns an empty DataFrame  \
(b) It raises a `TypeError`  \
(c) It raises a `FileNotFoundError`  \
(d) It works fine — Streamlit handles it

---

### Q6. Which of these is a security risk when handling uploaded files?

(a) Using `st.dataframe()` to display data  \
(b) Using `st.markdown(df.to_html(), unsafe_allow_html=True)` to display data  \
(c) Checking `uploaded.size` before processing  \
(d) Using `pd.read_csv()` to parse the file

---

### Q7. How do you provide a download button for a Pandas DataFrame as CSV?

(a) `st.download_button("Download", df)`  \
(b) `st.download_button("Download", df.to_csv(index=False), file_name="data.csv")`  \
(c) `st.download_button("Download", str(df), file_name="data.csv")`  \
(d) `df.download("data.csv")`

---

### Q8. What encoding should you try first when `pd.read_csv()` raises a `UnicodeDecodeError`?

(a) `encoding="ascii"`  \
(b) `encoding="utf-8"`  \
(c) `encoding="latin-1"`  \
(d) `encoding="binary"`

---

## Part B: Short Answer (3 points each)

### Q9. Explain the difference between the three levels of file validation: type/size, content, and data quality. Give one example check for each level.

---

### Q10. A user uploads a CSV file, but when they try to read it a second time with `pd.read_csv()`, it returns empty. Explain why this happens and how to fix it.

---

### Q11. Describe the complete UPLOAD → VALIDATE → READ → CLEAN → ANALYZE → VISUALIZE → DOWNLOAD pipeline. What Streamlit widget or function is used at each step?

---

### Q12. List three security best practices when handling untrusted file uploads in a Streamlit app.

---

## Part C: Code Completion (4 points)

### Q13. Complete this code to create a safe file upload handler:

```python
import streamlit as st
import pandas as pd

uploaded = st.file_uploader(
    "Upload CSV",
    type=["______"],
    max_upload_size=______,
)

if uploaded is not None:
    try:
        uploaded.______(0)  # Reset read position
        df = pd.read_csv(uploaded)
        st.success(f"Loaded {len(df):,} rows")
    except pd.errors.______:
        st.error("The file is empty.")
    except pd.errors.______:
        st.error("Could not parse the CSV file.")
except UnicodeDecodeError:
        st.error("Encoding issue. Try saving as UTF-8.")
```

---

### Q14. Complete this code to provide multiple download formats:

```python
import io

# CSV download
st.download_button(
    label="📥 Download CSV",
    data=df.______(index=False),
    file_name="data.csv",
    mime="text/csv",
)

# Excel download
buffer = io.______()
with pd.ExcelWriter(buffer, engine="openpyxl") as writer:
    df.to_excel(writer, index=False, sheet_name="Data")

st.download_button(
    label="📥 Download Excel",
    data=buffer.______(),
    file_name="data.xlsx",
)
```

---

## Answer Key (Instructor Only)

> **A1:** (c) `None`
>
> **A2:** (d) Both (a) and a list `type=["csv"]` work
>
> **A3:** (b) Limits the file size in megabytes per widget
>
> **A4:** (b) To reset the read position to the beginning
>
> **A5:** (b) It raises a `TypeError`
>
> **A6:** (b) Using `st.markdown(df.to_html(), unsafe_allow_html=True)` — potential XSS
>
> **A7:** (b) `st.download_button("Download", df.to_csv(index=False), file_name="data.csv")`
>
> **A8:** (c) `encoding="latin-1"` — it can decode almost any byte sequence
>
> **A9:** Level 1 (Type/Size): Check file extension, MIME type, and size against limits. Example: `if uploaded.size > MAX_SIZE: st.error("Too large")`. Level 2 (Content): Verify the file can be parsed correctly. Example: Wrap `pd.read_csv()` in try/except. Level 3 (Data Quality): Check for nulls, duplicates, wrong types after parsing. Example: `df.isnull().sum()` to find missing values.
>
> **A10:** The file's read position advances to the end after the first `read_csv()`. On the second call, there's nothing left to read. Fix: call `uploaded.seek(0)` before the second read, or read once and store the result in a variable.
>
> **A11:** Upload: `st.file_uploader()`. Validate: Check `uploaded.type`, `uploaded.size`, try/except on read. Read: `pd.read_csv()`/`pd.read_excel()`/`json.load()`. Clean: `dropna()`, `drop_duplicates()`, column renaming, type conversion. Analyze: `df.describe()`, `df.groupby()`, correlation. Visualize: `st.bar_chart()`, `st.line_chart()`, Plotly/Matplotlib. Download: `st.download_button()` with `df.to_csv()`.
>
> **A12:** (1) Enforce size limits with `max_upload_size`. (2) Sanitize filenames with regex before writing to disk. (3) Never render raw HTML from uploaded data — use `st.dataframe()` instead of `st.markdown(df.to_html())`. (4) Validate file type by checking both extension AND content. (5) Limit the number of rows processed.
>
> **A13:** `"csv"`, `100` (or any integer), `seek(0)`, `EmptyDataError`, `ParserError`
>
> **A14:** `to_csv`, `BytesIO`, `getvalue`

---

## Related Materials

- 📖 Reading: [09 — File Upload, Validation & Processing](../readings/09_file_upload_and_processing.md)
- 📓 Notebook: [09 — File Upload & Processing](../notebooks/09_file_upload_and_processing.ipynb)
- ✏️ Exercise: [09 — File Upload Workshop](../exercises/09_file_upload_workshop.py)
- 🖥️ Demo App: [09 — File Upload & Processing Dashboard](../apps/09_file_upload_demo.py)
