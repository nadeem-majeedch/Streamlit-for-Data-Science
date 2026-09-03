"""
✏️ Exercise 06 — Dashboard Builder
====================================
Module 03 · Beginner

Build a complete Data Science dashboard from scratch.

Run this file:
    streamlit run exercises/06_dashboard_builder.py

Instructions:
    Complete the TODO sections below to build a fully functional
    Sales Analytics Dashboard using layout elements from Module 03.

Related Materials:
- 📖 Reading: ../readings/05_layouts_and_containers.md
- 📖 Reading: ../readings/06_dashboard_design_ui_ux.md
- 📓 Notebook: ../notebooks/06_data_science_dashboards.ipynb
- 🖥️ Demo App: ../apps/06_dashboard_demo.py
"""

import streamlit as st
import pandas as pd
import numpy as np

# ---------------------------------------------------------------------------
# Page Config
# ---------------------------------------------------------------------------
st.set_page_config(
    page_title="Exercise 06 — Dashboard Builder",
    page_icon="✏️",
    layout="wide",
)

st.title("✏️ Exercise 06 — Dashboard Builder")
st.markdown(
    "Build a complete Sales Analytics Dashboard using everything from Module 03."
)

st.divider()

# ---------------------------------------------------------------------------
# Step 1: Generate Data
# ---------------------------------------------------------------------------
st.header("Step 1: Generate Synthetic Sales Data")

# TODO 1: Create a DataFrame with 90 rows containing:
#   - Date: pd.date_range("2026-01-01", periods=90, freq="D")
#   - Revenue: random integers between 25000 and 65000
#   - Users: random integers between 800 and 2500
#   - Orders: random integers between 50 and 300
#   - Returns: random integers between 0 and 20
#   - Region: random choice of ["North", "South", "East", "West"]
#
# Use np.random.seed(42) for reproducibility.
# Display the shape and first 5 rows.

# --- START YOUR CODE HERE ---
# np.random.seed(42)
# dates = pd.date_range(...)
# df = pd.DataFrame({...})
# st.write(f"Shape: {df.shape}")
# st.dataframe(df.head())
# --- END YOUR CODE HERE ---

st.divider()

# ---------------------------------------------------------------------------
# Step 2: Sidebar with Form
# ---------------------------------------------------------------------------
st.header("Step 2: Sidebar Filter Form")

# TODO 2: Create a sidebar form with filters:
#   a) st.sidebar.header("Dashboard Filters")
#   b) Inside a st.sidebar.form("filters"):
#      - st.sidebar.selectbox for Region (default "All")
#      - st.sidebar.slider for "Min Revenue" (0 to 100000, default 0)
#      - st.sidebar.checkbox for "High-performing only (Orders > 100)"
#   c) Add a st.form_submit_button("Apply")
#   d) After the form, filter the DataFrame based on selections
#   e) Display filtered row count

# --- START YOUR CODE HERE ---
# with st.sidebar.form("filters"):
#     ...
#     submitted = st.form_submit_button("Apply")
#
# if submitted:
#     filtered = df[...]
#     st.write(f"Showing {len(filtered)} of {len(df)} records")
# --- END YOUR CODE HERE ---

st.divider()

# ---------------------------------------------------------------------------
# Step 3: KPI Row
# ---------------------------------------------------------------------------
st.header("Step 3: KPI Metrics")

# TODO 3: Display 4 metric cards:
#   a) Create st.columns(4)
#   b) Total Revenue (sum, formatted with $ and commas, icon="💰")
#   c) Total Users (sum, formatted with commas, icon="👥")
#   d) Total Orders (sum, formatted with commas, icon="📦")
#   e) Avg Conversion (Users→Orders %, formatted as percentage, icon="🎯")

# --- START YOUR CODE HERE ---
# c1, c2, c3, c4 = st.columns(4)
# total_rev = filtered["Revenue"].sum()
# c1.metric("Total Revenue", f"${total_rev:,.0f}", icon="💰")
# c2.metric(...)
# c3.metric(...)
# c4.metric(...)
# --- END YOUR CODE HERE ---

st.divider()

# ---------------------------------------------------------------------------
# Step 4: Tabbed Charts
# ---------------------------------------------------------------------------
st.header("Step 4: Tabbed Chart Views")

# TODO 4: Create 3 tabs:
#   a) "📈 Trends" — line chart of Revenue over Date
#   b) "📊 Breakdown" — 2-column layout:
#      Left (70%): bar chart of Revenue by Region
#      Right (30%): bar chart of Orders by Region
#   c) "📋 Details" — full dataframe with export button

# --- START YOUR CODE HERE ---
# tab1, tab2, tab3 = st.tabs(["📈 Trends", "📊 Breakdown", "📋 Details"])
#
# with tab1:
#     st.line_chart(filtered.set_index("Date")["Revenue"])
#
# with tab2:
#     chart, table = st.columns([0.7, 0.3])
#     with chart:
#         st.bar_chart(filtered.groupby("Region")["Revenue"].sum())
#     with table:
#         st.bar_chart(filtered.groupby("Region")["Orders"].sum())
#
# with tab3:
#     st.dataframe(filtered, use_container_width=True, hide_index=True)
#     csv = filtered.to_csv(index=False)
#     st.download_button("Download CSV", csv, "sales.csv")
# --- END YOUR CODE HERE ---

st.divider()

# ---------------------------------------------------------------------------
# Step 5: Progressive Disclosure
# ---------------------------------------------------------------------------
st.header("Step 5: Details & Export")

# TODO 5: Add expanders:
#   a) "📊 Full Data" — show the complete filtered DataFrame
#   b) "📈 Summary Statistics" — show filtered.describe()
#   c) "📥 Export" — download button for CSV

# --- START YOUR CODE HERE ---
# with st.expander("📊 Full Data"):
#     st.dataframe(filtered, use_container_width=True)
#
# with st.expander("📈 Summary Statistics"):
#     st.write(filtered.describe())
#
# with st.expander("📥 Export"):
#     csv = filtered.to_csv(index=False)
#     st.download_button(...)
# --- END YOUR CODE HERE ---

st.divider()

# ---------------------------------------------------------------------------
# Step 6: Footer (Bonus)
# ---------------------------------------------------------------------------
st.header("Step 6: Dashboard Footer (Bonus)")

# TODO 6: Add a footer with:
#   a) st.divider()
#   b) st.caption with "Dashboard built by [Your Name] · Module 03"
#   c) st.caption with "Data source: Synthetic · Last updated: {today's date}"

# --- START YOUR CODE HERE ---
# st.divider()
# st.caption("Dashboard built by [Your Name] · Module 03")
# from datetime import date
# st.caption(f"Data source: Synthetic · Last updated: {date.today()}")
# --- END YOUR CODE HERE ---

# ---------------------------------------------------------------------------
# Footer
# ---------------------------------------------------------------------------
st.divider()
st.caption("Exercise 06 — Dashboard Builder · Module 03 · Streamlit for Data Science")
