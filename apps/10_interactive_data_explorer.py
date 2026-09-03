"""
🖥️ Demo App 10 — Interactive Data Explorer
=============================================
A complete Data Science dashboard demonstrating architecture,
filters, KPIs, charts, tables, and export.

Run this app:
    streamlit run apps/10_interactive_data_explorer.py

Related Materials:
- 📖 Reading: ../readings/10_interactive_dashboard.md
- 📓 Notebook: ../notebooks/10_interactive_dashboard.ipynb
- ✏️ Exercise: ../exercises/10_dashboard_workshop.py
- 🚀 Project: ../projects/P02_data_explorer.md
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import io

# ═══════════════════════════════════════════════════════════════════════════════
# SECTION 1: Page Configuration
# ═══════════════════════════════════════════════════════════════════════════════

st.set_page_config(
    page_title="Interactive Data Explorer",
    page_icon="🔍",
    layout="wide",
)

# ═══════════════════════════════════════════════════════════════════════════════
# SECTION 2: Data Functions (No Streamlit calls!)
# ═══════════════════════════════════════════════════════════════════════════════

@st.cache_data
def load_data():
    """Load and generate the e-commerce sales dataset.

    In a real app, this would read from a database or file.
    Here we generate synthetic data for demonstration.
    """
    np.random.seed(42)
    n_rows = 2000

    dates = pd.date_range("2024-01-01", periods=365, freq="D")
    products = ["Laptop", "Phone", "Tablet", "Headphones", "Monitor", "Keyboard"]
    regions = ["North America", "Europe", "Asia Pacific", "Latin America"]
    segments = ["Consumer", "Corporate", "Home Office"]
    base_prices = {
        "Laptop": 1200, "Phone": 800, "Tablet": 500,
        "Headphones": 150, "Monitor": 400, "Keyboard": 80,
    }

    data = []
    for _ in range(n_rows):
        product = np.random.choice(products)
        unit_price = base_prices[product] * np.random.uniform(0.8, 1.2)
        quantity = np.random.randint(1, 10)
        revenue = round(unit_price * quantity, 2)
        cost = round(revenue * np.random.uniform(0.4, 0.7), 2)

        data.append({
            "date": np.random.choice(dates),
            "product": product,
            "region": np.random.choice(regions),
            "segment": np.random.choice(segments),
            "unit_price": round(unit_price, 2),
            "quantity": quantity,
            "revenue": revenue,
            "cost": cost,
            "profit": round(revenue - cost, 2),
        })

    return pd.DataFrame(data)


def filter_data(df, regions, products, segments, date_range):
    """Apply filters to the DataFrame.

    Pure function — no Streamlit calls inside.
    This makes it testable and reusable.
    """
    result = df.copy()

    if regions:
        result = result[result["region"].isin(regions)]
    if products:
        result = result[result["product"].isin(products)]
    if segments:
        result = result[result["segment"].isin(segments)]
    if date_range and len(date_range) == 2:
        start = pd.Timestamp(date_range[0])
        end = pd.Timestamp(date_range[1])
        result = result[(result["date"] >= start) & (result["date"] <= end)]

    return result


def compute_kpis(df):
    """Compute Key Performance Indicators.

    Returns a dictionary of formatted metrics.
    """
    total_revenue = df["revenue"].sum()
    total_profit = df["profit"].sum()
    total_orders = len(df)
    avg_order_value = total_revenue / total_orders if total_orders > 0 else 0
    profit_margin = (total_profit / total_revenue * 100) if total_revenue > 0 else 0
    unique_products = df["product"].nunique()
    avg_quantity = df["quantity"].mean() if len(df) > 0 else 0

    return {
        "total_revenue": total_revenue,
        "total_profit": total_profit,
        "total_orders": total_orders,
        "avg_order_value": avg_order_value,
        "profit_margin": profit_margin,
        "unique_products": unique_products,
        "avg_quantity": avg_quantity,
    }


# ═══════════════════════════════════════════════════════════════════════════════
# SECTION 3: Load Data
# ═══════════════════════════════════════════════════════════════════════════════

df = load_data()

# ═══════════════════════════════════════════════════════════════════════════════
# SECTION 4: Sidebar Controls
# ═══════════════════════════════════════════════════════════════════════════════

with st.sidebar:
    st.header("🔍 Filters")

    date_range = st.date_input(
        "Date range",
        value=(df["date"].min(), df["date"].max()),
        help="Select the time period to analyze",
    )

    regions = st.multiselect(
        "Region",
        options=df["region"].unique().tolist(),
        default=df["region"].unique().tolist(),
        help="Filter by geographic region",
    )

    products = st.multiselect(
        "Product",
        options=df["product"].unique().tolist(),
        default=df["product"].unique().tolist(),
        help="Filter by product category",
    )

    segments = st.multiselect(
        "Customer Segment",
        options=df["segment"].unique().tolist(),
        default=df["segment"].unique().tolist(),
        help="Filter by customer type",
    )

    st.divider()
    st.header("⚙️ Display Options")

    chart_type = st.radio(
        "Chart type",
        ["Line", "Bar", "Area"],
        horizontal=True,
        help="Choose how to visualize the revenue trend",
    )

    show_trend = st.checkbox(
        "Show 7-day moving average",
        value=True,
        help="Overlay a smoothed trend line on the revenue chart",
    )

    st.divider()
    st.header("📥 Export")

    # Pre-compute filtered data for download buttons
    filtered_preview = filter_data(df, regions, products, segments, date_range)
    if not filtered_preview.empty:
        csv_data = filtered_preview.to_csv(index=False)
        st.download_button(
            "Download Filtered CSV",
            data=csv_data,
            file_name="filtered_sales.csv",
            mime="text/csv",
            use_container_width=True,
        )

# ═══════════════════════════════════════════════════════════════════════════════
# SECTION 5: Apply Filters
# ═══════════════════════════════════════════════════════════════════════════════

filtered = filter_data(df, regions, products, segments, date_range)

# ═══════════════════════════════════════════════════════════════════════════════
# SECTION 6: Page Title & Empty State
# ═══════════════════════════════════════════════════════════════════════════════

st.title("🔍 Interactive Data Explorer")
st.caption(
    f"Showing **{len(filtered):,}** of **{len(df):,}** records · "
    f"Date range: {df['date'].min().strftime('%b %d, %Y')} – {df['date'].max().strftime('%b %d, %Y')}"
)

if filtered.empty:
    st.warning(
        "🔍 **No data matches your filters.**\n\n"
        "Try adjusting the date range, regions, products, or segments."
    )
    with st.expander("Active Filters"):
        st.write(f"- **Regions:** {', '.join(regions) if regions else 'None'}")
        st.write(f"- **Products:** {', '.join(products) if products else 'None'}")
        st.write(f"- **Segments:** {', '.join(segments) if segments else 'None'}")
        if date_range and len(date_range) == 2:
            st.write(f"- **Date Range:** {date_range[0]} to {date_range[1]}")
    st.stop()

st.divider()

# ═══════════════════════════════════════════════════════════════════════════════
# SECTION 7: KPI Row
# ═══════════════════════════════════════════════════════════════════════════════

kpis = compute_kpis(filtered)

c1, c2, c3, c4 = st.columns(4)
c1.metric("Total Revenue", f"${kpis['total_revenue']:,.0f}", icon="💰")
c2.metric("Total Profit", f"${kpis['total_profit']:,.0f}", icon="📈")
c3.metric("Total Orders", f"{kpis['total_orders']:,}", icon="📦")
c4.metric("Profit Margin", f"{kpis['profit_margin']:.1f}%", icon="🎯")

# Second row of KPIs
c5, c6, c7, c8 = st.columns(4)
c5.metric("Avg Order Value", f"${kpis['avg_order_value']:,.2f}", icon="🛒")
c6.metric("Unique Products", f"{kpis['unique_products']}", icon="📋")
c7.metric("Avg Items/Order", f"{kpis['avg_quantity']:.1f}", icon="📊")
c8.metric("Revenue/Day", f"${kpis['total_revenue'] / len(filtered['date'].unique()):,.0f}", icon="📅")

st.divider()

# ═══════════════════════════════════════════════════════════════════════════════
# SECTION 8: Charts (Tabbed Layout)
# ═══════════════════════════════════════════════════════════════════════════════

tab_trend, tab_breakdown, tab_segment, tab_correlation = st.tabs(
    ["📈 Revenue Trend", "📊 Product Breakdown", "🏢 By Segment", "🔗 Correlation"]
)

with tab_trend:
    col_chart, col_summary = st.columns([2, 1])

    with col_chart:
        daily = filtered.groupby("date").agg({
            "revenue": "sum",
            "profit": "sum",
            "quantity": "sum",
        }).reset_index()

        if show_trend:
            daily["revenue_ma"] = daily["revenue"].rolling(7, min_periods=1).mean()

        if chart_type == "Line":
            fig = px.line(daily, x="date", y="revenue", title="Daily Revenue Trend")
            if show_trend:
                fig.add_scatter(
                    x=daily["date"], y=daily["revenue_ma"],
                    name="7-day MA", line=dict(dash="dash", color="#FF4B4B"),
                )
        elif chart_type == "Bar":
            fig = px.bar(daily, x="date", y="revenue", title="Daily Revenue")
        else:
            fig = px.area(daily, x="date", y="revenue", title="Daily Revenue Trend")
            if show_trend:
                fig.add_scatter(
                    x=daily["date"], y=daily["revenue_ma"],
                    name="7-day MA", line=dict(dash="dash", color="#FF4B4B"),
                )

        fig.update_layout(
            height=450,
            xaxis_title="Date",
            yaxis_title="Revenue ($)",
            hovermode="x unified",
        )
        st.plotly_chart(fig, use_container_width=True)

    with col_summary:
        st.subheader("Trend Summary")
        avg_daily = daily["revenue"].mean()
        best_day = daily.loc[daily["revenue"].idxmax()]
        worst_day = daily.loc[daily["revenue"].idxmin()]

        st.metric("Avg Daily Revenue", f"${avg_daily:,.0f}")
        st.metric("Best Day", best_day["date"].strftime("%b %d"),
                  f"${best_day['revenue']:,.0f}")
        st.metric("Worst Day", worst_day["date"].strftime("%b %d"),
                  f"${worst_day['revenue']:,.0f}")
        st.metric("Total Days", f"{len(daily):,}")

with tab_breakdown:
    col_bar, col_pie = st.columns(2)

    with col_bar:
        product_revenue = (
            filtered.groupby("product")["revenue"]
            .sum()
            .sort_values(ascending=True)
            .reset_index()
        )
        fig_bar = px.bar(
            product_revenue,
            x="revenue", y="product",
            orientation="h",
            title="Revenue by Product",
            color="revenue",
            color_continuous_scale="Teal",
        )
        fig_bar.update_layout(
            height=450,
            xaxis_title="Revenue ($)",
            yaxis_title="",
            showlegend=False,
        )
        st.plotly_chart(fig_bar, use_container_width=True)

    with col_pie:
        product_profit = (
            filtered.groupby("product")["profit"]
            .sum()
            .reset_index()
        )
        fig_pie = px.pie(
            product_profit,
            values="profit", names="product",
            title="Profit Distribution",
            hole=0.3,
        )
        fig_pie.update_layout(height=450)
        st.plotly_chart(fig_pie, use_container_width=True)

    # Product detail table
    st.subheader("Product Performance Table")
    product_detail = filtered.groupby("product").agg({
        "revenue": "sum",
        "profit": "sum",
        "quantity": "sum",
        "unit_price": "mean",
    }).round(2).sort_values("revenue", ascending=False)
    product_detail["margin_%"] = (product_detail["profit"] / product_detail["revenue"] * 100).round(1)
    product_detail.columns = ["Revenue", "Profit", "Qty Sold", "Avg Price", "Margin %"]
    st.dataframe(product_detail, use_container_width=True)

with tab_segment:
    col_seg_bar, col_seg_table = st.columns([1, 1])

    with col_seg_bar:
        segment_data = (
            filtered.groupby("segment")
            .agg({"revenue": "sum", "profit": "sum"})
            .reset_index()
        )
        fig_seg = px.bar(
            segment_data,
            x="segment", y=["revenue", "profit"],
            barmode="group",
            title="Revenue & Profit by Segment",
            color_discrete_map={"revenue": "#4ECDC4", "profit": "#45B7D1"},
        )
        fig_seg.update_layout(
            height=450,
            xaxis_title="Customer Segment",
            yaxis_title="Amount ($)",
        )
        st.plotly_chart(fig_seg, use_container_width=True)

    with col_seg_table:
        st.subheader("Segment Breakdown")
        seg_detail = (
            filtered.groupby("segment")
            .agg({
                "revenue": "sum",
                "profit": "sum",
                "quantity": "sum",
            })
            .round(2)
        )
        seg_detail["margin_%"] = (seg_detail["profit"] / seg_detail["revenue"] * 100).round(1)
        seg_detail["orders"] = filtered.groupby("segment").size()
        seg_detail = seg_detail[["revenue", "profit", "orders", "quantity", "margin_%"]]
        seg_detail.columns = ["Revenue", "Profit", "Orders", "Qty Sold", "Margin %"]
        st.dataframe(seg_detail, use_container_width=True)

with tab_correlation:
    st.subheader("Revenue vs Profit by Product")

    sample = filtered.sample(min(500, len(filtered)), random_state=42)
    fig_corr = px.scatter(
        sample,
        x="revenue", y="profit",
        color="product",
        size="quantity",
        hover_data=["region", "segment"],
        title="Revenue vs Profit (sampled)",
        opacity=0.6,
    )
    fig_corr.update_layout(
        height=500,
        xaxis_title="Revenue ($)",
        yaxis_title="Profit ($)",
    )
    st.plotly_chart(fig_corr, use_container_width=True)

    # Correlation matrix
    st.subheader("Correlation Matrix")
    numeric_cols = filtered[["revenue", "profit", "quantity", "unit_price", "cost"]]
    corr = numeric_cols.corr()
    fig_heat = px.imshow(
        corr,
        text_auto=".2f",
        color_continuous_scale="RdBu_r",
        title="Feature Correlations",
    )
    fig_heat.update_layout(height=400)
    st.plotly_chart(fig_heat, use_container_width=True)

# ═══════════════════════════════════════════════════════════════════════════════
# SECTION 9: Data Table (Progressive Disclosure)
# ═══════════════════════════════════════════════════════════════════════════════

st.divider()

with st.expander("📋 View Filtered Data", expanded=False):
    st.dataframe(
        filtered.sort_values("revenue", ascending=False),
        use_container_width=True,
        hide_index=True,
        column_config={
            "date": st.column_config.DateColumn("Date", format="MMM DD, YYYY"),
            "revenue": st.column_config.NumberColumn("Revenue", format="$%,.2f"),
            "profit": st.column_config.NumberColumn("Profit", format="$%,.2f"),
            "unit_price": st.column_config.NumberColumn("Unit Price", format="$%,.2f"),
            "cost": st.column_config.NumberColumn("Cost", format="$%,.2f"),
        },
        height=400,
    )

with st.expander("📈 Summary Statistics", expanded=False):
    st.dataframe(
        filtered[["revenue", "profit", "quantity", "unit_price", "cost"]].describe(),
        use_container_width=True,
    )

# ═══════════════════════════════════════════════════════════════════════════════
# SECTION 10: Export
# ═══════════════════════════════════════════════════════════════════════════════

st.divider()
st.subheader("📥 Export Data")

col_csv, col_excel, col_json = st.columns(3)

with col_csv:
    st.download_button(
        "📥 Download CSV",
        data=filtered.to_csv(index=False),
        file_name="explorer_sales.csv",
        mime="text/csv",
        use_container_width=True,
    )

with col_excel:
    buffer = io.BytesIO()
    with pd.ExcelWriter(buffer, engine="openpyxl") as writer:
        filtered.to_excel(writer, index=False, sheet_name="Sales")
        product_detail.reset_index().to_excel(writer, index=False, sheet_name="Products")
    st.download_button(
        "📥 Download Excel",
        data=buffer.getvalue(),
        file_name="explorer_sales.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        use_container_width=True,
    )

with col_json:
    st.download_button(
        "📥 Download JSON",
        data=filtered.to_json(orient="records", date_format="iso"),
        file_name="explorer_sales.json",
        mime="application/json",
        use_container_width=True,
    )

# ═══════════════════════════════════════════════════════════════════════════════
# SECTION 11: Footer
# ═══════════════════════════════════════════════════════════════════════════════

st.divider()
st.caption(
    "Interactive Data Explorer · Module 06 · "
    "Streamlit for Data Science · "
    "Data: Synthetic E-Commerce Sales"
)
