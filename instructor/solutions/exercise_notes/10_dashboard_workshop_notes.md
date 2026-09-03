# Exercise 10 — Dashboard Workshop: Solution Notes

> **👩‍🏫 Instructor Reference**
> *Expected approach, key code, and grading guidance.*

---

## Step 1: Data Generation

### Expected Approach
- `@st.cache_data` decorated function
- Product-dependent base prices
- Derived columns (revenue = price × quantity, cost, profit)

### Key Code
```python
@st.cache_data
def generate_sales_data(n_rows=1500):
    np.random.seed(42)
    dates = pd.date_range("2024-01-01", periods=365, freq="D")
    base_prices = {"Laptop": 1200, "Phone": 800, "Tablet": 500, "Headphones": 150, "Monitor": 400}

    data = []
    for _ in range(n_rows):
        product = np.random.choice(["Laptop", "Phone", "Tablet", "Headphones", "Monitor"])
        unit_price = base_prices[product] * np.random.uniform(0.8, 1.2)
        quantity = np.random.randint(1, 10)
        revenue = round(unit_price * quantity, 2)
        cost = round(revenue * np.random.uniform(0.4, 0.7), 2)
        data.append({
            "date": np.random.choice(dates),
            "product": product,
            "region": np.random.choice(["North America", "Europe", "Asia Pacific", "Latin America"]),
            "segment": np.random.choice(["Consumer", "Corporate", "Home Office"]),
            "unit_price": round(unit_price, 2),
            "quantity": quantity,
            "revenue": revenue,
            "cost": cost,
            "profit": round(revenue - cost, 2),
        })
    return pd.DataFrame(data)
```

### Common Mistakes
- Missing `@st.cache_data` decorator
- Not using `np.random.seed(42)` (non-reproducible)
- Wrong derived column formulas

---

## Step 2: Data Functions (No Streamlit Calls)

### Expected Approach
Pure functions with no `st.*` calls — critical for testability and caching.

### Key Code
```python
def filter_data(df, regions, products, segments, date_range):
    result = df.copy()
    if regions:
        result = result[result["region"].isin(regions)]
    if products:
        result = result[result["product"].isin(products)]
    if segments:
        result = result[result["segment"].isin(segments)]
    if date_range and len(date_range) == 2:
        start, end = pd.Timestamp(date_range[0]), pd.Timestamp(date_range[1])
        result = result[(result["date"] >= start) & (result["date"] <= end)]
    return result

def compute_kpis(df):
    total_revenue = df["revenue"].sum()
    total_profit = df["profit"].sum()
    total_orders = len(df)
    return {
        "total_revenue": total_revenue,
        "total_profit": total_profit,
        "total_orders": total_orders,
        "avg_order_value": total_revenue / total_orders if total_orders > 0 else 0,
        "profit_margin": (total_profit / total_revenue * 100) if total_revenue > 0 else 0,
    }
```

### Common Mistakes
- Putting `st.write()` inside data functions
- Not handling empty DataFrames in `compute_kpis`
- Division by zero in profit_margin calculation

### Grading Notes (20 marks)
- Full marks: Both functions work, no st.* calls, edge cases handled
- 15 marks: Functions work but missing edge case handling
- 10 marks: Functions work but have st.* calls

---

## Step 3: Sidebar Filters

### Expected Approach
- Date range, multiselects for region/product/segment
- Radio for chart type, checkbox for moving average
- All controls in `st.sidebar`

### Common Mistakes
- Not setting defaults to all unique values
- Missing `st.sidebar.divider()` between sections
- Using `st.selectbox` instead of `st.multiselect` for multi-select filters

---

## Steps 4-6: Filter Application, KPIs, Charts, Export

### Expected Approach
1. Apply filters → check empty state → show warning or continue
2. Display 5 KPI metric cards
3. Choose chart type based on radio selection
4. Add 7-day moving average if checkbox checked
5. Export filtered data as CSV

### Key Pattern for Moving Average
```python
if show_trend:
    daily = filtered.groupby("date")["revenue"].sum().reset_index()
    daily["ma7"] = daily["revenue"].rolling(7, min_periods=1).mean()
    st.line_chart(daily.set_index("date")[["revenue", "ma7"]])
```

### Grading Notes (Total: 100 marks for this exercise)
- Steps 1-2: 30 marks (data gen + functions)
- Steps 3-4: 25 marks (filters + empty state)
- Steps 5-6: 25 marks (KPIs + charts)
- Export + polish: 20 marks
