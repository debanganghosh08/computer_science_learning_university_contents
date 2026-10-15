# CAR301 · Labs and projects

Everything here is public evidence: a ledger of timed practice, links to merged pull requests, deployed projects, published posts. Each submission includes the links and a short note on what you did yourself and where AI helped.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Baseline and ledger | Measure where you start: one 90-minute set (AI off), GitHub audit, writing sample | Scores, a ledger template with columns for problem, family, minutes, result, error type | 2 h |
| 2 · Error taxonomy drills | Classify every failed attempt from track weeks 3–6 and design one drill per top error | Error counts by type; three targeted drills with before/after times | 3 h |
| 3 · Mock online assessment | Two practice OAs under real conditions (camera on, single screen, timer) | Scores, hidden-test failures and their causes | 2 h |
| 4 · Build from source | Build a large project from source and run its full test suite | Build log, time taken, every problem you hit and how you fixed it | 3 h |
| 5 · Trace one request | Follow one command or HTTP request through every layer with a debugger | Annotated call path with file and line links; one-page architecture map | 3 h |
| 6 · Project scorecard | Score five projects on activity, response time, maintainers, releases, rules and AI policy | Scorecard with data sources and your pick | 2 h |
| 7 · Reproduction and failing test | Reproduce a reported bug and write a failing test before any fix | Link to your issue comment with the reproduction; the test | 3 h |
| 8 · Reviewing others | Review two open PRs in your project respectfully and usefully | Links to your reviews; what the authors changed | 2 h |
| 9 · Proposal draft | Write a GSoC, LFX or Outreachy-style proposal for your project | Proposal with deliverables, timeline, buffers and prior-contribution links; feedback from one maintainer or mentor | 3 h |
| 10 · Five-minute README test | Rewrite three READMEs; time a person who has never seen them | Before/after READMEs, recorded times, what tripped the tester | 3 h |
| 11 · Mock interview pair | Interview and be interviewed with the four-part rubric | Two recordings, rubric scores, one change you made after each | 2 h per pair |
| 12 · Benchmark post | Publish a post with a reproducible benchmark (code, hardware, versions, variance) | Post link; repository with the benchmark script | 4 h |

## Projects

### P1 · Pattern library and error ledger (L1, ~6 hours)

**Real-world inspiration.** Competitive programmers and strong interviewers keep personal libraries of templates and post-mortems of failed attempts; the habit of testing against a brute-force oracle comes straight from contest practice (see [CS201](../../02_year_2_core_computer_science/semester_3/CS201_algorithms_and_complexity/README.md) Lab 2).

**What to build.** A repository of 40 problems you solved during the track, across at least 10 pattern families. Each problem has a brute force, an optimal solution, a stress test, a complexity note and a one-line "trigger" (what in the statement points to the pattern). Add a script that turns your ledger into a summary: solve time by family, error types over time.

**Acceptance criteria**
- 40 problems across at least 10 families; each optimal solution passes a stress test against its brute force on at least 1,000 random small inputs.
- Every problem has a written trigger and complexity; at least 10 have a second solution with a different trade-off.
- The summary script produces median solve time per family and error-type counts per fortnight from the ledger.
- Re-solve evidence (timestamps) at 7 and 30 days for at least 15 problems, with times falling or flat.

**Stretch goals.** A flashcard export of triggers for Anki; a small web page that quizzes you on triggers.

**What it proves to an employer.** You practise deliberately, test your own code and know your weaknesses in numbers.

### P2 · First merged contribution, documented (L2, ~15 hours)

**Real-world inspiration.** Maintainers of projects such as Kubernetes, CPython and Django publish contributor guides because most first PRs fail on process, not code. GSoC and LFX mentors look for applicants who have already landed a change.

**What to build.** Take one issue in the project you chose in Lab 6 from reproduction to merge, then write it up as post one.

**Acceptance criteria**
- The project has at least three maintainers active in the last 90 days and a release in the last six months (show the data).
- The PR is merged and changes behaviour: a bug fix or feature with tests (documentation-only or typo PRs do not count).
- The project's DCO or CLA and its AI-contribution policy are followed, and any AI help is disclosed as the project requires.
- Every review round is logged: what was asked, what you changed, how long you took to respond (target: 48 hours or less).
- After the merge, you either land a second PR or give two substantive reviews on others' PRs.
- The write-up is published with links to the issue, PR and commits.

**Stretch goals.** Become a regular reviewer for one subsystem; fix a follow-up issue you discovered while working.

**What it proves to an employer.** You can work in someone else's codebase, under strangers' review, to their standard.

### P3 · Portfolio and contribution trajectory (L3, portfolio-grade, ~30 hours)

**Real-world inspiration.** Hiring managers and recruiters look at a few repositories for seconds before deciding to read further; the projects that hold attention show a working demo, clear trade-offs and evidence of operation.

**What to build.** Your public portfolio: three flagship repositories (one from [05_industry_projects](../../06_career_and_market_readiness/05_industry_projects/), your open-source contribution story, and one L3 project from your major), a profile README, a submitted or submission-ready mentorship proposal, and post two.

**Acceptance criteria**
- Each repository passes the five-minute test with a person who has not seen it (recorded), has CI that runs tests on every push, and states trade-offs in at least two ADRs.
- One project is deployed with monitoring (uptime check and logs) and reports its monthly running cost.
- Your contribution trajectory shows at least three merged PRs in total, or one feature-sized PR of at least 200 changed lines including tests.
- The mentorship proposal has written feedback from a maintainer or past mentor, and you revised it.
- Post two contains a benchmark or experiment that a reader can rerun from a linked repository.
- The profile README links all of the above; nothing on it overstates your role.

**Stretch goals.** Get accepted into GSoC, LFX or Outreachy (this can count as the [IND401](../IND401_industry_co_op_studio/README.md) placement); give a short talk about your contribution at a meetup or maintainers' call.

**What it proves to an employer.** You ship, you operate what you ship, and other engineers have already trusted your code.

## Feeds into

- [CAR401 Career Lab II](../CAR401_career_lab_ii_interviews_system_design_and_ai/README.md): the portfolio becomes the evidence behind your resume; DSA continues as maintenance.
- [IND401 Industry Co-op Studio](../IND401_industry_co_op_studio/README.md): the open-source project can become your client organisation.
- [THS502 Thesis or Capstone II](../THS502_thesis_or_capstone_ii/README.md): the open-source release of your capstone follows the same standards.
- [LCH502 Career Launch and Founder Studio](../LCH502_career_launch_and_founder_studio/README.md): job-track applications link to this portfolio.
