"""
Deployable Data Science Dashboard
==================================
A complete Streamlit application ready for deployment on Streamlit Community Cloud.

Deployment Steps:
1. Push this folder's contents to a GitHub repository
2. Go to share.streamlit.io → "New app"
3. Select your repository, branch, and set main file to: apps/deployable_app/app.py
4. Click Deploy!

This app demonstrates:
- Clean application structure
- Session state for persistence
- Caching for performance
- Error handling for production
- No hardcoded secrets
"""

import streamlit as st
import pandas as pd
import numpy as np
import os

# ─── Page Config (must be first Streamlit call) ───
st.set_page_config(
    page_title="DS Dashboard — Deployable Example",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ─── Cached Data Loading ───
@st.cache_data
def load_sample_data() -> pd.DataFrame:
    """Generate sample sales data for demonstration."""
    np.random.seed(42)
    n = 500

    dates = pd.date_range("2024-01-01", periods=n, freq="D")
    categories = ["Electronics", "Clothing", "Food", "Books", "Sports"]
    regions = ["North", "South", "East", "West"]

    df = pd.DataFrame(
        {
            "date": np.random.choice(dates, n),
            "category": np.random.choice(categories, n),
            "region": np.random.choice(regions, n),
            "sales": np.random.uniform(10, 500, n).round(2),
            "quantity": np.random.randint(1, 20, n),
            "rating": np.random.uniform(1, 5, n).round(1),
        }
    )
    df["revenue"] = (df["sales"] * df["quantity"]).round(2)
    df["date"] = pd.to_datetime(df["date"])
    return df


def compute_kpis(df: pd.DataFrame) -> dict:
    """Compute key performance indicators from the dataset."""
    return {
        "total_revenue": df["revenue"].sum(),
        "avg_order_value": df["sales"].mean(),
        "total_orders": len(df),
        "avg_rating": df["rating"].mean(),
        "top_category": df.groupby("category")["revenue"]
        .sum()
        .idxmax(),
        "top_region": df.groupby("region")["revenue"]
        .sum()
        .idxmax(),
    }


def validate_filters(category: str, region: str, min_sales: float) -> bool:
    """Basic input validation."""
    if min_sales < 0:
        st.error("Minimum sales cannot be negative.")
        return False
    return True


# ─── Main Application ───
def main():
    st.title("📊 Deployable Data Science Dashboard")
    st.caption(
        "A complete example app ready for Streamlit Community Cloud deployment."
    )

    # Load data
    try:
        df = load_sample_data()
    except Exception as e:
        st.error(f"Failed to load data: {e}")
        st.stop()

    # ─── Sidebar Filters ───
    st.sidebar.header("🔍 Filters")

    categories = ["All"] + sorted(df["category"].unique().tolist())
    selected_category = st.sidebar.selectbox("Category", categories)

    regions = ["All"] + sorted(df["region"].unique().tolist())
    selected_region = st.sidebar.selectbox("Region", regions)

    min_sales = st.sidebar.number_input(
        "Minimum Sales ($)", min_value=0.0, value=0.0, step=10.0
    )

    date_range = st.sidebar.date_input(
        "Date Range",
        value=(df["date"].min(), df["date"].max()),
        min_value=df["date"].min(),
        max_value=df["date"].max(),
    )

    # Apply filters
    filtered = df.copy()
    if selected_category != "All":
        filtered = filtered[filtered["category"] == selected_category]
    if selected_region != "All":
        filtered = filtered[filtered["region"] == selected_region]
    filtered = filtered[filtered["sales"] >= min_sales]
    if len(date_range) == 2:
        start_date, end_date = pd.Timestamp(date_range[0]), pd.Timestamp(date_range[1])
        filtered = filtered[
            (filtered["date"] >= start_date) & (filtered["date"] <= end_date)
        ]

    if filtered.empty:
        st.warning("No data matches the selected filters. Try adjusting your criteria.")
        st.stop()

    # ─── KPI Metrics ───
    kpis = compute_kpis(filtered)

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Revenue", f"${kpis['total_revenue']:,.2f}")
    col2.metric("Avg Order Value", f"${kpis['avg_order_value']:.2f}")
    col3.metric("Total Orders", f"{kpis['total_orders']:,}")
    col4.metric("Avg Rating", f"{kpis['avg_rating']:.1f} ⭐")

    st.divider()

    # ─── Charts ───
    tab_chart, tab_table, tab_stats = st.tabs(
        ["📈 Charts", "📋 Data Table", "📊 Statistics"]
    )

    with tab_chart:
        st.subheader("Revenue Over Time")
        daily = (
            filtered.groupby("date")["revenue"]
            .sum()
            .reset_index()
            .sort_values("date")
        )
        st.line_chart(daily.set_index("date")["revenue"], use_container_width=True)

        st.subheader("Revenue by Category")
        cat_rev = (
            filtered.groupby("category")["revenue"]
            .sum()
            .sort_values(ascending=True)
        )
        st.bar_chart(cat_rev, use_container_width=True)

        st.subheader("Revenue by Region")
        region_rev = filtered.groupby("region")["revenue"].sum()
        st.bar_chart(region_rev, use_container_width=True)

    with tab_table:
        st.subheader(f"Filtered Data ({len(filtered)} rows)")
        st.dataframe(
            filtered.sort_values("revenue", ascending=False),
            use_container_width=True,
            hide_index=True,
        )

        # Download button
        csv = filtered.to_csv(index=False)
        st.download_button(
            label="📥 Download Filtered Data (CSV)",
            data=csv,
            file_name="filtered_sales_data.csv",
            mime="text/csv",
        )

    with tab_stats:
        st.subheader("Summary Statistics")
        st.dataframe(
            filtered.describe(),
            use_container_width=True,
        )

        st.subheader("Category Breakdown")
        breakdown = (
            filtered.groupby("category")
            .agg(
                orders=("sales", "count"),
                avg_sales=("sales", "mean"),
                total_revenue=("revenue", "sum"),
                avg_rating=("rating", "mean"),
            )
            .round(2)
        )
        st.dataframe(breakdown, use_container_width=True)

    # ─── Footer ───
    st.divider()
    st.caption(
        "Built with Streamlit · Data is generated for demonstration · "
        f"Showing {len(filtered)} of {len(df)} records"
    )


if __name__ == "__main__":
    main()
