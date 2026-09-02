# Course Curriculum

> **Streamlit for Data Science — Learn, Build, Deploy**  
> Complete module-by-module curriculum across 6 progression levels.

---

## Curriculum Overview

| Level | Label | Modules | Weeks | Bloom's Focus |
|---|---|---|---|---|
| [Level 1](#level-1--beginner) | **Beginner** | M01–M03 | 1–3 | Remember, Understand |
| [Level 2](#level-2--intermediate) | **Intermediate** | M04–M06 | 4–6 | Understand, Apply |
| [Level 3](#level-3--advanced) | **Advanced** | M07–M09 | 7–9 | Apply, Analyze |
| [Level 4](#level-4--machine-learning) | **Machine Learning** | M10–M12 | 10–12 | Analyze, Evaluate |
| [Level 5](#level-5--ainlp--llm) | **AI / NLP / LLM** | M13 | 13 | Analyze, Create |
| [Level 6](#level-6--deployment--production) | **Deployment & Production** | M14–M16 | 14–16 | Evaluate, Create |

**Total:** 16 modules · 16 notebooks · 16 exercises · 12 quizzes · 4 assignments · 8 projects

---

## Level 1 — Beginner

*Weeks 1–3 · Foundation — Students build their first interactive apps.*

---

### Module 01: Streamlit Fundamentals

| Attribute | Detail |
|---|---|
| **Week** | 1 |
| **Bloom's Level** | Remember, Understand |
| **Reading** | [R01 — What is Streamlit?](../readings/r01_what_is_streamlit.md) · [R02 — Streamlit vs Alternatives](../readings/r02_streamlit_vs_dash_vs_flask.md) |
| **Notebook** | [N01 — Your First Streamlit App](../notebooks/01_first_streamlit_app.ipynb) |
| **Exercise** | [E01 — Hello Streamlit](../exercises/exercise_01_hello_streamlit.py) |
| **Quiz** | [Q01 — Fundamentals](../quizzes/quiz_01_fundamentals.md) |
| **App Demo** | [hello.py](../apps/hello.py) |

**Topics:**
- What is Streamlit? Philosophy, use cases, comparison with Dash/Flask/Gradio
- Installation & environment setup (`pip install streamlit`)
- Hello World: `st.title`, `st.write`, `st.markdown`, `st.code`
- Running apps: `streamlit run`, port configuration, auto-reload
- Markdown in Streamlit: headings, bold, italic, links, code blocks, LaTeX
- `.streamlit/config.toml` basics
- Project structure best practices

**Prerequisites:** Python 3.10+ installed, basic command line familiarity  
**Expected Skills:** Create and run a minimal Streamlit app; render text, headings, and markdown

---

### Module 02: Widgets & User Input

| Attribute | Detail |
|---|---|
| **Week** | 1–2 |
| **Bloom's Level** | Remember, Apply |
| **Reading** | [R03 — Widget Internals](../readings/r03_widget_internals.md) |
| **Notebook** | [N02 — The Widget Zoo](../notebooks/02_widgets_and_input.ipynb) |
| **Exercise** | [E02 — Widget Master](../exercises/exercise_02_widget_master.py) |
| **Quiz** | [Q02 — Widgets](../quizzes/quiz_02_widgets.md) |
| **App Demo** | [widgets_demo.py](../apps/widgets_demo.py) |

**Topics:**
- Widget fundamentals: return values, keys, callbacks, `disabled` state
- Text input: `st.text_input`, `st.text_area`, `st.number_input`
- Selection widgets: `st.selectbox`, `st.multiselect`, `st.radio`, `st.checkbox`, `st.toggle`
- Sliders & dates: `st.slider`, `st.select_slider`, `st.date_input`, `st.time_input`
- Color & file: `st.color_picker`, `st.file_uploader`
- Buttons & downloads: `st.button`, `st.form_submit_button`, `st.download_button`
- New features: `validate` parameter, `type` for text input (1.62+)

**Prerequisites:** M01  
**Expected Skills:** Build interactive UIs using the full widget library; understand widget return values and state

---

### Module 03: Layouts, Containers & Pages

| Attribute | Detail |
|---|---|
| **Week** | 2–3 |
| **Bloom's Level** | Apply, Understand |
| **Reading** | (Integrated into N03) |
| **Notebook** | [N03 — Layout Mastery](../notebooks/03_layouts_and_containers.ipynb) |
| **Exercise** | [E03 — Layout Designer](../exercises/exercise_03_layout_designer.py) |
| **Quiz** | [Q03 — Layouts](../quizzes/quiz_03_layouts.md) |
| **App Demo** | [layouts_demo.py](../apps/layouts_demo.py) |

**Topics:**
- Sidebar: `st.sidebar`, sidebar widgets vs. main area
- Columns: `st.columns` with gap presets and pixel-gap support
- Containers: `st.container`, `st.expander`, `st.popover`, `st.dialog`
- Tabs: `st.tabs` with `height` parameter
- Horizontal layouts: `wrap=False` for scrollable rows
- Status & progress: `st.status`, `st.progress`, `st.spinner`, `st.toast`
- Theming: `config.toml` themes, dark mode, custom fonts
- First multi-file app: page directory structure

**Prerequisites:** M01, M02  
**Expected Skills:** Structure complex layouts with columns, tabs, sidebars; apply theming; organize multi-file apps

---

## Level 2 — Intermediate

*Weeks 4–6 · Data & Interaction — Students create data-rich, stateful applications.*

---

### Module 04: Data Visualization with Streamlit

| Attribute | Detail |
|---|---|
| **Week** | 4 |
| **Bloom's Level** | Apply, Understand |
| **Reading** | (Integrated into N04) |
| **Notebook** | [N04 — Data Visualization](../notebooks/04_data_visualization.ipynb) |
| **Exercise** | [E04 — Chart Gallery](../exercises/exercise_04_chart_gallery.py) |
| **Quiz** | [Q04 — Visualization](../quizzes/quiz_04_visualization.md) |
| **App Demo** | [charts_demo.py](../apps/charts_demo.py) |

**Topics:**
- Native charts: `st.line_chart`, `st.bar_chart`, `st.area_chart`, `st.scatter_chart`, `st.map`
- Matplotlib integration: `st.pyplot` (explicit figure required since 1.62)
- Plotly integration: `st.plotly_chart` with `use_container_width`
- Altair / Vega-Lite: `st.altair_chart`, `st.vega_lite_chart`
- PyDeck: `st.pydeck_chart` for geospatial
- Graphviz: `st.graphviz_chart`
- Chart configuration: toolbar, download buttons, theming
- Choosing the right chart: decision matrix

**Prerequisites:** M01–M03  
**Expected Skills:** Render native and third-party charts; select appropriate visualizations for different data types

---

### Module 05: Session State & App Memory

| Attribute | Detail |
|---|---|
| **Week** | 5 |
| **Bloom's Level** | Understand, Apply |
| **Reading** | [R04 — The Execution Model](../readings/r04_execution_model.md) · [R06 — Session State Internals](../readings/r06_session_state_internals.md) |
| **Notebook** | [N05 — Session State Deep Dive](../notebooks/05_session_state.ipynb) |
| **Exercise** | [E05 — State Counter](../exercises/exercise_05_state_counter.py) |
| **Quiz** | [Q05 — Session State](../quizzes/quiz_05_session_state.md) |
| **App Demo** | [state_demo.py](../apps/state_demo.py) |

**Topics:**
- Streamlit's execution model: top-to-bottom rerun on every interaction
- `st.session_state`: dict-like API, per-session isolation
- Initializing state: `.setdefault()`, conditional init patterns
- Callbacks: `on_click`, `on_change`, callback chains
- State patterns: counter, multi-page form, undo/redo, user preferences
- Common pitfalls: state loss, unintended rerun loops, stale values
- `st.fragment` (partial rerun): background auto-rerun with `run_every`

**Prerequisites:** M01–M03  
**Expected Skills:** Manage persistent state across reruns; design stateful interaction patterns; debug rerun-related issues

---

### Module 06: Forms, Inputs & File Handling

| Attribute | Detail |
|---|---|
| **Week** | 5–6 |
| **Bloom's Level** | Apply |
| **Reading** | (Integrated into N06) |
| **Notebook** | [N06 — Forms, Files & Data Pipelines](../notebooks/06_forms_file_handling.ipynb) |
| **Exercise** | [E06 — Form Builder](../exercises/exercise_06_form_builder.py) |
| **Quiz** | [Q06 — Forms & Files](../quizzes/quiz_06_forms_files.md) |
| **App Demo** | [forms_demo.py](../apps/forms_demo.py) |

**Topics:**
- `st.form` containers and `st.form_submit_button`
- Form validation: client-side `validate` (1.62+), custom patterns
- File uploaders: `st.file_uploader`, accepted types, size limits
- CSV/Excel processing with Pandas
- Image/audio/video: `st.image`, `st.audio`, `st.video`
- Download buttons: `st.download_button` with auto-inferred metadata
- Temporary files: `tempfile`, session-scoped storage
- File organization and upload directory structure

**Prerequisites:** M02, M05  
**Expected Skills:** Build form-based input flows; handle file uploads/downloads; process uploaded data with Pandas

---

## Level 3 — Advanced

*Weeks 7–9 · Architecture — Students build performant, well-structured applications.*

---

### Module 07: Caching, Fragments & Performance

| Attribute | Detail |
|---|---|
| **Week** | 7 |
| **Bloom's Level** | Apply, Analyze |
| **Reading** | [R05 — Caching Internals](../readings/r05_caching_internals.md) |
| **Notebook** | [N07 — Performance Engineering](../notebooks/07_caching_and_performance.ipynb) |
| **Exercise** | [E07 — Cache Challenge](../exercises/exercise_07_cache_challenge.py) |
| **Quiz** | [Q07 — Caching](../quizzes/quiz_07_caching.md) |
| **App Demo** | [caching_demo.py](../apps/caching_demo.py) |

**Topics:**
- Why caching matters: Streamlit's rerun model and performance
- `st.cache_data`: hash-based caching, TTL, `max_entries`
- `st.cache_resource`: singleton pattern for DB connections, ML models
- Background refresh: `refresh_mode="background"` (1.61+)
- Cache invalidation: `.clear()`, `hash_funcs`, manual control
- `st.fragment`: partial rerun scope, `run_every`, nesting
- Lazy loading: `st.dataframe` lazy parameter (1.61+), Polars LazyFrame
- Performance profiling and bottleneck identification

**Prerequisites:** M05  
**Expected Skills:** Optimize app performance through caching strategies; implement fragments for targeted reruns; diagnose performance issues

---

### Module 08: Multipage Apps & Navigation

| Attribute | Detail |
|---|---|
| **Week** | 8 |
| **Bloom's Level** | Apply, Analyze |
| **Reading** | (Integrated into N08) |
| **Notebook** | [N08 — Building Multipage Applications](../notebooks/08_multipage_apps.ipynb) |
| **Exercise** | [E08 — Multipage Navigator](../exercises/exercise_08_multipage_nav.py) |
| **Quiz** | [Q08 — Multipage](../quizzes/quiz_08_multipage.md) |
| **App Demo** | [multipage_demo/](../apps/multipage_demo/) |

**Topics:**
- Page directory convention: `pages/` folder, numbering, emoji prefixes
- `st.navigation`: modern API for programmatic page control
- `st.Page`: proper class (1.61+) with `isinstance` support
- Sidebar navigation: dynamic page selection, conditional pages
- URL query params: `st.query_params` for deep linking
- `st.set_page_config`: must be the first Streamlit call
- Reusable pages: composing navigation from functions
- Multipage testing patterns

**Prerequisites:** M05, M07  
**Expected Skills:** Build multi-page applications; implement programmatic navigation; manage URL state

---

### Module 09: Architecture & Design Patterns

| Attribute | Detail |
|---|---|
| **Week** | 8–9 |
| **Bloom's Level** | Apply, Analyze |
| **Reading** | [R07 — Architecture Patterns](../readings/r07_architecture_patterns.md) |
| **Notebook** | [N09 — Architecting Streamlit Apps](../notebooks/09_architecture_patterns.ipynb) |
| **Exercise** | [E09 — Architecture Review](../exercises/exercise_09_architecture_review.py) |
| **Quiz** | [Q09 — Architecture](../quizzes/quiz_09_architecture.md) |
| **App Demo** | [architecture_demo/](../apps/architecture_demo/) |

**Topics:**
- Project structure: `src/`, `pages/`, `utils/`, `components/`, `assets/`, `tests/`
- Separation of concerns: UI vs. logic vs. data layer
- Component pattern: reusable components via `st.fragment` or modules
- Configuration management: `config.toml`, env vars, `st.secrets`
- State management patterns: global vs. session vs. page-level
- Error handling: `try/except`, `st.error`, `st.warning`, graceful degradation
- Logging: Python `logging` in Streamlit context
- Code organization: when to extract into separate `.py` files

**Prerequisites:** M05, M07, M08  
**Expected Skills:** Design well-structured Streamlit applications; apply separation of concerns; choose appropriate architecture patterns

---

## Level 4 — Machine Learning

*Weeks 10–12 · Data Layer & ML — Students connect to data sources and deploy models.*

---

### Module 10: Databases & Persistent Storage

| Attribute | Detail |
|---|---|
| **Week** | 10 |
| **Bloom's Level** | Analyze, Apply |
| **Reading** | [R08 — Database Design Basics](../readings/r08_database_design_basics.md) |
| **Notebook** | [N10 — Database Connectivity](../notebooks/10_databases.ipynb) |
| **Exercise** | [E10 — Database CRUD](../exercises/exercise_10_database_crud.py) |
| **Quiz** | [Q10 — Databases](../quizzes/quiz_10_databases.md) |
| **App Demo** | [db_demo.py](../apps/db_demo.py) |

**Topics:**
- `st.connection`: unified connection API, built-in types
- SQL connections: `st.connections.SQLConnection`, SQLAlchemy integration
- Configuration via `secrets.toml`, query execution
- SQLite: local development and prototyping
- PostgreSQL: production database, connection pooling
- `conn.read_sql()`, `conn.query()` for data access
- Secrets management: `.streamlit/secrets.toml`, env vars
- ORM basics: SQLAlchemy models for Streamlit apps
- NoSQL introduction: MongoDB, Firestore (overview)

**Prerequisites:** M06  
**Expected Skills:** Connect Streamlit apps to SQL databases; implement CRUD operations; manage secrets properly

---

### Module 11: APIs, Connectors & External Data

| Attribute | Detail |
|---|---|
| **Week** | 11 |
| **Bloom's Level** | Analyze, Apply |
| **Reading** | [R09 — API Design Patterns](../readings/r09_api_design_patterns.md) |
| **Notebook** | [N11 — API Integration](../notebooks/11_api_integration.ipynb) |
| **Exercise** | [E11 — API Fetcher](../exercises/exercise_11_api_fetcher.py) |
| **Quiz** | [Q11 — APIs](../quizzes/quiz_11_apis.md) |
| **App Demo** | [api_demo.py](../apps/api_demo.py) |

**Topics:**
- HTTP in Python: `requests`, `httpx`, async patterns
- REST API consumption: GET/POST, authentication, rate limiting
- API keys in Streamlit: `st.secrets`, environment variables
- JSON processing: parsing, nested data, error handling
- External data connectors: `st.connection` for HTTP
- Data pipelines: Fetch → parse → cache → display
- Streamlit components: `streamlit.components.v1` for HTML/JS
- Building custom components: `st.components.v1.declare_component`

**Prerequisites:** M07, M09  
**Expected Skills:** Integrate external APIs; manage API keys securely; build custom Streamlit components

---

### Module 12: ML Model Deployment with Streamlit

| Attribute | Detail |
|---|---|
| **Week** | 12 |
| **Bloom's Level** | Apply, Analyze |
| **Reading** | [R10 — ML Serving Patterns](../readings/r10_ml_serving_patterns.md) |
| **Notebook** | [N12 — ML Dashboards](../notebooks/12_ml_dashboard.ipynb) |
| **Exercise** | [E12 — ML Predictor](../exercises/exercise_12_ml_predictor.py) |
| **Quiz** | [Q12 — ML & AI](../quizzes/quiz_12_ml_ai.md) |
| **App Demo** | [ml_demo.py](../apps/ml_demo.py) |
| **Assignment** | [Assignment 03 — Full Stack App](../assignments/assignment_03_full_stack_app/) |

**Topics:**
- Model serialization: `joblib`, `pickle`, ONNX, security concerns
- Loading models: `@st.cache_resource` for model loading
- Interactive prediction: widget-driven input → inference → display
- Feature engineering: input preprocessing in the app
- Model comparison: side-by-side dashboards
- Confidence & explanations: SHAP, LIME, feature importance
- Batch prediction: file upload → bulk inference → download
- Model versioning and organization
- Real-time vs. batch: when to use each approach

**Prerequisites:** M07, M10, scikit-learn basics  
**Expected Skills:** Deploy ML models as interactive apps; implement model explanations; build comparison dashboards

---

## Level 5 — AI / NLP / LLM

*Week 13 · Cutting Edge — Students build AI-powered conversational applications.*

---

### Module 13: NLP, AI & LLM Applications

| Attribute | Detail |
|---|---|
| **Week** | 13 |
| **Bloom's Level** | Analyze, Create |
| **Reading** | [R11 — RAG Concepts](../readings/r11_rag_concepts.md) |
| **Notebook** | [N13 — Building AI-Powered Apps](../notebooks/13_ai_llm_apps.ipynb) |
| **Exercise** | [E13 — Chatbot Builder](../exercises/exercise_13_chatbot_builder.py) |
| **Quiz** | (Covered in Q12) |
| **App Demo** | [ai_chat_demo.py](../apps/ai_chat_demo.py) |
| **Project** | [P07 — RAG Document Chat](../projects/p07_rag_chat/) |

**Topics:**
- NLP basics in Streamlit: text classification, sentiment analysis
- Text preprocessing: tokenization, vectorization, display
- Chat interfaces: `st.chat_message`, `st.chat_input`
- LLM integration: OpenAI API, Anthropic, Ollama (local)
- Conversation management: session-state-based chat history
- Streaming responses: token-by-token display
- RAG (Retrieval-Augmented Generation): document → chunk → embed → retrieve → generate
- Vector stores: ChromaDB, FAISS, Pinecone
- LangChain + Streamlit: chain orchestration, tool use
- Prompt engineering UIs: template interfaces
- Guardrails: output filtering, token limits, cost control

**Prerequisites:** M07, M12  
**Expected Skills:** Build conversational AI interfaces; implement RAG pipelines; integrate LLMs with Streamlit chat UI

---

## Level 6 — Deployment & Production

*Weeks 14–16 · Ship It — Students test, secure, deploy, and maintain production applications.*

---

### Module 14: Testing, Security & CI/CD

| Attribute | Detail |
|---|---|
| **Week** | 14 |
| **Bloom's Level** | Evaluate, Apply |
| **Reading** | [R12 — Security Best Practices](../readings/r12_security_best_practices.md) · [R13 — Testing Strategies](../readings/r13_testing_strategies.md) |
| **Notebook** | [N14 — Testing & Securing Apps](../notebooks/14_testing_security.ipynb) |
| **Exercise** | [E14 — Test Suite](../exercises/exercise_14_test_suite.py) |
| **Quiz** | (Integrated into capstone assessment) |
| **App Demo** | [test_demo.py](../apps/test_demo.py) |

**Topics:**
- `st.testing.AppTest`: Streamlit's native testing framework
- Unit tests with pytest: structure, fixtures, mocking
- AppTest API: `AppTest.from_file()`, simulate input, assert output
- Security fundamentals: OWASP Top 10 overview
- Secrets management: `.streamlit/secrets.toml`, production vaults
- Input validation: `validate` parameter, custom sanitization
- Server security: `allowedHosts`, CORS, XSRF protection
- Authentication: `streamlit-authenticator`, role-based access
- CI/CD with GitHub Actions: automated testing, linting, deployment
- Linting: Ruff, MyPy, pre-commit hooks

**Prerequisites:** M09  
**Expected Skills:** Write AppTest test suites; secure Streamlit apps; set up CI/CD pipelines

---

### Module 15: Streamlit Community Cloud & Deployment

| Attribute | Detail |
|---|---|
| **Week** | 15 |
| **Bloom's Level** | Evaluate, Apply |
| **Reading** | [R14 — Deployment Options](../readings/r14_deployment_options.md) |
| **Notebook** | [N15 — Deploy to the World](../notebooks/15_deployment_guide.ipynb) |
| **Exercise** | [E15 — Deploy Pipeline](../exercises/exercise_15_deploy_pipeline.py) |
| **Quiz** | (Integrated into capstone assessment) |
| **App Demo** | [deployed_app/](../apps/deployed_app/) |

**Topics:**
- Community Cloud overview: free hosting, GitHub integration, auto-deploy
- Prerequisites: GitHub repo, `requirements.txt`, entry point
- Deployment workflow: connect repo → select branch/file → deploy
- Secrets in Cloud: adding secrets via dashboard
- App sleep/wake: 7-day inactivity sleep, keep-awake strategies
- Alternatives: HuggingFace Spaces, Render, Railway, Docker
- Deployment checklist: file organization, dependency pinning, secrets
- Multi-app repos: deploying multiple apps from one repository
- Troubleshooting common deployment errors

**Prerequisites:** M14  
**Expected Skills:** Deploy Streamlit apps to Community Cloud; manage deployment secrets; troubleshoot deployment issues

---

### Module 16: Production, Maintenance & Monitoring

| Attribute | Detail |
|---|---|
| **Week** | 16 |
| **Bloom's Level** | Evaluate, Create |
| **Reading** | [R15 — Production Checklist](../readings/r15_production_checklist.md) |
| **Notebook** | [N16 — Production Readiness](../notebooks/16_production_readiness.ipynb) |
| **Exercise** | [E16 — Monitoring Setup](../exercises/exercise_16_monitoring.py) |
| **Quiz** | (Integrated into capstone assessment) |

**Topics:**
- Monitoring basics: logging, error tracking, usage analytics
- Performance monitoring: cache hit rates, load times, memory
- Version updates: keeping Streamlit current, migration guides
- User feedback: in-app feedback mechanisms
- Documentation: README, inline docs, user guides
- Maintenance tasks: dependency updates, security patches
- Scaling considerations: when Streamlit is (and isn't) the right tool
- MLOps integration: MLflow, DVC, model registry
- Course review and wrap-up

**Prerequisites:** M14, M15  
**Expected Skills:** Monitor production apps; plan maintenance cycles; evaluate when Streamlit is appropriate

---

## Cross-Module Dependencies

```
M01 ──► M02 ──► M03
              │
              ▼
M04 ──► M05 ──► M06
              │
              ▼
M07 ──► M08 ──► M09
              │
              ▼
M10 ──► M11    M12
              │
              ▼
           M13
              │
              ▼
M14 ──► M15 ──► M16
```

Key dependency chains:
- **State chain:** M01 → M02 → M05 → M07 (understanding state at each depth)
- **Data chain:** M06 → M10 → M11 → M12 (file handling → databases → APIs → ML)
- **Architecture chain:** M08 → M09 → M14 (multipage → patterns → testing)
- **Deployment chain:** M14 → M15 → M16 (test → deploy → maintain)
