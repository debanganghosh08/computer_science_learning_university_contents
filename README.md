# Computer Science and IT University

**A free, open, 5-year university curriculum for every computer science and IT role, built for the age of AI. It takes you from zero to industry-ready, and on to research.**

AI now writes a large share of everyday code, answers first-line support tickets, drafts SQL, and triages security alerts. Some jobs are shrinking and others are growing fast, and the skills that make someone hard to replace have changed. Most curricula have not caught up. This one is written for that reality:

- **Every course is AI-native.** Each one says what AI tools already do in that area, what you must still own, which drills to do without AI, and how to verify AI output.
- **It starts from zero.** Year 1 assumes you know nothing. Year 5 ends with research, a thesis or capstone, and a career launch or founder path.
- **It covers the whole field.** It has 20 majors, from software, backend, frontend and mobile to cloud, DevOps/SRE, cybersecurity, ethical hacking, security architecture, data analysis, data science, data engineering, machine learning, deep learning, AI engineering, forward-deployed engineering, embedded/IoT, quality engineering, IT infrastructure, and a theory-and-research major.
- **Overlaps are first-class.** Real jobs sit between fields, such as cloud + security, backend + cloud, ML + platform and AI + security. There are 12 overlap specializations for them.
- **It is hands-on.** Every course has weekly labs and three projects (beginner → portfolio-grade), each with measurable acceptance criteria inspired by real systems.
- **Job and market readiness is built in.** It includes hiring-level DSA, system design, AI-driven interviews (how they work today, with full simulation question banks), flagship industry projects, portfolio, job search, negotiation, and a solo-founder path.

> Status: this university is being written in phases. Every syllabus is planned in [`CATALOG.md`](CATALOG.md); what is finished is tracked in [`STATUS.md`](STATUS.md).

## How it is organised

```
00_start_here/                      how this university works, choosing a major, studying with AI, setting up your lab
01_year_1_foundations/              Year 1: the common foundation (programming, maths, systems, tools, AI-native learning)
02_year_2_core_computer_science/    Year 2: core CS (algorithms, OS, networks, databases, security, ML, cloud, compilers)
03_majors/                          Years 3–5: 20 majors, each with its own learning path
04_overlaps/                        12 cross-field specializations (e.g. cloud security, MLOps, AI security, FinTech)
05_shared_years_3_to_5/             ethics and law, career labs, industry co-op, research methods, thesis, career launch
06_career_and_market_readiness/     market map, DSA for hiring, system design, AI-driven interviews, industry projects, portfolio, founder path
07_library/                         glossary, reading lists, free resource index, certifications map
docs/CONTENT_STANDARD.md            how every page is written (templates and quality bar)
catalog.json                        the source of truth for every course code, title, semester and prerequisite
```

Every course folder has a `README.md` (the syllabus: chapters, lessons, weekly plan, assessment, resources), a `projects.md` (labs and projects), and `chapters/` (lesson notes).

## The 5-year map

| Year | Semesters | What happens |
|---|---|---|
| 1 · Foundations | 1–2 | Programming (Python, then Java/TypeScript), discrete maths, linear algebra and calculus, probability, how computers work, Linux/Git, web basics, SQL, AI-native learning, technical communication |
| 2 · Core CS | 3–4 | Algorithms, architecture and C, operating systems, networks, software engineering, maths for ML, database internals, distributed systems, security, ML foundations, cloud/DevOps, compilers |
| 3 · Major core | 5–6 | Your major's five core courses, professional ethics and law, Career Lab I (DSA, portfolio, open source), electives |
| 4 · Advanced + industry | 7–8 | Your major's four advanced courses, an overlap specialization, an industry co-op studio, Career Lab II (interviews, system design, AI-driven assessments) |
| 5 · Mastery + research | 9–10 | A frontier seminar, research methods, reproducing papers, a two-semester thesis or capstone, career launch or founder studio |

The levels run **L0 (absolute beginner) → L1 → L2 (intern-ready) → L3 (job-ready) → L4 (expert, hard to replace) → L5 (research)**. Every course states where it takes you, and every stage has a mastery gate: a concrete thing you must be able to do before moving on.

## Majors

| Major | Code |
|---|---|
| Computer Science (Theory, Systems and Research) | CSG |
| Software Engineering | SWE |
| Backend Engineering | BE |
| Frontend Engineering | FE |
| Mobile Engineering | MOB |
| Cloud Engineering | CLD |
| DevOps, SRE and Platform Engineering | OPS |
| Cybersecurity: Defense, Operations and Governance | SEC |
| Ethical Hacking and Offensive Security (Authorized Testing) | OFF |
| Security Architecture | SAR |
| Data Analysis and Analytics | DAN |
| Data Science | DSC |
| Data Engineering | DEN |
| Machine Learning Engineering | MLE |
| Deep Learning | DLR |
| AI Engineering: LLM Applications and Agents | AIE |
| Forward Deployed Engineering | FDE |
| Embedded Systems and IoT | EMB |
| Software Quality and Test Engineering | QAE |
| IT Infrastructure and Network Engineering | NET |

Each major lives in [`03_majors/`](03_majors/), and its README is the full learning path. The complete course list is in [`CATALOG.md`](CATALOG.md).

## How to use it

- **Self-learners:** start at [`00_start_here/`](00_start_here/). Take the placement check to skip what you already know, then follow one major's path. A full-time pace is about 40–48 hours a week (six 4-credit courses of ~120 hours each per 15-week semester); at 15–25 hours a week, take three courses per semester and the path stretches over more years.
- **College students:** use it alongside your degree. Map your college subjects onto Years 1–2, use the labs and projects to go deeper than your syllabus, and start the career-readiness section in your third year.
- **Working professionals:** every major has a fast track. Jump to the courses you lack and to the career-readiness section for the interview loop of your target role.
- **Teachers and clubs:** every syllabus is a ready course outline with weekly plans, labs, projects and assessments. Use it freely under the license.

## Contributing

Corrections and improvements are welcome. Read [`docs/CONTENT_STANDARD.md`](docs/CONTENT_STANDARD.md) first: specific beats generic, every fact needs a dated source, and security content teaches defense and authorized practice only. After adding course files, run `python tools/build_indexes.py`.

## License

[MIT](LICENSE) © Debangan Ghosh
