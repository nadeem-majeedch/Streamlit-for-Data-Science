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
| **Reading** | [R01 — What is Streamlit?](../readings/01_streamlit_introduction.md) · [R02 — Streamlit vs Alternatives](../readings/01_streamlit_introduction.md) |
| **Notebook** | [N01 — Your First Streamlit App](../notebooks/01_Streamlit_Introduction.ipynb) |
| **Exercise** | [E01 — Hello Streamlit](../exercises/01_hello_streamlit.py) |
| **Quiz** | [Q01 — Fundamentals](../quizzes/01_fundamentals.md) |
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
| **Reading** | [R03 — Widget Internals](../readings/03_streamlit_widgets_and_input.md) |
| **Notebook** | [N02 — The Widget Zoo](../notebooks/03_streamlit_widgets.ipynb) |
| **Exercise** | [E02 — Widget Master](../exercises/03_widget_mastery.py) |
| **Quiz** | [Q02 — Widgets](../quizzes/02_widgets_input.md) |
| **App Demo** | [widgets_demo.py](../apps/03_widgets_demo.py) |

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
| **Notebook** | [N03 — Layout Mastery](../notebooks/05_layouts_and_containers.ipynb) |
| **Exercise** | [E03 — Layout Designer](../exercises/05_layout_basics.py) |
| **Quiz** | [Q03 — Layouts](../quizzes/03_layouts_uiux.md) |
| **App Demo** | [layouts_demo.py](../apps/05_layouts_demo.py) |

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
| **Notebook** | [N04 — Data Visualization](../notebooks/08_interactive_visualization.ipynb) |
| **Exercise** | [E04 — Chart Gallery](../exercises/08_visualization_workshop.py) |
| **Quiz** | [Q04 — Visualization](../quizzes/04_dataframes_visualization.md) |
| **App Demo** | [charts_demo.py](../apps/07_data_display_demo.py) |

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
| **Reading** | [R04 — The Execution Model](../readings/11_session_state_and_execution.md) · [R06 — Session State Internals](../readings/11_session_state_and_execution.md) |
| **Notebook** | [N05 — Session State Deep Dive](../notebooks/11_session_state_execution_model.ipynb) |
| **Exercise** | [E05 — State Counter](../exercises/11_state_management_workshop.py) |
| **Quiz** | [Q05 — Session State](../quizzes/05_session_state.md) |
| **App Demo** | [state_demo.py](../apps/11_session_state_demo.py) |

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
| **Notebook** | [N06 — Forms, Files & Data Pipelines](../notebooks/09_file_upload_and_processing.ipynb) |
| **Exercise** | [E06 — Form Builder](../exercises/09_file_upload_workshop.py) |
| **Quiz** | [Q06 — Forms & Files](../quizzes/06_file_upload.md) |
| **App Demo** | [forms_demo.py](../apps/04_forms_demo.py) |

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
| **Reading** | [R05 — Caching Internals](../readings/12_caching_and_performance.md) |
| **Notebook** | [N07 — Performance Engineering](../notebooks/12_caching_performance.ipynb) |
| **Exercise** | [E07 — Cache Challenge](../exercises/12_caching_workshop.py) |
| **Quiz** | [Q07 — Caching](../quizzes/08_caching_performance.md) |
| **App Demo** | [caching_demo.py](../apps/12_caching_performance_demo.py) |

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
| **Notebook** | [N08 — Building Multipage Applications](../notebooks/13_application_architecture.ipynb) |
| **Exercise** | [E08 — Multipage Navigator](../exercises/13_architecture_workshop.py) |
| **Quiz** | [Q08 — Multipage](../quizzes/09_architecture_multipage.md) |
| **App Demo** | [multipage_demo/](../apps/13_modular_app/) |

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
| **Reading** | [R07 — Architecture Patterns](../readings/13_application_architecture.md) |
| **Notebook** | [N09 — Architecting Streamlit Apps](../notebooks/13_application_architecture.ipynb) |
| **Exercise** | [E09 — Architecture Review](../exercises/13_architecture_workshop.py) |
| **Quiz** | [Q09 — Architecture](../quizzes/09_architecture_multipage.md) |
| **App Demo** | [architecture_demo/](../apps/13_modular_app/) |

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
| **Reading** | [R08 — Database Design Basics](../readings/14_databases_and_persistence.md) |
| **Notebook** | [N10 — Database Connectivity](../notebooks/14_databases_persistence.ipynb) |
| **Exercise** | [E10 — Database CRUD](../exercises/14_database_workshop.py) |
| **Quiz** | [Q10 — Databases](../quizzes/10_databases_persistence.md) |
| **App Demo** | [db_demo.py](../apps/14_database_dashboard.py) |

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
| **Reading** | [R09 — API Design Patterns](../readings/13_application_architecture.md) |
| **Notebook** | [N11 — API Integration](../notebooks/14_databases_persistence.ipynb) |
| **Exercise** | [E11 — API Fetcher](../exercises/09_api_connectors.py) |
| **Quiz** | [Q11 — APIs](../quizzes/10_databases_persistence.md) |
| **App Demo** | [api_demo.py](../apps/09_file_upload_demo.py) |

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
| **Reading** | [R10 — ML Serving Patterns](../readings/15_machine_learning_streamlit.md) |
| **Notebook** | [N12 — ML Dashboards](../notebooks/15_ml_streamlit.ipynb) |
| **Exercise** | [E12 — ML Predictor](../exercises/15_ml_workshop.py) |
| **Quiz** | [Q12 — ML & AI](../quizzes/11_machine_learning.md) |
| **App Demo** | [ml_demo.py](../apps/15_classification_app.py) |
| **Assignment** | [Assignment 03 — Full Stack App](../assignments/A03_multipage_application.md) |

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
| **Reading** | [R11 — RAG Concepts](../readings/18_llm_rag_applications.md) |
| **Notebook** | [N13 — Building AI-Powered Apps](../notebooks/18_llm_applications.ipynb) |
| **Exercise** | [E13 — Chatbot Builder](../exercises/18_llm_workshop.py) |
| **Quiz** | (Covered in Q12) |
| **App Demo** | [ai_chat_demo.py](../apps/18_llm_chat.py) |
| **Project** | [P07 — RAG Document Chat](../projects/P07_rag_document_chat.md) |

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
| **Reading** | [R12 — Security Best Practices](../readings/security_and_secrets.md) · [R13 — Testing Strategies](../readings/13_application_architecture.md) |
| **Notebook** | [N14 — Testing & Securing Apps](../notebooks/security_practical_lab.ipynb) |
| **Exercise** | [E14 — Test Suite](../exercises/16_production_ready.py) |
| **Quiz** | (Integrated into capstone assessment) |
| **App Demo** | [test_demo.py](../apps/01_introduction_demo.py) |

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
| **Reading** | [R14 — Deployment Options](../readings/deployment_guide.md) |
| **Notebook** | [N15 — Deploy to the World](../notebooks/deployment_tutorial.ipynb) |
| **Exercise** | [E15 — Deploy Pipeline](../exercises/deployment_exercises.py) |
| **Quiz** | (Integrated into capstone assessment) |
| **App Demo** | [deployed_app/](../apps/deployable_app/) |

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
| **Reading** | [R15 — Production Checklist](../readings/deployment_guide.md) |
| **Notebook** | [N16 — Production Readiness](../notebooks/deployment_tutorial.ipynb) |
| **Exercise** | [E16 — Monitoring Setup](../exercises/16_production_ready.py) |
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
