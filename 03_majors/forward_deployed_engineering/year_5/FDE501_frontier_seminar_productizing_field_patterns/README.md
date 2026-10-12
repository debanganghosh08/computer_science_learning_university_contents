# FDE501 · Frontier Seminar: Productizing Field Patterns and the FDE-to-Founder Path

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 5 · 9 | 4 (≈ 120 hours) | L4 → L5 | [FDE401](../../year_4/FDE401_data_integration_and_ontology_modeling/README.md), [FDE403](../../year_4/FDE403_solution_architecture_pricing_and_roi/README.md); assumes [FDE404](../../year_4/FDE404_field_studio_three_simulated_customer/README.md); taken with [RES501](../../../../05_shared_years_3_to_5/RES501_research_methods_and_scientific_writing/README.md) | [THS501](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md), [THS502](../../../../05_shared_years_3_to_5/THS502_thesis_or_capstone_ii/README.md), [LCH502](../../../../05_shared_years_3_to_5/LCH502_career_launch_and_founder_studio/README.md), [RES502](../../../../05_shared_years_3_to_5/RES502_reading_reproducing_and_extending_papers/README.md) |

## Why this course matters now

The forward deployed model has a built-in tension. Palantir describes the product engineer's focus as "one capability, many customers" and the forward deployed engineer's as "one customer, many capabilities" (2019). Value compounds only when what is learned with one customer becomes something every customer gets. Employers now write this into roles: OpenAI measures Deployment Leads partly on "operating leverage (patterns reused across deployments)", Anthropic asks FDEs to "identify and codify repeatable deployment patterns", and Razorpay asks for a write-up whenever the same thing is built for two or more merchants. Investors argue that AI application companies should accept services-heavy early years to become the "system of work" and automate the services motion over time (a16z, 2025). Meanwhile AI is starting to automate parts of deployment itself, while its reliability on long tasks still lags its capability: on METR's software tasks, the best model measured in early 2026 succeeds half the time on tasks that take an expert about 12 hours, but its 80%-reliability horizon is about 70 minutes. Field studies show AI's effect on real work is uneven: a staggered rollout to 5,179 support agents raised issues resolved per hour by 14% on average and 34% for novices (Brynjolfsson, Li and Raymond), while consultants using AI on a task outside its "jagged frontier" were 19% less likely to be correct (Dell'Acqua et al., 2023). This seminar is about the next step: turning field patterns into products and platforms, measuring deployments rigorously enough to publish, and, for some students, founding a company from a problem seen repeatedly in the field.

## Learning outcomes

By the end you can:

1. **Extract** patterns from multiple deployments, **decide** which to productise, and **specify** them as product features, platform components or playbooks with evidence.
2. **Analyse** the economics of services-led AI companies (gross margin, services margin, partner ecosystems, outcome contracts) and **critique** published arguments.
3. **Design** agentic deployment tooling (agents that scaffold integrations, map data and run evaluations) with human checkpoints, and **measure** its reliability.
4. **Design** fleet-scale deployment operations across many customers: configuration over code, upgrades under constraints, per-customer evaluation suites.
5. **Plan** and **critique** field studies of deployments (staggered rollouts, randomised trials, case studies, design science) and their threats to validity.
6. **Map** deployments at scale to AI governance frameworks (ISO/IEC 42001, NIST AI RMF, India's AI Governance Guidelines, RBI FREE-AI, EU AI Act).
7. **Evaluate** a startup opportunity from field experience with customer-development evidence, and **identify** the legal and ethical boundaries of using what you learned at an employer or customer.
8. **Write** a research paper, thesis proposal or venture memo to a publishable or investable standard.

## Chapters and lessons

### Chapter 1 · From field to product (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 The Dev–Delta tension | "One capability, many customers" versus "one customer, many capabilities"; Deltas contributing code back with the product team's agreement (Palantir, 2019) | Map the flow of one field request to a product change in a company you studied |
| 1.2 Evidence for productising | Frequency across customers, cost of workarounds, willingness to pay, fit with the product's direction | Score ten field reports from your FDE404 work on a productisation rubric |
| 1.3 Forms of leverage | Core features, extension points, connectors, templates, evaluation suites, playbooks, partner kits | Classify your FDE404 P2 component and decide its best form |
| 1.4 What must stay custom | Customer-specific logic, confidential data and practices; the line between pattern and secret | Write rules for what may and may not leave a customer engagement |

**Check your understanding:** Why does productising too early fail as badly as never productising? What evidence would convince a sceptical head of product? Which field patterns are really customers' confidential practices?

### Chapter 2 · Economics of services-led AI companies (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Margin versus moat | a16z's argument: optimise total gross profit, not 80% gross margin, while racing to own the data layer; its counterarguments | Write a 1,000-word critique with evidence from public filings or posts |
| 2.2 Partners and certification | Ecosystems that scale deployment: Anthropic reports 36,000+ consultants certified since March 2026, with Indian firms (Infosys, TCS, Wipro, Persistent, Fractal) committing to thousands of certifications and EPAM planning 250 specialised FDEs | Design a partner programme for an illustrative AI start-up |
| 2.3 Outcome contracts | Outcome-based and risk-sharing constructs in Indian IT services (NASSCOM 2026); per-outcome AI pricing | Model a services firm's margin under outcome pricing as automation improves |
| 2.4 When services become a trap | Endless customisation, low-margin contracts, product neglect | Diagnose an illustrative company stuck in services |

**Check your understanding:** Under what conditions do services build a moat rather than a trap? Why would a model company want partners to do deployments? How does automation of deployment change a services firm's pricing power?

### Chapter 3 · Agentic deployment (weeks 3–4)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 What can be automated | a16z lists "process mining, data pipeline automation, system integrations, and combing through API documentation"; your FDE404 time logs as data | Measure which of your FDE404 tasks an agent completes reliably |
| 3.2 Building blocks | MCP (2026-07-28 revision), agent skills, agent-to-agent protocols (A2A), durable execution; Anthropic's FDE deliverables ("MCP servers, sub-agents, and agent skills") | Build an agent skill that scaffolds a connector from an OpenAPI file and a sample |
| 3.3 Reliability limits | METR time horizons: long tasks at 50% success, much shorter at 80%; checkpoints and human gates | Report pass^k for your scaffolding agent on 20 integration tasks |
| 3.4 Evaluation as the deployment gate | Customer-specific eval suites generated, versioned and run automatically | Build an evaluation-agreement generator and test it on two briefs |
| 3.5 Humans in agentic deployment | Where people stay: discovery, access, trust, go-live decisions, incidents | Write a design note on human roles in an automated deployment pipeline |

**Check your understanding:** Why does an 80% reliability horizon matter more than a 50% horizon for deployment automation? Which FDE tasks resist automation, and why? How would you prove your scaffolding agent saves time without hiding its failures?

### Chapter 4 · Fleet-scale operations (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Many customers, one product | Configuration over code; tenant isolation; feature flags per customer | Refactor a customer-specific deployment into configuration |
| 4.2 Upgrades under constraints | Palantir Apollo's model: product constraints plus environment constraints drive automatic, compliant upgrades across connected and air-gapped sites | Design an upgrade orchestrator for 50 illustrative sites with different windows |
| 4.3 Per-customer evaluation | Running each customer's eval suite before every model or prompt change | Simulate a model change across five customers' suites; decide per customer |
| 4.4 Telemetry with consent | What you may learn across customers; aggregation and anonymisation; contracts | Write a telemetry policy that a bank's CISO would accept |

**Check your understanding:** What breaks when fifty customers each have a fork? Why must a model upgrade pass each customer's suite? What cross-customer learning is ethical and contractual?

### Chapter 5 · Measuring deployments scientifically (weeks 6–7)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Field experiments | Staggered rollout across 5,179 support agents (Brynjolfsson, Li and Raymond, NBER w31161); randomised assignment of 758 consultants (Dell'Acqua et al., 2023) | Present one study's design, results and threats to validity |
| 5.2 When AI slows experts | METR's 2025 randomised trial: experienced developers 19% slower with AI on their own repositories, despite believing they were faster | Compare the three studies' designs and explain the different results |
| 5.3 Case study research | Guidelines for case studies in software engineering (Runeson and Höst, 2009); multiple-case designs | Design a multiple-case study of your FDE404 deployments |
| 5.4 Design science research | Building and evaluating artefacts as research (Hevner et al., 2004) | Frame your FDE404 P2 component as a design-science contribution |
| 5.5 Threats to validity | Selection, novelty effects, Hawthorne effects, measurement drift, contamination between groups | Write a validity section for a planned field study |

**Check your understanding:** Why did a staggered rollout give stronger evidence than a before/after comparison? How can AI raise average productivity and still harm some tasks? What makes a single-deployment case study publishable?

### Chapter 6 · Governance at scale (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Management systems | ISO/IEC 42001 and NIST AI RMF as the structure customers' auditors use | Map your deployment programme to the four NIST AI RMF functions |
| 6.2 India | AI Governance Guidelines (Nov 2025); RBI FREE-AI (Aug 2025); DPDP Rules (Nov 2025) | Write a governance pack for deploying the same product to a bank and a hospital |
| 6.3 Global | EU AI Act (Regulation (EU) 2024/1689) risk tiers; liability lessons (Moffatt v. Air Canada, 2024) | Classify your deployments under the EU AI Act and list obligations |
| 6.4 Governance as product | Building audit logs, evaluation evidence and model cards into the product so every deployment inherits them | Specify three governance features for your product |

**Check your understanding:** Why is governance cheaper built into the product than added per deployment? Which obligations differ between Indian banks and hospitals? What evidence would an auditor ask for first?

### Chapter 7 · From FDE to founder I: finding the company (weeks 9–10)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Repeated pain | Problems seen across customers; workarounds as demand signals; Paul Graham's "Do Things that Don't Scale" | List five problems from your field work with evidence of frequency and cost |
| 7.2 Customer development | Interviews for willingness to pay, not compliments; letters of intent; pilots with payment (Steve Blank's customer development) | Run ten customer interviews on one problem; report commitments obtained |
| 7.3 Legal and ethical boundaries | Employment IP assignment, confidentiality and non-solicitation clauses, customers' confidential information; take advice from a lawyer | Write a boundaries checklist for leaving an employer to start a company |
| 7.4 Founder-market fit | Domain knowledge, access to buyers, technical edge; Indian buyers (GCCs, mid-market, government via GeM) | Write a one-page founder-market-fit assessment for yourself |

**Check your understanding:** Why are compliments useless in customer development? What may you never take from an employer or customer? Which Indian buyer segment fits your problem, and how do they buy?

### Chapter 8 · From FDE to founder II: building the company (weeks 11–12)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Services-led start | Selling pilots with implementation; designing the services motion so it can be automated later (a16z's best practices) | Design your first three customer engagements |
| 8.2 Pricing and unit economics | Value metric, pricing model, gross margin path; using your FDE403 models | Build a 24-month model with explicit services and software margins |
| 8.3 First hires and partners | When to hire the first FDE; when to use partners; incentives | Write the job description for your first FDE |
| 8.4 India-specific steps | Company registration, Startup India recognition (DPIIT), GST registration, contracting with enterprises and government | List the steps and documents with official sources |

**Check your understanding:** Why should a founder do the first deployments personally? What must be true before hiring a first FDE? Which margin trend would worry an investor?

### Chapter 9 · Open problems (week 13)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Automating discovery | Can process mining and AI interviews replace parts of discovery? Evidence so far | Propose an experiment to test one claim |
| 9.2 Transfer of evaluation | Do evaluation suites transfer across customers in the same industry? | Design a study using your FDE404 data |
| 9.3 Trust and access | How organisations decide to grant AI and people access; measuring trust | Write a research question and a measurement plan |
| 9.4 Ontology automation | LLM-assisted modelling and entity resolution at enterprise scale | Summarise the state of evidence from your FDE401 labs and recent papers |

**Check your understanding:** Which open problem has the clearest commercial value? Which has the best available data? What would count as a negative result worth publishing?

### Chapter 10 · Proposals (week 14)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Research proposals | Question, contribution, method, data access, ethics approval, timeline | Draft a thesis proposal |
| 10.2 Venture memos | Problem, evidence, solution, market, model, risks, milestones | Draft a venture memo |
| 10.3 Review | Structured peer review and revision | Review two classmates' proposals with a rubric |
| 10.4 Presenting in public | Research talks, demo days and investor pitches; handling hard questions from reviewers and investors | Give a five-minute public talk on your proposal and answer three hostile questions |

**Check your understanding:** What makes a research question answerable in two semesters? What evidence must a venture memo contain to be taken seriously? How do you respond to a review that rejects your core assumption?

## Weekly rhythm

| Week | Chapter | Seminar and lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Seminar: Palantir posts; productisation rubric lab | Rubric scores |
| 2 | 2 | Seminar: a16z and partner ecosystems | Critique essay |
| 3 | 3 | Lab: agent skill for connector scaffolding | — |
| 4 | 3 | Lab: reliability of the scaffolding agent | **P1 due** |
| 5 | 4 | Lab: upgrade orchestrator and per-customer evals | — |
| 6 | 5 | Seminar: field experiments (Brynjolfsson et al.; Dell'Acqua et al.) | Study presentation |
| 7 | 5 | Seminar: METR trial; case study and design science methods | Validity section |
| 8 | 6 | Lab: governance pack | **P2 due** |
| 9 | 7 | Customer-development interviews | — |
| 10 | 7 | Interviews (cont.); boundaries checklist | Interview report |
| 11 | 8 | Lab: 24-month model | — |
| 12 | 8 | Seminar: founder guests or case discussion | — |
| 13 | 9 | Open-problems seminar | Experiment proposal |
| 14 | 10 | Proposal reviews | **P3 due** |
| 15 | Review | Public presentations and oral defence | Final assessment |

## Working with AI in this course

- **Use AI for:** literature search and summarisation (then read the papers); building agentic deployment tools; generating synthetic briefs to test them; financial model code; first drafts of sections you then rewrite.
- **Do without AI (drills):** seminar presentations and critiques; customer-development interviews; validity analyses; the oral defence. Research and investor scrutiny test whether you understand your own claims.
- **Verify AI output by:** checking every citation exists and says what is claimed; re-running agent reliability measurements yourself; recomputing financial models; having a domain expert review any regulatory mapping.
- **Where AI still fails here (show it):** fabricated or misattributed citations in literature summaries; agents that report success on deployment tasks they did not complete (check state, not claims); market-size numbers without sources. Record each with evidence.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Seminar presentations and critiques | 20% |
| Labs | 15% |
| Projects P1–P3 | 45% |
| Public presentation and oral defence | 20% |

**Mastery gate.** You pass when you can: (1) present a productisation decision backed by evidence from at least two deployments and defend it against a panel playing product and customer; (2) report the reliability of an agentic deployment tool with state-based checks and honest failure analysis; (3) submit a thesis proposal accepted by a supervisor or a venture memo rated investable-with-conditions by an external reviewer.

## Industry reality

Deployment roles explicitly include productising field learning (OpenAI, Anthropic, Razorpay postings, 2026). Partner ecosystems are scaling deployment through certification, with large Indian IT firms committing thousands of staff (Anthropic, 2026). Investors publicly debate services-led growth for AI applications (a16z, 2025). Rigorous field evidence on AI at work exists and is mixed by task and experience (NBER w31161; HBS 24-013; METR 2025). Many founders start from a problem they saw repeatedly while working with customers; treat any specific founder story as anecdote unless it is documented.

**Interview questions from this course**

1. *You have built the same connector for three customers. What do you do?* Strong answer: evidence of recurrence and cost, generalisation through configuration, field report to product, ownership and maintenance plan, confidentiality check.
2. *Should our start-up do implementation services?* Strong answer: weighs margin against learning and contract size; services sold at cost with a plan to automate; partner strategy; signals that services are becoming a trap.
3. *How would you measure whether our AI deployment improved productivity?* Strong answer: staggered or randomised rollout, pre-registered metrics, heterogeneity by experience, quality measures, validity threats, cites field studies.
4. *What parts of forward deployed engineering will agents take over first?* Strong answer: integration scaffolding, documentation reading, data mapping, eval generation; reliability limits from time-horizon data; humans keep discovery, access, trust and go-live judgement.
5. *You want to start a company from a problem you saw at a customer. What are the risks?* Strong answer: IP assignment and confidentiality, non-solicitation, customers' confidential practices; validates demand independently; takes legal advice.

## Resources (free first)

- **Primary sources on the model:** Palantir, "Dev versus Delta" — https://blog.palantir.com/dev-versus-delta-demystifying-engineering-roles-at-palantir-ad44c2a6e87 ; Palantir Apollo documentation — https://www.palantir.com/docs/apollo/core/introduction/ ; a16z, "Trading Margin for Moat" — https://a16z.com/services-led-growth/ ; Nabeel Qureshi, "Reflections on Palantir" (2024) — https://nabeelqu.co/reflections-on-palantir
- **Agents and protocols:** MCP specification (2026-07-28) — https://modelcontextprotocol.io/specification/2026-07-28 ; Agent Skills — https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview ; A2A protocol — https://a2a-protocol.org/ ; Anthropic, "Building effective agents" — https://www.anthropic.com/engineering/building-effective-agents ; METR time horizons — https://metr.org/time-horizons/
- **Evidence on AI at work:** Brynjolfsson, Li and Raymond, "Generative AI at Work" (NBER w31161) — https://www.nber.org/papers/w31161 ; Dell'Acqua et al., "Navigating the Jagged Technological Frontier" (HBS 24-013) — https://www.hbs.edu/faculty/Pages/item.aspx?num=64700 ; METR developer productivity trial (Jul 2025) — https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/ ; Anthropic Economic Index (Jan 2026) — https://www.anthropic.com/research/anthropic-economic-index-january-2026-report
- **Research methods:** Runeson and Höst, "Guidelines for conducting and reporting case study research in software engineering", *Empirical Software Engineering* (2009) — https://link.springer.com/article/10.1007/s10664-008-9102-8 ; Hevner, March, Park and Ram, "Design Science in Information Systems Research", *MIS Quarterly* 28(1) (2004)
- **Founding:** Paul Graham, "Do Things that Don't Scale" — https://paulgraham.com/ds.html ; Y Combinator Library — https://www.ycombinator.com/library ; Steve Blank's blog — https://steveblank.com/ ; DPIIT (Startup India recognition) — https://www.dpiit.gov.in/ ; Government e-Marketplace — https://gem.gov.in/
- **Governance:** ISO/IEC 42001 — https://www.iso.org/standard/42001 ; NIST AI RMF — https://www.nist.gov/itl/ai-risk-management-framework ; India AI Governance Guidelines — https://static.pib.gov.in/WriteReadData/specificdocs/documents/2025/nov/doc2025115685601.pdf ; RBI FREE-AI report — https://rbidocs.rbi.org.in/rdocs/PublicationReport/Pdfs/FREEAIR130820250A24FF2D4578453F824C72ED9F5D5851.PDF ; EU AI Act — https://eur-lex.europa.eu/eli/reg/2024/1689/oj

## Sources

- Palantir, "Dev versus Delta" (8 Apr 2019), URL above (checked 2026-10)
- OpenAI, Deployment Lead, FDE (SF) — https://openai.com/careers/deployment-lead-fde-sf-san-francisco/ ; Anthropic, Forward Deployed Engineer, London — https://job-boards.greenhouse.io/anthropic/jobs/5423029008 ; Razorpay, Forward Deployed Engineer (Aug 2026) — https://portfoliojobs.tcv.com/companies/razorpay/jobs/89918935-forward-deployed-engineer (checked 2026-10)
- a16z (4 Jun 2025), URL above; Anthropic, Claude certifications article (2026) — https://claude.com/resources/articles/four-role-based-claude-certifications ; NASSCOM Strategic Review 2026 — https://nasscom.in/knowledge-center/publications/technology-sector-india-strategic-review-2026 (checked 2026-10)
- METR benchmark data v1.1 (Claude Opus 4.6: ≈12 h at 50%, ≈70 min at 80%) — https://metr.org/assets/benchmark_results_1_1.yaml (checked 2026-10)
- Brynjolfsson, Li and Raymond (NBER w31161); Dell'Acqua et al. (HBS Working Paper 24-013, Sep 2023); METR (10 Jul 2025), URLs above (checked 2026-10)

_Last reviewed: 2026-10_
