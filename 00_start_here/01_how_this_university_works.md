# How this university works

| Read time | Read before | Next |
|---|---|---|
| ~20 minutes | Your first course | [Choose your major](02_choose_your_major.md) · [AI-native study protocol](03_ai_native_study_protocol.md) |

This page explains the structure (years, semesters, credits), how progress is measured (levels and mastery gates), how to pace yourself, how to prove your progress without a registrar, and how to study with others.

## 1. The structure

### Years and semesters

The curriculum has **5 years** and **10 semesters**. A semester is **15 weeks**: 14 teaching weeks and one review and exam week.

| Year | Semesters | What happens | Exit level |
|---|---|---|---|
| 1 · Foundations | 1–2 | 12 common courses: programming, maths, systems, tools, web, SQL, AI-native learning, communication | L2 (intern-ready practice) |
| 2 · Core CS | 3–4 | 12 common courses: algorithms, architecture and C, OS, networks, software engineering, maths for ML, databases, distributed systems, security, ML, cloud, compilers | L3 in the core |
| 3 · Major core | 5–6 | Your major's five core courses, PRO301 (ethics, law, responsible AI), CAR301 (Career Lab I), electives | L3 (job-ready) in your major |
| 4 · Advanced and industry | 7–8 | Your major's four advanced courses, two overlap courses, IND401 (industry co-op studio), CAR401 (Career Lab II) | L4 (expert) |
| 5 · Mastery and research | 9–10 | A frontier seminar, RES501 and RES502 (research methods, reproducing papers), a two-semester thesis or capstone (THS501–502), LCH502 (career launch or founder studio) | L5 (research) |

Years 1–2 are identical for every major. You **declare a major** at the end of Year 2 ([Year 2 README](../02_year_2_core_computer_science/README.md#declaring-your-major)).

### Credits

One credit is about **30 hours** of work, so a **4-credit course is about 120 hours**: reading and lectures, labs, projects, problem sets and AI-off drills. All 257 courses in the [catalog](../catalog.json) are 4 credits.

| Block | Courses | Credits | Hours (approx.) |
|---|---|---|---|
| Year 1 | 12 | 48 | 1,440 |
| Year 2 | 12 | 48 | 1,440 |
| Your major (Years 3–5) | 10 (5 core, 4 advanced, 1 frontier seminar) | 40 | 1,200 |
| Shared courses (Years 3–5) | 9 (PRO301, CAR301, IND401, CAR401, RES501, RES502, THS501, THS502, LCH502) | 36 | 1,080 |
| Overlap specialization (Year 4) | 2 | 8 | 240 |
| **Required total** | **45** | **180** | **≈ 5,400** |
| Electives | Recommended in each major's path, typically 4–6 courses | 16–24 | 480–720 |

Hours are an estimate for a learner starting at the course's entry level. Some people need more; nobody should need much less if they do the labs and projects properly.

### What every course contains

Each course folder has:

- `README.md`: the syllabus. Entry and exit level, prerequisites, learning outcomes, chapters and lessons, a 15-week plan, how to use AI in that course, assessment and the **mastery gate**, interview questions, and free resources.
- `projects.md`: weekly labs and three projects. P1 is L1 (about 6 hours), P2 is L2 (about 15 hours), and P3 is portfolio-grade L3 (about 30 hours), each with measurable acceptance criteria.
- `chapters/`: lesson notes, added in later phases. Until they exist, use the free resources the syllabus lists for each chapter.

Prerequisites are listed in [`CATALOG.md`](../CATALOG.md). A prerequisite means "you have passed its mastery gate", not "you have read it".

## 2. Levels L0–L5

Every course states where it starts and where it takes you.

| Level | Name | You can… | Typical point |
|---|---|---|---|
| L0 | Absolute beginner | follow instructions and reproduce worked examples | Start of Year 1 |
| L1 | Foundations | solve standard exercises alone and explain why they work | Mid Year 1 |
| L2 | Practitioner (intern-ready) | build small working systems, debug them, and read real code | End of Year 1 |
| L3 | Professional (job-ready) | ship production-quality work in a team, with tests, docs and trade-off reasoning | End of Year 3 in your major |
| L4 | Expert (senior, hard to replace) | design systems others build on, handle failures nobody planned for, and lead | End of Year 4 (and years of work after) |
| L5 | Research and frontier | create new knowledge: read, reproduce and extend papers; publish | Year 5 |

L4 is a direction, not a promise. Nobody becomes a senior engineer from coursework alone; the Year 4 co-op studio, open-source work and real production experience are part of getting there.

## 3. Mastery gates

A **mastery gate** is a concrete task you must be able to do before moving on. It is written as "You pass when you can…", and it is pass or fail. Examples from the courses:

- [FND104](../01_year_1_foundations/semester_1/FND104_the_developers_toolkit_linux_shell_git/README.md): on a fresh Linux VM with AI off, within 2 hours, set up key-only SSH, find the breaking commit with `git bisect run`, open a pull request with green CI, recover a "lost" commit with `reflog`, and write a ShellCheck-clean log-analysis script.
- [FND115](../01_year_1_foundations/semester_2/FND115_databases_i_data_modeling_and_sql/README.md): with AI off, turn an unseen business description into a normalised schema in 45 minutes, answer 10 SQL questions exactly, and make a slow query at least 10× faster with an index, proven with `EXPLAIN ANALYZE`.

There are three kinds:

| Gate | Where it is defined | What passing means |
|---|---|---|
| **Course gate** | The "Assessment and mastery gate" section of each course README | You may take courses that list this one as a prerequisite |
| **Year gate** | [Year 1 README](../01_year_1_foundations/README.md#year-1-mastery-gate) (a two-day practical) and [Year 2 README](../02_year_2_core_computer_science/README.md#year-2-mastery-gate) (oral systems trace, fundamentals sprint, portfolio check, major declaration) | You move to the next year |
| **Major skill-map gates** | The "Skill map by level" section of each major's README | You are at that level in that field |

### Rules for gates

1. **Unseen material.** A gate task must be new to you. Use the course's sample gate only for practice; for the real attempt, get a fresh task from a peer, a mentor, or a variation you did not write yourself.
2. **AI-off means off.** Official language and tool documentation is allowed unless the gate says otherwise; AI assistants, autocomplete that writes code, and search for solutions are not.
3. **Timed.** Use the stated time limit. Overrunning by more than 25% is a fail; try again in a week.
4. **Retakes are normal.** Failing a gate tells you what to practise. Record the attempt, fix the gap, and retake with a different task after at least a few days.
5. **Partial credit does not exist.** If the gate has four parts, you pass all four.

### Testing out of a course

If you already know a course, you do not have to sit through it. Answer its five [placement questions](05_placement_check.md); if you get all five right without help, attempt the course gate under the rules above. Pass, and the course is done. Record it like any other pass, with evidence.

## 4. Pacing: full-time and part-time

A full semester is six courses × 120 hours = 720 hours.

| Pace | Hours per week | Courses at once | One semester takes | Years 1–2 take | All 5 years take |
|---|---|---|---|---|---|
| Full-time intensive | about 48 | 6 | 15 weeks | 2 years | 5 years |
| Full-time standard | about 40 | 6 | 18 weeks | about 2 years | about 5½ years |
| Part-time | 15–25 (about 20) | 3 | two terms of 18 weeks | 3–4 years | about 8–9 years |
| Light | about 10 | 1–2 | four or more terms | 6+ years | Pick a target, not the whole path |

A curriculum "year" is two semesters of teaching plus breaks, as at a university. The part-time and light rows are arithmetic from the hours (Years 1–2 are about 2,880 hours; at 20 hours a week that is 144 study weeks before breaks), not a recommendation to stop early. Many part-time learners aim first for **job-readiness in one major**: Years 1–2, their major's five Year 3 courses, CAR301 and the career-readiness section, about 3,700 hours. At 20 hours a week that is roughly 4–5 years including breaks; with prior knowledge tested out through the placement check, often much less.

Pacing advice that holds at every speed:

- **Spread each course across at least two days a week.** Spacing practice over days helps long-term retention more than one long block (see the [study protocol](03_ai_native_study_protocol.md)).
- **Keep weekly rhythm per course:** about 3 hours of reading and lectures, 3 hours of lab, 2 hours of project work and AI-off drills (Year 1's split, at full-time pace).
- **Use the part-time pairings** given in the [Year 1](../01_year_1_foundations/README.md#suggested-weekly-timetable) and [Year 2](../02_year_2_core_computer_science/README.md#part-time-path-1525-hours-a-week) READMEs. They respect every prerequisite.
- **Rest one day a week** and take a two-week break between semesters. Burnout costs more weeks than rest does.
- **Working professionals** should use each major's "fast track" section: it lists which courses to take and which to test out of.

## 5. Self-certifying your progress

There is no registrar, so you keep your own record and make it checkable. The rule: **every gate you claim has public evidence that someone else can verify.**

### The progress repository

Create one public repository (for example `cs-university-progress`) with:

```text
cs-university-progress/
  PROGRESS.md        one row per course: status, date, evidence links, reviewer
  AI_LOG.md          optional summary; each project repo keeps its own AI log
  gates/
    FND101.md        what the gate task was, your result, time taken, what failed first
    FND104.md
  drills/
    baseline.md      AI-off scores over time (see the study protocol)
```

A `PROGRESS.md` template:

```markdown
| Code | Course | Status | Gate passed | Evidence | Reviewer |
|---|---|---|---|---|---|
| FND101 | Programming I | passed | 2026-12-04 | [P3 repo](https://github.com/you/expense-settler), [gate notes](gates/FND101.md), [screen recording](link) | A. Peer (study circle) |
| FND104 | Developer's Toolkit | passed (tested out) | 2026-11-20 | [gate notes](gates/FND104.md), [PR with green CI](link) | Mentor: B. Name |
| FND102 | How Computers Work | in progress | – | [nand2tetris projects 1–3](link) | – |
```

### What counts as evidence

| Evidence | Good for | How to make it checkable |
|---|---|---|
| Project repository (P2 or P3) | Every course | README a stranger can run in 10 minutes, tests in CI, a results section with measurements |
| Gate notes | Every gate | The task as given, your solution, time taken, and what you got wrong first |
| Screen recording of an AI-off gate | Gates where honesty matters most | One unedited recording, or a reviewer watching live on a call |
| Pull requests and code reviews | Collaboration skills | Links to merged PRs, including review comments you gave and received |
| AI log | Any AI-assisted work | Prompt, output, what you accepted or rejected, and how you verified it |
| A written explanation or short talk | Theory courses | A design note, proof write-up or recorded 5-minute explanation |

### Reviewers

A gate is stronger when someone else watched or checked it. In order of strength:

1. **A mentor or working engineer** set the task and reviewed the result.
2. **A peer** in your study circle set an unseen task, watched the AI-off part live, and checked the result against the gate statement.
3. **Self-review** with a recording, if no one is available. Mark it as self-reviewed.

Be honest about which kind each gate was. A recruiter or graduate school that reads your progress page will trust a page that says "self-reviewed" more than one that overclaims.

### What self-certification is not

It is not a degree, and it does not carry academic credit at any institution. Its value is that it **replaces a claim with evidence**: an interviewer can open your repository, read your gate notes and ask you to repeat a task live. See [the FAQ](06_faq.md) for where a formal degree still matters.

## 6. Studying in a group or with a mentor

People who study with others tend to keep going longer and catch their own blind spots sooner. You do not need permission to start a group.

### A study circle

- **Size:** 3–6 people at roughly the same point. Mixed levels work if the stronger members take the reviewer role.
- **Weekly meeting (60–90 minutes):**
  1. Each person: what you finished, where you are stuck, one thing you learned (3 minutes each).
  2. Explain-back: one person explains a hard concept from this week without notes; others ask "why" until it holds or breaks.
  3. Code or proof review: swap one piece of work and review it with the [FND106](../01_year_1_foundations/semester_1/FND106_technical_communication_and_professional_skills/README.md) checklist.
  4. Plan: each person names the next week's deliverable.
- **Rotating roles:** facilitator (keeps time), examiner (writes an unseen gate task for someone due to attempt one), reviewer (checks the evidence afterwards).
- **Mock gates:** once a month, run a timed AI-off gate for anyone who is ready, with someone watching.
- **Shared rules:** written in the group's README: the AI-off rules, how you give feedback, and that everyone's code is their own.

### A mentor

A mentor is someone a few years ahead in your target field. Mentors are not required, but they speed up the hard part: judgement.

- **What to ask for:** 30–45 minutes a month. Come with your progress page, one specific question, and one piece of work to review.
- **Good questions:** "Would this project convince you in an interview? What is missing?" "Which of these two designs would you choose, and why?" "What do new hires in your team struggle with?"
- **Where to find one:** maintainers of open-source projects you contribute to, alumni of your school or college, speakers at local meetups, people who answer questions well in public forums. Ask for one specific thing, not "will you be my mentor".
- **Give back:** share what you build, report what helped, and later mentor someone in Year 1.

### Teachers and clubs

Every syllabus is a ready course outline: weekly plan, labs, projects, assessments and a mastery gate. A college club can run one course per semester with weekly meetings; a teacher can adopt a course's labs and projects inside an existing subject. The content is MIT-licensed; attribution is appreciated.

## 7. How AI fits in

Every course has a "Working with AI" section. The defaults across the university:

| Situation | Rule |
|---|---|
| Year 1, weeks 1–6 | AI-off for writing code and proofs. AI may explain concepts as a tutor that gives hints, not answers. |
| From Year 1, week 7 | AI allowed for building, with an `AI_LOG.md` in every repository. |
| Every week, every course | At least one AI-off drill. |
| Exams and mastery gates | AI-off unless the course states an AI-allowed part. |

The reasons, with the research behind them and a daily routine, are in the [AI-native study protocol](03_ai_native_study_protocol.md).

## 8. Keeping up to date

The curriculum is written in phases and revised as tools, laws and markets change. Facts carry a "checked" month; check again before you pay for anything. [`STATUS.md`](../STATUS.md) shows which syllabi, projects and chapter notes exist today. Corrections are welcome through the repository's issues; read [`docs/CONTENT_STANDARD.md`](../docs/CONTENT_STANDARD.md) first.

_Last reviewed: 2026-10_
