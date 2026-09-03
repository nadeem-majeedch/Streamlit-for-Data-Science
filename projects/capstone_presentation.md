# Capstone Presentation Guide

> **🎤 Presentation Guide — 10-Minute Capstone Demo**
> *How to prepare and deliver an effective capstone presentation.*

---

## Overview

| Detail | Value |
|--------|-------|
| **Duration** | 10 minutes total |
| **Format** | 8-minute live demo + 2-minute Q&A |
| **Audience** | Instructor + classmates |
| **Equipment** | Laptop with deployed app, projector/screen |
| **Assessment** | 30 marks (see rubric) |

---

## Presentation Structure

### Minute 0–1: Introduction (60 seconds)

**What to cover:**
1. Your name and project title
2. One-sentence problem statement
3. Who the app is for
4. What the app does (high level)

**Example:**
> "Hi, I'm [Name]. My project is [Title] — a Streamlit dashboard that helps [target users] [solve problem]. It takes [input] and produces [output] through [key feature]."

**Tips:**
- Don't read from slides — speak naturally
- Make eye contact with the audience
- Keep it concise — you'll show the details in the demo

---

### Minute 1–6: Live Demo (5 minutes)

**What to demonstrate (in this order):**

1. **Start at the homepage** (30 seconds)
   - Show the overall layout
   - Point out the navigation
   - Mention the data source

2. **Demonstrate filters** (1 minute)
   - Change sidebar filters
   - Show how charts and KPIs update
   - Explain why you chose these filters

3. **Show visualizations** (1.5 minutes)
   - Walk through each chart type
   - Explain what insights they reveal
   - Show interactivity (hover, click, zoom)

4. **Demo ML/AI component** (1.5 minutes)
   - Enter sample input
   - Show prediction result
   - Explain confidence scores
   - Show model info

5. **Show error handling** (30 seconds)
   - Enter invalid input
   - Show graceful error message
   - Demonstrate edge case handling

**Demo Tips:**
- **Practice the demo 5+ times** before presentation day
- Have a backup plan if the internet is slow (prepare local version)
- Use realistic sample data, not random numbers
- Narrate as you go — don't just click silently
- If something breaks, acknowledge it and move on

**What NOT to do:**
- ❌ Click through everything silently
- ❌ Show code during the demo (save for Q&A)
- ❌ Demo features that aren't working
- ❌ Spend more than 5 minutes on the demo

---

### Minute 6–8: Architecture & Design (2 minutes)

**What to cover:**

1. **File structure** (30 seconds)
   - Show the directory tree
   - Explain what each file does
   - Highlight separation of concerns

2. **Key design decisions** (1 minute)
   - Why you chose this architecture
   - Why you chose this caching strategy
   - Why you chose this ML approach
   - What trade-offs you made

3. **Technical highlights** (30 seconds)
   - One clever solution you're proud of
   - One challenge you overcame
   - One thing you'd do differently

**Example script:**
> "My app has 6 main files: app.py is the entry point, data_loader.py handles all data operations, and each page is in the pages/ directory. I chose @st.cache_resource for the model because it's a singleton that should be shared across sessions. The hardest part was [challenge], and I solved it by [solution]."

---

### Minute 8–10: Q&A (2 minutes)

**Prepare for these common questions:**

| Question | What to Explain |
|----------|----------------|
| "Why did you choose this dataset?" | Domain relevance, size, variety, accessibility |
| "How does the model work?" | Algorithm choice, training process, evaluation metrics |
| "What would you do differently?" | Honest reflection, show growth mindset |
| "How did you handle [specific challenge]?" | Technical solution with reasoning |
| "Is this ready for production?" | Honest assessment of limitations |
| "How does caching work here?" | Explain @st.cache_data vs @st.cache_resource |
| "Why did you use session state here?" | Explain persistence needs |
| "What's the most interesting insight from the data?" | Domain knowledge, analytical thinking |

**Q&A Tips:**
- It's OK to say "I don't know, but I would investigate by..."
- Be honest about limitations
- Show you understand YOUR code
- If you used AI, be transparent about what it helped with

---

## Presentation Checklist

### Before the Presentation
- [ ] Deployed app is live and accessible
- [ ] Local backup version works (for offline demo)
- [ ] Presentation slides ready (optional but recommended)
- [ ] Demo practiced 5+ times
- [ ] All features tested on presentation day
- [ ] Sample data loaded and ready
- [ ] Browser bookmarks set for quick navigation
- [ ] Internet connection tested
- [ ] Backup plan for technical issues

### During the Presentation
- [ ] Start with introduction (name, project, problem)
- [ ] Show the live app (don't just show slides)
- [ ] Narrate as you demonstrate
- [ ] Explain architecture clearly
- [ ] Mention challenges and solutions
- [ ] Keep to time (8 min demo + 2 min Q&A)
- [ ] Answer questions confidently

### After the Presentation
- [ ] Submit all deliverables
- [ ] Upload presentation slides (if applicable)
- [ ] Verify deployment still works
- [ ] Respond to any follow-up questions

---

## Presentation Slide Template (Optional)

If you use slides, keep them minimal:

### Slide 1: Title
- Project name
- Your name
- Course name
- Date

### Slide 2: Problem
- One sentence problem statement
- Target users
- Why this matters

### Slide 3: Solution
- What the app does
- Key features (3-4 bullet points)
- Screenshot of the app

### Slide 4: Architecture
- File structure diagram
- Key technology choices
- Design decisions

### Slide 5: Demo (Transition)
- "Let me show you the live application"
- (Switch to browser for demo)

### Slide 6: Challenges & Lessons
- Biggest challenge faced
- How you solved it
- What you'd do differently

### Slide 7: Future Work
- Features you'd add with more time
- Scalability considerations
- Next steps

### Slide 8: Thank You
- "Questions?"
- Your contact info
- Repository URL
- Deployment URL

---

## Timing Guide

| Section | Time | Content |
|---------|------|---------|
| Introduction | 1:00 | Name, project, problem |
| Demo: Homepage | 0:30 | Layout, navigation, data |
| Demo: Filters | 1:00 | Sidebar controls, updates |
| Demo: Charts | 1:30 | Visualization walkthrough |
| Demo: ML/AI | 1:30 | Prediction, explanation |
| Demo: Errors | 0:30 | Error handling |
| Architecture | 1:00 | File structure, decisions |
| Design Choices | 1:00 | Trade-offs, highlights |
| Q&A | 2:00 | Questions and answers |
| **Total** | **10:00** | |

---

## Common Presentation Mistakes

| Mistake | Better Approach |
|---------|----------------|
| Reading from slides | Speak naturally, use slides as visual aid |
| Clicking through demo silently | Narrate every action and its purpose |
| Showing code during demo | Save code discussion for Q&A |
| Apologizing for bugs | Acknowledge and move on, or show backup |
| Going over time | Practice with a timer, cut non-essential parts |
| Not practicing | Practice 5+ times, including with an audience |
| Ignoring the audience | Make eye contact, speak to the room |
| Reading notes | Know your material, use bullet points only |

---

## Grading Criteria Reminder

| Criteria | Marks | What They Look For |
|----------|-------|-------------------|
| App walkthrough | 15 | Smooth demo, all features shown, engaging |
| Architecture explanation | 10 | Clear, shows understanding of design decisions |
| Q&A response | 5 | Accurate, thoughtful, shows technical depth |
| **Total** | **30** | |

---

## Related Materials

- 📋 Capstone Spec: [final_capstone.md](final_capstone.md)
- 📋 Grading Rubric: [capstone_rubric.md](capstone_rubric.md)
- ✅ Submission Checklist: [capstone_submission_checklist.md](capstone_submission_checklist.md)
