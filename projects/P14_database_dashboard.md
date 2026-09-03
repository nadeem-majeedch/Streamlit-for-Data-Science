# P14 — Database-Powered Data Science Dashboard

> **🚀 Project · Advanced · M08–M10**
> *Build a multipage dashboard backed by a SQLite database with full CRUD operations.*
> Difficulty: ★★★★☆ · Duration: 2 weeks · Weight: Part of 15% project grade

---

## Problem Statement

A research lab needs a dashboard to manage experimental data. Scientists should be able to add, view, edit, and delete experiment records, visualize trends, and generate reports — all backed by a persistent database.

---

## Learning Objectives

1. Design and implement a database schema (CLO7)
2. Build CRUD operations with parameterized SQL (CLO7)
3. Create a multipage application with `st.navigation()` (CLO6)
4. Implement caching with proper invalidation (CLO5)
5. Separate database logic from UI (CLO6)

---

## Prerequisites

- Completed Modules 08–10
- SQLite basics (CREATE TABLE, INSERT, SELECT, UPDATE, DELETE)
- `@st.cache_resource` for connection caching
- `st.navigation()` and `st.Page` for multipage

---

## Functional Requirements

| # | Requirement | Marks |
|---|-------------|-------|
| F1 | SQLite database with experiments table (id, title, date, method, result, rating) | 6 |
| F2 | "Home" page: dashboard with KPIs (total experiments, avg rating, methods used) | 8 |
| F3 | "Data Entry" page: form to add new experiments | 8 |
| F4 | "Data Entry" page: edit and delete existing experiments | 8 |
| F5 | "Analysis" page: filter by method, date range, rating; show charts | 10 |
| F6 | "Reports" page: export filtered data as CSV, summary statistics | 6 |
| F7 | Multipage navigation with `st.navigation()` | 6 |
| F8 | Parameterized SQL queries (no f-strings) | 6 |
| F9 | Cache invalidation after writes | 5 |
| F10 | Error handling for database operations | 5 |

**Total: 68 marks**

---

## Architecture

```
research_dashboard/
├── app.py              # Entry point with navigation
├── config.py           # Database path, app settings
├── database.py         # All CRUD operations
├── components.py       # Reusable UI components
├── pages/
│   ├── __init__.py
│   ├── home.py
│   ├── entry.py
│   ├── analysis.py
│   └── reports.py
├── requirements.txt
└── README.md
```

---

## Evaluation Criteria

| Criteria | Marks |
|----------|-------|
| Database design and CRUD | 25 |
| Multipage architecture | 15 |
| Analysis and visualization | 15 |
| Security (parameterized SQL) | 8 |
| Code quality | 5 |
| **Total** | **68** |

---

## Extensions

- Add user authentication (simple password)
- Add data import from CSV
- Add experiment comparison view
- Add audit trail (log all changes)

---

## Related Materials

- 📖 Reading: [Databases](../readings/14_databases_and_persistence.md)
- 📓 Notebook: [14 — Databases](../notebooks/14_databases_persistence.ipynb)
- ✏️ Exercise: [14 — Database](../exercises/14_database_workshop.py)
- 🖥️ Demo: [14 — Database Dashboard](../apps/14_database_dashboard.py)
