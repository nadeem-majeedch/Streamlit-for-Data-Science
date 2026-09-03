"""
Streamlit LLM Chat App
=======================

Module 14 · AI/LLM

A complete LLM chat application demonstrating:
- Provider abstraction (OpenAI, Local)
- Secrets management
- Conversation state
- Chat interface with streaming
- Security considerations

Run: streamlit run apps/18_llm_chat.py
"""

import streamlit as st
from abc import ABC, abstractmethod
from typing import List, Dict, Generator
import json

st.set_page_config(
    page_title="LLM Chat",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 LLM Chat App")
st.caption("Module 14 · Advanced LLM Applications")

# ============================================================================
# Provider Abstraction
# ============================================================================

class LLMProvider(ABC):
    """Base class for LLM providers."""
    
    @abstractmethod
    def chat(self, messages: list, **kwargs) -> str:
        """Send chat completion request."""
        pass
    
    @abstractmethod
    def stream_chat(self, messages: list, **kwargs) -> Generator:
        """Stream chat completion response."""
        pass

class OpenAIProvider(LLMProvider):
    """OpenAI API provider."""
    
    def __init__(self, api_key: str, model: str = "gpt-3.5-turbo"):
        try:
            import openai
            self.client = openai.OpenAI(api_key=api_key)
            self.model = model
        except ImportError:
            raise ImportError("Install openai: pip install openai")
    
    def chat(self, messages: list, **kwargs) -> str:
        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            **kwargs
        )
        return response.choices[0].message.content
    
    def stream_chat(self, messages: list, **kwargs) -> Generator:
        stream = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            stream=True,
            **kwargs
        )
        for chunk in stream:
            if chunk.choices[0].delta.content:
                yield chunk.choices[0].delta.content

class LocalProvider(LLMProvider):
    """Local model provider (Ollama)."""
    
    def __init__(self, base_url: str = "http://localhost:11434"):
        self.base_url = base_url
    
    def chat(self, messages: list, model: str = "llama2", **kwargs) -> str:
        import requests
        response = requests.post(
            f"{self.base_url}/api/chat",
            json={"model": model, "messages": messages}
        )
        return response.json()["message"]["content"]
    
    def stream_chat(self, messages: list, model: str = "llama2", **kwargs) -> Generator:
        import requests
        response = requests.post(
            f"{self.base_url}/api/chat",
            json={"model": model, "messages": messages},
            stream=True
        )
        for line in response.iter_lines():
            if line:
                data = json.loads(line)
                if "message" in data:
                    yield data["message"]["content"]

class DemoProvider(LLMProvider):
    """Demo provider (no API required)."""
    
    def chat(self, messages: list, **kwargs) -> str:
        last_msg = messages[-1]["content"] if messages else ""
        return f"Echo: {last_msg}\n\n[This is a demo response. Configure an API key for real responses.]"
    
    def stream_chat(self, messages: list, **kwargs) -> Generator:
        response = self.chat(messages, **kwargs)
        for word in response.split():
            yield word + " "

def get_provider(provider_name: str = "demo") -> LLMProvider:
    """Get LLM provider by name."""
    
    if provider_name == "openai":
        api_key = st.secrets.get("openai", {}).get("api_key")
        if not api_key:
            st.error("⚠️ OpenAI API key not configured!")
            st.info("Add to `.streamlit/secrets.toml`:\n```toml\n[openai]\napi_key = \"sk-...\"\n```")
            st.stop()
        return OpenAIProvider(api_key=api_key)
    
    elif provider_name == "local":
        return LocalProvider()
    
    else:
        return DemoProvider()

# ============================================================================
# Conversation State
# ============================================================================

def init_conversation():
    """Initialize conversation state."""
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "system_prompt" not in st.session_state:
        st.session_state.system_prompt = "You are a helpful assistant."

def add_message(role: str, content: str):
    """Add message to history."""
    st.session_state.messages.append({"role": role, "content": content})

def get_messages() -> List[Dict]:
    """Get conversation messages."""
    return st.session_state.messages

def clear_conversation():
    """Clear chat history."""
    st.session_state.messages = []

def get_context_messages(max_history: int = 20) -> List[Dict]:
    """Get messages for API (with system prompt)."""
    messages = [{"role": "system", "content": st.session_state.system_prompt}]
    messages.extend(st.session_state.messages[-max_history:])
    return messages

# ============================================================================
# Security
# ============================================================================

def sanitize_input(text: str) -> str:
    """Basic input sanitization."""
    suspicious = [
        "ignore previous", "ignore all instructions",
        "you are now", "system prompt:",
        "reveal your instructions", "what are your instructions"
    ]
    
    text_lower = text.lower()
    for pattern in suspicious:
        if pattern in text_lower:
            st.warning("⚠️ Input contains potentially suspicious content")
            return text  # Allow but warn
    
    return text

def validate_prompt(prompt: str, max_length: int = 4000) -> bool:
    """Validate prompt before sending."""
    if len(prompt) > max_length:
        st.error(f"Prompt too long (max {max_length} characters)")
        return False
    
    if not prompt.strip():
        st.error("Prompt cannot be empty")
        return False
    
    return True

# ============================================================================
# Sidebar
# ============================================================================

st.sidebar.title("📚 Module 14 Demo")
st.sidebar.markdown("---")

# Provider selection
provider_name = st.sidebar.selectbox(
    "LLM Provider",
    ["demo", "openai", "local"],
    help="Demo: no API needed. OpenAI: requires API key. Local: requires Ollama."
)

# Model selection (for OpenAI)
model = "gpt-3.5-turbo"
if provider_name == "openai":
    model = st.sidebar.selectbox(
        "Model",
        ["gpt-3.5-turbo", "gpt-4", "gpt-4-turbo"]
    )

# Settings
temperature = st.sidebar.slider(
    "Temperature",
    min_value=0.0,
    max_value=2.0,
    value=0.7,
    help="Higher = more creative, lower = more focused"
)

max_tokens = st.sidebar.slider(
    "Max Tokens",
    min_value=100,
    max_value=4000,
    value=1000
)

# System prompt
system_prompt = st.sidebar.text_area(
    "System Prompt",
    value="You are a helpful Data Science assistant.",
    height=100
)
st.session_state.system_prompt = system_prompt

st.sidebar.markdown("---")

# Clear button
if st.sidebar.button("🗑️ Clear Chat", use_container_width=True):
    clear_conversation()
    st.rerun()

# Provider info
st.sidebar.markdown("---")
st.sidebar.subheader("ℹ️ Provider Info")

if provider_name == "demo":
    st.sidebar.info("Demo mode - no API required. Responses are simulated.")
elif provider_name == "openai":
    api_key = st.secrets.get("openai", {}).get("api_key")
    if api_key:
        st.sidebar.success("✅ OpenAI API key configured")
    else:
        st.sidebar.error("❌ OpenAI API key not found")
elif provider_name == "local":
    st.sidebar.info("Local mode - requires Ollama running on localhost:11434")

# ============================================================================
# Main Chat Interface
# ============================================================================

# Initialize
init_conversation()

# Get provider
provider = get_provider(provider_name)

# Display chat history
for message in get_messages():
    with st.chat_message(message["role"]):
        st.write(message["content"])

# User input
if prompt := st.chat_input("Type your message..."):
    # Sanitize
    prompt = sanitize_input(prompt)
    
    # Validate
    if not validate_prompt(prompt):
        st.stop()
    
    # Add user message
    add_message("user", prompt)
    with st.chat_message("user"):
        st.write(prompt)
    
    # Get response
    with st.chat_message("assistant"):
        messages = get_context_messages()
        
        try:
            if provider_name == "demo":
                # Demo mode - no streaming
                response = provider.chat(messages)
                st.write(response)
            else:
                # Real provider - streaming
                response = st.write_stream(
                    provider.stream_chat(messages, temperature=temperature, max_tokens=max_tokens)
                )
        except Exception as e:
            response = f"Error: {str(e)}"
            st.error(response)
    
    # Add response
    add_message("assistant", response)

# ============================================================================
# Footer
# ============================================================================

st.divider()
st.caption("""
**🎓 Module 14: Advanced LLM/RAG Applications**
- Provider abstraction for swappable backends
- Secrets management with `st.secrets`
- Conversation state with session state
- Streaming responses for better UX
- Input validation and security
""")

# Run verification
if __name__ == "__main__":
    st.write("✅ App is running correctly!")
