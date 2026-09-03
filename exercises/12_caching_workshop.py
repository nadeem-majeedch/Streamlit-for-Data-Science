"""
Exercise 12: Caching & Performance Workshop
=============================================

Module 08 · Advanced

Master Streamlit's caching decorators to build fast applications.

Learning Objectives:
- Distinguish between cache_data and cache_resource
- Implement TTL, max_entries, and persistence
- Build performance-aware applications

Instructions:
Complete each section by filling in the TODOs.
Run with: streamlit run exercises/12_caching_workshop.py
"""

import streamlit as st
import time
import pandas as pd
import numpy as np
from datetime import datetime

st.set_page_config(page_title="Caching Workshop", page_icon="⚡", layout="wide")
st.title("⚡ Exercise 12: Caching & Performance Workshop")
st.markdown("*Module 08 · Advanced — Master Streamlit caching*")

st.divider()

# ============================================================================
# CHALLENGE 1: Cached Data Loader
# ============================================================================
st.header("🎯 Challenge 1: Cached Data Loader")
st.write("Create a cached function that loads data with performance monitoring.")

# TODO: Create a cached function `load_data(n_rows)` that:
# - Generates random data using numpy
# - Uses @st.cache_data decorator
# - Takes n_rows as parameter
# - Sleeps 1 second to simulate I/O
# - Returns a DataFrame with columns: category, value, quantity

# TODO: Add performance tracking
# - Show spinner with "Loading data..."
# - Display time taken using show_time=True or manual timing
# - Show cache hit/miss status

# TODO: Create UI
# - Slider for n_rows (100 to 5000)
# - Button to load data
# - Display the loaded data

st.divider()

# ============================================================================
# CHALLENGE 2: Model Registry
# ============================================================================
st.header("🎯 Challenge 2: Model Registry")
st.write("Build a model loader that caches multiple ML models.")

# TODO: Create a cached function `load_model(model_name)` that:
# - Uses @st.cache_resource (models are shared resources)
# - Simulates loading with time.sleep(2)
# - Returns a dict with model metadata

# TODO: Create UI
# - Selectbox to choose model: "random_forest", "gradient_boost", "neural_net"
# - Button to load model
# - Show loaded model info

# TODO: Add model management
# - Show which models are currently cached
# - Button to clear specific model cache
# - Button to clear all model caches

st.divider()

# ============================================================================
# CHALLENGE 3: Query Cache with Statistics
# ============================================================================
st.header("🎯 Challenge 3: Query Cache with Stats")
st.write("Build a query executor that tracks cache performance.")

# TODO: Create a cached function `execute_query(query_text)` that:
# - Uses @st.cache_data with TTL=60
# - Simulates database query with time.sleep(0.5)
# - Returns a DataFrame

# TODO: Track statistics in session_state
# - total_queries (int)
# - cache_hits (int)
# - cache_misses (int)

# TODO: Create UI
# - Text area for SQL query
# - Execute button
# - Display query results
# - Show statistics (hits, misses, hit rate)

# TODO: Add cache management
# - Clear specific query cache
# - Clear all caches
# - Reset statistics

st.divider()

# ============================================================================
# CHALLENGE 4: TTL Comparison
# ============================================================================
st.header("🎯 Challenge 4: TTL Comparison")
st.write("Compare cached values with different TTL settings.")

# TODO: Create three cached functions with different TTLs:
# - get_fast_data() with TTL=5 seconds
# - get_medium_data() with TTL=30 seconds
# - get_slow_data() with no TTL (never expires)

# Each should return current timestamp

# TODO: Create UI showing:
# - Current time for each function
# - Time since cached
# - Whether cache is still valid

# TODO: Add auto-refresh
# - Checkbox to enable auto-refresh every 2 seconds
# - Show countdown to next cache expiration

st.divider()

# ============================================================================
# CHALLENGE 5: Pipeline Cache
# ============================================================================
st.header("🎯 Challenge 5: Multi-Stage Pipeline")
st.write("Cache each stage of a data processing pipeline independently.")

# TODO: Create a pipeline with three cached stages:
# 1. generate_data(n) -> DataFrame
# 2. clean_data(df) -> DataFrame (removes nulls, adds derived columns)
# 3. aggregate_data(df, group_by) -> DataFrame

# TODO: Create UI
# - Slider for n_rows
# - Selectbox for group_by column
# - Execute pipeline button
# - Show results at each stage

# TODO: Add timing display
# - Show time for each cached stage
# - Show total pipeline time
# - Highlight which stages used cache vs recomputed

st.divider()

# ============================================================================
# BONUS CHALLENGE: Cache Health Monitor
# ============================================================================
st.header("🏆 Bonus: Cache Health Monitor")
st.write("Build a tool to monitor cache performance.")

# TODO: Create functions that track:
# - Cache hit rate over time
# - Average computation time saved
# - Memory usage approximation

# TODO: Display dashboard showing:
# - Hit rate gauge
# - Time saved metric
# - Cache entry counts per function

# TODO: Add controls to:
# - Clear specific function caches
# - Clear all caches
# - Export cache statistics

st.divider()

# ============================================================================
# COMPLETION
# ============================================================================
st.success("🎉 Workshop Complete!")
st.markdown("""
**What you practiced:**
- ✅ `@st.cache_data` for data caching
- ✅ `@st.cache_resource` for shared resources
- ✅ TTL, max_entries, and cache invalidation
- ✅ Performance measurement and monitoring
- ✅ Multi-stage pipeline caching

**Key distinctions:**
- `cache_data` → returns **copies** (DataFrames, queries)
- `cache_resource` → returns **same object** (connections, models)

**Next steps:**
- Read: [Caching & Performance](../readings/12_caching_and_performance.md)
- Notebook: [Caching & Performance](../notebooks/12_caching_performance.ipynb)
- Demo App: [Caching Performance Demo](../apps/12_caching_performance_demo.py)
""")

# Run check
if __name__ == "__main__":
    st.write("✅ Exercise file is valid and ready to run!")
