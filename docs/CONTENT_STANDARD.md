# Content standard

Every page in this university follows this standard. If you add or edit a course, read this first.

## 1. The promise we write to

A reader who knows nothing walks in at Year 1, and walks out of Year 5 able to get hired in their field, hold their own against senior engineers, ship a product alone, or start research. Every page must move the reader toward that. If a sentence does not teach, show, or test something, delete it.

## 2. Non-negotiables

1. **Specific, never generic.** Name the algorithm, the data structure, the protocol, the tool (with a version or year when it matters), the standard (RFC number, NIST document, OWASP list), the paper, the dataset, the real system. "Learn about databases" is banned; "B+tree page splits, write-ahead logging, MVCC snapshots in PostgreSQL" is the bar.
2. **Teach the concept, then the tool.** Tools change every two years; concepts last twenty. Every tool appears as an example of a concept.
3. **Hands-on everywhere.** Every chapter has practice. Every course has weekly labs and three projects (L1, L2, L3) with measurable acceptance criteria.
4. **AI-era honest.** Every course says what AI tools already do in this area (named tools), what a human must still own, which drills to do without AI, and how to verify AI output. No hype, no doom: only what can be checked.
5. **Sourced facts only.** Any number about the job market, salaries, adoption or performance needs a link and the month it was checked. If you cannot verify it, write "(unconfirmed)" or leave it out. Never invent statistics, quotes, company practices or benchmark results.
6. **Real-world inspired.** Use real systems as case studies, from India and the world: UPI and NPCI, IRCTC, Aadhaar and DigiLocker, ONDC, Swiggy, Zomato, Flipkart, Zerodha, as well as Google, Netflix, Stripe, Amazon, Uber, Cloudflare and others. State only what is public and sourced. Label anything you imagine as "illustrative scenario".
7. **Safe security teaching.** Security content teaches concepts, defenses, methodology, law and ethics, and points to legal practice environments (PortSwigger Web Security Academy, OWASP Juice Shop, TryHackMe, Hack The Box, OverTheWire, picoCTF, CTF archives). Never step-by-step attack instructions against real systems, never working payloads or weaponized code, never evasion techniques. Always written authorization and scope first.
8. **Free resources first.** Prefer official documentation, open textbooks, university course pages (MIT OpenCourseWare, Stanford, CMU, Berkeley), arXiv, and standards bodies. Paid resources only when nothing free is as good, and say so.
9. **Plain English.** Short sentences. Define every term the first time it appears. Example before abstraction. Write for a smart 18-year-old whose first language may not be English.
10. **Neutral teaching voice.** No meta-notes about how a page was produced, no self-promotion, no filler like "in today's fast-paced world".

## 3. Levels and mastery gates

| Level | Name | You can… |
|---|---|---|
| L0 | Absolute beginner | follow instructions and reproduce worked examples |
| L1 | Foundations | solve standard exercises alone and explain why they work |
| L2 | Practitioner (intern-ready) | build small working systems, debug them, and read real code |
| L3 | Professional (job-ready) | ship production-quality work in a team, with tests, docs and trade-off reasoning |
| L4 | Expert (senior, hard to replace) | design systems others build on, handle failures nobody planned for, and lead |
| L5 | Research and frontier | create new knowledge: read, reproduce and extend papers; publish |

Every course states its entry and exit level. A **mastery gate** is a concrete thing you must be able to do (not a percentage) before moving on.

## 4. Folder layout

```
<CODE>_<slug>/
  README.md        the syllabus (template A)
  projects.md      labs and projects (template C)
  chapters/        lesson notes, one file per chapter (template B), named NN_<slug>.md
```

Course codes, titles, semesters and folder paths come from [`catalog.json`](../catalog.json). Do not invent new codes; propose changes in an issue. File and folder names are lowercase `snake_case`. Links between pages are relative.

## 5. Template A: course syllabus (`README.md`)

```markdown
# CODE · Course title

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 1 · 1 | 4 (≈ 120 hours) | L0 → L2 | none | CODE, CODE |

## Why this course matters now
3–5 specific sentences: what this work looks like in industry today, what AI tools already
do here (named), and what still needs a skilled human.

## Learning outcomes
6–10 measurable outcomes ("implement", "measure", "debug", "design", "compare", "explain why").

## Chapters and lessons
### Chapter 1 · Title (weeks 1–2)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Title | concrete concepts, named techniques, the key idea in one line | a specific exercise |
(4–6 lessons per chapter, 8–12 chapters covering 14 weeks)
**Check your understanding:** 3 questions that test reasoning, not recall.

## Weekly rhythm
Week → chapter, lab, deliverable (14 weeks + review/exam week).

## Working with AI in this course
- Use AI for: …
- Do without AI (drills): …
- Verify AI output by: …
- Where AI still fails here: … (only what you can show)

## Assessment and mastery gate
Weights (labs, projects, exam). Gate: "You pass when you can …".

## Industry reality
Where this is used (named systems, sourced) and 5 interview questions that come from this
course, each with what a strong answer must cover.

## Resources (free first)
Primary text or course, documentation, papers, practice platforms (all links checked).

## Sources
Dated sources for every fact on this page.

_Last reviewed: YYYY-MM_
```

## 6. Template B: chapter lesson notes (`chapters/NN_slug.md`)

```markdown
# CODE · Chapter N · Title

**Goal:** one sentence. **Time:** ~X hours. **Level:** Lx → Ly.

## Lesson N.1 · Title
**You will learn:** …
Explanation with a worked example (code, diagram or numbers).
**Common mistakes:** …
**Try it:** exercises with expected outputs.
**AI pair exercise:** a prompt to try, and how to critique and verify the answer.

(more lessons)

## Chapter quiz
Questions, with answers inside <details> blocks.

## Further reading
```

## 7. Template C: labs and projects (`projects.md`)

```markdown
# CODE · Labs and projects

## Labs
| Lab | Goal | You submit | Time |

## Projects
### P1 · Name (L1, ~6 hours)
Real-world inspiration · What to build · Acceptance criteria (measurable) · Stretch goals ·
What it proves to an employer
### P2 · Name (L2, ~15 hours)
### P3 · Name (L3, portfolio-grade, ~30 hours)

## Feeds into
Which later course, overlap or capstone builds on this work.
```

## 8. Major learning path (`03_majors/<major>/README.md`)

Each major's README is its learning path:

1. Who the major is for and the roles it leads to (titles and what people in them actually do).
2. How AI is changing this field: sourced and dated. What is being automated, and what is growing in value.
3. The 5-year path as a table: Years 1–2 (common core, with the courses that matter most for this major), Years 3–5 (this major's courses by semester, plus the shared courses PRO301, CAR301, IND401, CAR401, RES501, RES502, THS501, THS502, LCH502).
4. Skill map by level (L0 → L5).
5. Recommended overlaps and electives.
6. The flagship industry project (link into `06_career_and_market_readiness/05_industry_projects/`).
7. Certifications worth having, with an honest value note (optional; never required).
8. The interview loop for this role (link into `06_career_and_market_readiness/04_ai_driven_interviews/`).
9. A fast track for working professionals.

## 9. Overlap specialization (`04_overlaps/<code>_<slug>/README.md`)

Why the overlap exists (the real job it maps to), the courses it is composed of, the two overlap courses (full syllabi in the same folder), a capstone, and the roles it leads to.

## 10. Keeping it current

Facts about tools, markets and laws change. When you update a fact, update its source and the `_Last reviewed_` line. Run `python tools/build_indexes.py` after adding or renaming course files: it rebuilds [`CATALOG.md`](../CATALOG.md) and [`STATUS.md`](../STATUS.md).
