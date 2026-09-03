"""
Explore Page
============

Interactive data exploration with filters and visualizations.
"""

import streamlit as st
import pandas as pd
from components import (
    section_header, data_preview, metric_row, 
    sidebar_select, sidebar_multiselect
)
from data_loader import (
    load_sample_data, filter_data, compute_summary_stats,
    compute_category_breakdown, compute_monthly_trend
)
from config import CATEGORIES, REGIONS


def render():
    """Render the explore page."""
    
    section_header(
        "🔍 Explore Data",
        "Filter and visualize your data interactively"
    )
    
    # Load raw data
    df = load_sample_data()
    
    # --- Sidebar Filters ---
    with st.sidebar:
        st.subheader("🎛️ Filters")
        
        category = sidebar_select(
            "Category",
            ["All"] + CATEGORIES,
            key="explore_category"
        )
        
        region = sidebar_select(
            "Region",
            ["All"] + REGIONS,
            key="explore_region"
        )
        
        date_range = st.date_input(
            "Date Range",
            value=(df["date"].min(), df["date"].max()),
            key="explore_date_range"
        )
    
    # Apply filters
    filtered = filter_data(
        df,
        category=category if category != "All" else None,
        region=region if region != "All" else None,
        date_range=date_range if len(date_range) == 2 else None
    )
    
    # Summary metrics
    stats = compute_summary_stats(filtered)
    
    metric_row({
        "Rows": f"{len(filtered):,}",
        "Revenue": f"${stats['total_revenue']:,.0f}",
        "Units": f"{stats['total_units']:,}",
        "Products": f"{stats['unique_products']}",
    })
    
    # Visualizations
    section_header("📈 Visualizations")
    
    tab1, tab2, tab3 = st.tabs(["Category Breakdown", "Monthly Trend", "Raw Data"])
    
    with tab1:
        category_data = compute_category_breakdown(filtered)
        st.bar_chart(category_data["revenue"])
    
    with tab2:
        monthly_data = compute_monthly_trend(filtered)
        st.line_chart(monthly_data.set_index("month")["revenue"])
    
    with tab3:
        data_preview(filtered, max_rows=20)


# For multipage navigation
if __name__ == "__main__":
    render()
