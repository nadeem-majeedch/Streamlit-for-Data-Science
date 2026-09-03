# Exercise 14 — Database Workshop: Solution Notes

> **👩‍🏫 Instructor Reference**
> *Expected approach, key code, and grading guidance.*

---

## Challenge 1: Basic Queries

### Expected Approach
Use `@st.cache_resource` for connection, parameterized INSERT, and `pd.read_sql` for display.

### Key Code
```python
@st.cache_resource
def get_connection():
    conn = sqlite3.connect("workshop.db", check_same_thread=False)
    conn.execute("PRAGMA journal_mode=WAL")
    return conn

# INSERT with form
with st.form("add_employee"):
    name = st.text_input("Name")
    department = st.selectbox("Department", ["Engineering", "Sales", "Marketing", "HR"])
    salary = st.number_input("Salary", 30000, 200000, 60000)
    hire_date = st.date_input("Hire Date")
    if st.form_submit_button("Add"):
        conn = get_connection()
        conn.execute(
            "INSERT INTO employees (name, department, salary, hire_date) VALUES (?, ?, ?, ?)",
            (name, department, salary, str(hire_date))
        )
        conn.commit()
        get_connection.clear()  # Invalidate cache
        st.success(f"Added {name}!")
        st.rerun()

# Display
conn = get_connection()
df = pd.read_sql("SELECT * FROM employees", conn)
st.dataframe(df, use_container_width=True)
```

### Common Mistakes
- Using f-strings in SQL (SQL injection)
- Forgetting `conn.commit()` after INSERT
- Not clearing cache after writes (stale data)
- Using `sqlite3.connect()` without `check_same_thread=False`

### Grading Notes (25 marks)
- Full marks: Form works, INSERT succeeds, data displays, stats shown
- 18 marks: INSERT works, display works, missing stats
- 10 marks: Basic connection works

---

## Challenge 2: Parameterized Queries

### Key Code
```python
search = st.text_input("Search by name")
if search:
    results = pd.read_sql(
        "SELECT * FROM employees WHERE name LIKE ?",
        conn,
        params=(f"%{search}%",)
    )
    st.write(f"Found {len(results)} results")
    st.dataframe(results)

min_sal, max_sal = st.columns(2)
with min_sal:
    min_s = st.number_input("Min Salary", 30000, 200000, 50000)
with max_sal:
    max_s = st.number_input("Max Salary", 30000, 200000, 100000)

filtered = pd.read_sql(
    "SELECT * FROM employees WHERE salary BETWEEN ? AND ?",
    conn, params=(min_s, max_s)
)
st.dataframe(filtered)
```

### Common Mistakes
- Using string formatting: `f"WHERE name = '{search}'"` (SQL injection!)
- Not using `params=` parameter

---

## Challenge 3: CRUD Operations

### Key Patterns

**UPDATE:**
```python
conn.execute(
    "UPDATE employees SET salary = ? WHERE id = ?",
    (new_salary, employee_id)
)
conn.commit()
```

**DELETE:**
```python
if st.button(f"Delete {name}", type="secondary"):
    conn.execute("DELETE FROM employees WHERE id = ?", (emp_id,))
    conn.commit()
    st.success(f"Deleted {name}")
    st.rerun()
```

### Common Mistakes
- Forgetting WHERE clause in UPDATE/DELETE
- Not committing after changes
- Not refreshing display after mutation

---

## Challenge 4: Project Management (if present)

### Expected Approach
Second table (projects) with JOIN query to show project assignments.

### Key Code
```python
# JOIN query
st.dataframe(pd.read_sql("""
    SELECT e.name, e.department, p.name as project, p.budget, p.status
    FROM employees e
    LEFT JOIN projects p ON 1=1
    ORDER BY e.name
""", conn))
```

### Grading Notes (25 marks)
- Full marks: All CRUD operations work, parameterized queries, cache invalidation
- 18 marks: CRUD works but missing cache invalidation
- 10 marks: Basic operations work

---

## Security Notes

### What to Check During Grading
1. **All SQL uses parameterized queries** (no f-strings)
2. **Connection cached with `check_same_thread=False`**
3. **Cache cleared after writes** (`.clear()` or `st.cache_resource.clear()`)
4. **No hardcoded database paths** (use config or relative paths)
5. **Error handling around database operations**
