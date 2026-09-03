# Quiz 16 — Production, Maintenance & Monitoring

> **📝 Post-Quiz · Module 16 · Production**
> *Test your understanding of production deployment, monitoring, and maintenance.*
> ⏱ Time: 15 minutes · 📊 Points: 25 · Bloom's: Evaluate, Create

---

## Part A: Multiple Choice (2 points each)

### Q1. Your app works locally but shows a white page on Community Cloud. What is the FIRST thing to check?

(a) Clear browser cache
(b) Check deployment logs on Community Cloud
(c) Restart the app
(d) Push a new commit

**CLO:** CLO11

---

### Q2. Which is the correct order for a deployment workflow?

(a) Deploy → Test → Commit → Push
(b) Test → Commit → Push → Deploy
(c) Commit → Push → Deploy → Test
(d) Push → Deploy → Commit → Test

**CLO:** CLO11

---

### Q3. What does "app sleep" mean on Community Cloud?

(a) The app shuts down permanently
(b) The app pauses after inactivity and restarts on next visit
(c) The app runs at reduced speed
(d) The app stops accepting new users

**CLO:** CLO11

---

### Q4. Which is NOT a reason to use `@st.cache_data`?

(a) Database query that takes 10 seconds
(b) Generating a random UUID per session
(c) Loading a large CSV file
(d) Computing a heavy aggregation

**CLO:** CLO5, CLO11

---

## Part B: True/False (1 point each)

### Q5. You should commit `.streamlit/secrets.toml` to your repository.

**CLO:** CLO10

---

### Q6. Community Cloud automatically redeploys when you push to GitHub.

**CLO:** CLO11

---

### Q7. `requirements.txt` is optional for Community Cloud deployment.

**CLO:** CLO11

---

## Part C: Short Answer (3 points each)

### Q8. A user reports your deployed app is "very slow." List 3 strategies to diagnose and fix the performance issue.

**CLO:** CLO5, CLO11

---

### Q9. Explain why `st.set_page_config()` must be the first Streamlit call and what happens if it's not.

**CLO:** CLO1

---

### Q10. You need to store an OpenAI API key in your deployed app. Describe the correct way to do this, including where the key is stored and how it's accessed in code.

**CLO:** CLO10, CLO11

---

## Part D: Debugging (4 points each)

### Q11. This app is deployed but crashes with `FileNotFoundError`. Find and fix ALL issues:

```python
import streamlit as st
import pandas as pd

df = pd.read_csv("data/sales.csv")
st.dataframe(df.head())
```

**CLO:** CLO11

---

### Q12. This app shows stale data after the user adds a new record to the database. Find and fix the caching issue:

```python
@st.cache_resource
def get_db():
    return sqlite3.connect("app.db")

def add_record(name, value):
    conn = get_db()
    conn.execute("INSERT INTO records VALUES (?, ?)", (name, value))
    conn.commit()

# Display records
conn = get_db()
df = pd.read_sql("SELECT * FROM records", conn)
st.dataframe(df)
```

**CLO:** CLO5, CLO11

---

## Part E: Architecture (5 points)

### Q13. You are deploying a Streamlit app that processes uploaded CSV files, runs ML predictions, and displays results. Design the deployment-ready architecture including:
1. File structure
2. requirements.txt contents
3. .gitignore entries
4. Error handling strategy
5. Performance optimization

**CLO:** CLO6, CLO11, CLO12

---

## Answer Key

> ⚠️ **Instructor copy**

| Q | Answer | Explanation | Bloom's |
|---|--------|-------------|---------|
| Q1 | **(b)** | Logs contain the actual error. Always check logs first. | Evaluate |
| Q2 | **(b)** | Test locally → Commit → Push → Deploy. | Evaluate |
| Q3 | **(b)** | Apps pause after inactivity; first visit triggers cold start (30-60s). | Understand |
| Q4 | **(b)** | UUIDs should be unique per session, not cached across sessions. | Analyze |
| Q5 | **False** | Secrets must NEVER be committed. Use `.gitignore` and Community Cloud settings. | Evaluate |
| Q6 | **True** | Pushing to the deployment branch triggers auto-redeploy. | Understand |
| Q7 | **False** | `requirements.txt` is REQUIRED — Community Cloud won't build without it. | Understand |
| Q8 | 1) Check logs for errors. 2) Add `@st.cache_data` to expensive computations. 3) Reduce `requirements.txt` dependencies. 4) Use lazy imports for heavy packages. | Evaluate |
| Q9 | `st.set_page_config()` sets page title, icon, layout. It must be first because Streamlit needs to know the page configuration before rendering any content. If called later, it raises an exception. | Understand |
| Q10 | Store in `.streamlit/secrets.toml` locally (gitignored). On Community Cloud: app settings → Secrets → paste TOML. Access in code: `st.secrets["openai"]["api_key"]`. Never hardcode. | Evaluate |
| Q11 | Issue 1: `data/sales.csv` may not exist on Community Cloud. Issue 2: No error handling. Fix: Use generated data or commit the file, add try/except. | Evaluate |
| Q12 | After `add_record()`, the cached connection returns stale data. Fix: Call `get_db.clear()` after any write operation to invalidate the cache. | Evaluate |
| Q13 | Files: app.py, model_utils.py, data_processing.py, config.py. requirements.txt: streamlit, pandas, numpy, scikit-learn, joblib. .gitignore: secrets.toml, __pycache__, *.joblib. Error handling: try/except on file ops, validate uploads. Performance: @st.cache_resource for model, @st.cache_data for processing. | Create |

---

## CLO Mapping

| CLO | Questions |
|-----|-----------|
| CLO1 — Explain core concepts | Q9 |
| CLO5 — Optimize performance | Q4, Q8, Q12 |
| CLO6 — Design well-architected apps | Q13 |
| CLO10 — Test and secure apps | Q5, Q10 |
| CLO11 — Deploy to production | Q1–Q13 |
| CLO12 — Execute full lifecycle | Q13 |

---

## Related Materials

- 📖 Reading: [Deployment Guide](../readings/deployment_guide.md)
- 📖 Reading: [Security](../readings/security_and_secrets.md)
- 📓 Notebook: [Deployment Tutorial](../notebooks/deployment_tutorial.ipynb)
- ✏️ Exercise: [16 — Production Ready](../exercises/16_production_ready.py)
- 📋 Checklist: [Deployment Checklist](../docs/deployment_checklist.md)
