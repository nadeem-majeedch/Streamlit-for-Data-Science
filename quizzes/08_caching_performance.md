# Quiz 08: Caching & Performance

> **📝 Quiz · Module 08 · Advanced**  
> *Test your understanding of Streamlit caching and performance optimization.*

---

## Multiple Choice

### Q1. When should you use `@st.cache_data` vs `@st.cache_resource`?

a) `cache_data` for database connections, `cache_resource` for DataFrames  
b) `cache_data` for DataFrames and queries, `cache_resource` for connections and models  
c) They're interchangeable — use either one  
d) `cache_resource` is always faster

---

### Q2. What does `@st.cache_data` return to each caller?

a) The same object (singleton)  
b) A copy of the cached object  
c) A reference to the cached object  
d) A proxy object

---

### Q3. What does `@st.cache_resource` return to each caller?

a) A copy of the cached object  
b) The same object (singleton)  
c) A deep copy of the cached object  
d) A new instance each time

---

### Q4. How do you set a cache to expire after 1 hour?

```python
# Option A
@st.cache_data(ttl=3600)

# Option B
@st.cache_data(expiry=3600)

# Option C
@st.cache_data(timeout=3600)

# Option D
@st.cache_data(lifetime=3600)
```

---

### Q5. Why might you need `@st.cache_resource` instead of `@st.cache_data` for a database connection?

a) Connections are faster to cache  
b) Connections aren't pickleable  
c) Connections need to be shared  
d) Both B and C

---

### Q6. How do you clear a specific function's cache?

a) `st.cache_data.clear_all()`  
b) `func.clear()`  
c) `del st.cache_data[func]`  
d) `st.cache_data.remove(func)`

---

### Q7. What happens if you modify a cached object returned by `@st.cache_data`?

a) The modification affects all users  
b) The modification is lost  
c) The modification only affects the local copy  
d) Streamlit raises an error

---

### Q8. What happens if you modify a cached object returned by `@st.cache_resource`?

a) Only your session is affected  
b) The modification affects ALL users and sessions  
c) The modification is automatically reverted  
d) Streamlit raises an error

---

### Q9. Which is TRUE about `scope="session"` in caching?

a) The cache is shared across all users  
b) The cache is cleared when the session disconnects  
c) The cache persists to disk  
d) The cache is faster than global scope

---

### Q10. What is the `refresh_mode="background"` option?

a) Refreshes the cache in a separate thread  
b) Returns stale value immediately, refreshes asynchronously  
c) Only refreshes when the user clicks a button  
d) Refreshes during off-peak hours

---

### Q11. Why shouldn't you cache functions with side effects (logging, email)?

a) Side effects are too slow  
b) Side effects won't repeat on cache hits  
c) Streamlit doesn't allow side effects  
d) Side effects cause errors

---

### Q12. What is `max_entries` used for?

a) Limiting the number of function calls  
b) Limiting cache size to prevent memory issues  
c) Limiting the number of users  
d) Limiting computation time

---

## Short Answer

### Q13. Explain the difference between `@st.cache_data` and `@st.cache_resource`. When would you use each? Give two examples for each.

---

### Q14. A developer is caching a function that returns a Pandas DataFrame. They notice that modifications to the DataFrame don't persist across reruns. Explain why and provide the correct approach if they need persistent modifications.

---

### Q15. Describe three strategies for cache invalidation in Streamlit applications. When would you use each?

---

## Code Completion

### Q16. Complete the cached database query function:

```python
import streamlit as st
import pandas as pd
from sqlalchemy import text

# TODO: Add caching with 5-minute TTL
def run_query(engine, query):
    """Execute SQL query with caching."""
    # TODO: Write the implementation
    pass

# Usage
engine = get_engine()
df = run_query(engine, "SELECT * FROM users")
```

---

### Q17. Complete the model loader with validation:

```python
import streamlit as st
import joblib

# TODO: Cache the model as a resource
def load_model(model_path):
    """Load ML model with validation."""
    # TODO: Write the implementation
    pass

# TODO: Add validation function
def validate_model(model):
    """Check if model is still valid."""
    # TODO: Write the implementation
    pass

# Usage
model = load_model("classifier.joblib")
prediction = model.predict(X)
```

---

## Answer Key

### Multiple Choice

1. **B** - `cache_data` for data (returns copies), `cache_resource` for resources (returns same object)
2. **B** - Returns copies so each user has independent data
3. **B** - Returns the same object (singleton) for shared resources
4. **A** - `ttl=3600` sets expiration to 3600 seconds (1 hour)
5. **D** - Connections aren't pickleable AND need to be shared
6. **B** - `func.clear()` clears all entries for that function
7. **C** - Modifications only affect the local copy (other users unaffected)
8. **B** - Resources are shared — modifications affect everyone
9. **B** - Session-scoped caches are cleared when the session disconnects
10. **B** - Returns stale value immediately, updates in background
11. **B** - Side effects only execute on cache miss, not on hits
12. **B** - Limits number of cached entries to control memory usage

### Short Answer

**Q13.** 
- `@st.cache_data`: Returns **copies**, use for DataFrames, queries, transforms. Examples: loading CSV files, executing SQL queries, API responses.
- `@st.cache_resource`: Returns **same object**, use for connections, models, clients. Examples: database connections, loaded ML models, API client objects.

**Q14.** `@st.cache_data` returns copies, so modifications only affect the local copy. If persistent modifications are needed, store the modified data in `st.session_state` or use `@st.cache_resource` if the object should be shared.

**Q15.** 
1. **TTL** - Automatic expiration for time-sensitive data (e.g., stock prices)
2. **Manual clearing** - `func.clear()` or `st.cache_data.clear()` for on-demand refresh
3. **Max entries** - LRU eviction when cache is full

### Code Completion

**Q16.**
```python
@st.cache_data(ttl=300)  # 5 minutes
def run_query(engine, query):
    """Execute SQL query with caching."""
    with engine.connect() as conn:
        return pd.read_sql(text(query), conn)
```

**Q17.**
```python
@st.cache_resource(validate=validate_model)
def load_model(model_path):
    """Load ML model with validation."""
    return joblib.load(model_path)

def validate_model(model):
    """Check if model is still valid."""
    return hasattr(model, "predict") and callable(model.predict)
```

---

## Related Materials

- 📖 Reading: [12 — Caching & Performance](../readings/12_caching_and_performance.md)
- 📓 Notebook: [12 — Caching & Performance](../notebooks/12_caching_performance.ipynb)
- ✏️ Exercise: [12 — Caching Workshop](../exercises/12_caching_workshop.py)
- 🖥️ Demo App: [12 — Caching Demo](../apps/12_caching_performance_demo.py)
