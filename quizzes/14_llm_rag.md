# Quiz 14: LLM & RAG Applications

> **📝 Quiz · Module 14 · AI/LLM**  
> *Test your understanding of LLM and RAG applications with Streamlit.*

---

## Multiple Choice

### Q1. What is provider abstraction in LLM applications?

a) Using only one LLM provider  
b) Creating a common interface for multiple LLM backends  
c) Hiding the LLM from users  
d) Encrypting API calls

---

### Q2. Where should you store API keys in Streamlit?

a) Hard-coded in the script  
b) In `.streamlit/secrets.toml` or environment variables  
c) In a public GitHub repository  
d) In `st.session_state`

---

### Q3. What is the purpose of conversation state?

a) To store API keys  
b) To persist chat history across reruns  
c) To cache LLM responses  
d) To validate inputs

---

### Q4. How do you display streaming responses in Streamlit?

```python
# Option A
st.write(response)

# Option B
st.write_stream(provider.stream_chat(messages))
```

---

### Q5. What is RAG (Retrieval-Augmented Generation)?

a) A type of LLM  
b) Combining retrieval of relevant documents with LLM generation  
c) A database technology  
d) A caching strategy

---

### Q6. Why chunk documents in RAG?

a) To reduce storage costs  
b) To fit within LLM context limits and improve retrieval  
c) To encrypt the content  
d) To make documents shorter

---

### Q7. What is prompt injection?

a) Adding prompts to a database  
b) Manipulating LLM behavior through crafted inputs  
c) Injecting code into Streamlit  
d) A type of API authentication

---

### Q8. Why use a system prompt?

a) To hide the user's message  
b) To set the LLM's behavior and context  
c) To encrypt the conversation  
d) To limit token usage

---

### Q9. What is the advantage of local models (Ollama)?

a) They're always faster  
b) They work offline and don't require API keys  
c) They're more accurate  
d) They use less memory

---

### Q10. How do you implement rate limiting?

a) Limit the number of characters in a prompt  
b) Track requests per user and block excess  
c) Use a slower LLM  
d) Reduce the context window

---

### Q11. What is the purpose of text chunking overlap?

a) To make chunks longer  
b) To preserve context between chunks  
c) To reduce processing time  
d) To encrypt the text

---

### Q12. Why validate LLM outputs?

a) LLMs always produce correct answers  
b) To prevent executing potentially harmful generated code  
c) To improve response speed  
d) To reduce API costs

---

## Short Answer

### Q13. Explain the complete RAG pipeline. What are the key steps and why is each important?

---

### Q14. A developer hard-codes their OpenAI API key in the script and commits it to GitHub. What are the risks and how do you fix it?

---

### Q15. Describe three security best practices for LLM applications.

---

## Code Completion

### Q16. Complete the provider abstraction:

```python
from abc import ABC, abstractmethod

class LLMProvider(ABC):
    """Base class for LLM providers."""
    
    @abstractmethod
    def chat(self, messages: list, **kwargs) -> str:
        """Send chat completion request."""
        pass
    
    @abstractmethod
    def stream_chat(self, messages: list, **kwargs):
        """Stream chat completion response."""
        pass

# TODO: Implement demo provider
class DemoProvider(LLMProvider):
    def chat(self, messages: list, **kwargs) -> str:
        # TODO: Return demo response
        pass
    
    def stream_chat(self, messages: list, **kwargs):
        # TODO: Yield demo response words
        pass
```

---

### Q17. Complete the conversation state functions:

```python
import streamlit as st
from typing import List, Dict

def init_conversation():
    """Initialize conversation state."""
    # TODO: Initialize messages and system_prompt
    pass

def add_message(role: str, content: str):
    """Add message to history."""
    # TODO: Append to session state
    pass

def get_context_messages(max_history: int = 10) -> List[Dict]:
    """Get messages for API context."""
    # TODO: Build messages with system prompt
    pass
```

---

## Answer Key

### Multiple Choice

1. **B** — Provider abstraction creates a common interface for multiple backends
2. **B** — Use `.streamlit/secrets.toml` or environment variables
3. **B** — Conversation state persists chat history across reruns
4. **B** — Use `st.write_stream()` for streaming responses
5. **B** — RAG combines document retrieval with LLM generation
6. **B** — Chunking fits within context limits and improves retrieval
7. **B** — Prompt injection manipulates LLM through crafted inputs
8. **B** — System prompt sets the LLM's behavior and context
9. **B** — Local models work offline and don't require API keys
10. **B** — Track requests and block excess usage
11. **B** — Overlap preserves context between chunks
12. **B** — Validate outputs to prevent harmful code execution

### Short Answer

**Q13.** RAG Pipeline:
1. **Document Ingestion** — Upload and extract text from documents
2. **Chunking** — Split into smaller pieces for retrieval
3. **Embedding** — Convert chunks to vector representations
4. **Indexing** — Store vectors in a vector database
5. **Query Processing** — Convert user question to embedding
6. **Retrieval** — Find similar chunks using vector similarity
7. **Context Injection** — Add retrieved chunks to LLM prompt
8. **Generation** — LLM generates answer with context
9. **Source Attribution** — Link answer to source documents

**Q14.** Risks:
- API key exposed to anyone with repository access
- Attackers can use the key for unauthorized API calls
- Financial liability for usage charges
- Potential data breach if key has broad permissions

**Fix:**
1. Remove the key from the repository (git history too)
2. Rotate the compromised key immediately
3. Add `.streamlit/secrets.toml` to `.gitignore`
4. Use `st.secrets` or environment variables
5. Never commit secrets again

**Q15.** Security best practices:
1. **Secrets management** — Never hard-code API keys, use `st.secrets`
2. **Input validation** — Sanitize prompts, limit length, check for injection
3. **Rate limiting** — Limit requests per user to prevent abuse
4. **Output validation** — Don't execute LLM-generated code directly
5. **Data privacy** — Don't send sensitive data to external APIs

### Code Completion

**Q16.**
```python
class DemoProvider(LLMProvider):
    def chat(self, messages: list, **kwargs) -> str:
        last_msg = messages[-1]["content"] if messages else ""
        return f"Demo: {last_msg}"
    
    def stream_chat(self, messages: list, **kwargs):
        response = self.chat(messages)
        for word in response.split():
            yield word + " "
```

**Q17.**
```python
def init_conversation():
    """Initialize conversation state."""
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "system_prompt" not in st.session_state:
        st.session_state.system_prompt = "You are a helpful assistant."

def add_message(role: str, content: str):
    """Add message to history."""
    st.session_state.messages.append({"role": role, "content": content})

def get_context_messages(max_history: int = 10) -> List[Dict]:
    """Get messages for API context."""
    messages = [{"role": "system", "content": st.session_state.system_prompt}]
    messages.extend(st.session_state.messages[-max_history:])
    return messages
```

---

## Related Materials

- 📖 Reading: [18 — LLM/RAG Applications](../readings/18_llm_rag_applications.md)
- 📓 Notebook: [18 — LLM Applications](../notebooks/18_llm_applications.ipynb)
- ✏️ Exercise: [18 — LLM Workshop](../exercises/18_llm_workshop.py)
- 🖥️ Demo App: [18 — LLM Chat](../apps/18_llm_chat.py)
- 🖥️ Demo App: [18 — RAG Q&A](../apps/18_rag_app.py)
- 🚀 Project: [P07 — RAG Document Chat](../projects/P07_rag_document_chat.md)
