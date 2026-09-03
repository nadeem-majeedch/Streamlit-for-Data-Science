"""
✏️ Exercise 09 — File Upload Workshop
=======================================
Module 06 · Intermediate

Master file upload, validation, processing, and download in Streamlit.

Run this file:
    streamlit run exercises/09_file_upload_workshop.py

Instructions:
    Complete each challenge independently. Do NOT copy code from the notebooks.
    Each challenge builds different skills — read the requirements carefully.

Related Materials:
- 📖 Reading: ../readings/09_file_upload_and_processing.md
- 📓 Notebook: ../notebooks/09_file_upload_and_processing.ipynb
- 🖥️ Demo App: ../apps/09_file_upload_demo.py
"""

import streamlit as st
import pandas as pd
import numpy as np
import io

# ---------------------------------------------------------------------------
# Page Config
# ---------------------------------------------------------------------------
st.set_page_config(
    page_title="Exercise 09 — File Upload Workshop",
    page_icon="✏️",
    layout="wide",
)

st.title("✏️ Exercise 09 — File Upload Workshop")
st.markdown(
    "Master file upload, validation, processing, and download.\n"
    "Complete each challenge independently."
)

st.divider()

# ---------------------------------------------------------------------------
# Challenge 1: Multi-Format Uploader
# ---------------------------------------------------------------------------
st.header("Challenge 1 — Multi-Format Uploader")

st.markdown(
    "**Task:** Build an uploader that accepts CSV, Excel, and JSON files.\n"
    "For each format, display file info and preview."
)

# TODO 1: Create a file_uploader that accepts csv, xlsx, json
# TODO 2: Detect the file type from the extension
# TODO 3: Read the file into a DataFrame based on its type
# TODO 4: Display: file name, size (formatted), rows, columns
# TODO 5: Show first 10 rows with st.dataframe

# --- START YOUR CODE HERE ---
# uploaded = st.file_uploader(
#     "Upload a data file",
#     type=["csv", "xlsx", "json"],
#     key="challenge1",
# )
#
# if uploaded is not None:
#     suffix = uploaded.name.split(".")[-1].lower()
#
#     # Display file info
#     st.write(f"**File:** {uploaded.name}")
#     st.write(f"**Size:** {uploaded.size / 1024:.1f} KB")
#     st.write(f"**Type:** {suffix.upper()}")
#
#     # Read based on type
#     try:
#         if suffix == "csv":
#             df = pd.read_csv(uploaded)
#         elif suffix in ("xlsx", "xls"):
#             df = pd.read_excel(uploaded)
#         elif suffix == "json":
#             import json
#             data = json.load(uploaded)
#             df = pd.json_normalize(data if isinstance(data, list) else [data])
#         else:
#             st.error("Unsupported format")
#             st.stop()
#
#         st.success(f"Loaded: {len(df)} rows × {len(df.columns)} columns")
#         st.dataframe(df.head(10), use_container_width=True)
#
#     except Exception as e:
#         st.error(f"Error reading file: {e}")
# --- END YOUR CODE HERE ---

st.divider()

# ---------------------------------------------------------------------------
# Challenge 2: Data Quality Reporter
# ---------------------------------------------------------------------------
st.header("Challenge 2 — Data Quality Reporter")

st.markdown(
    "**Task:** Upload a CSV and generate a comprehensive quality report.\n"
    "Display results in a tabbed layout."
)

# TODO 1: Create a file_uploader for CSV only
# TODO 2: After upload, create 3 tabs: Overview, Nulls, Types
# TODO 3: Overview tab: rows, columns, total nulls, total duplicates, memory usage
# TODO 4: Nulls tab: DataFrame showing each column's null count and null percentage
# TODO 5: Types tab: DataFrame showing column names, data types, non-null count, sample values

# --- START YOUR CODE HERE ---
# uploaded_qr = st.file_uploader("Upload CSV for quality report", type=["csv"], key="challenge2")
#
# if uploaded_qr is not None:
#     df_qr = pd.read_csv(uploaded_qr)
#
#     tab1, tab2, tab3 = st.tabs(["Overview", "Nulls", "Types"])
#
#     with tab1:
#         c1, c2, c3, c4 = st.columns(4)
#         c1.metric("Rows", f"{len(df_qr):,}")
#         c2.metric("Columns", len(df_qr.columns))
#         c3.metric("Null Cells", f"{df_qr.isnull().sum().sum():,}")
#         c4.metric("Duplicates", f"{df_qr.duplicated().sum():,}")
#
#     with tab2:
#         null_df = pd.DataFrame({
#             "Column": df_qr.columns,
#             "Null Count": df_qr.isnull().sum().values,
#             "Null %": (df_qr.isnull().mean() * 100).round(1).values,
#         }).sort_values("Null %", ascending=False)
#         st.dataframe(null_df, hide_index=True, use_container_width=True)
#
#     with tab3:
#         type_df = pd.DataFrame({
#             "Column": df_qr.columns,
#             "Dtype": df_qr.dtypes.values,
#             "Non-Null": df_qr.notnull().sum().values,
#             "Sample": [str(df_qr[col].dropna().iloc[0]) if df_qr[col].notnull().any() else "N/A"
#                        for col in df_qr.columns],
#         })
#         st.dataframe(type_df, hide_index=True, use_container_width=True)
# --- END YOUR CODE HERE ---

st.divider()

# ---------------------------------------------------------------------------
# Challenge 3: Custom Cleaning Pipeline
# ---------------------------------------------------------------------------
st.header("Challenge 3 — Custom Cleaning Pipeline")

st.markdown(
    "**Task:** Build a cleaning app with user-controlled options.\n"
    "Show before/after comparison and provide download."
)

# TODO 1: Create a file_uploader for CSV
# TODO 2: After upload, show cleaning options using checkboxes:
#    - Remove duplicate rows
#    - Standardize column names (lowercase, strip, replace spaces)
#    - Drop columns with >50% null values
#    - Fill remaining numeric nulls with median
# TODO 3: Apply selected cleaning steps in order
# TODO 4: Show before/after in tabs
# TODO 5: Show cleaning summary (rows removed, nulls filled, etc.)
# TODO 6: Provide download button for cleaned CSV

# --- START YOUR CODE HERE ---
# uploaded_clean = st.file_uploader("Upload CSV to clean", type=["csv"], key="challenge3")
#
# if uploaded_clean is not None:
#     df_original = pd.read_csv(uploaded_clean)
#
#     st.subheader("Cleaning Options")
#     col1, col2 = st.columns(2)
#     with col1:
#         remove_dupes = st.checkbox("Remove duplicates", value=True)
#         fix_names = st.checkbox("Standardize column names", value=True)
#     with col2:
#         drop_null_cols = st.checkbox("Drop columns >50% null", value=False)
#         fill_nulls = st.checkbox("Fill numeric nulls with median", value=True)
#
#     # Apply cleaning
#     df_cleaned = df_original.copy()
#     changes = []
#
#     if fix_names:
#         df_cleaned.columns = df_cleaned.columns.str.strip().str.lower().str.replace(" ", "_")
#         changes.append("Standardized column names")
#
#     if remove_dupes:
#         n = len(df_cleaned)
#         df_cleaned = df_cleaned.drop_duplicates()
#         removed = n - len(df_cleaned)
#         if removed > 0:
#             changes.append(f"Removed {removed} duplicate rows")
#
#     if drop_null_cols:
#         threshold = len(df_cleaned) * 0.5
#         before = len(df_cleaned.columns)
#         df_cleaned = df_cleaned.dropna(axis=1, thresh=threshold)
#         dropped = before - len(df_cleaned.columns)
#         if dropped > 0:
#             changes.append(f"Dropped {dropped} high-null columns")
#
#     if fill_nulls:
#         num_cols = df_cleaned.select_dtypes(include="number").columns
#         filled = df_cleaned[num_cols].isnull().sum().sum()
#         df_cleaned[num_cols] = df_cleaned[num_cols].fillna(df_cleaned[num_cols].median())
#         if filled > 0:
#             changes.append(f"Filled {filled} numeric nulls with median")
#
#     # Show results
#     tab_before, tab_after = st.tabs(["Before", "After"])
#     with tab_before:
#         st.dataframe(df_original.head(20), use_container_width=True, height=300)
#     with tab_after:
#         st.dataframe(df_cleaned.head(20), use_container_width=True, height=300)
#
#     st.write(f"**Changes:** {'; '.join(changes) if changes else 'No changes applied'}")
#
#     # Download
#     st.download_button(
#         "📥 Download Cleaned CSV",
#         data=df_cleaned.to_csv(index=False),
#         file_name="cleaned_data.csv",
#         mime="text/csv",
#         type="primary",
#     )
# --- END YOUR CODE HERE ---

st.divider()

# ---------------------------------------------------------------------------
# Challenge 4: Security Validation (Bonus)
# ---------------------------------------------------------------------------
st.header("Challenge 4 — Security Validation (Bonus)")

st.markdown(
    "**Task:** Implement a secure upload handler with multiple safety checks."
)

# TODO 1: Create a file_uploader with max_upload_size=5
# TODO 2: Validate file type by checking BOTH extension AND content
# TODO 3: Check for required columns (e.g., "name", "date", "value")
# TODO 4: Limit to first 10,000 rows max
# TODO 5: Display security status with st.success/st.warning/st.error

# --- START YOUR CODE HERE ---
# uploaded_sec = st.file_uploader(
#     "Secure upload (max 5MB, CSV only)",
#     type=["csv"],
#     max_upload_size=5,
#     key="challenge4",
# )
#
# if uploaded_sec is not None:
#     st.subheader("Security Report")
#
#     # Size check
#     size_mb = uploaded_sec.size / (1024 * 1024)
#     if size_mb > 5:
#         st.error(f"❌ File too large: {size_mb:.1f} MB (max: 5 MB)")
#         st.stop()
#     st.success(f"✅ Size check passed: {size_mb:.2f} MB")
#
#     # Content check
#     try:
#         uploaded_sec.seek(0)
#         df_sec = pd.read_csv(uploaded_sec)
#         st.success("✅ Content is valid CSV")
#     except Exception as e:
#         st.error(f"❌ Invalid CSV content: {e}")
#         st.stop()
#
#     # Column check
#     required = ["name", "date", "value"]
#     missing = [c for c in required if c not in df_sec.columns.str.lower()]
#     if missing:
#         st.warning(f"⚠️ Missing recommended columns: {', '.join(missing)}")
#     else:
#         st.success("✅ All required columns present")
#
#     # Row limit
#     if len(df_sec) > 10000:
#         st.warning(f"⚠️ File has {len(df_sec):,} rows. Limiting to 10,000.")
#         df_sec = df_sec.head(10000)
#     else:
#         st.success(f"✅ Row count OK: {len(df_sec):,}")
#
#     st.dataframe(df_sec, use_container_width=True, height=300)
# --- END YOUR CODE HERE ---

# ---------------------------------------------------------------------------
# Footer
# ---------------------------------------------------------------------------
st.divider()
st.caption(
    "Exercise 09 — File Upload Workshop · Module 06 · Streamlit for Data Science"
)
