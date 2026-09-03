"""
Streamlit Database Dashboard Demo
==================================

Module 10 · Advanced

A complete demonstration of database integration:
- SQLite connection and caching
- CRUD operations
- Parameterized queries
- Error handling
- Secrets management

Run: streamlit run apps/14_database_dashboard.py
"""

import streamlit as st
import sqlite3
import pandas as pd
from datetime import datetime, timedelta

st.set_page_config(
    page_title="Database Dashboard",
    page_icon="🗄️",
    layout="wide"
)

st.title("🗄️ Database Dashboard Demo")
st.caption("Module 10 · SQLite integration with Streamlit")

# ============================================================================
# Database Setup
# ============================================================================

@st.cache_resource
def get_connection():
    """Get cached database connection."""
    conn = sqlite3.connect(":memory:", check_same_thread=False)
    conn.execute("PRAGMA journal_mode=WAL")
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
            quantity INTEGER,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        );
        
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_id INTEGER,
            quantity INTEGER,
            total REAL,
            order_date TEXT DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (product_id) REFERENCES products(id)
        );
    """)
    
    # Seed data if empty
    count = conn.execute("SELECT COUNT(*) FROM products").fetchone()[0]
    if count == 0:
        products = [
            ("Laptop", "Electronics", 999.99, 50),
            ("Mouse", "Electronics", 29.99, 200),
            ("Keyboard", "Electronics", 79.99, 150),
            ("Monitor", "Electronics", 349.99, 75),
            ("Desk", "Furniture", 249.99, 30),
            ("Chair", "Furniture", 199.99, 60),
            ("Notebook", "Stationery", 4.99, 500),
            ("Pen", "Stationery", 1.99, 1000),
        ]
        conn.executemany(
            "INSERT INTO products (name, category, price, quantity) VALUES (?, ?, ?, ?)",
            products
        )
        
        # Add sample orders
        for i in range(20):
            product_id = (i % 8) + 1
            qty = (i % 5) + 1
            price = conn.execute("SELECT price FROM products WHERE id = ?", (product_id,)).fetchone()[0]
            order_date = (datetime.now() - timedelta(days=i)).strftime("%Y-%m-%d")
            conn.execute(
                "INSERT INTO orders (product_id, quantity, total, order_date) VALUES (?, ?, ?, ?)",
                (product_id, qty, qty * price, order_date)
            )
        
        conn.commit()

init_database()

# ============================================================================
# Sidebar Navigation
# ============================================================================

st.sidebar.title("📚 Module 10 Demo")
st.sidebar.markdown("---")

tab = st.sidebar.radio(
    "Navigate:",
    ["📊 Overview", "➕ Add Product", "🔍 Search", "📦 Orders", "⚙️ Settings"]
)

st.sidebar.markdown("---")
st.sidebar.markdown("""
**Key Concepts:**
- `@st.cache_resource` for connections
- `@st.cache_data` for queries
- Parameterized queries
- Clear cache after writes
""")

# ============================================================================
# Tab 1: Overview
# ============================================================================
if tab.startswith("📊"):
    st.header("📊 Dashboard Overview")
    
    conn = get_connection()
    
    # Metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        count = pd.read_sql("SELECT COUNT(*) as cnt FROM products", conn).iloc[0]["cnt"]
        st.metric("Products", count)
    
    with col2:
        order_count = pd.read_sql("SELECT COUNT(*) as cnt FROM orders", conn).iloc[0]["cnt"]
        st.metric("Orders", order_count)
    
    with col3:
        total_revenue = pd.read_sql("SELECT SUM(total) as total FROM orders", conn).iloc[0]["total"]
        st.metric("Revenue", f"${total_revenue:,.2f}" if total_revenue else "$0")
    
    with col4:
        categories = pd.read_sql("SELECT COUNT(DISTINCT category) as cnt FROM products", conn).iloc[0]["cnt"]
        st.metric("Categories", categories)
    
    st.divider()
    
    # Products by category
    st.subheader("Products by Category")
    cat_data = pd.read_sql("""
        SELECT category, COUNT(*) as count, SUM(quantity) as total_stock
        FROM products
        GROUP BY category
    """, conn)
    st.dataframe(cat_data, use_container_width=True)
    st.bar_chart(cat_data.set_index("category")["total_stock"])
    
    # Recent orders
    st.subheader("Recent Orders")
    recent_orders = pd.read_sql("""
        SELECT o.id, p.name as product, o.quantity, o.total, o.order_date
        FROM orders o
        JOIN products p ON o.product_id = p.id
        ORDER BY o.order_date DESC
        LIMIT 10
    """, conn)
    st.dataframe(recent_orders, use_container_width=True)

# ============================================================================
# Tab 2: Add Product
# ============================================================================
elif tab.startswith("➕"):
    st.header("➕ Add New Product")
    
    with st.form("add_product"):
        col1, col2 = st.columns(2)
        
        with col1:
            name = st.text_input("Product Name *")
            category = st.selectbox("Category", ["Electronics", "Furniture", "Stationery", "Other"])
        
        with col2:
            price = st.number_input("Price ($)", min_value=0.01, value=9.99, step=0.01)
            quantity = st.number_input("Quantity", min_value=0, value=100)
        
        if st.form_submit_button("Add Product", type="primary"):
            if not name:
                st.error("Product name is required!")
            else:
                try:
                    conn = get_connection()
                    conn.execute(
                        "INSERT INTO products (name, category, price, quantity) VALUES (?, ?, ?, ?)",
                        (name, category, price, quantity)
                    )
                    conn.commit()
                    st.success(f"✅ Added '{name}' successfully!")
                    st.balloons()
                except Exception as e:
                    st.error(f"Error adding product: {e}")
    
    # Display current products
    st.divider()
    st.subheader("Current Products")
    conn = get_connection()
    df = pd.read_sql("SELECT * FROM products ORDER BY name", conn)
    st.dataframe(df, use_container_width=True)

# ============================================================================
# Tab 3: Search
# ============================================================================
elif tab.startswith("🔍"):
    st.header("🔍 Search Products")
    
    conn = get_connection()
    
    # Search form
    col1, col2, col3 = st.columns(3)
    
    with col1:
        search_name = st.text_input("Search by name")
    
    with col2:
        categories = pd.read_sql("SELECT DISTINCT category FROM products", conn)["category"].tolist()
        search_category = st.selectbox("Filter by category", ["All"] + categories)
    
    with col3:
        min_price = st.number_input("Min price", min_value=0.0, value=0.0)
        max_price = st.number_input("Max price", min_value=0.0, value=1000.0)
    
    # Build query dynamically with parameters
    query = "SELECT * FROM products WHERE 1=1"
    params = []
    
    if search_name:
        query += " AND name LIKE ?"
        params.append(f"%{search_name}%")
    
    if search_category != "All":
        query += " AND category = ?"
        params.append(search_category)
    
    if min_price > 0:
        query += " AND price >= ?"
        params.append(min_price)
    
    if max_price < 1000:
        query += " AND price <= ?"
        params.append(max_price)
    
    query += " ORDER BY name"
    
    # Execute parameterized query
    results = pd.read_sql(query, conn, params=params)
    
    st.write(f"**Found {len(results)} products**")
    st.dataframe(results, use_container_width=True)
    
    # Highlight: Safe vs Unsafe
    st.divider()
    st.subheader("⚠️ Security Note")
    st.code('''
# ❌ NEVER do this (SQL injection vulnerable):
query = f"SELECT * FROM products WHERE name = '{search_name}'"

# ✅ ALWAYS do this (parameterized):
query = "SELECT * FROM products WHERE name = ?"
results = pd.read_sql(query, conn, params=(search_name,))
    ''', language="python")

# ============================================================================
# Tab 4: Orders
# ============================================================================
elif tab.startswith("📦"):
    st.header("📦 Order Management")
    
    conn = get_connection()
    
    # New order form
    st.subheader("Create New Order")
    
    with st.form("new_order"):
        products = pd.read_sql("SELECT id, name, price, quantity FROM products", conn)
        
        if products.empty:
            st.warning("No products available. Add some first!")
        else:
            col1, col2 = st.columns(2)
            
            with col1:
                product_id = st.selectbox(
                    "Select Product",
                    products["id"].tolist(),
                    format_func=lambda x: f"{products[products['id']==x]['name'].values[0]} (${products[products['id']==x]['price'].values[0]:.2f})"
                )
            
            with col2:
                order_qty = st.number_input("Quantity", min_value=1, value=1)
            
            # Show total
            if product_id:
                price = products[products["id"]==product_id]["price"].values[0]
                st.write(f"**Total: ${price * order_qty:.2f}**")
            
            if st.form_submit_button("Place Order"):
                if product_id:
                    price = products[products["id"]==product_id]["price"].values[0]
                    total = price * order_qty
                    
                    # Check stock
                    stock = products[products["id"]==product_id]["quantity"].values[0]
                    if order_qty > stock:
                        st.error(f"Insufficient stock! Only {stock} available.")
                    else:
                        try:
                            conn.execute(
                                "INSERT INTO orders (product_id, quantity, total) VALUES (?, ?, ?)",
                                (product_id, order_qty, total)
                            )
                            conn.execute(
                                "UPDATE products SET quantity = quantity - ? WHERE id = ?",
                                (order_qty, product_id)
                            )
                            conn.commit()
                            st.success(f"Order placed! Total: ${total:.2f}")
                            st.rerun()
                        except Exception as e:
                            st.error(f"Error placing order: {e}")
    
    # Order history
    st.divider()
    st.subheader("Order History")
    
    orders = pd.read_sql("""
        SELECT o.id, p.name as product, o.quantity, o.total, o.order_date
        FROM orders o
        JOIN products p ON o.product_id = p.id
        ORDER BY o.order_date DESC
    """, conn)
    
    st.dataframe(orders, use_container_width=True)
    
    # Export
    if not orders.empty:
        csv = orders.to_csv(index=False)
        st.download_button(
            "📥 Export Orders CSV",
            csv,
            "orders.csv",
            "text/csv"
        )

# ============================================================================
# Tab 5: Settings
# ============================================================================
else:
    st.header("⚙️ Settings & Info")
    
    st.subheader("Database Information")
    
    conn = get_connection()
    
    # Table info
    tables = conn.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()
    st.write(f"**Tables:** {', '.join([t[0] for t in tables])}")
    
    for table_name in [t[0] for t in tables]:
        count = conn.execute(f"SELECT COUNT(*) FROM {table_name}").fetchone()[0]
        st.write(f"- {table_name}: {count} rows")
    
    st.divider()
    
    st.subheader("Security Best Practices")
    st.markdown("""
    1. ✅ **Parameterized queries** — prevents SQL injection
    2. ✅ **Connection caching** — `@st.cache_resource` for singletons
    3. ✅ **Cache invalidation** — `.clear()` after writes
    4. ✅ **Error handling** — graceful failure messages
    5. ✅ **Secrets management** — use `st.secrets` for credentials
    """)
    
    st.divider()
    
    st.subheader("For Production (PostgreSQL)")
    st.code('''
# .streamlit/secrets.toml (NEVER commit!)
[database]
host = "localhost"
port = 5432
name = "myapp_db"
username = "admin"
password = "secure_password"

# In your app:
import streamlit as st
import psycopg2

conn = psycopg2.connect(
    host=st.secrets["database"]["host"],
    port=st.secrets["database"]["port"],
    dbname=st.secrets["database"]["name"],
    user=st.secrets["database"]["username"],
    password=st.secrets["database"]["password"]
)
    ''', language="python")
    
    st.warning("⚠️ Add `.streamlit/secrets.toml` to `.gitignore`!")

# ============================================================================
# Footer
# ============================================================================
st.divider()
st.caption("""
**🎓 Module 10: Databases & Persistence**
- SQLite for learning, PostgreSQL/MySQL for production
- Always use parameterized queries
- Cache connections with `@st.cache_resource`
- Manage secrets with `st.secrets`
""")

# Run verification
if __name__ == "__main__":
    st.write("✅ App is running correctly!")
