# Quiz 10: Databases & Persistence

> **📝 Quiz · Module 10 · Advanced**  
> *Test your understanding of database integration with Streamlit.*

---

## Multiple Choice

### Q1. Why is SQLite preferred for teaching database concepts?

a) It's faster than PostgreSQL  
b) It requires no server setup  
c) It supports more SQL features  
d) It has better security

---

### Q2. Which decorator should you use to cache a database connection?

a) `@st.cache_data`  
b) `@st.cache_resource`  
c) `@st.cache`  
d) `@st.memo`

---

### Q3. Why must you use `check_same_thread=False` with SQLite?

a) To enable caching  
b) To allow multi-threaded access  
c) To improve performance  
d) To enable WAL mode

---

### Q4. What is SQL injection?

a) A way to improve query performance  
b) A technique to insert malicious SQL code through user input  
c) A method to connect to databases  
d) A type of database backup

---

### Q5. Which is the SAFE way to execute a query with user input?

```python
# Option A
query = f"SELECT * FROM users WHERE name = '{user_input}'"
cursor.execute(query)

# Option B
query = "SELECT * FROM users WHERE name = ?"
cursor.execute(query, (user_input,))
```

---

### Q6. What does `conn.commit()` do?

a) Reads data from the database  
b) Saves (persists) changes to the database  
c) Closes the connection  
d) Creates a backup

---

### Q7. Why should you call `.clear()` after database writes?

a) To free memory  
b) To invalidate cached query results  
c) To close the connection  
d) To improve performance

---

### Q8. What is the correct way to store database credentials?

a) Hard-code in the script  
b) Use `st.secrets` or environment variables  
c) Store in a public GitHub repo  
d) Use `st.session_state`

---

### Q9. What does "ACID" stand for in databases?

a) Atomicity, Consistency, Isolation, Durability  
b) Authentication, Connection, Integration, Data  
c) Add, Change, Insert, Delete  
d) Array, Class, Integer, Dictionary

---

### Q10. What is a parameterized query?

a) A query with many parameters  
b) A query that uses placeholders for user input  
c) A query that runs multiple times  
d) A query with complex logic

---

### Q11. When should you use `@st.cache_data` vs `@st.cache_resource` for database operations?

a) `cache_data` for connections, `cache_resource` for queries  
b) `cache_data` for queries, `cache_resource` for connections  
c) Both work the same way  
d) Neither should be used

---

### Q12. What is WAL mode in SQLite?

a) Write-Ahead Logging — improves concurrent access  
b) Web Application Layer — for HTTP connections  
c) Wireless Access Link — for network databases  
d) A backup method

---

## Short Answer

### Q13. Explain the difference between SQLite, PostgreSQL, and MySQL. When would you choose each?

---

### Q14. A developer writes this code and gets a "database is locked" error. Explain why and provide the fix:

```python
conn = sqlite3.connect("data.db")

def add_user(name):
    conn.execute("INSERT INTO users (name) VALUES (?)", (name,))
    conn.commit()
```

---

### Q15. Describe three security best practices for database-connected Streamlit apps.

---

## Code Completion

### Q16. Complete the cached connection function:

```python
import streamlit as st
import sqlite3

# TODO: Add proper caching decorator
def get_connection():
    """Get or create cached database connection."""
    # TODO: Implement connection with proper settings
    pass
```

---

### Q17. Complete the parameterized query:

```python
import sqlite3
import pandas as pd

def search_products(conn, name=None, category=None, min_price=None):
    """
    Search products with optional filters.
    Use parameterized queries!
    """
    query = "SELECT * FROM products WHERE 1=1"
    params = []
    
    # TODO: Add name filter
    # if name:
    #     pass
    
    # TODO: Add category filter
    # if category:
    #     pass
    
    # TODO: Add min_price filter
    # if min_price:
    #     pass
    
    return pd.read_sql(query, conn, params=params)
```

---

## Answer Key

### Multiple Choice

1. **B** - SQLite requires no server — database is just a file
2. **B** - `@st.cache_resource` returns the same connection object (singleton)
3. **B** - SQLite's default thread check prevents multi-threaded access
4. **B** - SQL injection inserts malicious code through user input
5. **B** - Parameterized queries treat input as values, not SQL code
6. **B** - `commit()` saves changes to the database
7. **B** - Clear cache so fresh data is fetched after writes
8. **B** - Never hard-code credentials; use `st.secrets` or env vars
9. **A** - ACID = Atomicity, Consistency, Isolation, Durability
10. **B** - Parameterized queries use placeholders (?, :name)
11. **B** - `cache_data` for queries (copies), `cache_resource` for connections (singleton)
12. **A** - WAL = Write-Ahead Logging, improves concurrent read/write

### Short Answer

**Q13.**
- **SQLite:** No server, file-based, single-writer. Use for learning, prototypes, single-user apps.
- **PostgreSQL:** Feature-rich, ACID compliant, advanced features. Use for production, complex queries, multi-user.
- **MySQL:** Fast, widely supported, good for web apps. Use for read-heavy applications, existing MySQL infrastructure.

**Q14.** The error occurs because SQLite allows only one writer at a time. If multiple threads/reruns try to write simultaneously, it locks.

**Fix:**
```python
@st.cache_resource
def get_connection():
    return sqlite3.connect("data.db", check_same_thread=False)

def add_user(name):
    conn = get_connection()
    conn.execute("INSERT INTO users (name) VALUES (?)", (name,))
    conn.commit()
```

**Q15.**
1. **Parameterized queries** — prevent SQL injection
2. **Secrets management** — use `st.secrets`, never hard-code credentials
3. **Connection caching** — use `@st.cache_resource` with proper thread settings
4. **Error handling** — graceful failure messages, no sensitive data in errors
5. **Cache invalidation** — clear cache after writes to prevent stale data

### Code Completion

**Q16.**
```python
@st.cache_resource
def get_connection():
    """Get or create cached database connection."""
    conn = sqlite3.connect("data.db", check_same_thread=False)
    conn.execute("PRAGMA journal_mode=WAL")
    return conn
```

**Q17.**
```python
def search_products(conn, name=None, category=None, min_price=None):
    """Search products with optional filters."""
    query = "SELECT * FROM products WHERE 1=1"
    params = []
    
    if name:
        query += " AND name LIKE ?"
        params.append(f"%{name}%")
    
    if category:
        query += " AND category = ?"
        params.append(category)
    
    if min_price is not None:
        query += " AND price >= ?"
        params.append(min_price)
    
    return pd.read_sql(query, conn, params=params)
```

---

## Related Materials

- 📖 Reading: [14 — Databases & Persistence](../readings/14_databases_and_persistence.md)
- 📓 Notebook: [14 — Databases & Persistence](../notebooks/14_databases_persistence.ipynb)
- ✏️ Exercise: [14 — Database Workshop](../exercises/14_database_workshop.py)
- 🖥️ Demo App: [14 — Database Dashboard](../apps/14_database_dashboard.py)
