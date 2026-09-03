# Exercise 12 — Caching Workshop: Solution Notes

> **👩‍🏫 Instructor Reference**
> *Expected approach, key code, and grading guidance.*

---

## Challenge 1: Cached Data Loader

### Expected Approach
`@st.cache_data` decorated function with simulated I/O delay. Performance tracking with manual timing or `show_time`.

### Key Code
```python
@st.cache_data(show_spinner=False)
def load_data(n_rows):
    time.sleep(1)  # Simulate I/O
    np.random.seed(42)
    return pd.DataFrame({
        "category": np.random.choice(["A", "B", "C"], n_rows),
        "value": np.random.randn(n_rows) * 10 + 50,
        "quantity": np.random.randint(1, 50, n_rows),
    })

n_rows = st.slider("Rows", 100, 5000, 1000)

start = time.time()
with st.spinner("Loading data..."):
    df = load_data(n_rows)
elapsed = time.time() - start

st.write(f"Loaded in **{elapsed:.3f}s**")
st.dataframe(df.head())
```

### Common Mistakes
- Not decorating with `@st.cache_data`
- Using `time.sleep` inside cached function (runs only on cache miss)
- Not passing parameters that affect the cached result

### Grading Notes (20 marks)
- Full marks: Caching works, performance tracked, slider controls size
- 14 marks: Caching works but no performance tracking
- 7 marks: Function works but not cached

---

## Challenge 2: Model Registry

### Expected Approach
`@st.cache_resource` for models (singletons). Show cached models, allow clearing specific entries.

### Key Code
```python
@st.cache_resource
def load_model(model_name):
    time.sleep(2)  # Simulate loading
    return {
        "name": model_name,
        "accuracy": np.random.uniform(0.75, 0.95),
        "loaded_at": datetime.now().isoformat(),
    }

model_name = st.selectbox("Model", ["random_forest", "gradient_boost", "neural_net"])

if st.button("Load Model"):
    model = load_model(model_name)
    st.success(f"Loaded: {model['name']} (accuracy: {model['accuracy']:.2%})")

# Show cached entries
if load_model.cache_info():
    st.write(f"Cached models: {load_model.cache_info().currsize}")

if st.button("Clear All Model Cache"):
    load_model.clear()
    st.success("Cache cleared")
```

### Common Mistakes
- Using `cache_data` instead of `cache_resource` for models
- Not understanding that `cache_resource` returns the SAME object
- Forgetting `.clear()` for cache invalidation

---

## Challenge 3: Query Cache with Stats

### Expected Approach
Track hits/misses in session_state. Compare total queries before and after to detect cache hits.

### Key Code
```python
@st.cache_data(ttl=60)
def execute_query(query_text):
    time.sleep(0.5)  # Simulate DB query
    np.random.seed(hash(query_text) % 2**31)
    return pd.DataFrame({
        "result": np.random.randint(1, 100, 5),
        "label": [f"Row {i}" for i in range(5)],
    })

if "stats" not in st.session_state:
    st.session_state.stats = {"total": 0, "hits": 0}

query = st.text_area("SQL Query", "SELECT * FROM users")

if st.button("Execute"):
    before = execute_query.cache_info().currsize
    result = execute_query(query)
    after = execute_query.cache_info().currsize

    st.session_state.stats["total"] += 1
    if after == before:  # No new entry = cache hit
        st.session_state.stats["hits"] += 1

    st.dataframe(result)

hits = st.session_state.stats["hits"]
total = st.session_state.stats["total"]
st.write(f"**Hits:** {hits}/{total} ({hits/total*100:.0f}%)")
```

---

## Challenge 4: TTL Comparison

### Expected Approach
Three functions with different TTL values. Display current time vs cached time.

### Key Code
```python
@st.cache_data(ttl=5)
def get_fast_data():
    return datetime.now().strftime("%H:%M:%S")

@st.cache_data(ttl=30)
def get_medium_data():
    return datetime.now().strftime("%H:%M:%S")

@st.cache_data  # No TTL
def get_slow_data():
    return datetime.now().strftime("%H:%M:%S")

col1, col2, col3 = st.columns(3)
with col1:
    st.write(f"**Fast (5s TTL):** {get_fast_data()}")
with col2:
    st.write(f"**Medium (30s TTL):** {get_medium_data()}")
with col3:
    st.write(f"**No TTL:** {get_slow_data()}")

if st.checkbox("Auto-refresh every 2s"):
    import time
    time.sleep(2)
    st.rerun()
```

---

## Challenge 5: Pipeline Cache

### Expected Approach
Three cached stages: generate → clean → aggregate. Each cached independently so intermediate results persist.

### Key Code
```python
@st.cache_data
def generate_data(n):
    return pd.DataFrame({
        "category": np.random.choice(["A", "B", "C"], n),
        "value": np.random.randn(n) * 10 + 50,
    })

@st.cache_data
def clean_data(df):
    df = df.dropna()
    df["value_z"] = (df["value"] - df["value"].mean()) / df["value"].std()
    return df

@st.cache_data
def aggregate_data(df, group_by):
    return df.groupby(group_by)["value"].agg(["mean", "std", "count"])

n = st.slider("Rows", 100, 5000, 1000)
group_by = st.selectbox("Group by", ["category"])

start = time.time()
raw = generate_data(n)
t1 = time.time()
cleaned = clean_data(raw)
t2 = time.time()
result = aggregate_data(cleaned, group_by)
t3 = time.time()

st.write(f"Generate: {t1-start:.3f}s · Clean: {t2-t1:.3f}s · Aggregate: {t3-t2:.3f}s")
st.dataframe(result)
```

### Grading Notes (20 marks)
- Full marks: All 3 stages cached independently, timing shown
- 14 marks: Pipeline works but timing or caching partial
- 7 marks: Basic pipeline works but no caching
