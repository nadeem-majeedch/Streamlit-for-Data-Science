"""
Home Page
=========

Main dashboard with key metrics and overview.
"""

import streamlit as st
from components import metric_row, section_header, data_preview, info_box
from data_loader import load_sample_data, compute_summary_stats


def render():
    """Render the home page."""
    
    section_header(
        "Welcome to Data Explorer",
        "Your interactive data analysis dashboard"
    )
    
    # Load data
    df = load_sample_data()
    stats = compute_summary_stats(df)
    
    # Key metrics
    section_header("📊 Key Metrics", divider=False)
    
    metric_row({
        "Total Revenue": f"${stats['total_revenue']:,.0f}",
        "Units Sold": f"{stats['total_units']:,}",
        "Avg Order": f"${stats['avg_order_value']:,.2f}",
        "Products": f"{stats['unique_products']}",
    })
    
    # Data overview
    section_header("📋 Data Overview")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        data_preview(df, max_rows=10)
    
    with col2:
        info_box(
            "About This Data",
            f"""
            **Date Range:** {stats['date_range']}
            
            **Categories:** Electronics, Clothing, Food, Books, Sports
            
            **Regions:** North, South, East, West, Central
            
            Use the **Explore** page to filter and analyze this data.
            """,
            type="info"
        )
    
    # Quick insights
    section_header("💡 Quick Insights")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.info("**Top Category**\n\nElectronics leads with highest revenue")
    
    with col2:
        st.info("**Top Region**\n\nNorth region shows strongest performance")
    
    with col3:
        st.info("**Trend**\n\nSteady growth throughout the year")


# For multipage navigation
if __name__ == "__main__":
    render()
