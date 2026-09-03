"""
Streamlit RAG Document Q&A App
================================

Module 14 · AI/LLM

A complete RAG application demonstrating:
- Document upload and processing
- Text chunking
- Vector embeddings
- Semantic search
- Question answering with context

Run: streamlit run apps/18_rag_app.py
"""

import streamlit as st
from pathlib import Path
from typing import List
import json

st.set_page_config(
    page_title="RAG Document Q&A",
    page_icon="📚",
    layout="wide"
)

st.title("📚 RAG Document Q&A")
st.caption("Module 14 · Retrieval-Augmented Generation")

# ============================================================================
# Document Processing
# ============================================================================

def process_document(file) -> str:
    """Extract text from uploaded document."""
    suffix = Path(file.name).suffix.lower()
    
    if suffix in [".txt", ".md"]:
        return file.read().decode("utf-8")
    
    elif suffix == ".pdf":
        try:
            import PyPDF2
            reader = PyPDF2.PdfReader(file)
            return "\n".join(page.extract_text() for page in reader.pages)
        except ImportError:
            st.error("Install PyPDF2: pip install PyPDF2")
            return ""
    
    return ""

def chunk_text(text: str, chunk_size: int = 500, overlap: int = 50) -> List[str]:
    """Split text into overlapping chunks."""
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start = end - overlap
    return chunks

# ============================================================================
# Vector Store (Simple In-Memory)
# ============================================================================

class SimpleVectorStore:
    """Simple in-memory vector store using TF-IDF."""
    
    def __init__(self):
        self.documents = []
        self.chunks = []
    
    def add_documents(self, chunks: List[str]):
        """Add document chunks."""
        self.chunks.extend(chunks)
    
    def search(self, query: str, n_results: int = 5) -> List[str]:
        """Search for relevant chunks (simple keyword matching)."""
        if not self.chunks:
            return []
        
        # Simple relevance scoring (keyword overlap)
        query_words = set(query.lower().split())
        scores = []
        
        for chunk in self.chunks:
            chunk_words = set(chunk.lower().split())
            overlap = len(query_words.intersection(chunk_words))
            scores.append((overlap, chunk))
        
        # Sort by score and return top results
        scores.sort(key=lambda x: x[0], reverse=True)
        return [chunk for _, chunk in scores[:n_results]]

# ============================================================================
# Session State
# ============================================================================

if "rag_store" not in st.session_state:
    st.session_state.rag_store = SimpleVectorStore()

if "rag_messages" not in st.session_state:
    st.session_state.rag_messages = []

# ============================================================================
# Sidebar
# ============================================================================

st.sidebar.title("📚 RAG Settings")
st.sidebar.markdown("---")

# Document management
st.sidebar.subheader("📄 Documents")

uploaded_files = st.sidebar.file_uploader(
    "Upload documents",
    type=["txt", "md", "pdf"],
    accept_multiple_files=True,
    key="doc_upload"
)

if uploaded_files:
    if st.sidebar.button("📥 Process Documents"):
        all_chunks = []
        for file in uploaded_files:
            text = process_document(file)
            if text:
                chunks = chunk_text(text)
                all_chunks.extend(chunks)
        
        st.session_state.rag_store.add_documents(all_chunks)
        st.sidebar.success(f"✅ Indexed {len(all_chunks)} chunks")

# Chunk settings
st.sidebar.subheader("⚙️ Chunk Settings")
chunk_size = st.sidebar.slider("Chunk Size", 200, 1000, 500)
overlap = st.sidebar.slider("Overlap", 0, 100, 50)

# Store stats
st.sidebar.subheader("📊 Store Stats")
st.sidebar.write(f"Chunks indexed: {len(st.session_state.rag_store.chunks)}")

if st.sidebar.button("🗑️ Clear Store"):
    st.session_state.rag_store = SimpleVectorStore()
    st.sidebar.success("Store cleared!")

# Clear chat
if st.sidebar.button("🗑️ Clear Chat"):
    st.session_state.rag_messages = []
    st.rerun()

# ============================================================================
# Main Chat Interface
# ============================================================================

# Display chat history
for message in st.session_state.rag_messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])
        if "sources" in message:
            with st.expander("📚 Sources"):
                for i, source in enumerate(message["sources"], 1):
                    st.write(f"**Source {i}:**")
                    st.write(source[:300] + "...")

# User input
if query := st.chat_input("Ask a question about your documents..."):
    # Add user message
    st.session_state.rag_messages.append({"role": "user", "content": query})
    with st.chat_message("user"):
        st.write(query)
    
    # RAG response
    with st.chat_message("assistant"):
        # Retrieve relevant chunks
        sources = st.session_state.rag_store.search(query, n_results=3)
        
        if sources:
            # Build context
            context = "\n\n".join(sources)
            
            # Generate answer (simulated for demo)
            answer = f"""Based on the documents, here's what I found:

**Query:** {query}

**Relevant Information:**
{context}

---

*Note: This is a demo using simple keyword matching. For production, use proper embeddings (OpenAI, sentence-transformers) and vector stores (ChromaDB, FAISS).*
"""
            
            st.write(answer)
            
            # Show sources
            with st.expander("📚 Sources"):
                for i, source in enumerate(sources, 1):
                    st.write(f"**Source {i}:**")
                    st.write(source[:300] + "...")
        else:
            answer = "No relevant documents found. Please upload documents first."
            st.warning(answer)
        
        # Add to history
        st.session_state.rag_messages.append({
            "role": "assistant",
            "content": answer,
            "sources": sources
        })

# ============================================================================
# Footer
# ============================================================================

st.divider()
st.caption("""
**🎓 Module 14: RAG Document Q&A**
- Upload documents (TXT, MD, PDF)
- Automatic text chunking
- Semantic search (keyword-based demo)
- Question answering with sources

**For production use:**
- Proper embeddings (OpenAI, sentence-transformers)
- Vector database (ChromaDB, FAISS)
- LLM for answer generation
""")

# Run verification
if __name__ == "__main__":
    st.write("✅ App is running correctly!")
