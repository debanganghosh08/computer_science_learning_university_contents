# FDE403 · Solution Architecture, Pricing and ROI

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 4 · 8 | 4 (≈ 120 hours) | L2 → L4 | [FDE303](../../year_3/FDE303_rapid_integration_engineering_apis_legacy/README.md); assumes [FDE304](../../year_3/FDE304_deploying_ai_in_the_enterprise/README.md), [FDE305](../../year_3/FDE305_technical_communication_in_the_field_demos/README.md), [CS215](../../../../02_year_2_core_computer_science/semester_4/CS215_cloud_and_devops_foundations/README.md), [FND116](../../../../01_year_1_foundations/semester_2/FND116_probability_and_statistics_i/README.md) | [FDE501](../../year_5/FDE501_frontier_seminar_productizing_field_patterns/README.md), [LCH502](../../../../05_shared_years_3_to_5/LCH502_career_launch_and_founder_studio/README.md), [CAR401](../../../../05_shared_years_3_to_5/CAR401_career_lab_ii_interviews_system_design_and_ai/README.md) |

## Why this course matters now

Senior forward deployed engineers, solutions architects and deployment leads are judged on whether a deployment is worth paying for, not only on whether it works. OpenAI's Deployment Leads "own value cases and ROI" and report pre- and post-deployment measurement to executive sponsors. Pricing for AI products is moving from seats to usage and outcomes: Intercom lists its Fin AI agent at $0.99 per outcome, and Salesforce offers Agentforce at $2 per conversation, through Flex Credits sold at $500 per 100,000 credits and charged per action, or through per-user licences (pricing pages, October 2026). In India, NASSCOM reports providers moving "away from FTE delivery to outcome-based, risk-sharing constructs" (2026). An analysis of AI start-ups argues for selling implementation services at cost to win larger contracts (a16z, 2025). AI tools now draft architecture diagrams, cost spreadsheets and proposal text quickly. They do not know the customer's procurement rules, which costs are hidden in human review, or what happens to an outcome-priced contract when nobody agrees what counts as an outcome. This course teaches you to design a solution, cost it fully, price it sensibly, build an honest business case, and get it through procurement and security review.

## Learning outcomes

By the end you can:

1. **Design** a solution architecture from requirements, with options, trade-offs, and decisions recorded, against a framework such as AWS Well-Architected.
2. **Apply** reference architectures for common AI deployments (retrieval assistants, document pipelines, agents with tools, voice and messaging channels) and **adapt** them to constraints.
3. **Decide** build versus buy versus partner with a weighted, evidence-based analysis that includes exit costs.
4. **Model** total cost of ownership: model usage, infrastructure, integration, human review, support, change management and people, with sensitivity analysis.
5. **Compare** seat, usage, outcome and hybrid pricing, and **design** a value metric that customers can verify.
6. **Build** an ROI and business case (NPV, payback, ranges) from a measured baseline, and **defend** its assumptions.
7. **Navigate** procurement (RFI, RFP, MSA, SOW, DPA, SLA; India's Government e-Marketplace for public buyers) and **plan** a security review timeline.
8. **Write** a statement of work with assumptions, acceptance criteria and change control that protects both sides.

## Chapters and lessons

### Chapter 1 · Solution architecture practice (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 From requirements to options | Functional and non-functional requirements drive options; at least three options per major decision | Produce three architecture options for an illustrative insurer's claims assistant |
| 1.2 Frameworks | AWS Well-Architected pillars (operational excellence, security, reliability, performance efficiency, cost optimisation, sustainability) and its Generative AI Lens; Azure and Google Cloud architecture centres | Review one option against the Generative AI Lens; list findings |
| 1.3 Decisions and records | Architecture decision records; reversible versus irreversible decisions | Write ADRs for the three most expensive decisions |
| 1.4 Architecture reviews with customers | Presenting to enterprise architecture boards; standards they enforce | Run a mock architecture board review |

**Check your understanding:** Why present options rather than a single design? Which decisions deserve the most analysis? What does an enterprise architecture board care about that your team may not?

### Chapter 2 · Reference architectures for AI deployments (weeks 2–3)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Retrieval assistants | Ingestion, permissions, retrieval, generation, evaluation, monitoring; latency and cost budgets | Draw a reference architecture with budgets per component |
| 2.2 Document pipelines | Batch extraction, validation, human review queues, write-back | Size a pipeline for 50,000 documents a day |
| 2.3 Agents with tools | Tool layer (MCP or services), approvals, durable execution, audit | Adapt an agent reference architecture to a bank's change-control rules |
| 2.4 Channels | Web, email, voice and messaging (WhatsApp is a common customer channel in India); latency and compliance per channel | Add a messaging channel to a design; list new risks |
| 2.5 Deployment models | Multi-tenant SaaS, single-tenant, customer's cloud account ("bring your own cloud"), on-premises; effect on cost and support | Compare four deployment models for one customer |

**Check your understanding:** Where does latency accumulate in a voice assistant? Why does a single-tenant deployment change your support costs? What must change in a reference architecture for a regulated bank?

### Chapter 3 · Build, buy or partner (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Criteria | Differentiation, time to value, capability, total cost, risk, lock-in, exit cost | Build a weighted decision matrix with sensitivity to weights |
| 3.2 Lock-in and exit | Data portability, model portability, contract terms, switching costs | Estimate the exit cost of two vendor choices |
| 3.3 Open-weight versus API models | Control, cost at scale, operations burden, quality gap | Compute the break-even volume for self-hosting under stated assumptions |
| 3.4 Partners | Systems integrators and certified partners (for example, Indian IT firms certifying staff on AI platforms); when partners lower or raise risk | Write a partner-selection checklist |

**Check your understanding:** Why does a weighted matrix need a sensitivity check? What hidden cost appears when you self-host a model? When is a partner the better choice than your own FDEs?

### Chapter 4 · Total cost of ownership (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Cost components | Model tokens or GPU hours, infrastructure, storage, integration build, human review time, support, training, change management, FDE time | List every cost for your FDE304 deployment |
| 4.2 Unit economics | Cost per document, per conversation, per successful task; why cost per success beats cost per call | Compute cost per successful task including review and retries |
| 4.3 Sensitivity | Tornado charts; which assumptions move the answer most | Build a sensitivity analysis with five drivers |
| 4.4 Cloud cost practice | FinOps Foundation framework; FOCUS billing data specification; tagging for allocation | Tag a deployment's resources and produce a cost allocation report |

**Check your understanding:** Why do AI cost estimates that ignore review time mislead? Which cost driver usually dominates at scale? How would you allocate shared infrastructure cost across customers?

### Chapter 5 · Pricing models (weeks 6–7)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Seats | Per-user pricing; predictability; why it fits poorly when AI replaces work | Model revenue under seat pricing as AI reduces seats needed |
| 5.2 Usage | Per call, per token, per action, credits (Salesforce Flex Credits); predictability problems for buyers | Design a usage price with a monthly cap and alerts |
| 5.3 Outcomes | Per resolution or per outcome (Intercom Fin at $0.99 per outcome); defining and auditing an outcome; disputes | Write an outcome definition that both sides can verify from logs |
| 5.4 Hybrid and services | Platform fee plus usage; implementation services priced at cost (a16z); outcome-based, risk-sharing contracts in Indian IT services (NASSCOM) | Design a hybrid price for an illustrative logistics customer |
| 5.5 Value metrics | Price tied to what the customer values and can measure; avoiding perverse incentives | Pick and defend a value metric for three products |
| 5.6 Indian market realities | Price sensitivity, GST on software services, procurement by lowest bid in some public tenders; rupee pricing | Adapt a global price sheet for an Indian mid-market buyer (illustrative) |

**Check your understanding:** What perverse incentive does per-conversation pricing create? Why must an outcome be auditable by the customer? When does outcome pricing transfer too much risk to the vendor?

### Chapter 6 · ROI and business cases (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Financial basics | Net present value, payback period, internal rate of return, discount rates (Damodaran's free materials) | Compute NPV and payback for three scenarios |
| 6.2 Benefits | Measured baseline, quality-adjusted benefits, who captures them, when they arrive | Build a benefits model from your FDE304 baseline |
| 6.3 Ranges and assumptions | Low, expected and high cases; assumption registers; Monte Carlo for key drivers | Run a Monte Carlo on three drivers; report a range |
| 6.4 Honest cases | The Klarna example: headline savings in 2024 and a 2025 return to human agents because cost had been "a too predominant evaluation factor" (as reported) | Rewrite an overclaiming business case honestly |
| 6.5 Benefits realisation | Tracking actual benefits after go-live; who owns them | Design a benefits-tracking plan for 12 months |

**Check your understanding:** Why is payback period popular with buyers despite its flaws? How do you present a benefit that depends on staff being redeployed? What makes a business case credible to a CFO?

### Chapter 7 · Procurement (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Buying processes | RFI, RFP, RFQ; evaluation criteria; proof-of-concept clauses | Respond to a short illustrative RFP section |
| 7.2 Contract documents | Master services agreement, statement of work, order form, data processing agreement, service-level agreement | Map which document holds each commitment |
| 7.3 Public procurement in India | Government e-Marketplace (GeM) for government buyers; tender rules; empanelment | Read GeM's seller guidance and list steps to sell a software service |
| 7.4 Timelines | Legal, security and finance reviews in parallel; procurement calendars and fiscal-year timing | Build a procurement timeline backwards from a go-live date |

**Check your understanding:** Why should acceptance criteria live in the SOW, not in an email? What slows public procurement, and how do you plan for it? Which review is usually on the critical path?

### Chapter 8 · Security review cycles (week 10)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Vendor risk management | Tiers of review by data sensitivity; standard questionnaires (SIG, CAIQ); evidence (SOC 2 Type II, ISO/IEC 27001, penetration test summaries) | Plan the review for a high-sensitivity deployment |
| 8.2 Running reviews in parallel | Starting early, reusable answer libraries, trust portals | Build a reusable answer library from your FDE304 pack |
| 8.3 Remediation plans | Committing to fixes with dates; compensating controls | Write a remediation plan for three findings |
| 8.4 AI governance reviews | Model risk questions, ISO/IEC 42001, NIST AI RMF, RBI FREE-AI recommendations for banks | Answer a bank's AI governance questionnaire (illustrative) |

**Check your understanding:** Why do answer libraries go stale, and how do you prevent it? When is a compensating control acceptable? What extra questions does an AI deployment trigger?

### Chapter 9 · Statements of work and proposals (week 11)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 SOW structure | Scope, deliverables, assumptions, dependencies on the customer, acceptance criteria, timeline, change control | Write a SOW for a six-week pilot |
| 9.2 Assumptions that protect | Data access dates, customer staff availability, environment readiness | Add ten assumptions and the consequence if each fails |
| 9.3 Change control | Change requests with impact on time and cost | Process two change requests against your SOW |
| 9.4 Proposals | Executive summary, solution, plan, team, pricing, risks; tailored to evaluation criteria | Write a ten-page proposal for an illustrative RFP |

**Check your understanding:** Why are customer dependencies the most common cause of SOW disputes? What makes an acceptance criterion contract-grade? How do you price uncertainty in a pilot?

### Chapter 10 · Architecture for scale and many customers (weeks 12–13)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 From one customer to many | Configuration over code, tenant isolation, per-tenant cost tracking | Refactor a single-customer design for ten customers |
| 10.2 Sovereign and regional deployments | Data residency (DPDP, RBI payment data storage), regional clouds, customer-managed keys | Design a regional deployment for Indian and EU customers |
| 10.3 Margin at scale | Gross margin of AI products; services margin; when automation of deployment changes economics | Model gross margin as deployment effort falls |
| 10.4 Field CTO judgement | Saying no to unprofitable deals; designing offers that scale | Write a deal review memo recommending against an illustrative deal |

**Check your understanding:** What makes a customer-specific design expensive at scale? Why do customer-managed keys change your operations? When should you walk away from a deal?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Options and ADRs | — |
| 2 | 2 | Lab 2 · Reference architectures with budgets | — |
| 3 | 2 | Lab 2 (cont.): deployment models | **P1 due** |
| 4 | 3 | Lab 3 · Build-buy-partner matrix | — |
| 5 | 4 | Lab 4 · TCO and unit economics | — |
| 6 | 5 | Lab 5 · Pricing designs | — |
| 7 | 5 | Lab 5 (cont.): outcome definitions | Mid-term (AI off): costing and pricing case |
| 8 | 6 | Lab 6 · NPV, ranges and Monte Carlo | — |
| 9 | 7 | Lab 7 · RFP response and procurement timeline | **P2 due** |
| 10 | 8 | Lab 8 · Security review plan and answer library | — |
| 11 | 9 | Lab 9 · SOW and change control | — |
| 12 | 10 | Lab 10 · Multi-customer refactor | — |
| 13 | 10 | P3 preparation | Deal review memo |
| 14 | Integration | P3 panel defence | **P3 due** |
| 15 | Review | Final exam | Final exam (AI off) |

## Working with AI in this course

- **Use AI for:** drafting architecture options and diagrams for you to critique, building spreadsheet formulas and Monte Carlo code, summarising RFP documents, generating first drafts of proposal sections from your notes, checking a SOW for missing standard clauses.
- **Do without AI (drills):** the mid-term costing and pricing case; NPV and payback by hand; outcome definitions; deal review memos; the final exam.
- **Verify AI output by:** recomputing every financial figure independently; checking prices against vendors' current pricing pages with dates; reading contract clauses with a legal reviewer (instructor or mentor) rather than trusting summaries; testing outcome definitions against real or simulated logs.
- **Where AI still fails here (show it):** out-of-date vendor prices stated as current, ROI cases that omit review and change-management costs, and invented procurement rules. Log one example of each from your labs.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (10) | 25% |
| Projects P1–P3 | 40% |
| Mid-term (AI off) | 10% |
| Final exam (AI off) + P3 panel defence | 25% |

**Mastery gate.** You pass when you can: (1) from an unfamiliar RFP and customer brief, produce in one day an architecture with options and ADRs, a full TCO with sensitivity, and a priced offer; (2) defend a business case with ranges and named assumptions before a panel playing CFO, CISO and procurement, and change it correctly when an assumption is challenged; (3) write an outcome-pricing definition that both sides can verify from logs.

## Industry reality

Value and ROI are explicit parts of deployment roles (OpenAI's Deployment Lead posting). Vendors publish usage and outcome pricing for AI agents (Intercom, Salesforce, October 2026). Indian IT services firms report a shift to outcome-based, risk-sharing contracts (NASSCOM 2026). Cloud providers publish architecture frameworks and reference architectures; the FinOps Foundation maintains cost-management practices and the FOCUS billing specification. Government buyers in India purchase through the Government e-Marketplace. Anthropic's professional-level architect certification covers "integration architecture, governance, and evaluation" for large enterprises.

**Interview questions from this course**

1. *Design and price an AI assistant for a 2,000-agent contact centre.* Strong answer: options and reference architecture; TCO including review and support; unit cost per resolved conversation; pricing options (seat, usage, outcome, hybrid) with risks; value metric; pilot with baseline.
2. *Should the customer self-host an open-weight model?* Strong answer: break-even volume, quality gap from their own evals, operations burden, residency and control needs, exit costs; recommends with a sensitivity range.
3. *Our outcome-based contract is in dispute. What went wrong and how do you fix it?* Strong answer: outcome definition not auditable or not agreed; attribution unclear; proposes a log-based definition, an audit process, caps and floors, and a renegotiation path.
4. *Build a business case the CFO will trust.* Strong answer: measured baseline, full costs, quality-adjusted benefits, ranges, named assumptions with owners, benefits-tracking plan; avoids headline-only savings.
5. *Procurement says the deal will take six months. How do you shorten it?* Strong answer: maps reviews and runs them in parallel; reusable security answers and evidence; standard contract templates; early legal engagement; scopes a pilot under procurement thresholds where allowed.

## Resources (free first)

- **Architecture:** AWS Well-Architected Framework — https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html ; Generative AI Lens — https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/generative-ai-lens.html ; Azure Architecture Center — https://learn.microsoft.com/en-us/azure/architecture/ ; Google Cloud Architecture Center — https://cloud.google.com/architecture ; ADRs — https://adr.github.io/ ; C4 model — https://c4model.com/
- **Cost and finance:** FinOps Foundation framework — https://www.finops.org/framework/ ; FOCUS specification — https://focus.finops.org/ ; Aswath Damodaran's free valuation materials — https://pages.stern.nyu.edu/~adamodar/
- **Pricing examples (check current pages):** Intercom pricing — https://www.intercom.com/pricing ; Salesforce Agentforce pricing — https://www.salesforce.com/agentforce/pricing/
- **Procurement and review:** Government e-Marketplace — https://gem.gov.in/ ; Shared Assessments SIG — https://sharedassessments.org/sig/ ; CSA Cloud Controls Matrix — https://cloudsecurityalliance.org/research/cloud-controls-matrix ; ISO/IEC 27001 — https://www.iso.org/standard/27001 ; ISO/IEC 42001 — https://www.iso.org/standard/42001
- **Paid, optional:** Madhavan Ramanujam and Georg Tacke, *Monetizing Innovation* (2016); Mark Richards and Neal Ford, *Fundamentals of Software Architecture* (2nd ed., 2025).

## Sources

- OpenAI, Deployment Lead, FDE (SF) — https://openai.com/careers/deployment-lead-fde-sf-san-francisco/ (checked 2026-10)
- Intercom pricing page (Fin AI Agent $0.99 per outcome) — https://www.intercom.com/pricing ; Salesforce Agentforce pricing page ($2 per conversation; Flex Credits $500 per 100,000 credits; per-user licensing) — https://www.salesforce.com/agentforce/pricing/ (checked 2026-10-12)
- NASSCOM Strategic Review 2026 — https://nasscom.in/knowledge-center/publications/technology-sector-india-strategic-review-2026 (checked 2026-10)
- a16z, "Trading Margin for Moat" (4 Jun 2025) — https://a16z.com/services-led-growth/ (checked 2026-10)
- Klarna press release (27 Feb 2024) — https://www.klarna.com/international/press/klarna-ai-assistant-handles-two-thirds-of-customer-service-chats-in-its-first-month/ ; Entrepreneur (May 2025) — https://www.entrepreneur.com/business-news/klarna-ceo-reverses-course-by-hiring-more-humans-not-ai/491396 (checked 2026-10)
- Anthropic, Claude certifications article (2026) — https://claude.com/resources/articles/four-role-based-claude-certifications (checked 2026-10)

_Last reviewed: 2026-10_
