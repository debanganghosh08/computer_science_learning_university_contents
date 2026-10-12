# FDE302 · Customer Discovery and Requirements Engineering

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 3 · 5 | 4 (≈ 120 hours) | L1 → L3 | [CS205](../../../../02_year_2_core_computer_science/semester_3/CS205_software_engineering_i_design_testing/README.md), [CS215](../../../../02_year_2_core_computer_science/semester_4/CS215_cloud_and_devops_foundations/README.md); assumes [FND106](../../../../01_year_1_foundations/semester_1/FND106_technical_communication_and_professional_skills/README.md) and [FND116](../../../../01_year_1_foundations/semester_2/FND116_probability_and_statistics_i/README.md) | [FDE402](../../year_4/FDE402_debugging_and_operating_in_customer_environments/README.md), [FDE304](../FDE304_deploying_ai_in_the_enterprise/README.md), [FDE305](../FDE305_technical_communication_in_the_field_demos/README.md), [FDE404](../../year_4/FDE404_field_studio_three_simulated_customer/README.md) |

## Why this course matters now

Customers rarely ask for what they need. They ask for "a chatbot" when the problem is that discharge summaries take four hours, or for "a dashboard" when nobody trusts the numbers behind it. OpenAI's Deployment Leads are expected to embed with customers "to map workflows and success criteria"; Palantir's deployment strategists co-create workflows with the people who will use them and run pilots of 4–12 weeks (2022). AI tools now transcribe interviews, cluster notes into themes and draft requirement documents in minutes, which makes discovery look easy. They cannot tell you that the interviewee was describing the official process while the real one runs on a shared spreadsheet, or that the person asking for automation is not the person who will lose time if it fails. This course teaches you to find the real problem, map the work as it is actually done, write requirements and success criteria that can be tested, and scope a pilot that will produce a decision.

## Learning outcomes

By the end you can:

1. **Separate** a customer's requested solution from the underlying problem, and **write** a problem statement that names who is affected, how often, and at what cost.
2. **Map** stakeholders by influence and interest, and **identify** the economic buyer, users, blockers and approvers (IT, security, legal, procurement).
3. **Run** a non-leading user interview and a contextual observation session, and **synthesise** findings with traceable evidence.
4. **Model** a workflow as it is actually done (swimlanes and BPMN), including exceptions and workarounds, and **measure** cycle time and wait time.
5. **Discover** process variants from an event log with process mining, and **compare** them with the documented process.
6. **Write** requirements as job stories, testable acceptance criteria (Gherkin) and EARS statements, including non-functional and compliance requirements.
7. **Scope** a pilot with an appetite, in-scope and out-of-scope lists, a baseline, success criteria and kill criteria.
8. **Use** AI to speed up synthesis while **verifying** every theme against raw notes, with consent and data protection in place.

## Chapters and lessons

### Chapter 1 · The problem behind the ask (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Asks are solutions | The XY problem; "we need a chatbot" as a hypothesis; restating an ask as a problem | Rewrite ten illustrative customer asks as problem hypotheses |
| 1.2 Five whys and its limits | Toyota's five whys; why a single causal chain misleads; issue trees (mutually exclusive, collectively exhaustive) | Build an issue tree for "our invoice processing is too slow" |
| 1.3 Cost of the problem | Frequency × time × people × error cost; who pays; what happens if nothing changes | Estimate the annual cost of an illustrative problem with stated assumptions and ranges |
| 1.4 Problem statements | Who, what, when, how often, current cost, desired outcome; no solution words | Write and peer-review three problem statements |

**Check your understanding:** Why is "the customer said so" weak evidence that a problem matters? What makes an issue tree useful rather than decorative? When does a problem not deserve a pilot?

### Chapter 2 · Stakeholders and the buying centre (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Who is who | Economic buyer, executive sponsor, champion, end users, IT, security, legal, procurement, works with unions or staff representatives where relevant | Build a stakeholder map for an illustrative hospital deployment |
| 2.2 Influence and interest | Power-interest grid; informal influence; the person whose job changes most | Place 12 stakeholders on a grid; justify three placements |
| 2.3 Stakeholder interviews | Different questions for sponsors, managers and front-line staff; NN/g stakeholder interview guidance | Write three tailored interview guides |
| 2.4 Conflicting goals | Sponsor wants cost cuts, users want fewer clicks, IT wants fewer systems; making trade-offs explicit | Write a one-page conflict summary and a proposal to resolve it |
| 2.5 Hierarchy and culture | Deference in hierarchical organisations (common in large Indian enterprises and public bodies); getting honest answers from junior staff | Role-play an interview where a manager is present; then redesign the session |

**Check your understanding:** Why can a strong champion still lose a deal? Whose objections arrive late in a deployment and how do you surface them in week one? What changes when a senior manager sits in on a user interview?

### Chapter 3 · Interviewing users (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Questions that do not lie | Ask about specific past events, not opinions about the future; avoid pitching (Fitzpatrick, *The Mom Test*) | Rewrite 15 bad questions into good ones |
| 3.2 Running the session | Consent, recording rules, opening, timeline questions ("walk me through the last time…"), silence, follow-ups, closing | Run two practice interviews; get feedback on leading questions |
| 3.3 Interviewing across languages | Interpreters, code-switching between English and Hindi or a regional language, translating jargon, checking understanding | Run one interview in a language other than English (or with an interpreter) and record what was lost |
| 3.4 Notes and evidence | Verbatim quotes versus interpretation; tagging; keeping a link from every finding to a source | Produce a note template with quote, observation and interpretation columns |
| 3.5 Synthesis | Affinity mapping, themes with counts, surprising findings, contradictions | Synthesise five interviews into findings, each with at least two pieces of evidence |

**Check your understanding:** Why do compliments in an interview carry almost no information? How many interviews are enough, and what tells you to stop? What is the risk of synthesising only from your memory of a session?

### Chapter 4 · Observation and contextual inquiry (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Say versus do | People describe the official process; observation reveals the real one (NN/g contextual inquiry; master-apprentice model) | Observe someone doing a routine digital task for 30 minutes; list differences from their own description |
| 4.2 Workarounds as signals | Shadow spreadsheets, sticky notes, WhatsApp groups, copy-paste between systems | Catalogue every workaround in one observed workflow |
| 4.3 Artefacts | Forms, printed reports, email templates, exception logs as data | Collect and annotate five artefacts (anonymised) |
| 4.4 Ethics of observation | Consent, recording rules, not evaluating individuals' performance, what you must not write down | Write an observation consent script and a data-handling note |

**Check your understanding:** Why are workarounds often the best evidence of unmet needs? What would make an observation session unethical even with consent? How do you observe a task that happens once a month?

### Chapter 5 · Workflow mapping (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Swimlanes and SIPOC | Suppliers, inputs, process, outputs, customers; handoffs between roles | Map an illustrative purchase-to-pay process as swimlanes |
| 5.2 BPMN 2.0 basics | Events, activities, gateways, pools and lanes (OMG BPMN 2.0.2); enough notation to be precise | Redraw your swimlane map in BPMN with exclusive and parallel gateways |
| 5.3 Value stream mapping | Process time versus wait time; queues; rework loops; where the hours actually go | Compute process-time ratio for an observed workflow |
| 5.4 Exceptions | The 20% of cases that consume most effort; exception categories and their frequency | Count exceptions from a sample of 50 illustrative cases |
| 5.5 Automation candidates | Steps that are high-volume, rule-based or text-heavy; where a human must stay in the loop | Mark candidate steps for automation and justify each |

**Check your understanding:** Why does automating a step with mostly wait time around it often change nothing? Which BPMN element captures "a manager approves within two days or it escalates"? What happens to a workflow map that ignores exceptions?

### Chapter 6 · Process mining from event logs (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Event logs | Case ID, activity, timestamp, resource; extracting them from ERP, ticketing and audit tables | Build an event log from an illustrative ticket export |
| 6.2 Discovery | Directly-follows graphs, variants, frequency and performance views (PM4Py) | Discover the top ten variants of a public process mining dataset |
| 6.3 Conformance | Comparing the documented model with the log; deviations and their causes | Measure how many cases follow the documented path |
| 6.4 Limits | Missing events, wrong timestamps, merged cases, time zones; logs show what systems record, not what people do | List five ways your log could mislead you |

**Check your understanding:** What can a log tell you that interviews cannot, and the reverse? Why do time zones and batch jobs distort waiting times? When is process mining not worth the effort?

### Chapter 7 · Jobs-to-be-done and outcomes (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Jobs-to-be-done | The progress a person is trying to make in a circumstance (Christensen et al., HBR 2016); functional, emotional and social dimensions | Write job statements for three user groups in one deployment |
| 7.2 Job stories | "When…, I want to…, so I can…" versus persona-based user stories | Convert ten user stories into job stories and note what changed |
| 7.3 Desired outcomes | Measurable outcome statements (minimise time to…, reduce likelihood of…) | Write eight outcome statements and rank them with users |
| 7.4 Switching forces | What pushes users away from the current way, what pulls them to a new one, and the anxieties and habits that hold them back | Map switching forces for an AI assistant in a claims team |

**Check your understanding:** Why can two users with the same title have different jobs? How do switching anxieties predict adoption problems? What does a job statement exclude that a feature request includes?

### Chapter 8 · Requirements that can be tested (weeks 8–9)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Acceptance criteria | Given-When-Then (Gherkin); examples as specifications; edge cases | Write acceptance criteria for five job stories, including two failure cases each |
| 8.2 EARS | Easy Approach to Requirements Syntax: ubiquitous, event-driven, state-driven, unwanted-behaviour and optional patterns (Mavin et al., 2009) | Rewrite ten vague requirements in EARS |
| 8.3 Non-functional requirements | Latency, availability, throughput, accessibility, languages, audit, data residency, retention | Write a non-functional requirements table with measurable targets |
| 8.4 Compliance and security requirements | DPDP consent and purpose, sector rules (RBI, health records), audit trails, access control | Extract requirements from one regulation section and trace each to a test |
| 8.5 Traceability and change | Requirement → design → test links; change control; ISO/IEC/IEEE 29148 as a reference vocabulary | Build a traceability matrix for a small pilot |
| 8.6 Requirements for AI features | Examples instead of rules; accuracy thresholds; acceptable errors; when a human must review | Write requirements for an AI document classifier with a target and a review rule |

**Check your understanding:** Why does "the system should be fast" fail as a requirement? How do requirements for a probabilistic AI feature differ from those for a form? Which requirement is most often discovered too late in enterprise deployments, and why?

### Chapter 9 · Data discovery (week 10)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Data inventory | Systems, tables, files, owners, refresh rates, access paths, sensitivity | Build a data inventory for an illustrative distributor |
| 9.2 Sample pulls | Asking for small samples early; profiling them; what bad data looks like | Profile a messy public dataset and list quality issues |
| 9.3 Access reality | Who must approve access, how long it takes, what can be shared off-site | Write the access request and approval chain for a pilot |
| 9.4 Seeding evaluation data | Collecting real examples and expert judgements during discovery for later golden sets | Collect 30 labelled examples from a classmate acting as domain expert |

**Check your understanding:** Why ask for sample data in the first week? What is the cost of discovering a missing field in week six? How do discovery interviews double as evaluation data collection?

### Chapter 10 · Scoping pilots (weeks 11–12)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Appetite | Fixing time and varying scope (Basecamp, *Shape Up*); rabbit holes and no-gos | Shape a six-week pilot with explicit no-gos |
| 10.2 Pilot charter | Problem, users, scope, data, success criteria, baseline, kill criteria, decision date, owners | Write a full charter and get a sponsor-role classmate to sign it |
| 10.3 Success criteria | Specific, measurable, agreed before build; thresholds for go, extend and stop | Define go/extend/stop thresholds for an illustrative pilot |
| 10.4 Avoiding pilot purgatory | Pilots without a decision owner, budget or production path; designing for the decision | Diagnose three illustrative stalled pilots |
| 10.5 Discovery plans | Planning the first two weeks of an engagement: who to talk to, what to observe, which data to request | Write a two-week discovery plan with a calendar |

**Check your understanding:** Why must success criteria be agreed before the build starts? What makes a kill criterion credible? How does fixing time change what you choose to build?

### Chapter 11 · Discovery with AI, safely (week 13)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Transcription | Whisper and commercial transcription; consent for recording; accuracy on Indian English and code-switched speech | Transcribe a consented interview; measure word error rate on a two-minute sample |
| 11.2 AI-assisted synthesis | Clustering notes, drafting themes, extracting requirements; prompt with raw notes, not summaries | Compare AI themes with your manual synthesis; list missing and invented themes |
| 11.3 Synthetic users | Why LLM "personas" cannot replace real users; acceptable uses (practice, question design) | Run a synthetic interview and a real one on the same topic; compare |
| 11.4 Data protection | Approved tools, redaction of personal data, retention settings, customer policy | Write a redaction step and test it on ten transcripts |

**Check your understanding:** What does an AI summary of interviews lose that matters for design? Why is a synthetic user's answer not evidence? What must be true before a customer's interview recordings go into any AI tool?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Asks to problems | Problem statements |
| 2 | 2 | Lab 2 · Stakeholder map and guides | — |
| 3 | 3 | Lab 3 · Interviews and synthesis | — |
| 4 | 4 | Lab 4 · Contextual observation | **P1 due** |
| 5 | 5 | Lab 5 · BPMN and value stream map | — |
| 6 | 6 | Lab 6 · Process mining | — |
| 7 | 7 | Lab 7 · Jobs and outcomes | Mid-term (AI off): case discovery plan |
| 8 | 8 | Lab 8 · Requirements and traceability | — |
| 9 | 8 | Lab 8 (cont.) | Requirements pack |
| 10 | 9 | Lab 9 · Data inventory and profiling | **P2 due** |
| 11 | 10 | Lab 10 · Pilot charter | — |
| 12 | 10 | P3 discovery | Charter signed |
| 13 | 11 | Lab 11 · AI-assisted synthesis audit | — |
| 14 | Integration | P3 presentations | **P3 due** |
| 15 | Review | Live discovery role-play exam | Final exam (AI off) |

## Working with AI in this course

- **Use AI for:** transcription (with consent), first-pass clustering of notes, drafting interview guides for you to edit, converting requirements into Gherkin skeletons, generating edge cases for acceptance criteria, and writing PM4Py analysis code. Claude, ChatGPT and Gemini handle synthesis drafts; Whisper handles transcription locally.
- **Do without AI (drills):** live interviews and observation; the first synthesis of every interview set; issue trees; the mid-term and final role-plays. Customers notice when you are reading from a script.
- **Verify AI output by:** tracing every theme to at least two quotes in the raw notes; counting how many raw observations an AI summary dropped; re-running process mining numbers on a filtered log; reading generated Gherkin against the job story.
- **Where AI still fails here (show it):** in Lab 11, record themes the AI invented and minority findings it dropped; measure transcription errors on code-switched speech; show one case where an AI-drafted requirement silently added a solution.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (11) | 25% |
| Projects P1–P3 | 35% |
| Requirements pack and pilot charter | 10% |
| Mid-term (AI off) | 10% |
| Final role-play exam (AI off) + P3 defence | 20% |

**Mastery gate.** You pass when you can: (1) in a 45-minute live role-play with an instructor playing a customer with a misleading ask, find the underlying problem and agree a written problem statement; (2) from a raw event log and three interview transcripts you have not seen, produce in one day a workflow map with measured wait times, five testable requirements and a pilot charter with go/extend/stop thresholds; (3) show that every finding in your synthesis traces to raw evidence.

## Industry reality

Discovery is named as core work in current postings: OpenAI's FDEs "own discovery, technical scoping, system design" and its Deployment Leads "map workflows and success criteria"; Anthropic's India Applied AI Architects guide customers "from initial technical discovery through successful deployment". Public-sector service teams in the UK run a formal discovery phase before building (GOV.UK Service Manual), a useful free model. Process mining is used on ERP and ticketing logs in large enterprises; PM4Py is the main open-source library.

**Interview questions from this course**

1. *A hospital asks you to build a chatbot for patients. How do you start?* Strong answer: does not start with the chatbot; asks what problem it should solve and for whom; plans stakeholder and user interviews, observation of the front desk or call centre, and a data request; defines a baseline; considers non-AI solutions.
2. *How do you know an interviewee is telling you the real process?* Strong answer: asks about specific recent cases; observes the work; looks for workarounds and artefacts; checks against system logs; interviews several roles.
3. *Write a requirement for an AI feature that extracts invoice fields.* Strong answer: field-level accuracy targets on a defined test set, behaviour on low confidence (route to human), latency, languages and formats, audit trail, data retention.
4. *Your sponsor wants a pilot to "show AI value". How do you scope it?* Strong answer: chooses one workflow and user group; baseline first; success, extend and stop thresholds agreed in writing; fixed time with variable scope; a decision owner and a path to production.
5. *Two stakeholders want contradictory things. What do you do?* Strong answer: makes the conflict explicit with evidence, quantifies the trade-off, takes it to the decision owner with options, documents the decision.

## Resources (free first)

- **Discovery and research methods:** GOV.UK Service Manual, discovery phase — https://www.gov.uk/service-manual/agile-delivery/how-the-discovery-phase-works ; user research — https://www.gov.uk/service-manual/user-research ; Nielsen Norman Group: user interviews — https://www.nngroup.com/articles/user-interviews/ , contextual inquiry — https://www.nngroup.com/articles/contextual-inquiry/ , stakeholder interviews — https://www.nngroup.com/articles/stakeholder-interviews/
- **Jobs-to-be-done:** Christensen, Hall, Dillon and Duncan, "Know Your Customers' 'Jobs to Be Done'", HBR (Sep 2016) — https://hbr.org/2016/09/know-your-customers-jobs-to-be-done
- **Workflow and process mining:** OMG BPMN 2.0.2 — https://www.omg.org/spec/BPMN/2.0.2/ ; PM4Py — https://processintelligence.solutions/pm4py ; Process Mining course (van der Aalst, Coursera, free to audit) — https://www.coursera.org/learn/process-mining ; EventStorming — https://www.eventstorming.com/
- **Requirements:** EARS — https://alistairmavin.com/ears/ ; Gherkin reference — https://cucumber.io/docs/gherkin/reference/ ; ISO/IEC/IEEE 29148:2018 (paid standard; vocabulary reference) — https://www.iso.org/standard/72089.html
- **Scoping:** Basecamp, *Shape Up* (free online) — https://basecamp.com/shapeup
- **Tools:** Whisper — https://github.com/openai/whisper
- **Paid, optional:** Rob Fitzpatrick, *The Mom Test* (2013) — https://www.momtestbook.com/ ; Teresa Torres, *Continuous Discovery Habits* (2021).

## Sources

- OpenAI, Forward Deployed Engineer (Tokyo) and Deployment Lead (SF) postings — https://openai.com/careers/forward-deployed-engineer-tokyo/ ; https://openai.com/careers/deployment-lead-fde-sf-san-francisco/ (checked 2026-10)
- Palantir, "A Day in the Life of a Palantir Deployment Strategist" (8 Mar 2022) — https://blog.palantir.com/a-day-in-the-life-of-a-palantir-deployment-strategist-951cb59a5a96 (checked 2026-10)
- Anthropic, Applied AI Architect, Bangalore — https://job-boards.greenhouse.io/anthropic/jobs/5390746008 (checked 2026-10)
- Christensen et al., HBR (Sep 2016), URL above; Mavin et al., "Easy Approach to Requirements Syntax (EARS)", IEEE RE 2009, summary at https://alistairmavin.com/ears/ (checked 2026-10)
- GOV.UK Service Manual and NN/g articles, URLs above (checked 2026-10)

_Last reviewed: 2026-10_
