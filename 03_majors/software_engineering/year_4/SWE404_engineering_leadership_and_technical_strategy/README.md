# SWE404 · Engineering Leadership and Technical Strategy

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 4 · 8 | 4 (≈ 120 hours) | L3 → L4 | [SWE304](../../year_3/SWE304_ai_assisted_software_engineering_agents/README.md); assumes [FND106](../../../../01_year_1_foundations/semester_1/FND106_technical_communication_and_professional_skills/README.md) and [IND401](../../../../05_shared_years_3_to_5/IND401_industry_co_op_studio/README.md) | [LCH502](../../../../05_shared_years_3_to_5/LCH502_career_launch_and_founder_studio/README.md); tech lead, staff and engineering-manager tracks |

## Why this course matters now

The scarce resource in a software team is no longer typing speed. It is deciding what to build, splitting it into work that people and agents can do, keeping quality high when code arrives faster than anyone can read it, and growing engineers whose first rung (simple, well-specified tasks) is the rung AI automates first. Hiring data shows the shift: on one large assessment platform, hiring for lead developers grew 22% and for entry-level developers 7% in a year, and 76% of developers said AI makes assessments easier to game (HackerRank 2025). DORA's 2025 AI Capabilities Model names leadership-owned conditions for AI to help rather than hurt, starting with "a clear and communicated AI stance". Anthropic's own engineers reported in late 2025 that they get fewer questions from junior colleagues and worry about skill atrophy. Will Larson's four staff archetypes (Tech Lead, Architect, Solver, Right Hand) describe how senior engineers lead without managing. This course teaches the leadership skills of the senior and staff engineer and the first-line manager: planning, writing strategy and RFCs, running decisions, mentoring, structured hiring, and leading AI-augmented teams, with practice on real teams of your classmates.

## Learning outcomes

By the end you can:

1. **Describe** the IC and management career paths and **place** yourself and others on a public career framework with evidence.
2. **Lead** a team as tech lead: plan, split work between people and agents, run design reviews, and protect quality.
3. **Write** RFCs and run a decision process that ends in a recorded decision, including "disagree and commit".
4. **Forecast** delivery with probabilistic methods and **communicate** uncertainty to non-engineers.
5. **Write** a technical strategy with a diagnosis, guiding policies and coherent actions, and **defend** it to a panel.
6. **Mentor** an engineer with goals, feedback and deliberate practice, including AI-off practice.
7. **Design** and **run** structured, calibrated interviews for the AI era.
8. **Lead** an AI-augmented team: policy, measurement, review capacity, cost and skill development.
9. **Handle** conflict, underperformance and burnout conversations with a documented, fair process.

## Chapters and lessons

### Chapter 1 · Paths, levels and scope (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Two ladders | Individual contributor vs engineering manager; when people switch; public frameworks (Dropbox's career framework) | Map 3 public engineering ladders to each other; note where they disagree |
| 1.2 Staff archetypes | Tech Lead, Architect, Solver, Right Hand (StaffEng) | Interview (or read StaffEng stories of) two staff engineers; classify their work |
| 1.3 Scope and impact | Task → feature → system → organisation; impact you can show | Write your own "brag document" with evidence for one semester |
| 1.4 Leadership without authority | Influence through writing, credibility, and relationships | Identify one cross-team problem in a club or co-op and propose a change |

**Check your understanding:** What changes between senior and staff that is not "more code"? Why is a brag document useful even if you never get promoted with it? Which archetype fits a person who mostly fixes the company's hardest outages?

### Chapter 2 · The tech lead (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Responsibilities | Technical direction of one team; quality bar; unblocking; how much to code | Time-log a week of leading P2; compare with your plan |
| 2.2 Splitting work for people and agents | Task sizing, ownership, which tasks go to agents (well-specified, verifiable) and which to people (ambiguous, risky, growth tasks) | Split a feature into tasks with owners (person or agent) and reasons |
| 2.3 Running rituals | Stand-ups that unblock, design reviews, retrospectives with actions | Run a retro whose actions are done by next retro |
| 2.4 Protecting quality | Review standards, test bars, saying no to shortcuts, technical debt budget | Write your team's definition of done, including agent PRs |

**Check your understanding:** Why should a tech lead avoid taking the critical-path task? Which tasks should go to a junior engineer even if an agent could do them faster? What makes a retrospective useless?

### Chapter 3 · RFCs, design reviews and decisions (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 RFC cultures | Rust RFCs, Python PEPs, Kubernetes KEPs, Oxide RFDs; Google-style design docs | Compare 3 processes: who decides, how long, what happens on disagreement |
| 3.2 Writing an RFC | Problem, constraints, options, recommendation, risks, rollout | Write an RFC for a real change in an open-source project or your co-op team |
| 3.3 Deciding | Decision owners, DACI/RACI, consent vs consensus, "disagree and commit" (Amazon leadership principles) | Run a 45-minute decision meeting on a contentious RFC; record the decision |
| 3.4 Reviewing others' designs | Asking questions, not issuing verdicts; separating blocking from preference | Review two RFCs; mark every comment as blocking or not |

**Check your understanding:** Why should every RFC name its decision owner? When is consensus the wrong goal? What makes "disagree and commit" healthy instead of coercive?

### Chapter 4 · Estimation and planning (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Forecasting from data | Throughput-based Monte Carlo forecasts; reference classes; ranges with confidence | Forecast your team's P2 with Monte Carlo; publish the 50% and 85% dates |
| 4.2 Planning a quarter | Goals, milestones, dependencies, critical path, buffers; Brooks's law | Quarter plan for a 6-person team with 2 external dependencies |
| 4.3 Communicating uncertainty | Ranges, confidence levels, early warnings, re-forecasting | Write the email that says a launch will slip, with options |
| 4.4 Plans with agents | What agents change (implementation throughput) and what they do not (review, integration, decisions) | Re-plan with agent-assisted throughput; find the new bottleneck |

**Check your understanding:** Why is "two weeks" without a confidence level not an estimate? Why does adding people late make projects later, and does adding agents behave the same way? Which bottleneck appears when implementation becomes cheap?

### Chapter 5 · Technical strategy (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 What strategy is | Rumelt's kernel: diagnosis, guiding policy, coherent actions; strategy vs vision vs plan | Rewrite a "strategy" that is really a wish list |
| 5.2 Writing strategy from evidence | Larson's approach: write design docs, then synthesise a strategy from them | Synthesise a strategy from 5 ADRs and design docs you have written |
| 5.3 Technology choices | Technology radars (Thoughtworks), build vs buy vs open source, standardisation vs autonomy | Run a technology-radar session for your cohort's projects |
| 5.4 Debt and platform strategy | Paying down debt deliberately; when to build a platform team | Debt strategy for the P3 system with costs and a timeline |

**Check your understanding:** Why is a good diagnosis the hardest part of strategy? What makes a guiding policy different from a goal? When should a team standardise on one language or framework?

### Chapter 6 · Mentoring and growing engineers (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Mentoring, coaching, sponsoring | Different help for different needs; sponsorship as using your credibility for someone | Write a growth plan with a junior (a first- or second-year student) |
| 6.2 Feedback | Situation–behaviour–impact; timely, specific, kind; receiving feedback | Give and receive 3 pieces of feedback; log the outcomes |
| 6.3 Growing juniors with AI around | Learning penalties under heavy AI reliance (Shen and Tamkin, cited in the AI Index 2026); fewer mentoring questions (Anthropic, Dec 2025); AI-off practice, review as teaching, pairing | Design a 12-week onboarding plan mixing AI-off drills and agent work |
| 6.4 Psychological safety | Edmondson's research; Google's team-effectiveness findings | Run a team-health survey; act on one result |

**Check your understanding:** Why might a junior who uses agents heavily ship more and learn less? What is the difference between mentoring and sponsorship? What behaviour from a leader most reduces psychological safety?

### Chapter 7 · Hiring (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 What predicts performance | Structured interviews and work samples outperform unstructured interviews (Sackett et al., 2022 meta-analysis) | Turn an unstructured interview plan into a structured one with rubrics |
| 7.2 Rubrics and calibration | Anchored scoring, independent scoring before discussion, bar-raiser roles | Score 4 recorded mock interviews; calibrate with peers |
| 7.3 Interviews in the AI era | AI-assisted rounds (Canva) vs AI-free rounds (Anthropic guidance); assessment integrity; testing verification skill | Design one AI-assisted and one AI-free round for an SDE-2 role |
| 7.4 Fairness and the candidate experience | Bias in interviews; accommodations; clear communication and timelines | Audit a hiring loop for bias risks and fix two |

**Check your understanding:** Why do unstructured interviews feel accurate but predict poorly? What should an AI-assisted interview measure that an AI-free one cannot? How do you stop interviewers anchoring on each other?

### Chapter 8 · Leading AI-augmented teams (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Setting the stance | DORA's seven AI capabilities: clear and communicated AI stance, healthy data ecosystems, AI-accessible internal data, strong version control practices, working in small batches, user-centric focus, quality internal platforms | Assess a team against the seven; pick two to improve |
| 8.2 Review capacity as the bottleneck | Review load, routing, PR size limits; DORA's throughput-vs-stability finding | Model review hours per week as agent output doubles |
| 8.3 Cost and tool governance | Seats, tokens, usage budgets, approved tools and data rules | A tool budget and approval policy for a 30-person organisation |
| 8.4 Roles and skills | The "agent boss" idea (Microsoft Work Trend Index 2025); what juniors, seniors and managers do differently; measuring honestly (SWE304) | Rewrite role expectations for SDE-1 and SDE-2 in an agent-heavy team |

**Check your understanding:** Why does DORA list "small batches" as an AI capability? What happens to a team whose agent output grows faster than its review capacity? How would you tell your manager that AI tools are not paying off yet?

### Chapter 9 · Management fundamentals (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 One-on-ones | Agenda owned by the report; career, feedback, blockers | Run 4 weekly 1:1s with a peer; keep notes |
| 9.2 Performance | Expectations, evidence, regular feedback, improvement plans done fairly | Role-play an underperformance conversation with a written plan |
| 9.3 Conflict | Interests vs positions; mediating technical disputes | Mediate a role-played disagreement between two engineers |
| 9.4 Sustainable pace | On-call load, burnout signals, saying no to scope | Audit a team's on-call load; propose changes |

**Check your understanding:** Why should 1:1s not be status meetings? What makes a performance process fair to the person being managed? How do you tell overload from underperformance?

### Chapter 10 · Organisation design (week 10)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Conway's law at org scale | Team boundaries shape architecture (link to SWE301) | Map a public open-source foundation's teams to its architecture |
| 10.2 Team types | Stream-aligned, platform, enabling and complicated-subsystem teams; cognitive load (Team Topologies) | Redesign a 40-person organisation around cognitive load |
| 10.3 Platform and inner source | Internal platforms as products; inner-source contribution models | Write a platform team charter with users and metrics |
| 10.4 Changing an organisation | Reorganisation risks, communication, transition plans | Plan a team split with a 90-day transition |

**Check your understanding:** Why do reorganisations often cause architecture changes nobody planned? What is a platform team's product, and who are its customers? How does cognitive load limit what a team can own?

### Chapter 11 · Influence and communication (week 11)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Writing for executives | One-pagers, narrative memos (Amazon's six-page memos, 2017 shareholder letter), the answer first | Write a one-page decision memo for a migration investment |
| 11.2 Presenting trade-offs | Options with costs, risks and a recommendation | 5-minute presentation to a "VP" panel that interrupts |
| 11.3 Managing up and across | Aligning with product and other teams; escalation without blame | Write an escalation note for a blocked dependency |
| 11.4 Saying no | Protecting focus; offering alternatives | Decline three requests in writing while keeping the relationship |

**Check your understanding:** Why should the recommendation come first in an executive memo? What makes an escalation feel like an attack, and how do you avoid it? What does a good "no" include?

### Chapter 12 · Leadership portfolio (weeks 12–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 12.1 Strategy defence | Present and defend P3's strategy | Panel with product, engineering and finance roles |
| 12.2 Reflection | What worked as a tech lead in P2; what you would change | Written reflection with evidence and peer feedback |
| 12.3 Mentoring report | Evidence of a mentee's growth against agreed goals | Report co-signed by your mentee, with their written view |
| 12.4 Your next 12 months | A personal development plan toward tech lead, staff or manager | Plan with three skills, the practice for each, and how you will get feedback |

**Check your understanding:** Which of your decisions this semester would you reverse, and why? What evidence shows your mentee grew? Which leadership skill do you most need to practise next, and how will you?

## Weekly rhythm

| Week | Chapter | Lab or workshop | Deliverable |
|---|---|---|---|
| 1 | 1 | Ladders and archetypes | Brag document |
| 2 | 2 | P2 team formation; tech-lead rotation starts | Definition of done |
| 3 | 3 | RFC writing and decision meeting | **P1 due** (RFC) |
| 4 | 4 | Monte Carlo forecasting | Forecast |
| 5 | 5 | Strategy kernel workshop | — |
| 6 | 6 | Mentoring kickoff with a junior | Growth plan |
| 7 | 7 | Structured interview design and calibration | Mid-term (AI off): written leadership scenarios |
| 8 | 8 | AI-team assessment | — |
| 9 | 9 | 1:1 and performance role-plays | — |
| 10 | 10 | Organisation design | **P2 due** |
| 11 | 11 | Executive memo and presentation | — |
| 12 | 12 | P3 strategy writing | — |
| 13 | 12 | P3 review rounds | — |
| 14 | 12 | Strategy panel | **P3 due** |
| 15 | Review | Mentoring report and reflection | Final oral exam |

## Working with AI in this course

- **Use AI for:** critiquing drafts of RFCs, memos and strategies ("what would a sceptical CFO ask?"); generating interview question variants; summarising long discussion threads into decision logs (then checking them with participants); simulating stakeholder role-plays for practice.
- **Do without AI (drills):** live decision meetings, 1:1s, feedback conversations, interview calibration, the mid-term written scenarios and the oral final. Leadership happens between people in real time.
- **Verify AI output by:** checking every fact in a strategy against your own data and sources; asking the people summarised whether the summary is accurate; testing interview questions on a peer before use; comparing an AI's forecast with your Monte Carlo from real throughput data.
- **Where AI still fails here (show it):** you log cases where an assistant (a) produced a strategy with no diagnosis (a list of goals), (b) misrepresented a disagreement in a meeting summary, (c) proposed interview questions that leak the answer or test trivia, or (d) gave confident delivery dates with no data. Use the log in your reflection.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Workshops and role-plays | 15% |
| P1 (RFC and decision) | 10% |
| P2 (tech-lead rotation, peer-assessed) | 20% |
| P3 (strategy and leadership portfolio) | 25% |
| Mentoring report (with mentee feedback) | 10% |
| Mid-term (AI off) + oral final | 20% |

**Mastery gate.** You pass when you can: (1) write a technical strategy for a real or realistic organisation with a diagnosis, guiding policies and actions that a panel of three accepts after questioning; (2) run a decision meeting on a contested RFC that ends with a recorded decision, owner and dissent noted, as rated by observers; (3) show evidence that a mentee met at least two agreed growth goals over the semester; (4) design and calibrate a structured interview loop for one role, with rubrics that two independent scorers apply consistently.

## Industry reality

Where this is used (public sources): Rust, Python and Kubernetes run open RFC/PEP/KEP processes; Oxide publishes its RFDs; Google's design-doc practice is described publicly by its engineers; Amazon's leadership principles include "Have Backbone; Disagree and Commit", and its 2017 shareholder letter describes six-page narrative memos. StaffEng documents staff archetypes from interviews. Canva and Anthropic have published opposite policies on AI in interviews, which every hiring manager now has to decide on.

**Interview questions from this course** (behavioural and leadership rounds)

1. *Tell me about a technical decision you drove across teams.* Strong answer: the problem and stakes, options considered, how disagreement was handled, the written artefact (RFC or design doc), the decision and its outcome with evidence, what you would do differently.
2. *How would you introduce coding agents to a team of 12 that has not used them?* Strong answer: stance and policy first, pilot with measurement, review and security gates, training including AI-off practice, protect juniors' learning, measure DORA metrics and rework, adjust.
3. *Your project will miss its deadline by a month. What do you do?* Strong answer: tell people early with a re-forecast and options (cut scope, add time, change approach), surface the cause, protect quality, learn for future estimates.
4. *How do you grow a junior engineer when agents do the easy tasks?* Strong answer: deliberate growth tasks, AI-off practice on fundamentals, review as teaching, pairing, ownership of something small but real, feedback cadence, sponsorship.
5. *Two senior engineers disagree strongly on a design. How do you resolve it?* Strong answer: make the decision owner and criteria explicit, separate facts from preferences, prototype the riskiest disagreement, decide with a written record, disagree and commit, revisit on evidence.

## Resources (free first)

- **Staff and leadership:** StaffEng guides and stories — https://staffeng.com/ ; Will Larson, "Writing an engineering strategy" — https://lethain.com/eng-strategies/ ; Lara Hogan's management writing — https://larahogan.me/
- **RFC and design processes:** Rust RFCs — https://github.com/rust-lang/rfcs ; PEP 1 — https://peps.python.org/pep-0001/ ; Kubernetes enhancements (KEPs) — https://github.com/kubernetes/enhancements ; Oxide RFD 1 — https://rfd.shared.oxide.computer/rfd/0001 ; "Design Docs at Google" — https://www.industrialempathy.com/posts/design-docs-at-google/
- **Career frameworks:** Dropbox Engineering Career Framework — https://dropbox.github.io/dbx-career-framework/
- **Teams and organisations:** Team Topologies key concepts — https://teamtopologies.com/key-concepts ; Google re:Work, team effectiveness — https://rework.withgoogle.com/ ; Thoughtworks Technology Radar — https://www.thoughtworks.com/radar ; DORA research — https://dora.dev/
- **Hiring:** Canva on AI-assisted interviews — https://www.canva.dev/blog/engineering/yes-you-can-use-ai-in-our-interviews/ ; Anthropic candidate AI guidance — https://www.anthropic.com/candidate-ai-guidance
- **Paid, optional:** Fournier, *The Manager's Path*; Larson, *Staff Engineer* and *An Elegant Puzzle*; Reilly, *The Staff Engineer's Path*; Rumelt, *Good Strategy Bad Strategy*; Skelton and Pais, *Team Topologies*; Brooks, *The Mythical Man-Month*.

## Sources

- HackerRank, 2025 Developer Skills Report — https://www.hackerrank.com/reports/developer-skills-report-2025 (checked 2026-10)
- Google Cloud, "Introducing DORA's inaugural AI Capabilities Model" (24 Sep 2025) — https://cloud.google.com/blog/products/ai-machine-learning/introducing-doras-inaugural-ai-capabilities-model (checked 2026-10)
- Anthropic, "How AI is transforming work at Anthropic" (2 Dec 2025) — https://www.anthropic.com/research/how-ai-is-transforming-work-at-anthropic (checked 2026-10)
- StaffEng, "Staff archetypes" — https://staffeng.com/guides/staff-archetypes/ (checked 2026-10)
- Sackett, Zhang, Berry and Lievens, "Revisiting meta-analytic estimates of validity in personnel selection", *Journal of Applied Psychology* 107(11), 2022 — https://doi.org/10.1037/apl0000994 (checked 2026-10)
- Edmondson, "Psychological Safety and Learning Behavior in Work Teams", *Administrative Science Quarterly* 44(2), 1999 — https://doi.org/10.2307/2666999 (checked 2026-10)
- Amazon Leadership Principles — https://www.amazon.jobs/content/en/our-workplace/leadership-principles ; 2017 Letter to Shareholders — https://www.aboutamazon.com/news/company-news/2017-letter-to-shareholders (checked 2026-10)
- Microsoft, 2025 Work Trend Index (23 Apr 2025) — https://www.microsoft.com/en-us/worklab/work-trend-index/2025-the-year-the-frontier-firm-is-born (checked 2026-10)
- Stanford HAI, AI Index 2026 (learning study by Shen and Tamkin) — https://hai.stanford.edu/assets/files/ai_index_report_2026.pdf (checked 2026-10)

_Last reviewed: 2026-10_
