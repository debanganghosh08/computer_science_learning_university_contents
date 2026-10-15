# The one-page resume

| Goal | Time | Level | Back to |
|---|---|---|---|
| A one-page resume for your level that survives software screening, a 30-second human skim and a 45-minute interview about every line | ~6 hours for v1, 1 hour per tailored version | L2 → L3 | [Portfolio hub](README.md) |

## 1. What a resume is for

A resume has one job: to get you a conversation. It is read three times, by three different readers:

1. **Software.** An applicant tracking system (ATS) parses it into fields, stores it, and lets recruiters search and filter. Some employers add knockout questions (for example, work authorisation) and some add automated ranking.
2. **A recruiter or hiring manager skimming.** They look for the target role, recent and relevant work, recognisable signals (employers, projects, open source) and results.
3. **An interviewer.** They pick lines and ask "tell me more". Every line becomes a question.

Write for the third reader and format for the first. If a line would embarrass you in an interview, it does not belong on the page.

## 2. Structure by level

Order sections by strength: the strongest evidence for the target role goes first.

| Section | Intern (L2, Year 3) | New graduate (L3, Year 4–5) | Experienced (2+ years) or career switcher |
|---|---|---|---|
| Header | Name, city, email, phone, GitHub, LinkedIn, portfolio | Same | Same |
| Summary | Skip | Optional, one line naming the target role | Two lines: role, years, domain, one result |
| Education | First | After experience if you had an internship or co-op | Last, one line |
| Experience | Internships, teaching assistant work, freelance | Internships, co-op ([IND401](../../05_shared_years_3_to_5/IND401_industry_co_op_studio/)) | First, the bulk of the page |
| Projects | 3 projects, the core of the page | Flagship project first, then 1–2 others | 1 project only if it shows the new direction |
| Open source | Merged pull requests with links | Sustained contributions | Maintainer roles |
| Skills | Grouped: languages, frameworks, tools, cloud | Same, only what you can be tested on | Same, shorter |
| Awards, writing | Hackathons, competitive programming ratings, GSoC/Outreachy/LFX | Selected writing, talks | Talks, patents, publications |

**One page.** For students and people with less than about ten years of experience, one page is the norm. It forces you to choose your best evidence.

## 3. Format rules

| Rule | Why |
|---|---|
| Single column, top to bottom | Multi-column layouts and text boxes can be read out of order by parsers |
| Standard headings: Experience, Projects, Education, Skills | Parsers and recruiters look for them |
| PDF with selectable text, exported from a text source (Markdown, LaTeX, Typst, Google Docs) | Text inside images, icons or scanned pages cannot be parsed |
| No tables for layout, no skill bars, no photo (unless the country norm requires one) | Skill bars ("Python ████░") say nothing measurable; photos invite bias and take space |
| 10–11 pt body text, 0.5–0.75 inch margins | Readable on a phone and when printed |
| Dates as "Jun 2026 – Aug 2026" | Unambiguous across countries |
| Links written out or clearly labelled (github.com/yourname) | Printed copies and parsers lose hyperlinks |
| File name: `Firstname_Lastname_Resume_Backend.pdf` | Recruiters download dozens of files named `resume.pdf` |
| Keep a plain `.txt` copy | To paste into application forms that strip formatting |

**Test your own PDF.** Open it, select all, copy, and paste into a plain text editor. If the order is scrambled, characters are missing or bullets turn into symbols, a parser will see the same mess. Fix the source, not the PDF.

## 4. Templates

Write the content in Markdown first. Content is the hard part; the typesetting takes an hour.

### 4.1 Intern (L2)

```markdown
# Asha Rao
Pune, India · asha.rao@example.com · +91 90000 00000 · github.com/asharao · linkedin.com/in/asharao

## Education
B.Tech, Computer Science, Example Institute of Technology · CGPA 8.4/10 · Aug 2024 – May 2028 (expected)
Relevant: Operating Systems, Database Internals, Distributed Systems I, Security Foundations

## Projects
**rate-limiter-go** · Go, Redis, k6 · github.com/asharao/rate-limiter-go
- Built a token-bucket rate limiter as HTTP middleware; held 2,000 requests/s with p99 added
  latency of 1.8 ms on a 2-vCPU VM (k6 load test, results in repo).
- Found and fixed a race in token refill with `go test -race`; added a regression test.

**campus-notes-search** · Python, PostgreSQL full-text search, FastAPI
- Search over 12,000 lecture notes used by ~300 students in one semester (server logs).
- Cut median query time from 420 ms to 35 ms by adding a GIN index; documented the EXPLAIN plans.

**tiny-kv** · Rust
- Log-structured key-value store with crash recovery; 40 property-based tests (proptest).

## Open source
- **Apache Example** · 2 merged pull requests: fixed a timezone bug in date parsing (#1234);
  added missing tests for config loading (#1301).

## Experience
**Teaching Assistant, Data Structures** · Example Institute · Jan 2026 – May 2026
- Ran weekly labs for 60 students; wrote 15 auto-graded exercises with hidden tests.

## Skills
Languages: Go, Python, Rust, SQL, C · Tools: Git, Docker, Linux, k6, GitHub Actions ·
Data: PostgreSQL, Redis
```

### 4.2 New graduate (L3)

```markdown
# Rahul Menon
Bengaluru, India · rahul.menon@example.com · github.com/rmenon · linkedin.com/in/rmenon · rmenon.dev

## Experience
**Software Engineering Intern (Payments)** · Example Fintech Pvt Ltd · May 2027 – Jul 2027
- Added idempotency keys to the refund API; duplicate refunds in staging replay tests fell from
  14 per 10,000 to 0. Shipped behind a feature flag to production.
- Wrote the reconciliation job's alerting runbook; used in 2 incidents during the internship.

**Co-op Engineer** · Example Logistics (IND401 co-op) · Aug 2027 – Dec 2027
- Moved route-optimisation batch jobs from cron to a queue with retries; failed nightly runs
  dropped from 6 in August to 0 in November.

## Flagship project
**ledger-lite** · Go, PostgreSQL, Kafka, OpenTelemetry · github.com/rmenon/ledger-lite · design doc in repo
- Double-entry ledger service with exactly-once posting semantics via an outbox table; 1,500
  postings/s at p95 38 ms on a 3-node local cluster (load-test report in repo).
- Chaos test: killed the consumer mid-batch 50 times; zero lost or duplicated postings.

## Open source
- **OpenTelemetry Go contrib** · 6 merged pull requests, including a fix for span-context loss
  in a gRPC interceptor (#4567).

## Education
B.Tech, Computer Science · Example University · 2024–2028 · CGPA 8.1/10

## Skills
Go, Python, SQL, TypeScript · PostgreSQL, Redis, Kafka · Docker, Kubernetes, Terraform ·
OpenTelemetry, Prometheus, Grafana · AWS (EC2, RDS, SQS)
```

### 4.3 Experienced or career switcher

```markdown
# Priya Sharma
Hyderabad, India · priya.sharma@example.com · github.com/psharma · linkedin.com/in/psharma

Backend engineer, 4 years in B2B SaaS; moving into ML platform engineering. Built and ran the
feature store serving 30 models.

## Experience
**Software Engineer II** · Example SaaS · Jul 2023 – present
- Designed the feature-store read path (Redis + PostgreSQL); p99 lookup 9 ms at 20,000 reads/s.
- Led the migration of 40 cron jobs to Airflow; on-call pages for data jobs fell 70% over two
  quarters (PagerDuty export).
- Reviewed ~25 pull requests a month; wrote the team's guide for reviewing AI-generated code.

**Software Engineer** · Example Services Ltd · Jul 2021 – Jun 2023
- Built REST APIs for a retail client's order system (Java, Spring Boot); 3 releases a month.

## Selected project (new direction)
**drift-watch** · Python, Evidently, Prometheus · github.com/psharma/drift-watch
- Data-drift monitor for tabular models; caught a schema change in a public dataset replay.

## Education
B.E., Information Technology · Example College · 2017–2021

## Skills
Python, Java, Go, SQL · PostgreSQL, Redis, Kafka, Airflow · Kubernetes, Terraform, AWS · MLflow
```

All names, employers and numbers in these templates are **illustrative**. Replace every number with one you measured.

### 4.4 Typesetting: LaTeX, Typst or a document editor

| Option | Good for | Notes |
|---|---|---|
| LaTeX on [Overleaf](https://www.overleaf.com/) (free tier) | Precise layout, version control | Popular student templates exist in Overleaf's gallery (search "resume"). Choose a single-column one and check it with the copy-paste test |
| [RenderCV](https://github.com/rendercv/rendercv) | Writing the resume as YAML and generating a PDF | Open source; keeps content and design separate |
| [Typst](https://typst.app/) | Faster compile than LaTeX, simpler syntax | Newer, smaller template ecosystem |
| Google Docs or Word | Speed, easy sharing for review | Avoid text boxes and multi-column tables |

A minimal single-column LaTeX skeleton that uses only standard packages:

```latex
\documentclass[10pt]{article}
\usepackage[margin=0.6in]{geometry}
\usepackage[T1]{fontenc}
\usepackage{lmodern}
\usepackage[hidelinks]{hyperref}
\usepackage{enumitem}
\input{glyphtounicode}   % map glyphs to Unicode so copied text is readable
\pdfgentounicode=1       % (pdfLaTeX) helps parsers extract text correctly
\pagestyle{empty}
\setlength{\parindent}{0pt}
\setlist[itemize]{leftmargin=1.2em,itemsep=1pt,topsep=2pt}
\newcommand{\heading}[1]{\vspace{6pt}{\large\bfseries #1}\par\vspace{1pt}\hrule\vspace{4pt}}
\newcommand{\entry}[2]{\textbf{#1}\hfill #2\par}

\begin{document}
{\LARGE\bfseries Asha Rao}\par
Pune, India $\cdot$ asha.rao@example.com $\cdot$ github.com/asharao $\cdot$ linkedin.com/in/asharao

\heading{Projects}
\entry{rate-limiter-go $\cdot$ Go, Redis, k6}{github.com/asharao/rate-limiter-go}
\begin{itemize}
  \item Built a token-bucket rate limiter; held 2,000 requests/s with p99 added latency of 1.8 ms.
\end{itemize}

\heading{Education}
\entry{B.Tech, Computer Science, Example Institute of Technology}{2024 -- 2028}
\end{document}
```

Keep the `.tex` (or `.md`, `.yaml`) file in a private Git repository. Tag each version you send (`v2026-10-acme-backend`) so you know exactly what an interviewer is looking at.

## 5. Applicant tracking systems: realities and myths

**How common they are.** A 2026 survey of public job pages detected an ATS at 487 of the Fortune 500 companies (97.4%); Workday was used by over 40% of them. In a broader sample of 13,000+ companies, the most common were Greenhouse (19.0%), Workday (17.5%), Lever (15.6%) and iCIMS (14.4%) ([Jobscan ATS Usage Report, 20 Aug 2026](https://www.jobscan.co/blog/fortune-500-use-applicant-tracking-systems/)). Note that Jobscan sells resume-optimisation software, so it has an interest in the topic; the method (detecting the system behind each careers page) is described in the report. In India, mid-size employers also use local HR suites, and job portals such as Naukri let recruiters search their candidate databases directly, so the structured profile fields you fill in on a portal are themselves searched.

**What an ATS does.**

- Parses your resume into fields (name, employers, dates, education, skills). Parsing errors are the most common technical failure, which is why the format rules above matter.
- Stores applications and lets recruiters **search** them by keyword, title, location and other fields.
- Applies **knockout questions** the employer configured (work authorisation, location, notice period, minimum degree).
- Depending on the product and the employer's settings, it may **rank or score** candidates, increasingly with AI features.

**What is overstated.** A widely repeated claim says that "75% of resumes are rejected by ATS before a human sees them". No published study with a stated method behind that number could be found (unconfirmed; treat it as folklore). Rejection depends on how an employer configures knockouts and ranking, not on a universal robot.

**What is real.** Rigid filters do exclude qualified people. In the Harvard Business School and Accenture *Hidden Workers* study (September 2021, more than 2,250 executives in the US, UK and Germany), 88% of employers agreed that qualified high-skills candidates were screened out because they did not match the exact criteria in the job description, rising to 94% for middle-skills candidates ([HBS project page](https://www.hbs.edu/managing-the-future-of-work/research/Pages/hidden-workers-untapped-talent.aspx); figures as reported by [HR Executive](https://hrexecutive.com/sage-gavin-3-ways-to-hire-hidden-talent-and-boost-your-bottom-line/) and [The Register](https://www.theregister.com/2021/09/08/harvard_jobs_report/)).

**What to do about it.**

1. **Mirror real terms honestly.** If the job description says "PostgreSQL" and you used PostgreSQL, write "PostgreSQL", not only "SQL databases". Use the employer's spelling of skills you actually have.
2. **Answer knockout questions accurately.** A wrong "yes" to work authorisation or notice period gets you rejected later, after more effort on both sides.
3. **Never hide keywords** (white text, tiny fonts, a pasted job description). Many systems show recruiters the parsed plain text, where hidden text is visible, and it reads as dishonest.
4. **Do not rely on the portal alone.** Referrals and direct messages to hiring managers reach a human first ([search strategy](../07_job_search_offers_negotiation/search_strategy.md)).

## 6. Bullets that show impact

### 6.1 The shape of a strong bullet

**Action + what + result + how you know.** A common form, often attributed to former Google HR head Laszlo Bock, is "Accomplished [X] as measured by [Y], by doing [Z]."

| Weak | Strong (illustrative numbers) |
|---|---|
| Worked on backend APIs | Built the order-status API (Go, gRPC) used by the mobile app; p95 latency 60 ms at launch traffic of 300 requests/s |
| Responsible for testing | Added contract tests between 4 services; caught 3 breaking changes in CI before release in one quarter |
| Used machine learning to predict churn | Trained a gradient-boosted churn model (AUC 0.81 on a time-split holdout vs 0.72 for the existing rule); deployed as a weekly batch score |
| Improved website performance | Cut Largest Contentful Paint on the product page from 4.1 s to 2.2 s (Lighthouse, mobile profile) by lazy-loading images and splitting the bundle |
| Worked on security | Wrote 12 detection rules for suspicious OAuth consent grants; 2 true positives in the first month, false-positive rate documented |
| Managed cloud infrastructure | Moved 30 services to Terraform modules; drift found in weekly plans fell from ~20 resources to 0 |
| Did data analysis | Defined the "active seller" metric with finance and product; replaced 3 conflicting dashboard definitions |

### 6.2 Where honest numbers come from

You do not need a job to have numbers. You need to **measure**.

| Kind of result | How to measure it yourself |
|---|---|
| Latency and throughput | Load tests with k6, Locust or wrk; report p50/p95/p99, machine size and request mix |
| Reliability | Chaos tests (kill processes, drop the network), number of runs, outcome |
| Correctness | Tests count and what they cover; property-based tests; mutation-testing score |
| Front-end performance | Lighthouse or WebPageTest runs, device profile stated |
| Model quality | Metric on a held-out set with a baseline; evaluation set size |
| Cost | Cloud bill before and after; cost per 1,000 requests |
| Usage | Real users, from server logs or analytics, with the period stated |
| Time saved | Before and after timings of a task, with how many times you measured |

If you have no number, describe **scope** ("used by 60 students for a semester"), **verifiable artefacts** ("merged as #4567") or **difficulty** ("crash-safe under 50 forced kills"). Never estimate a number you did not measure and present it as measured.

### 6.3 Verbs and words

Start with a specific verb: built, designed, measured, cut, migrated, automated, diagnosed, wrote, reviewed, led. Avoid "responsible for", "helped with", "worked on", and adjectives that cannot be checked ("robust", "scalable", "cutting-edge", "passionate").

## 7. Honest AI-assisted writing

AI tools are good editors and poor witnesses: they can tighten your sentences, but they do not know what you did.

**Rules.**

1. **Write the first draft yourself.** Some employers ask for exactly this; Anthropic's candidate guidance says "Please create your first draft yourself, then use Claude to refine it" ([Anthropic, updated 10 Jul 2025](https://www.anthropic.com/candidate-ai-guidance)).
2. **Every fact comes from you.** Do not accept numbers, technologies, team sizes or outcomes that an AI tool added. Check each edited bullet against your notes or repository.
3. **No inflation.** "Led" means you led people or a decision. A course project is not "production". An internship title stays the title you had.
4. **Keep your voice.** Remove phrases you would never say aloud. Interviewers notice when the person and the page do not match.
5. **Follow each employer's stated policy** on AI in applications, and answer honestly if asked how you used AI.

**A critique prompt that works better than "improve my resume":**

```text
You are a hiring manager for <role> at <type of company>. Here is a job description and my
resume. Do not rewrite anything. Instead:
1. List the 5 bullets you would ask about first, and the question you would ask.
2. List claims that sound vague or unverifiable.
3. List requirements in the job description my resume does not show evidence for.
4. Point out formatting that could confuse a parser.
```

Then decide yourself what to change. For each question in step 1, write a two-minute answer; this doubles as interview preparation.

## 8. India and global notes

**India.**

- Leave out date of birth, marital status, religion, father's name, a photo and a "Declaration: I hereby declare…" line. They are not needed to judge your work and take space.
- State CGPA with its scale ("8.1/10"). Some mass-recruitment drives set minimum percentages for Class 10, Class 12 and the degree; the criteria vary by employer and drive, so check each one. Put the marks in the application form if asked, not necessarily on the page.
- Job portals ask for current CTC, expected CTC and notice period. Fill them in carefully; recruiters filter on them. See [offers and negotiation](../07_job_search_offers_negotiation/offers_and_negotiation.md) before writing an expected CTC.

**Global.**

- In the US, UK and Canada, leave out photo, age and marital status.
- Use the employer's language and spelling (for example, "optimise" or "optimize"), and convert grades only if the employer asks.
- Remote roles abroad: state your time zone and work authorisation in the header ("Bengaluru, India (UTC+5:30) · open to remote").

## 9. Final checklist

- [ ] One page, single column, PDF passes the copy-paste test.
- [ ] Target role is obvious within five seconds.
- [ ] Strongest evidence first; every bullet starts with a verb.
- [ ] Every number was measured, with the method in a repository or your notes.
- [ ] Every technology listed is one you can be tested on today.
- [ ] Links work and point to the right repositories.
- [ ] Two working engineers reviewed it; one in your target role.
- [ ] Tailored version saved and tagged for each application.

## 10. Practice

1. **Rewrite drill.** Take the seven weak bullets in section 6.1 and rewrite each for one of your own projects with a number you measure this week.
2. **Interview from your resume.** Ask a friend to pick any three lines and question you for five minutes each. Remove or fix any line you could not defend.
3. **Parser test.** Paste your PDF text into a plain text file and into a free resume parser; compare the extracted fields with what you intended.

## Sources

All checked October 2026.

1. Jobscan. *Applicant Tracking System (ATS) Usage Report*, 6th edition (20 Aug 2026). https://www.jobscan.co/blog/fortune-500-use-applicant-tracking-systems/
2. Fuller, Raman, Sage-Gavin, Hines. *Hidden Workers: Untapped Talent* (Harvard Business School and Accenture, September 2021). https://www.hbs.edu/managing-the-future-of-work/research/Pages/hidden-workers-untapped-talent.aspx ; coverage: HR Executive https://hrexecutive.com/sage-gavin-3-ways-to-hire-hidden-talent-and-boost-your-bottom-line/ and The Register (8 Sep 2021) https://www.theregister.com/2021/09/08/harvard_jobs_report/
3. Anthropic. *Guidance on candidates' AI usage* (updated 10 Jul 2025). https://www.anthropic.com/candidate-ai-guidance
4. Tools: Overleaf https://www.overleaf.com/ ; RenderCV https://github.com/rendercv/rendercv ; Typst https://typst.app/

_Last reviewed: 2026-10_
