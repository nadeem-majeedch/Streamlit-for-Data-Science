"""
Exercise 06 — Dashboard Builder SOLUTION
==========================================
INSTRUCTOR USE ONLY — Do not share with students.

Reference implementation with all TODOs completed.
Run: streamlit run instructor/solutions/exercises_solutions/06_dashboard_builder_solution.py
"""

import streamlit as st
import pandas as pd
import numpy as np
from datetime import date

st.set_page_config(
    page_title="Exercise 06 — Dashboard Builder (SOLUTION)",
    page_icon="✅",
    layout="wide",
)

st.title("✅ Exercise 06 — Dashboard Builder (Solution)")
st.markdown("Complete reference implementation for instructor use.")
st.divider()

# ============================================================================
# Step 1: Generate Data
# ============================================================================

st.header("Step 1: Generate Synthetic Sales Data")

np.random.seed(42)
dates = pd.date_range("2026-01-01", periods=90, freq="D")
df = pd.DataFrame({
    "Date": dates,
    "Revenue": np.random.randint(25000, 65000, 90),
    "Users": np.random.randint(800, 2500, 90),
    "Orders": np.random.randint(50, 300, 90),
    "Returns": np.random.randint(0, 20, 90),
    "Region": np.random.choice(["North", "South", "East", "West"], 90),
})

st.write(f"Shape: {df.shape}")
st.dataframe(df.head(), use_container_width=True)

st.divider()

# ============================================================================
# Step 2: Sidebar Filter Form
# ============================================================================

st.header("Step 2: Sidebar Filter Form")

with st.sidebar.form("filters"):
    st.header("Dashboard Filters")
    region = st.selectbox("Region", ["All"] + df["Region"].unique().tolist())
    min_revenue = st.slider("Min Revenue", 0, 100000, 0)
    high_performing = st.checkbox("High-performing only (Orders > 100)")
    submitted = st.form_submit_button("Apply Filters")

if submitted:
    filtered = df.copy()
    if region != "All":
        filtered = filtered[filtered["Region"] == region]
    filtered = filtered[filtered["Revenue"] >= min_revenue]
    if high_performing:
        filtered = filtered[filtered["Orders"] > 100]
else:
    filtered = df.copy()

st.write(f"Showing **{len(filtered)}** of **{len(df)}** records")

st.divider()

# ============================================================================
# Step 3: KPI Row
# ============================================================================

st.header("Step 3: KPI Metrics")

c1, c2, c3, c4 = st.columns(4)

total_rev = filtered["Revenue"].sum()
total_users = filtered["Users"].sum()
total_orders = filtered["Orders"].sum()
conversion = (total_orders / total_users * 100) if total_users > 0 else 0

c1.metric("Total Revenue", f"${total_rev:,.0f}", icon="💰")
c2.metric("Total Users", f"{total_users:,}", icon="👥")
c3.metric("Total Orders", f"{total_orders:,}", icon="📦")
c4.metric("Avg Conversion", f"{conversion:.1f}%", icon="🎯")

st.divider()

# ============================================================================
# Step 4: Tabbed Charts
# ============================================================================

st.header("Step 4: Tabbed Chart Views")

tab1, tab2, tab3 = st.tabs(["📈 Trends", "📊 Breakdown", "📋 Details"])

with tab1:
    daily = filtered.groupby("Date")["Revenue"].sum().reset_index()
    st.line_chart(daily.set_index("Date")["Revenue"])

with tab2:
    chart, table = st.columns([0.7, 0.3])
    with chart:
        st.subheader("Revenue by Region")
        rev_by_region = filtered.groupby("Region")["Revenue"].sum()
        st.bar_chart(rev_by_region)
    with table:
        st.subheader("Orders by Region")
        orders_by_region = filtered.groupby("Region")["Orders"].sum()
        st.bar_chart(orders_by_region)

with tab3:
    st.dataframe(filtered, use_container_width=True, hide_index=True)
    csv = filtered.to_csv(index=False)
    st.download_button("Download CSV", csv, "dashboard_data.csv")

st.divider()

# ============================================================================
# Step 5: Details & Export
# ============================================================================

st.header("Step 5: Details & Export")

with st.expander("📊 Full Data"):
    st.dataframe(filtered, use_container_width=True)

with st.expander("📈 Summary Statistics"):
    st.write(filtered.describe())

with st.expander("📥 Export"):
    csv = filtered.to_csv(index=False)
    st.download_button("Download Full Data (CSV)", csv, "sales_full.csv")

st.divider()

# ============================================================================
# Step 6: Footer
# ============================================================================

st.divider()
st.caption("Dashboard built by Instructor · Module 03")
st.caption(f"Data source: Synthetic · Last updated: {date.today()}")

st.divider()
st.caption("Solution: Exercise 06 — Dashboard Builder · Module 03")
