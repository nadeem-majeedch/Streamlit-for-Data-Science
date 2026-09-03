# P17 — Document Q&A Application

> **🚀 Project · AI/LLM · M13–M14**
> *Build a RAG-based document question answering system.*
> Difficulty: ★★★★★ · Duration: 2.5 weeks · Weight: Part of 15% project grade

---

## Problem Statement

Legal and research teams need to quickly find answers within large document collections. Build a Streamlit app that lets users upload documents, ask questions, and receive answers grounded in the uploaded content using RAG (Retrieval-Augmented Generation).

---

## Learning Objectives

1. Implement document upload and text extraction (CLO2)
2. Build a text chunking pipeline (CLO9)
3. Create a vector-based retrieval system (CLO9)
4. Integrate retrieval with LLM generation (CLO9)
5. Design a user-friendly Q&A interface (CLO6)

---

## Prerequisites

- Completed Modules 13–14
- Text chunking concepts
- Embedding concepts (even at a high level)
- LLM API usage

---

## Functional Requirements

| # | Requirement | Marks |
|---|-------------|-------|
| F1 | Document upload: support TXT, CSV, MD files | 5 |
| F2 | Text extraction and chunking (configurable chunk size) | 8 |
| F3 | Simple keyword-based or embedding-based retrieval | 10 |
| F4 | Question input with chat-like interface | 5 |
| F5 | Answer generation using retrieved context | 8 |
| F6 | Display source chunks used for answer | 6 |
| F7 | Conversation history with session state | 5 |
| F8 | Document management: list uploaded docs, delete | 5 |
| F9 | Configuration: chunk size, top-k retrieval, system prompt | 6 |
| F10 | Error handling for API failures and empty documents | 4 |

**Total: 62 marks**

---

## Architecture

```
document_qa/
├── app.py
├── document_processor.py  # Upload, extract, chunk
├── retriever.py           # Search and retrieval
├── generator.py           # LLM answer generation
├── conversation.py        # Chat state management
├── config.py
├── documents/             # Uploaded documents (gitignored)
├── requirements.txt
└── README.md
```

---

## Evaluation Criteria

| Criteria | Marks |
|----------|-------|
| RAG pipeline quality | 25 |
| Document processing | 15 |
| Q&A interface | 10 |
| Source attribution | 5 |
| Code quality | 5 |
| **Total** | **62** |

---

## Extensions

- Add PDF document support
- Add embedding-based semantic search
- Add answer confidence scoring
- Add document highlighting (show where answer came from)

---

## Related Materials

- 📖 Reading: [LLM/RAG Applications](../readings/18_llm_rag_applications.md)
- 📓 Notebook: [18 — LLM](../notebooks/18_llm_applications.ipynb)
- ✏️ Exercise: [18 — LLM](../exercises/18_llm_workshop.py)
- 🖥️ Demo: [18 — RAG App](../apps/18_rag_app.py)
- 🚀 Project: [P07 — RAG Chat](P07_rag_document_chat.md)
