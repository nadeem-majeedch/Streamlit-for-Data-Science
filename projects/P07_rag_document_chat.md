# P07 — RAG Document Chat

> **🚀 Project · Module 13 · AI/LLM**  
> *Build a document question-answering application with Retrieval-Augmented Generation.*

---

## Project Overview

Create a Streamlit application that allows users to:
1. Upload documents (PDF, TXT, MD)
2. Process and index document content
3. Ask questions about the documents
4. Get answers with source references
5. Chat with context from uploaded documents

This project demonstrates RAG (Retrieval-Augmented Generation) for document Q&A.

---

## Learning Objectives

By completing this project, you will be able to:

- Implement document processing pipelines
- Build vector embeddings for semantic search
- Create retrieval-augmented generation systems
- Design conversational UI with chat interfaces
- Handle document state management
- Implement source attribution

---

## Functional Requirements

### 1. Document Upload
- [ ] Support PDF, TXT, and Markdown files
- [ ] Display document preview
- [ ] Show document statistics (pages, words, characters)
- [ ] Handle multiple documents

### 2. Document Processing
- [ ] Extract text from documents
- [ ] Split into chunks with overlap
- [ ] Generate embeddings
- [ ] Store in vector database

### 3. Question Answering
- [ ] Accept user questions
- [ ] Retrieve relevant document chunks
- [ ] Generate answers with context
- [ ] Show source references

### 4. Chat Interface
- [ ] Conversational UI
- [ ] Chat history
- [ ] Context-aware responses
- [ ] Clear conversation option

---

## UI Requirements

### Layout
```
┌─────────────────────────────────────────────────────┐
│  Sidebar                           │  Main Content  │
│  ─────────                         │  ───────────── │
│  • Document upload                 │  • Chat area   │
│  • Document list                   │  • Source refs  │
│  • Settings                        │  • Input box   │
└─────────────────────────────────────────────────────┘
```

### Pages/Tabs
1. **Chat** — Main question-answering interface
2. **Documents** — Upload and manage documents
3. **Settings** — Configuration options

---

## Technical Requirements

### Document Processing
- Text extraction from PDF/TXT/MD
- Chunking with configurable size and overlap
- Metadata preservation

### Vector Storage
- In-memory vector store (ChromaDB or similar)
- Embedding generation (sentence-transformers or OpenAI)
- Similarity search

### Generation
- LLM integration (OpenAI, local models, or prompt templates)
- Context injection
- Source attribution

### Caching
- Cache document processing
- Cache embeddings
- Cache query results

---

## Implementation Guide

### Step 1: Project Structure

```
P07_rag_chat/
├── app.py                 # Main entry point
├── pages/
│   ├── chat.py           # Chat interface
│   ├── documents.py      # Document management
│   └── settings.py       # Configuration
├── utils/
│   ├── __init__.py
│   ├── document_processor.py  # Text extraction
│   ├── embeddings.py          # Vector embeddings
│   ├── vector_store.py        # Vector database
│   └── llm.py                 # LLM integration
├── requirements.txt
└── README.md
```

### Step 2: Document Processor

```python
# utils/document_processor.py
import streamlit as st
from pathlib import Path

def extract_text(file_path):
    """Extract text from document."""
    suffix = Path(file_path).suffix.lower()
    
    if suffix == ".txt" or suffix == ".md":
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    
    elif suffix == ".pdf":
        # Use PyPDF2 or pdfplumber
        import PyPDF2
        with open(file_path, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            return "\n".join(page.extract_text() for page in reader.pages)
    
    return ""

def chunk_text(text, chunk_size=500, overlap=50):
    """Split text into chunks."""
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start = end - overlap
    return chunks
```

### Step 3: Vector Store

```python
# utils/vector_store.py
import streamlit as st

@st.cache_resource
def get_vector_store():
    """Get or create vector store."""
    import chromadb
    return chromadb.Client()

def add_documents(texts, metadatas=None):
    """Add documents to vector store."""
    store = get_vector_store()
    collection = store.get_or_create_collection("documents")
    
    # Generate embeddings
    # Add to collection
    ...

def search(query, n_results=5):
    """Search for relevant documents."""
    store = get_vector_store()
    collection = store.get_collection("documents")
    return collection.query(query_texts=[query], n_results=n_results)
```

### Step 4: Chat Interface

```python
# pages/chat.py
import streamlit as st
from utils.vector_store import search

def chat_page():
    st.header("💬 Chat with Documents")
    
    # Chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    # Display history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])
    
    # Input
    if query := st.chat_input("Ask a question..."):
        # Add user message
        st.session_state.messages.append({"role": "user", "content": query})
        
        # Search for relevant documents
        results = search(query)
        
        # Generate answer
        context = "\n".join(results["documents"][0])
        answer = generate_answer(query, context)
        
        # Add assistant message
        st.session_state.messages.append({"role": "assistant", "content": answer})
        
        # Display
        with st.chat_message("assistant"):
            st.write(answer)
```

---

## Experiments to Try

1. **Chunk size** — Test different chunk sizes (256, 512, 1024)
2. **Overlap** — Compare no overlap vs. 10% overlap
3. **Embedding models** — Compare different embedding models
4. **Retrieval count** — Test different numbers of retrieved chunks
5. **Prompt templates** — Experiment with different prompt formats

---

## Common Mistakes to Avoid

1. ❌ Processing documents on every query (use caching)
2. ❌ Losing document metadata during processing
3. ❌ Not handling different file formats
4. ❌ Poor chunk boundaries (splitting mid-sentence)
5. ❌ Not showing source references

---

## Testing Checklist

- [ ] PDF text extraction works
- [ ] TXT/MD text extraction works
- [ ] Document chunking produces reasonable chunks
- [ ] Similarity search returns relevant results
- [ ] Chat interface maintains history
- [ ] Source references are displayed
- [ ] Multiple documents can be uploaded
- [ ] Error handling for unsupported formats

---

## Extension Ideas

1. **Multi-modal** — Support images with OCR
2. **Citations** — Link answers to specific document sections
3. **Summarization** — Generate document summaries
4. **Comparison** — Compare information across documents
5. **Export** — Export chat history as PDF/Markdown
6. **Authentication** — User accounts and document access control

---

## Grading Rubric

| Component | Points | Criteria |
|-----------|--------|----------|
| **Functionality** | 35 | All features work correctly |
| **UI/UX** | 20 | Intuitive chat interface |
| **Code Quality** | 20 | Clean, modular, well-documented |
| **RAG Implementation** | 15 | Proper retrieval and generation |
| **Error Handling** | 10 | Graceful failure for edge cases |

---

## Optional Dependencies

```txt
# For PDF processing
PyPDF2>=3.0.0
# OR
pdfplumber>=0.10.0

# For embeddings
sentence-transformers>=2.2.0
# OR
openai>=1.0.0

# For vector store
chromadb>=0.4.0
# OR
faiss-cpu>=1.7.0

# For LLM
openai>=1.0.0
# OR
llama-cpp-python>=0.2.0
```

---

## Submission

1. Push code to GitHub repository
2. Deploy to Streamlit Community Cloud (if applicable)
3. Submit repository URL
4. Include README with:
   - Setup instructions
   - Feature list
   - Screenshots
   - Sample documents for testing

---

## Related Materials

- 📖 Reading: [17 — NLP & AI Applications](../readings/17_nlp_ai_applications.md)
- 📓 Notebook: [17 — NLP Applications](../notebooks/17_nlp_applications.ipynb)
- 🖥️ Demo App: [17 — Sentiment Analyzer](../apps/17_sentiment_app.py)
- 📝 Quiz: [13 — NLP & AI](../quizzes/13_nlp_ai.md)
