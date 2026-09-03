# P19 — AI-Powered Data Science Application

> **🚀 Project · Expert · M13–M16**
> *Build an application that combines ML predictions with LLM-powered insights.*
> Difficulty: ★★★★★ · Duration: 3 weeks · Weight: Part of 15% project grade

---

## Problem Statement

A business analyst team wants an AI assistant that not only shows data and predictions but also explains insights in natural language. Build an application that combines traditional ML with LLM-powered analysis and explanation.

---

## Learning Objectives

1. Integrate ML predictions with LLM explanations (CLO8, CLO9)
2. Build a conversational data analysis interface (CLO9)
3. Design a complex multi-component architecture (CLO6)
4. Handle multiple API integrations securely (CLO10)
5. Deploy a complete AI application (CLO11)

---

## Prerequisites

- Completed Modules 13–16
- ML model training and deployment
- LLM API usage
- RAG concepts

---

## Functional Requirements

| # | Requirement | Marks |
|---|-------------|-------|
| F1 | Data upload or built-in dataset | 4 |
| F2 | ML model: train or load, predict, show metrics | 8 |
| F3 | LLM integration: explain predictions in natural language | 8 |
| F4 | Chat interface for asking questions about the data | 8 |
| F5 | Dashboard: KPIs, charts, data table | 8 |
| F6 | Document upload for context (optional RAG) | 6 |
| F7 | Conversation history with session state | 5 |
| F8 | Secrets management for LLM API key | 5 |
| F9 | Error handling for API failures | 5 |
| F10 | Deployed on Community Cloud | 8 |
| F11 | Tests (unit + AppTest) | 5 |

**Total: 70 marks**

---

## Architecture

```
ai_data_app/
├── app.py
├── ml_engine.py         # ML training and prediction
├── llm_engine.py        # LLM integration and prompts
├── chat_manager.py      # Conversation state
├── data_processor.py    # Data handling
├── config.py
├── pages/
│   ├── dashboard.py
│   ├── predictions.py
│   └── chat.py
├── tests/
├── models/
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Evaluation Criteria

| Criteria | Marks |
|----------|-------|
| ML + LLM integration | 25 |
| Architecture quality | 15 |
| Chat interface | 10 |
| Deployment and testing | 13 |
| Documentation | 7 |
| **Total** | **70** |

---

## Extensions

- Add streaming LLM responses
- Add visualization of LLM reasoning
- Add multi-model comparison with LLM analysis
- Add automated report generation

---

## Related Materials

- 📖 Reading: [NLP Applications](../readings/17_nlp_ai_applications.md)
- 📖 Reading: [LLM/RAG](../readings/18_llm_rag_applications.md)
- 📖 Reading: [ML Streamlit](../readings/15_machine_learning_streamlit.md)
- 📋 Security: [Security Guide](../docs/security.md)
