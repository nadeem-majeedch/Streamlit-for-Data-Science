# Learning Outcomes

> **Streamlit for Data Science — Learn, Build, Deploy**  
> Course Learning Outcomes (CLOs) with full assessment and resource mapping.

---

## Course Learning Outcomes

Upon successful completion of this course, students will be able to:

| # | CLO | Bloom's Level | Primary Modules |
|---|---|---|---|
| [CLO1](#clo1--explain-streamlit-core-concepts) | Explain Streamlit's execution model, architecture, and widget lifecycle | Understand | M01, M02, M05 |
| [CLO2](#clo2--build-interactive-applications) | Build interactive data applications using Streamlit widgets, layouts, and state management | Apply | M01–M03, M05 |
| [CLO3](#clo3--implement-data-visualization) | Implement data visualization strategies using Streamlit's native and third-party chart integrations | Apply | M04 |
| [CLO4](#clo4--manage-application-state) | Design and manage application state across reruns using session state, callbacks, and fragments | Apply, Analyze | M05, M07 |
| [CLO5](#clo5--optimize-performance) | Optimize Streamlit application performance through caching, fragments, and lazy loading | Analyze | M07, M08 |
| [CLO6](#clo6--design-well-architected-applications) | Design well-structured Streamlit applications using proven architecture patterns | Apply, Analyze | M08, M09 |
| [CLO7](#clo7--connect-to-data-sources) | Connect Streamlit apps to databases and external APIs for persistent data and real-time information | Apply | M10, M11 |
| [CLO8](#clo8--deploy-ml-models) | Deploy machine learning models as interactive Streamlit applications with explanations | Apply, Analyze | M12 |
| [CLO9](#clo9--build-ai-powered-applications) | Build AI-powered applications including chat interfaces and RAG systems | Apply, Create | M13 |
| [CLO10](#clo10--test-and-secure-applications) | Apply testing, security best practices, and CI/CD to Streamlit applications | Evaluate | M14 |
| [CLO11](#clo11--deploy-to-production) | Deploy, monitor, and maintain Streamlit applications in production environments | Evaluate | M15, M16 |
| [CLO12](#clo12--execute-full-development-lifecycle) | Execute a complete software development lifecycle for a data application, from requirements to deployment | Create | M14–M16, P08 |

---

## CLO Detail & Traceability

### CLO1 — Explain Streamlit Core Concepts

> **"Students can explain Streamlit's execution model, architecture, and widget lifecycle."**

**Bloom's Level:** Understand

| Resource Type | Resource | Description |
|---|---|---|
| **Reading** | [R01 — What is Streamlit?](../readings/01_streamlit_introduction.md) | Origin, philosophy, comparison with alternatives |
| **Reading** | [R02 — Streamlit vs Alternatives](../readings/01_streamlit_introduction.md) | Feature comparison, use-case analysis |
| **Reading** | [R04 — The Execution Model](../readings/11_session_state_and_execution.md) | Top-to-bottom reruns, lifecycle |
| **Reading** | [R06 — Session State Internals](../readings/11_session_state_and_execution.md) | Per-session isolation, dict-like behavior |
| **Notebook** | [N01 — Your First Streamlit App](../notebooks/01_Streamlit_Introduction.ipynb) | Hands-on introduction |
| **Notebook** | [N02 — The Widget Zoo](../notebooks/03_streamlit_widgets.ipynb) | Widget fundamentals |
| **Notebook** | [N05 — Session State Deep Dive](../notebooks/11_session_state_execution_model.ipynb) | Execution model in practice |
| **Exercise** | [E01 — Hello Streamlit](../exercises/01_hello_streamlit.py) | Build a basic app |
| **Quiz** | [Q01 — Fundamentals](../quizzes/01_fundamentals.md) | Concept recall (MC + short answer) |
| **Quiz** | [Q02 — Widgets](../quizzes/02_widgets_input.md) | Widget API knowledge |
| **Assessment** | [Midterm Theory](../assessments/midcourse_assessment.md) | Architecture and lifecycle questions |
| **Assessment** | [Pre-Course Assessment](../quizzes/pre_course_assessment.md) | Baseline placement |

---

### CLO2 — Build Interactive Applications

> **"Students can build interactive data applications using Streamlit widgets, layouts, and state management."**

**Bloom's Level:** Apply

| Resource Type | Resource | Description |
|---|---|---|
| **Notebook** | [N01 — Your First Streamlit App](../notebooks/01_Streamlit_Introduction.ipynb) | Basic app creation |
| **Notebook** | [N02 — The Widget Zoo](../notebooks/03_streamlit_widgets.ipynb) | Full widget library |
| **Notebook** | [N03 — Layout Mastery](../notebooks/05_layouts_and_containers.ipynb) | Complex layouts |
| **Notebook** | [N05 — Session State Deep Dive](../notebooks/11_session_state_execution_model.ipynb) | Stateful apps |
| **Exercise** | [E01 — Hello Streamlit](../exercises/01_hello_streamlit.py) | Basic app |
| **Exercise** | [E02 — Widget Master](../exercises/03_widget_mastery.py) | Widget implementation |
| **Exercise** | [E03 — Layout Designer](../exercises/05_layout_basics.py) | Layout challenge |
| **Exercise** | [E05 — State Counter](../exercises/11_state_management_workshop.py) | State management |
| **Quiz** | [Q03 — Layouts](../quizzes/03_layouts_uiux.md) | Layout API knowledge |
| **Assignment** | [Assignment 01 — Basic App](../assignments/A01_personal_dashboard.md) | Graded app submission |
| **Project** | [P01 — Personal Dashboard](../projects/P01_csv_data_viewer.md) | Complete single-page app |
| **App Demo** | [hello.py](../apps/hello.py), [widgets_demo.py](../apps/03_widgets_demo.py), [layouts_demo.py](../apps/05_layouts_demo.py) | Reference implementations |

---

### CLO3 — Implement Data Visualization

> **"Students can implement data visualization strategies using Streamlit's native and third-party chart integrations."**

**Bloom's Level:** Apply

| Resource Type | Resource | Description |
|---|---|---|
| **Notebook** | [N04 — Data Visualization](../notebooks/08_interactive_visualization.ipynb) | All chart types and integrations |
| **Exercise** | [E04 — Chart Gallery](../exercises/08_visualization_workshop.py) | Multi-chart implementation |
| **Quiz** | [Q04 — Visualization](../quizzes/04_dataframes_visualization.md) | Chart selection and API |
| **Assignment** | [Assignment 02 — Data Dashboard](../assignments/A02_data_explorer.md) | Interactive dashboard |
| **Project** | [P02 — Data Explorer](../projects/P02_data_explorer.md) | Chart-driven data exploration |
| **App Demo** | [charts_demo.py](../apps/07_data_display_demo.py) | All chart types demonstrated |

---

### CLO4 — Manage Application State

> **"Students can design and manage application state across reruns using session state, callbacks, and fragments."**

**Bloom's Level:** Apply, Analyze

| Resource Type | Resource | Description |
|---|---|---|
| **Reading** | [R04 — The Execution Model](../readings/11_session_state_and_execution.md) | Why state is needed |
| **Reading** | [R06 — Session State Internals](../readings/11_session_state_and_execution.md) | How state works |
| **Notebook** | [N05 — Session State Deep Dive](../notebooks/11_session_state_execution_model.ipynb) | State patterns |
| **Notebook** | [N07 — Performance Engineering](../notebooks/12_caching_performance.ipynb) | Fragment-based partial reruns |
| **Exercise** | [E05 — State Counter](../exercises/11_state_management_workshop.py) | State implementation |
| **Exercise** | [E07 — Cache Challenge](../exercises/12_caching_workshop.py) | Fragment patterns |
| **Quiz** | [Q05 — Session State](../quizzes/05_session_state.md) | State concepts |
| **Quiz** | [Q07 — Caching](../quizzes/08_caching_performance.md) | Fragment and cache state |
| **Project** | [P04 — Real-Time Dashboard](../projects/P02_data_explorer.md) | Advanced state management |
| **App Demo** | [state_demo.py](../apps/11_session_state_demo.py), [caching_demo.py](../apps/12_caching_performance_demo.py) | State demos |

---

### CLO5 — Optimize Performance

> **"Students can optimize Streamlit application performance through caching, fragments, and lazy loading."**

**Bloom's Level:** Analyze

| Resource Type | Resource | Description |
|---|---|---|
| **Reading** | [R05 — Caching Internals](../readings/12_caching_and_performance.md) | Hash-based caching, TTL |
| **Notebook** | [N07 — Performance Engineering](../notebooks/12_caching_performance.ipynb) | Caching and fragments |
| **Notebook** | [N08 — Building Multipage Applications](../notebooks/13_application_architecture.ipynb) | Navigation performance |
| **Exercise** | [E07 — Cache Challenge](../exercises/12_caching_workshop.py) | Caching implementation |
| **Quiz** | [Q07 — Caching](../quizzes/08_caching_performance.md) | Cache strategy selection |
| **Assignment** | [Assignment 02 — Data Dashboard](../assignments/A02_data_explorer.md) | Performance-optimized dashboard |
| **Project** | [P04 — Real-Time Dashboard](../projects/P02_data_explorer.md) | Caching + fragments |
| **App Demo** | [caching_demo.py](../apps/12_caching_performance_demo.py) | Caching patterns |

---

### CLO6 — Design Well-Architected Applications

> **"Students can design well-structured Streamlit applications using proven architecture patterns."**

**Bloom's Level:** Apply, Analyze

| Resource Type | Resource | Description |
|---|---|---|
| **Reading** | [R07 — Architecture Patterns](../readings/13_application_architecture.md) | MVC-like patterns, components |
| **Notebook** | [N09 — Architecting Streamlit Apps](../notebooks/13_application_architecture.ipynb) | Design patterns |
| **Notebook** | [N08 — Building Multipage Applications](../notebooks/13_application_architecture.ipynb) | Multi-page structure |
| **Exercise** | [E08 — Multipage Navigator](../exercises/13_architecture_workshop.py) | Navigation design |
| **Exercise** | [E09 — Architecture Review](../exercises/13_architecture_workshop.py) | Architecture analysis |
| **Quiz** | [Q08 — Multipage](../quizzes/09_architecture_multipage.md) | Navigation patterns |
| **Quiz** | [Q09 — Architecture](../quizzes/09_architecture_multipage.md) | Architecture concepts |
| **Assignment** | [Assignment 03 — Full Stack App](../assignments/A03_multipage_application.md) | Full architecture exercise |
| **Project** | [P04 — Real-Time Dashboard](../projects/P02_data_explorer.md) | Architecture in practice |
| **App Demo** | [architecture_demo/](../apps/13_modular_app/), [multipage_demo/](../apps/13_modular_app/) | Pattern demos |

---

### CLO7 — Connect to Data Sources

> **"Students can connect Streamlit apps to databases and external APIs for persistent data and real-time information."**

**Bloom's Level:** Apply

| Resource Type | Resource | Description |
|---|---|---|
| **Reading** | [R08 — Database Design Basics](../readings/14_databases_and_persistence.md) | Schema design, ORM vs raw SQL |
| **Reading** | [R09 — API Design Patterns](../readings/13_application_architecture.md) | REST conventions, error handling |
| **Notebook** | [N10 — Database Connectivity](../notebooks/14_databases_persistence.ipynb) | SQL connections |
| **Notebook** | [N11 — API Integration](../notebooks/14_databases_persistence.ipynb) | REST APIs |
| **Exercise** | [E10 — Database CRUD](../exercises/14_database_workshop.py) | CRUD operations |
| **Exercise** | [E11 — API Fetcher](../exercises/09_api_connectors.py) | API consumption |
| **Quiz** | [Q10 — Databases](../quizzes/10_databases_persistence.md) | Database concepts |
| **Quiz** | [Q11 — APIs](../quizzes/10_databases_persistence.md) | API patterns |
| **Project** | [P05 — CRUD Database App](../projects/P14_database_dashboard.md) | Full database application |
| **App Demo** | [db_demo.py](../apps/14_database_dashboard.py), [api_demo.py](../apps/09_file_upload_demo.py) | Data integration demos |

---

### CLO8 — Deploy ML Models

> **"Students can deploy machine learning models as interactive Streamlit applications with explanations."**

**Bloom's Level:** Apply, Analyze

| Resource Type | Resource | Description |
|---|---|---|
| **Reading** | [R10 — ML Serving Patterns](../readings/15_machine_learning_streamlit.md) | Batch vs real-time, serialization |
| **Notebook** | [N12 — ML Dashboards](../notebooks/15_ml_streamlit.ipynb) | End-to-end ML deployment |
| **Exercise** | [E12 — ML Predictor](../exercises/15_ml_workshop.py) | Model deployment |
| **Quiz** | [Q12 — ML & AI](../quizzes/11_machine_learning.md) | ML concepts |
| **Assignment** | [Assignment 03 — Full Stack App](../assignments/A03_multipage_application.md) | ML integration |
| **Project** | [P06 — ML Model Playground](../projects/P06_ml_model_playground.md) | Interactive ML explorer |
| **App Demo** | [ml_demo.py](../apps/15_classification_app.py) | ML deployment demo |

---

### CLO9 — Build AI-Powered Applications

> **"Students can build AI-powered applications including chat interfaces and RAG systems."**

**Bloom's Level:** Apply, Create

| Resource Type | Resource | Description |
|---|---|---|
| **Reading** | [R11 — RAG Concepts](../readings/18_llm_rag_applications.md) | Embeddings, vector stores, chunking |
| **Notebook** | [N13 — Building AI-Powered Apps](../notebooks/18_llm_applications.ipynb) | LLM + RAG integration |
| **Exercise** | [E13 — Chatbot Builder](../exercises/18_llm_workshop.py) | Chat interface implementation |
| **Project** | [P07 — RAG Document Chat](../projects/P07_rag_document_chat.md) | Document Q&A application |
| **App Demo** | [ai_chat_demo.py](../apps/18_llm_chat.py) | Chat + RAG demo |

---

### CLO10 — Test and Secure Applications

> **"Students can apply testing, security best practices, and CI/CD to Streamlit applications."**

**Bloom's Level:** Evaluate

| Resource Type | Resource | Description |
|---|---|---|
| **Reading** | [R12 — Security Best Practices](../readings/security_and_secrets.md) | OWASP Top 10 for Streamlit |
| **Reading** | [R13 — Testing Strategies](../readings/13_application_architecture.md) | Unit vs integration vs e2e |
| **Notebook** | [N14 — Testing & Securing Apps](../notebooks/security_practical_lab.ipynb) | AppTest + security |
| **Exercise** | [E14 — Test Suite](../exercises/16_production_ready.py) | Test implementation |
| **Assessment** | [Midterm Practical](../assessments/practical_exam.md) | Testing and debugging |
| **Project** | [P08 — Capstone Project](../projects/final_capstone.md) | Full test suite required |
| **App Demo** | [test_demo.py](../apps/01_introduction_demo.py) | Testing patterns |

---

### CLO11 — Deploy to Production

> **"Students can deploy, monitor, and maintain Streamlit applications in production environments."**

**Bloom's Level:** Evaluate

| Resource Type | Resource | Description |
|---|---|---|
| **Reading** | [R14 — Deployment Options](../readings/deployment_guide.md) | Cloud, Docker, alternatives |
| **Reading** | [R15 — Production Checklist](../readings/deployment_guide.md) | Monitoring, logging, scaling |
| **Notebook** | [N15 — Deploy to the World](../notebooks/deployment_tutorial.ipynb) | Community Cloud deployment |
| **Notebook** | [N16 — Production Readiness](../notebooks/deployment_tutorial.ipynb) | Monitoring and maintenance |
| **Exercise** | [E15 — Deploy Pipeline](../exercises/deployment_exercises.py) | Deployment setup |
| **Exercise** | [E16 — Monitoring Setup](../exercises/16_production_ready.py) | Monitoring implementation |
| **Assignment** | [Assignment 04 — Production App](../assignments/A04_ml_production_app.md) | Deployed application |
| **Project** | [P08 — Capstone Project](../projects/final_capstone.md) | Full deployment |
| **App Demo** | [deployed_app/](../apps/deployable_app/) | Deployment reference |

---

### CLO12 — Execute Full Development Lifecycle

> **"Students can execute a complete software development lifecycle for a data application, from requirements to deployment."**

**Bloom's Level:** Create (highest)

| Resource Type | Resource | Description |
|---|---|---|
| **All readings** | [R01–R15](roadmap.md#quick-links) | Full conceptual foundation |
| **All notebooks** | [N01–N16](roadmap.md#module--resource-matrix) | Complete skill progression |
| **All exercises** | [E01–E16](roadmap.md#module--resource-matrix) | Applied practice |
| **All quizzes** | [Q01–Q12](roadmap.md#module--resource-matrix) | Knowledge validation |
| **Assignments** | [A01–A04](roadmap.md#assessment-milestones) | Graded milestones |
| **Capstone Project** | [P08 — Capstone](../projects/final_capstone.md) | End-to-end lifecycle |
| **Assessment** | [Capstone Rubric](../assessments/rubrics/capstone_rubric.md) | Final evaluation |

The capstone integrates all prior CLOs:
- CLO1–C2: App fundamentals and interactivity
- CLO3: Visualization strategy
- CLO4–C5: State management and performance
- CLO6: Architecture decisions
- CLO7: Data source integration
- CLO8–C9: ML/AI components
- CLO10: Testing and security
- CLO11: Deployment and monitoring

---

## Assessment ↔ CLO Mapping

| Assessment | CLOs Assessed | Bloom's Level | Weight |
|---|---|---|---|
| [Pre-Course Assessment](../quizzes/pre_course_assessment.md) | CLO1 | Remember, Understand | 5% |
| Weekly Quizzes (Q01–Q12) | CLO1–CLO8 | Remember, Understand | 10% |
| Exercises (E01–E16) | CLO1–CLO11 | Apply | 20% |
| Labs (in-class) | CLO2–CLO6 | Apply | 10% |
| [Assignment 01](../assignments/A01_personal_dashboard.md) | CLO2, CLO6 | Apply | 15% (total) |
| [Assignment 02](../assignments/A02_data_explorer.md) | CLO3, CLO4, CLO5 | Apply, Analyze | — |
| [Assignment 03](../assignments/A03_multipage_application.md) | CLO6, CLO7, CLO8 | Apply, Analyze | — |
| [Assignment 04](../assignments/A04_ml_production_app.md) | CLO10, CLO11 | Evaluate | — |
| [Midterm](../assessments/practical_exam.md) | CLO1–CLO6 | Analyze, Evaluate | 10% |
| Projects (P01–P07) | CLO2–CLO9 | Apply, Analyze, Create | 15% |
| [Capstone (P08)](../projects/final_capstone.md) | CLO1–CLO12 | All levels | 15% |

---

## Bloom's Taxonomy Reference

| Level | Description | Course Context |
|---|---|---|
| **Remember** | Recall facts and basic concepts | API names, widget functions, terminology |
| **Understand** | Explain ideas or concepts | Explain execution model, describe when to use caching |
| **Apply** | Use information in new situations | Build apps, implement widgets, connect to APIs |
| **Analyze** | Draw connections among ideas | Compare caching strategies, choose architecture patterns |
| **Evaluate** | Justify a stand or decision | Review security posture, assess deployment options |
| **Create** | Produce new or original work | Design and build complete applications, capstone project |

---

## Content Quality Standards

Every learning outcome must be traceable through the full chain:

```
Topic → Reading → Notebook → Exercise → Quiz → Assessment → Project
  │         │          │          │         │          │           │
  │         │          │          │         │          │           └─ Real-world application
  │         │          │          │         │          └─ Formal evaluation
  │         │          │          │         └─ Knowledge check
  │         │          │          └─ Applied practice
  │         │          └─ Guided exploration
  │         └─ Conceptual foundation
  └─ Module topic definition
```

This document serves as the **accountability layer**: if any link in this chain is missing for a CLO, it must be flagged and filled before the course is delivered.
