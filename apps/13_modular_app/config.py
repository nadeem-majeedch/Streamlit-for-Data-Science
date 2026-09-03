"""
Configuration Module
====================

Centralize all app settings and constants.
Single source of truth for configuration.
"""

# App Settings
APP_TITLE = "Data Explorer App"
APP_ICON = "📊"
APP_DESCRIPTION = "A modular Streamlit application demonstrating best practices"

# Data Settings
MAX_ROWS = 10000
DEFAULT_SAMPLE_SIZE = 1000
SUPPORTED_FORMATS = ["csv", "json", "xlsx"]

# Cache Settings
CACHE_TTL = 3600  # 1 hour in seconds
MAX_CACHE_ENTRIES = 100
SHOW_CACHE_SPINNER = True

# UI Settings
DEFAULT_THEME = "light"
CHART_HEIGHT = 400
TABLE_HEIGHT = 300
METRICS_COLUMNS = 4

# Data Paths
import os
DATA_DIR = os.path.join(os.path.dirname(__file__), "sample_data")
RAW_DATA_DIR = os.path.join(DATA_DIR, "raw")
PROCESSED_DATA_DIR = os.path.join(DATA_DIR, "processed")

# Chart Colors
COLORS = {
    "primary": "#FF4B4B",
    "secondary": "#1F77B4",
    "success": "#28A745",
    "warning": "#FFC107",
    "danger": "#DC3545",
}

# Categories for sample data
CATEGORIES = ["Electronics", "Clothing", "Food", "Books", "Sports"]
REGIONS = ["North", "South", "East", "West", "Central"]
