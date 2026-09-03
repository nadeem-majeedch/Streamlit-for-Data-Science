# Assignment 03 — Multipage Data Science Application

> **📋 Assignment · Level 3 (Advanced) — Modules 07–10**
> *Build a production-quality multipage Streamlit application with caching, databases, and proper architecture.*

---

## Course Information

| Field | Detail |
|-------|--------|
| **Course** | Streamlit for Data Science |
| **Assignment** | A03 — Multipage Data Science Application |
| **Due Date** | End of Week 10 |
| **Weight** | 4% of course grade |
| **Difficulty** | ★★★☆☆ Advanced |
| **Collaboration** | Individual or Pair (max 2) |

---

## Learning Outcomes

After completing this assignment you will be able to:

1. **LO1** — Design modular application architecture with separation of concerns (Analyze)
2. **LO2** — Implement multipage navigation with shared state (Apply)
3. **LO3** — Optimize performance with caching strategies (Analyze)
4. **LO4** — Integrate SQLite for persistent data storage (Apply)
5. **LO5** — Implement input validation and error handling (Evaluate)
6. **LO6** — Write clean, maintainable, well-documented code (Evaluate)

---

## Prerequisites

- Completed Modules 07, 08, 09, 10
- Caching with `@st.cache_data` and `@st.cache_resource`
- Multipage apps with `st.navigation` and `st.Page`
- SQLite and parameterized SQL queries
- Session state for cross-page persistence

---

## Overview

Build a **Research Data Manager** — a multipage Streamlit application that
lets researchers manage, analyze, and visualize experimental data. The app
must persist data across sessions using SQLite and provide a clean,
modular architecture.

This assignment is the bridge between intermediate app-building and
production-ready deployment.

---

## Architecture Requirements

Your application MUST have this structure:

```
assignments/A03/
├── app.py                    # Entry point with navigation
├── config.py                 # Configuration constants
├── data_access.py            # Database operations (CRUD)
├── components.py             # Reusable UI components
├── requirements.txt          # Dependencies
├── README.md                 # Documentation
└── pages/
    ├── __init__.py
    ├── home.py               # Dashboard overview
    ├── data_entry.py         # Add/edit/delete experiments
    ├── analysis.py           # Data analysis and visualization
    └── reports.py            # Generate and download reports
```

---

## Tasks

### Task 1: Application Architecture (20 marks)

| Requirement | Marks |
|-------------|-------|
| Clean entry point (`app.py`) with `st.navigation` | 3 |
| Separate `config.py` with constants (DB path, app name, etc.) | 3 |
| Separate `data_access.py` with all database operations | 4 |
| Separate `components.py` with reusable UI functions | 3 |
| Each page is a separate file in `pages/` | 3 |
| No database queries in page files — only via `data_access.py` | 2 |
| No duplicate code across pages | 2 |

### Task 2: Database Integration (20 marks)

| Requirement | Marks |
|-------------|-------|
| SQLite database created on first run | 3 |
| `@st.cache_resource` for database connection with `check_same_thread=False` | 3 |
| Create `experiments` table: id, title, date, method, result_notes, rating | 3 |
| INSERT: add new experiment records | 3 |
| UPDATE: edit existing experiment records | 2 |
| DELETE: remove experiment records with confirmation | 2 |
| SELECT: query with filters (by method, date range, rating) | 2 |
| All queries use parameterized SQL (no f-strings) | 2 |

### Task 3: Multipage Navigation (15 marks)

| Requirement | Marks |
|-------------|-------|
| `st.navigation()` with grouped pages (sidebar sections) | 3 |
| Each page has a clear title and description | 2 |
| Shared sidebar with app-wide controls (theme, filters) | 3 |
| `st.session_state` used to share data between pages | 3 |
| Page transitions are smooth (no flash of empty content) | 2 |
| Active page is visually indicated | 2 |

### Task 4: Caching & Performance (10 marks)

| Requirement | Marks |
|-------------|-------|
| `@st.cache_data` on expensive query/processing functions | 3 |
| Cache invalidation after INSERT/UPDATE/DELETE operations | 3 |
| `@st.cache_resource` for database connection | 2 |
| Data processing functions separated from UI | 2 |

### Task 5: Data Analysis Page (15 marks)

| Requirement | Marks |
|-------------|-------|
| Display all experiments in `st.dataframe()` with sorting | 3 |
| Filter by method (selectbox), date range (date_input), rating (slider) | 3 |
| Show aggregate statistics: count by method, average rating | 3 |
| At least 2 visualizations of the experiment data | 3 |
| Charts update when filters change | 3 |

### Task 6: Input Validation & Error Handling (10 marks)

| Requirement | Marks |
|-------------|-------|
| Form validation: title required, rating 1–5, date not future | 3 |
| Graceful error messages for database failures | 2 |
| Confirmation dialog before deleting records | 2 |
| `st.toast()` or `st.success()` feedback on operations | 2 |
| Handles empty database state gracefully | 1 |

### Task 7: Code Quality & Documentation (10 marks)

| Requirement | Marks |
|-------------|-------|
| Docstrings on all functions | 2 |
| Type hints on function signatures | 2 |
| Consistent naming conventions (snake_case, descriptive) | 2 |
| README with architecture diagram, setup instructions, screenshots | 2 |
| `requirements.txt` present and correct | 2 |

**Total: 100 marks**

---

## Deliverables

1. **Complete application directory** with all files listed in architecture
2. **`README.md`** with architecture diagram, feature list, screenshots
3. **`requirements.txt`** with pinned versions
4. **Screenshot(s)** of each page running

### Submission

```
assignments/A03/
├── app.py
├── config.py
├── data_access.py
├── components.py
├── requirements.txt
├── README.md
├── screenshots/
│   ├── home.png
│   ├── data_entry.png
│   ├── analysis.png
│   └── reports.png
└── pages/
    ├── __init__.py
    ├── home.py
    ├── data_entry.py
    ├── analysis.py
    └── reports.py
```

---

## Database Schema

```sql
CREATE TABLE IF NOT EXISTS experiments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    date TEXT NOT NULL,
    method TEXT NOT NULL,
    description TEXT,
    result_notes TEXT,
    rating INTEGER CHECK(rating >= 1 AND rating <= 5),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

## Grading Rubric Summary

| Category | Marks | Bloom's Level |
|----------|-------|---------------|
| Architecture | 20 | Analyze, Evaluate |
| Database Integration | 20 | Apply |
| Multipage Navigation | 15 | Apply |
| Caching & Performance | 10 | Analyze |
| Data Analysis Page | 15 | Apply, Analyze |
| Input Validation | 10 | Evaluate |
| Code Quality & Docs | 10 | Evaluate |
| **Total** | **100** | |

---

## Common Mistakes to Avoid

1. **❌ SQL injection** — Never use f-strings in SQL queries
2. **❌ All code in one file** — Must have separate modules
3. **❌ No cache invalidation** — Stale data after writes
4. **❌ Hardcoded file paths** — Use relative paths or `config.py`
5. **❌ No error handling** — Database operations can fail

---

## Related Materials

- 📖 Reading: [Caching & Performance](../readings/12_caching_and_performance.md)
- 📖 Reading: [Application Architecture](../readings/13_application_architecture.md)
- 📖 Reading: [Databases & Persistence](../readings/14_databases_and_persistence.md)
- 📓 Notebook: [12 — Caching](../notebooks/12_caching_performance.ipynb)
- 📓 Notebook: [13 — Architecture](../notebooks/13_application_architecture.ipynb)
- 📓 Notebook: [14 — Databases](../notebooks/14_databases_persistence.ipynb)
- ✏️ Exercise: [12 — Caching](../exercises/12_caching_workshop.py)
- ✏️ Exercise: [13 — Architecture](../exercises/13_architecture_workshop.py)
- ✏️ Exercise: [14 — Database](../exercises/14_database_workshop.py)
- 🖥️ Demo: [13 — Modular App](../apps/13_modular_app/app.py)
- 🖥️ Demo: [14 — Database Dashboard](../apps/14_database_dashboard.py)
