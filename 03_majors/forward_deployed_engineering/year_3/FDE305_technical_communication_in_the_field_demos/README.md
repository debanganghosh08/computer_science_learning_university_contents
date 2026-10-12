# FDE305 · Technical Communication in the Field: Demos, Design Docs and Workshops

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 3 · 6 | 4 (≈ 120 hours) | L1 → L3 | [CS205](../../../../02_year_2_core_computer_science/semester_3/CS205_software_engineering_i_design_testing/README.md), [CS215](../../../../02_year_2_core_computer_science/semester_4/CS215_cloud_and_devops_foundations/README.md); assumes [FND106](../../../../01_year_1_foundations/semester_1/FND106_technical_communication_and_professional_skills/README.md) and [FDE302](../FDE302_customer_discovery_and_requirements_engineering/README.md) | [FDE404](../../year_4/FDE404_field_studio_three_simulated_customer/README.md), [FDE403](../../year_4/FDE403_solution_architecture_pricing_and_roi/README.md), [CAR401](../../../../05_shared_years_3_to_5/CAR401_career_lab_ii_interviews_system_design_and_ai/README.md), [LCH502](../../../../05_shared_years_3_to_5/LCH502_career_launch_and_founder_studio/README.md) |

## Why this course matters now

Customer-facing engineering roles describe communication as core work, not a soft extra. Anthropic's India-based Applied AI Architects must deliver content "from technical deep dives for engineering & development teams up to business value focused conversations with executives"; OpenAI wants Deployment Leads who make "complex technical trade-offs legible to business leaders"; Razorpay's FDE posting asks for someone who "can explain a complex system to a non-technical merchant lead" and keeps "a regular progress cadence"; Sarvam AI's early-career FDEs "support pre-sales activities with technical demonstrations". AI assistants now draft documents, slides and status reports in seconds, which makes polished but empty text cheap and makes clear, true, specific writing more valuable. Live AI demos add a new risk: a model that answered well yesterday may answer differently in front of a chief financial officer today. This course teaches you to plan demos that work and stay honest, write design documents that get decisions made, summarise for executives, run workshops that produce outputs, handle objections, and write for people who do not share your vocabulary.

## Learning outcomes

By the end you can:

1. **Analyse** an audience (executive, manager, end user, IT, security, procurement) and **choose** what each needs to decide or do.
2. **Design** and **deliver** a demo with a story, realistic data, a rehearsed failure plan and honest disclosure of what is real.
3. **Write** a design document and architecture decision records that state goals, non-goals, alternatives and trade-offs, with C4 diagrams.
4. **Write** a one-page executive summary and a weekly status report with honest status, decisions needed and risks.
5. **Facilitate** a discovery or design workshop (EventStorming, Liberating Structures, design sprint techniques) and **capture** its outputs.
6. **Handle** objections about security, cost, accuracy, job loss and "we can build it ourselves" with evidence and without overclaiming.
7. **Explain** probabilistic AI results (error rates, confidence, evaluation results) to non-technical stakeholders accurately.
8. **Produce** handover documentation organised by user need (tutorials, how-to guides, reference, explanation).
9. **Use** AI writing tools while **verifying** facts, removing generic filler and protecting customer confidentiality.

## Chapters and lessons

### Chapter 1 · Audiences and messages (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Who decides what | Executive sponsor, budget owner, manager, end user, IT, security, procurement; the decision each makes | Map audiences for an illustrative deployment and the one message each must hear |
| 1.2 Bottom line up front | Lead with the conclusion and the ask; supporting points grouped under it (pyramid structure) | Rewrite three chronological emails into conclusion-first form |
| 1.3 Specific beats impressive | Numbers with units and denominators, named systems, dates; deleting adjectives | Edit a vague project update into a specific one; count removed words |
| 1.4 Register and language | Plain English; avoiding idioms for second-language readers; when to switch to Hindi or a regional language, and when to use a translator | Rewrite a technical paragraph at two reading levels |

**Check your understanding:** Why does an executive summary fail when it starts with background? What is the cost of an unexplained acronym in a customer email? When does "specific" become "too detailed"?

### Chapter 2 · Demos that work (weeks 2–3)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Story first | Problem → today's workflow → the new workflow → the result; show the user's moment, not the architecture | Script a five-minute demo around one user's task |
| 2.2 Data and environment | Realistic, anonymised or synthetic data in the customer's vocabulary; a dedicated demo environment; reset scripts | Build a resettable demo environment with seeded data |
| 2.3 Live AI demos | Non-determinism; fixed inputs you have tested; temperature and model version pinned; what to say when the model errs | Run the same demo prompt 20 times; record variance; choose inputs that are representative, not lucky |
| 2.4 Failure plans | Offline fallback, recorded backup, network failure, login failure; recovering calmly | Rehearse with a classmate who injects three failures |
| 2.5 Honesty | Never imply a mocked step is live; label prototypes; no cherry-picked results presented as typical | Write a disclosure line for every mocked component in your demo |
| 2.6 Discovery demos | Demos that ask questions ("is this how your team does it?") and collect requirements | Run a discovery demo and capture three corrections from the audience |

**Check your understanding:** Why is a demo with only perfect examples a future support problem? What should you disclose about a cached or mocked AI response? How do you recover when the model gives a wrong answer live?

### Chapter 3 · Design documents and decisions (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Design doc structure | Context and scope, goals and non-goals, the design, alternatives considered, cross-cutting concerns (security, privacy, operations) (Ubl, "Design Docs at Google") | Write a design doc for your FDE303 P2 integration |
| 3.2 Architecture decision records | One decision per record: context, decision, consequences; status and supersession | Write five ADRs for decisions you have already made |
| 3.3 Diagrams | C4 model levels (context, container, component); Mermaid for diagrams in version control; sequence diagrams for flows | Draw C4 context and container diagrams and one sequence diagram |
| 3.4 Reviews | Asking for review from the customer's architects; recording objections and resolutions | Run a review meeting and produce a resolution log |

**Check your understanding:** Why do non-goals prevent conflict later? When is a design doc too long to be useful? What belongs in an ADR's consequences section?

### Chapter 4 · Executive summaries and status reports (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 One page | Situation, result so far, decision needed, options with cost and risk, recommendation | Write a one-page summary for a pilot go/no-go decision |
| 4.2 Status that tells the truth | Red/amber/green with criteria; "watermelon" reports (green outside, red inside); early bad news | Rewrite a misleading green report honestly |
| 4.3 Numbers for executives | Ranges instead of point estimates; baselines; what changed and why | Present an ROI result with its uncertainty in three sentences |
| 4.4 Cadence | Weekly status, monthly steering committee, decision logs; what goes where | Design a reporting cadence for a three-month engagement |

**Check your understanding:** What are the criteria that turn a status from amber to red? Why does early bad news build trust? How do you present a result that is good but uncertain?

### Chapter 5 · Workshops (weeks 6–7)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Designing a workshop | Purpose, outputs, participants, agenda, materials; outputs defined before activities | Design a two-hour discovery workshop for an illustrative warehouse |
| 5.2 EventStorming | Domain events on a timeline, commands, actors, hotspots; finding where the process breaks | Run a 90-minute EventStorming session on a real campus process |
| 5.3 Liberating Structures | 1-2-4-All, 15% Solutions, TRIZ, Troika consulting; getting quiet people heard | Facilitate two structures with a group of six |
| 5.4 Design sprint techniques | Map, sketch, decide, prototype, test (GV design sprint); compressing it to two days | Run a compressed sprint on one problem |
| 5.5 Remote and hybrid | Virtual whiteboards, timeboxing, breakouts, accessibility | Run one session remotely and compare outputs with an in-person one |
| 5.6 After the workshop | Writing up outputs within 24 hours; owners and dates | Produce a workshop report and action list |

**Check your understanding:** Why define outputs before choosing activities? What does a workshop with only senior people in the room miss? Why must the write-up go out within a day?

### Chapter 6 · Objections and difficult conversations (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Listening first | Acknowledge, clarify, respond, confirm; finding the concern behind the objection | Role-play five objections with an observer scoring each step |
| 6.2 Security and privacy objections | Answering from evidence (architecture, contracts, certifications); saying "I will confirm" rather than guessing | Answer ten security objections using your FDE304 pack |
| 6.3 Accuracy and trust | "AI makes mistakes": showing evaluation results, human review and error handling honestly | Explain an 8% error rate and the controls around it to a sceptical manager |
| 6.4 Jobs and fear | Talking with staff whose work changes; what you can and cannot promise | Role-play a session with front-line staff worried about their roles |
| 6.5 Saying no and bad news | Declining scope, missed deadlines, a failed pilot; offering options | Deliver a missed-milestone message in person and in writing |

**Check your understanding:** Why does answering an objection immediately often fail? What must you never promise about jobs or accuracy? How do you say no to a sponsor without losing them?

### Chapter 7 · Explaining AI to non-specialists (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Probabilities in plain words | Natural frequencies ("8 in 100 letters need correction") instead of percentages alone; base rates | Rewrite five evaluation results as natural frequencies |
| 7.2 Error types | False positives versus false negatives in the customer's terms (missed fraud versus blocked customer) | Explain a precision-recall trade-off to a branch manager with one example |
| 7.3 Uncertainty language | Confidence intervals in words; what is known, unknown and assumed | Write a findings paragraph with calibrated wording |
| 7.4 Visuals | Simple charts with labelled axes and units; avoiding truncated axes and 3D charts | Redesign two misleading charts |

**Check your understanding:** Why are natural frequencies easier to understand than percentages? Which error type does your customer fear more, and how does that change the threshold? What makes a chart misleading even when every number is correct?

### Chapter 8 · Documentation and handover (week 10)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Diátaxis | Tutorials, how-to guides, reference and explanation serve different needs | Reorganise a messy README into the four types |
| 8.2 Runbooks for customers | Prerequisites, steps with expected output, verification, rollback, escalation contacts | Write a runbook a classmate can follow without asking you |
| 8.3 Style | Google developer documentation style guide; consistent terms; screenshots that age well | Apply five style rules to a document and list the changes |
| 8.4 Leaving a trail | Documentation so partners can repeat a deployment (a16z's "leave a trail") | Write a partner handover guide for one integration |

**Check your understanding:** Why do tutorials and reference pages conflict when merged? What makes a runbook step verifiable? What does a partner need that the customer's team does not?

### Chapter 9 · Presenting live (week 11)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Slides that carry an argument | Assertion-evidence slides: a sentence headline and visual evidence | Convert a bullet deck into assertion-evidence form |
| 9.2 Time and structure | Ten-minute readouts; one idea per slide; leaving time for questions | Deliver a ten-minute readout to a timed panel |
| 9.3 Questions | Repeating the question, answering briefly, parking off-topic questions, "I don't know yet" | Handle a hostile Q&A round |
| 9.4 Cross-cultural settings | Hierarchy, indirect disagreement, meeting styles across India, Japan, Europe and the US (OpenAI's Tokyo FDE role requires Japanese and English) | Prepare one readout for two audiences with different norms |

**Check your understanding:** Why does a sentence headline beat a topic headline? How do you handle a question you cannot answer in front of an executive? What signals disagreement in a meeting where nobody says "no"?

### Chapter 10 · Writing with AI, responsibly (week 12)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Useful drafting | Outlines, first drafts from your own notes, tightening, translating, alternative phrasings | Draft a design doc section with an assistant; edit it; record changes |
| 10.2 What goes wrong | Invented facts, generic filler, wrong tone, claims you cannot support | Audit three AI drafts; mark every unsupported sentence |
| 10.3 Confidentiality | Customer documents in approved tools only; redaction; retention settings | Write a redaction checklist and apply it before using an assistant |
| 10.4 Voice and accountability | Your name is on it; you must be able to defend every sentence | Defend an AI-assisted document line by line in a review |

**Check your understanding:** Which parts of a customer document should never be AI-drafted? How do you detect generic filler in your own writing? What makes an AI-assisted document trustworthy?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Audience map and rewrites | — |
| 2 | 2 | Lab 2 · Demo script and environment | — |
| 3 | 2 | Lab 3 · Failure-injected demo rehearsal | **P1 due** |
| 4 | 3 | Lab 4 · Design doc, ADRs and C4 | — |
| 5 | 4 | Lab 5 · Executive summary and honest status | — |
| 6 | 5 | Lab 6 · EventStorming session | — |
| 7 | 5 | Lab 6 (cont.): Liberating Structures | Mid-term (AI off): timed written summary |
| 8 | 6 | Lab 7 · Objection role-plays | — |
| 9 | 7 | Lab 8 · Explaining evaluation results | **P2 due** |
| 10 | 8 | Lab 9 · Runbook handoff test | — |
| 11 | 9 | Lab 10 · Timed readout and Q&A | — |
| 12 | 10 | Lab 11 · AI-draft audit | — |
| 13 | Integration | P3 workshop and demo | — |
| 14 | Integration | P3 readout to panel | **P3 due** |
| 15 | Review | Live demo exam with injected failures | Final exam (AI off for writing) |

## Working with AI in this course

- **Use AI for:** outlining, tightening drafts you wrote, generating role-play objections and personas for practice, converting diagrams to Mermaid, translating summaries for review by a fluent speaker, and generating synthetic demo data.
- **Do without AI (drills):** the mid-term timed summary; live demos and Q&A; objection role-plays; first drafts of executive summaries. Customers judge you in the room.
- **Verify AI output by:** checking every number and name against the source; reading aloud to catch generic filler; asking a fluent speaker to review translations; running every command in a runbook exactly as written.
- **Where AI still fails here (show it):** in Lab 11, record invented facts, generic claims ("seamless", "robust") and tone errors in AI drafts; show one translation error that would mislead a customer.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (11) | 25% |
| Projects P1–P3 | 35% |
| Design doc and runbook | 10% |
| Mid-term (AI off) | 10% |
| Final live demo exam + P3 readout | 20% |

**Mastery gate.** You pass when you can: (1) deliver a ten-minute demo of a working system to a panel that injects two failures, recover from both, and disclose every mocked part; (2) write, AI off and in 45 minutes, a one-page executive summary from a ten-page technical report that a non-technical reader rates as clear and that contains no factual error; (3) facilitate a 60-minute workshop that produces the outputs you defined in advance.

## Industry reality

Postings for FDE-type roles name these skills directly (Anthropic, OpenAI, Razorpay, Sarvam AI, 2026). Design documents and architecture decision records are standard engineering practice; Google's design-doc culture is publicly described by its engineers. Workshop methods such as EventStorming and design sprints are widely used for discovery. In India, customer-facing engineers often present to mixed audiences and switch between English and Hindi or regional languages; written summaries are what travel up the hierarchy.

**Interview questions from this course**

1. *Demo our product to me as if I were the CFO of a mid-size manufacturer.* Strong answer: starts with the CFO's problem and numbers; shows one workflow end to end; quantifies impact with assumptions; invites questions; avoids architecture detail unless asked.
2. *Your live demo fails in front of the customer. What do you do?* Strong answer: stays calm, names what happened, switches to the fallback, explains the failure mode and how production handles it, follows up in writing.
3. *Write a status update for a project that is two weeks late.* Strong answer: bottom line first, cause, impact, revised date with confidence, what is needed from whom, no blame.
4. *A security architect says "AI is too risky for our data." Respond.* Strong answer: asks which risks; answers with architecture, contract terms, residency and controls; offers evidence and a review; does not dismiss or overpromise.
5. *Explain to a branch manager what "92% accuracy" means for their team.* Strong answer: natural frequencies (8 in 100 need correction), which errors matter, how review catches them, time cost of review, how the number was measured.

## Resources (free first)

- **Design docs and decisions:** Malte Ubl, "Design Docs at Google" — https://www.industrialempathy.com/posts/design-docs-at-google/ ; Architecture decision records — https://adr.github.io/ ; C4 model — https://c4model.com/ ; Mermaid — https://mermaid.js.org/
- **Writing and documentation:** Diátaxis — https://diataxis.fr/ ; Google developer documentation style guide — https://developers.google.com/style ; US federal plain language guidelines — https://www.plainlanguage.gov/guidelines/
- **Workshops:** Liberating Structures — https://www.liberatingstructures.com/ ; EventStorming — https://www.eventstorming.com/ ; GV design sprint — https://www.gv.com/sprint/
- **Presenting:** Assertion-evidence approach (Michael Alley) — https://www.assertion-evidence.com/
- **Paid, optional:** Barbara Minto, *The Pyramid Principle*; Peter Cohan, *Great Demo!*; Alberto Brandolini, *Introducing EventStorming*.

## Sources

- Anthropic, Applied AI Architect, Bangalore — https://job-boards.greenhouse.io/anthropic/jobs/5390746008 (checked 2026-10)
- OpenAI, Deployment Lead, FDE (SF) — https://openai.com/careers/deployment-lead-fde-sf-san-francisco/ ; Forward Deployed Engineer, Tokyo — https://openai.com/careers/forward-deployed-engineer-tokyo/ (checked 2026-10)
- Razorpay, Forward Deployed Engineer (Aug 2026) — https://portfoliojobs.tcv.com/companies/razorpay/jobs/89918935-forward-deployed-engineer ; Sarvam AI, FDSE — https://careers.kula.ai/sarvam-ai/17986 (checked 2026-10)
- a16z, "Trading Margin for Moat" (4 Jun 2025) — https://a16z.com/services-led-growth/ (checked 2026-10)

_Last reviewed: 2026-10_
