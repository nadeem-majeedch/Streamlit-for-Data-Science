"""
✏️ Exercise 10 — Interactive Dashboard Workshop
=================================================
Module 06 · Intermediate

Build a complete Interactive Data Explorer dashboard from scratch.

Run this file:
    streamlit run exercises/10_dashboard_workshop.py

Instructions:
    Complete each challenge independently. Do NOT copy code from the notebooks.
    Each challenge builds different skills — read the requirements carefully.

Related Materials:
- 📖 Reading: ../readings/10_interactive_dashboard.md
- 📓 Notebook: ../notebooks/10_interactive_dashboard.ipynb
- 🖥️ Demo App: ../apps/10_interactive_data_explorer.py
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# ---------------------------------------------------------------------------
# Page Config
# ---------------------------------------------------------------------------
st.set_page_config(
    page_title="Exercise 10 — Dashboard Workshop",
    page_icon="✏️",
    layout="wide",
)

st.title("✏️ Exercise 10 — Interactive Dashboard Workshop")
st.markdown(
    "Build a complete Interactive Data Explorer dashboard.\\n"
    "Complete each challenge independently."
)

st.divider()

# ---------------------------------------------------------------------------
# Step 1: Generate Dataset
# ---------------------------------------------------------------------------
st.header("Step 1 — Generate E-Commerce Data")

# TODO 1: Create a function `generate_sales_data(n_rows=1500)` that returns
# a DataFrame with these columns:
#   - date: pd.date_range("2024-01-01", periods=365, freq="D"), sampled randomly
#   - product: random choice of ["Laptop", "Phone", "Tablet", "Headphones", "Monitor"]
#   - region: random choice of ["North America", "Europe", "Asia Pacific", "Latin America"]
#   - segment: random choice of ["Consumer", "Corporate", "Home Office"]
#   - unit_price: varies by product (Laptop ~1200, Phone ~800, etc.) * random uniform 0.8-1.2
#   - quantity: random int 1-9
#   - revenue: unit_price * quantity (rounded to 2 decimals)
#   - cost: revenue * random uniform 0.4-0.7 (rounded to 2 decimals)
#   - profit: revenue - cost (rounded to 2 decimals)
#
# Use np.random.seed(42) for reproducibility.
# Decorate with @st.cache_data
# Display the shape and first 5 rows.

# --- START YOUR CODE HERE ---
# @st.cache_data
# def generate_sales_data(n_rows=1500):
#     np.random.seed(42)
#     dates = pd.date_range("2024-01-01", periods=365, freq="D")
#     products = ["Laptop", "Phone", "Tablet", "Headphones", "Monitor"]
#     regions = ["North America", "Europe", "Asia Pacific", "Latin America"]
#     segments = ["Consumer", "Corporate", "Home Office"]
#     base_prices = {"Laptop": 1200, "Phone": 800, "Tablet": 500, "Headphones": 150, "Monitor": 400}
#
#     data = []
#     for _ in range(n_rows):
#         product = np.random.choice(products)
#         unit_price = base_prices[product] * np.random.uniform(0.8, 1.2)
#         quantity = np.random.randint(1, 10)
#         revenue = round(unit_price * quantity, 2)
#         cost = round(revenue * np.random.uniform(0.4, 0.7), 2)
#         data.append({
#             "date": np.random.choice(dates),
#             "product": product,
#             "region": np.random.choice(regions),
#             "segment": np.random.choice(segments),
#             "unit_price": round(unit_price, 2),
#             "quantity": quantity,
#             "revenue": revenue,
#             "cost": cost,
#             "profit": round(revenue - cost, 2),
#         })
#     return pd.DataFrame(data)
#
# df = generate_sales_data()
# st.write(f"Shape: {df.shape}")
# st.dataframe(df.head(), use_container_width=True)
# --- END YOUR CODE HERE ---

st.divider()

# ---------------------------------------------------------------------------
# Step 2: Data Functions
# ---------------------------------------------------------------------------
st.header("Step 2 — Data Functions (No Streamlit Calls!)")

st.markdown(
    "**Key principle:** Data functions must be pure — no `st.*` calls inside.\n"
    "This makes them testable, reusable, and cacheable."
)

# TODO 2a: Create `filter_data(df, regions, products, segments, date_range)` that:
#   - Starts with a copy of df
#   - Filters by region if regions list is not empty
#   - Filters by product if products list is not empty
#   - Filters by segment if segments list is not empty
#   - Filters by date_range if it has 2 elements
#   - Returns the filtered DataFrame

# --- START YOUR CODE HERE ---
# def filter_data(df, regions, products, segments, date_range):
#     result = df.copy()
#     if regions:
#         result = result[result["region"].isin(regions)]
#     if products:
#         result = result[result["product"].isin(products)]
#     if segments:
#         result = result[result["segment"].isin(segments)]
#     if date_range and len(date_range) == 2:
#         start, end = pd.Timestamp(date_range[0]), pd.Timestamp(date_range[1])
#         result = result[(result["date"] >= start) & (result["date"] <= end)]
#     return result
# --- END YOUR CODE HERE ---

# TODO 2b: Create `compute_kpis(df)` that returns a dict with:
#   - total_revenue: sum of revenue
#   - total_profit: sum of profit
#   - total_orders: len(df)
#   - avg_order_value: revenue / orders (0 if orders is 0)
#   - profit_margin: (profit / revenue * 100) (0 if revenue is 0)

# --- START YOUR CODE HERE ---
# def compute_kpis(df):
#     total_revenue = df["revenue"].sum()
#     total_profit = df["profit"].sum()
#     total_orders = len(df)
#     avg_order_value = total_revenue / total_orders if total_orders > 0 else 0
#     profit_margin = (total_profit / total_revenue * 100) if total_revenue > 0 else 0
#     return {
#         "total_revenue": total_revenue,
#         "total_profit": total_profit,
#         "total_orders": total_orders,
#         "avg_order_value": avg_order_value,
#         "profit_margin": profit_margin,
#     }
# --- END YOUR CODE HERE ---

st.info("💡 After defining these functions, test them by calling them below the definitions.")

st.divider()

# ---------------------------------------------------------------------------
# Step 3: Sidebar Filters
# ---------------------------------------------------------------------------
st.header("Step 3 — Sidebar Filter Panel")

# TODO 3: Create a sidebar with these controls:
#   a) st.sidebar.header("🔍 Filters")
#   b) date_input for "Date range" (default: full date range)
#   c) multiselect for "Region" (default: all)
#   d) multiselect for "Product" (default: all)
#   e) multiselect for "Customer Segment" (default: all)
#   f) st.sidebar.divider()
#   g) st.sidebar.header("⚙️ Display")
#   h) radio for "Chart type" ["Line", "Bar", "Area"] (horizontal=True)
#   i) checkbox for "Show 7-day moving average" (default: True)

# --- START YOUR CODE HERE ---
# with st.sidebar:
#     st.header("🔍 Filters")
#     date_range = st.date_input("Date range", value=(df["date"].min(), df["date"].max()))
#     regions = st.multiselect("Region", df["region"].unique().tolist(), default=df["region"].unique().tolist())
#     products = st.multiselect("Product", df["product"].unique().tolist(), default=df["product"].unique().tolist())
#     segments = st.multiselect("Customer Segment", df["segment"].unique().tolist(), default=df["segment"].unique().tolist())
#     st.sidebar.divider()
#     st.sidebar.header("⚙️ Display")
#     chart_type = st.radio("Chart type", ["Line", "Bar", "Area"], horizontal=True)
#     show_trend = st.checkbox("Show 7-day moving average", value=True)
# --- END YOUR CODE HERE ---

st.divider()

# ---------------------------------------------------------------------------
# Step 4: Apply Filters & Handle Empty State
# ---------------------------------------------------------------------------
st.header("Step 4 — Filter Application & Empty State")

# TODO 4: Apply filters using filter_data() and handle empty results:
#   a) filtered = filter_data(df, regions, products, segments, date_range)
#   b) If filtered.empty:
#      - Show st.warning with a helpful message
#      - Show active filters
#      - Call st.stop()
#   c) Otherwise, show record count

# --- START YOUR CODE HERE ---
# filtered = filter_data(df, regions, products, segments, date_range)
#
# if filtered.empty:
#     st.warning("🔍 No data matches your filters. Try adjusting criteria.")
#     st.write(f"Active filters: Regions={regions}, Products={products}, Segments={segments}")
#     st.stop()
#
# st.write(f"Showing **{len(filtered):,}** of **{len(df):,}** records")
# --- END YOUR CODE HERE ---

st.divider()

# ---------------------------------------------------------------------------
# Step 5: KPI Metrics
# ---------------------------------------------------------------------------
st.header("Step 5 — KPI Metric Row")

# TODO 5: Display 4 KPI cards:
#   a) Compute kpis = compute_kpis(filtered)
#   b) Create st.columns(4)
#   c) Total Revenue (formatted as $X,XXX,XXX, icon="💰")
#   d) Total Profit (formatted as $X,XXX,XXX, icon="📈")
#   e) Total Orders (formatted with commas, icon="📦")
#   f) Profit Margin (formatted as X.X%, icon="🎯")

# --- START YOUR CODE HERE ---
# kpis = compute_kpis(filtered)
# c1, c2, c3, c4 = st.columns(4)
# c1.metric("Total Revenue", f"${kpis['total_revenue']:,.0f}", icon="💰")
# c2.metric("Total Profit", f"${kpis['total_profit']:,.0f}", icon="📈")
# c3.metric("Total Orders", f"{kpis['total_orders']:,}", icon="📦")
# c4.metric("Profit Margin", f"{kpis['profit_margin']:.1f}%", icon="🎯")
# --- END YOUR CODE HERE ---

st.divider()

# ---------------------------------------------------------------------------
# Step 6: Charts
# ---------------------------------------------------------------------------
st.header("Step 6 — Tabbed Charts")

# TODO 6: Create 3 tabs with Plotly charts:
#   Tab 1: "📈 Revenue Trend"
#     - Aggregate revenue by date
#     - Create a line/bar/area chart based on chart_type
#     - If show_trend, add 7-day moving average line
#     - Use use_container_width=True
#
#   Tab 2: "📊 Product Breakdown"
#     - Horizontal bar chart of revenue by product
#     - Pie chart of profit by product
#     - Use st.columns([1, 1])
#
#   Tab 3: "🏢 By Segment"
#     - Grouped bar chart of revenue & profit by segment
#     - Use px.bar with barmode="group"

# --- START YOUR CODE HERE ---
# tab_trend, tab_breakdown, tab_segment = st.tabs(["📈 Revenue Trend", "📊 Product Breakdown", "🏢 By Segment"])
#
# with tab_trend:
#     daily = filtered.groupby("date").agg({"revenue": "sum", "profit": "sum"}).reset_index()
#     if show_trend:
#         daily["revenue_ma"] = daily["revenue"].rolling(7, min_periods=1).mean()
#     if chart_type == "Line":
#         fig = px.line(daily, x="date", y="revenue", title="Daily Revenue")
#     elif chart_type == "Bar":
#         fig = px.bar(daily, x="date", y="revenue", title="Daily Revenue")
#     else:
#         fig = px.area(daily, x="date", y="revenue", title="Daily Revenue")
#     if show_trend:
#         fig.add_scatter(x=daily["date"], y=daily["revenue_ma"], name="7-day MA", line=dict(dash="dash"))
#     fig.update_layout(height=400)
#     st.plotly_chart(fig, use_container_width=True)
#
# with tab_breakdown:
#     col1, col2 = st.columns(2)
#     with col1:
#         rev_by_product = filtered.groupby("product")["revenue"].sum().sort_values(ascending=True)
#         fig1 = px.bar(x=rev_by_product.values, y=rev_by_product.index, orientation="h", title="Revenue by Product")
#         fig1.update_layout(height=400)
#         st.plotly_chart(fig1, use_container_width=True)
#     with col2:
#         profit_data = filtered.groupby("product")["profit"].sum().reset_index()
#         fig2 = px.pie(profit_data, values="profit", names="product", title="Profit Distribution")
#         fig2.update_layout(height=400)
#         st.plotly_chart(fig2, use_container_width=True)
#
# with tab_segment:
#     seg_data = filtered.groupby("segment").agg({"revenue": "sum", "profit": "sum"}).reset_index()
#     fig3 = px.bar(seg_data, x="segment", y=["revenue", "profit"], barmode="group", title="Revenue & Profit by Segment")
#     fig3.update_layout(height=400)
#     st.plotly_chart(fig3, use_container_width=True)
# --- END YOUR CODE HERE ---

st.divider()

# ---------------------------------------------------------------------------
# Step 7: Data Table & Export (Bonus)
# ---------------------------------------------------------------------------
st.header("Step 7 — Data Table & Export (Bonus)")

# TODO 7: Add progressive disclosure and export:
#   a) An expander with the filtered data (sorted by revenue desc)
#   b) An expander with summary statistics (.describe())
#   c) A CSV download button
#   d) An Excel download button (requires openpyxl)

# --- START YOUR CODE HERE ---
# with st.expander("📋 View Filtered Data", expanded=False):
#     st.dataframe(filtered.sort_values("revenue", ascending=False), use_container_width=True, hide_index=True)
#
# with st.expander("📈 Summary Statistics", expanded=False):
#     st.dataframe(filtered[["revenue", "profit", "quantity"]].describe(), use_container_width=True)
#
# col1, col2 = st.columns(2)
# with col1:
#     st.download_button("📥 Download CSV", filtered.to_csv(index=False), "filtered_sales.csv", use_container_width=True)
# with col2:
#     import io
#     buffer = io.BytesIO()
#     with pd.ExcelWriter(buffer, engine="openpyxl") as writer:
#         filtered.to_excel(writer, index=False, sheet_name="Sales")
#     st.download_button("📥 Download Excel", buffer.getvalue(), "filtered_sales.xlsx", use_container_width=True)
# --- END YOUR CODE HERE ---

# ---------------------------------------------------------------------------
# Footer
# ---------------------------------------------------------------------------
st.divider()
st.caption(
    "Exercise 10 — Interactive Dashboard Workshop · Module 06 · Streamlit for Data Science"
)
