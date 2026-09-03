"""
✏️ Exercise 05 — Layout Basics
================================
Module 03 · Beginner

Practice building structured layouts with sidebar, columns, tabs, expanders.

Run this file:
    streamlit run exercises/05_layout_basics.py

Instructions:
    Complete the TODO sections below. Each step builds on the previous one.

Related Materials:
- 📖 Reading: ../readings/05_layouts_and_containers.md
- 📓 Notebook: ../notebooks/05_layouts_and_containers.ipynb
- 🖥️ Demo App: ../apps/05_layouts_demo.py
"""

import streamlit as st
import pandas as pd
import numpy as np

# ---------------------------------------------------------------------------
# Page Config
# ---------------------------------------------------------------------------
st.set_page_config(
    page_title="Exercise 05 — Layout Basics",
    page_icon="✏️",
    layout="wide",
)

st.title("✏️ Exercise 05 — Layout Basics")
st.markdown(
    "Practice building structured layouts with sidebar, columns, tabs, and expanders."
)

st.divider()

# ---------------------------------------------------------------------------
# Step 1: Sidebar Controls
# ---------------------------------------------------------------------------
st.header("Step 1: Sidebar as Control Panel")

# TODO 1: Add the following sidebar widgets:
#   a) st.sidebar.header("Data Controls")
#   b) st.sidebar.selectbox("Dataset", ["Sales", "Inventory", "Customers"])
#   c) st.sidebar.slider("Time Range (days)", 7, 90, 30)
#   d) st.sidebar.checkbox("Show details")
#   e) st.sidebar.radio("Sort by", ["Name", "Value", "Date"], horizontal=True)
#
# Then display the selected values in the main area.

# --- START YOUR CODE HERE ---
# st.sidebar.header("Data Controls")
# dataset = st.sidebar.selectbox(...)
# days = st.sidebar.slider(...)
# show_details = st.sidebar.checkbox(...)
# sort_by = st.sidebar.radio(...)
#
# st.write(f"Dataset: **{dataset}**")
# st.write(f"Time range: **{days} days**")
# st.write(f"Show details: **{show_details}**")
# st.write(f"Sort by: **{sort_by}**")
# --- END YOUR CODE HERE ---

st.divider()

# ---------------------------------------------------------------------------
# Step 2: Column Layout
# ---------------------------------------------------------------------------
st.header("Step 2: KPI Cards with Columns")

# TODO 2: Create 4 metric cards in a single row:
#   a) Create st.columns(4) — assign to c1, c2, c3, c4
#   b) Use st.metric() in each column with:
#      - Revenue: "$45,231", delta="+5.2%"
#      - Users: "1,204", delta="+12.1%"
#      - Orders: "347", delta="-3.2%"
#      - Conversion: "3.2%", delta="+0.4%"
#   c) Add an icon parameter to each metric

# --- START YOUR CODE HERE ---
# c1, c2, c3, c4 = st.columns(4)
# c1.metric(...)
# c2.metric(...)
# c3.metric(...)
# c4.metric(...)
# --- END YOUR CODE HERE ---

st.divider()

# ---------------------------------------------------------------------------
# Step 3: Unequal Columns
# ---------------------------------------------------------------------------
st.header("Step 3: Content Split (70/30)")

# TODO 3: Create a 70/30 column layout:
#   a) main, side = st.columns([0.7, 0.3])
#   b) In main: create a line chart with random data (20 points, 3 series)
#   c) In side: show summary text with the shape of the data
#   d) Add border=True to the columns

# --- START YOUR CODE HERE ---
# main, side = st.columns(...)
# with main:
#     np.random.seed(42)
#     chart_data = pd.DataFrame(...)
#     st.line_chart(chart_data)
# with side:
#     st.write(f"Shape: {chart_data.shape}")
#     st.write(f"Series: {list(chart_data.columns)}")
# --- END YOUR CODE HERE ---

st.divider()

# ---------------------------------------------------------------------------
# Step 4: Tabs
# ---------------------------------------------------------------------------
st.header("Step 4: Tabbed Content")

# TODO 4: Create 3 tabs for different chart views:
#   a) Create st.tabs(["Bar", "Line", "Area"])
#   b) Generate a DataFrame with 3 columns of random data
#   c) In each tab, show the same data with the appropriate chart type
#   d) In the third tab, also show the raw data with st.dataframe()

# --- START YOUR CODE HERE ---
# tab1, tab2, tab3 = st.tabs([...])
# np.random.seed(42)
# data = pd.DataFrame(...)
# with tab1:
#     st.bar_chart(data)
# with tab2:
#     st.line_chart(data)
# with tab3:
#     st.area_chart(data)
#     st.dataframe(data)
# --- END YOUR CODE HERE ---

st.divider()

# ---------------------------------------------------------------------------
# Step 5: Expander
# ---------------------------------------------------------------------------
st.header("Step 5: Progressive Disclosure")

# TODO 5: Add expanders for progressive disclosure:
#   a) First, show a st.metric with "Total Records: 1,234"
#   b) Add an expander "📊 Data Distribution" with a bar_chart
#   c) Add an expander "📥 Export Options" with a st.download_button
#   d) Add an expander "📋 Raw Data" (start expanded) with st.dataframe

# --- START YOUR CODE HERE ---
# st.metric("Total Records", "1,234")
#
# with st.expander("📊 Data Distribution"):
#     ...
#
# with st.expander("📥 Export Options"):
#     ...
#
# with st.expander("📋 Raw Data", expanded=True):
#     ...
# --- END YOUR CODE HERE ---

# ---------------------------------------------------------------------------
# Footer
# ---------------------------------------------------------------------------
st.divider()
st.caption("Exercise 05 — Layout Basics · Module 03 · Streamlit for Data Science")
