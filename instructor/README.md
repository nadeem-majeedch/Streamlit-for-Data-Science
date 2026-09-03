# 👩‍🏫 Instructor Resources

> **Streamlit for Data Science — Learn, Build, Deploy**
> *Teaching guide, session plans, assessment tools, and instructor-only reference materials.*

---

## ⚠️ Instructor-Only Content

This directory contains materials **not shared with students**. Keep solution files, grading guides, and internal documentation here. Do not place student-facing links to these files in any README students can see.

---

## Navigation

| Document | Description | When to Use |
|----------|-------------|-------------|
| [**Course Plan**](course_plan.md) | Semester-long plan, weekly schedule, time allocation | Start of semester, course planning |
| [**Teaching Roadmap**](teaching_roadmap.md) | Module progression, prerequisites, dependencies | Planning module order and pacing |
| [**Lecture/Lab Sequence**](lecture_lab_sequence.md) | Complete 20-session sequence with CLO mapping and resource links | Course planning, before each session |
| [**Session Plans**](2_hour_lecture_plan.md) | Detailed 90–120 min session plans for every module | Before each lecture |
| [**Lab Activities**](lab_activities.md) | Hands-on lab guides with timing and solutions | Lab sessions |
| [**Discussion Questions**](discussion_questions.md) | Prompts for class discussions by topic | Seminars, review sessions |
| [**Assessment Strategy**](assessment_strategy.md) | Grading policies, rubrics, weight distribution | Start of semester, grading |
| [**Common Mistakes**](common_student_mistakes.md) | Error catalog with interventions and fixes | Grading, feedback, review sessions |
| [**Solution Guide**](solution_guide.md) | Index and walkthrough of all exercise solutions | Grading, office hours |
| [**Exercise Guide**](exercise_guide.md) | Per-exercise grading notes and common issues | Grading assignments |
| [**Deployment Troubleshooting**](deployment_troubleshooting.md) | Instructor guide for student deployment issues | Deployment weeks, office hours |

### Solution Files (Keep Separate)

| Directory | Contents |
|-----------|----------|
| [solutions/](solutions/README.md) | All exercise and assignment solutions |
| [solutions/exercises_solutions/](solutions/exercises_solutions/) | Runnable Streamlit app solutions |
| [solutions/exercise_notes/](solutions/exercise_notes/) | Grading notes and approach guides |
| [solutions/assignment_solutions/](solutions/assignment_solutions/) | Assignment rubrics and solution notes |

---

## Quick Start for New Instructors

### Before the Semester

1. Read the [Course Plan](course_plan.md) for the full 16-week schedule
2. Review the [Teaching Roadmap](teaching_roadmap.md) for module dependencies
3. Set up your local environment with all dependencies
4. Run through all 20 exercises yourself — expect ~8 hours
5. Deploy one app to Streamlit Community Cloud to understand the process

### Before Each Session

1. Open the [Session Plan](2_hour_lecture_plan.md) for that module's session
2. Review the reading material students should have completed
3. Prepare the live-coding example (test it the night before)
4. Note which exercises are assigned for that week

### During Grading

1. Use the [Exercise Guide](exercise_guide.md) for per-exercise grading notes
2. Check [Common Mistakes](common_student_mistakes.md) for patterns
3. Run student submissions against solutions in [solutions/](solutions/README.md)
4. Apply rubrics from [Assessment Strategy](assessment_strategy.md)

---

## Session Structure (Recommended)

Every 90–120 minute session follows this pattern:

| Time | Activity | Notes |
|------|----------|-------|
| 0:00–0:05 | **Check-in** | Attendance, brief recap of previous session |
| 0:05–0:20 | **Concept Introduction** | Why this matters, real-world motivation |
| 0:20–0:35 | **Live Demo** | Build something small in Streamlit live |
| 0:35–0:40 | **Break** | — |
| 0:40–0:65 | **Guided Practice** | Students follow along, modifying the demo |
| 0:65–0:85 | **Independent Work** | Students work on exercise or notebook |
| 0:85–0:95 | **Discussion / Q&A** | Common mistakes, design decisions |
| 0:95–0:100 | **Wrap-up** | Next session preview, homework assignment |

---

## Repository File Map (Instructor View)

```
instructor/
├── README.md                          ← You are here
├── course_plan.md                     ← Semester schedule
├── teaching_roadmap.md                ← Module progression
├── lecture_lab_sequence.md            ← Complete 20-session sequence (PRIMARY REFERENCE)
├── 2_hour_lecture_plan.md             ← Session-by-session lecture plans
├── lab_activities.md                  ← Lab session guides
├── discussion_questions.md            ← Discussion prompts
├── assessment_strategy.md             ← Grading and rubrics
├── common_student_mistakes.md         ← Error catalog
├── solution_guide.md                  ← Solution walkthroughs
├── exercise_guide.md                  ← Exercise grading notes
├── deployment_troubleshooting.md      ← Deployment help
├── .gitkeep
└── solutions/
    ├── README.md                      ← Solution index
    ├── exercises_solutions/           ← Runnable .py solutions
    │   ├── 01_hello_streamlit_solution.py
    │   ├── 03_widget_mastery_solution.py
    │   ├── 04_dataset_filter_solution.py
    │   ├── 05_layout_basics_solution.py
    │   ├── 06_dashboard_builder_solution.py
    │   ├── 09_api_connectors_solution.py
    │   └── 16_production_ready_solution.py
    ├── exercise_notes/                ← Markdown grading guides
    │   ├── 07_data_display_notes.md
    │   ├── 08_visualization_notes.md
    │   ├── 09_file_upload_notes.md
    │   ├── 10_dashboard_workshop_notes.md
    │   ├── 11_state_management_notes.md
    │   ├── 12_caching_notes.md
    │   ├── 13_architecture_notes.md
    │   ├── 14_database_notes.md
    │   ├── 15_ml_notes.md
    │   ├── 17_nlp_notes.md
    │   └── 18_llm_notes.md
    └── assignment_solutions/          ← Assignment grading guides
        ├── A01_solution_notes.md
        ├── A02_solution_notes.md
        ├── A03_solution_notes.md
        └── A04_solution_notes.md
```

---

## Related Materials (Student-Facing)

- [Course Blueprint](../docs/course_blueprint.md)
- [Curriculum](../docs/curriculum.md)
- [Learning Outcomes](../docs/learning_outcomes.md)
- [Deployment Checklist](../docs/deployment_checklist.md)
- [Security Guide](../docs/security.md)

---

> **Note:** Do not commit solution files to a public repository. Use `.gitignore` or a private branch for instructor materials if needed.
