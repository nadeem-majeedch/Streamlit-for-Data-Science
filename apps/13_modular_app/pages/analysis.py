"""
Analysis Page
=============

Statistical analysis and deeper insights.
"""

import streamlit as st
import pandas as pd
from components import section_header, metric_row, info_box
from data_loader import (
    load_sample_data, filter_data, compute_summary_stats,
    compute_category_breakdown, compute_top_products
)


def render():
    """Render the analysis page."""
    
    section_header(
        "📈 Statistical Analysis",
        "Deep dive into your data patterns"
    )
    
    # Load and filter data
    df = load_sample_data()
    
    # Simple filter for analysis
    st.subheader("Select Data Subset")
    col1, col2 = st.columns(2)
    
    with col1:
        category = st.selectbox("Category", ["All"] + df["category"].unique().tolist())
    
    with col2:
        region = st.selectbox("Region", ["All"] + df["region"].unique().tolist())
    
    filtered = filter_data(
        df,
        category=category if category != "All" else None,
        region=region if region != "All" else None
    )
    
    # Statistics
    section_header("📊 Descriptive Statistics")
    
    if not filtered.empty:
        stats = filtered.describe()
        st.dataframe(stats, use_container_width=True)
    else:
        st.warning("No data matches your filters.")
    
    # Top Products
    section_header("🏆 Top Products by Revenue")
    
    top_products = compute_top_products(filtered, n=10)
    st.dataframe(top_products, use_container_width=True)
    
    # Correlation
    section_header("🔗 Correlations")
    
    numeric_cols = ["quantity", "unit_price", "revenue"]
    if all(col in filtered.columns for col in numeric_cols):
        corr = filtered[numeric_cols].corr()
        st.dataframe(corr, use_container_width=True)
        
        st.info("""
        **Interpretation:**
        - Revenue is calculated from quantity × unit_price
        - Look for unexpected correlations in your actual data
        """)
    
    # Insights
    section_header("💡 Key Insights")
    
    if not filtered.empty:
        col1, col2 = st.columns(2)
        
        with col1:
            avg_revenue = filtered["revenue"].mean()
            st.metric("Average Revenue per Transaction", f"${avg_revenue:,.2f}")
        
        with col2:
            total_products = filtered["product"].nunique()
            st.metric("Unique Products", total_products)
        
        info_box(
            "Analysis Summary",
            f"""
            **Data analyzed:** {len(filtered):,} transactions
            
            **Date range:** {filtered['date'].min().strftime('%Y-%m-%d')} to {filtered['date'].max().strftime('%Y-%m-%d')}
            
            **Categories:** {', '.join(filtered['category'].unique())}
            
            **Regions:** {', '.join(filtered['region'].unique())}
            """,
            type="success"
        )


# For multipage navigation
if __name__ == "__main__":
    render()
