# 🗺️ Teaching Roadmap

> **Streamlit for Data Science — Learn, Build, Deploy**
> *Module progression, prerequisites, and dependency chain for instructors.*

---

## Module Dependency Map

```
PHASE 1: FOUNDATION
M01 Fundamentals ──────────→ M02 Widgets ──────────→ M03 Layouts
   (Week 1)                    (Week 2)                 (Week 3)
   ▼                            ▼                        ▼
   No prereqs                  Requires M01            Requires M02

PHASE 2: DATA & VISUALIZATION
M04 Data Display ←────────── M05 Session State ──────→ M06 Files & Dashboards
   (Week 4)                    (Week 5)                  (Week 6)
   ▼                            ▼                         ▼
   Requires M01–M03           Requires M03             Requires M04, M05

PHASE 3: ARCHITECTURE
M07 Caching ────────────────→ M08 Architecture
   (Week 7)                    (Week 8)
   ▼                            ▼
   Requires M05               Requires M03, M07

M09 APIs ────────────────────→ M10 Databases
   (Week 9)                    (Week 9)
   ▼                            ▼
   Requires M06               Requires M06

PHASE 4: MACHINE LEARNING
M11 ML Intro ────────────────→ M12 ML Deploy ──────────→ M13 NLP
   (Week 10)                   (Week 11)                  (Week 12)
   ▼                            ▼                          ▼
   Requires M04–M07           Requires M11              Requires M12

PHASE 5: AI & PRODUCTION
M14 LLM/RAG ────────────────→ M15 Deployment ──────────→ M16 Production
   (Week 13)                   (Week 14)                  (Week 14)
   ▼                            ▼                          ▼
   Requires M12              Requires M06–M08           Requires M08, M15

PHASE 6: CAPSTONE
   All Modules ─────────────→ Capstone Project
                                (Weeks 15–16)
                                ▼
                                Requires all phases
```

---

## Module Summary Table

| Module | Title | Phase | Weeks | Prerequisites | Key Dependencies |
|--------|-------|-------|-------|---------------|------------------|
| M01 | Streamlit Fundamentals | Foundation | 1 | Python basics | None |
| M02 | Widgets & Input | Foundation | 2 | M01 | streamlit |
| M03 | Layouts & Dashboard UI | Foundation | 3 | M02 | streamlit |
| M04 | DataFrames & Visualization | Data | 4 | M01–M03 | pandas, matplotlib, plotly |
| M05 | Session State & Reruns | Data | 5 | M03 | streamlit session_state |
| M06 | File Upload & Dashboards | Data | 6 | M04, M05 | pandas, file I/O |
| M07 | Caching & Performance | Architecture | 7 | M05 | streamlit caching |
| M08 | Architecture & Multipage | Architecture | 8 | M03, M07 | streamlit.navigation |
| M09 | APIs & External Data | Architecture | 9 | M06 | requests, json |
| M10 | Database Integration | Architecture | 9 | M06 | sqlite3 |
| M11 | ML with Streamlit | ML | 10 | M04–M07 | scikit-learn, joblib |
| M12 | ML Model Deployment | ML | 11 | M11 | scikit-learn, streamlit |
| M13 | NLP & Text Analysis | ML | 12 | M12 | scikit-learn, transformers |
| M14 | LLM & RAG | AI/LLM | 13 | M12 | openai/transformers |
| M15 | Deployment & Community Cloud | Production | 14 | M06–M08 | git, Community Cloud |
| M16 | Production & Maintenance | Production | 14 | M08, M15 | logging, testing |

---

## Teaching Strategies by Phase

### Phase 1 — Foundation (Weeks 1–3)
**Goal:** Get every student running Streamlit apps confidently.

**Strategy:**
- Heavy live coding — build every app together
- Minimal theory, maximum hands-on
- Celebrate first working app as a milestone
- Pair stronger students with beginners during labs

**Common student concerns:**
- "Is this just another framework to learn?"
- "How is this different from Jupyter?"

**Response:** Build the same visualization in Jupyter and Streamlit side by side in Week 1. Show the immediate interactivity advantage.

---

### Phase 2 — Data & Visualization (Weeks 4–6)
**Goal:** Students can display any dataset interactively.

**Strategy:**
- Use real, messy datasets — not clean toy data
- Show the full PANDA→VISUALIZATION→STREAMLIT pipeline
- Emphasize widget-to-chart connections
- Session state is the hardest concept — spend extra time

**Common student struggles:**
- Understanding reruns
- Connecting widget output to chart input
- Session state initialization

**Response:** Draw the Streamlit execution model on the whiteboard. Show step by step what happens on each interaction.

---

### Phase 3 — Architecture (Weeks 7–9)
**Goal:** Students can build maintainable, non-trivial apps.

**Strategy:**
- Start with a messy single-file app, then refactor live
- Show the pain of not caching before teaching caching
- Multipage feels like a big jump — use the app store metaphor

**Common student struggles:**
- cache_data vs cache_resource
- When to use callbacks
- File organization

**Response:** The "refactor live" demo is powerful — show a 200-line app.py, then break it into modules while students watch.

---

### Phase 4 — Machine Learning (Weeks 10–12)
**Goal:** Students can deploy a trained model in a Streamlit app.

**Strategy:**
- Train a simple model first (sklearn), save it, then build the UI
- Emphasize: DO NOT retrain on every rerun
- Show the preprocessing trap (training vs inference mismatch)
- Keep models simple — accuracy is not the goal, deployment is

**Common student struggles:**
- Serialization/pickling concepts
- Feature engineering consistency
- Handling categorical inputs

**Response:** Build the prediction app together step by step. Use caching for model loading. Show the "wrong way" (training on every rerun) and measure the performance difference.

---

### Phase 5 — AI/LLM & Production (Weeks 13–14)
**Goal:** Students can build AI-powered apps and deploy them.

**Strategy:**
- Provide starter code for API calls — focus on Streamlit integration
- RAG is conceptual — don't expect full implementation from all students
- Security is a mindset, not a checklist
- Deployment day should feel like a celebration, not a panic

**Common student struggles:**
- API key management
- Understanding embeddings and vector stores
- Deployment failures

**Response:** Have a backup plan for every student whose deployment fails. Let them demo locally if needed, but require the attempt.

---

### Phase 6 — Capstone (Weeks 15–16)
**Goal:** Students demonstrate mastery through a complete project.

**Strategy:**
- Week 15: Dedicated work sessions with instructor roaming
- Peer debugging encouraged
- Presentation should be a demo, not a slide deck
- Grade the process (git history, milestones) not just the result

**Common student struggles:**
- Scope creep (too ambitious)
- Running out of time
- Deployment at the last minute

**Response:** Mandate milestone check-ins at Week 14 (proposal), Week 15 (working prototype), Week 16 (final). No-coding-on-presentation-day rule.

---

## Bloom's Taxonomy Progression

| Level | Where Emphasized | Modules |
|-------|------------------|---------|
| L1 — Remember | Foundation | M01, M02 |
| L2 — Understand | Foundation + Data | M01–M06 |
| L3 — Apply | Data + Architecture | M04–M10 |
| L4 — Analyze | Architecture + ML | M07–M13 |
| L5 — Evaluate | ML + Production | M11–M16 |
| L6 — Create | Capstone | Final Project |

---

## Pacing Guide

### If You're Behind Schedule
- Combine M09 (APIs) and M10 (Databases) into one session
- Reduce M13 (NLP) to a lecture-only session with demo
- Skip M16 (Production) deep-dive — cover essentials in M15

### If You're Ahead of Schedule
- Add a debugging workshop (common mistakes review)
- Run a mini-hackathon using M04–M06 skills
- Let students start capstone proposals early

### If Students Are Struggling
- Add an extra lab session for M05 (Session State) — the hardest concept
- Provide more scaffolded exercises for M08 (Architecture)
- Create a "catch-up" reading list for the foundation phase

---

## Related Materials

- [Course Plan](course_plan.md) — Weekly schedule
- [Session Plans](2_hour_lecture_plan.md) — Detailed per-session breakdown
- [Lab Activities](lab_activities.md) — Hands-on lab guides
- [Common Mistakes](common_student_mistakes.md) — Error catalog by module
- [Curriculum](../docs/curriculum.md) — Full curriculum design
