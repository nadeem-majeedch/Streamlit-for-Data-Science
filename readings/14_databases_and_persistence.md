# 14 — Databases & Persistence

> **📖 Reading · Module 10 · Advanced**  
> *Connect Streamlit apps to databases for persistent, queryable data storage.*

---

## Learning Objectives

After completing this reading you will be able to:

- Explain why databases are essential for Data Science applications
- Understand relational database concepts (tables, rows, columns, keys)
- Write basic SQL queries (SELECT, WHERE, JOIN, GROUP BY)
- Connect Python/Streamlit to SQLite databases
- Execute parameterized queries to prevent SQL injection
- Cache database connections for performance
- Implement CRUD operations (Create, Read, Update, Delete)
- Handle database errors gracefully
- Manage credentials securely using Streamlit secrets

---

## 1. Why Databases Matter

### Problems with File-Based Data

| Problem | Description |
|---------|-------------|
| **No concurrent access** | Two users can't write simultaneously |
| **No querying** | Must load entire file to filter |
| **No transactions** | Partial writes corrupt data |
| **No relationships** | Duplicating data across files |
| **Scalability** | Large files become slow |

### Database Benefits

| Benefit | Description |
|---------|-------------|
| **Concurrent access** | Multiple users read/write safely |
| **SQL queries** | Filter, aggregate, join without loading all data |
| **ACID transactions** | Consistent, reliable writes |
| **Relationships** | Normalized data, no duplication |
| **Scalability** | Handle millions of rows efficiently |
| **Security** | Access control, encryption at rest |

---

## 2. Relational Database Concepts

### Tables, Rows, Columns

```
+----+----------+--------+--------+
| id | name     | email  | score  |
+----+----------+--------+--------+
| 1  | Alice    | a@b.co | 95     |
| 2  | Bob      | b@b.co | 87     |
| 3  | Charlie  | c@b.co | 92     |
+----+----------+--------+--------+

- Table: "students"
- Rows: 3 records
- Columns: id, name, email, score
```

### Primary Keys

Unique identifier for each row:

```sql
CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT UNIQUE,
    score REAL
);
```

### Relationships (Foreign Keys)

```sql
CREATE TABLE enrollments (
    id INTEGER PRIMARY KEY,
    student_id INTEGER,
    course_id INTEGER,
    FOREIGN KEY (student_id) REFERENCES students(id),
    FOREIGN KEY (course_id) REFERENCES courses(id)
);
```

---

## 3. SQL Basics

### SELECT — Read Data

```sql
-- Select all columns
SELECT * FROM students;

-- Select specific columns
SELECT name, score FROM students;

-- With conditions
SELECT * FROM students WHERE score > 90;

-- Ordering
SELECT * FROM students ORDER BY score DESC;

-- Limiting
SELECT * FROM students LIMIT 10;
```

### Aggregation

```sql
-- Count rows
SELECT COUNT(*) FROM students;

-- Average, sum, min, max
SELECT AVG(score), SUM(score), MIN(score), MAX(score)
FROM students;

-- Group by
SELECT department, AVG(score) as avg_score
FROM students
GROUP BY department
HAVING AVG(score) > 85;
```

### JOIN — Combine Tables

```sql
-- Inner join
SELECT s.name, e.course_id, e.grade
FROM students s
JOIN enrollments e ON s.id = e.student_id;

-- Left join (include all students even without enrollments)
SELECT s.name, e.course_id
FROM students s
LEFT JOIN enrollments e ON s.id = e.student_id;
```

### INSERT — Create Data

```sql
INSERT INTO students (name, email, score)
VALUES ('Diana', 'd@b.co', 88);
```

### UPDATE — Modify Data

```sql
UPDATE students
SET score = 96
WHERE name = 'Alice';
```

### DELETE — Remove Data

```sql
DELETE FROM students
WHERE id = 3;
```

---

## 4. SQLite — The Teaching Database

### Why SQLite?

- **No server required** — database is a single file
- **Built into Python** — no additional installation
- **Perfect for teaching** — focus on SQL, not setup
- **Works locally** — ideal for learning and prototyping

### Limitations (Production)

- Single-writer at a time
- No network access
- No user authentication
- Use PostgreSQL/MySQL for production

---

## 5. Python + SQLite Connection

### Basic Connection

```python
import sqlite3

# Connect to database (creates if doesn't exist)
conn = sqlite3.connect("my_database.db")

# Create a cursor for executing queries
cursor = conn.cursor()

# Execute a query
cursor.execute("SELECT * FROM students")
results = cursor.fetchall()

# Close connection
conn.close()
```

### With Pandas

```python
import sqlite3
import pandas as pd

conn = sqlite3.connect("my_database.db")

# Read SQL query directly to DataFrame
df = pd.read_sql("SELECT * FROM students", conn)

conn.close()
```

---

## 6. Parameterized Queries (Security Critical!)

### The SQL Injection Problem

```python
# ❌ DANGEROUS: Never do this!
user_input = "'; DROP TABLE students; --"
query = f"SELECT * FROM students WHERE name = '{user_input}'"
cursor.execute(query)
# This executes: SELECT * FROM students WHERE name = ''; DROP TABLE students; --'
# Goodbye, students table!
```

### The Safe Solution: Parameterized Queries

```python
# ✅ SAFE: Use placeholders
user_input = "'; DROP TABLE students; --"
query = "SELECT * FROM students WHERE name = ?"
cursor.execute(query, (user_input,))
# This safely treats the input as a string value, not SQL code
```

### SQLite Placeholders

```python
# SQLite uses ? as placeholder
cursor.execute("SELECT * FROM students WHERE name = ? AND score > ?", 
               (name, min_score))

# Or use named parameters
cursor.execute("SELECT * FROM students WHERE name = :name AND score > :min_score",
               {"name": name, "min_score": min_score})
```

### Pandas with Parameters

```python
# Pandas read_sql also supports parameters
df = pd.read_sql(
    "SELECT * FROM students WHERE score > ?",
    conn,
    params=(min_score,)
)
```

---

## 7. Connection Reuse & Caching

### The Problem

Creating a new connection on every rerun is expensive:

```python
# ❌ BAD: New connection every rerun
def get_data():
    conn = sqlite3.connect("data.db")  # Slow!
    df = pd.read_sql("SELECT * FROM data", conn)
    conn.close()
    return df
```

### The Solution: Cache the Connection

```python
import streamlit as st
import sqlite3

@st.cache_resource
def get_connection():
    """Create and cache database connection (singleton)."""
    return sqlite3.connect("data.db", check_same_thread=False)

def get_data():
    """Use cached connection for queries."""
    conn = get_connection()
    return pd.read_sql("SELECT * FROM data", conn)
```

### Why `@st.cache_resource`?

- Returns the **same connection object** to all users
- Connections are not pickleable (can't use `@st.cache_data`)
- `check_same_thread=False` allows multi-threaded access

---

## 8. Streamlit + SQLite Dashboard Pattern

```python
import streamlit as st
import sqlite3
import pandas as pd

# --- Database Setup ---
@st.cache_resource
def get_connection():
    conn = sqlite3.connect("app_data.db", check_same_thread=False)
    conn.execute("PRAGMA journal_mode=WAL")  # Better concurrent access
    return conn

def init_database():
    """Initialize database schema."""
    conn = get_connection()
    conn.executescript("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            category TEXT,
            price REAL,
            quantity INTEGER
        );
    """)
    conn.commit()

# --- Data Operations ---
@st.cache_data(ttl=60)
def get_products():
    conn = get_connection()
    return pd.read_sql("SELECT * FROM products", conn)

def add_product(name, category, price, quantity):
    conn = get_connection()
    conn.execute(
        "INSERT INTO products (name, category, price, quantity) VALUES (?, ?, ?, ?)",
        (name, category, price, quantity)
    )
    conn.commit()
    get_products.clear()  # Invalidate cache

def delete_product(product_id):
    conn = get_connection()
    conn.execute("DELETE FROM products WHERE id = ?", (product_id,))
    conn.commit()
    get_products.clear()

# --- UI ---
st.title("Product Database")

# Initialize on first run
init_database()

# Add product form
with st.form("add_product"):
    name = st.text_input("Name")
    category = st.selectbox("Category", ["Electronics", "Clothing", "Food"])
    price = st.number_input("Price", min_value=0.0)
    quantity = st.number_input("Quantity", min_value=0)
    if st.form_submit_button("Add"):
        add_product(name, category, price, quantity)
        st.success("Product added!")
        st.rerun()

# Display products
df = get_products()
st.dataframe(df)

# Delete product
if not df.empty:
    product_id = st.selectbox("Select product to delete", df["id"].tolist())
    if st.button("Delete"):
        delete_product(product_id)
        st.rerun()
```

---

## 9. Credentials Management

### Streamlit Secrets (Recommended)

Create `.streamlit/secrets.toml` (NEVER commit to git):

```toml
# .streamlit/secrets.toml
[database]
host = "localhost"
port = 5432
name = "myapp_db"
username = "admin"
password = "secure_password_here"
```

### Access in App

```python
import streamlit as st

# Access secrets
db_config = st.secrets["database"]

# Use in connection
conn = sqlite3.connect(
    st.secrets.database.name  # Attribute access
)

# Or for PostgreSQL
import psycopg2
conn = psycopg2.connect(
    host=st.secrets["database"]["host"],
    port=st.secrets["database"]["port"],
    dbname=st.secrets["database"]["name"],
    user=st.secrets["database"]["username"],
    password=st.secrets["database"]["password"]
)
```

### Environment Variables (Alternative)

```python
import os

db_path = os.getenv("DATABASE_PATH", "default.db")
```

---

## 10. Error Handling

### Common Database Errors

```python
import sqlite3
import streamlit as st

def safe_query(query, params=()):
    """Execute query with error handling."""
    try:
        conn = get_connection()
        result = pd.read_sql(query, conn, params=params)
        return result
    except sqlite3.OperationalError as e:
        st.error(f"Query error: {e}")
        return pd.DataFrame()
    except sqlite3.DatabaseError as e:
        st.error(f"Database error: {e}")
        return pd.DataFrame()
    except Exception as e:
        st.error(f"Unexpected error: {e}")
        return pd.DataFrame()

def safe_execute(query, params=()):
    """Execute statement with error handling."""
    try:
        conn = get_connection()
        conn.execute(query, params)
        conn.commit()
        return True
    except sqlite3.IntegrityError as e:
        st.error(f"Data integrity error: {e}")
        return False
    except Exception as e:
        st.error(f"Error: {e}")
        return False
```

### Transaction Pattern

```python
def transfer_funds(from_id, to_id, amount):
    """Transfer with transaction safety."""
    conn = get_connection()
    try:
        conn.execute("BEGIN")
        conn.execute(
            "UPDATE accounts SET balance = balance - ? WHERE id = ?",
            (amount, from_id)
        )
        conn.execute(
            "UPDATE accounts SET balance = balance + ? WHERE id = ?",
            (amount, to_id)
        )
        conn.commit()
        return True
    except Exception:
        conn.rollback()
        return False
```

---

## 11. Production Considerations

### SQLite vs PostgreSQL/MySQL

| Feature | SQLite | PostgreSQL/MySQL |
|---------|--------|------------------|
| Setup | None (file-based) | Server required |
| Concurrent writes | Single writer | Multiple writers |
| Authentication | None | Built-in |
| Network access | No | Yes |
| Scalability | Limited | High |
| Best for | Learning, prototypes | Production apps |

### When to Upgrade

- Multi-user write access needed
- Data exceeds 1GB
- Network access required
- User authentication needed
- Advanced features (JSON, full-text search)

---

## 12. Learning vs Production

### Learning Environment

```python
# SQLite — perfect for learning
import sqlite3
conn = sqlite3.connect("learning.db")
```

### Production Environment

```python
# PostgreSQL with connection pooling
import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.pool import QueuePool

# Use SQLAlchemy for connection pooling
engine = create_engine(
    st.secrets.database.url,
    poolclass=QueuePool,
    pool_size=5,
    max_overflow=10
)
```

---

## Key Takeaways

- **Databases provide** persistent, queryable, concurrent data storage
- **SQLite is ideal for learning** — no setup, built into Python
- **Always use parameterized queries** — never concatenate user input into SQL
- **Cache connections with `@st.cache_resource`** — connections are singletons
- **Manage secrets securely** — use `st.secrets`, never hardcode credentials
- **Handle errors gracefully** — database operations can fail
- **Use transactions** for multi-step operations

---

## Further Reading

- [SQLite Python Docs](https://docs.python.org/3/library/sqlite3.html)
- [Streamlit Secrets Management](https://docs.streamlit.io/develop/concepts/connections/secrets-management)
- [SQLAlchemy Docs](https://docs.sqlalchemy.org/)

---

## Related Materials

- 📓 Notebook: [14 — Databases & Persistence](../notebooks/14_databases_persistence.ipynb)
- ✏️ Exercise: [14 — Database Workshop](../exercises/14_database_workshop.py)
- 🖥️ Demo App: [14 — Database Dashboard](../apps/14_database_dashboard.py)
- 📝 Quiz: [10 — Databases & Persistence](../quizzes/10_databases_persistence.md)
