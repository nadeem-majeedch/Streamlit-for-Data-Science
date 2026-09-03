# P16 — LLM Chat Application

> **🚀 Project · AI/LLM · M13–M14**
> *Build a chat interface powered by an LLM with conversation history and context.*
> Difficulty: ★★★★☆ · Duration: 2 weeks · Weight: Part of 15% project grade

---

## Problem Statement

A company wants an internal AI assistant that employees can chat with for Data Science questions. Build a Streamlit chat application with conversation history, system prompts, and optional document context.

---

## Learning Objectives

1. Build a chat UI with `st.chat_message` and `st.chat_input` (CLO9)
2. Manage conversation state with session state (CLO4)
3. Implement provider abstraction for LLM APIs (CLO6)
4. Handle secrets securely (CLO10)
5. Implement streaming responses where supported (CLO9)

---

## Prerequisites

- Completed Modules 13–14
- Session state for conversation history
- `st.secrets` for API key management
- Understanding of LLM API patterns

---

## Functional Requirements

| # | Requirement | Marks |
|---|-------------|-------|
| F1 | Chat UI with `st.chat_message` for history display | 6 |
| F2 | User input with `st.chat_input` | 4 |
| F3 | Conversation history stored in session state | 6 |
| F4 | System prompt configuration (editable in sidebar) | 5 |
| F5 | LLM provider abstraction (Demo + at least one real provider) | 8 |
| F6 | Secrets management: API key from `st.secrets` | 5 |
| F7 | Clear conversation button | 3 |
| F8 | Conversation export as text/JSON | 4 |
| F9 | Input validation: length limits, empty message handling | 5 |
| F10 | Error handling for API failures | 5 |
| F11 | Message count and token estimate display | 4 |

**Total: 55 marks**

---

## Architecture

```
llm_chat/
├── app.py
├── providers.py        # LLM provider abstraction
├── conversation.py     # Conversation state management
├── config.py           # System prompts, settings
├── .streamlit/
│   └── secrets.toml    # API keys (gitignored)
├── requirements.txt
└── README.md
```

---

## Evaluation Criteria

| Criteria | Marks |
|----------|-------|
| Chat functionality | 25 |
| Architecture (provider abstraction) | 15 |
| Security (secrets, validation) | 10 |
| UX quality | 5 |
| **Total** | **55** |

---

## Extensions

- Add streaming responses with `st.write_stream`
- Add conversation branching (regenerate last response)
- Add markdown rendering in responses
- Add conversation search

---

## Related Materials

- 📖 Reading: [LLM/RAG Applications](../readings/18_llm_rag_applications.md)
- 📓 Notebook: [18 — LLM](../notebooks/18_llm_applications.ipynb)
- ✏️ Exercise: [18 — LLM](../exercises/18_llm_workshop.py)
- 🖥️ Demo: [18 — LLM Chat](../apps/18_llm_chat.py)
