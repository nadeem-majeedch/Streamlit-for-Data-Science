"""
Exercise 14: Database Workshop
================================

Module 10 · Advanced

Master database integration with Streamlit and SQLite.

Learning Objectives:
- Connect to SQLite databases
- Execute SQL queries
- Use parameterized queries
- Implement CRUD operations
- Cache connections properly

Instructions:
Complete each section by filling in the TODOs.
Run with: streamlit run exercises/14_database_workshop.py
"""

import streamlit as st
import sqlite3
import pandas as pd

st.set_page_config(page_title="Database Workshop", page_icon="🗄️", layout="wide")
st.title("🗄️ Exercise 14: Database Workshop")
st.markdown("*Module 10 · Advanced — Database integration with Streamlit*")

st.divider()

# ============================================================================
# DATABASE SETUP
# ============================================================================

@st.cache_resource
def get_connection():
    """Get or create cached database connection."""
    conn = sqlite3.connect("workshop.db", check_same_thread=False)
    conn.execute("PRAGMA journal_mode=WAL")
    return conn

def init_database():
    """Initialize database schema."""
    conn = get_connection()
    conn.executescript("""
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            department TEXT,
            salary REAL,
            hire_date TEXT
        );
        
        CREATE TABLE IF NOT EXISTS projects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            budget REAL,
            status TEXT DEFAULT 'Active'
        );
    """)
    conn.commit()

# Initialize on first run
init_database()

# ============================================================================
# CHALLENGE 1: Basic Queries
# ============================================================================
st.header("🎯 Challenge 1: Basic SQL Queries")
st.write("Practice fundamental SQL operations.")

# TODO: Create a form to add employees
# with st.form("add_employee"):
#     name = st.text_input("Name")
#     department = st.selectbox("Department", ["Engineering", "Sales", "Marketing", "HR"])
#     salary = st.number_input("Salary", 30000, 200000, 60000)
#     hire_date = st.date_input("Hire Date")
#     if st.form_submit_button("Add"):
#         conn = get_connection()
#         conn.execute(
#             "INSERT INTO employees (name, department, salary, hire_date) VALUES (?, ?, ?, ?)",
#             (name, department, salary, str(hire_date))
#         )
#         conn.commit()
#         st.success(f"Added {name}!")

# TODO: Display all employees
# conn = get_connection()
# df = pd.read_sql("SELECT * FROM employees", conn)
# st.dataframe(df)

# TODO: Calculate and display department statistics
# dept_stats = pd.read_sql(\"\"\"
#     SELECT 
#         department,
#         COUNT(*) as headcount,
#         AVG(salary) as avg_salary
#     FROM employees
#     GROUP BY department
# \"\"\", conn)
# st.dataframe(dept_stats)

st.divider()

# ============================================================================
# CHALLENGE 2: Parameterized Queries
# ============================================================================
st.header("🎯 Challenge 2: Parameterized Queries")
st.write("Practice safe, parameterized SQL queries.")

# TODO: Create a search form with parameterized query
# search_term = st.text_input("Search by name:")
# if search_term:
#     conn = get_connection()
#     # SAFE: Use parameterized query
#     results = pd.read_sql(
#         "SELECT * FROM employees WHERE name LIKE ?",
#         conn,
#         params=(f"%{search_term}%",)
#     )
#     st.write(f"Found {len(results)} results:")
#     st.dataframe(results)

# TODO: Create salary range filter
# col1, col2 = st.columns(2)
# with col1:
#     min_salary = st.number_input("Min Salary", 30000, 200000, 50000)
# with col2:
#     max_salary = st.number_input("Max Salary", 30000, 200000, 100000)
# 
# filtered = pd.read_sql(
#     "SELECT * FROM employees WHERE salary BETWEEN ? AND ?",
#     conn,
#     params=(min_salary, max_salary)
# )
# st.dataframe(filtered)

st.divider()

# ============================================================================
# CHALLENGE 3: CRUD Operations
# ============================================================================
st.header("🎯 Challenge 3: CRUD Operations")
st.write("Implement Create, Read, Update, Delete.")

# TODO: UPDATE operation
# st.subheader("Update Employee Salary")
# conn = get_connection()
# employees = pd.read_sql("SELECT id, name FROM employees", conn)
# if not employees.empty:
#     emp_id = st.selectbox("Select employee", employees["id"].tolist(), 
#                           format_func=lambda x: employees[employees["id"]==x]["name"].values[0])
#     new_salary = st.number_input("New Salary", 30000, 200000, 70000)
#     if st.button("Update Salary"):
#         conn.execute("UPDATE employees SET salary = ? WHERE id = ?", (new_salary, emp_id))
#         conn.commit()
#         st.success("Updated!")
#         st.rerun()

# TODO: DELETE operation
# st.subheader("Delete Employee")
# if not employees.empty:
#     del_id = st.selectbox("Select to delete", employees["id"].tolist(),
#                           format_func=lambda x: employees[employees["id"]==x]["name"].values[0],
#                           key="delete")
#     if st.button("Delete"):
#         conn.execute("DELETE FROM employees WHERE id = ?", (del_id,))
#         conn.commit()
#         st.success("Deleted!")
#         st.rerun()

# TODO: Display current data
# df = pd.read_sql("SELECT * FROM employees ORDER BY name", conn)
# st.dataframe(df, use_container_width=True)

st.divider()

# ============================================================================
# CHALLENGE 4: Project Management
# ============================================================================
st.header("🎯 Challenge 4: Project Management")
st.write("Build a project management system.")

# TODO: Add projects
# with st.form("add_project"):
#     proj_name = st.text_input("Project Name")
#     budget = st.number_input("Budget", 10000, 1000000, 100000)
#     status = st.selectbox("Status", ["Active", "On Hold", "Completed"])
#     if st.form_submit_button("Create Project"):
#         conn = get_connection()
#         conn.execute(
#             "INSERT INTO projects (name, budget, status) VALUES (?, ?, ?)",
#             (proj_name, budget, status)
#         )
#         conn.commit()
#         st.success(f"Created project: {proj_name}")

# TODO: Display projects with statistics
# conn = get_connection()
# projects = pd.read_sql("SELECT * FROM projects", conn)
# st.dataframe(projects)
# 
# if not projects.empty:
#     st.metric("Total Budget", f"${projects['budget'].sum():,.0f}")
#     st.metric("Active Projects", len(projects[projects["status"] == "Active"]))

# TODO: Filter projects by status
# status_filter = st.multiselect("Filter by status", ["Active", "On Hold", "Completed"])
# if status_filter:
#     filtered = pd.read_sql(
#         "SELECT * FROM projects WHERE status IN ({})".format(",".join("?" * len(status_filter))),
#         conn,
#         params=status_filter
#     )
#     st.dataframe(filtered)

st.divider()

# ============================================================================
# CHALLENGE 5: Error Handling
# ============================================================================
st.header("🎯 Challenge 5: Error Handling")
st.write("Practice graceful error handling.")

# TODO: Create a safe query function
# def safe_query(query, params=()):
#     try:
#         conn = get_connection()
#         return pd.read_sql(query, conn, params=params)
#     except sqlite3.OperationalError as e:
#         st.error(f"Query error: {e}")
#         return pd.DataFrame()
#     except Exception as e:
#         st.error(f"Unexpected error: {e}")
#         return pd.DataFrame()

# TODO: Create a safe execute function
# def safe_execute(query, params=()):
#     try:
#         conn = get_connection()
#         conn.execute(query, params)
#         conn.commit()
#         return True
#     except sqlite3.IntegrityError as e:
#         st.error(f"Data integrity error: {e}")
#         return False
#     except Exception as e:
#         st.error(f"Error: {e}")
#         return False

# TODO: Test error handling with invalid queries
# if st.button("Test Error Handling"):
#     result = safe_query("SELECT * FROM nonexistent_table")
#     if result.empty:
#         st.info("Handled error gracefully!")

st.divider()

# ============================================================================
# BONUS: Data Export
# ============================================================================
st.header("🏆 Bonus: Data Export")
st.write("Export query results to CSV.")

# TODO: Add export functionality
# conn = get_connection()
# df = pd.read_sql("SELECT * FROM employees", conn)
# if not df.empty:
#     csv = df.to_csv(index=False)
#     st.download_button(
#         "Download CSV",
#         csv,
#         "employees.csv",
#         "text/csv",
#         key="download-csv"
#     )

st.divider()

# ============================================================================
# COMPLETION
# ============================================================================
st.success("🎉 Workshop Complete!")
st.markdown("""
**What you practiced:**
- ✅ SQLite connection and caching
- ✅ Basic SQL queries (SELECT, WHERE, GROUP BY)
- ✅ Parameterized queries for security
- ✅ CRUD operations (Create, Read, Update, Delete)
- ✅ Error handling patterns
- ✅ Data export

**Key security rule:**
- ⚠️ **NEVER** concatenate user input into SQL
- ✅ **ALWAYS** use parameterized queries

**Next steps:**
- Read: [Databases & Persistence](../readings/14_databases_and_persistence.md)
- Notebook: [Databases & Persistence](../notebooks/14_databases_persistence.ipynb)
- Demo App: [Database Dashboard](../apps/14_database_dashboard.py)
""")

# Run check
if __name__ == "__main__":
    st.write("✅ Exercise file is valid and ready to run!")
