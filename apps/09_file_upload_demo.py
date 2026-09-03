"""
🖥️ Demo App 09 — File Upload & Processing Dashboard
=====================================================
A complete dashboard demonstrating file upload, validation,
data cleaning, analysis, visualization, and download.

Run this app:
    streamlit run apps/09_file_upload_demo.py

Related Materials:
- 📖 Reading: ../readings/09_file_upload_and_processing.md
- 📓 Notebook: ../notebooks/09_file_upload_and_processing.ipynb
- ✏️ Exercise: ../exercises/09_file_upload_workshop.py
"""

import streamlit as st
import pandas as pd
import numpy as np
import json
import io
from datetime import datetime

# ---------------------------------------------------------------------------
# Page Config
# ---------------------------------------------------------------------------
st.set_page_config(
    page_title="09 — File Upload & Processing",
    page_icon="📤",
    layout="wide",
)

# ---------------------------------------------------------------------------
# Helper Functions
# ---------------------------------------------------------------------------

def read_uploaded_file(uploaded_file):
    """Read an uploaded file into a DataFrame based on its extension."""
    suffix = uploaded_file.name.split(".")[-1].lower()

    if suffix == "csv":
        # Try multiple encodings
        for encoding in ["utf-8", "latin-1", "cp1252"]:
            try:
                uploaded_file.seek(0)
                return pd.read_csv(uploaded_file, encoding=encoding), suffix
            except UnicodeDecodeError:
                continue
        raise ValueError("Could not read CSV with any supported encoding (utf-8, latin-1, cp1252).")

    elif suffix in ("xlsx", "xls"):
        return pd.read_excel(uploaded_file), suffix

    elif suffix == "json":
        uploaded_file.seek(0)
        data = json.load(uploaded_file)
        if isinstance(data, list):
            return pd.json_normalize(data), suffix
        elif isinstance(data, dict):
            for key in ["data", "results", "records", "items"]:
                if key in data:
                    data = data[key]
                    break
            return pd.json_normalize(data if isinstance(data, list) else [data]), suffix
        else:
            raise ValueError("Unrecognized JSON structure.")

    else:
        raise ValueError(f"Unsupported file type: {suffix}")


def validate_file(uploaded_file, max_size_mb=100):
    """Validate file type and size. Returns (is_valid, message)."""
    if uploaded_file is None:
        return False, "No file uploaded."

    suffix = uploaded_file.name.split(".")[-1].lower()
    allowed = ["csv", "xlsx", "xls", "json"]
    if suffix not in allowed:
        return False, f"Unsupported file type: .{suffix}. Allowed: {', '.join(allowed)}"

    size_mb = uploaded_file.size / (1024 * 1024)
    if size_mb > max_size_mb:
        return False, f"File too large: {size_mb:.1f} MB (max: {max_size_mb} MB)"

    return True, f"Valid {suffix.upper()} file ({size_mb:.1f} MB)"


def get_quality_summary(df):
    """Generate a data quality summary DataFrame."""
    null_counts = df.isnull().sum()
    return pd.DataFrame({
        "Column": df.columns,
        "Type": [str(dt) for dt in df.dtypes],
        "Non-Null": df.notnull().sum().values,
        "Null Count": null_counts.values,
        "Null %": (null_counts / len(df) * 100).round(1).values,
        "Unique": [df[c].nunique() for c in df.columns],
    }).sort_values("Null Count", ascending=False)


# ---------------------------------------------------------------------------
# Title
# ---------------------------------------------------------------------------
st.title("📤 File Upload & Processing Dashboard")
st.caption("UPLOAD → VALIDATE → READ → CLEAN → ANALYZE → VISUALIZE → DOWNLOAD")

st.divider()

# ---------------------------------------------------------------------------
# Sidebar
# ---------------------------------------------------------------------------
with st.sidebar:
    st.header("⚙️ Settings")
    max_size = st.slider("Max file size (MB)", 1, 200, 100)
    max_rows = st.number_input("Max rows to process", 1000, 1000000, 100000, step=1000)

    st.divider()
    st.header("📋 Pipeline")
    st.markdown(
        "1. 📤 Upload file\n"
        "2. ✅ Validate\n"
        "3. 📖 Read data\n"
        "4. 🧹 Clean data\n"
        "5. 📊 Analyze\n"
        "6. 📥 Download"
    )

# ---------------------------------------------------------------------------
# Step 1: Upload & Validate
# ---------------------------------------------------------------------------
st.header("📤 Step 1 — Upload & Validate")

uploaded = st.file_uploader(
    "Upload a data file (CSV, Excel, or JSON)",
    type=["csv", "xlsx", "xls", "json"],
    max_upload_size=max_size,
    help="Supported formats: CSV, Excel (.xlsx), JSON",
)

if uploaded is not None:
    is_valid, message = validate_file(uploaded, max_size)

    if is_valid:
        st.success(f"✅ {message}")
    else:
        st.error(f"❌ {message}")
        st.stop()

    # Step 2: Read
    st.header("📖 Step 2 — Read Data")

    try:
        df, file_type = read_uploaded_file(uploaded)
    except Exception as e:
        st.error(f"Error reading file: {e}")
        st.stop()

    # Row limit
    if len(df) > max_rows:
        st.warning(f"⚠️ File has {len(df):,} rows. Processing first {max_rows:,}.")
        df = df.head(max_rows)

    # File info
    info_col1, info_col2, info_col3, info_col4 = st.columns(4)
    info_col1.metric("Rows", f"{len(df):,}")
    info_col2.metric("Columns", len(df.columns))
    info_col3.metric("Null Cells", f"{df.isnull().sum().sum():,}")
    info_col4.metric("Memory", f"{df.memory_usage(deep=True).sum() / 1024:.0f} KB")

    st.divider()

    # Step 3: Data Quality
    st.header("🔍 Step 3 — Data Quality")

    quality_df = get_quality_summary(df)

    tab_raw, tab_quality, tab_stats = st.tabs(["Raw Data", "Quality Report", "Statistics"])

    with tab_raw:
        st.dataframe(df, use_container_width=True, height=400)

    with tab_quality:
        st.dataframe(quality_df, hide_index=True, use_container_width=True)

        # Duplicates
        n_dupes = df.duplicated().sum()
        if n_dupes > 0:
            st.warning(f"⚠️ {n_dupes:,} duplicate rows ({n_dupes/len(df)*100:.1f}%)")
        else:
            st.success("✅ No duplicate rows found.")

    with tab_stats:
        numeric_df = df.select_dtypes(include="number")
        if len(numeric_df.columns) > 0:
            st.dataframe(numeric_df.describe(), use_container_width=True)
        else:
            st.info("No numeric columns found.")

    st.divider()

    # Step 4: Clean
    st.header("🧹 Step 4 — Clean Data")

    clean_col1, clean_col2 = st.columns(2)

    with clean_col1:
        st.subheader("Cleaning Options")
        fix_names = st.checkbox("Standardize column names", value=True, key="demo_fix_names")
        remove_dupes = st.checkbox("Remove duplicates", value=True, key="demo_remove_dupes")
        drop_high_null = st.checkbox("Drop columns >50% null", value=False, key="demo_drop_null")

    with clean_col2:
        st.subheader("Missing Value Strategy")
        null_strategy = st.selectbox(
            "How to handle remaining nulls",
            ["Keep as-is", "Drop rows with any null", "Fill numeric with mean",
             "Fill numeric with median", "Fill with 0"],
            key="demo_null_strategy",
        )

    # Apply cleaning
    df_clean = df.copy()
    cleaning_log = []

    if fix_names:
        old_cols = list(df_clean.columns)
        df_clean.columns = df_clean.columns.str.strip().str.lower().str.replace(" ", "_")
        if old_cols != list(df_clean.columns):
            cleaning_log.append("Standardized column names")

    if remove_dupes:
        n_before = len(df_clean)
        df_clean = df_clean.drop_duplicates()
        n_removed = n_before - len(df_clean)
        if n_removed > 0:
            cleaning_log.append(f"Removed {n_removed:,} duplicate rows")

    if drop_high_null:
        threshold = len(df_clean) * 0.5
        before_cols = len(df_clean.columns)
        df_clean = df_clean.dropna(axis=1, thresh=threshold)
        n_dropped = before_cols - len(df_clean.columns)
        if n_dropped > 0:
            cleaning_log.append(f"Dropped {n_dropped} high-null columns")

    if null_strategy != "Keep as-is":
        nulls_before = df_clean.isnull().sum().sum()
        if null_strategy == "Drop rows with any null":
            df_clean = df_clean.dropna()
        elif null_strategy == "Fill numeric with mean":
            num_cols = df_clean.select_dtypes(include="number").columns
            df_clean[num_cols] = df_clean[num_cols].fillna(df_clean[num_cols].mean())
        elif null_strategy == "Fill numeric with median":
            num_cols = df_clean.select_dtypes(include="number").columns
            df_clean[num_cols] = df_clean[num_cols].fillna(df_clean[num_cols].median())
        elif null_strategy == "Fill with 0":
            df_clean = df_clean.fillna(0)
        nulls_after = df_clean.isnull().sum().sum()
        if nulls_before != nulls_after:
            cleaning_log.append(f"Nulls: {nulls_before:,} → {nulls_after:,}")

    # Show cleaning summary
    if cleaning_log:
        for step in cleaning_log:
            st.write(f"✅ {step}")
    else:
        st.info("No cleaning steps applied.")

    # Before/After comparison
    st.subheader("Before / After")
    tab_before, tab_after = st.tabs(["Before Cleaning", "After Cleaning"])

    with tab_before:
        st.dataframe(df.head(20), use_container_width=True, height=300)
    with tab_after:
        st.dataframe(df_clean.head(20), use_container_width=True, height=300)

    change_col1, change_col2, change_col3 = st.columns(3)
    change_col1.metric("Rows", f"{len(df):,}", f"{len(df_clean) - len(df):,}")
    change_col2.metric("Columns", len(df.columns), len(df_clean.columns) - len(df.columns))
    change_col3.metric("Nulls", f"{df.isnull().sum().sum():,}",
                       f"{df_clean.isnull().sum().sum() - df.isnull().sum().sum():,}")

    st.divider()

    # Step 5: Analyze & Visualize
    st.header("📊 Step 5 — Analyze & Visualize")

    numeric_cols = df_clean.select_dtypes(include="number").columns.tolist()
    categorical_cols = df_clean.select_dtypes(include=["object", "category"]).columns.tolist()

    if numeric_cols:
        st.subheader("Numeric Distributions")

        dist_col1, dist_col2 = st.columns(2)

        with dist_col1:
            selected_num = st.selectbox("Select numeric column", numeric_cols, key="demo_dist_col")
            fig_data = df_clean[selected_num].dropna()
            if len(fig_data) > 0:
                st.bar_chart(fig_data.value_counts().sort_index().head(50))

        with dist_col2:
            if len(numeric_cols) >= 2:
                corr_cols = st.multiselect(
                    "Correlation columns",
                    numeric_cols,
                    default=numeric_cols[:min(4, len(numeric_cols))],
                    key="demo_corr_cols",
                )
                if len(corr_cols) >= 2:
                    corr = df_clean[corr_cols].corr()
                    st.dataframe(
                        corr.style.background_gradient(cmap="coolwarm", vmin=-1, vmax=1),
                        use_container_width=True,
                    )

    if categorical_cols:
        st.subheader("Categorical Breakdown")
        selected_cat = st.selectbox("Select categorical column", categorical_cols, key="demo_cat_col")
        cat_counts = df_clean[selected_cat].value_counts().head(20)
        st.bar_chart(cat_counts)

    st.divider()

    # Step 6: Download
    st.header("📥 Step 6 — Download Processed Data")

    dl_col1, dl_col2, dl_col3 = st.columns(3)

    with dl_col1:
        st.download_button(
            label="📥 Download CSV",
            data=df_clean.to_csv(index=False),
            file_name=f"processed_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
            mime="text/csv",
            use_container_width=True,
            type="primary",
        )

    with dl_col2:
        buffer = io.BytesIO()
        with pd.ExcelWriter(buffer, engine="openpyxl") as writer:
            df_clean.to_excel(writer, index=False, sheet_name="Processed Data")
        st.download_button(
            label="📥 Download Excel",
            data=buffer.getvalue(),
            file_name=f"processed_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            use_container_width=True,
        )

    with dl_col3:
        st.download_button(
            label="📥 Download JSON",
            data=df_clean.to_json(orient="records", indent=2, date_format="iso"),
            file_name=f"processed_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
            mime="application/json",
            use_container_width=True,
        )

else:
    # No file uploaded — show instructions
    st.info("👆 Upload a CSV, Excel, or JSON file to get started.")

    st.subheader("What This Dashboard Does")
    st.markdown("""
    1. **📤 Upload** — Accept CSV, Excel, or JSON files
    2. **✅ Validate** — Check file type, size, and readability
    3. **📖 Read** — Parse into a Pandas DataFrame
    4. **🔍 Quality Report** — Nulls, duplicates, data types
    5. **🧹 Clean** — User-controlled cleaning options
    6. **📊 Analyze** — Distributions, correlations, breakdowns
    7. **📥 Download** — Export as CSV, Excel, or JSON
    """)

# ---------------------------------------------------------------------------
# Footer
# ---------------------------------------------------------------------------
st.divider()
st.caption(
    "File Upload & Processing Dashboard · Module 06 · "
    "Streamlit for Data Science · "
    "[Streamlit Docs](https://docs.streamlit.io/develop/api-reference)"
)
