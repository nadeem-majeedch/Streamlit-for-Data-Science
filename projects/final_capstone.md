# Final Capstone Project

> **🎓 Capstone · "Build and Deploy a Production-Style Data Science / AI Application with Streamlit"**
> *The culminating project of the course — demonstrate mastery of every learning outcome.*
> ⏱ Duration: 4 weeks (assigned Week 13, due Week 16) · 📊 Total: 200 marks · Difficulty: ★★★★★

---

## 1. Overview

This capstone project requires you to **identify a real-world problem, build a complete Streamlit application to address it, and deploy it to production**. You will go through the full software development lifecycle: requirements gathering, data acquisition, development, testing, security hardening, deployment, documentation, and presentation.

This is not a toy demo. By the end, you should have a **portfolio-quality application** that you could show to an employer or client.

### What Makes This Different From Other Projects

| Aspect | Other Projects | Capstone |
|--------|---------------|----------|
| Problem definition | Given to you | **You identify it** |
| Dataset | Provided | **You find/obtain it** |
| Scope | Focused on one topic | **Full-stack, all skills** |
| Deployment | Optional | **Required** |
| Testing | Encouraged | **Required with coverage** |
| Presentation | None | **10-minute live demo** |
| Documentation | Basic README | **Comprehensive documentation** |

---

## 2. Learning Outcomes

This project assesses **all 12 course learning outcomes**:

| CLO | Outcome | Bloom's | Where Assessed |
|-----|---------|---------|----------------|
| CLO1 | Explain Streamlit's execution model, architecture, and widget lifecycle | Understand | Presentation Q&A |
| CLO2 | Build interactive data applications using widgets, layouts, and state | Apply | Application functionality |
| CLO3 | Implement data visualization strategies | Apply | Charts and dashboards |
| CLO4 | Design and manage application state across reruns | Apply | Session state usage |
| CLO5 | Optimize performance through caching and fragments | Analyze | Caching strategy |
| CLO6 | Design well-structured applications using architecture patterns | Analyze | File structure, separation |
| CLO7 | Connect to databases and external APIs | Apply | Data layer |
| CLO8 | Deploy ML models as interactive Streamlit applications | Apply | ML/AI component |
| CLO9 | Build AI-powered applications | Apply | LLM/NLP integration (if applicable) |
| CLO10 | Apply testing, security best practices | Evaluate | Tests, security measures |
| CLO11 | Deploy, monitor, and maintain applications in production | Evaluate | Community Cloud deployment |
| CLO12 | Execute a complete software development lifecycle | Create | End-to-end project |

---

## 3. The 17-Step Capstone Workflow

You must complete ALL 17 steps. Each step has specific deliverables.

### Step 1: Identify a Real Problem (Week 13, Days 1–2)

**What to do:** Find a meaningful problem that a Streamlit app can solve.

**Requirements:**
- Must be a real problem (not made up for the course)
- Must have a data component (analysis, prediction, or both)
- Must benefit from interactivity (not just a static report)
- Must be achievable in 4 weeks with your skill level

**Deliverables:**
- [ ] Problem statement (2–3 paragraphs)
- [ ] Target users (who will use this app?)
- [ ] Value proposition (why is this useful?)
- [ ]可行性 assessment (can you build this in 4 weeks?)

**Examples of good problem statements:**
- "Small business owners struggle to understand their sales trends from raw CSV exports. I will build a dashboard that lets them upload sales data and see trends, top products, and forecasting."
- "Researchers need to quickly analyze text sentiment in survey responses. I will build an NLP tool that processes uploaded CSVs of open-ended responses and shows sentiment distribution."

---

### Step 2: Obtain a Suitable Dataset (Week 13, Days 2–3)

**What to do:** Find or create a dataset that supports your problem.

**Acceptable data sources:**
- Public datasets (Kaggle, UCI, government open data, Our World in Data)
- Generated synthetic data (clearly documented as synthetic)
- API data (with proper attribution)
- Your own data (with privacy considerations)

**Requirements:**
- At least 100 rows (for ML tasks) or meaningful volume
- At least 3 numeric + 2 categorical columns (or appropriate types for your domain)
- Document data source, license, and any preprocessing needed
- No personally identifiable information (PII) without explicit consent

**Deliverables:**
- [ ] Dataset file(s) in `data/` directory
- [ ] Data source documentation (where it came from, license)
- [ ] Data dictionary (column descriptions, types, ranges)

---

### Step 3: Process the Data (Week 13, Days 3–5)

**What to do:** Clean, transform, and prepare your data for analysis.

**Requirements:**
- Handle missing values (document your strategy)
- Handle duplicates
- Convert data types as needed
- Create derived features if useful
- All processing in reusable functions (not top-level code)

**Deliverables:**
- [ ] Data processing functions in a separate module
- [ ] Documentation of cleaning decisions
- [ ] Processed data ready for visualization and modeling

---

### Step 4: Build Analysis / Model / AI Workflow (Week 13–14)

**What to do:** Implement the core data science or AI workflow.

**Requirements (choose at least one):**
- **Analysis workflow:** Statistical analysis, trend detection, anomaly detection
- **ML workflow:** Train a model, evaluate it, make predictions
- **AI workflow:** LLM integration, NLP processing, RAG pipeline

**For ML projects specifically:**
- Train/test split with `random_state` for reproducibility
- At least one classification OR regression model
- Save model artifacts with joblib
- Display model performance metrics

**Deliverables:**
- [ ] Model training or analysis code
- [ ] Saved model artifacts (if ML)
- [ ] Performance metrics displayed in app

---

### Step 5: Design Streamlit UI (Week 14, Days 1–3)

**What to do:** Design the user interface before coding.

**Requirements:**
- Sketch or wireframe your layout (even rough pencil sketch is fine)
- Plan page structure (multipage or single-page with tabs)
- Design sidebar controls
- Plan where KPIs, charts, and tables go
- Consider user flow (what does the user see first? what do they do next?)

**Deliverables:**
- [ ] Layout sketch/wireframe (photo or digital)
- [ ] Page structure plan
- [ ] Widget inventory (list all widgets you'll need)

---

### Step 6: Implement Validation (Week 14, Days 3–5)

**What to do:** Validate all user inputs and data.

**Requirements:**
- Validate file uploads (type, size, content)
- Validate numeric inputs (range, type)
- Validate text inputs (length, format)
- Show clear error messages for invalid inputs
- Never crash on bad input

**Deliverables:**
- [ ] Input validation functions
- [ ] Error messages for each validation case
- [ ] App handles edge cases gracefully

---

### Step 7: Visualize Results (Week 14, Days 3–5)

**What to do:** Create clear, informative visualizations.

**Requirements:**
- At least 4 different chart types
- Charts update with filter changes
- Clear titles, labels, and legends
- Appropriate chart types for the data
- At least one Plotly interactive chart

**Deliverables:**
- [ ] All visualizations implemented
- [ ] Charts respond to user interactions
- [ ] Visual inspection for clarity and correctness

---

### Step 8: Integrate ML/AI Where Appropriate (Week 14–15)

**What to do:** Add machine learning or AI capabilities.

**Requirements (choose at least one):**
- **Classification:** Predict a category with confidence scores
- **Regression:** Predict a continuous value with error bounds
- **Clustering:** Group data into segments
- **NLP:** Text analysis, sentiment, classification
- **LLM:** Chat interface, document Q&A, text generation

**Must include:**
- Feature input UI (sliders, text inputs, etc.)
- Prediction output with confidence/explanation
- Model information panel
- Preprocessing consistency (same at train and inference)

**Deliverables:**
- [ ] Working prediction/analysis interface
- [ ] Model cached with `@st.cache_resource`
- [ ] Preprocessing saved and reused

---

### Step 9: Manage Application State (Week 14–15)

**What to do:** Implement proper state management.

**Requirements:**
- Session state for filter persistence
- Session state for prediction history (if applicable)
- Session state for user preferences
- No state bugs (variables resetting on rerun)

**Deliverables:**
- [ ] All stateful values in `st.session_state`
- [ ] No state-related bugs
- [ ] State initialization handled correctly

---

### Step 10: Optimize Performance (Week 15)

**What to do:** Ensure the app is fast and efficient.

**Requirements:**
- `@st.cache_data` for expensive data computations
- `@st.cache_resource` for model/database connections
- No redundant computations on rerun
- App loads within 15 seconds
- Interactions respond within 3 seconds

**Deliverables:**
- [ ] Caching decorators applied where needed
- [ ] Performance tested (time key operations)
- [ ] No unnecessary rerun computations

---

### Step 11: Secure Secrets (Week 15)

**What to do:** Implement security best practices.

**Requirements:**
- No hardcoded API keys, passwords, or tokens
- `.streamlit/secrets.toml` in `.gitignore`
- Secrets accessed via `st.secrets` with fallback
- Input sanitization where applicable
- No `exec()` or `eval()` calls

**Deliverables:**
- [ ] `.gitignore` includes secrets files
- [ ] No secrets in source code
- [ ] Secrets documentation in README

---

### Step 12: Create requirements.txt (Week 15)

**What to do:** Document all dependencies.

**Requirements:**
- All imported packages listed
- Version pins (using `>=` or `==`)
- No development-only packages (jupyter, ipython)
- Minimal — only what the app actually uses

**Deliverables:**
- [ ] `requirements.txt` at repo root
- [ ] `requirements-dev.txt` for testing (optional)
- [ ] All imports verified

---

### Step 13: Create GitHub Repository (Week 15)

**What to do:** Set up proper version control.

**Requirements:**
- Clean repository structure
- `.gitignore` configured (secrets, __pycache__, model files, data)
- Meaningful commit messages
- At least 5 commits showing development progress

**Deliverables:**
- [ ] GitHub repository with clean history
- [ ] Proper `.gitignore`
- [ ] All files committed (no untracked sensitive files)

---

### Step 14: Deploy to Streamlit Community Cloud (Week 15)

**What to do:** Deploy your application.

**Requirements:**
- App deployed on Community Cloud
- Deployment URL accessible
- Entry point correctly configured
- `requirements.txt` at root
- All features work in deployed version

**Deliverables:**
- [ ] Live deployment URL
- [ ] Verified: all features work in cloud
- [ ] Verified: no hardcoded paths or secrets

---

### Step 15: Test Deployment (Week 15–16)

**What to do:** Verify the deployed application thoroughly.

**Requirements:**
- Test every feature in the deployed version
- Test with different browsers if possible
- Check for cold start time
- Verify error handling works
- Check mobile/responsive behavior (if applicable)

**Deliverables:**
- [ ] Deployment testing checklist completed
- [ ] All issues fixed
- [ ] Performance acceptable

---

### Step 16: Document the Project (Week 16)

**What to do:** Create comprehensive documentation.

**Requirements:**
- README.md with: title, description, features, setup, deployment link, screenshots, data sources, limitations
- Code documentation: docstrings, comments, type hints
- Architecture documentation: file structure, design decisions
- At least 4 screenshots of the running app

**Deliverables:**
- [ ] Complete README.md
- [ ] Code documented with docstrings
- [ ] Screenshots in `screenshots/` directory
- [ ] Architecture diagram (text-based is fine)

---

### Step 17: Present the Application (Week 16)

**What to do:** Present your work to the class.

**Requirements:**
- 10-minute presentation (8 min demo + 2 min Q&A)
- Live demonstration of the deployed application
- Explain architecture and key design decisions
- Discuss challenges and how you overcame them
- Answer technical questions from instructor/class

**Deliverables:**
- [ ] Presentation slides (optional but recommended)
- [ ] Live demo ready
- [ ] Prepared to answer technical questions

---

## 4. Project Categories

Choose ONE category for your capstone:

### Category A: Analytics Dashboard
Build a data analysis and visualization dashboard.
- Must include: data upload/loading, filters, KPIs, 4+ charts, export
- ML optional but recommended
- Examples: Sales analytics, health monitoring, financial tracker

### Category B: ML Prediction App
Build an application centered around machine learning predictions.
- Must include: model training/loading, prediction UI, batch prediction, model explanation
- Examples: Churn predictor, risk calculator, recommendation engine

### Category C: NLP/Text Application
Build a text analysis or natural language processing application.
- Must include: text input, analysis results, visualization of text insights
- Examples: Sentiment analyzer, topic classifier, text summarizer

### Category D: AI Assistant
Build an LLM-powered application.
- Must include: chat interface, conversation history, secrets management
- Examples: Data science chatbot, document Q&A, code assistant

### Category E: Full-Stack Data App
Build an application combining multiple technologies.
- Must include: database, ML/AI, deployment, testing
- Examples: End-to-end data pipeline, multi-source aggregator

---

## 5. Required Project Structure

```
capstone/
├── app.py                      # Entry point
├── config.py                   # Configuration constants
├── data_loader.py              # Data loading functions
├── data_processing.py          # Data transformation functions
├── model_utils.py              # ML/AI functions (if applicable)
├── components.py               # Reusable UI components
├── pages/                      # Multipage navigation
│   ├── __init__.py
│   ├── home.py                 # Overview / dashboard
│   ├── explore.py              # Data exploration
│   ├── predict.py              # ML/AI predictions (if applicable)
│   ├── chat.py                 # Chat interface (if applicable)
│   └── about.py                # About / methodology
├── tests/
│   ├── __init__.py
│   ├── test_data.py            # Tests for data functions
│   ├── test_model.py           # Tests for model functions (if applicable)
│   └── test_app.py             # Streamlit AppTest tests
├── models/                     # Saved model artifacts
│   └── .gitkeep
├── data/                       # Dataset files
│   └── .gitkeep
├── docs/                       # Additional documentation
│   └── architecture.md
├── screenshots/                # App screenshots
│   ├── dashboard.png
│   ├── exploration.png
│   ├── predictions.png
│   └── deployed.png
├── .gitignore
├── requirements.txt
├── README.md
└── CAPSTONE_REPORT.md          # Optional: detailed project report
```

---

## 6. Timeline & Milestones

| Week | Day | Milestone | Deliverable | Marks |
|------|-----|-----------|-------------|-------|
| 13 | 1–2 | **Problem & Data** | Problem statement, dataset, data dictionary | 20 |
| 13 | 3–5 | **Processing & Design** | Clean data, UI wireframe, architecture plan | 20 |
| 14 | 1–3 | **Core Development** | Data loading, filters, visualizations working | 30 |
| 14 | 3–5 | **ML/AI Integration** | Model working, prediction UI, state management | 30 |
| 15 | 1–3 | **Testing & Security** | Tests passing, security measures, caching | 30 |
| 15 | 3–5 | **Deployment** | Deployed on Community Cloud, verified | 20 |
| 16 | 1–2 | **Documentation** | README, screenshots, code documentation | 20 |
| 16 | 3–5 | **Presentation** | 10-minute live demo + Q&A | 30 |
| | | | **Total** | **200** |

### Milestone 1: Project Plan (Due end of Week 13)
Submit:
1. Problem statement and justification
2. Dataset description and data dictionary
3. Feature list (prioritized: must-have, should-have, nice-to-have)
4. Architecture diagram
5. UI wireframe/sketch
6. Technology choices and justification

### Milestone 2: Working Prototype (Due end of Week 14)
Submit:
1. Data loading and processing working
2. Interactive filters functional
3. At least 2 visualizations rendered
4. ML/AI component working (at least basic)
5. Session state implemented
6. App runs locally without errors

### Milestone 3: Pre-Deployment (Due end of Week 15)
Submit:
1. All features implemented
2. Tests passing (`pytest tests/ -v`)
3. Security measures applied
4. `requirements.txt` correct
5. Deployed on Community Cloud
6. Deployment URL provided

### Milestone 4: Final Submission (Due end of Week 16)
Submit:
1. Complete application deployed
2. README with screenshots
3. Code documented
4. Presentation ready
5. All deliverables complete

---

## 7. Minimum Viable Product (MVP) vs. Excellence

### MVP (Passing Grade: C, 100–119 marks)
- App solves a real problem
- Data loading and basic filtering
- At least 2 visualizations
- One ML model or AI component
- Deployed on Community Cloud
- Basic README
- Tests exist (may not have full coverage)

### Good (Grade: B, 120–159 marks)
Everything in MVP plus:
- Clean modular architecture
- 4+ chart types
- Proper caching
- Session state for persistence
- Comprehensive testing
- Security measures
- Detailed documentation with screenshots

### Excellent (Grade: A, 160–200 marks)
Everything in Good plus:
- Innovative features beyond requirements
- Professional UX design
- Advanced ML/AI with explanation
- Performance optimized
- Accessibility considerations
- Thoughtful architecture decisions
- Polished presentation

---

## 8. Educational vs. Production Expectations

This is a **university course project**, not a production deployment. Understand the difference:

| Aspect | Educational Expectation | Production Expectation |
|--------|------------------------|----------------------|
| Authentication | Optional (bonus marks) | Required |
| Database | SQLite acceptable | PostgreSQL/Cloud DB |
| Testing | Basic coverage OK | 80%+ coverage, CI/CD |
| Security | No hardcoded secrets | Full security audit |
| Performance | Works for demo | Handles 1000+ concurrent users |
| Monitoring | Screenshot of logs | APM, alerting, dashboards |
| Documentation | README + code comments | API docs, runbooks, ADRs |
| Deployment | Community Cloud free tier | Production infrastructure |
| Model | Single model OK | Model registry, A/B testing |
| Data | Static or generated | Real-time, validated, governed |

**We grade on educational quality, not production scale.** A well-architected app with clean code and good documentation will score higher than a complex but messy app.

---

## 9. Common Mistakes to Avoid

1. ❌ **Spending too long on planning, not enough on building**
2. ❌ **Choosing a problem that's too ambitious for 4 weeks**
3. ❌ **Not deploying** (lose 20 marks immediately)
4. ❌ **No tests** (lose 15+ marks)
5. ❌ **All code in one file** (lose architecture marks)
6. ❌ **Charts don't update with filters** (looks broken)
7. ❌ **Missing requirements.txt** (deployment fails)
8. ❌ **Hardcoded secrets** (security failure)
9. ❌ **No README or screenshots** (documentation marks lost)
10. ❌ **Poor time management** — rushing in Week 16

---

## 10. Academic Integrity

### Acceptable
- Using course materials as reference
- Using official documentation (Streamlit, scikit-learn, etc.)
- Using Stack Overflow for syntax help
- Using AI coding assistants for snippets (must declare in README)
- Using public datasets

### NOT Acceptable
- Copying code from other students
- Submitting someone else's project
- Using pre-built Streamlit templates without understanding
- Plagiarizing documentation or reports
- Submitting work from previous courses without disclosure

### AI Declaration
If you used AI assistants (GitHub Copilot, ChatGPT, etc.), include this in your README:

```
## AI Assistance Declaration
I used [tool name] for:
- [specific purpose, e.g., "generating boilerplate code for file upload"]
- [specific purpose, e.g., "debugging a caching issue"]

I understand all code I have submitted and can explain every decision.
```

---

## 11. Submission Format

### GitHub Repository
```
capstone_yourname/
├── [all project files as specified in Section 5]
```

### Submission Links (submit all three)
1. **GitHub Repository URL**
2. **Community Cloud Deployment URL**
3. **Presentation slides** (if using)

### What the Instructor Will Check
1. Repository exists and is accessible
2. Deployment URL works
3. App runs locally from fresh clone
4. Tests pass
5. No hardcoded secrets
6. README is complete

---

## 12. Extensions & Bonus Opportunities

| Extension | Bonus Marks | Description |
|-----------|-------------|-------------|
| Streaming LLM responses | +5 | Use `st.write_stream` for real-time generation |
| Real-time data updates | +5 | Use `st.fragment(run_every=...)` for live data |
| Multi-language support | +3 | Internationalization with session state |
| Dark mode toggle | +2 | Theme switching with `st.theme` |
| API endpoint | +5 | REST API for programmatic access |
| CI/CD pipeline | +5 | GitHub Actions for automated testing |
| Accessibility audit | +3 | WCAG compliance checks |
| Performance benchmarking | +3 | Detailed timing analysis |

Maximum bonus: 15 marks (capped)

---

## 13. Getting Help

### Resources Available
- **Instructor office hours** — Bring specific questions
- **Course readings** — All topics covered in modules
- **Peer collaboration** — Discuss ideas, not code
- **Documentation** — Streamlit docs, scikit-learn docs
- **Community** — Stack Overflow, Streamlit forum

### When to Ask for Help
- Stuck on a problem for more than 2 hours
- Unsure about architecture decisions
- Deployment issues you can't resolve
- Need feedback on your approach

### What to Include When Asking
- What you're trying to do
- What you've tried
- Error messages (full traceback)
- Screenshots if visual issue

---

## Related Materials

- 📋 Rubric: [capstone_rubric.md](capstone_rubric.md)
- ✅ Checklist: [capstone_submission_checklist.md](capstone_submission_checklist.md)
- 🎤 Presentation: [capstone_presentation.md](capstone_presentation.md)
- 📋 Learning Outcomes: [docs/learning_outcomes.md](../docs/learning_outcomes.md)
- 📋 Curriculum: [docs/curriculum.md](../docs/curriculum.md)
- 📋 Deployment Checklist: [docs/deployment_checklist.md](../docs/deployment_checklist.md)
- 📋 Security Guide: [docs/security.md](../docs/security.md)
- 📋 Troubleshooting: [docs/deployment_troubleshooting.md](../docs/deployment_troubleshooting.md)
- 📖 All Readings: [readings/](../readings/)
- 📓 All Notebooks: [notebooks/](../notebooks/)
