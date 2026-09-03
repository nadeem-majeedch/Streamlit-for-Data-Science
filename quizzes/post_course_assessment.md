# Post-Course Assessment

> **📝 Post-Course Assessment · End of Course**
> *Measure learning gains by comparing with pre-course assessment results.*
> ⏱ Time: 30 minutes · 📊 Points: 50

---

## Purpose

This assessment mirrors the pre-course assessment structure. Compare your answers here with your pre-course responses to measure what you've learned. **It does not count toward your grade** — it's a self-reflection tool.

---

## Part A: Streamlit Fundamentals (10 points)

### A1. (2 pts) Explain Streamlit's execution model. What happens when a user clicks a widget?

---

### A2. (2 pts) Write a Streamlit app that:
1. Sets the page title to "My App"
2. Displays a heading
3. Shows a DataFrame with 3 rows
4. Has a sidebar with a selectbox

---

### A3. (2 pts) What is the difference between `st.write()` and `st.markdown()`? When would you use each?

---

### A4. (2 pts) Explain why `st.set_page_config()` must be the first Streamlit call.

---

### A5. (2 pts) A student reports that their Streamlit app shows "st.set_page_config can only be called once per page" error. What is the likely cause?

---

## Part B: Widgets & State (10 points)

### B1. (2 pts) Write a counter app using session state that:
1. Shows the current count as a metric
2. Has Increment, Decrement, and Reset buttons
3. Persists across reruns

---

### B2. (2 pts) Explain the difference between a widget's return value and its value in `st.session_state`.

---

### B3. (2 pts) Write a form that collects user feedback with:
- Rating (1–5 slider)
- Comment (text area)
- Submit button
- On submit: show the feedback as a formatted card

---

### B4. (2 pts) Explain what `@st.cache_data` does and when you would use it.

---

### B5. (2 pts) What is the difference between `@st.cache_data` and `@st.cache_resource`?

---

## Part C: Data & Visualization (10 points)

### C1. (2 pts) Write code to display a DataFrame with:
- Salary formatted as currency
- Date formatted as "YYYY-MM-DD"
- Hidden index

---

### C2. (2 pts) You have daily sales data for a year. Describe which chart type you would use and why.

---

### C3. (2 pts) Write a Plotly scatter plot showing the relationship between two numeric columns, colored by a categorical column.

---

### C4. (2 pts) Explain how you would filter a DataFrame based on sidebar widget selections.

---

### C5. (2 pts) Write code to add a download button that exports filtered data as CSV.

---

## Part D: Architecture & Deployment (10 points)

### D1. (2 pts) Draw the file structure for a multipage Streamlit app with database integration.

---

### D2. (2 pts) Explain how to properly handle secrets (API keys) in a deployed Streamlit app.

---

### D3. (2 pts) What are the minimum files needed for Community Cloud deployment?

---

### D4. (2 pts) A deployed app shows a white page. List 3 things to check and how to fix each.

---

### D5. (2 pts) Explain why parameterized SQL queries are important and show an example.

---

## Part E: ML & AI (10 points)

### E1. (2 pts) Explain the correct ML deployment pipeline from training to Streamlit prediction.

---

### E2. (2 pts) Why must you save the scaler alongside the model? What happens if you don't?

---

### E3. (2 pts) Write code for a single prediction interface that shows class probabilities.

---

### E4. (2 pts) What is RAG and why is it useful for LLM applications?

---

### E5. (2 pts) List 3 security best practices for a Streamlit application.

---

## Self-Reflection

After completing this assessment, compare your answers with your pre-course responses:

1. Which topics improved the most?
2. Which topics still need work?
3. What would you like to learn more about?

---

## Answer Key

> ⚠️ **Instructor copy**

<details>
<summary>Click to view answer key</summary>

### Part A

| Q | Answer |
|---|--------|
| A1 | Streamlit reruns the entire script top-to-bottom on every user interaction. When a widget is clicked, the script reruns and the widget returns its current value. |
| A2 | `st.set_page_config(page_title="My App"); st.header("Welcome"); st.dataframe(pd.DataFrame({"A":[1,2,3]})); st.sidebar.selectbox("Choose", ["X","Y"])` |
| A3 | `st.write()` auto-detects type (DataFrames, charts, text). `st.markdown()` renders Markdown specifically. Use `st.write()` for general output, `st.markdown()` for formatted text. |
| A4 | Streamlit needs to know page configuration before rendering any content. If called later, it raises an exception because the page is already being rendered. |
| A5 | `st.set_page_config()` was called more than once, or it wasn't the first Streamlit call in the script. |

### Part B

| Q | Answer |
|---|--------|
| B1 | Initialize `count` in session_state. Button handlers increment/decrement. Display with `st.metric("Count", st.session_state.count)`. |
| B2 | Return value: available only during the current rerun. session_state value: persists across reruns and can be accessed/modified anywhere in the script. |
| B3 | Form with `st.slider("Rating", 1, 5)`, `st.text_area("Comment")`, `st.form_submit_button("Submit")`. On submit, display formatted card. |
| B4 | `@st.cache_data` caches the return value based on function arguments. Used for expensive computations that should run once per unique input. |
| B5 | `cache_data` returns a COPY (safe for mutable data). `cache_resource` returns the SAME object (singleton for models/connections). |

### Part C

| Q | Answer |
|---|--------|
| C1 | `st.dataframe(df, hide_index=True, column_config={"Salary": st.column_config.NumberColumn(format="$%,.0f"), "Date": st.column_config.DateColumn(format="YYYY-MM-DD")})` |
| C2 | Line chart — best for showing trends over continuous time periods. Shows progression, seasonality, and anomalies clearly. |
| C3 | `fig = px.scatter(df, x="col1", y="col2", color="category"); st.plotly_chart(fig, use_container_width=True)` |
| C4 | Read widget values, apply boolean indexing: `filtered = df[(df["cat"].isin(selected)) & (df["val"] >= min_val)]` |
| C5 | `csv = filtered.to_csv(index=False); st.download_button("Download", csv, "data.csv", "text/csv")` |

### Part D

| Q | Answer |
|---|--------|
| D1 | `app.py` (entry point), `pages/` (home.py, entry.py, analysis.py, reports.py), `data_access.py` (CRUD), `config.py` (constants), `components.py` (UI). |
| D2 | Store in `.streamlit/secrets.toml` (gitignored). On Community Cloud: app settings → Secrets → paste TOML. Access: `st.secrets["key"]`. Never hardcode. |
| D3 | `app.py` (entry point) and `requirements.txt` (dependencies). Optional: `.streamlit/config.toml`, `README.md`. |
| D4 | 1) Check deployment logs. 2) Verify requirements.txt has all imports. 3) Ensure entry point file exists and runs locally. 4) Check for missing committed files. |
| D5 | Prevents SQL injection. `conn.execute("SELECT * FROM users WHERE name = ?", (name,))` — user input never enters the SQL string directly. |

### Part E

| Q | Answer |
|---|--------|
| E1 | Train model offline → save with joblib → create Streamlit app → load with @st.cache_resource → build input UI → apply saved preprocessing → predict → display results. |
| E2 | The scaler normalizes features using training statistics (mean, std). Without it, a new untrained scaler produces different values, causing wrong predictions. |
| E3 | Sliders for features, `model.predict()` and `model.predict_proba()`, display class and probability bar chart. |
| E4 | RAG = Retrieval-Augmented Generation. Retrieves relevant document chunks and injects them as context for the LLM. Useful for grounding responses in specific documents. |
| E5 | 1) Never hardcode secrets. 2) Use parameterized SQL queries. 3) Validate all user inputs. 4) Use .gitignore for sensitive files. 5) Enable XSRF protection. |

</details>

---

## Scoring Guide

| Score | Level | Description |
|-------|-------|-------------|
| 45–50 | Expert | Ready for professional data app development |
| 35–44 | Proficient | Strong command of core concepts |
| 25–34 | Developing | Solid foundation, room for growth |
| 15–24 | Beginning | Basic understanding, needs practice |
| Below 15 | Novice | Significant review needed |

---

## Related Materials

- 📋 Pre-Course Assessment: [quizzes/pre_course_assessment.md](pre_course_assessment.md)
- 📋 Question Bank: [quizzes/question_bank.md](question_bank.md)
- 📋 Final Quiz: [quizzes/final_comprehensive_quiz.md](final_comprehensive_quiz.md)
- 📋 Curriculum: [docs/curriculum.md](../docs/curriculum.md)
