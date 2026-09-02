"""
✏️ Exercise 04 — Dataset Filter App
====================================
Module 02 · Beginner

Build an interactive dataset filtering app using Streamlit widgets.

Run this file:
    streamlit run exercises/04_dataset_filter_app.py

Instructions:
    Complete the TODO sections below. You will build a fully functional
    dataset explorer with sidebar filters and interactive display.

Related Materials:
- 📖 Reading: ../readings/03_streamlit_widgets_and_input.md
- 📓 Notebook: ../notebooks/04_interactive_ds_controls.ipynb
- 🖥️ Demo App: ../apps/03_widgets_demo.py
"""

import streamlit as st
import pandas as pd
import numpy as np

# ---------------------------------------------------------------------------
# Page Config
# ---------------------------------------------------------------------------
st.set_page_config(
    page_title="Exercise 04 — Dataset Filter",
    page_icon="✏️",
    layout="wide",
)

st.title("✏️ Exercise 04 — Dataset Filter App")
st.markdown(
    "Build an interactive dataset explorer with sidebar controls."
)

st.divider()

# ---------------------------------------------------------------------------
# Step 1: Generate Data
# ---------------------------------------------------------------------------
st.header("Step 1: Generate Dataset")

# TODO 1: Create a synthetic dataset with 500 rows containing:
#   - product: random choice of ["Laptop", "Phone", "Tablet", "Monitor"]
#   - region: random choice of ["North", "South", "East", "West"]
#   - sales: random integers between 100 and 10000
#   - units: random integers between 1 and 50
#   - rating: random floats between 1.0 and 5.0 (rounded to 1 decimal)
#
# Use np.random.seed(42) for reproducibility.
# Display the first 10 rows with st.dataframe().

# --- START YOUR CODE HERE ---
# df = pd.DataFrame({...})
# st.dataframe(df.head(10))
# --- END YOUR CODE HERE ---

st.divider()

# ---------------------------------------------------------------------------
# Step 2: Sidebar Filters
# ---------------------------------------------------------------------------
st.header("Step 2: Add Sidebar Filters")

# TODO 2: Add the following filters in the sidebar:
#   a) st.sidebar.multiselect for "product" (default: all selected)
#   b) st.sidebar.multiselect for "region" (default: all selected)
#   c) st.sidebar.slider for "sales range" (min to max of the data)
#   d) st.sidebar.checkbox for "High-rated only (≥ 4.0)"
#   e) st.sidebar.number_input for "Minimum units" (range 1-50, default 1)

# --- START YOUR CODE HERE ---
# products = st.sidebar.multiselect(...)
# regions = st.sidebar.multiselect(...)
# min_sales, max_sales = st.sidebar.slider(...)
# high_rated = st.sidebar.checkbox(...)
# min_units = st.sidebar.number_input(...)
# --- END YOUR CODE HERE ---

st.divider()

# ---------------------------------------------------------------------------
# Step 3: Apply Filters
# ---------------------------------------------------------------------------
st.header("Step 3: Apply Filters")

# TODO 3: Filter the DataFrame based on all sidebar selections.
# Display the number of filtered rows vs. total rows.

# --- START YOUR CODE HERE ---
# filtered = df[
#     (df["product"].isin(products)) &
#     (df["region"].isin(regions)) &
#     (df["sales"] >= min_sales) &
#     (df["sales"] <= max_sales) &
#     (df["units"] >= min_units)
# ]
# if high_rated:
#     filtered = filtered[filtered["rating"] >= 4.0]
# --- END YOUR CODE HERE ---

st.divider()

# ---------------------------------------------------------------------------
# Step 4: Display Results
# ---------------------------------------------------------------------------
st.header("Step 4: Display Results")

# TODO 4: Show 4 metric cards:
#   - Total Records (filtered count)
#   - Total Sales (sum of filtered sales, formatted with commas)
#   - Average Rating (mean of filtered rating)
#   - Average Units (mean of filtered units)
#
# Then display the filtered DataFrame sorted by sales descending.

# --- START YOUR CODE HERE ---
# col1, col2, col3, col4 = st.columns(4)
# col1.metric(...)
# col2.metric(...)
# col3.metric(...)
# col4.metric(...)
# st.dataframe(...)
# --- END YOUR CODE HERE ---

st.divider()

# ---------------------------------------------------------------------------
# Step 5: Download Button (Bonus)
# ---------------------------------------------------------------------------
st.header("Step 5: Download (Bonus)")

# TODO 5: Add a download button that exports the filtered data as CSV.
# Hint: Use st.download_button() with filtered.to_csv(index=False).

# --- START YOUR CODE HERE ---
# csv = filtered.to_csv(index=False)
# st.download_button(...)
# --- END YOUR CODE HERE ---

# ---------------------------------------------------------------------------
# Footer
# ---------------------------------------------------------------------------
st.divider()
st.caption("Exercise 04 — Dataset Filter App • Module 02 • Streamlit for Data Science")
