# 12 — Caching & Performance in Streamlit

> **📖 Reading · Module 08 · Advanced**  
> *Master Streamlit's caching decorators to build fast, responsive applications.*

---

## Learning Objectives

After completing this reading you will be able to:

- Explain why caching matters in Streamlit's rerun model
- Use `@st.cache_data` to cache function results
- Use `@st.cache_resource` to cache shared resources
- Choose between `cache_data` and `cache_resource` appropriately
- Implement cache invalidation strategies
- Avoid common caching mistakes
- Optimize application performance

---

## 1. Why Caching Matters

### The Rerun Problem

Every user interaction causes Streamlit to rerun your entire script. Without caching, expensive operations execute on every rerun:

```python
import streamlit as st
import pandas as pd

# ⚠️ This downloads data on EVERY interaction!
def get_data():
    return pd.read_csv("https://example.com/large_data.csv")  # 5 seconds

df = get_data()  # Runs every time any widget changes
st.dataframe(df)
```

### The Solution: Caching

Caching stores the result of expensive functions. On subsequent reruns with the same inputs, Streamlit returns the cached result instead of recomputing.

```python
import streamlit as st
import pandas as pd

# ✅ Cached — only downloads once per unique URL
@st.cache_data
def get_data(url):
    return pd.read_csv(url)  # 5 seconds first time, instant after

df = get_data("https://example.com/large_data.csv")
st.dataframe(df)  # Fast on every rerun!
```

---

## 2. `st.cache_data` — For Data

### When to Use

Use `@st.cache_data` for functions that return **data**:
- DataFrame transformations
- Database queries
- API calls that return JSON
- File reads
- Any computation that returns pickleable data

### Basic Usage

```python
import streamlit as st
import pandas as pd

@st.cache_data
def load_data(file_path):
    """Load and preprocess data — cached by file_path."""
    df = pd.read_csv(file_path)
    df["date"] = pd.to_datetime(df["date"])
    return df

# First call: executes function
df = load_data("sales.csv")  # Runs (cache miss)

# Second call: returns cached result
df2 = load_data("sales.csv")  # Instant (cache hit)

# Different argument: executes again
df3 = load_data("customers.csv")  # Runs (different URL)
```

### Key Behavior: Returns Copies

**Critical:** `@st.cache_data` returns **copies** of cached objects. Each caller gets their own independent copy.

```python
@st.cache_data
def get_data():
    return {"count": 0}

data1 = get_data()
data2 = get_data()

data1["count"] = 10
print(data2["count"])  # Still 0! (separate copy)
```

This prevents side effects between users but means modifications don't persist.

---

## 3. `st.cache_resource` — For Resources

### When to Use

Use `@st.cache_resource` for functions that return **shared resources**:
- Database connections
- ML models
- File handles
- API clients
- Any object that should be shared, not copied

### Basic Usage

```python
import streamlit as st
from sqlalchemy import create_engine

@st.cache_resource
def get_database_engine():
    """Create database engine — shared across all users."""
    return create_engine("sqlite:///data.db")

engine = get_database_engine()  # Created once, shared everywhere
```

### Key Behavior: Returns Same Object

**Critical:** `@st.cache_resource` returns the **same object** to all callers (singleton pattern).

```python
@st.cache_resource
def get_model():
    return load_my_model()

model1 = get_model()
model2 = get_model()

print(model1 is model2)  # True! Same object
```

### Thread Safety Warning

Global resources must be thread-safe. If your resource isn't thread-safe:

```python
# Option 1: Session-scoped (one per user)
@st.cache_resource(scope="session")
def get_session_model():
    return load_model()

# Option 2: Use session_state
if "model" not in st.session_state:
    st.session_state.model = load_model()
```

---

## 4. When to Use Which?

| Aspect | `st.cache_data` | `st.cache_resource` |
|--------|-----------------|---------------------|
| **Return value** | Copies | Same object (singleton) |
| **Use for** | Data, queries, transforms | Connections, models, clients |
| **Mutable?** | Each caller has own copy | Shared, can mutate |
| **Thread safety** | Not required | Required (global scope) |
| **Pickleable?** | Yes (required) | Not required |

### Decision Tree

```
What does your function return?
    │
    ├── Data (DataFrame, dict, list, number)
    │       → @st.cache_data
    │
    └── Resource (connection, model, client)
            → @st.cache_resource
```

---

## 5. Cache Parameters

### TTL (Time-to-Live)

Control how long cached values persist:

```python
# Never expires (default)
@st.cache_data
def get_data():
    ...

# Expires after 1 hour
@st.cache_data(ttl=3600)
def get_daily_data():
    ...

# Expires after 1 day (string format)
@st.cache_data(ttl="1D")
def get_weekly_report():
    ...

# Using timedelta
from datetime import timedelta
@st.cache_data(ttl=timedelta(minutes=30))
def get_realtime_data():
    ...
```

### Max Entries

Limit cache size:

```python
# Keep only last 100 entries
@st.cache_data(max_entries=100)
def process_item(item_id):
    ...
```

### Show Spinner

Control spinner display:

```python
# Default: shows spinner on cache miss
@st.cache_data
def load_data():
    ...

# Custom spinner text
@st.cache_data(show_spinner="Loading data...")
def load_data():
    ...

# No spinner
@st.cache_data(show_spinner=False)
def quick_load():
    ...

# Show elapsed time (since 1.60+)
@st.cache_data(show_time=True)
def load_data():
    ...
```

### Scope

Control cache scope:

```python
# Global (shared across all users, default)
@st.cache_data(scope="global")
def get_public_data():
    ...

# Session (per-user, cleared on disconnect)
@st.cache_data(scope="session")
def get_user_data(user_id):
    ...
```

### Refresh Mode

Control TTL expiration behavior:

```python
# Foreground (default): waits for refresh
@st.cache_data(ttl=3600, refresh_mode="foreground")
def get_data():
    ...

# Background: returns stale value, refreshes async
@st.cache_data(ttl=3600, refresh_mode="background")
def get_data():
    ...
```

### Persistence

Save cache to disk:

```python
# Persist to disk (survives server restart)
@st.cache_data(persist="disk")
def get_data():
    ...

# Persist with TTL (note: TTL ignored with persist)
@st.cache_data(persist="disk", ttl=3600)
def get_data():
    ...
```

---

## 6. Cache Invalidation

### Automatic Invalidation

Streamlit invalidates cache when:
1. Function source code changes
2. Arguments change
3. TTL expires
4. `max_entries` exceeded (oldest removed)
5. Manual clear via `func.clear()`

### Manual Invalidation

```python
@st.cache_data
def load_data(source):
    return pd.read_csv(source)

# Clear specific entry
load_data.clear("data1.csv")

# Clear all entries for this function
load_data.clear()

# Clear ALL caches (all functions)
st.cache_data.clear()
```

### Using Underdash for Non-Hashable Arguments

Arguments starting with `_` are excluded from hashing:

```python
@st.cache_data
def query_data(_db_connection, query):
    """_db_connection won't affect cache key."""
    return pd.read_sql(query, _db_connection)

# These return cached result (same query, different connection)
conn1 = get_connection()
conn2 = get_connection()
df1 = query_data(conn1, "SELECT * FROM users")  # Runs
df2 = query_data(conn2, "SELECT * FROM users")  # Cached!
```

---

## 7. Custom Hash Functions

Override default hashing for complex objects:

```python
import streamlit as st
import datetime

@st.cache_data(hash_funcs={datetime.datetime: lambda dt: dt.isoformat()})
def get_data_by_date(dt):
    """Cache by datetime, using ISO format for hashing."""
    return fetch_data(dt)

# Alternative: use fully-qualified name
@st.cache_data(hash_funcs={"datetime.datetime": lambda dt: dt.isoformat()})
def get_data_by_date(dt):
    ...
```

---

## 8. Common Caching Mistakes

### Mistake 1: Caching Mutable Returns

```python
# ⚠️ WRONG: Mutating cached data affects all users!
@st.cache_data
def get_data():
    return pd.DataFrame({"a": [1, 2, 3]})

df = get_data()
df["b"] = df["a"] * 2  # This is fine (own copy)
# But be aware: each caller gets a fresh copy
```

Actually this is fine — `cache_data` returns copies. The mistake is thinking modifications persist.

### Mistake 2: Caching Non-Pickleable Objects

```python
# ❌ WRONG: Database connection isn't pickleable
@st.cache_data
def get_connection():
    return sqlite3.connect("data.db")

# ✅ CORRECT: Use cache_resource for resources
@st.cache_resource
def get_connection():
    return sqlite3.connect("data.db")
```

### Mistake 3: Not Considering User Isolation

```python
# ⚠️ DANGER: Returns same data to all users
@st.cache_data
def get_user_profile(user_id):
    return db.get_user(user_id)

# ✅ BETTER: Use session scope for user-specific data
@st.cache_data(scope="session")
def get_user_profile(user_id):
    return db.get_user(user_id)
```

### Mistake 4: Missing TTL for Fresh Data

```python
# ⚠️ Stale data forever
@st.cache_data
def get_stock_price():
    return api.get_price("AAPL")

# ✅ Better: Set appropriate TTL
@st.cache_data(ttl=60)  # Refresh every minute
def get_stock_price():
    return api.get_price("AAPL")
```

---

## 9. Performance Measurement

### Using `show_time`

```python
@st.cache_data(show_time=True)
def expensive_computation(n):
    return sum(i**2 for i in range(n))

result = expensive_computation(1_000_000)
# Shows elapsed time next to spinner
```

### Manual Timing

```python
import time

def measure(func, *args, **kwargs):
    start = time.time()
    result = func(*args, **kwargs)
    elapsed = time.time() - start
    return result, elapsed

# Compare cached vs uncached
data1, t1 = measure(load_data_uncached, "data.csv")
data2, t2 = measure(load_data_cached, "data.csv")
st.write(f"Uncached: {t1:.2f}s, Cached: {t2:.4f}s")
```

---

## 10. Caching Patterns

### Pattern 1: Data Loading Pipeline

```python
import streamlit as st
import pandas as pd

@st.cache_data(ttl=3600, show_spinner="Loading data...")
def load_raw_data(url):
    """Load raw data — expensive I/O."""
    return pd.read_csv(url)

@st.cache_data
def clean_data(df):
    """Clean data — depends on input, cached automatically."""
    df = df.dropna()
    df["date"] = pd.to_datetime(df["date"])
    return df

@st.cache_data
def aggregate_data(df, group_col):
    """Aggregate data — cached per group column."""
    return df.groupby(group_col).agg({"value": "sum"})

# Pipeline
raw = load_raw_data("data.csv")
cleaned = clean_data(raw)
summary = aggregate_data(cleaned, "category")
```

### Pattern 2: Model Loading

```python
import streamlit as st

@st.cache_resource
def load_model(model_name):
    """Load ML model — shared resource, loaded once."""
    import joblib
    return joblib.load(f"models/{model_name}.joblib")

model = load_model("classifier_v2")

if st.button("Predict"):
    prediction = model.predict(input_features)
    st.write(f"Prediction: {prediction}")
```

### Pattern 3: Database Connection

```python
import streamlit as st
from sqlalchemy import create_engine, text

@st.cache_resource
def get_engine():
    """Create database engine — singleton resource."""
    return create_engine(st.secrets["DATABASE_URL"])

@st.cache_data(ttl=300)
def run_query(query):
    """Execute query — results cached for 5 minutes."""
    engine = get_engine()
    with engine.connect() as conn:
        return pd.read_sql(text(query), conn)
```

---

## 11. Best Practices

### Do's

1. **Cache expensive operations** — I/O, computations, API calls
2. **Choose the right decorator** — `cache_data` for data, `cache_resource` for resources
3. **Set TTL for real-time data** — avoid serving stale data
4. **Use `max_entries`** — limit memory usage for large caches
5. **Clear caches manually when needed** — provide UI for users to refresh
6. **Measure performance** — use `show_time=True` or manual timing

### Don'ts

1. **Don't cache side effects** — logging, email, database writes
2. **Don't cache non-deterministic functions** — random number generators
3. **Don't cache user-specific data globally** — use `scope="session"`
4. **Don't forget pickleability** — `cache_data` requires pickleable returns
5. **Don't over-cache** — not everything needs caching

---

## 12. Learning vs. Production

### Learning Environment

```python
# Simple caching — fine for learning
@st.cache_data
def load_data(url):
    return pd.read_csv(url)
```

### Production Considerations

```python
# Production-ready caching
@st.cache_data(
    ttl=300,           # Refresh every 5 minutes
    max_entries=10,    # Limit memory
    show_spinner="Loading...",
    persist="disk",    # Survive restarts
    show_time=True     # Monitor performance
)
def load_data(url):
    """Load data with production settings."""
    df = pd.read_csv(url)
    st.info(f"Loaded {len(df)} rows")  # Show on first load
    return df

# Provide manual refresh
if st.button("🔄 Refresh Data"):
    load_data.clear()
    st.rerun()
```

---

## Key Takeaways

- **`@st.cache_data`** caches data (returns copies) — use for DataFrames, queries, transforms
- **`@st.cache_resource`** caches resources (returns same object) — use for connections, models
- **TTL controls freshness** — set appropriate expiration for time-sensitive data
- **Manual clearing** — `func.clear()` and `st.cache_data.clear()` for on-demand refresh
- **Performance monitoring** — use `show_time=True` to measure cache effectiveness
- **Choose wisely** — wrong decorator = bugs (non-pickleable returns, shared state issues)

---

## Further Reading

- [Streamlit Caching Overview](https://docs.streamlit.io/develop/concepts/architecture/caching)
- [st.cache_data](https://docs.streamlit.io/develop/api-reference/caching-and-state/st.cache_data)
- [st.cache_resource](https://docs.streamlit.io/develop/api-reference/caching-and-state/st.cache_resource)

---

## Related Materials

- 📓 Notebook: [12 — Caching & Performance](../notebooks/12_caching_performance.ipynb)
- ✏️ Exercise: [12 — Caching Workshop](../exercises/12_caching_workshop.py)
- 🖥️ Demo App: [12 — Caching Performance Demo](../apps/12_caching_performance_demo.py)
- 📝 Quiz: [08 — Caching & Performance](../quizzes/08_caching_performance.md)
