# 💬 Discussion Questions

> **Streamlit for Data Science — Learn, Build, Deploy**
> *Prompts for class discussions, review sessions, and active learning.*

---

## How to Use These Questions

- **Warm-ups (5 min):** Pick 1 question to start a session
- **Review sessions (30 min):** Work through 4–6 questions in groups
- **Seminars (60 min):** Assign questions as group presentations
- **Exam prep:** Students practice answers independently

---

## Phase 1 — Foundation (M01–M03)

### Streamlit vs. Other Tools
1. "If you already know Jupyter, why would you use Streamlit? When would you NOT use Streamlit?"
2. "A colleague says 'Dash is better than Streamlit.' What are the tradeoffs? When might they be right?"
3. "Your manager wants a 'simple dashboard.' Do you build it in Streamlit, Excel, or Tableau? Why?"

### First Applications
4. "What makes a good first Streamlit app for a Data Science portfolio?"
5. "You just built your first Streamlit app. What would you add to make it useful for your research group?"

### Design Philosophy
6. "A Data Science application is NOT simply a notebook placed inside a web page." — Discuss what this means in practice.
7. "What are the biggest UX mistakes you see in Data Science dashboards?"

---

## Phase 2 — Data & Visualization (M04–M06)

### Data Display
8. "When would you use `st.table()` instead of `st.dataframe()`? Give a real scenario."
9. "You have a dataset with 50 columns. How do you decide which to display and which to hide?"
10. "Your DataFrame has mixed types and missing values. How do you present this professionally?"

### Visualization
11. "Your stakeholder asks for a pie chart with 15 categories. How do you respond?"
12. "When would you choose Plotly over Matplotlib in a Streamlit app? When would you choose native `st.bar_chart`?"
13. "A chart looks correct but tells the wrong story. How do you catch this?"

### Session State
14. "Explain the Streamlit rerun model to someone who has never used Streamlit. Use an analogy."
15. "You have a multi-step form. Where should you store the data from each step? Why?"
16. "A student uses `global` variables instead of `st.session_state`. What goes wrong?"

---

## Phase 3 — Architecture & Performance (M07–M09)

### Caching
17. "You add `@st.cache_data` to a function that returns a database connection. What breaks?"
18. "When is caching harmful? Give two real examples."
19. "How would you implement cache invalidation when new data arrives?"

### Architecture
20. "Your colleague has a 500-line `app.py`. How do you convince them to refactor? What's the first step?"
21. "Should every Streamlit app be multipage? Why or why not?"
22. "How do you decide what goes in a shared utility module vs. a page-specific file?"

### APIs and Databases
23. "You're fetching data from an API that goes down every afternoon. How do you handle this?"
24. "Show this code to the class. What's the security vulnerability?" (show SQL injection example)
25. "When would you use a database instead of a CSV file in a Streamlit app?"

---

## Phase 4 — Machine Learning (M10–M12)

### ML Pipeline
26. "Your model works great in a notebook but poorly in the Streamlit app. What could be wrong?"
27. "How do you explain model confidence to a non-technical user through a Streamlit interface?"
28. "Should the app retrain the model when new data is uploaded? What are the tradeoffs?"

### Model Deployment
29. "Your model was trained on data from 2022. It's now 2025. What concerns do you have?"
30. "How would you handle a prediction request where the input is missing a critical feature?"
31. "A user says the prediction 'feels wrong.' How do you investigate?"

---

## Phase 5 — AI/LLM & Production (M13–M16)

### LLM Applications
32. "Should a healthcare Streamlit app use an LLM for diagnosis? Why or why not?"
33. "What is prompt injection? How would you defend against it in a Streamlit chat app?"
34. "When would you use a local/open-source model instead of a cloud API?"
35. "How would you test an LLM-powered Streamlit application?"

### Security
36. "You find a hardcoded API key in a student's GitHub repo. What do you do?"
37. "A user uploads a file to your Streamlit app. What security risks exist?"
38. "What's the difference between authentication and authorization in a Streamlit context?"

### Deployment and Production
39. "Your Streamlit app works perfectly on your laptop. It fails on Community Cloud. Walk through your debugging process."
40. "What does 'production-ready' mean for a student project vs. a company application?"
41. "How would you monitor a Streamlit app running in production?"

---

## Phase 6 — Capstone & Integration

### Design Decisions
42. "You have 3 weeks to build a capstone project. How do you scope it to be achievable?"
43. "Your capstone project requires an ML model and a chat interface. How do you structure the code?"
44. "How do you decide between building a feature from scratch vs. using an existing library?"

### Professional Practice
45. "What would you include in a README for a deployed Streamlit app?"
46. "How do you version a Streamlit application that's deployed on Community Cloud?"
47. "If you were hiring a junior Data Scientist, what Streamlit projects would impress you?"

### Reflection
48. "What was the hardest concept in this course? How did you overcome it?"
49. "How will you use Streamlit in your future work or studies?"
50. "If you could add one feature to Streamlit, what would it be and why?"

---

## Group Discussion Activities

### Activity 1: Code Review (20 min)
Show a student's Streamlit app code (anonymized). Groups discuss:
- What's good about the code?
- What would you improve?
- Is the architecture maintainable?

### Activity 2: Architecture Debate (15 min)
Two groups argue for different approaches:
- Group A: "Single-file app is fine for small projects"
- Group B: "Always modularize from the start"

### Activity 3: Debugging Race (10 min)
Show 3 broken Streamlit apps. First team to identify all bugs wins.

### Activity 4: Design Challenge (20 min)
Given a dataset and a user story, groups sketch a dashboard design on paper. Present and critique.

---

## Related Materials

- [Session Plans](2_hour_lecture_plan.md) — When to use each question
- [Common Mistakes](common_student_mistakes.md) — Related error patterns
- [Teaching Roadmap](teaching_roadmap.md) — Module progression
