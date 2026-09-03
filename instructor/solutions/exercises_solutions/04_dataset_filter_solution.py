"""
Exercise 04 — Dataset Filter App SOLUTION
============================================
INSTRUCTOR USE ONLY — Do not share with students.

Reference implementation with all TODOs completed.
Run: streamlit run instructor/solutions/exercises_solutions/04_dataset_filter_solution.py
"""

import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Exercise 04 — Dataset Filter (SOLUTION)",
    page_icon="✅",
    layout="wide",
)

st.title("✅ Exercise 04 — Dataset Filter App (Solution)")
st.markdown("Complete reference implementation for instructor use.")
st.divider()

# ============================================================================
# Step 1: Generate Data
# ============================================================================

st.header("Step 1: Generate Dataset")

np.random.seed(42)
n = 500

df = pd.DataFrame({
    "product": np.random.choice(["Laptop", "Phone", "Tablet", "Monitor"], n),
    "region": np.random.choice(["North", "South", "East", "West"], n),
    "sales": np.random.randint(100, 10000, n),
    "units": np.random.randint(1, 50, n),
    "rating": np.random.uniform(1.0, 5.0, n).round(1),
})

st.dataframe(df.head(10), use_container_width=True)
st.write(f"Total rows: {len(df)}")

st.divider()

# ============================================================================
# Step 2: Sidebar Filters
# ============================================================================

st.header("Step 2: Add Sidebar Filters")

products = st.sidebar.multiselect(
    "Product",
    df["product"].unique().tolist(),
    default=df["product"].unique().tolist(),
)

regions = st.sidebar.multiselect(
    "Region",
    df["region"].unique().tolist(),
    default=df["region"].unique().tolist(),
)

min_sales, max_sales = st.sidebar.slider(
    "Sales Range",
    int(df["sales"].min()),
    int(df["sales"].max()),
    (int(df["sales"].min()), int(df["sales"].max())),
)

high_rated = st.sidebar.checkbox("High-rated only (≥ 4.0)")

min_units = st.sidebar.number_input(
    "Minimum Units", min_value=1, max_value=50, value=1
)

st.divider()

# ============================================================================
# Step 3: Apply Filters
# ============================================================================

st.header("Step 3: Apply Filters")

filtered = df[
    (df["product"].isin(products))
    & (df["region"].isin(regions))
    & (df["sales"] >= min_sales)
    & (df["sales"] <= max_sales)
    & (df["units"] >= min_units)
]

if high_rated:
    filtered = filtered[filtered["rating"] >= 4.0]

st.write(f"Showing **{len(filtered)}** of **{len(df)}** records")

st.divider()

# ============================================================================
# Step 4: Display Results
# ============================================================================

st.header("Step 4: Display Results")

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Records", f"{len(filtered):,}")
col2.metric("Total Sales", f"${filtered['sales'].sum():,}")
col3.metric("Avg Rating", f"{filtered['rating'].mean():.1f}")
col4.metric("Avg Units", f"{filtered['units'].mean():.1f}")

st.dataframe(
    filtered.sort_values("sales", ascending=False),
    use_container_width=True,
    hide_index=True,
)

st.divider()

# ============================================================================
# Step 5: Download Button
# ============================================================================

st.header("Step 5: Download")

csv = filtered.to_csv(index=False)
st.download_button(
    label="📥 Download Filtered Data (CSV)",
    data=csv,
    file_name="filtered_sales.csv",
    mime="text/csv",
)

st.divider()
st.caption("Solution: Exercise 04 — Dataset Filter App · Module 02")
