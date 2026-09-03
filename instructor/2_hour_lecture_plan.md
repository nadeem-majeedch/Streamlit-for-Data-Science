# 🎓 Session Plans (90–120 Minutes)

> **Streamlit for Data Science — Learn, Build, Deploy**
> *Detailed lecture plans with time allocation, live coding, and student activities.*

---

## Session Template

Each session follows this structure:

| Time | Block | Description |
|------|-------|-------------|
| 0:00–0:05 | **Warm-up** | Recap, quiz, or discussion |
| 0:05–0:25 | **Concept** | Why, what, intuition |
| 0:25–0:50 | **Live Coding** | Build together in Streamlit |
| 0:50–0:55 | **Break** | — |
| 0:55–1:15 | **Guided Practice** | Students modify/extend the demo |
| 1:15–1:35 | **Independent Work** | Exercise or notebook |
| 1:35–1:45 | **Discussion** | Common mistakes, design decisions |
| 1:45–1:50 | **Wrap-up** | Preview, homework, Q&A |

---

## Session 01 — Streamlit Fundamentals (Week 1)

### Learning Objectives
- Explain what Streamlit is and why it's useful for Data Science
- Build and run a first Streamlit application
- Use text elements (title, header, markdown, caption)
- Understand the Streamlit rerun model

### Materials
- Reading: `readings/01_streamlit_introduction.md`
- Notebook: `notebooks/01_Streamlit_Introduction.ipynb`
- App: `apps/01_hello_streamlit.py`
- Exercise: `exercises/01_hello_streamlit.py`
- Quiz: `quizzes/01_fundamentals.md`

### Time Plan

| Time | Activity | Details |
|------|----------|---------|
| 0:00–0:05 | Warm-up | "What tools do you use for data analysis? What's frustrating about them?" |
| 0:05–0:15 | Motivation | Show Jupyter → Streamlit transformation. Show 3 real-world Streamlit apps. |
| 0:15–0:25 | Concept | What is Streamlit? How does it compare? The execution model (script runs top to bottom on every interaction). |
| 0:25–0:50 | Live Coding | **Build together:** `st.title`, `st.write`, `st.markdown`, `st.dataframe` with a sample dataset. Add `st.set_page_config`. Show the rerun behavior. |
| 0:50–0:55 | Break | — |
| 0:55–1:10 | Guided Practice | Students modify the demo app: change text, add a chart, display different data. |
| 1:10–1:30 | Independent Work | Start Exercise 01 (text elements + data display). |
| 1:30–1:40 | Discussion | "Why does Streamlit rerun the whole script? What are the implications?" |
| 1:40–1:50 | Wrap-up | Assign reading 01 + notebook 01. Preview: widgets next week. |

### Live Coding Script
```python
# Step 1: Create file hello.py
import streamlit as st

st.set_page_config(page_title="My First App", layout="wide")
st.title("Hello, Streamlit!")
st.write("This is my first Streamlit application.")

# Step 2: Add data
import pandas as pd
df = pd.DataFrame({"Name": ["Alice", "Bob", "Charlie"], "Score": [85, 92, 78]})
st.dataframe(df)

# Step 3: Show the rerun model
if st.button("Click me"):
    st.write("Button was clicked!")
# Explain: every interaction reruns the script
```

---

## Session 02 — Widgets & Input (Week 2)

### Learning Objectives
- Use all major Streamlit widget types
- Understand widget return values and keys
- Build an interactive form
- Connect widget output to application behavior

### Materials
- Reading: `readings/02_widgets_and_input.md`
- Notebook: `notebooks/02_widgets_and_input.ipynb`
- Exercise: `exercises/03_widget_mastery.py`
- Exercise: `exercises/04_dataset_filter_app.py`
- Quiz: `quizzes/02_widgets_input.md`

### Time Plan

| Time | Activity | Details |
|------|----------|---------|
| 0:00–0:05 | Warm-up | Quick quiz: "What happens when you click a widget in Streamlit?" |
| 0:05–0:20 | Concept | Widgets = inputs. Each returns a value. Keys = identity. Forms = batch submissions. |
| 0:20–0:50 | Live Coding | **Build a dataset filter:** `st.selectbox` for column, `st.slider` for range, `st.checkbox` for toggle. Show how filters connect to `st.dataframe`. |
| 0:50–0:55 | Break | — |
| 0:55–1:15 | Guided Practice | Add more filter types to the demo: `st.multiselect`, `st.radio`, `st.text_input`. |
| 1:15–1:35 | Independent Work | Start Exercise 03 (widget mastery) or 04 (dataset filter). |
| 1:35–1:45 | Discussion | "When should you use a form vs. direct widgets?" |
| 1:45–1:50 | Wrap-up | Assign reading 02 + notebook 02. Preview: layouts. |

---

## Session 03 — Layouts & Dashboard UI (Week 3)

### Learning Objectives
- Use sidebar, columns, tabs, and expanders
- Design a readable dashboard layout
- Understand UX principles for Data Science apps

### Materials
- Reading: `readings/05_layouts_and_containers.md`
- Reading: `readings/06_dashboard_design_ui_ux.md`
- Notebook: `notebooks/05_layouts_and_containers.ipynb`
- Notebook: `notebooks/06_data_science_dashboards.ipynb`
- Exercise: `exercises/05_layout_basics.py`
- Exercise: `exercises/06_dashboard_builder.py`
- Assignment: `assignments/A01_personal_dashboard.md` (Due)

### Time Plan

| Time | Activity | Details |
|------|----------|---------|
| 0:00–0:05 | Warm-up | Show a poorly laid-out app. "What's wrong with this?" |
| 0:05–0:20 | Concept | Layout hierarchy: page → sidebar → columns → containers. "A DS app is not a notebook in a web page." |
| 0:20–0:50 | Live Coding | **Build a dashboard:** sidebar for filters, 3 columns for KPIs, tabs for charts/tables, expander for details. |
| 0:50–0:55 | Break | — |
| 0:55–1:15 | Guided Practice | Students redesign the layout: swap tabs for columns, add a sidebar. |
| 1:15–1:35 | Independent Work | Start Exercise 05 or 06. |
| 1:35–1:45 | Discussion | Dashboard design principles. "What makes a dashboard readable?" |
| 1:45–1:50 | Wrap-up | A01 due. Preview: data display + visualization. |

---

## Session 04 — DataFrames & Visualization (Week 4)

### Learning Objectives
- Display DataFrames with column configuration
- Choose appropriate chart types
- Integrate Matplotlib and Plotly with Streamlit

### Materials
- Reading: `readings/07_data_display_dataframes.md`
- Reading: `readings/08_visualization_matplotlib_plotly.md`
- Notebook: `notebooks/07_DataFrames_Tables_Pandas.ipynb`
- Notebook: `notebooks/08_Interactive_Visualization.ipynb`
- Exercise: `exercises/07_data_display_challenges.py`
- Exercise: `exercises/08_visualization_workshop.py`
- Quiz: `quizzes/04_data_display.md`

### Time Plan

| Time | Activity | Details |
|------|----------|---------|
| 0:00–0:05 | Warm-up | "What chart would you use for this data?" (show 3 datasets) |
| 0:05–0:20 | Concept | `st.dataframe` vs `st.table`, column_config, native charts vs Matplotlib vs Plotly |
| 0:20–0:50 | Live Coding | **Build an EDA view:** Load Iris dataset, `st.dataframe` with column_config, histogram, scatter, line chart. Add Plotly for interactivity. |
| 0:50–0:55 | Break | — |
| 0:55–1:15 | Guided Practice | Students add a bar chart, customize colors, switch between Matplotlib and Plotly. |
| 1:15–1:35 | Independent Work | Start Exercise 07 or 08. |
| 1:35–1:45 | Discussion | "When to use Plotly vs Matplotlib vs native charts?" |
| 1:45–1:50 | Wrap-up | Preview: session state. |

---

## Session 05 — Session State & Reruns (Week 5)

### Learning Objectives
- Explain why Streamlit reruns and when state is needed
- Initialize and use `st.session_state`
- Use callbacks for stateful interactions
- Debug common state bugs

### Materials
- Reading: `readings/10_session_state_and_reruns.md`
- Notebook: `notebooks/10_Session_State_Reruns.ipynb`
- Exercise: `exercises/11_state_management_workshop.py`
- Quiz: `quizzes/05_session_state.md`

### Time Plan

| Time | Activity | Details |
|------|----------|---------|
| 0:00–0:05 | Warm-up | Counter demo: "Why does this reset to 0 every time?" |
| 0:05–0:25 | Concept | **The core lesson:** Draw the Streamlit execution model. Show step-by-step what happens on each interaction. Introduce session_state as the solution. |
| 0:25–0:50 | Live Coding | **Build a multi-step wizard:** Step 1 (select data), Step 2 (configure), Step 3 (results). Use session_state to track progress. Add a reset button. |
| 0:50–0:55 | Break | — |
| 0:55–1:15 | Guided Practice | Students add an undo feature, or a "comparison" feature that saves multiple results. |
| 1:15–1:35 | Independent Work | Start Exercise 11 (state management). |
| 1:35–1:45 | Discussion | "What other stateful patterns do you see in apps?" (shopping cart, multi-step form, undo/redo) |
| 1:45–1:50 | Wrap-up | Preview: file upload and dashboards. |

### Key Demo: Counter Bug
```python
# THIS DOES NOT WORK — explain why
count = 0
if st.button("Increment"):
    count += 1
st.write(f"Count: {count}")

# THIS WORKS
if "count" not in st.session_state:
    st.session_state.count = 0
if st.button("Increment"):
    st.session_state.count += 1
st.write(f"Count: {st.session_state.count}")
```

---

## Session 06 — File Upload & Dashboards (Week 6)

### Learning Objectives
- Handle file uploads (CSV, Excel, JSON)
- Process and validate uploaded data
- Build a complete interactive dashboard
- Use download buttons for results

### Materials
- Reading: `readings/09_file_upload_and_processing.md`
- Notebook: `notebooks/09_File_Upload_Processing.ipynb`
- Exercise: `exercises/09_file_upload_workshop.py`
- Exercise: `exercises/10_dashboard_workshop.py`
- Assignment: `assignments/A02_data_explorer.md` (Due)

### Time Plan

| Time | Activity | Details |
|------|----------|---------|
| 0:00–0:05 | Warm-up | "What file types does your data come in?" |
| 0:05–0:20 | Concept | File upload workflow: UPLOAD → VALIDATE → READ → CLEAN → ANALYZE → VISUALIZE |
| 0:20–0:50 | Live Coding | **Build a data explorer:** File upload → auto-detect columns → dynamic filters → summary stats → charts → download processed data. |
| 0:50–0:55 | Break | — |
| 0:55–1:15 | Guided Practice | Students add Excel support, a data quality report, or a correlation matrix. |
| 1:15–1:35 | Independent Work | Start Exercise 10 (dashboard workshop). |
| 1:35–1:45 | Discussion | Dashboard design review. Students show their dashboards. |
| 1:45–1:50 | Wrap-up | A02 due. Preview: caching and performance. |

---

## Session 07 — Caching & Performance (Week 7)

### Learning Objectives
- Explain why caching matters for Streamlit apps
- Use `st.cache_data` and `st.cache_resource` correctly
- Implement cache invalidation with TTL
- Measure and improve app performance

### Materials
- Reading: `readings/11_caching_and_performance.md`
- Notebook: `notebooks/11_Caching_Performance.ipynb`
- Exercise: `exercises/12_caching_workshop.py`
- Quiz: `quizzes/07_caching.md`

### Time Plan

| Time | Activity | Details |
|------|----------|---------|
| 0:00–0:05 | Warm-up | "How long does your dashboard take to load? Why?" |
| 0:05–0:20 | Concept | The performance problem: expensive computation on every rerun. Cache = remember results. `cache_data` = copies, `cache_resource` = singletons. |
| 0:20–0:50 | Live Coding | **Performance experiment:** Load a large CSV (100k rows) WITHOUT caching (show slow). Add `@st.cache_data` (show fast). Add TTL. Try `cache_resource` for a model. |
| 0:50–0:55 | Break | — |
| 0:55–1:15 | Guided Practice | Students add caching to their previous exercises. Measure before/after with `time.time()`. |
| 1:15–1:35 | Independent Work | Start Exercise 12 (caching workshop). |
| 1:35–1:45 | Discussion | "When should you NOT cache?" (real-time data, security-sensitive) |
| 1:45–1:50 | Wrap-up | Preview: architecture and multipage apps. |

---

## Session 08 — Architecture & Multipage (Week 8)

### Learning Objectives
- Refactor a monolithic app into modular components
- Build multipage Streamlit applications
- Use `st.navigation` for page routing
- Apply separation of concerns

### Materials
- Reading: `readings/12_app_architecture_multipage.md`
- Notebook: `notebooks/12_Architecture_Multipage.ipynb`
- Exercise: `exercises/13_architecture_workshop.py`
- Quiz: `quizzes/08_architecture.md`

### Time Plan

| Time | Activity | Details |
|------|----------|---------|
| 0:00–0:05 | Warm-up | "How many lines is your longest app file?" |
| 0:05–0:25 | Concept | Why modularize: maintainability, reusability, team collaboration. Show the progression: single file → functions → modules → pages. |
| 0:25–0:50 | Live Coding | **Refactor live:** Take a 200-line `app.py` and break it into `pages/`, `utils/`, `config.py`. Show `st.navigation`. |
| 0:50–0:55 | Break | — |
| 0:55–1:15 | Guided Practice | Students add a new page to their app. |
| 1:15–1:35 | Independent Work | Start Exercise 13 (architecture). |
| 1:35–1:45 | Discussion | "What goes in a shared module vs. a page file?" |
| 1:45–1:50 | Wrap-up | Preview: APIs and databases. |

---

## Session 09 — APIs & Databases (Week 9)

### Learning Objectives
- Fetch data from REST APIs
- Connect Streamlit to SQLite
- Perform CRUD operations
- Use parameterized queries for security

### Materials
- Reading: `readings/13_api_integration.md`
- Reading: `readings/14_database_integration.md`
- Exercise: `exercises/09_api_connectors.py`
- Exercise: `exercises/14_database_workshop.py`
- Quiz: `quizzes/09_api_integration.md`
- Quiz: `quizzes/10_database.md`
- **Mid-Course Assessment** (end of week)

### Time Plan

| Time | Activity | Details |
|------|----------|---------|
| 0:00–0:10 | Warm-up | **Mid-course review:** What have we learned? Key concepts quiz. |
| 0:10–0:25 | Concept | APIs: HTTP methods, JSON, error handling. Databases: SQL basics, CRUD, parameterized queries. |
| 0:25–0:50 | Live Coding | **API:** Fetch from a public API, parse JSON, display in DataFrame. **Database:** Create SQLite table, insert, query, display. |
| 0:50–0:55 | Break | — |
| 0:55–1:15 | Guided Practice | Students combine API data with database storage. |
| 1:15–1:35 | Independent Work | Start Exercise 09 (API) or 14 (database). |
| 1:35–1:45 | Discussion | SQL injection demo. "Why must we use parameterized queries?" |
| 1:45–1:50 | Wrap-up | Mid-course assessment details. Preview: ML. |

---

## Session 10 — Intro to ML with Streamlit (Week 10)

### Learning Objectives
- Train a simple model with scikit-learn
- Visualize model evaluation metrics in Streamlit
- Understand the ML pipeline: train → save → load → predict

### Materials
- Reading: `readings/15_ml_with_streamlit.md`
- Notebook: `notebooks/13_ML_Prediction.ipynb`
- Exercise: `exercises/15_ml_workshop.py`
- Quiz: `quizzes/11_machine_learning.md`

### Time Plan

| Time | Activity | Details |
|------|----------|---------|
| 0:00–0:05 | Warm-up | "Have you trained a model before? What was the hardest part?" |
| 0:05–0:25 | Concept | ML in Streamlit: train once, save model, load with caching, build prediction UI. The key insight: don't retrain on every rerun. |
| 0:25–0:50 | Live Coding | **Build a classifier:** Train Decision Tree on Iris, save with joblib, build Streamlit UI with feature inputs, show prediction + probability. |
| 0:50–0:55 | Break | — |
| 0:55–1:15 | Guided Practice | Students change the model type, add feature importance chart, try a different dataset. |
| 1:15–1:35 | Independent Work | Start Exercise 15 (ML workshop). |
| 1:35–1:45 | Discussion | "What could go wrong in production with this model?" |
| 1:45–1:50 | Wrap-up | Preview: model deployment and NLP. |

---

## Session 11 — ML Model Deployment (Week 11)

### Learning Objectives
- Save and load models correctly
- Build preprocessing pipelines that match training
- Handle invalid inputs gracefully
- Build batch prediction interfaces

### Materials
- Reading: `readings/15_ml_with_streamlit.md` (continued)
- Notebook: `notebooks/14_ML_Deployment.ipynb`
- Exercise: `exercises/15_ml_workshop.py` (continued)
- Quiz: `quizzes/12_ml_deployment.md`

### Time Plan

| Time | Activity | Details |
|------|----------|---------|
| 0:00–0:05 | Warm-up | "What happened when you changed the model in Exercise 15?" |
| 0:05–0:25 | Concept | Preprocessing trap: training vs inference. Model versioning. Batch prediction. Input validation. |
| 0:25–0:50 | Live Coding | **Build batch predictor:** Upload CSV → validate columns → preprocess → predict → display results → download. Add error handling for missing columns. |
| 0:50–0:55 | Break | — |
| 0:55–1:15 | Guided Practice | Students add confidence scores, a confusion matrix, or try a regression model. |
| 1:15–1:35 | Independent Work | Continue Exercise 15 or start assignment work. |
| 1:35–1:45 | Discussion | "What's the difference between a notebook and a deployed model?" |
| 1:45–1:50 | Wrap-up | Preview: NLP. |

---

## Session 12 — NLP & Text Analysis (Week 12)

### Learning Objectives
- Apply text preprocessing techniques
- Build a text classification pipeline
- Deploy NLP models in Streamlit
- Handle text input validation

### Materials
- Reading: `readings/16_nlp_text_analysis.md`
- Notebook: `notebooks/15_NLP_Applications.ipynb`
- Exercise: `exercises/17_nlp_workshop.py`
- Quiz: `quizzes/13_nlp.md`
- **Practical Exam** (end of week)

### Time Plan

| Time | Activity | Details |
|------|----------|---------|
| 0:00–0:05 | Warm-up | "How would you build an app that detects spam?" |
| 0:05–0:20 | Concept | NLP pipeline: text → preprocessing → features → model → prediction. TF-IDF. Sentiment analysis. |
| 0:20–0:50 | Live Coding | **Build sentiment analyzer:** Train TF-IDF + Logistic Regression on sample data. Build Streamlit UI: text input → preprocess → predict → show confidence. |
| 0:50–0:55 | Break | — |
| 0:55–1:15 | Guided Practice | Students try different models, add batch text prediction, or analyze a real dataset. |
| 1:15–1:35 | Independent Work | Start Exercise 17 (NLP workshop). |
| 1:35–1:45 | Discussion | "What are the limitations of simple NLP models?" |
| 1:45–1:50 | Wrap-up | Practical exam details. Preview: LLMs. |

---

## Session 13 — LLM & RAG (Week 13)

### Learning Objectives
- Build a chat interface with Streamlit
- Integrate with an LLM provider (or local alternative)
- Understand RAG architecture at a high level
- Be aware of prompt injection and AI safety

### Materials
- Reading: `readings/17_llm_rag_applications.md`
- Reading: `readings/18_ai_safety_and_security.md`
- Notebook: `notebooks/16_LLM_RAG.ipynb`
- Exercise: `exercises/18_llm_workshop.py`
- Quiz: `quizzes/14_llm_rag.md`
- Assignment: `assignments/A03_multipage_application.md` (Due)

### Time Plan

| Time | Activity | Details |
|------|----------|---------|
| 0:00–0:05 | Warm-up | "What AI tools do you use daily? How do they work?" |
| 0:05–0:25 | Concept | LLM apps: prompt → model → response. Chat UI. Streaming. RAG: documents → chunks → embeddings → retrieve → prompt. |
| 0:25–0:50 | Live Coding | **Build a chat app:** Use `st.chat_message`, `st.chat_input`. Connect to OpenAI API (or mock). Add session state for conversation history. Show secrets management. |
| 0:50–0:55 | Break | — |
| 0:55–1:15 | Guided Practice | Students add system prompts, try local alternatives, or modify the chat interface. |
| 1:15–1:35 | Independent Work | Start Exercise 18 (LLM workshop). |
| 1:35–1:45 | Discussion | "What are the risks of building LLM applications?" |
| 1:45–1:50 | Wrap-up | A03 due. Preview: deployment and production. |

---

## Session 14 — Security, Deployment & Production (Week 14)

### Learning Objectives
- Apply security best practices
- Deploy to Streamlit Community Cloud
- Monitor and debug deployed applications
- Implement testing and logging

### Materials
- Reading: `readings/security_and_secrets.md`
- Reading: `readings/deployment_guide.md`
- Reading: `readings/19_testing_and_monitoring.md`
- Notebook: `notebooks/deployment_tutorial.ipynb`
- Exercise: `exercises/deployment_exercises.py`
- Exercise: `exercises/16_production_ready.py`
- Quiz: `quizzes/15_deployment.md`
- Quiz: `quizzes/16_production_maintenance.md`
- Assignment: `assignments/A04_ml_production_app.md` (Due)

### Time Plan

| Time | Activity | Details |
|------|----------|---------|
| 0:00–0:10 | Warm-up | **Security quiz:** "What's wrong with this code?" (show SQL injection, hardcoded key) |
| 0:10–0:25 | Concept | Security essentials + deployment workflow. Community Cloud overview. |
| 0:25–0:50 | Live Coding | **Deploy together:** Take a working app → add requirements.txt → add .gitignore → push to GitHub → deploy on Community Cloud → test → fix one issue → verify. |
| 0:50–0:55 | Break | — |
| 0:55–1:15 | Guided Practice | Students deploy their own apps. Instructor helps with failures. |
| 1:15–1:35 | Independent Work | Start Exercise 16 (production ready) or deployment exercises. |
| 1:35–1:45 | Discussion | "What breaks in production that works locally?" |
| 1:45–1:50 | Wrap-up | A04 due. Capstone instructions distributed. |

---

## Session 15 — Capstone Work Session (Week 15)

### Learning Objectives
- Apply all course skills to a complete project
- Debug and optimize a non-trivial application
- Prepare for deployment and presentation

### Materials
- Project spec: `projects/final_capstone.md`
- Rubric: `projects/capstone_rubric.md`
- Checklist: `projects/capstone_submission_checklist.md`
- Presentation guide: `projects/capstone_presentation.md`
- **Final Practical Assessment** (start of session)

### Time Plan

| Time | Activity | Details |
|------|----------|---------|
| 0:00–0:10 | Final Practical Assessment | Timed assessment (continue separately or start here) |
| 0:10–0:20 | Capstone Check-in | Students report milestone progress. Identify blockers. |
| 0:20–0:50 | Guided Work | Instructor circulates, helps individual students debug. |
| 0:50–0:55 | Break | — |
| 0:55–1:25 | Independent Work | Students continue capstone development. |
| 1:25–1:40 | Deployment Help | Dedicated time for students struggling with deployment. |
| 1:40–1:50 | Presentation Prep | Review presentation guide. Practice demos. |

---

## Session 16 — Capstone Presentations (Week 16)

### Learning Objectives
- Present a complete application to an audience
- Answer technical questions about design decisions
- Provide constructive peer feedback

### Materials
- Presentation guide: `projects/capstone_presentation.md`
- Rubric: `projects/capstone_rubric.md`

### Time Plan

| Time | Activity | Details |
|------|----------|---------|
| 0:00–0:05 | Setup | Arrange room for demos. Test projector. |
| 0:05–1:30 | **Presentations** | ~10 min per student (8 students per session). Live demo + 3 min Q&A. |
| 1:30–1:40 | Peer Feedback | Students fill brief feedback forms for 2 peers. |
| 1:40–1:50 | Course Wrap-up | Key takeaways, where to go next, course evaluation. |

### Presentation Format (per student)
| Time | Activity |
|------|----------|
| 0:00–1:00 | Problem statement and motivation |
| 1:00–3:00 | Live demo of the application |
| 3:00–5:00 | Technical overview (architecture, key decisions) |
| 5:00–7:00 | Challenges and what you learned |
| 7:00–8:00 | Future improvements |
| 8:00–10:00 | Q&A from instructor and peers |

---

## Related Materials

- [Course Plan](course_plan.md) — Semester schedule
- [Teaching Roadmap](teaching_roadmap.md) — Module dependencies
- [Lab Activities](lab_activities.md) — Hands-on lab guides
- [Common Mistakes](common_student_mistakes.md) — Error catalog
- [Assessment Strategy](assessment_strategy.md) — Grading policies
