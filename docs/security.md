# Streamlit Security Guide

> **📚 Documentation**  
> *Comprehensive security practices for Streamlit applications.*

---

## Overview

Security is critical for production Streamlit applications. This guide covers essential security practices for the entire course.

---

## 1. Secrets Management

### Never Hard-Code Credentials

```python
# ❌ WRONG: Hard-coded secrets
API_KEY = "sk-your-real-key-here"
DB_PASSWORD = "mypassword123"

# ✅ CORRECT: Use Streamlit secrets
import streamlit as st
api_key = st.secrets.openai.api_key
```

### Streamlit Secrets (.streamlit/secrets.toml)

```toml
# .streamlit/secrets.toml — NEVER commit this file!

[openai]
api_key = "sk-your-key-here"

[database]
host = "localhost"
port = 5432
name = "myapp_db"
username = "admin"
password = "secure_password"
```

### Environment Variables (Alternative)

```python
import os

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    st.error("Set OPENAI_API_KEY environment variable")
    st.stop()
```

### .gitignore Configuration

```gitignore
# Streamlit secrets
.streamlit/secrets.toml

# Environment files
.env
.env.local
.env.production

# Uploaded files
uploads/

# Database files
*.db
*.sqlite
```

---

## 2. Input Validation

### Text Input Validation

```python
def validate_text_input(text, max_length=5000):
    """Validate text input."""
    errors = []
    
    if not text or not text.strip():
        errors.append("Text cannot be empty")
    
    if len(text) > max_length:
        errors.append(f"Text too long (max {max_length} characters)")
    
    # Check for suspicious patterns
    suspicious = ['<script>', 'javascript:', 'onerror=']
    for pattern in suspicious:
        if pattern.lower() in text.lower():
            errors.append("Text contains suspicious content")
    
    return errors
```

### File Upload Validation

```python
def validate_upload(file, allowed_types, max_size_mb=10):
    """Validate uploaded file."""
    errors = []
    
    # Check file type
    if file.type not in allowed_types:
        errors.append(f"File type {file.type} not allowed")
    
    # Check file size
    size_mb = file.size / (1024 * 1024)
    if size_mb > max_size_mb:
        errors.append(f"File too large (max {max_size_mb}MB)")
    
    return errors
```

### Numeric Input Validation

```python
def validate_numeric(value, min_val=None, max_val=None, name="value"):
    """Validate numeric input."""
    if min_val is not None and value < min_val:
        return f"{name} must be at least {min_val}"
    if max_val is not None and value > max_val:
        return f"{name} must be at most {max_val}"
    return None
```

---

## 3. SQL Injection Prevention

### Parameterized Queries (Always Use)

```python
import sqlite3

# ✅ SAFE: Parameterized query
def get_user(username):
    conn = sqlite3.connect("users.db")
    query = "SELECT * FROM users WHERE username = ?"
    cursor = conn.execute(query, (username,))
    return cursor.fetchone()

# ❌ DANGEROUS: String concatenation
def get_user_unsafe(username):
    conn = sqlite3.connect("users.db")
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor = conn.execute(query)
    return cursor.fetchone()
```

### SQLAlchemy with Parameters

```python
from sqlalchemy import text

# ✅ SAFE
def get_users(session, min_age):
    query = text("SELECT * FROM users WHERE age > :age")
    result = session.execute(query, {"age": min_age})
    return result.fetchall()
```

---

## 4. File Upload Security

### Safe File Handling

```python
import streamlit as st
from pathlib import Path
import tempfile

def safe_file_processing(uploaded_file):
    """Safely process uploaded file."""
    # Validate file type
    allowed_types = ["text/csv", "application/pdf"]
    if uploaded_file.type not in allowed_types:
        st.error("File type not allowed")
        return None
    
    # Validate file size
    if uploaded_file.size > 10 * 1024 * 1024:  # 10MB
        st.error("File too large")
        return None
    
    # Read content (don't execute!)
    content = uploaded_file.read()
    
    # For CSV, use pandas (safe)
    if uploaded_file.type == "text/csv":
        import pandas as pd
        import io
        df = pd.read_csv(io.BytesIO(content))
        return df
    
    return content
```

### What NOT to Do

```python
# ❌ NEVER: Execute uploaded Python files
exec(uploaded_file.read())

# ❌ NEVER: Use eval on user content
eval(user_input)

# ❌ NEVER: Run shell commands from user input
import os
os.system(f"process {user_filename}")
```

---

## 5. Authentication Concepts

### Basic Authentication Pattern

```python
import streamlit as st
import hashlib

def hash_password(password):
    """Hash password (for demo only - use proper auth in production)."""
    return hashlib.sha256(password.encode()).hexdigest()

def check_password():
    """Simple password authentication."""
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False
    
    if not st.session_state.authenticated:
        st.text_input("Username", key="username")
        st.text_input("Password", type="password", key="password")
        
        if st.button("Login"):
            # In production, check against database
            if (st.session_state.username == "admin" and 
                hash_password(st.session_state.password) == hash_password("admin")):
                st.session_state.authenticated = True
                st.rerun()
            else:
                st.error("Invalid credentials")
        
        st.stop()
```

### Production Authentication

For production apps, use:
- **OAuth** (Google, GitHub, Microsoft)
- **SSO** (Single Sign-On)
- **Streamlit Authenticator** library
- **Custom JWT-based auth**

---

## 6. LLM Security

### Prompt Injection Prevention

```python
def sanitize_llm_input(text):
    """Sanitize input for LLM."""
    suspicious = [
        "ignore previous instructions",
        "ignore all instructions",
        "you are now",
        "system prompt:",
        "reveal your instructions"
    ]
    
    text_lower = text.lower()
    for pattern in suspicious:
        if pattern in text_lower:
            return None  # Block or warn
    
    return text
```

### Output Validation

```python
def validate_llm_output(response):
    """Validate LLM response before displaying."""
    # Don't execute code from LLM
    if "```python" in response:
        st.warning("⚠️ Response contains code - review before using")
    
    # Check for sensitive data leaks
    sensitive_patterns = ["api_key", "password", "secret"]
    for pattern in sensitive_patterns:
        if pattern in response.lower():
            st.warning("⚠️ Response may contain sensitive information")
    
    return response
```

---

## 7. Data Privacy

### Don't Log Sensitive Data

```python
import logging

# ❌ WRONG: Logging secrets
logging.info(f"API Key: {api_key}")

# ✅ CORRECT: Log without sensitive data
logging.info("API request successful")
```

### Don't Display Sensitive Data

```python
# ❌ WRONG: Showing full API key
st.write(f"API Key: {api_key}")

# ✅ CORRECT: Mask sensitive data
st.write(f"API Key: {api_key[:8]}...")
```

### Data Minimization

- Only collect data you need
- Don't store what you don't need
- Provide data deletion options
- Document data retention policies

---

## 8. Dependency Security

### Check for Vulnerabilities

```bash
# Check installed packages
pip-audit

# Check specific package
pip-audit package-name
```

### Pin Dependencies

```txt
# requirements.txt — Pin versions
streamlit==1.44.0
pandas==2.2.0
numpy==1.26.0
```

### Regular Updates

```bash
# Check for outdated packages
pip list --outdated

# Update specific package
pip install --upgrade streamlit
```

---

## 9. Deployment Security

### Streamlit Cloud

- Never expose secrets in code
- Use the Secrets dashboard
- Enable HTTPS
- Review connected repositories

### Self-Hosted

```toml
# .streamlit/config.toml
[server]
headless = true
enableCORS = false
enableXsrfProtection = true
# Don't disable these in production!
```

---

## Security Checklist

- [ ] No hard-coded secrets in source code
- [ ] `.streamlit/secrets.toml` is in `.gitignore`
- [ ] All user inputs are validated
- [ ] SQL queries use parameterized statements
- [ ] File uploads are validated and sandboxed
- [ ] `eval()` and `exec()` are never used on user input
- [ ] Sensitive data is not logged or displayed
- [ ] Dependencies are pinned and audited
- [ ] CORS and XSRF protection are enabled
- [ ] HTTPS is used in production

---

## Course Security Progression

| Module | Security Topic |
|--------|---------------|
| M01 | `.gitignore` basics, never hard-code keys |
| M02 | Input validation for widgets |
| M06 | File upload validation |
| M10 | SQL injection prevention, parameterized queries |
| M13 | Prompt injection, LLM output validation |
| M14 | Secrets management, provider abstraction |
| M15 | Deployment security, Cloud secrets |
| M16 | Production security checklist |

---

## Further Reading

- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [Streamlit Security](https://docs.streamlit.io/develop/concepts/architecture/security)
- [Python Security](https://pythonsecurity.readthedocs.io/)
