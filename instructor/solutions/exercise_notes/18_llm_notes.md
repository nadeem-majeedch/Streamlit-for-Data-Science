# Exercise 18 — LLM Workshop: Solution Notes

> **👩‍🏫 Instructor Reference**
> *Expected approach, key code, and grading guidance.*

---

## Challenge 1: Provider Abstraction

### Expected Approach
Abstract base class `LLMProvider` with `chat()` and `stream_chat()` methods. Demo provider for testing without API keys.

### Key Code
```python
from abc import ABC, abstractmethod

class LLMProvider(ABC):
    @abstractmethod
    def chat(self, messages: list, **kwargs) -> str:
        pass

    @abstractmethod
    def stream_chat(self, messages: list, **kwargs):
        pass

class DemoProvider(LLMProvider):
    def chat(self, messages: list, **kwargs) -> str:
        user_msg = messages[-1]["content"]
        return f"Demo response to: '{user_msg[:50]}...' This is a simulated response."

    def stream_chat(self, messages: list, **kwargs):
        response = self.chat(messages)
        for word in response.split():
            yield word + " "

def get_provider(name: str) -> LLMProvider:
    if name == "demo":
        return DemoProvider()
    elif name == "openai":
        try:
            api_key = st.secrets.get("openai", {}).get("api_key", "")
            if not api_key:
                st.warning("OpenAI API key not configured")
                return DemoProvider()
            # Would create OpenAIProvider here
            return DemoProvider()
        except Exception:
            return DemoProvider()
    return DemoProvider()
```

### Common Mistakes
- Not using abstract base class
- Hardcoding API keys
- Not providing a fallback/demo provider

### Grading Notes (25 marks)
- Full marks: ABC defined, demo provider works, factory function handles missing keys
- 18 marks: Provider works but missing ABC or factory
- 10 marks: Basic response without abstraction

---

## Challenge 2: Conversation State

### Key Code
```python
def init_conversation():
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "system_prompt" not in st.session_state:
        st.session_state.system_prompt = "You are a helpful Data Science assistant."

def add_message(role: str, content: str):
    st.session_state.messages.append({"role": role, "content": content})

def get_context_messages(max_history: int = 10):
    messages = [{"role": "system", "content": st.session_state.system_prompt}]
    messages.extend(st.session_state.messages[-max_history:])
    return messages

def clear_conversation():
    st.session_state.messages = []
```

### Common Mistakes
- Not including system prompt in context
- Not limiting history (token limits)
- Storing messages in wrong format

---

## Challenge 3: Chat Interface

### Key Code
```python
def chat_interface(provider):
    init_conversation()

    # Display history
    for message in get_context_messages():
        if message["role"] != "system":
            with st.chat_message(message["role"]):
                st.write(message["content"])

    # User input
    if prompt := st.chat_input("Type your message..."):
        # Sanitize input
        if len(prompt) > 5000:
            st.error("Message too long (max 5000 characters)")
            return
        if not prompt.strip():
            return

        add_message("user", prompt)
        with st.chat_message("user"):
            st.write(prompt)

        # Get response
        with st.chat_message("assistant"):
            response = provider.chat(get_context_messages())
            st.write(response)
            add_message("assistant", response)
```

### Common Mistakes
- Not checking for empty input
- Not limiting input length (security)
- Not including system prompt in context

---

## Challenge 4: RAG Pipeline

### Expected Approach
Document upload → text extraction → chunking → simple keyword matching (or vector search) → context retrieval → grounded answer.

### Key Code (simplified RAG)
```python
def chunk_text(text, chunk_size=500, overlap=50):
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start = end - overlap
    return chunks

def retrieve_context(query, chunks, top_k=3):
    """Simple keyword-based retrieval."""
    query_words = set(query.lower().split())
    scored = []
    for chunk in chunks:
        chunk_words = set(chunk.lower().split())
        overlap = len(query_words & chunk_words)
        scored.append((overlap, chunk))
    scored.sort(reverse=True)
    return [chunk for _, chunk in scored[:top_k]]

# Usage
if st.button("Upload & Index"):
    if uploaded_doc:
        text = uploaded_doc.read().decode("utf-8")
        chunks = chunk_text(text)
        st.session_state.chunks = chunks
        st.success(f"Indexed {len(chunks)} chunks")

if st.session_state.get("chunks"):
    query = st.text_input("Ask a question about the document")
    if query:
        context = retrieve_context(query, st.session_state.chunks)
        prompt = f"Context: {' '.join(context)}\n\nQuestion: {query}\n\nAnswer based on context:"
        # Send to LLM provider...
```

### Grading Notes (25 marks)
- Full marks: Upload, chunking, retrieval, and answer generation work
- 18 marks: Upload and chunking work, retrieval basic
- 10 marks: Basic document handling

---

## Security Checklist
1. ✅ No hardcoded API keys (use `st.secrets`)
2. ✅ Input length validation (prevent token exhaustion)
3. ✅ Input sanitization (strip whitespace, check for injection patterns)
4. ✅ Provider abstraction (easy to swap/mock)
5. ✅ Error handling for API failures
6. ✅ Conversation history limited (prevent context overflow)
