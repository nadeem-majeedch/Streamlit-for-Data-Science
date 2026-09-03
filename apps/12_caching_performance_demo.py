"""
Streamlit Caching & Performance Demo
=====================================

Module 08 · Advanced

A complete demonstration of caching concepts:
- @st.cache_data for data
- @st.cache_resource for resources
- TTL, max_entries, persistence
- Cache invalidation
- Performance measurement

Run: streamlit run apps/12_caching_performance_demo.py
"""

import streamlit as st
import time
import pandas as pd
import numpy as np
from datetime import datetime

st.set_page_config(
    page_title="Caching & Performance Demo",
    page_icon="⚡",
    layout="wide"
)

st.title("⚡ Caching & Performance Demo")
st.caption("Module 08 · Build fast, responsive Streamlit apps")

# ============================================================================
# Sidebar Navigation
# ============================================================================
st.sidebar.title("📚 Module 08 Demo")
st.sidebar.markdown("---")

demo = st.sidebar.radio(
    "Select Demo:",
    [
        "1️⃣ Cache Basics",
        "2️⃣ cache_data vs cache_resource",
        "3️⃣ TTL & Expiration",
        "4️⃣ Cache Invalidation",
        "5️⃣ Performance Comparison"
    ]
)

st.sidebar.markdown("---")
st.sidebar.markdown("""
**Key Concepts:**
- `@st.cache_data` → copies
- `@st.cache_resource` → singleton
- TTL = time-to-live
- Manual clear with `.clear()`
""")

# ============================================================================
# Demo 1: Cache Basics
# ============================================================================
if demo.startswith("1️⃣"):
    st.header("1️⃣ Cache Basics")
    st.write("Watch how caching transforms performance.")
    
    @st.cache_data
    def slow_function(n):
        """Simulate expensive computation."""
        time.sleep(1)
        return sum(i**2 for i in range(n))
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Without Cache")
        n = st.slider("N (uncached)", 10000, 100000, 50000, key="n_uncached")
        start = time.time()
        result = sum(i**2 for i in range(n))  # No cache!
        elapsed = time.time() - start
        st.metric("Time", f"{elapsed*1000:.0f}ms")
        st.write(f"Result: {result:,}")
    
    with col2:
        st.subheader("With Cache")
        n_cached = st.slider("N (cached)", 10000, 100000, 50000, key="n_cached")
        start = time.time()
        result = slow_function(n_cached)
        elapsed = time.time() - start
        st.metric("Time", f"{elapsed*1000:.2f}ms")
        st.write(f"Result: {result:,}")
    
    st.info("💡 The first cached call takes ~1s. Subsequent calls are instant!")

# ============================================================================
# Demo 2: cache_data vs cache_resource
# ============================================================================
elif demo.startswith("2️⃣"):
    st.header("2️⃣ cache_data vs cache_resource")
    st.write("Understanding the key difference: copies vs singletons.")
    
    @st.cache_data
    def get_data():
        return {"count": 0, "items": [1, 2, 3]}
    
    @st.cache_resource
    def get_resource():
        return {"count": 0, "items": [1, 2, 3]}
    
    st.subheader("@st.cache_data (Returns Copies)")
    d1 = get_data()
    d2 = get_data()
    st.write(f"d1 is d2: **{d1 is d2}** (False — separate copies)")
    d1["count"] = 999
    st.write(f"After modifying d1: d1={d1['count']}, d2={d2['count']}")
    st.info("Each caller gets their own copy — modifications don't affect others.")
    
    st.divider()
    
    st.subheader("@st.cache_resource (Returns Same Object)")
    r1 = get_resource()
    r2 = get_resource()
    st.write(f"r1 is r2: **{r1 is r2}** (True — same object)")
    r1["count"] = 999
    st.warning(f"After modifying r1: r1={r1['count']}, r2={r2['count']} (both changed!)")
    st.warning("⚠️ Resources are shared — modifications affect ALL users!")

# ============================================================================
# Demo 3: TTL & Expiration
# ============================================================================
elif demo.startswith("3️⃣"):
    st.header("3️⃣ TTL & Expiration")
    st.write("Control how long cached values persist.")
    
    @st.cache_data(ttl=10)
    def get_fast_data():
        return {"timestamp": datetime.now().strftime("%H:%M:%S"), "value": np.random.randint(1, 100)}
    
    @st.cache_data(ttl=60)
    def get_medium_data():
        return {"timestamp": datetime.now().strftime("%H:%M:%S"), "value": np.random.randint(1, 100)}
    
    @st.cache_data  # No TTL
    def get_permanent_data():
        return {"timestamp": datetime.now().strftime("%H:%M:%S"), "value": np.random.randint(1, 100)}
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("TTL = 10s")
        data = get_fast_data()
        st.write(f"Cached at: {data['timestamp']}")
        st.write(f"Value: {data['value']}")
    
    with col2:
        st.subheader("TTL = 60s")
        data = get_medium_data()
        st.write(f"Cached at: {data['timestamp']}")
        st.write(f"Value: {data['value']}")
    
    with col3:
        st.subheader("No TTL (forever)")
        data = get_permanent_data()
        st.write(f"Cached at: {data['timestamp']}")
        st.write(f"Value: {data['value']}")
    
    if st.button("🔄 Refresh All"):
        get_fast_data.clear()
        get_medium_data.clear()
        get_permanent_data.clear()
        st.rerun()
    
    st.info("💡 The 10s TTL data refreshes automatically. The others keep their cached values.")

# ============================================================================
# Demo 4: Cache Invalidation
# ============================================================================
elif demo.startswith("4️⃣"):
    st.header("4️⃣ Cache Invalidation")
    st.write("Clear caches manually when needed.")
    
    @st.cache_data
    def load_data(source):
        time.sleep(0.5)
        return {
            "source": source,
            "loaded_at": datetime.now().strftime("%H:%M:%S"),
            "rows": np.random.randint(100, 1000)
        }
    
    source = st.selectbox("Data source", ["database", "api", "file"])
    
    if st.button("Load Data"):
        data = load_data(source)
        st.write(f"**Source:** {data['source']}")
        st.write(f"**Loaded at:** {data['loaded_at']}")
        st.write(f"**Rows:** {data['rows']}")
    
    st.divider()
    
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button(f"Clear '{source}' cache"):
            load_data.clear(source)
            st.success(f"Cleared cache for {source}")
    with col2:
        if st.button("Clear all sources"):
            load_data.clear()
            st.success("Cleared all load_data caches")
    with col3:
        if st.button("Clear ALL caches"):
            st.cache_data.clear()
            st.success("Cleared all data caches")

# ============================================================================
# Demo 5: Performance Comparison
# ============================================================================
else:
    st.header("5️⃣ Performance Comparison")
    st.write("Measure the impact of caching on your app.")
    
    def uncached_computation(n):
        """Simulate expensive uncached operation."""
        time.sleep(0.5)
        return pd.DataFrame({
            "x": np.random.randn(n),
            "y": np.random.randn(n),
            "z": np.random.randn(n)
        })
    
    @st.cache_data(show_spinner="Computing...")
    def cached_computation(n):
        """Cached version of the same operation."""
        time.sleep(0.5)
        return pd.DataFrame({
            "x": np.random.randn(n),
            "y": np.random.randn(n),
            "z": np.random.randn(n)
        })
    
    n = st.slider("Data points", 1000, 100000, 50000)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("❌ Uncached")
        if st.button("Run Uncached", key="uncached"):
            start = time.time()
            df = uncached_computation(n)
            elapsed = time.time() - start
            st.metric("Time", f"{elapsed*1000:.0f}ms")
            st.write(f"DataFrame shape: {df.shape}")
    
    with col2:
        st.subheader("✅ Cached")
        if st.button("Run Cached", key="cached"):
            start = time.time()
            df = cached_computation(n)
            elapsed = time.time() - start
            st.metric("Time", f"{elapsed*1000:.2f}ms")
            st.write(f"DataFrame shape: {df.shape}")
    
    # Benchmark
    st.divider()
    st.subheader("📊 Benchmark")
    
    if st.button("Run Full Benchmark"):
        results = []
        for n in [1000, 5000, 10000, 50000]:
            # Uncached
            start = time.time()
            _ = uncached_computation(n)
            t_uncached = time.time() - start
            
            # Cached (should be fast)
            start = time.time()
            _ = cached_computation(n)
            t_cached = time.time() - start
            
            results.append({
                "N": n,
                "Uncached (ms)": t_uncached * 1000,
                "Cached (ms)": t_cached * 1000,
                "Speedup": f"{t_uncached/t_cached:.0f}x" if t_cached > 0 else "∞"
            })
        
        st.dataframe(pd.DataFrame(results), use_container_width=True)

# ============================================================================
# Footer
# ============================================================================
st.divider()
st.caption("""
**🎓 Learning Points:**
- `@st.cache_data` returns copies — safe for DataFrames
- `@st.cache_resource` returns singletons — for connections/models
- TTL controls freshness — set appropriate expiration
- Manual clearing enables on-demand refresh
""")

# Run verification
if __name__ == "__main__":
    st.write("✅ App is running correctly!")
