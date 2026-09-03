"""
Exercise 05 — Layout Basics SOLUTION
======================================
INSTRUCTOR USE ONLY — Do not share with students.

Reference implementation with all TODOs completed.
Run: streamlit run instructor/solutions/exercises_solutions/05_layout_basics_solution.py
"""

import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Exercise 05 — Layout Basics (SOLUTION)",
    page_icon="✅",
    layout="wide",
)

st.title("✅ Exercise 05 — Layout Basics (Solution)")
st.markdown("Complete reference implementation for instructor use.")
st.divider()

# ============================================================================
# Step 1: Sidebar Controls
# ============================================================================

st.header("Step 1: Sidebar as Control Panel")

st.sidebar.header("Data Controls")
dataset = st.sidebar.selectbox("Dataset", ["Sales", "Inventory", "Customers"])
days = st.sidebar.slider("Time Range (days)", 7, 90, 30)
show_details = st.sidebar.checkbox("Show details")
sort_by = st.sidebar.radio("Sort by", ["Name", "Value", "Date"], horizontal=True)

st.write(f"**Dataset:** {dataset}")
st.write(f"**Time Range:** {days} days")
st.write(f"**Show Details:** {show_details}")
st.write(f"**Sort by:** {sort_by}")

if show_details:
    st.info(f"Currently viewing {dataset} data for the last {days} days, sorted by {sort_by}.")

st.divider()

# ============================================================================
# Step 2: KPI Cards
# ============================================================================

st.header("Step 2: KPI Cards with Columns")

c1, c2, c3, c4 = st.columns(4)
c1.metric("Revenue", "$45,231", delta="+5.2%", icon="💰")
c2.metric("Users", "1,204", delta="+12.1%", icon="👥")
c3.metric("Orders", "347", delta="-3.2%", icon="📦")
c4.metric("Conversion", "3.2%", delta="+0.4%", icon="🎯")

st.divider()

# ============================================================================
# Step 3: Unequal Columns (70/30)
# ============================================================================

st.header("Step 3: Content Split (70/30)")

main, side = st.columns([0.7, 0.3], border=True)

with main:
    np.random.seed(42)
    chart_data = pd.DataFrame({
        "Series A": np.random.randn(20).cumsum(),
        "Series B": np.random.randn(20).cumsum(),
        "Series C": np.random.randn(20).cumsum(),
    })
    st.line_chart(chart_data)

with side:
    st.write(f"**Shape:** {chart_data.shape}")
    st.write(f"**Series:** {list(chart_data.columns)}")
    st.write(f"**Range A:** {chart_data['Series A'].min():.1f} to {chart_data['Series A'].max():.1f}")

st.divider()

# ============================================================================
# Step 4: Tabs
# ============================================================================

st.header("Step 4: Tabbed Content")

np.random.seed(42)
tab_data = pd.DataFrame({
    "Category A": np.random.randint(10, 100, 10),
    "Category B": np.random.randint(10, 100, 10),
    "Category C": np.random.randint(10, 100, 10),
})

tab1, tab2, tab3 = st.tabs(["Bar", "Line", "Area"])

with tab1:
    st.bar_chart(tab_data)
    st.caption("Bar chart view of categories")

with tab2:
    st.line_chart(tab_data)
    st.caption("Line chart view — better for trends")

with tab3:
    st.area_chart(tab_data)
    st.dataframe(tab_data, use_container_width=True)
    st.caption("Area chart with raw data table")

st.divider()

# ============================================================================
# Step 5: Expander
# ============================================================================

st.header("Step 5: Progressive Disclosure")

st.metric("Total Records", "1,234")

with st.expander("📊 Data Distribution"):
    dist_data = pd.DataFrame({
        "Count": np.random.randint(10, 200, 5),
    }, index=["A", "B", "C", "D", "E"])
    st.bar_chart(dist_data)

with st.expander("📥 Export Options"):
    csv = tab_data.to_csv(index=False)
    st.download_button("Download CSV", csv, "data.csv")

with st.expander("📋 Raw Data", expanded=True):
    st.dataframe(tab_data, use_container_width=True)

st.divider()
st.caption("Solution: Exercise 05 — Layout Basics · Module 03")
