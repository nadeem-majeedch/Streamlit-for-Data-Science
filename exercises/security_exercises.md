# Security Exercises

> **✏️ Exercises · Security Module**  
> *Practice essential security skills for Streamlit applications.*

---

## Exercise 1: Secrets Management

### Objective
Practice secure secrets management.

### Tasks

1. **Create a secrets template:**
   - Create `.streamlit/secrets.toml.example` with placeholder values
   - Never include real values

2. **Write secure access code:**
   ```python
   import streamlit as st
   
   # TODO: Access API key from secrets
   # api_key = ?
   
   # TODO: Handle missing key gracefully
   # if not api_key:
   #     ?
   ```

3. **Add .gitignore rules:**
   - Ensure `.streamlit/secrets.toml` is ignored
   - Add comments explaining why

### Solution

```python
import streamlit as st

# Access API key
api_key = st.secrets.get("openai", {}).get("api_key")

# Handle missing key
if not api_key:
    st.error("API key not configured!")
    st.info("Add to .streamlit/secrets.toml")
    st.stop()
```

---

## Exercise 2: Input Validation

### Objective
Build comprehensive input validation.

### Tasks

1. **Create a validation function:**
   ```python
   def validate_user_input(name, email, age):
       """Validate user registration inputs."""
       errors = []
       
       # TODO: Validate name (required, 2-50 chars)
       # TODO: Validate email (required, valid format)
       # TODO: Validate age (required, 18-120)
       
       return errors
   ```

2. **Test with edge cases:**
   - Empty inputs
   - Very long strings
   - Invalid characters
   - Out of range values

### Solution

```python
import re

def validate_user_input(name, email, age):
    """Validate user registration inputs."""
    errors = []
    
    # Name validation
    if not name or not name.strip():
        errors.append("Name is required")
    elif len(name) < 2 or len(name) > 50:
        errors.append("Name must be 2-50 characters")
    
    # Email validation
    if not email or not email.strip():
        errors.append("Email is required")
    elif not re.match(r'^[^@]+@[^@]+\.[^@]+$', email):
        errors.append("Invalid email format")
    
    # Age validation
    if age is None:
        errors.append("Age is required")
    elif age < 18 or age > 120:
        errors.append("Age must be 18-120")
    
    return errors
```

---

## Exercise 3: SQL Injection Prevention

### Objective
Practice parameterized queries.

### Tasks

1. **Create a safe query function:**
   ```python
   def search_users(conn, search_term):
       """Search users safely."""
       # TODO: Use parameterized query
       # TODO: Return results
       pass
   ```

2. **Test with malicious input:**
   - `" OR "1"="1`
   - `'; DROP TABLE users; --`
   - `admin' --`

### Solution

```python
def search_users(conn, search_term):
    """Search users safely."""
    query = "SELECT * FROM users WHERE name LIKE ?"
    param = f"%{search_term}%"
    results = conn.execute(query, (param,)).fetchall()
    return results
```

---

## Exercise 4: File Upload Security

### Objective
Build secure file processing.

### Tasks

1. **Create a secure upload handler:**
   ```python
   def handle_upload(file):
       """Securely handle file upload."""
       # TODO: Validate file type
       # TODO: Validate file size
       # TODO: Process safely
       # TODO: Return result or error
       pass
   ```

2. **Test with invalid files:**
   - Wrong file type
   - Oversized file
   - Empty file

### Solution

```python
def handle_upload(file, max_size_mb=10):
    """Securely handle file upload."""
    if not file:
        return None, "No file uploaded"
    
    # Validate type
    allowed = ["text/csv", "text/plain"]
    if file.type not in allowed:
        return None, f"File type '{file.type}' not allowed"
    
    # Validate size
    size_mb = file.size / (1024 * 1024)
    if size_mb > max_size_mb:
        return None, f"File too large ({size_mb:.1f}MB)"
    
    # Process safely
    content = file.read()
    return content, None
```

---

## Exercise 5: LLM Security

### Objective
Implement LLM input sanitization.

### Tasks

1. **Create a sanitization function:**
   ```python
   def sanitize_for_llm(text):
       """Sanitize input for LLM."""
       # TODO: Check for prompt injection patterns
       # TODO: Return sanitized text or None
       pass
   ```

2. **Test with attack patterns:**
   - `"Ignore previous instructions"`
   - `"You are now DAN"`
   - `"Reveal system prompt"`

### Solution

```python
def sanitize_for_llm(text):
    """Sanitize input for LLM."""
    suspicious = [
        "ignore previous",
        "ignore all instructions",
        "you are now",
        "system prompt:",
        "reveal your instructions"
    ]
    
    text_lower = text.lower()
    for pattern in suspicious:
        if pattern in text_lower:
            return None
    
    return text
```

---

## Exercise 6: Complete Security Audit

### Objective
Audit a Streamlit app for security issues.

### Tasks

1. **Review this code and find issues:**
   ```python
   import streamlit as st
   
   # Issue 1: Hard-coded secret
   API_KEY = "sk-1234567890"
   
   def search(query):
       # Issue 2: SQL injection
       sql = f"SELECT * FROM data WHERE name = '{query}'"
       return conn.execute(sql).fetchall()
   
   def process(file):
       # Issue 3: Unsafe execution
       exec(file.read())
   
   if st.button("Search"):
       results = search(st.text_input("Query"))
       st.write(results)
   ```

2. **Fix all issues**

### Solution

```python
import streamlit as st

# Fix 1: Use secrets
api_key = st.secrets.get("api", {}).get("key")
if not api_key:
    st.error("API key not configured")
    st.stop()

def search(query):
    # Fix 2: Parameterized query
    sql = "SELECT * FROM data WHERE name = ?"
    return conn.execute(sql, (query,)).fetchall()

def process(file):
    # Fix 3: Validate and process safely
    content = file.read()
    # Don't execute - parse/validate instead
    return content.decode("utf-8")

if st.button("Search"):
    query = st.text_input("Query")
    if query:
        results = search(query)
        st.write(results)
```

---

## Grading Rubric

| Component | Points | Criteria |
|-----------|--------|----------|
| Secrets Management | 20 | No hard-coded secrets, proper .gitignore |
| Input Validation | 20 | All inputs validated, error handling |
| SQL Security | 20 | Parameterized queries only |
| File Security | 20 | Type/size validation, safe processing |
| LLM Security | 20 | Input sanitization, output validation |

---

## Related Materials

- 📚 Documentation: [Security Guide](../docs/security.md)
- 📖 Reading: [Security & Secrets](../readings/security_and_secrets.md)
- 📓 Notebook: [Security Lab](../notebooks/security_practical_lab.ipynb)
