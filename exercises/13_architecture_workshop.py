"""
Exercise 13: Architecture & Multipage Apps Workshop
====================================================

Module 09 · Advanced

Master Streamlit application architecture and multipage apps.

Learning Objectives:
- Structure applications from single-file to modular
- Separate UI, data, and business logic
- Create multipage applications
- Implement shared components

Instructions:
Complete each section by filling in the TODOs.
Run with: streamlit run exercises/13_architecture_workshop.py
"""

import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Architecture Workshop", page_icon="🏗️", layout="wide")
st.title("🏗️ Exercise 13: Architecture Workshop")
st.markdown("*Module 09 · Advanced — Build maintainable Streamlit apps*")

st.divider()

# ============================================================================
# CHALLENGE 1: Refactor to Functions
# ============================================================================
st.header("🎯 Challenge 1: Refactor to Functions")
st.write("The code below works but is messy. Refactor it into clean, separated functions.")

st.subheader("Current Messy Code:")
st.code('''
# ❌ BAD: Everything mixed together
np.random.seed(42)
df = pd.DataFrame({
    "category": np.random.choice(["A", "B", "C"], 100),
    "value": np.random.randn(100) * 10 + 50,
    "quantity": np.random.randint(1, 50, 100)
})

category = st.selectbox("Filter", ["All", "A", "B", "C"])
if category != "All":
    df = df[df["category"] == category]

st.metric("Total Rows", len(df))
st.metric("Avg Value", f"{df['value'].mean():.1f}")
st.metric("Total Quantity", df["quantity"].sum())

st.dataframe(df)
st.line_chart(df[["value", "quantity"]])
''', language="python")

st.subheader("Your Refactored Code:")

# TODO: Create a data loading function
# @st.cache_data
# def load_data(n_rows):
#     """Load sample data."""
#     pass

# TODO: Create a filtering function
# def filter_data(df, category):
#     """Filter DataFrame by category."""
#     pass

# TODO: Create a metrics computation function
# def compute_metrics(df):
#     """Compute summary metrics."""
#     pass

# TODO: Create UI rendering functions
# def render_metrics(metrics):
#     """Render metric cards."""
#     pass

# def render_data(df):
#     """Render data table."""
#     pass

# def render_charts(df):
#     """Render visualizations."""
#     pass

# TODO: Implement the main flow using your functions
# load_data → filter_data → compute_metrics → render_*

st.divider()

# ============================================================================
# CHALLENGE 2: Build Reusable Components
# ============================================================================
st.header("🎯 Challenge 2: Reusable Components")
st.write("Create a library of reusable UI components.")

# TODO: Create a metric card component
# def metric_card(label, value, delta=None, delta_color="normal"):
#     """Render a consistent metric card."""
#     pass

# TODO: Create a data preview component
# def data_preview(df, max_rows=5, show_shape=True):
#     """Show data with consistent formatting."""
#     pass

# TODO: Create a section header component
# def section_header(title, description=None, divider=True):
#     """Render section header with optional description."""
#     pass

# TODO: Create a status badge component
# def status_badge(status):
#     """Render status with appropriate color/icon."""
#     pass

# --- Test Your Components ---
# Use your components to build a dashboard:

# section_header("Sales Dashboard", "Key metrics for Q4 2024")

# col1, col2, col3 = st.columns(3)
# with col1:
#     metric_card("Revenue", "$1.2M", "+12%")
# with col2:
#     metric_card("Orders", "3,450", "+8%")
# with col3:
#     metric_card("Returns", "42", "-15%", delta_color="inverse")

# data_preview(your_dataframe)

st.divider()

# ============================================================================
# CHALLENGE 3: Configuration Pattern
# ============================================================================
st.header("🎯 Challenge 3: Configuration Module")
st.write("Centralize app settings in a configuration dictionary.")

# TODO: Create a configuration dictionary
# APP_CONFIG = {
#     "title": "My Data Dashboard",
#     "icon": "📊",
#     "max_rows": 10000,
#     "cache_ttl": 3600,
#     "theme": "light",
#     "categories": ["Electronics", "Clothing", "Food", "Books"],
#     "currency_symbol": "$",
# }

# TODO: Use configuration throughout the app
# st.set_page_config(
#     page_title=APP_CONFIG["title"],
#     page_icon=APP_CONFIG["icon"]
# )

# TODO: Display current configuration
# with st.expander("📋 Current Configuration"):
#     st.json(APP_CONFIG)

# TODO: Add configuration editing
# with st.sidebar:
#     st.subheader("⚙️ Settings")
#     APP_CONFIG["theme"] = st.selectbox("Theme", ["light", "dark"])
#     APP_CONFIG["max_rows"] = st.number_input("Max Rows", 100, 100000, APP_CONFIG["max_rows"])

st.divider()

# ============================================================================
# CHALLENGE 4: Multipage Navigation
# ============================================================================
st.header("🎯 Challenge 4: Multipage Navigation")
st.write("Design a multipage app structure.")

st.subheader("App Structure Design")

# TODO: Design your page structure
# pages = {
#     "Main": [
#         {"file": "pages/home.py", "title": "Home", "icon": "🏠"},
#         {"file": "pages/explore.py", "title": "Explore Data", "icon": "📊"},
#     ],
#     "Analysis": [
#         {"file": "pages/analysis.py", "title": "Statistical Analysis", "icon": "📈"},
#         {"file": "pages/ml.py", "title": "ML Models", "icon": "🤖"},
#     ],
#     "Settings": [
#         {"file": "pages/config.py", "title": "Configuration", "icon": "⚙️"},
#     ]
# }

# TODO: Display the planned structure
# st.write("**Planned Pages:**")
# for section, page_list in pages.items():
#     st.write(f"**{section}:**")
#     for page in page_list:
#         st.write(f"  - {page['icon']} {page['title']} ({page['file']})")

# TODO: Show the st.navigation code that would implement this
# st.code('''
# import streamlit as st
# 
# pages = {
#     "Main": [
#         st.Page("pages/home.py", title="Home", icon="🏠"),
#         st.Page("pages/explore.py", title="Explore Data", icon="📊"),
#     ],
#     "Analysis": [
#         st.Page("pages/analysis.py", title="Analysis", icon="📈"),
#         st.Page("pages/ml.py", title="ML Models", icon="🤖"),
#     ]
# }
# 
# pg = st.navigation(pages)
# pg.run()
# ''', language="python")

st.divider()

# ============================================================================
# CHALLENGE 5: Data Logic Separation
# ============================================================================
st.header("🎯 Challenge 5: Separated Data Logic")
st.write("Practice separating data concerns from UI concerns.")

# TODO: Create data layer functions
# @st.cache_data
# def load_sales_data(region):
#     """Load sales data for a region."""
#     pass

# @st.cache_data
# def compute_top_products(df, n=10):
#     """Get top N products by revenue."""
#     pass

# @st.cache_data
# def compute_monthly_trend(df):
#     """Compute monthly revenue trend."""
#     pass

# TODO: Create business logic functions
# def calculate_growth_rate(current, previous):
#     """Calculate percentage growth rate."""
#     pass

# def classify_performance(value, thresholds):
#     """Classify performance as Excellent/Good/Fair/Poor."""
#     pass

# TODO: Create UI functions that use data and business logic
# def render_top_products(df):
#     """Display top products."""
#     pass

# def render_trend_chart(df):
#     """Display trend visualization."""
#     pass

# TODO: Main flow using separated concerns
# region = st.sidebar.selectbox("Region", ["North", "South", "East", "West"])
# 
# # Data layer
# sales_data = load_sales_data(region)
# top_products = compute_top_products(sales_data)
# monthly_trend = compute_monthly_trend(sales_data)
# 
# # UI layer
# render_top_products(top_products)
# render_trend_chart(monthly_trend)

st.divider()

# ============================================================================
# BONUS: Testing Pattern
# ============================================================================
st.header("🏆 Bonus: Testing Pattern")
st.write("Practice testing business logic without Streamlit.")

st.code('''
# tests/test_business_logic.py

import pytest
from your_module import calculate_growth_rate, classify_performance

def test_calculate_growth_rate():
    assert calculate_growth_rate(120, 100) == 20.0
    assert calculate_growth_rate(80, 100) == -20.0
    assert calculate_growth_rate(100, 100) == 0.0

def test_classify_performance():
    assert classify_performance(95, {"excellent": 90}) == "Excellent"
    assert classify_performance(75, {"excellent": 90, "good": 70}) == "Good"
    assert classify_performance(50, {"excellent": 90, "good": 70}) == "Fair"
''', language="python")

# TODO: Implement the functions above
# def calculate_growth_rate(current, previous):
#     """Calculate percentage growth rate."""
#     pass

# def classify_performance(value, thresholds):
#     """Classify performance based on thresholds."""
#     pass

# # Test your functions
# if st.button("Run Tests"):
#     try:
#         assert calculate_growth_rate(120, 100) == 20.0
#         st.success("✅ Test 1 passed: Positive growth")
#     except AssertionError:
#         st.error("❌ Test 1 failed")
#     
#     try:
#         assert calculate_growth_rate(80, 100) == -20.0
#         st.success("✅ Test 2 passed: Negative growth")
#     except AssertionError:
#         st.error("❌ Test 2 failed")

st.divider()

# ============================================================================
# COMPLETION
# ============================================================================
st.success("🎉 Workshop Complete!")
st.markdown("""
**What you practiced:**
- ✅ Refactoring monolithic code into functions
- ✅ Creating reusable UI components
- ✅ Implementing configuration patterns
- ✅ Designing multipage app structures
- ✅ Separating data, business logic, and UI
- ✅ Testing business logic independently

**Key architectural principles:**
- Single Responsibility: each function does one thing
- Separation of Concerns: UI, Data, Business Logic
- DRY: Don't Repeat Yourself
- Configuration: single source of truth

**Next steps:**
- Read: [Application Architecture](../readings/13_application_architecture.md)
- Notebook: [Application Architecture](../notebooks/13_application_architecture.ipynb)
- Demo App: [Modular App](../apps/13_modular_app/app.py)
""")

# Run check
if __name__ == "__main__":
    st.write("✅ Exercise file is valid and ready to run!")
