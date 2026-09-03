# P09 — Interactive Visualization Dashboard

> **🚀 Project · Intermediate · M04–M06**
> *Build a chart-heavy dashboard with multiple interactive visualization types.*
> Difficulty: ★★★☆☆ · Duration: 1.5 weeks · Weight: Part of 15% project grade

---

## Problem Statement

A marketing team needs a dashboard to visualize campaign performance across channels, regions, and time periods. Build a visualization-focused dashboard that lets them explore data through multiple chart types with interactive controls.

---

## Learning Objectives

1. Integrate multiple chart libraries (Matplotlib, Plotly) (CLO3)
2. Build dynamic chart selection with sidebar controls (CLO2)
3. Create comparative visualizations with side-by-side layouts (CLO3)
4. Implement chart customization (titles, labels, colors) (CLO3)
5. Design a cohesive visual theme (CLO6)

---

## Prerequisites

- Completed Modules 04–M06
- Plotly Express basics
- Matplotlib basics
- `st.plotly_chart()` and `st.pyplot()`

---

## Functional Requirements

| # | Requirement | Marks |
|---|-------------|-------|
| F1 | Generate or load marketing campaign data (date, channel, region, impressions, clicks, conversions, spend) | 5 |
| F2 | Sidebar: chart type selector (Bar/Line/Scatter/Heatmap), X-axis, Y-axis, Color encoding | 10 |
| F3 | Main chart: Plotly chart that updates based on sidebar selections | 10 |
| F4 | Side-by-side comparison: two charts in columns (e.g., impressions vs conversions) | 8 |
| F5 | Tabbed view: "Trends", "Channels", "Regions", "Performance" | 10 |
| F6 | Matplotlib subplot: 2×2 grid with different chart types | 8 |
| F7 | Chart annotation: add insights/captions to charts | 4 |
| F8 | Download chart as image (Plotly `write_image` or screenshot) | 5 |

**Total: 60 marks**

---

## Architecture

```
viz_dashboard/
├── app.py
├── chart_functions.py  # Chart creation functions
├── data_generator.py   # Sample data
├── requirements.txt
└── README.md
```

---

## Evaluation Criteria

| Criteria | Marks |
|----------|-------|
| Chart variety and quality | 25 |
| Interactivity (sidebar controls, updates) | 15 |
| Layout and visual design | 10 |
| Code quality | 5 |
| Documentation | 5 |
| **Total** | **60** |

---

## Extensions

- Add real-time data simulation with `st.fragment(run_every=...)`
- Add geographic map visualization
- Add chart animations with Plotly
- Add user annotations/bookmarks

---

## Related Materials

- 📖 Reading: [Visualization](../readings/08_visualization_matplotlib_plotly.md)
- 📓 Notebook: [08 — Visualization](../notebooks/08_interactive_visualization.ipynb)
- 📖 Reading: [Dashboard Design](../readings/06_dashboard_design_ui_ux.md)
- ✏️ Exercise: [10 — Dashboard](../exercises/10_dashboard_workshop.py)
