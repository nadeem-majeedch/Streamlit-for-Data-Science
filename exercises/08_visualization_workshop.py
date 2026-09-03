"""
✏️ Exercise 08 — Visualization Workshop
=========================================
Module 04 · Intermediate

Master chart selection, Matplotlib, Plotly, and interactive visualization.

Run this file:
    streamlit run exercises/08_visualization_workshop.py

Instructions:
    Complete each challenge independently. Do NOT copy code from the notebooks.
    Each challenge builds different skills — read the requirements carefully.

Related Materials:
- 📖 Reading: ../readings/08_visualization_matplotlib_plotly.md
- 📓 Notebook: ../notebooks/08_interactive_visualization.ipynb
- 🖥️ Demo App: ../apps/07_data_display_demo.py
"""

import streamlit as st
import pandas as pd
import numpy as np

# ---------------------------------------------------------------------------
# Page Config
# ---------------------------------------------------------------------------
st.set_page_config(
    page_title="Exercise 08 — Visualization Workshop",
    page_icon="✏️",
    layout="wide",
)

st.title("✏️ Exercise 08 — Visualization Workshop")
st.markdown(
    "Master chart selection, Matplotlib, Plotly, and interactive visualization.\n"
    "Complete each challenge independently."
)

# ---------------------------------------------------------------------------
# Generate Data
# ---------------------------------------------------------------------------
np.random.seed(42)
n = 365

products = ["Laptop", "Phone", "Tablet", "Monitor", "Keyboard"]
regions = ["North", "South", "East", "West"]

sales_df = pd.DataFrame({
    "Date": pd.date_range("2026-01-01", periods=n, freq="D"),
    "Product": np.random.choice(products, n),
    "Region": np.random.choice(regions, n),
    "Revenue": np.random.randint(5000, 50000, n).astype(float),
    "Units": np.random.randint(5, 200, n),
    "Marketing": np.random.randint(500, 10000, n).astype(float),
    "Rating": np.random.uniform(1.0, 5.0, n).round(1),
})

st.divider()

# ---------------------------------------------------------------------------
# Challenge 1: Chart Selection
# ---------------------------------------------------------------------------
st.header("Challenge 1 — Choose the Right Chart")

st.markdown(
    "**Task:** For each question below, create the appropriate chart.\n"
    "Choose the chart type that best answers the question."
)

st.subheader("Q1: How did revenue change over the year?")
# TODO: Create a LINE chart showing monthly revenue trend
# Hint: resample to monthly, then use st.line_chart or px.line

# --- START YOUR CODE HERE ---
# monthly = sales_df.set_index("Date").resample("M")["Revenue"].sum()
# st.line_chart(monthly)
# --- END YOUR CODE HERE ---

st.subheader("Q2: Which product sold the most units?")
# TODO: Create a BAR chart showing total units per product
# Hint: groupby Product, sum Units, sort descending

# --- START YOUR CODE HERE ---
# product_units = sales_df.groupby("Product")["Units"].sum().sort_values(ascending=False)
# st.bar_chart(product_units)
# --- END YOUR CODE HERE ---

st.subheader("Q3: What is the distribution of daily revenue?")
# TODO: Create a HISTOGRAM showing revenue distribution
# Hint: Use Plotly px.histogram or Matplotlib plt.hist

# --- START YOUR CODE HERE ---
# import plotly.express as px
# fig = px.histogram(sales_df, x="Revenue", nbins=40, title="Revenue Distribution")
# st.plotly_chart(fig, use_container_width=True)
# --- END YOUR CODE HERE ---

st.subheader("Q4: Is there a relationship between marketing spend and revenue?")
# TODO: Create a SCATTER plot with Marketing on X, Revenue on Y
# Hint: Use st.scatter_chart or px.scatter

# --- START YOUR CODE HERE ---
# fig = px.scatter(sales_df, x="Marketing", y="Revenue", trendline="ols")
# st.plotly_chart(fig, use_container_width=True)
# --- END YOUR CODE HERE ---

st.subheader("Q5: How does revenue vary by region?")
# TODO: Create a BOX PLOT showing revenue distribution per region
# Hint: Use px.box

# --- START YOUR CODE HERE ---
# fig = px.box(sales_df, x="Region", y="Revenue", color="Region")
# st.plotly_chart(fig, use_container_width=True)
# --- END YOUR CODE HERE ---

st.divider()

# ---------------------------------------------------------------------------
# Challenge 2: Matplotlib Deep Dive
# ---------------------------------------------------------------------------
st.header("Challenge 2 — Matplotlib Subplots")

st.markdown(
    "**Task:** Create a 2x2 subplot grid with four different visualizations."
)

# TODO: Create a 2x2 Matplotlib figure:
#   - Top-left: Revenue histogram (colored, with mean line)
#   - Top-right: Revenue by Region (bar chart)
#   - Bottom-left: Rating distribution (histogram)
#   - Bottom-right: Marketing vs Revenue (scatter)
# Add titles to each subplot. Use plt.tight_layout().

# --- START YOUR CODE HERE ---
# import matplotlib.pyplot as plt
#
# fig, axes = plt.subplots(2, 2, figsize=(12, 10))
#
# # Top-left: Revenue histogram
# axes[0, 0].hist(sales_df["Revenue"], bins=30, edgecolor="black", alpha=0.7)
# axes[0, 0].set_title("Revenue Distribution")
# ...
#
# plt.tight_layout()
# st.pyplot(fig)
# --- END YOUR CODE HERE ---

st.divider()

# ---------------------------------------------------------------------------
# Challenge 3: Interactive Plotly Dashboard
# ---------------------------------------------------------------------------
st.header("Challenge 3 — Interactive Plotly Dashboard")

st.markdown(
    "**Task:** Build an interactive dashboard where the user controls what they see."
)

# TODO: Build a Plotly dashboard with sidebar controls:
#   a) Sidebar: selectbox for chart type (Bar/Line/Scatter)
#   b) Sidebar: selectbox for X axis (Region/Product/Date)
#   c) Sidebar: selectbox for Y axis (Revenue/Units/Marketing)
#   d) Sidebar: selectbox for Color (Region/Product/None)
#   e) Main area: Plotly chart that updates based on selections
#   f) Add use_container_width=True to the chart

# --- START YOUR CODE HERE ---
# with st.sidebar:
#     chart_type = st.selectbox("Chart type", ["Bar", "Line", "Scatter"])
#     x_col = st.selectbox("X axis", ["Region", "Product"])
#     y_col = st.selectbox("Y axis", ["Revenue", "Units"])
#     color_by = st.selectbox("Color", ["None", "Region", "Product"])
#
# color = color_by if color_by != "None" else None
# if chart_type == "Bar":
#     fig = px.bar(sales_df, x=x_col, y=y_col, color=color)
# elif chart_type == "Line":
#     ...
# st.plotly_chart(fig, use_container_width=True)
# --- END YOUR CODE HERE ---

st.divider()

# ---------------------------------------------------------------------------
# Challenge 4: Side-by-Side Comparison
# ---------------------------------------------------------------------------
st.header("Challenge 4 — Side-by-Side Comparison")

st.markdown(
    "**Task:** Compare two views of the same data in two columns."
)

# TODO: Create a side-by-side comparison:
#   a) Two columns (col1, col2)
#   b) col1: Bar chart of Revenue by Product (horizontal, sorted)
#   c) col2: Bar chart of Units by Product (horizontal, sorted)
#   d) Use different colors for each chart
#   e) Add a caption explaining the insight

# --- START YOUR CODE HERE ---
# col1, col2 = st.columns(2)
# with col1:
#     st.subheader("Revenue by Product")
#     rev = sales_df.groupby("Product")["Revenue"].sum().sort_values()
#     fig1 = px.bar(x=rev.values, y=rev.index, orientation="h")
#     st.plotly_chart(fig1, use_container_width=True)
#
# with col2:
#     st.subheader("Units by Product")
#     units = sales_df.groupby("Product")["Units"].sum().sort_values()
#     fig2 = px.bar(x=units.values, y=units.index, orientation="h", ...)
#     st.plotly_chart(fig2, use_container_width=True)
# --- END YOUR CODE HERE ---

st.divider()

# ---------------------------------------------------------------------------
# Challenge 5: Complete Visualization Dashboard (Bonus)
# ---------------------------------------------------------------------------
st.header("Challenge 5 — Complete Dashboard (Bonus)")

st.markdown(
    "**Task:** Combine everything into a polished dashboard."
)

# TODO: Build a complete visualization dashboard:
#   a) Sidebar: chart library selector (Native/Matplotlib/Plotly)
#   b) Sidebar: X-axis, Y-axis, color-by selectors
#   c) Main area: the selected chart
#   d) A second tab with a Matplotlib 2x2 subplot grid
#   e) A third tab with a correlation heatmap (seaborn or matplotlib)
#   f) Every chart has a title and axis labels
#   g) Use consistent color palette

# --- START YOUR CODE HERE ---
# library = st.sidebar.selectbox("Chart library", ["Native", "Matplotlib", "Plotly"])
# ...
# --- END YOUR CODE HERE ---

# ---------------------------------------------------------------------------
# Footer
# ---------------------------------------------------------------------------
st.divider()
st.caption(
    "Exercise 08 — Visualization Workshop · Module 04 · Streamlit for Data Science"
)
