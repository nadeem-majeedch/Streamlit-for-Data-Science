"""
✏️ Exercise 07 — Data Display Challenges
==========================================
Module 04 · Intermediate

Master st.dataframe, column_config, filtering, and data transformation.

Run this file:
    streamlit run exercises/07_data_display_challenges.py

Instructions:
    Complete each challenge independently. Do NOT copy code from the notebooks.
    Each challenge builds different skills — read the requirements carefully.

Related Materials:
- 📖 Reading: ../readings/07_data_display_dataframes.md
- 📓 Notebook: ../notebooks/07_dataframes_tables_pandas.ipynb
- 🖥️ Demo App: ../apps/07_data_display_demo.py
"""

import streamlit as st
import pandas as pd
import numpy as np

# ---------------------------------------------------------------------------
# Page Config
# ---------------------------------------------------------------------------
st.set_page_config(
    page_title="Exercise 07 — Data Display Challenges",
    page_icon="✏️",
    layout="wide",
)

st.title("✏️ Exercise 07 — Data Display Challenges")
st.markdown(
    "Master data display, formatting, filtering, and transformation.\n"
    "Complete each challenge independently."
)

st.divider()

# ---------------------------------------------------------------------------
# Challenge 1: Formatted Employee Table
# ---------------------------------------------------------------------------
st.header("Challenge 1 — Formatted Employee Table")

# TODO 1: Create an employee DataFrame with 50 rows containing:
#   - Name: random choice of 20 first names
#   - Department: ["Engineering", "Sales", "Marketing", "HR", "Finance"]
#   - Salary: random integers between 40000 and 120000
#   - Start Date: random dates between 2020-01-01 and 2026-01-01
#   - Performance Rating: random floats between 1.0 and 5.0
#
# Display it with:
#   a) Salary formatted as currency ($XX,XXX)
#   b) Start Date formatted as "MMM D, YYYY"
#   c) Rating formatted as "X.X ⭐"
#   d) Hidden index
#   e) Sorted by Salary descending
#   f) Only show top 25 rows

np.random.seed(42)

# --- START YOUR CODE HERE ---
# names = ["Alice", "Bob", ...]  # 20 names
# departments = ["Engineering", "Sales", ...]
# df = pd.DataFrame({...})
# st.dataframe(
#     df.sort_values("Salary", ascending=False).head(25),
#     hide_index=True,
#     column_config={
#         "Salary": st.column_config.NumberColumn(...),
#         "Start Date": st.column_config.DateColumn(...),
#         "Performance Rating": st.column_config.NumberColumn(...),
#     },
# )
# --- END YOUR CODE HERE ---

st.divider()

# ---------------------------------------------------------------------------
# Challenge 2: Filtered Customer Dashboard
# ---------------------------------------------------------------------------
st.header("Challenge 2 — Filtered Customer Dashboard")

# TODO 2: Create a customer dataset with 200 rows:
#   - Customer ID: CUST-001 to CUST-200
#   - Name: random 20 names
#   - City: ["New York", "London", "Tokyo", "Paris", "Sydney"]
#   - Purchase Amount: random between 10 and 5000
#   - Date: random dates in 2026
#   - Category: ["Electronics", "Clothing", "Food", "Books"]
#
# Add sidebar filters:
#   a) City: multiselect (default: all)
#   b) Purchase Amount: slider (min to max)
#   c) Category: multiselect (default: all)
#
# Display filtered results with:
#   - Purchase Amount formatted as currency
#   - Date formatted nicely
#   - Total count shown above the table
#   - A metric card showing total purchase amount

# --- START YOUR CODE HERE ---
# with st.sidebar:
#     st.header("Filters")
#     cities = st.multiselect("City", ...)
#     purchase_range = st.slider("Purchase Amount", ...)
#     cats = st.multiselect("Category", ...)
#
# filtered = df[...]
# st.write(f"Showing {len(filtered)} customers")
# st.dataframe(filtered, hide_index=True, column_config={...})
# --- END YOUR CODE HERE ---

st.divider()

# ---------------------------------------------------------------------------
# Challenge 3: Conditional Formatting Report
# ---------------------------------------------------------------------------
st.header("Challenge 3 — Conditional Formatting Report")

# TODO 3: Create a product performance dataset with 100 rows:
#   - Product: ["Laptop", "Phone", "Tablet", "Monitor", "Keyboard"]
#   - Region: ["North", "South", "East", "West"]
#   - Revenue: random between 1000 and 20000
#   - Units: random between 1 and 100
#   - Return Rate: random between 0% and 15%
#
# Display a Pandas Styler with:
#   a) Revenue colored: green (≥$15K), yellow (≥$8K), red (<$8K)
#   b) Return Rate colored: green (<5%), yellow (<10%), red (≥10%)
#   c) Revenue formatted as currency
#   d) Return Rate formatted as percentage
#
# Also show a summary table:
#   e) GroupBy Region: total Revenue, total Units, avg Return Rate
#   f) Format the summary with column_config

# --- START YOUR CODE HERE ---
# def color_revenue(val):
#     ...
#
# def color_return_rate(val):
#     ...
#
# styled = df.style.applymap(color_revenue, subset=["Revenue"])
# styled = styled.applymap(color_return_rate, subset=["Return Rate"])
# st.dataframe(styled)
# --- END YOUR CODE HERE ---

st.divider()

# ---------------------------------------------------------------------------
# Challenge 4: Pivot Table Explorer
# ---------------------------------------------------------------------------
st.header("Challenge 4 — Pivot Table Explorer")

# TODO 4: Using the same product dataset from Challenge 3:
#   a) Create a pivot table: rows=Region, columns=Product, values=Revenue
#   b) Display it with NumberColumn formatting
#   c) Add a "Total" column (row sums)
#   d) Add a "Total" row (column sums) using pd.concat
#   e) Show the pivot table with a heatmap-style coloring using Styler

# --- START YOUR CODE HERE ---
# pivot = df.pivot_table(values="Revenue", index="Region", columns="Product", aggfunc="sum")
# ... add totals ...
# st.dataframe(styled_pivot)
# --- END YOUR CODE HERE ---

st.divider()

# ---------------------------------------------------------------------------
# Challenge 5: Interactive Row Selection (Bonus)
# ---------------------------------------------------------------------------
st.header("Challenge 5 — Row Selection Analytics (Bonus)")

# TODO 5: Build an interactive analytics view:
#   a) Generate 100 rows of sales data (Date, Product, Revenue, Units, Region)
#   b) Display with st.dataframe using on_select="rerun" and selection_mode="multi-row"
#   c) When rows are selected:
#      - Show 3 metric cards: Total Revenue, Total Units, Avg Revenue/Unit
#      - Show a detail table of selected rows
#   d) Add a download button for selected data as CSV

# --- START YOUR CODE HERE ---
# selection = st.dataframe(
#     df, on_select="rerun", selection_mode="multi-row", ...
# )
# if selection and selection["selection"]["rows"]:
#     selected = df.iloc[selection["selection"]["rows"]]
#     c1, c2, c3 = st.columns(3)
#     c1.metric("Total Revenue", f"${selected['Revenue'].sum():,.0f}")
#     ...
# --- END YOUR CODE HERE ---

# ---------------------------------------------------------------------------
# Footer
# ---------------------------------------------------------------------------
st.divider()
st.caption(
    "Exercise 07 — Data Display Challenges · Module 04 · Streamlit for Data Science"
)
