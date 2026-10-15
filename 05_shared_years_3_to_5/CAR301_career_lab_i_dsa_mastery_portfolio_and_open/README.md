# CAR301 · Career Lab I: DSA Mastery, Portfolio and Open Source

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 3 · 6 | 4 (≈ 120 hours) | L2 → L3 | [CS201](../../02_year_2_core_computer_science/semester_3/CS201_algorithms_and_complexity/README.md) | [CAR401](../CAR401_career_lab_ii_interviews_system_design_and_ai/README.md), [IND401](../IND401_industry_co_op_studio/README.md) |

This course is a structured semester that runs three things in parallel: the 16-week DSA track in [`06_career_and_market_readiness/02_dsa_for_hiring/`](../../06_career_and_market_readiness/02_dsa_for_hiring/), a first meaningful open-source contribution, and a public portfolio with writing. The DSA content lives in the track; this page sets the schedule, the practice method, the evidence you must produce and the gate.

## Why this course matters now

Most technical hiring still starts with timed algorithm problems on platforms such as HackerRank and CodeSignal, and the first screen is often a resume link to GitHub. At the same time, AI assistants solve many standard interview problems and generate whole repositories, so a portfolio of tutorial clones proves nothing and a solved problem set proves little unless you solved it under exam conditions. What still separates candidates is evidence that cannot be faked cheaply: timed problem solving with AI off, merged work in someone else's codebase reviewed by strangers, and writing that shows how you think. GitHub's Octoverse 2025 counted 21.9 million developers in India, second in the world, and March 2025 was GitHub's largest month ever for first-time open-source contributors (255,000); the bar for standing out keeps rising.

## Learning outcomes

By the end you can:

1. **Solve** unseen medium and hard problems in 35–45 minutes each with AI off, stating constraints, complexity and tests aloud.
2. **Maintain** an error log and a spaced-repetition schedule, and **show** with data which problem families you have mastered.
3. **Build, run and trace** an unfamiliar codebase of 50,000+ lines within one working day.
4. **Evaluate** open-source projects with health signals and **choose** one where a contribution is likely to be merged.
5. **Land** a merged pull request that changes behaviour (bug fix or feature with tests) and **respond** to review professionally.
6. **Write** a mentorship-programme proposal (GSoC, LFX or Outreachy) that a maintainer would rank.
7. **Engineer** a three-project portfolio whose READMEs let a reviewer run each project in five minutes.
8. **Publish** two technical posts with runnable code and verified claims.

## Chapters and lessons

### Chapter 1 · The hiring funnel and your baseline (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 How hiring works | Screen → online assessment → technical rounds → design → behavioural; what each round measures; role differences (see the [market map](../../06_career_and_market_readiness/01_market_map/README.md)) | Write the loop for your two target roles |
| 1.2 Baseline diagnostic | One 90-minute timed set (AI off), a GitHub audit, a writing sample | Record scores; they are your week-1 numbers |
| 1.3 Deliberate practice | Work at the edge of ability, fast feedback, specific goals; why re-reading solutions is not practice | Set measurable term targets |
| 1.4 The evidence ledger | One spreadsheet: problems, time, pattern, error type, PRs, posts | Create the ledger you will keep all term |

**Check your understanding:** Which round of your target loop are you weakest in, and what evidence says so? Why does watching a solution video feel like learning but rarely transfer? What would an employer accept as proof that you can work in a codebase you did not write?

### Chapter 2 · DSA track I: core patterns under the clock (weeks 1–5)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Error taxonomy | Misread, wrong pattern, off-by-one, wrong complexity, missed edge case, slow coding | Classify every failed attempt in the ledger |
| 2.2 Arrays, hashing, two pointers, sliding window, prefix sums | Trigger words that signal each pattern; invariants behind them | Track weeks' problem sets; 3 timed problems weekly |
| 2.3 Binary search on the answer, stacks, intervals | Monotonic predicates; monotonic stacks; sort-and-sweep | Rewrite two accepted solutions with a cleaner invariant |
| 2.4 Trees and heaps | Traversals, BST properties, top-k with heaps, two-heap median | Solve one problem three ways and compare |
| 2.5 Spaced repetition | Re-solve at 1, 7 and 30 days; "trigger → pattern" flashcards in Anki | 40 cards by week 5 |

**Check your understanding:** What in a problem statement tells you a sliding window will work, and what breaks it? Why must you re-solve rather than re-read? Your ledger shows mostly off-by-one errors: what drill fixes that?

### Chapter 3 · DSA track II: graphs, dynamic programming, advanced structures (weeks 6–10)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Graph modelling fast | Grid, state-space and implicit graphs; BFS, Dijkstra, topological sort, union-find chosen in under two minutes | 10 modelling-only drills: name the graph, not the code |
| 3.2 Interview DP | State, transition, base case, order; top-down first, then tabulate; reconstructing the answer | Write recurrences before code for 10 problems |
| 3.3 Structures that appear | Tries, Fenwick and segment trees, LRU (hash map + list), heaps with lazy deletion | Implement each once from memory |
| 3.4 Online assessment conditions | Hidden tests, partial scoring, proctoring, IDE limits | Two full mock OAs on HackerRank or CodeSignal practice sets |

**Check your understanding:** How do you know your DP state is complete? When is union-find better than BFS for connectivity? Your solution passes visible tests and fails hidden ones: list your first three checks.

### Chapter 4 · DSA track III: speed, communication, contests (weeks 11–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Thinking aloud | Clarify, examples, brute force, optimise, code, test, analyse | Record and transcribe one solve; cut silent gaps |
| 4.2 Mock interviews | Peer mocks with a four-part rubric (problem solving, code, verification, communication) | Two mocks given and two received per fortnight |
| 4.3 Contests as speed training | Codeforces Div. 3/Div. 2, LeetCode weekly, CodeChef Starters, AtCoder Beginner Contest | One rated contest per week from week 11 |
| 4.4 AI-era formats | AI-allowed rounds, AI-proctored tests, explaining and verifying generated code (see [04_ai_driven_interviews](../../06_career_and_market_readiness/04_ai_driven_interviews/)) | One AI-allowed mock: you must find the model's bug |

**Check your understanding:** What does an interviewer learn from your brute force? In an AI-allowed round, what must you still do yourself? How do contest skills and interview skills differ?

### Chapter 5 · Reading code you did not write (weeks 2–3)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Build and run first | README, devcontainer, Makefile, test suite green before reading | Build a large project (e.g. CPython, Redis or a framework you use) from source |
| 5.2 The top-down map | Entry points, module boundaries, `ARCHITECTURE.md` documents, dependency graphs | Draw a one-page map of the project |
| 5.3 Trace one request | Debugger, logging, breakpoints on one end-to-end path | Trace one CLI command or HTTP request through every layer |
| 5.4 History as documentation | `git log -S`, `git blame`, linked issues and PR discussions | Explain why one odd-looking line exists, with links |
| 5.5 Search and AI agents | GitHub code search, Sourcegraph, language servers; asking an agent for a map, then verifying it by stepping through | Grade an AI-produced architecture summary line by line |

**Check your understanding:** Why build before reading? What does `git log -S` find that `grep` cannot? What did the AI map get wrong, and how did you find out?

### Chapter 6 · Choosing an open-source project (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Fit | Your major, your language, a tool you already use; aim where your future employer's stack lives | Shortlist five projects |
| 6.2 Health signals | Commits in the last 90 days, time to first response on issues and PRs, active maintainers, release cadence; CHAOSS metrics; OpenSSF Scorecard | Score the five on one sheet |
| 6.3 Rules of the house | CONTRIBUTING, code of conduct, DCO vs CLA, AI-contribution policies (Gentoo bans them; NetBSD and QEMU restrict them; curl has been flooded with AI-generated vulnerability reports) | Summarise each shortlisted project's rules |
| 6.4 Where to look | `good first issue` and `help wanted` labels, goodfirstissue.dev, Up For Grabs, CodeTriage; digital public goods such as DIGIT, OpenMRS and Bahmni; FOSS United | Pick one project and three candidate issues |

**Check your understanding:** Why might a famous project be a worse first choice than a mid-sized one? What does a 30-day median time to first response tell you? Why do some projects refuse AI-generated contributions, and what follows for you?

### Chapter 7 · Your first contribution, end to end (weeks 5–8)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Reproduce first | Minimal reproduction and a failing test before any fix | Post a reproduction on the issue |
| 7.2 Talk before code | Propose an approach on the issue; ask to be assigned; respect existing work | Comment with a plan; wait for a maintainer's response |
| 7.3 The pull request | One concern, small diff, tests, docs, changelog, `git commit -s` for DCO, green CI | Open the PR |
| 7.4 Review as collaboration | Reply within 48 hours; fixups and rebases; disagree with evidence, not tone | Log every review round and what you changed |
| 7.5 After the merge | Follow-up issues, triage, reviewing others' PRs: the path toward maintainer | Review two PRs by other contributors |

**Check your understanding:** Why does a failing test make a maintainer trust your fix? What do you do when a maintainer goes silent for three weeks? How does reviewing others' PRs help your own?

### Chapter 8 · Mentorship programmes and proposals (weeks 8–9)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Google Summer of Code | 18+, a student or an open-source beginner; up to three proposals, one accepted; projects of ~90, ~175 or ~350 hours; 2026 applications ran 16–31 March | Read three accepted proposals from your target organisation |
| 8.2 LFX Mentorship | 18+, not a previous Linux Foundation mentee; CNCF, kernel and OpenSSF projects | List open LFX projects in your field |
| 8.3 Outreachy | For people facing under-representation, systemic bias or discrimination in tech; 30 hours a week, USD 7,000, cohorts May–August and December–March | Check eligibility and the next cohort's dates |
| 8.4 Indian programmes | GirlScript Summer of Code; FOSS United events and grants | Pick the programme that fits your calendar |
| 8.5 Writing the proposal | Problem, deliverables, timeline with buffers, prior contributions, communication plan | Draft a proposal for your project |

**Check your understanding:** Why do proposals from people with merged PRs win? What makes a timeline believable to a maintainer? Which programme fits a working professional, and why?

### Chapter 9 · Portfolio engineering (weeks 9–11)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 What a portfolio must prove | You can build, operate and judge; it matches your target roles | Write one sentence per project saying what it proves |
| 9.2 Three flagship projects | One from [05_industry_projects](../../06_career_and_market_readiness/05_industry_projects/), your open-source story, one L3 project from your major | Pick and justify the three |
| 9.3 The README standard | Problem, demo, architecture diagram, run in five minutes, tests and CI, benchmarks, trade-offs (ADRs), what next | Rewrite three READMEs; time a friend running each |
| 9.4 Deploy and observe | Live demo, logs, uptime, cost per month | Deploy one project with monitoring |
| 9.5 Profile and honesty | Profile README, pinned repos; no inflated contribution graphs; credit co-authors and AI help | Publish the profile |

**Check your understanding:** What does a reviewer learn in the first 30 seconds on your repo? Why is a deployed, monitored small project worth more than a large unfinished one? How do you show your part in a team project?

### Chapter 10 · Writing in public (weeks 11–13)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Post types | Bug hunt, benchmark, concept explainer, project postmortem, paper summary | Outline three ideas from your own work |
| 10.2 Structure | Claim first, evidence, runnable code, diagrams, limitations; Diátaxis for documentation | Write a post about your open-source contribution |
| 10.3 Publishing | Own domain on GitHub Pages with Hugo; cross-post to DEV or Hashnode with a canonical link; Show HN rules | Publish post one |
| 10.4 Honesty and AI | Every command run, every number measured; disclose AI help; never publish unverified generated text | Publish post two with a reproducible benchmark |

**Check your understanding:** Why put the conclusion first? What makes a benchmark post trustworthy? What is wrong with a post an AI wrote that you have not run?

### Chapter 11 · Professional presence and the first network (week 14)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 The weak-ties effect | A LinkedIn experiment with 20 million people (Rajkumar et al., *Science*, 2022) found moderately weak ties most useful for job mobility | List 20 moderately weak ties in your field |
| 11.2 Community | Meetups, conference talks (IndiaFOSS, PyCon India), maintainers' calls | Attend one event or call; write notes |
| 11.3 Messages that get replies | Specific, short, a small ask, evidence of your work | Send five messages; log replies |

**Check your understanding:** Why are weak ties more useful than close friends for jobs? What makes a cold message easy to answer? What will you bring to a maintainer's call?

## Weekly rhythm

Start the DSA track two weeks before term so that track weeks 3–16 run in term weeks 1–14. If you cannot, run the last two track weeks in review week and the break before CAR401.

| Week | DSA track week | Other chapter | Deliverable |
|---|---|---|---|
| 1 | 3 | 1 | Baseline, ledger |
| 2 | 4 | 5 | Project built from source |
| 3 | 5 | 5 | Codebase map; **P1 due** |
| 4 | 6 | 6 | Project scorecard |
| 5 | 7 | 7 | Reproduction posted |
| 6 | 8 | 7 | PR opened |
| 7 | 9 | 7 | Mid-term timed set (AI off) |
| 8 | 10 | 7–8 | PR review rounds logged |
| 9 | 11 | 8–9 | Proposal draft |
| 10 | 12 | 9 | **P2 due** (merged PR + write-up) |
| 11 | 13 | 9–10 | Portfolio READMEs |
| 12 | 14 | 10 | Post one |
| 13 | 15 | 10 | Post two |
| 14 | 16 | 11 | **P3 due** |
| 15 | Review | — | Final AI-off exam, mock interview, portfolio review |

## Working with AI in this course

- **Use AI for:** explaining an editorial solution *after* your own timed attempt; generating stress tests and edge cases; a first map of a large codebase that you then verify; reviewing your blog drafts for clarity; checking your proposal for gaps.
- **Do without AI (drills):** every timed set, contest and mock; the first attempt at every problem; your PR's code if the project forbids AI contributions; your error-log analysis.
- **Verify AI output by:** running stress tests against a brute force; stepping through code paths the model described; reading the project's AI policy before using any generated code; executing every command in a post on a clean machine.
- **Where AI still fails here:** in unfamiliar codebases, assistants often call functions or configuration options that do not exist and "fix" symptoms instead of causes; maintainers notice. curl's maintainer has described the cost of AI-generated vulnerability reports that looked plausible and were wrong. Keep a log of every AI suggestion that failed in your project and why.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| DSA: weekly timed sets and contests (ledger) | 20% |
| DSA: final exam (AI off) and one recorded mock | 15% |
| Open-source contribution (P2) and reviews given | 25% |
| Portfolio (P3) | 20% |
| Two published posts | 10% |
| Labs | 10% |

**Mastery gate.** You pass when you can show: (1) with AI off, 2 of 3 unseen medium-to-hard problems solved in 90 minutes, each with stated complexity and passing tests, explained aloud to an examiner; (2) at least one merged pull request that changes behaviour (bug fix or feature with tests) in a project with at least three active maintainers and a release in the last six months, plus two reviews you gave on others' PRs; (3) three portfolio repositories that a stranger runs from the README in five minutes or less, one of them deployed with monitoring; (4) two published posts whose code runs as written.

## Industry reality

Online assessments with two or three timed problems are a common first round for SDE roles in India and globally (see [02_dsa_for_hiring](../../06_career_and_market_readiness/02_dsa_for_hiring/)). Open-source maintainers and companies with open codebases (for example GitLab, Grafana Labs, Mozilla and many CNCF projects) can see your work before any interview. Mentorship programmes such as GSoC, LFX and Outreachy pay contributors and are a recognised path to first jobs.

**Interview questions from this course**

1. *Tell me about a contribution you made to a codebase you did not write.* Strong answer: the problem, how you reproduced it, how you navigated the code, what reviewers asked for, what you changed, and a link.
2. *You join a team with a 500,000-line codebase. What do you do in week one?* Strong answer: build and test locally, trace one request end to end, read recent PRs and incident notes, draw a map, ship a small fix, ask targeted questions.
3. *Return the k most frequent items in the last hour of a stream.* Strong answer: sliding window with timestamps, hash map counts plus a heap or bucket structure, eviction, complexity, memory bounds, approximate options (count-min sketch) if scale demands.
4. *A maintainer rejected your PR. What happened?* Strong answer: honest account, what the maintainer's constraint was, what you learned, what you did next (revised, closed, or contributed elsewhere).
5. *Walk me through the hardest trade-off in your portfolio project.* Strong answer: names alternatives, the measurement that decided it, the cost accepted, and what would change the decision.

## Resources (free first)

- **DSA:** the track — [02_dsa_for_hiring](../../06_career_and_market_readiness/02_dsa_for_hiring/) ; CSES — https://cses.fi/problemset/ ; USACO Guide — https://usaco.guide/ ; Tech Interview Handbook — https://www.techinterviewhandbook.org/coding-interview-prep/ ; NeetCode roadmap — https://neetcode.io/roadmap ; LeetCode — https://leetcode.com/ ; Codeforces — https://codeforces.com/ ; CodeChef — https://www.codechef.com/ ; AtCoder — https://atcoder.jp/ ; Anki — https://apps.ankiweb.net/
- **Open source:** Open Source Guides — https://opensource.guide/how-to-contribute/ ; goodfirstissue.dev — https://goodfirstissue.dev/ ; Up For Grabs — https://up-for-grabs.net/ ; CodeTriage — https://www.codetriage.com/ ; OpenSSF Scorecard — https://scorecard.dev/ ; CHAOSS metrics — https://chaoss.community/kb-metrics-and-metrics-models/ ; DCO — https://developercertificate.org/ ; Digital Public Goods registry — https://digitalpublicgoods.net/registry ; FOSS United — https://fossunited.org/
- **Programmes:** GSoC — https://summerofcode.withgoogle.com/ ; LFX Mentorship — https://mentorship.lfx.linuxfoundation.org/ ; Outreachy — https://www.outreachy.org/ ; GirlScript Summer of Code — https://gssoc.girlscript.tech/ ; Hacktoberfest — https://hacktoberfest.com/
- **Reading code:** Pro Git — https://git-scm.com/book/en/v2 ; ARCHITECTURE.md (matklad) — https://matklad.github.io/2021/02/06/ARCHITECTURE.md.html ; GitHub code search syntax — https://docs.github.com/en/search-github/github-code-search/understanding-github-code-search-syntax ; Sourcegraph — https://sourcegraph.com/search
- **Writing:** Google Technical Writing courses — https://developers.google.com/tech-writing ; Diátaxis — https://diataxis.fr/ ; GitHub Pages — https://pages.github.com/ ; Hugo — https://gohugo.io/ ; Show HN guidelines — https://news.ycombinator.com/showhn.html ; Julia Evans's blog as a model of clear technical writing — https://jvns.ca/
- **Paid, optional:** none required.

## Sources

- GitHub Octoverse 2025 (28 Oct 2025, updated 28 Feb 2026): India 21.9 million developers, #2 globally; 255,000 first-time contributors in March 2025 — https://github.blog/news-insights/octoverse/octoverse-a-new-developer-joins-github-every-second-as-ai-leads-typescript-to-1/ (checked 2026-10)
- GSoC FAQ (eligibility, project sizes, proposals) and timeline (2026 contributor applications 16–31 March) — https://developers.google.com/open-source/gsoc/faq , https://developers.google.com/open-source/gsoc/timeline (checked 2026-10)
- LFX Mentorship eligibility — https://docs.linuxfoundation.org/lfx/mentorship/mentee-guide/am-i-eligible (checked 2026-10)
- Outreachy eligibility, 30 hours a week, USD 7,000, two cohorts — https://www.outreachy.org/apply/eligibility/ , https://www.outreachy.org/docs/internship/ (checked 2026-10)
- Gentoo Council AI policy (14 Apr 2024) — https://projects.gentoo.org/council/meeting-logs/20240414-summary.txt ; NetBSD commit guidelines — https://www.netbsd.org/developers/commit-guidelines.html ; QEMU code provenance — https://www.qemu.org/docs/master/devel/code-provenance.html ; Daniel Stenberg, "Death by a thousand slops" (14 Jul 2025) — https://daniel.haxx.se/blog/2025/07/14/death-by-a-thousand-slops/ (checked 2026-10)
- Rajkumar et al., "A causal test of the strength of weak ties", *Science* 377 (2022) — https://www.science.org/doi/10.1126/science.abl4476 (checked 2026-10)

_Last reviewed: 2026-10_
