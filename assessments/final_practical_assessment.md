# Final Practical Assessment

> **🎯 Final Practical · Week 15 · End of Course**
> *Comprehensive practical assessment: build and deploy a complete data application.*
> ⏱ Duration: 4 hours · 📊 Total: 150 marks · Difficulty: ★★★★★

---

## Course Information

| Field | Detail |
|-------|--------|
| **Course** | Streamlit for Data Science |
| **Assessment** | Final Practical Examination |
| **Weight** | 15% of course grade |
| **Duration** | 4 hours (240 minutes) |
| **Type** | Individual, supervised, deployed |
| **Environment** | Local machine + Community Cloud account |

---

## Learning Outcomes Assessed

| CLO | Outcome | Bloom's | Marks |
|-----|---------|---------|-------|
| CLO2 | Build interactive data applications | Apply | 20 |
| CLO3 | Implement data visualization | Apply | 15 |
| CLO4 | Manage application state | Apply | 15 |
| CLO5 | Optimize performance | Analyze | 10 |
| CLO6 | Design well-structured applications | Analyze | 15 |
| CLO7 | Connect to data sources | Apply | 10 |
| CLO8 | Deploy ML models | Apply | 20 |
| CLO10 | Apply testing and security | Evaluate | 15 |
| CLO11 | Deploy to production | Evaluate | 20 |
| CLO12 | Execute full development lifecycle | Create | 10 |
| **Total** | | | **150** |

---

## Instructions

1. You have **4 hours** to build, test, and deploy a complete application
2. You may use **official documentation** (offline copies provided)
3. You may **NOT** access the internet except for deploying to Community Cloud
4. You may **NOT** use previously submitted code from assignments or exercises
5. The app must be **deployed and accessible via URL** at submission
6. All code must be in a git repository
7. **Submit** the GitHub repository URL and deployment URL

---

## Scenario

You are a Data Scientist at an e-commerce company. The VP of Analytics wants a **Customer Analytics Dashboard** that the business team can use daily. The dashboard must:

1. Load and display e-commerce transaction data
2. Allow interactive filtering and exploration
3. Show KPI metrics and trends
4. Include a customer segmentation model
5. Support batch analysis
6. Be deployed and accessible to the team

---

## Dataset

Create a synthetic e-commerce dataset:

```python
# exam_dataset.py
import pandas as pd
import numpy as np

np.random.seed(42)
n = 2000

customers = pd.DataFrame({
    "customer_id": [f"C{i:04d}" for i in range(1, n+1)],
    "age": np.random.randint(18, 70, n),
    "gender": np.random.choice(["M", "F", "Other"], n, p=[0.45, 0.45, 0.1]),
    "total_purchases": np.random.randint(1, 100, n),
    "avg_order_value": np.random.uniform(10, 500, n).round(2),
    "days_since_last_purchase": np.random.randint(1, 365, n),
    "customer_segment": np.random.choice(["Premium", "Regular", "New", "At-Risk"], n, p=[0.15, 0.45, 0.25, 0.15]),
    "region": np.random.choice(["North", "South", "East", "West"], n),
})

transactions = pd.DataFrame({
    "transaction_id": [f"T{i:05d}" for i in range(1, 5001)],
    "customer_id": np.random.choice(customers["customer_id"], 5000),
    "date": pd.date_range("2024-01-01", periods=5000, freq="4h"),
    "amount": np.random.uniform(5, 1000, 5000).round(2),
    "category": np.random.choice(["Electronics", "Clothing", "Food", "Books", "Sports"], 5000),
})
```

---

## Tasks

### Task 1: Data Architecture (15 marks)

1. (5 marks) **File structure:** Create a clean, modular application:
   - `app.py` — Entry point with navigation
   - `config.py` — Constants and settings
   - `data_loader.py` — Data loading and processing functions
   - `components.py` — Reusable UI components
   - `pages/` — Individual page modules

2. (5 marks) **Data functions:** Write pure data functions (no `st.*` calls):
   - `load_customers()` — with `@st.cache_data`
   - `load_transactions()` — with `@st.cache_data`
   - `compute_segment_stats(df)` — returns aggregated stats
   - `compute_trends(df, period)` — returns time-series data

3. (5 marks) **Configuration:** Centralize settings in `config.py`:
   - App title, icon, layout
   - Dataset paths
   - Chart color scheme
   - Feature names for ML

---

### Task 2: Interactive Dashboard (25 marks)

1. (8 marks) **Sidebar filters:**
   - Customer segment (multiselect)
   - Region (multiselect)
   - Date range (date_input)
   - Purchase amount range (slider)
   - "Apply Filters" button in a form

2. (8 marks) **KPI Metrics:**
   - Total Customers, Total Revenue, Avg Order Value, Retention Rate
   - Display in 4-column layout with deltas
   - Metrics update with filter changes

3. (9 marks) **Tabbed visualization:**
   - "Overview": Revenue trend line chart + category bar chart
   - "Customers": Segment distribution + regional heatmap
   - "Transactions": Daily volume + amount distribution
   - Use Plotly for at least 2 charts

---

### Task 3: Customer Segmentation Model (25 marks)

1. (8 marks) **Model training:**
   - Use KMeans clustering (or provided sklearn model)
   - Features: total_purchases, avg_order_value, days_since_last_purchase
   - Determine optimal k using elbow method or silhouette score
   - Save model and scaler with joblib

2. (10 marks) **Single prediction:**
   - Input widgets for customer features
   - Predict segment assignment
   - Show predicted segment with confidence
   - Display similar customers from the dataset

3. (7 marks) **Batch analysis:**
   - Upload CSV of new customers
   - Assign segments to all
   - Show segment distribution
   - Download results with segment column

---

### Task 4: Testing & Security (15 marks)

1. (5 marks) **Testing:**
   - At least 2 unit tests for data functions (using pytest)
   - At least 1 `st.testing.AppTest` test for app loading
   - Tests pass: `pytest tests/ -v`

2. (5 marks) **Security:**
   - No hardcoded secrets in source
   - `.gitignore` includes secrets, __pycache__, model files
   - Input validation on all user inputs
   - File upload validation (type, size, columns)

3. (5 marks) **Error handling:**
   - Graceful failure for missing data
   - User-friendly error messages
   - App doesn't crash on edge cases

---

### Task 5: Deployment (20 marks)

1. (5 marks) **Deployment preparation:**
   - `requirements.txt` at repo root
   - Entry point file correct
   - All files committed to git
   - README with description and setup instructions

2. (10 marks) **Community Cloud deployment:**
   - App deployed and accessible via URL
   - All features work in deployed version
   - No hardcoded paths or secrets
   - App loads within 30 seconds

3. (5 marks) **Post-deployment:**
   - Deployment URL provided
   - Screenshot of deployed app in README
   - App handles Community Cloud environment correctly

---

### Task 6: Documentation & Polish (15 marks)

1. (5 marks) **README.md:**
   - Project title and description
   - Features list
   - Setup and deployment instructions
   - Screenshots (at least 3)
   - Architecture diagram (text-based is fine)

2. (5 marks) **Code quality:**
   - Functions with docstrings
   - Type hints on function signatures
   - Consistent naming conventions
   - No commented-out code

3. (5 marks) **UX polish:**
   - Consistent styling throughout
   - Loading spinners for slow operations
   - Clear labels and descriptions
   - Professional appearance

---

### Task 7: Architecture Decision Record (15 marks)

Write a brief (1-page) architecture decision record explaining:

1. (3 marks) **Why you chose your file structure** — what problem does it solve?

2. (3 marks) **Why you chose specific caching strategies** — which functions, why that decorator?

3. (3 marks) **How you handled state management** — what goes in session_state and why?

4. (3 marks) **What you would do differently with more time** — identify at least 2 improvements

5. (3 marks) **What you found most challenging** — honest reflection with technical detail

---

## Submission

### GitHub Repository
```
final_practical/
├── app.py
├── config.py
├── data_loader.py
├── components.py
├── requirements.txt
├── .gitignore
├── README.md
├── architecture_decision.md
├── pages/
│   ├── __init__.py
│   ├── dashboard.py
│   ├── customers.py
│   ├── predictions.py
│   └── reports.py
├── tests/
│   ├── __init__.py
│   ├── test_data_loader.py
│   └── test_app.py
├── models/
│   └── .gitkeep
└── screenshots/
    ├── dashboard.png
    ├── predictions.png
    └── deployed.png
```

### Submission Links
1. GitHub repository URL
2. Community Cloud deployment URL
3. Screenshot links in README

---

## Marking Guide

| Task | Marks | Bloom's | Key Criteria |
|------|-------|---------|--------------|
| 1. Data Architecture | 15 | Analyze | Clean structure, pure functions, config |
| 2. Interactive Dashboard | 25 | Apply | Filters, KPIs, charts, all update |
| 3. ML Model | 25 | Apply | Model works, single + batch prediction |
| 4. Testing & Security | 15 | Evaluate | Tests pass, no security issues |
| 5. Deployment | 20 | Evaluate | Deployed, works, no errors |
| 6. Documentation | 15 | Create | README, code quality, UX |
| 7. Architecture Decision | 15 | Evaluate, Create | Thoughtful reflection |
| **Total** | **150** | | |

---

## Grade Boundaries

| Grade | Score | Description |
|-------|-------|-------------|
| A | 130–150 | Exceptional: production-ready app, deployed, well-tested |
| B | 110–129 | Strong: complete app, most features, deployed |
| C | 90–109 | Good: working app, some gaps in testing/deployment |
| D | 70–89 | Adequate: partial app, basic functionality |
| F | < 70 | Insufficient: app doesn't work or major missing pieces |

---

## Common Mistakes to Avoid

1. ❌ Spending too long on ML, not enough on deployment
2. ❌ No tests (15 marks lost)
3. ❌ Not deploying (20 marks lost)
4. ❌ All code in one file (15 marks from architecture)
5. ❌ Charts don't update with filters
6. ❌ Missing requirements.txt (deployment fails)
7. ❌ Hardcoded secrets
8. ❌ No README or documentation

---

## Answer Key

> ⚠️ **Instructor copy — do not distribute**
> Reference implementation and grading rubric in `assessments/rubrics/final_practical_reference/`

---

## Related Materials

- 📋 Curriculum: [docs/curriculum.md](../docs/curriculum.md)
- 📋 Learning Outcomes: [docs/learning_outcomes.md](../docs/learning_outcomes.md)
- 📋 Deployment Checklist: [docs/deployment_checklist.md](../docs/deployment_checklist.md)
- ✏️ Exercise: [16 — Production Ready](../exercises/16_production_ready.py)
