# FDE301 · The Forward Deployed Engineer: Role, Mindset and Operating Model

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 3 · 5 | 4 (≈ 120 hours) | L1 → L3 | [CS205](../../../../02_year_2_core_computer_science/semester_3/CS205_software_engineering_i_design_testing/README.md), [CS215](../../../../02_year_2_core_computer_science/semester_4/CS215_cloud_and_devops_foundations/README.md); taken with [PRO301](../../../../05_shared_years_3_to_5/PRO301_professional_practice_ethics_law_and_responsible/README.md) | [FDE401](../../year_4/FDE401_data_integration_and_ontology_modeling/README.md), [FDE501](../../year_5/FDE501_frontier_seminar_productizing_field_patterns/README.md), [IND401](../../../../05_shared_years_3_to_5/IND401_industry_co_op_studio/README.md) |

## Why this course matters now

Palantir describes its forward deployed software engineers ("Deltas") as engineers whose focus is "one customer, many capabilities", against a product engineer's "one capability, many customers" (2019). In 2025–26 the model spread to AI companies: OpenAI's FDEs "own discovery, technical scoping, system design, build, and production rollout" and are measured by "production adoption, measurable workflow impact, and eval-driven feedback", Anthropic's FDEs deliver "MCP servers, sub-agents, and agent skills" into customers' production workflows, and Razorpay and Sarvam AI hire FDEs in Bengaluru. AI tools now write integration code, drafts and demos in hours. What they cannot do is decide which problem matters to this customer, earn access to sensitive systems, handle a hostile stakeholder, or judge when a deployment is good enough to go live. This course teaches the role, its economics, its ethics, and the operating habits that make an FDE trusted by the customer and useful to the product team.

## Learning outcomes

By the end you can:

1. **Explain** how the FDE role differs from consulting, sales engineering, solutions architecture, implementation, support and product engineering, using primary sources.
2. **Map** an engagement lifecycle (qualification, discovery, pilot, production, expansion, handover) with entry and exit criteria for each stage.
3. **Design** success metrics for an engagement that separate adoption, workflow impact and product learning from vanity activity.
4. **Decide**, with a written argument, whether a customer need should be built into the core product, built as a reusable extension, or built as a one-off.
5. **Write** a field report that a product team can act on: evidence, frequency, impact, proposed change.
6. **Plan** an operating cadence with a customer (status, escalation, decision log) and keep it for a simulated four-week engagement.
7. **Apply** least-privilege, data minimisation and confidentiality rules to customer data access, and refuse or escalate an unethical request.
8. **Use** AI tools in a customer setting without leaking customer data, and verify what they produce.

## Chapters and lessons

### Chapter 1 · What a forward deployed engineer is (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Dev and Delta | Palantir's split between product engineers and forward deployed engineers; "one customer, many capabilities"; Deltas sit in Business Development and measure success by the customer's goal | Summarise Palantir's 2019 post in 150 words; list three claims you would test with a current FDE |
| 1.2 FDE versus consultant | Palantir's argument: consultants produce "a one-time analysis, recommendation, or solution", Deltas deploy software for a long-term solution; where the line blurs in practice | Rewrite one consulting deliverable (a slide recommendation) as an FDE deliverable (a working system plus a metric) |
| 1.3 The neighbouring roles | Solutions engineer (pre-sale), solutions or applied AI architect, implementation engineer, customer success manager, support engineer, deployment strategist; who owns code, who owns the customer, who owns revenue | Build a RACI for one deployment across the seven roles |
| 1.4 Who hires FDEs in 2026 | Palantir; OpenAI (FDEs by industry, Deployment Leads); Anthropic (Applied AI team); Salesforce (Agentforce FDEs and Deployment Strategists); Sarvam AI and Razorpay in India | Tear down 10 live postings: tasks, travel, years of experience, tools, success measures |
| 1.5 The FDE mindset | Ownership of outcomes, comfort with ambiguity, speed with care, curiosity about the customer's business | Write a one-page "how I work" note for a future customer |

**Check your understanding:** Why does "one customer, many capabilities" create both the role's value and its biggest risk to the product? Which deliverable would a customer pay a consultant for but never pay an FDE for? A posting asks for "5+ years of customer-facing engineering": what does that tell you about what the company cannot train?

### Chapter 2 · History and economics of the model (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Palantir's Echo and Delta | Deployment strategists ("Echos") and Deltas on mixed teams; 4–12 week pilot engagements; pipelines into a customer's ERP as typical early work (Palantir, 2022) | Draw the team composition of a pilot and each person's first-week tasks |
| 2.2 Services-led growth | a16z's "Trading Margin for Moat" (2025): accept lower gross margin to become the "system of work"; sell services at cost; the counterarguments (scalability, commodity signal) | Write a 300-word rebuttal and a 300-word defence of the a16z argument |
| 2.3 Why model companies hire FDEs | Interchangeable models move value to the application and deployment layer; field signal improves models and products (OpenAI and Anthropic postings) | List what a model company learns from a deployment that it cannot learn from API logs |
| 2.4 Unit economics of an engagement | Cost of an FDE-month against contract value; time to first value; expansion revenue; why a pilot that never converts is the most expensive outcome (illustrative numbers only) | Build a spreadsheet model of a 12-month engagement with three conversion scenarios |
| 2.5 Partners and ecosystems | When deployment moves to partners: Claude Partner Network certifications at Indian IT firms; the "leave a trail" principle so partners can repeat your work | Write the handover note a partner would need to repeat one deployment |

**Check your understanding:** Under what conditions does services-led growth become a trap rather than a moat? Why might a company sell implementation at cost? What has to be true about your documentation before a partner can deploy without you?

### Chapter 3 · The engagement lifecycle (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Qualification | Is there a real problem, a sponsor, data access and a decision date? Disqualifying early | Write five qualification questions and the answer that would make you walk away |
| 3.2 Discovery to pilot | Pilot charter, scope, success criteria, kill criteria; why pilots stall ("pilot purgatory") | Draft a one-page pilot charter for an illustrative logistics customer |
| 3.3 Pilot to production | Production readiness: security review, SSO, monitoring, support model, training; OpenAI's "0→1 prototypes through MVP and scale" | Write a production-readiness checklist with an owner per item |
| 3.4 Expansion | Second use case, more users, more data; turning one success into a programme | Map three expansion paths from one deployed workflow |
| 3.5 Handover and exit | Leaving a customer self-sufficient: runbooks, training, support tiers, partner handover | Define measurable handover acceptance criteria |

**Check your understanding:** Which lifecycle stage has the most hidden work, and why? What is the difference between a pilot that failed and a pilot that was never designed to decide anything? When should an FDE recommend ending an engagement?

### Chapter 4 · Success metrics (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Outcome, adoption, activity | Workflow impact versus adoption versus activity (demos given, tickets closed); leading and lagging indicators | Classify 20 metrics from real job postings and engagement reports |
| 4.2 What employers say they measure | OpenAI: production adoption, workflow impact, eval-driven feedback; Deployment Leads: delivery reliability ("milestones hit, low reopen/churn"), operating leverage ("patterns reused across deployments"), product impact | Turn each into a measurable definition with a denominator |
| 4.3 Baselines | Measuring before you change anything; time-and-motion, system logs, sampling | Design a two-week baseline for a document-review workflow |
| 4.4 Attribution | Why "cost went down" may not be your doing; comparison groups; staggered rollouts | Critique an illustrative claim of "40% faster processing" |
| 4.5 Metrics that backfire | Goodhart's law; optimising for pilot count or usage minutes | Name the perverse incentive in three metric designs and fix each |

**Check your understanding:** Why is "number of active users" weak evidence of value in an enterprise tool? What would you measure if the customer has no baseline data? How can an FDE's success metric conflict with the product team's?

### Chapter 5 · The field-to-product loop (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Core, extension or one-off | Palantir's Deltas "frequently need to decide whether to invest time building a feature your customer needs into the core platform, or to create something custom that we can deliver faster" | Write decision memos for three illustrative requests |
| 5.2 Contributing upstream | Deltas contribute code to the core product, coordinated with the product team and its roadmap; review and ownership after merge | Plan an upstream contribution: design note, reviewers, tests, owner |
| 5.3 Field reports | Evidence, frequency across customers, impact, workaround cost, proposed change; Razorpay's rule of writing up anything built for "2+ merchants" | Write a field report from your Chapter 1 posting teardown data |
| 5.4 Fork debt | Customer-specific branches and forks, configuration sprawl, upgrade pain; feature flags and extension points as alternatives | Estimate upgrade cost for a fork that drifts 40 commits a month (illustrative) |
| 5.5 Codifying patterns | Playbooks, templates, reusable connectors and evals (OpenAI: "codify working patterns into tools, playbooks, or building blocks") | Turn one repeated task into a template with instructions |

**Check your understanding:** Why does a customer-specific fork feel cheap in week one and expensive in month twelve? What evidence would convince a product manager to accept your field report? When is a one-off the right call?

### Chapter 6 · Operating model and cadence (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 The pod | FDE, deployment strategist, account executive, customer success, product liaison; incentive alignment (a16z: implementation leads rarely want a quota) | Write a team charter for a four-person pod |
| 6.2 Customer cadence | Weekly status, steering committee, decision log, risk register; Razorpay's posting asks FDEs to acknowledge merchant issues within 2 hours and "never go silent" | Run a mock weekly status meeting from a template |
| 6.3 Internal escalation | When and how to pull in product, security, legal and leadership; writing an escalation that gets read | Write two escalations: one too vague, one actionable |
| 6.4 Prioritising across customers | Several customers, one FDE; triage by impact and commitments; saying no with alternatives | Prioritise 12 illustrative requests across three customers |
| 6.5 Knowledge capture | Engagement wiki, architecture notes, decision records; making yourself replaceable | Set up an engagement repository structure |

**Check your understanding:** What belongs in a decision log that does not belong in meeting notes? How do you escalate without blaming the customer? What breaks when only one person knows how a deployment works?

### Chapter 7 · Working on site (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Travel realities | Anthropic lists 25–50% travel for FDEs; OpenAI's Deployment Lead role lists travel up to 50%; a Palantir Delta describes "a couple of days" a week at customer premises | Plan a sustainable month with two customer sites and one home week |
| 7.2 Why presence matters | a16z: being physically present helps "sort through internal power dynamics and drive adoption"; what you learn from sitting with users | List ten things you can only learn on site |
| 7.3 Access logistics | Badges, customer laptops and virtual desktops, VPNs, background checks, clearances for public-sector work | Write a first-day access checklist |
| 7.4 Professional conduct | Dress and meeting norms, hierarchy, language (English, Hindi and regional languages in Indian deployments), cross-cultural communication | Role-play a first meeting with a senior plant manager |
| 7.5 Sustainability | Context switching, fatigue, boundaries, safety while travelling | Write a personal operating plan with recovery time |

**Check your understanding:** What is lost when an FDE never visits a site? What can a remote FDE do to compensate? Which access problems should be solved before you travel?

### Chapter 8 · Ethics of customer data and trust (weeks 8–9)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Access you hold | Production data, admin rights, personal data; least privilege, need-to-know, time-bound access, logging your own access | Design an access request for a pilot that asks for the minimum |
| 8.2 Law that applies | India's DPDP Act 2023 and Rules 2025 (data fiduciary and processor duties, purpose limitation, 18-month phase-in); contracts: NDA, DPA; sector rules such as RBI's payment data localisation | Map one pilot's data flows to DPDP obligations |
| 8.3 Confidentiality across customers | Never moving one customer's data, code or insight to another; separate environments; what "pattern" may be reused and what may not | Classify ten artefacts as reusable, reusable after abstraction, or never reusable |
| 8.4 Customer data and AI tools | Pasting customer data into a public chatbot as a data breach; approved tools, zero-retention settings, redaction | Write an AI-tool usage policy for a deployment team |
| 8.5 Refusing and escalating | Requests to monitor employees covertly, bypass consent, or hide model errors; ACM Code of Ethics; escalation paths | Analyse three illustrative scenarios; write your response to each |

**Check your understanding:** Why is "the customer gave us admin access" not permission to look at everything? What may you reuse from a deployment, and how do you decide? A sponsor asks you to hide a known error rate from end users: what do you do?

### Chapter 9 · The FDE in the AI era (weeks 10–11)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 What AI does for an FDE | Integration boilerplate, API documentation search, data mapping drafts, test data, demo scaffolding (a16z lists "combing through API documentation" among tasks to automate) | Time yourself building a connector with and without an AI coding agent; log the defects in each |
| 9.2 What FDEs now deliver | MCP servers, sub-agents and agent skills (Anthropic); evals and production AI workflows (OpenAI) | Read the MCP specification overview; list three customer systems you would expose as MCP tools and the permissions each needs |
| 9.3 The AI-leveraged engineer | Coding agents for routine changes, knowledge agents for customer context, triage agents (Razorpay posting); supervising agents | Design an agent-assisted daily workflow with explicit human checkpoints |
| 9.4 Where AI fails in the field | Plausible but wrong integration code, invented API fields, overconfident root-cause guesses, generic customer communication | Collect five AI failures from your own Lab 7 work with evidence |
| 9.5 Why the role grows anyway | Deployment gap: 88% of organisations use AI but agent deployment is in the single digits (AI Index 2026) | Write a two-paragraph argument, with sources, about where FDE demand goes next |

**Check your understanding:** Which FDE tasks get faster with AI, and which get more important because of AI? What must you check before running AI-generated code against a customer system? Why might customers trust a person more than a tool with access?

### Chapter 10 · Careers and the Indian market (week 12)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Ladders | Entry to leadership titles (see the [role page](../../../../06_career_and_market_readiness/01_market_map/roles/FDE_forward_deployed_engineering.md)); what changes at each level | Write the evidence you would need for a promotion to senior FDE |
| 10.2 India | GCCs (2,117 in FY26, Nasscom–Zinnov), IT services firms certifying staff on AI platforms, Indian AI startups and fintechs hiring FDEs | Find five India-based roles that are FDE work under other titles; compare tasks |
| 10.3 Paths out | Product management, solutions architecture, engineering leadership, founding (FDE501, LCH502) | Interview one person in a customer-facing engineering role (with consent) |
| 10.4 Portfolio evidence | Case studies with measured outcomes, anonymised and approved; demo videos; design docs | Draft the outline of your first case study |

**Check your understanding:** Why are pay figures for "FDE" unreliable, and what proxies are better? What makes a case study credible to a hiring manager? Which of your past projects could be rewritten as deployment evidence?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Job-posting teardown | Role comparison table |
| 2 | 2 | Lab 2 · Engagement economics model | — |
| 3 | 3 | Lab 3 · Lifecycle map and pilot charter | **P1 due** |
| 4 | 4 | Lab 4 · Metric design and baseline plan | — |
| 5 | 5 | Lab 5 · Core-versus-custom memos | Field report |
| 6 | 6 | Lab 6 · Cadence simulation (starts four-week engagement) | — |
| 7 | 7 | Lab 6 (cont.) | Mid-term (AI off): case analysis |
| 8 | 8 | Lab 7 · Data-access and AI-tool policy | — |
| 9 | 8 | Lab 8 · Ethics scenarios | Ethics memo |
| 10 | 9 | Lab 9 · AI-assisted versus manual connector | **P2 due** |
| 11 | 9 | Lab 9 (cont.) | AI failure log |
| 12 | 10 | Lab 10 · Practitioner interview | — |
| 13 | Integration | P3 build | Case study draft |
| 14 | Integration | P3 presentations | **P3 due** |
| 15 | Review | Oral defence of P3 | Final exam (AI off) |

## Working with AI in this course

- **Use AI for:** summarising long job postings and engineering blogs (then check every quoted line against the source); drafting status-report and escalation templates; building the engagement economics spreadsheet; generating role-play customer personas for practice, labelled as synthetic.
- **Do without AI (drills):** ethics scenario responses; core-versus-custom decision memos; the mid-term case analysis; your first draft of every field report. Judgement under pressure is what interviews and customers test.
- **Verify AI output by:** opening every source an AI cites about a company's FDE practice and confirming the exact claim; recomputing spreadsheet formulas by hand for one scenario; checking AI-written policies against the DPDP Rules text.
- **Where AI still fails here (show it):** ask an assistant how a named company runs its FDE team and check the answer against primary sources; record invented practices. Ask it to draft a customer escalation and mark every sentence that is generic or that blames the customer.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (10) | 25% |
| Projects P1–P3 | 35% |
| Field report and ethics memo | 10% |
| Mid-term case analysis (AI off) | 10% |
| Final exam (AI off) + oral defence of P3 | 20% |

**Mastery gate.** You pass when you can: (1) given an unfamiliar company's deployment situation in a two-page brief, produce in 90 minutes (AI off) an engagement plan with stages, a success metric with a baseline method, and the three biggest risks; (2) defend a core-versus-custom decision to a panel playing product and customer; (3) respond correctly, in writing, to an ethics scenario involving customer data.

## Industry reality

The role is documented by employers themselves: Palantir's blog posts on Deltas (2019) and Echos (2022), OpenAI's FDE and Deployment Lead postings (with success measures stated), Anthropic's FDE postings (25–50% travel, MCP servers and agent skills as deliverables), Salesforce's Agentforce FDE and Deployment Strategist roles, and Razorpay's merchant-embedded FDE role in Bengaluru. Investors argue about the economics in public (a16z, 2025). How each company evaluates its FDEs internally is not public; treat any claim about it as unconfirmed.

**Interview questions from this course**

1. *What is the difference between an FDE and a consultant?* Strong answer: FDEs deploy and customise software and own a technical outcome over time; consultants often deliver analysis or recommendations; mentions contributing back to the product and the core-versus-custom decision; gives an example.
2. *A customer asks for a feature the product does not have. What do you do?* Strong answer: finds the underlying need first; checks whether existing capabilities solve it; weighs core, extension and one-off with cost and timeline; involves product with evidence; keeps the customer informed of the decision and the date.
3. *How would you measure whether a deployment succeeded?* Strong answer: baseline before change; workflow impact metric with a denominator; adoption by the intended users; a comparison group or staggered rollout; reports uncertainty; separates activity from outcome.
4. *You have admin access to a customer's HR system for an integration. A manager asks you to pull one employee's records. What do you do?* Strong answer: declines; access is for the agreed purpose only; refers the manager to the proper process; documents and escalates internally; cites purpose limitation and contract terms.
5. *Tell me about a time you worked in ambiguity.* Strong answer: concrete situation, the questions asked to reduce ambiguity, a decision made with incomplete information, how it was checked, and what changed afterwards.

## Resources (free first)

- **Primary sources on the role:** Palantir, "Dev versus Delta" — https://blog.palantir.com/dev-versus-delta-demystifying-engineering-roles-at-palantir-ad44c2a6e87 ; Palantir, "A Day in the Life of a Palantir Deployment Strategist" — https://blog.palantir.com/a-day-in-the-life-of-a-palantir-deployment-strategist-951cb59a5a96 ; OpenAI FDE and Deployment Lead postings — https://openai.com/careers/search/?q=forward%20deployed ; Anthropic jobs — https://www.anthropic.com/jobs
- **Economics:** a16z, "Trading Margin for Moat" — https://a16z.com/services-led-growth/ ; Paul Graham, "Do Things that Don't Scale" — https://paulgraham.com/ds.html
- **Ethics and law:** ACM Code of Ethics — https://www.acm.org/code-of-ethics ; DPDP Rules 2025 (PIB) — https://www.pib.gov.in/PressReleasePage.aspx?PRID=2190014 ; RBI, Storage of Payment System Data — https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=11244
- **AI in the field:** Model Context Protocol — https://modelcontextprotocol.io/ ; Anthropic, "Building effective agents" — https://www.anthropic.com/engineering/building-effective-agents
- **Market context:** [FDE role page](../../../../06_career_and_market_readiness/01_market_map/roles/FDE_forward_deployed_engineering.md) ; Stanford AI Index 2026 — https://hai.stanford.edu/assets/files/ai_index_report_2026.pdf

## Sources

- Palantir blog posts (8 Apr 2019; 8 Mar 2022), URLs above (checked 2026-10)
- OpenAI, Forward Deployed Engineer, Tokyo — https://openai.com/careers/forward-deployed-engineer-tokyo/ ; Deployment Lead, FDE, SF — https://openai.com/careers/deployment-lead-fde-sf-san-francisco/ (checked 2026-10)
- Anthropic, Forward Deployed Engineer, London (updated 14 Sep 2026) — https://job-boards.greenhouse.io/anthropic/jobs/5423029008 (checked 2026-10)
- Razorpay, Forward Deployed Engineer (Aug 2026, via TCV job board) — https://portfoliojobs.tcv.com/companies/razorpay/jobs/89918935-forward-deployed-engineer ; Sarvam AI, FDSE — https://careers.kula.ai/sarvam-ai/17986 (checked 2026-10)
- Salesforce careers search, 12 Oct 2026 — https://salesforce.wd12.myworkdayjobs.com/External_Career_Site (checked 2026-10)
- a16z, "Trading Margin for Moat" (4 Jun 2025) — https://a16z.com/services-led-growth/ (checked 2026-10)
- Anthropic, Claude certifications article (2026) — https://claude.com/resources/articles/four-role-based-claude-certifications (checked 2026-10)
- Nasscom–Zinnov GCC report (Jul 2026), via The Tribune — https://www.tribuneindia.com/news/business/india-s-gccs-are-increasingly-leading-the-ai-mandate-for-global-enterprises-driving-global-value-creation-nasscom-zinnov-report/ (checked 2026-10)
- Stanford HAI, AI Index 2026 — https://hai.stanford.edu/assets/files/ai_index_report_2026.pdf (checked 2026-10)

_Last reviewed: 2026-10_
