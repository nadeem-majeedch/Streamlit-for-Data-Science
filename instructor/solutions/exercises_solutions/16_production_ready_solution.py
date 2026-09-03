"""
Exercise 16 — Production Ready SOLUTION
=========================================
INSTRUCTOR USE ONLY — Do not share with students.

Reference implementation with all TODOs completed.
Run: streamlit run instructor/solutions/exercises_solutions/16_production_ready_solution.py
"""

import streamlit as st
import logging
import sys
import os
import pandas as pd
import numpy as np
from datetime import datetime

# ============================================================================
# Logging Setup
# ============================================================================

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)
logger = logging.getLogger(__name__)

# ============================================================================
# Page Config
# ============================================================================

st.set_page_config(
    page_title="Exercise 16 — Production Ready (SOLUTION)",
    page_icon="✅",
    layout="wide",
)

logger.info("App started")
st.title("✅ Exercise 16 — Production Ready (Solution)")
st.markdown("Complete reference implementation for instructor use.")
st.divider()

# ============================================================================
# PART 1 — Theory (answers embedded)
# ============================================================================

st.header("Part 1 — Production vs Development")
st.info(
    "Q1: **B** (Missing files) · "
    "Q2: **B** (Check logs) · "
    "Q3: **B** (UUID should not be cached)"
)
st.divider()

# ============================================================================
# PART 2 — Error Handling
# ============================================================================

st.header("Part 2 — Graceful Error Handling")


def safe_divide(a, b):
    """Safely divide a by b, handling errors gracefully."""
    try:
        result = float(a) / float(b)
        return result
    except ZeroDivisionError:
        st.warning("Cannot divide by zero.")
        return None
    except (TypeError, ValueError) as e:
        st.error(f"Invalid input: {e}")
        return None


def safe_load_data():
    """Load sample data with error handling."""
    try:
        np.random.seed(42)
        df = pd.DataFrame({
            "category": np.random.choice(["A", "B", "C"], 50),
            "value": np.random.randn(50) * 10 + 50,
            "quantity": np.random.randint(1, 20, 50),
        })
        logger.info(f"Data loaded: {len(df)} rows")
        return df
    except Exception as e:
        st.error(f"Failed to load data: {e}")
        logger.error(f"Data load failed: {e}", exc_info=True)
        return pd.DataFrame()


col1, col2 = st.columns(2)

with col1:
    st.subheader("Safe Divide")
    result = safe_divide(10, 2)
    if result is not None:
        st.success(f"10 / 2 = {result}")

    result = safe_divide(10, 0)
    if result is None:
        st.info("Division by zero handled gracefully")

    result = safe_divide("abc", 5)
    if result is None:
        st.info("Invalid input handled gracefully")

with col2:
    st.subheader("Safe Data Load")
    df = safe_load_data()
    if not df.empty:
        st.dataframe(df.head())
    else:
        st.info("Empty DataFrame returned (failure handled)")

st.divider()

# ============================================================================
# PART 3 — Structured Logging
# ============================================================================

st.header("Part 3 — Application Logging")


def run_monitored_app():
    """Run an app with structured logging."""
    logger.info("Application function called")

    data = safe_load_data()
    if not data.empty:
        logger.info(f"Processing {len(data)} rows")
        total = data["value"].sum()
        logger.info(f"Computed total value: {total:.2f}")
        return data
    else:
        logger.warning("No data to process")
        return data


result_df = run_monitored_app()

if not result_df.empty:
    st.success(f"Processed {len(result_df)} rows successfully")
    st.write(f"Total value: {result_df['value'].sum():.2f}")

st.divider()

# ============================================================================
# PART 4 — Health Check
# ============================================================================

st.header("Part 4 — Health Check Dashboard")

import streamlit.components.v1 as components

col1, col2 = st.columns(2)

with col1:
    st.subheader("System Information")
    st.write(f"**App Version:** 1.0.0")
    st.write(f"**Timestamp:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    st.write(f"**Python:** {sys.version.split()[0]}")
    st.write(f"**Streamlit:** {st.__version__}")
    st.write(f"**Platform:** {sys.platform}")

with col2:
    st.subheader("Dependency Status")

    @st.cache_resource
    def check_dependencies():
        """Check status of key dependencies."""
        deps = {}
        for name in ["streamlit", "pandas", "numpy"]:
            try:
                mod = __import__(name)
                deps[name] = "✅ Available"
            except ImportError:
                deps[name] = "❌ Missing"
        return deps

    deps = check_dependencies()
    for name, status in deps.items():
        st.write(f"**{name}:** {status}")

    # Memory usage estimate
    try:
        import psutil
        mem = psutil.virtual_memory()
        st.write(f"**Memory:** {mem.percent}% used ({mem.used / 1e9:.1f} GB)")
    except ImportError:
        st.write("**Memory:** psutil not installed (optional)")

st.divider()

# ============================================================================
# PART 5 — Design Decision
# ============================================================================

st.header("Part 5 — Architecture Decision")
st.markdown("""
**Answer:** **E** — Both B and C are acceptable depending on predictability.

- **`st.spinner()`** — Best when duration is unpredictable (simple, always works)
- **`st.progress()`** — Best when you can estimate completion time (better UX)
- **`st.toast()`** — Best for background tasks that don't block the UI

In production, consider `st.fragment` with `run_every` for periodic updates.
""")

st.divider()

# ============================================================================
# PART 6 — Debug
# ============================================================================

st.header("Part 6 — Debug This Production App")
st.markdown("""
**Issues found:**
1. `data/sales_2024.csv` may not exist on Community Cloud
2. `requirements.txt` may be missing
3. `.streamlit/config.toml` with `headless = true` may be missing

**Fixed version shown above** — uses generated sample data instead of file dependency.
""")

st.divider()
st.caption("Solution: Exercise 16 — Production Ready · Module 16")
