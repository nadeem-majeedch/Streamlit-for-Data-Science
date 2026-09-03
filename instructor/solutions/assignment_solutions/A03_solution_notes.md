# A03 — Multipage Application: Solution Notes

> **👩‍🏫 Instructor Reference**
> *Architecture, key implementation, grading breakdown, and common errors.*

---

## Expected Architecture

```
assignments/A03/
├── app.py              # Entry point with st.navigation
├── config.py           # Constants (DB path, app name)
├── data_access.py      # All database CRUD operations
├── components.py       # Reusable UI components
├── pages/
│   ├── __init__.py
│   ├── home.py         # Dashboard overview
│   ├── data_entry.py   # Add/edit/delete experiments
│   ├── analysis.py     # Charts and statistics
│   └── reports.py      # Export and reports
├── requirements.txt
├── README.md
└── screenshots/
```

---

## Key Implementation Patterns

### app.py (Entry Point)
```python
import streamlit as st
from pages import home, data_entry, analysis, reports

st.set_page_config(page_title="Research Data Manager", layout="wide")

# Shared sidebar
st.sidebar.header("Research Data Manager")
page = st.sidebar.radio("Navigate", ["Home", "Data Entry", "Analysis", "Reports"])

if page == "Home":
    home.render()
elif page == "Data Entry":
    data_entry.render()
elif page == "Analysis":
    analysis.render()
else:
    reports.render()
```

### config.py
```python
DATABASE_PATH = "research_data.db"
APP_TITLE = "Research Data Manager"
APP_ICON = "🔬"
```

### data_access.py
```python
import sqlite3
import streamlit as st

@st.cache_resource
def get_connection():
    conn = sqlite3.connect("research_data.db", check_same_thread=False)
    conn.execute("PRAGMA journal_mode=WAL")
    return conn

def init_db():
    conn = get_connection()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS experiments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            date TEXT NOT NULL,
            method TEXT NOT NULL,
            description TEXT,
            result_notes TEXT,
            rating INTEGER CHECK(rating >= 1 AND rating <= 5),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()

def insert_experiment(title, date, method, description, result_notes, rating):
    conn = get_connection()
    conn.execute(
        "INSERT INTO experiments (title, date, method, description, result_notes, rating) VALUES (?, ?, ?, ?, ?, ?)",
        (title, str(date), method, description, result_notes, rating)
    )
    conn.commit()
    get_connection.clear()

def get_all_experiments():
    import pandas as pd
    conn = get_connection()
    return pd.read_sql("SELECT * FROM experiments ORDER BY date DESC", conn)

def delete_experiment(exp_id):
    conn = get_connection()
    conn.execute("DELETE FROM experiments WHERE id = ?", (exp_id,))
    conn.commit()
    get_connection.clear()
```

### components.py
```python
import streamlit as st

def metric_card(label, value, delta=None, icon=None):
    st.metric(label=label, value=value, delta=delta, icon=icon)

def data_preview(df, max_rows=5):
    if df.empty:
        st.info("No data available")
    else:
        st.dataframe(df.head(max_rows), use_container_width=True, hide_index=True)

def section_header(title, description=None):
    st.header(title)
    if description:
        st.caption(description)
```

---

## Grading Breakdown by Task

### Task 1: Architecture (20 marks)
| Criteria | Points |
|----------|--------|
| Separate app.py with navigation | 3 |
| config.py with constants | 3 |
| data_access.py with all DB operations | 4 |
| components.py with reusable UI | 3 |
| Pages in pages/ directory | 3 |
| No DB queries in page files | 2 |
| No duplicate code | 2 |

### Task 2: Database (20 marks)
| Criteria | Points |
|----------|--------|
| SQLite created on first run | 3 |
| @st.cache_resource for connection | 3 |
| Table with required columns | 3 |
| INSERT operation | 3 |
| UPDATE operation | 2 |
| DELETE with confirmation | 2 |
| SELECT with filters | 2 |
| Parameterized queries (no f-strings) | 2 |

### Task 3: Navigation (15 marks)
| Criteria | Points |
|----------|--------|
| st.navigation() with groups | 3 |
| Clear page titles | 2 |
| Shared sidebar controls | 3 |
| Session state for cross-page data | 3 |
| Smooth transitions | 2 |
| Active page indicated | 2 |

---

## Common Class-Wide Issues

1. **SQL injection with f-strings** — Most critical security issue
   ```python
   # WRONG (deduct 2 marks)
   conn.execute(f"SELECT * FROM experiments WHERE method = '{method}'")
   
   # RIGHT
   conn.execute("SELECT * FROM experiments WHERE method = ?", (method,))
   ```

2. **All code in one file** — If no separate modules, deduct 10+ marks from Architecture

3. **No cache invalidation after writes** — Data doesn't update after add/delete
   ```python
   # Must clear cache after any write
   get_connection.clear()
   ```

4. **Missing error handling** — App crashes on empty database or invalid input

5. **No delete confirmation** — Dangerous without confirmation dialog

---

## Grading Strategy

1. Check file structure first — are files properly separated?
2. Run the app — does it start and navigate?
3. Test CRUD: Add → View → Edit → Delete
4. Check SQL queries — all parameterized?
5. Check for cache invalidation after writes
6. Test edge cases: empty database, invalid input

**Estimated grading time:** 15-20 minutes per student/pair
