"""
Data Loading Module
===================

Handles all data loading and processing.
Separated from UI for testability.
"""

import streamlit as st
import pandas as pd
import numpy as np
from config import CACHE_TTL, CATEGORIES, REGIONS


@st.cache_data(ttl=CACHE_TTL, show_spinner="Loading data...")
def load_sample_data(n_rows=1000, seed=42):
    """
    Generate sample sales data.
    
    Args:
        n_rows: Number of rows to generate
        seed: Random seed for reproducibility
        
    Returns:
        DataFrame with columns: date, category, region, product, 
                                quantity, unit_price, revenue, units_sold
    """
    np.random.seed(seed)
    
    # Generate dates
    dates = pd.date_range("2024-01-01", periods=min(n_rows, 365), freq="D")
    
    # Generate data
    data = pd.DataFrame({
        "date": np.random.choice(dates, n_rows),
        "category": np.random.choice(CATEGORIES, n_rows),
        "region": np.random.choice(REGIONS, n_rows),
        "product": [f"Product_{i}" for i in np.random.randint(1, 50, n_rows)],
        "quantity": np.random.randint(1, 100, n_rows),
        "unit_price": np.round(np.random.uniform(10, 500, n_rows), 2),
    })
    
    # Calculate derived columns
    data["revenue"] = data["quantity"] * data["unit_price"]
    data["units_sold"] = data["quantity"]
    
    # Sort by date
    data = data.sort_values("date").reset_index(drop=True)
    
    return data


@st.cache_data
def filter_data(df, category=None, region=None, date_range=None):
    """
    Filter DataFrame based on criteria.
    
    Args:
        df: Input DataFrame
        category: Category filter (None = all)
        region: Region filter (None = all)
        date_range: Tuple of (start_date, end_date)
        
    Returns:
        Filtered DataFrame
    """
    filtered = df.copy()
    
    if category and category != "All":
        filtered = filtered[filtered["category"] == category]
    
    if region and region != "All":
        filtered = filtered[filtered["region"] == region]
    
    if date_range:
        start, end = date_range
        filtered = filtered[
            (filtered["date"] >= pd.Timestamp(start)) & 
            (filtered["date"] <= pd.Timestamp(end))
        ]
    
    return filtered


@st.cache_data
def compute_summary_stats(df):
    """
    Compute summary statistics.
    
    Args:
        df: Input DataFrame
        
    Returns:
        Dictionary of summary statistics
    """
    if df.empty:
        return {
            "total_revenue": 0,
            "total_units": 0,
            "avg_order_value": 0,
            "unique_products": 0,
            "unique_customers": 0,
            "date_range": "No data",
        }
    
    return {
        "total_revenue": df["revenue"].sum(),
        "total_units": df["units_sold"].sum(),
        "avg_order_value": df["revenue"].mean(),
        "unique_products": df["product"].nunique(),
        "unique_regions": df["region"].nunique(),
        "date_range": f"{df['date'].min().strftime('%Y-%m-%d')} to {df['date'].max().strftime('%Y-%m-%d')}",
    }


@st.cache_data
def compute_category_breakdown(df):
    """
    Compute breakdown by category.
    
    Args:
        df: Input DataFrame
        
    Returns:
        DataFrame with category breakdown
    """
    return df.groupby("category").agg({
        "revenue": "sum",
        "units_sold": "sum",
        "product": "nunique"
    }).rename(columns={"product": "unique_products"}).sort_values("revenue", ascending=False)


@st.cache_data
def compute_region_breakdown(df):
    """
    Compute breakdown by region.
    
    Args:
        df: Input DataFrame
        
    Returns:
        DataFrame with region breakdown
    """
    return df.groupby("region").agg({
        "revenue": "sum",
        "units_sold": "sum"
    }).sort_values("revenue", ascending=False)


@st.cache_data
def compute_monthly_trend(df):
    """
    Compute monthly revenue trend.
    
    Args:
        df: Input DataFrame
        
    Returns:
        DataFrame with monthly aggregation
    """
    df_copy = df.copy()
    df_copy["month"] = df_copy["date"].dt.to_period("M")
    
    return df_copy.groupby("month").agg({
        "revenue": "sum",
        "units_sold": "sum"
    }).reset_index()


@st.cache_data
def compute_top_products(df, n=10):
    """
    Get top N products by revenue.
    
    Args:
        df: Input DataFrame
        n: Number of top products
        
    Returns:
        DataFrame with top products
    """
    return df.groupby("product").agg({
        "revenue": "sum",
        "quantity": "sum"
    }).sort_values("revenue", ascending=False).head(n)


@st.cache_data
def compute_growth_rate(current_value, previous_value):
    """
    Calculate percentage growth rate.
    
    Args:
        current_value: Current period value
        previous_value: Previous period value
        
    Returns:
        Growth rate as percentage
    """
    if previous_value == 0:
        return 0
    return ((current_value - previous_value) / previous_value) * 100
