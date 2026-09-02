# 02 — Your First Streamlit App

> **📖 Reading · Module 01 · Beginner**  
> *Install Streamlit, build your first app, and understand how the execution model works.*

---

## Learning Objectives

After completing this reading you will be able to:

- Install Streamlit in a virtual environment.
- Create and run a minimal Streamlit app.
- Explain the top-to-bottom rerun execution model.
- Use text elements: `st.title`, `st.header`, `st.subheader`, `st.markdown`, `st.caption`, `st.code`, `st.divider`.
- Organize a Streamlit app with a clear structure.

---

## 1. Installation

### Prerequisites

- Python 3.10 or later.
- A terminal / command prompt.
- (Recommended) A virtual environment.

### Step-by-Step

```bash
# 1. Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate        # macOS / Linux
# .venv\Scripts\activate         # Windows

# 2. Install Streamlit and core data-science packages
pip install streamlit numpy pandas matplotlib plotly scikit-learn

# 3. Verify the installation
streamlit version
```

You should see output like:

```
Streamlit, version 1.44.x
```

### What Gets Installed?

Streamlit pulls in a number of dependencies. The key ones:

| Package | Role |
|---|---|
| `streamlit` | The framework itself |
| `tornado` | Async web server |
| `altair` | Declarative visualization (used internally) |
| `pandas` | Data handling (used by `st.dataframe`, etc.) |

> **Tip:** Always use a virtual environment. It prevents dependency conflicts between projects.

---

## 2. Creating Your First App

Create a file called `hello.py`:

```python
# hello.py
import streamlit as st

st.title("Hello, Streamlit!")
st.write("This is my very first Streamlit app.")
```

That's it. Two lines of Streamlit produce a fully styled web page.

### What Happened Behind the Scenes?

1. You called `st.title()` — Streamlit rendered an `<h1>` tag.
2. You called `st.write()` — Streamlit detected a string and rendered a `<p>` tag.
3. `st.write()` is polymorphic: it accepts strings, DataFrames, charts, images, and more. We'll explore this extensively in later modules.

---

## 3. Running a Streamlit App

```bash
streamlit run hello.py
```

This starts a local web server (default: `http://localhost:8501`) and opens your browser automatically.

### Useful Command-Line Options

| Flag | Purpose | Example |
|---|---|---|
| `--server.port` | Change the port | `--server.port 8502` |
| `--server.headless` | Don't open a browser | `--server.headless true` |
| `--theme.base` | Set theme (light/dark) | `--theme.base dark` |
| `--server.address` | Bind to a specific address | `--server.address 0.0.0.0` |

### Hot Reload

Streamlit watches your script for changes. Save the file, and the browser updates automatically — no manual refresh needed. This is one of Streamlit's biggest quality-of-life features.

---

## 4. The Execution Model: Top-to-Bottom Rerun

This is **the most important concept** in Streamlit.

### How It Works

Every time a user interacts with a widget (clicks a button, moves a slider, types in a text box), Streamlit **reruns the entire script from top to bottom**.

```python
import streamlit as st

st.title("Counter")
st.write("Click the button to increment the counter.")

# BUG: This counter resets on every rerun!
count = 0
if st.button("Increment"):
    count += 1
st.write(f"Count: {count}")
```

If you run this, the count will always show 0 or 1 — never 2, 3, 4. That's because:

1. Script runs → `count = 0`
2. Button clicked → script reruns → `count = 0` again → `count += 1` → displays 1
3. Button clicked again → script reruns → `count = 0` again → `count += 1` → displays 1

### The Fix: `st.session_state`

To persist values across reruns, use `st.session_state`:

```python
import streamlit as st

st.title("Counter")

if "count" not in st.session_state:
    st.session_state.count = 0

if st.button("Increment"):
    st.session_state.count += 1

st.write(f"Count: {st.session_state.count}")
```

Now the count persists across reruns because `st.session_state` is a dictionary-like object that survives between reruns.

### Visualizing the Rerun Cycle

```
User clicks button
        │
        ▼
┌───────────────────┐
│ Streamlit reruns  │
│ entire script     │
│ top to bottom     │
│                   │
│ 1. Import         │
│ 2. Page config    │
│ 3. Text / widgets │
│ 4. Logic          │
│ 5. Output         │
└───────────────────┘
        │
        ▼
  Browser updates
```

> **Key Insight:** Streamlit is *not* a traditional web framework where you define routes and handlers. It's a *script rerunner* that renders output to a browser. Think of it as a supercharged Jupyter cell that reruns automatically.

---

## 5. Text Elements: Markdown and Beyond

Streamlit supports several text-rendering functions. Here's your toolkit:

### Titles and Headers

```python
st.title("Main Title")          # Largest — rendered as <h1>
st.header("Section Header")     # Rendered as <h2>
st.subheader("Sub-Header")      # Rendered as <h3>
```

### Body Text

```python
st.write("Plain text output — works with almost any data type.")
st.markdown("**Bold**, *italic*, and `code`.")  # Full Markdown support
st.caption("Small, gray caption text.")          # Subtle annotation
```

### Code Blocks

```python
st.code("print('Hello, world!')", language="python")   # Syntax-highlighted
st.code("""
def add(a, b):
    return a + b
""", language="python")
```

### LaTeX

```python
st.latex(r"E = mc^2")   # Rendered LaTeX math
```

### Dividers and Empty Space

```python
st.divider()    # Horizontal rule
st.empty()      # Placeholder that can be replaced later
```

### Putting It All Together

```python
import streamlit as st

st.set_page_config(page_title="Text Demo", page_icon="📝")

st.title("📝 Text Elements Demo")
st.caption("A tour of Streamlit's text-rendering capabilities")

st.header("1. Headers")
st.write("Streamlit provides three levels of section headers:")
st.subheader("This is a subheader")
st.markdown("**Bold text** and *italic text* are supported via Markdown.")

st.divider()

st.header("2. Code Blocks")
st.code("import streamlit as st\nst.write('Hello!')", language="python")

st.divider()

st.header("3. Captions and Notes")
st.caption("This caption appears in small gray text below content.")
```

---

## 6. Basic Application Structure

As your apps grow beyond a single file, organization matters.

### Minimal Single-File App

```
my_app/
├── app.py
└── requirements.txt
```

### Multi-File App (Using Imports)

```
my_app/
├── app.py              # Main entry point
├── utils.py            # Helper functions
├── data_processing.py  # Data loading and cleaning
├── pages/              # For multipage apps (covered in Module 08)
│   ├── 1_Explore.py
│   └── 2_Model.py
├── data/               # Datasets
│   └── sales.csv
├── assets/             # Images, CSS, etc.
│   └── logo.png
├── .streamlit/
│   └── config.toml     # Theme and server config
└── requirements.txt
```

### The `st.set_page_config()` Rule

**`st.set_page_config()` must be the very first Streamlit command in your script.** If you place any other `st.` call before it, Streamlit throws an error.

```python
import streamlit as st

# ✅ Correct — page config is first
st.set_page_config(
    page_title="My App",
    page_icon="🚀",
    layout="wide",
)

st.title("Welcome!")
```

```python
import streamlit as st

# ❌ Wrong — st.title() before st.set_page_config()
st.title("Welcome!")
st.set_page_config(page_title="My App")  # ERROR!
```

### Common Page Config Options

| Parameter | Options | Default | Notes |
|---|---|---|---|
| `page_title` | Any string | "Streamlit" | Appears in browser tab |
| `page_icon` | Emoji or favicon URL | ⚡ | Appears in browser tab |
| `layout` | `"centered"` or `"wide"` | `"centered"` | `"wide"` uses full viewport |
| `initial_sidebar_state` | `"auto"`, `"expanded"`, `"collapsed"` | `"auto"` | Controls sidebar on load |

---

## 7. Common Mistakes

### Mistake 1: Forgetting `st.set_page_config()` Must Be First

**Error message:** `StreamlitAPIException: st.set_page_config() can only be called once per app page, and it must be the first Streamlit command in your script.`

**Fix:** Move `st.set_page_config()` to the top, right after imports.

### Mistake 2: Not Understanding the Rerun Model

**Symptom:** Widget values disappear, counters reset, state is lost.

**Fix:** Use `st.session_state` for anything that must persist across reruns. We'll cover this in depth in Module 05.

### Mistake 3: Using `print()` Instead of `st.write()`

**Symptom:** Output appears in the terminal, not the browser.

**Fix:** Always use `st.write()`, `st.markdown()`, or other `st.` functions for browser output. `print()` goes to stdout only.

### Mistake 4: Placing `st.set_page_config()` After Conditional Logic

**Symptom:** Error when the conditional branch is taken.

**Fix:** Always call `st.set_page_config()` unconditionally at the top.

---

## 8. Debugging Tips

| Problem | Solution |
|---|---|
| App doesn't update | Check for errors in the terminal where `streamlit run` is running |
| Widget value resets | You're storing state in a variable, not `st.session_state` |
| `st.set_page_config()` error | Move it to be the first `st.` call |
| Import errors | Make sure you're in the right virtual environment |
| Port already in use | Use `--server.port 8502` to use a different port |
| App is slow | Check for expensive computations outside `@st.cache_data` |

---

## 9. Best Practices

1. **Keep `st.set_page_config()` at the top** — always, unconditionally.
2. **Use meaningful variable names** — since the script reruns, clarity matters.
3. **Separate concerns** — put data processing in helper functions, not inline in the main script.
4. **Use `st.session_state` early** — even for simple apps, think about state.
5. **Version control your apps** — `.py` files with Streamlit are just scripts; Git works perfectly.
6. **Don't use `print()`** — use `st.write()` or `st.markdown()` for browser output.
7. **Comment your code** — future-you (and your teammates) will thank you.

---

## Key Takeaways

- Install Streamlit with `pip install streamlit` inside a virtual environment.
- Run an app with `streamlit run app.py`.
- The **rerun model** is the most important concept: the entire script reruns top-to-bottom on every interaction.
- Use `st.session_state` to persist data across reruns.
- `st.set_page_config()` **must** be the first Streamlit call.
- Streamlit provides rich text elements: titles, headers, Markdown, code blocks, captions, and dividers.

---

## Further Reading

- [Streamlit API Reference — Text Elements](https://docs.streamlit.io/develop/api-reference/text)
- [Streamlit API Reference — st.write](https://docs.streamlit.io/develop/api-reference/write-magic/st.write)
- [Streamlit Execution Model](https://docs.streamlit.io/develop/concepts/architecture/exec-model)
- [Streamlit Cheat Sheet](https://cheat-sheet.streamlit.app/)

---

## Related Materials

- 📓 Notebook: [01 — Streamlit Introduction](../notebooks/01_Streamlit_Introduction.ipynb)
- 📓 Notebook: [02 — First Streamlit App](../notebooks/02_First_Streamlit_App.ipynb)
- 📖 Reading: [01 — What Is Streamlit?](01_streamlit_introduction.md)
- 🖥️ Demo App: [01 — Introduction Demo](../apps/01_introduction_demo.py)
- 🖥️ Demo App: [02 — First App Demo](../apps/02_first_app_demo.py)
- ✏️ Exercise: [02 — First App Exercise](../exercises/02_first_app_exercise.py)
- 📝 Quiz: [01 — Streamlit Basics](../quizzes/01_streamlit_basics.md)
