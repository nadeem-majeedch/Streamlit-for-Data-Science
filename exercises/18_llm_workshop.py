"""
Exercise 18: LLM Workshop
==========================

Module 14 · AI/LLM

Master LLM and RAG applications with Streamlit.

Learning Objectives:
- Implement provider abstraction
- Manage secrets securely
- Build conversation state
- Create chat interfaces
- Implement RAG pipelines

Instructions:
Complete each section by filling in the TODOs.
Run with: streamlit run exercises/18_llm_workshop.py
"""

import streamlit as st
from abc import ABC, abstractmethod
from typing import List, Dict, Generator

st.set_page_config(page_title="LLM Workshop", page_icon="🤖", layout="wide")
st.title("🤖 Exercise 18: LLM Workshop")
st.markdown("*Module 14 · AI/LLM — Build LLM applications with Streamlit*")

st.divider()

# ============================================================================
# CHALLENGE 1: Provider Abstraction
# ============================================================================
st.header("🎯 Challenge 1: Provider Abstraction")
st.write("Build a modular provider system.")

# TODO: Create base provider class
# class LLMProvider(ABC):
#     @abstractmethod
#     def chat(self, messages: list, **kwargs) -> str:
#         pass
#     
#     @abstractmethod
#     def stream_chat(self, messages: list, **kwargs) -> Generator:
#         pass

# TODO: Create demo provider
# class DemoProvider(LLMProvider):
#     def chat(self, messages: list, **kwargs) -> str:
#         return f"Demo response to: {messages[-1]['content']}"
#     
#     def stream_chat(self, messages: list, **kwargs) -> Generator:
#         response = self.chat(messages)
#         for word in response.split():
#             yield word + " "

# TODO: Create provider factory
# def get_provider(name: str) -> LLMProvider:
#     if name == "demo":
#         return DemoProvider()
#     elif name == "openai":
#         # Check for API key
#         pass

st.divider()

# ============================================================================
# CHALLENGE 2: Conversation State
# ============================================================================
st.header("🎯 Challenge 2: Conversation State")
st.write("Implement chat history management.")

# TODO: Initialize conversation
# def init_conversation():
#     if "messages" not in st.session_state:
#         st.session_state.messages = []
#     if "system_prompt" not in st.session_state:
#         st.session_state.system_prompt = "You are a helpful assistant."

# TODO: Add message function
# def add_message(role: str, content: str):
#     st.session_state.messages.append({"role": role, "content": content})

# TODO: Get context messages
# def get_context_messages(max_history: int = 10) -> List[Dict]:
#     messages = [{"role": "system", "content": st.session_state.system_prompt}]
#     messages.extend(st.session_state.messages[-max_history:])
#     return messages

# TODO: Clear conversation
# def clear_conversation():
#     st.session_state.messages = []

st.divider()

# ============================================================================
# CHALLENGE 3: Chat Interface
# ============================================================================
st.header("🎯 Challenge 3: Chat Interface")
st.write("Build a complete chat UI.")

# TODO: Implement chat interface
# def chat_interface(provider):
#     init_conversation()
#     
#     # Display history
#     for message in get_context_messages():
#         if message["role"] != "system":
#             with st.chat_message(message["role"]):
#                 st.write(message["content"])
#     
#     # User input
#     if prompt := st.chat_input("Type your message..."):
#         # Add user message
#         add_message("user", prompt)
#         with st.chat_message("user"):
#             st.write(prompt)
#         
#         # Get response
#         with st.chat_message("assistant"):
#             messages = get_context_messages()
#             response = provider.chat(messages)
#             st.write(response)
#         
#         # Add response
#         add_message("assistant", response)

st.divider()

# ============================================================================
# CHALLENGE 4: Input Validation
# ============================================================================
st.header("🎯 Challenge 4: Input Validation")
st.write("Implement security measures.")

# TODO: Sanitize input
# def sanitize_input(text: str) -> str:
#     suspicious = ["ignore previous", "ignore all instructions", "system prompt:"]
#     
#     text_lower = text.lower()
#     for pattern in suspicious:
#         if pattern in text_lower:
#             st.warning("⚠️ Suspicious content detected")
#             return text  # Allow but warn
#     
#     return text

# TODO: Validate prompt
# def validate_prompt(prompt: str, max_length: int = 4000) -> bool:
#     if len(prompt) > max_length:
#         st.error(f"Too long (max {max_length} chars)")
#         return False
#     
#     if not prompt.strip():
#         st.error("Cannot be empty")
#         return False
#     
#     return True

# TODO: Rate limiting
# def check_rate_limit(max_requests: int = 10) -> bool:
#     if "request_log" not in st.session_state:
#         st.session_state.request_log = []
#     
#     from datetime import datetime, timedelta
#     cutoff = datetime.now() - timedelta(minutes=60)
#     st.session_state.request_log = [
#         t for t in st.session_state.request_log if t > cutoff
#     ]
#     
#     if len(st.session_state.request_log) >= max_requests:
#         st.error("Rate limit exceeded")
#         return False
#     
#     st.session_state.request_log.append(datetime.now())
#     return True

st.divider()

# ============================================================================
# CHALLENGE 5: RAG Pipeline
# ============================================================================
st.header("🎯 Challenge 5: RAG Pipeline")
st.write("Implement Retrieval-Augmented Generation.")

# TODO: Simple vector store
# class SimpleVectorStore:
#     def __init__(self):
#         self.chunks = []
#     
#     def add_documents(self, chunks: List[str]):
#         self.chunks.extend(chunks)
#     
#     def search(self, query: str, n_results: int = 3) -> List[str]:
#         # Simple keyword matching
#         query_words = set(query.lower().split())
#         scores = []
#         
#         for chunk in self.chunks:
#             chunk_words = set(chunk.lower().split())
#             overlap = len(query_words.intersection(chunk_words))
#             scores.append((overlap, chunk))
#         
#         scores.sort(key=lambda x: x[0], reverse=True)
#         return [chunk for _, chunk in scores[:n_results]]

# TODO: RAG class
# class RAGPipeline:
#     def __init__(self, provider, vector_store):
#         self.provider = provider
#         self.vector_store = vector_store
#     
#     def query(self, question: str) -> str:
#         context = self.vector_store.search(question)
#         if not context:
#             return "No relevant documents found."
#         
#         context_text = "\n\n".join(context)
#         messages = [
#             {"role": "system", "content": f"Answer based on context:\n\n{context_text}"},
#             {"role": "user", "content": question}
#         ]
#         
#         return self.provider.chat(messages)

# TODO: Document processing
# def process_document(file) -> str:
#     suffix = Path(file.name).suffix.lower()
#     if suffix in [".txt", ".md"]:
#         return file.read().decode("utf-8")
#     return ""

# def chunk_text(text: str, chunk_size: int = 500) -> List[str]:
#     chunks = []
#     start = 0
#     while start < len(text):
#         chunks.append(text[start:start + chunk_size])
#         start += chunk_size - 50  # overlap
#     return chunks

st.divider()

# ============================================================================
# BONUS: Streaming Response
# ============================================================================
st.header("🏆 Bonus: Streaming Response")
st.write("Implement streaming with placeholder.")

# TODO: Stream with placeholder
# def stream_with_placeholder(provider, messages):
#     placeholder = st.empty()
#     full_response = ""
#     
#     for chunk in provider.stream_chat(messages):
#         full_response += chunk
#         placeholder.markdown(full_response + "▌")
#     
#     placeholder.markdown(full_response)
#     return full_response

st.divider()

# ============================================================================
# COMPLETION
# ============================================================================
st.success("🎉 Workshop Complete!")
st.markdown("""
**What you practiced:**
- ✅ Provider abstraction pattern
- ✅ Conversation state management
- ✅ Chat interface building
- ✅ Input validation and security
- ✅ RAG pipeline implementation

**Key LLM deployment rules:**
- Never hard-code API keys
- Use provider abstraction for flexibility
- Validate all inputs
- Implement rate limiting
- Use RAG for grounded answers

**Next steps:**
- Read: [LLM/RAG Applications](../readings/18_llm_rag_applications.md)
- Notebook: [LLM Applications](../notebooks/18_llm_applications.ipynb)
- Demo Apps: [LLM Chat](../apps/18_llm_chat.py), [RAG Q&A](../apps/18_rag_app.py)
""")

# Run check
if __name__ == "__main__":
    st.write("✅ Exercise file is valid and ready to run!")
