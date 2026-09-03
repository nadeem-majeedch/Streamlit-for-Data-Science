"""
🖥️ Demo App 07 — Data Display & Visualization Dashboard
=========================================================
A complete dashboard demonstrating DataFrame display, column_config,
filtering, Matplotlib, Plotly, and interactive visualization.

Run this app:
    streamlit run apps/07_data_display_demo.py

Related Materials:
- 📖 Reading: ../readings/07_data_display_dataframes.md
- 📖 Reading: ../readings/08_visualization_matplotlib_plotly.md
- 📓 Notebook: ../notebooks/07_dataframes_tables_pandas.ipynb
- 📓 Notebook: ../notebooks/08_interactive_visualization.ipynb
- ✏️ Exercise: ../exercises/07_data_display_challenges.py
- ✏️ Exercise: ../exercises/08_visualization_workshop.py
"""

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

# ---------------------------------------------------------------------------
# Page Config
# ---------------------------------------------------------------------------
st.set_page_config(
    page_title="07 — Data Display & Visualization",
    page_icon="📊",
    layout="wide",
)

# ---------------------------------------------------------------------------
# Data Generation (cached)
# ---------------------------------------------------------------------------
@st.cache_data
def generate_data(n=365):
    np.random.seed(42)
    products = ["Laptop", "Phone", "Tablet", "Monitor", "Keyboard"]
    regions = ["North", "South", "East", "West"]
    categories = ["Electronics", "Accessories", "Peripherals"]

    dates = pd.date_range("2026-01-01", periods=n, freq="D")
    df = pd.DataFrame({
        "Date": dates,
        "Product": np.random.choice(products, n),
        "Region": np.random.choice(regions, n),
        "Category": np.random.choice(categories, n),
        "Revenue": np.random.randint(5000, 50000, n).astype(float),
        "Units": np.random.randint(5, 200, n),
        "Marketing": np.random.randint(500, 10000, n).astype(float),
        "Rating": np.random.uniform(1.0, 5.0, n).round(1),
        "Return Rate": np.random.uniform(0, 0.15, n).round(3),
    })
    return df


df = generate_data()

# ---------------------------------------------------------------------------
# Sidebar Controls
# ---------------------------------------------------------------------------
with st.sidebar:
    st.header("🔍 Filters")

    selected_products = st.multiselect(
        "Products",
        options=df["Product"].unique().tolist(),
        default=df["Product"].unique().tolist(),
    )

    selected_regions = st.multiselect(
        "Regions",
        options=df["Region"].unique().tolist(),
        default=df["Region"].unique().tolist(),
    )

    min_rating = st.slider("Minimum Rating", 1.0, 5.0, 1.0, 0.1)

    date_range = st.date_input(
        "Date Range",
        value=(df["Date"].min(), df["Date"].max()),
    )

    st.divider()
    st.header("⚙️ Display")
    chart_lib = st.radio("Chart Library", ["Plotly", "Matplotlib", "Native"], horizontal=True)

# ---------------------------------------------------------------------------
# Apply Filters
# ---------------------------------------------------------------------------
filtered = df.copy()
filtered = filtered[filtered["Product"].isin(selected_products)]
filtered = filtered[filtered["Region"].isin(selected_regions)]
filtered = filtered[filtered["Rating"] >= min_rating]

if isinstance(date_range, tuple) and len(date_range) == 2:
    filtered = filtered[
        (filtered["Date"] >= pd.Timestamp(date_range[0]))
        & (filtered["Date"] <= pd.Timestamp(date_range[1]))
    ]

# ---------------------------------------------------------------------------
# Title
# ---------------------------------------------------------------------------
st.title("📊 Data Display & Visualization Dashboard")
st.caption(f"Showing **{len(filtered)}** of **{len(df)}** records")

st.divider()

# ---------------------------------------------------------------------------
# KPI Row
# ---------------------------------------------------------------------------
total_rev = filtered["Revenue"].sum()
total_units = filtered["Units"].sum()
avg_rating = filtered["Rating"].mean() if len(filtered) > 0 else 0
avg_return = filtered["Return Rate"].mean() * 100 if len(filtered) > 0 else 0

c1, c2, c3, c4 = st.columns(4)
c1.metric("Total Revenue", f"${total_rev:,.0f}", icon="💰")
c2.metric("Total Units", f"{total_units:,}", icon="📦")
c3.metric("Avg Rating", f"{avg_rating:.1f} ⭐", icon="⭐")
c4.metric("Avg Return Rate", f"{avg_return:.1f}%", icon="🔄")

st.divider()

# ---------------------------------------------------------------------------
# Tab Layout
# ---------------------------------------------------------------------------
tab_table, tab_charts, tab_matplotlib, tab_analysis = st.tabs(
    ["📋 Data Table", "📈 Charts", "🎨 Matplotlib", "📊 Analysis"]
)

# --- Tab 1: Formatted DataFrame ---
with tab_table:
    st.subheader("Interactive Data Table")

    st.dataframe(
        filtered,
        hide_index=True,
        column_config={
            "Date": st.column_config.DateColumn("Date", format="MMM D, YYYY"),
            "Revenue": st.column_config.NumberColumn("Revenue", format="$ %d"),
            "Units": st.column_config.NumberColumn("Units", format="%d"),
            "Marketing": st.column_config.NumberColumn("Marketing ($)", format="$ %d"),
            "Rating": st.column_config.NumberColumn("Rating", format="%.1f ⭐"),
            "Return Rate": st.column_config.NumberColumn("Return Rate", format="%.1f%%"),
        },
        column_order=["Date", "Product", "Region", "Category", "Revenue", "Units",
                       "Marketing", "Rating", "Return Rate"],
        height=400,
    )

    # Conditional formatting with Styler
    with st.expander("🎨 Conditional Formatting"):
        def color_revenue(val):
            if val >= 35000:
                return "background-color: #c6efce; color: #006100"
            elif val >= 20000:
                return "background-color: #ffeb9c; color: #9c6500"
            else:
                return "background-color: #ffc7ce; color: #9c0006"

        def color_rating(val):
            if val >= 4.0:
                return "background-color: #c6efce"
            elif val >= 3.0:
                return "background-color: #ffeb9c"
            else:
                return "background-color: #ffc7ce"

        sample = filtered.head(30).copy()
        styled = sample.style.applymap(color_revenue, subset=["Revenue"])
        styled = styled.applymap(color_rating, subset=["Rating"])
        styled = styled.format({
            "Revenue": "${:,.0f}",
            "Rating": "{:.1f}",
            "Return Rate": "{:.1%}",
        })
        st.dataframe(styled, height=400)

    # Export
    with st.expander("📥 Export Data"):
        csv = filtered.to_csv(index=False)
        st.download_button("Download CSV", csv, "filtered_data.csv", type="primary")

# --- Tab 2: Charts ---
with tab_charts:
    st.subheader(f"Visualizations ({chart_lib})")

    chart_col1, chart_col2 = st.columns(2)

    with chart_col1:
        st.markdown("**Revenue Trend**")
        monthly = filtered.set_index("Date").resample("M")["Revenue"].sum()

        if chart_lib == "Plotly":
            fig = px.line(x=monthly.index, y=monthly.values, title="Monthly Revenue")
            fig.update_layout(xaxis_title="Month", yaxis_title="Revenue ($)")
            st.plotly_chart(fig, use_container_width=True)
        elif chart_lib == "Matplotlib":
            fig, ax = plt.subplots(figsize=(8, 4))
            ax.plot(monthly.index, monthly.values, color="#4ecdc4", linewidth=2)
            ax.set_title("Monthly Revenue")
            ax.set_xlabel("Month")
            ax.set_ylabel("Revenue ($)")
            ax.grid(True, alpha=0.3)
            plt.tight_layout()
            st.pyplot(fig)
        else:
            st.line_chart(monthly)

    with chart_col2:
        st.markdown("**Revenue by Product**")
        product_rev = filtered.groupby("Product")["Revenue"].sum().sort_values(ascending=False)

        if chart_lib == "Plotly":
            fig = px.bar(x=product_rev.index, y=product_rev.values,
                         color=product_rev.index, title="Revenue by Product")
            fig.update_layout(xaxis_title="Product", yaxis_title="Revenue ($)", showlegend=False)
            st.plotly_chart(fig, use_container_width=True)
        elif chart_lib == "Matplotlib":
            fig, ax = plt.subplots(figsize=(8, 4))
            colors = ["#4ecdc4", "#ff6b6b", "#45b7d1", "#96ceb4", "#ffeaa7"]
            ax.bar(product_rev.index, product_rev.values, color=colors)
            ax.set_title("Revenue by Product")
            ax.set_ylabel("Revenue ($)")
            plt.xticks(rotation=30)
            plt.tight_layout()
            st.pyplot(fig)
        else:
            st.bar_chart(product_rev)

    # Full-width charts
    chart_col3, chart_col4 = st.columns(2)

    with chart_col3:
        st.markdown("**Revenue Distribution**")
        if chart_lib == "Plotly":
            fig = px.histogram(filtered, x="Revenue", nbins=30, title="Revenue Distribution",
                               marginal="box")
            st.plotly_chart(fig, use_container_width=True)
        elif chart_lib == "Matplotlib":
            fig, ax = plt.subplots(figsize=(8, 4))
            ax.hist(filtered["Revenue"], bins=30, edgecolor="black", alpha=0.7, color="#4ecdc4")
            ax.axvline(filtered["Revenue"].mean(), color="red", linestyle="--",
                       label=f"Mean: ${filtered['Revenue'].mean():,.0f}")
            ax.set_title("Revenue Distribution")
            ax.legend()
            plt.tight_layout()
            st.pyplot(fig)
        else:
            st.area_chart(filtered.set_index("Date")[["Revenue"]])

    with chart_col4:
        st.markdown("**Marketing vs Revenue**")
        if chart_lib == "Plotly":
            fig = px.scatter(filtered, x="Marketing", y="Revenue", color="Region",
                             trendline="ols", title="Marketing vs Revenue")
            st.plotly_chart(fig, use_container_width=True)
        elif chart_lib == "Matplotlib":
            fig, ax = plt.subplots(figsize=(8, 4))
            for region in filtered["Region"].unique():
                subset = filtered[filtered["Region"] == region]
                ax.scatter(subset["Marketing"], subset["Revenue"], label=region, alpha=0.6)
            ax.set_title("Marketing vs Revenue")
            ax.set_xlabel("Marketing Spend ($)")
            ax.set_ylabel("Revenue ($)")
            ax.legend()
            plt.tight_layout()
            st.pyplot(fig)
        else:
            st.scatter_chart(filtered[["Marketing", "Revenue"]])

# --- Tab 3: Matplotlib Deep Dive ---
with tab_matplotlib:
    st.subheader("Matplotlib Subplot Panel")

    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    # Top-left: Revenue histogram
    axes[0, 0].hist(filtered["Revenue"], bins=30, edgecolor="black", alpha=0.7, color="#4ecdc4")
    axes[0, 0].axvline(filtered["Revenue"].mean(), color="red", linestyle="--",
                       label=f"Mean: ${filtered['Revenue'].mean():,.0f}")
    axes[0, 0].set_title("Revenue Distribution", fontweight="bold")
    axes[0, 0].set_xlabel("Revenue ($)")
    axes[0, 0].legend()

    # Top-right: Revenue by Region
    region_rev = filtered.groupby("Region")["Revenue"].sum()
    axes[0, 1].bar(region_rev.index, region_rev.values,
                    color=["#4ecdc4", "#ff6b6b", "#45b7d1", "#96ceb4"])
    axes[0, 1].set_title("Revenue by Region", fontweight="bold")
    axes[0, 1].set_ylabel("Revenue ($)")

    # Bottom-left: Rating distribution
    axes[1, 0].hist(filtered["Rating"], bins=20, edgecolor="black", alpha=0.7, color="#ff6b6b")
    axes[1, 0].set_title("Rating Distribution", fontweight="bold")
    axes[1, 0].set_xlabel("Rating")

    # Bottom-right: Units by Product
    product_units = filtered.groupby("Product")["Units"].sum().sort_values(ascending=True)
    axes[1, 1].barh(product_units.index, product_units.values, color="#4ecdc4")
    axes[1, 1].set_title("Units Sold by Product", fontweight="bold")
    axes[1, 1].set_xlabel("Units Sold")

    plt.tight_layout()
    st.pyplot(fig)

    # Correlation heatmap
    st.subheader("Correlation Matrix")
    fig2, ax2 = plt.subplots(figsize=(8, 6))
    numeric_cols = filtered[["Revenue", "Units", "Marketing", "Rating"]].corr()
    try:
        import seaborn as sns
        sns.heatmap(numeric_cols, annot=True, cmap="coolwarm", center=0, ax=ax2,
                    fmt=".2f", square=True, linewidths=0.5)
    except ImportError:
        cax = ax2.matshow(numeric_cols, cmap="coolwarm")
        ax2.set_xticks(range(len(numeric_cols.columns)))
        ax2.set_yticks(range(len(numeric_cols.columns)))
        ax2.set_xticklabels(numeric_cols.columns, rotation=45)
        ax2.set_yticklabels(numeric_cols.columns)
        fig2.colorbar(cax)
    ax2.set_title("Correlation Matrix", fontweight="bold", pad=20)
    plt.tight_layout()
    st.pyplot(fig2)

# --- Tab 4: Analysis ---
with tab_analysis:
    st.subheader("Deep Analysis")

    analysis_col1, analysis_col2 = st.columns(2)

    with analysis_col1:
        st.markdown("**Revenue by Region × Product**")
        pivot = filtered.pivot_table(
            values="Revenue", index="Region", columns="Product",
            aggfunc="sum", fill_value=0
        )
        st.dataframe(
            pivot,
            column_config={col: st.column_config.NumberColumn(format="$ %d")
                           for col in pivot.columns},
        )

    with analysis_col2:
        st.markdown("**Top 10 Transactions**")
        top10 = filtered.nlargest(10, "Revenue")[
            ["Date", "Product", "Region", "Revenue", "Units", "Rating"]
        ]
        st.dataframe(
            top10,
            hide_index=True,
            column_config={
                "Date": st.column_config.DateColumn("Date", format="MMM D"),
                "Revenue": st.column_config.NumberColumn("Revenue", format="$ %d"),
                "Rating": st.column_config.NumberColumn("Rating", format="%.1f"),
            },
        )

    # Sunburst
    st.markdown("**Revenue Hierarchy**")
    fig = px.sunburst(filtered, path=["Region", "Product"], values="Revenue",
                      title="Revenue: Region → Product")
    st.plotly_chart(fig, use_container_width=True)

# ---------------------------------------------------------------------------
# Footer
# ---------------------------------------------------------------------------
st.divider()
st.caption(
    "Data Display & Visualization Dashboard · Module 04 · "
    "Streamlit for Data Science · "
    "[Streamlit Docs](https://docs.streamlit.io/develop/api-reference)"
)
