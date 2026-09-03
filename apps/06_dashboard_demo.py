"""
🖥️ Demo App 06 — Sales Analytics Dashboard
=============================================
A complete Data Science dashboard demonstrating best practices
in layout, status, metrics, and UI/UX design.

Run this app:
    streamlit run apps/06_dashboard_demo.py

Related Materials:
- 📖 Reading: ../readings/06_dashboard_design_ui_ux.md
- 📓 Notebook: ../notebooks/06_data_science_dashboards.ipynb
- ✏️ Exercise: ../exercises/06_dashboard_builder.py
"""

import streamlit as st
import pandas as pd
import numpy as np
import time

# ---------------------------------------------------------------------------
# Page Config
# ---------------------------------------------------------------------------
st.set_page_config(
    page_title="06 — Sales Dashboard",
    page_icon="📊",
    layout="wide",
)

# ---------------------------------------------------------------------------
# Generate Data (cached)
# ---------------------------------------------------------------------------
@st.cache_data
def generate_sales_data(n_days=90):
    """Generate synthetic sales data for demonstration."""
    np.random.seed(42)
    dates = pd.date_range("2026-01-01", periods=n_days, freq="D")
    regions = np.random.choice(["North", "South", "East", "West"], n_days)
    products = np.random.choice(["Laptop", "Phone", "Tablet", "Monitor"], n_days)

    df = pd.DataFrame({
        "Date": dates,
        "Revenue": np.random.randint(25000, 65000, n_days),
        "Users": np.random.randint(800, 2500, n_days),
        "Orders": np.random.randint(50, 300, n_days),
        "Returns": np.random.randint(0, 20, n_days),
        "Region": regions,
        "Product": products,
    })
    df["AvgOrder"] = (df["Revenue"] / df["Orders"]).round(2)
    df["Conversion"] = (df["Orders"] / df["Users"] * 100).round(1)
    return df


# ---------------------------------------------------------------------------
# Loading State
# ---------------------------------------------------------------------------
with st.spinner("Loading dashboard data..."):
    df = generate_sales_data()
    time.sleep(0.5)  # Simulate load time

# ---------------------------------------------------------------------------
# Sidebar Controls
# ---------------------------------------------------------------------------
with st.sidebar:
    st.header("🔍 Filters")

    with st.form("filter_form"):
        date_range = st.date_input(
            "Date range",
            value=(df["Date"].min(), df["Date"].max()),
        )
        regions = st.multiselect(
            "Regions",
            options=df["Region"].unique().tolist(),
            default=df["Region"].unique().tolist(),
        )
        products = st.multiselect(
            "Products",
            options=df["Product"].unique().tolist(),
            default=df["Product"].unique().tolist(),
        )
        min_revenue = st.number_input("Min Revenue", value=0, step=5000)
        apply_filters = st.form_submit_button("Apply Filters", type="primary")

    st.divider()
    st.header("⚙️ Display")
    chart_type = st.radio("Chart type", ["Line", "Bar", "Area"], horizontal=True)
    show_returns = st.checkbox("Show returns analysis")

    st.divider()
    st.header("📥 Export")
    csv = df.to_csv(index=False)
    st.download_button("Download Full Data", csv, "sales_full.csv", use_container_width=True)

# ---------------------------------------------------------------------------
# Apply Filters
# ---------------------------------------------------------------------------
filtered = df.copy()

if isinstance(date_range, tuple) and len(date_range) == 2:
    filtered = filtered[
        (filtered["Date"] >= pd.Timestamp(date_range[0]))
        & (filtered["Date"] <= pd.Timestamp(date_range[1]))
    ]

if regions:
    filtered = filtered[filtered["Region"].isin(regions)]
if products:
    filtered = filtered[filtered["Product"].isin(products)]

if min_revenue > 0:
    filtered = filtered[filtered["Revenue"] >= min_revenue]

# ---------------------------------------------------------------------------
# Dashboard Title
# ---------------------------------------------------------------------------
st.title("📊 Sales Analytics Dashboard")
st.caption(
    f"Showing **{len(filtered)}** of **{len(df)}** records · "
    f"Last updated: just now"
)

st.divider()

# ---------------------------------------------------------------------------
# KPI Row — 4 metric cards
# ---------------------------------------------------------------------------
total_rev = filtered["Revenue"].sum()
total_users = filtered["Users"].sum()
total_orders = filtered["Orders"].sum()
avg_conversion = filtered["Conversion"].mean() if len(filtered) > 0 else 0

c1, c2, c3, c4 = st.columns(4)
c1.metric("Total Revenue", f"${total_rev:,.0f}", "+8.3%", icon="💰")
c2.metric("Total Users", f"{total_users:,}", "+5.1%", icon="👥")
c3.metric("Total Orders", f"{total_orders:,}", "+3.7%", icon="📦")
c4.metric("Avg Conversion", f"{avg_conversion:.1f}%", "+0.4%", icon="🎯")

st.divider()

# ---------------------------------------------------------------------------
# Main Content — Tabs
# ---------------------------------------------------------------------------
tab_trend, tab_breakdown, tab_region, tab_details = st.tabs(
    ["📈 Trends", "📊 Breakdown", "🌍 Regional", "📋 Details"]
)

with tab_trend:
    chart_col, summary_col = st.columns([2, 1])

    with chart_col:
        st.subheader(f"Daily {chart_type} Chart")
        chart_data = filtered.set_index("Date")[["Revenue", "Users", "Orders"]]

        if chart_type == "Line":
            st.line_chart(chart_data)
        elif chart_type == "Bar":
            st.bar_chart(chart_data)
        else:
            st.area_chart(chart_data)

    with summary_col:
        st.subheader("Summary")
        if len(filtered) > 0:
            peak_day = filtered.loc[filtered["Revenue"].idxmax(), "Date"]
            avg_daily_rev = filtered["Revenue"].mean()
            avg_daily_users = filtered["Users"].mean()

            st.metric("Avg Daily Revenue", f"${avg_daily_rev:,.0f}")
            st.metric("Avg Daily Users", f"{avg_daily_users:,.0f}")
            st.metric("Peak Revenue Day", peak_day.strftime("%b %d"))
            st.metric("Data Points", str(len(filtered)))
        else:
            st.warning("No data matches current filters.")

with tab_breakdown:
    st.subheader("Revenue by Product")

    if len(filtered) > 0:
        product_rev = filtered.groupby("Product")["Revenue"].sum().sort_values(ascending=False)
        st.bar_chart(product_rev)

        if show_returns:
            st.subheader("Returns by Product")
            product_returns = filtered.groupby("Product")["Returns"].sum().sort_values(ascending=False)
            st.bar_chart(product_returns)
    else:
        st.info("No data to display.")

with tab_region:
    st.subheader("Regional Performance")

    if len(filtered) > 0:
        region_data = filtered.groupby("Region").agg({
            "Revenue": "sum",
            "Users": "sum",
            "Orders": "sum",
            "Returns": "sum"
        }).sort_values("Revenue", ascending=False)

        # KPI row for regions
        rc1, rc2, rc3 = st.columns(3)
        with rc1:
            top_region = region_data.index[0]
            st.metric("Top Region", top_region,
                      f"${region_data.loc[top_region, 'Revenue']:,.0f}")
        with rc2:
            total_returns = region_data["Returns"].sum()
            st.metric("Total Returns", f"{total_returns:,}",
                      delta_color="inverse")
        with rc3:
            avg_return_rate = (total_returns / total_orders * 100) if total_orders > 0 else 0
            st.metric("Return Rate", f"{avg_return_rate:.1f}%",
                      delta_color="inverse")

        st.dataframe(region_data, use_container_width=True)
    else:
        st.info("No regional data to display.")

with tab_details:
    st.subheader("Raw Data")

    if len(filtered) > 0:
        st.dataframe(filtered, use_container_width=True, hide_index=True)

        with st.expander("📈 Summary Statistics"):
            st.write(filtered[["Revenue", "Users", "Orders", "Returns",
                               "AvgOrder", "Conversion"]].describe())

        with st.expander("📥 Export Filtered Data"):
            filtered_csv = filtered.to_csv(index=False)
            st.download_button(
                "Download Filtered CSV",
                filtered_csv,
                "sales_filtered.csv",
                type="primary",
            )
    else:
        st.warning("No data to display with current filters.")

# ---------------------------------------------------------------------------
# Footer
# ---------------------------------------------------------------------------
st.divider()
st.caption(
    "Sales Analytics Dashboard • Module 03 • "
    "A Data Science application — not a notebook in a browser. • "
    "[Streamlit Docs](https://docs.streamlit.io/develop/api-reference)"
)
