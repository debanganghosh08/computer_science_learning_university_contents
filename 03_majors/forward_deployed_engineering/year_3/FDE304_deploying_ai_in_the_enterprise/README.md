# FDE304 · Deploying AI in the Enterprise

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 3 · 6 | 4 (≈ 120 hours) | L2 → L3 | [CS205](../../../../02_year_2_core_computer_science/semester_3/CS205_software_engineering_i_design_testing/README.md), [CS215](../../../../02_year_2_core_computer_science/semester_4/CS215_cloud_and_devops_foundations/README.md); assumes [CS214](../../../../02_year_2_core_computer_science/semester_4/CS214_machine_learning_foundations/README.md), [FDE302](../FDE302_customer_discovery_and_requirements_engineering/README.md), [FDE303](../FDE303_rapid_integration_engineering_apis_legacy/README.md); best taken with [AIE305](../../../ai_engineering/year_3/AIE305_evaluating_llm_systems/README.md) | [FDE404](../../year_4/FDE404_field_studio_three_simulated_customer/README.md), [FDE402](../../year_4/FDE402_debugging_and_operating_in_customer_environments/README.md), [FDE403](../../year_4/FDE403_solution_architecture_pricing_and_roi/README.md), [OV12](../../../../04_overlaps/OV12_agent_infrastructure_platform/) |

## Why this course matters now

The Stanford AI Index 2026 reports that 88% of surveyed organisations use AI but that agent deployment is "in the single digits across nearly all business functions". The gap is not model capability. It is everything between a demo and a system that a bank's compliance team approves, a nurse trusts, and a finance director can measure. OpenAI measures its FDEs by "production adoption, measurable workflow impact, and eval-driven feedback", and its Deployment Leads own "readiness and change management for adoption" and "pre-/post-deployment measurement". Public cases show what goes wrong without this work: in Moffatt v. Air Canada (2024) a tribunal held the airline responsible for its chatbot's wrong answer about fares, and Klarna, which reported in February 2024 that its AI assistant did "the equivalent work of 700 full-time agents", said in May 2025 that it would again recruit human agents because cost had been "a too predominant evaluation factor" (as reported). AI tools can now scaffold a retrieval system or an agent in an afternoon. This course teaches the rest: choosing the right use case, evaluating on the customer's own data, passing security and compliance review, keeping humans in the loop where it matters, getting people to change how they work, and proving value honestly. Technical depth on retrieval, agents and evaluation lives in the AI Engineering courses ([AIE303](../../../ai_engineering/year_3/AIE303_retrieval_augmented_generation_and_search/README.md), [AIE304](../../../ai_engineering/year_3/AIE304_tool_use_and_ai_agents_loops_harnesses_memory/README.md), [AIE305](../../../ai_engineering/year_3/AIE305_evaluating_llm_systems/README.md)); this course applies it inside a customer.

## Learning outcomes

By the end you can:

1. **Select** and **rank** AI use cases inside a customer by value, feasibility, data readiness and risk, and **reject** ones that should not use AI.
2. **Design** a deployment architecture on customer data (retrieval with permission sync, tool-using agents, deterministic workflows with model steps) and **choose** where the model runs (vendor API, cloud region, self-hosted).
3. **Build** a customer-specific evaluation set with domain experts, **agree** acceptance thresholds in writing, and **run** it in the customer's environment.
4. **Complete** a security review pack: data-flow diagram, questionnaire answers (SIG or CAIQ style), AI-specific risk answers, and evidence.
5. **Map** a deployment to data protection and sector rules (DPDP Act and Rules, RBI payment data storage and FREE-AI recommendations, CERT-In reporting, EU AI Act where relevant).
6. **Design** human-in-the-loop controls: confidence routing, approvals, audit trails, reversible actions, escalation.
7. **Roll out** in stages (shadow, pilot cohort, canary, general availability) with kill switches and monitoring.
8. **Lead** adoption with a change plan, and **measure** return on investment against a baseline with an honest comparison design.

## Chapters and lessons

### Chapter 1 · Choosing what to deploy (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Task suitability | High-volume, text-heavy, verifiable tasks versus rare, high-stakes, unverifiable ones; where rules or a form beat a model | Score 15 illustrative use cases on volume, verifiability, error cost and data access |
| 1.2 Value hypotheses | Time saved, errors avoided, revenue, risk reduction; who captures the value | Write value hypotheses with a measurable indicator for three use cases |
| 1.3 Risk tiers | Internal assistive versus customer-facing versus autonomous action; harm severity; NIST AI RMF "map" function | Assign risk tiers and minimum controls to your 15 use cases |
| 1.4 Data readiness | Can the model see what it needs, with permission, at the right freshness? | Write a data-readiness checklist and apply it to two use cases |

**Check your understanding:** Why is "summarise all documents" a weak first use case? What makes a task verifiable? When should you recommend not using AI at all?

### Chapter 2 · Architectures on customer data (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Retrieval with permissions | Syncing document ACLs from SharePoint, Google Drive or Confluence; filtering at query time; why a "public index" leaks (depth in AIE303) | Design permission-aware retrieval over two sources with different ACL models |
| 2.2 Agents with tools | Tools over customer systems via MCP or services; narrow tools, approval-gated writes, budgets (depth in AIE304) | Specify tools and permissions for a purchase-order agent |
| 2.3 Workflows first | Deterministic pipelines with model steps (classify, extract, draft) versus open-ended agents; Anthropic's "Building effective agents" guidance | Redesign an agent idea as a workflow and compare failure modes |
| 2.4 Where the model runs | Vendor API, cloud-hosted models in a chosen region, self-hosted open-weight models; latency, cost, residency and control | Write a placement decision for a bank, a hospital and a retailer |
| 2.5 Integration points | Where AI output enters systems of record; write-back with idempotency and audit | Draw the write-back path for an invoice extraction workflow |

**Check your understanding:** How can a retrieval system leak a document a user may not open? Why do enterprises often prefer workflows to open agents in a first deployment? What changes in your design if the model must run on the customer's own servers?

### Chapter 3 · Evaluation on the customer's data (weeks 3–4)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Golden sets with domain experts | Sampling real cases with consent, labelling sessions with the customer's experts, guidelines, agreement | Run a labelling session with a classmate-expert on 60 cases; compute agreement |
| 3.2 Acceptance thresholds | Per-criterion thresholds agreed in writing before launch; severity-weighted errors; what "good enough" means for this customer | Draft an evaluation agreement for a claims-triage assistant |
| 3.3 Evaluating in place | Running evals inside the customer's environment; no data leaves; reproducible harness | Package an eval harness that runs offline from a container |
| 3.4 Regression and change | Re-running evals on prompt, model or data change; vendor model deprecations | Simulate a model swap and decide go or no-go from paired results |
| 3.5 Reliability | Pass@1 versus pass^k for agents; cost per successful task including human review | Report pass^5 and cost per success for a small agent |

**Check your understanding:** Why must thresholds be agreed before results are seen? What does a customer's expert disagreeing with another expert tell you? Why report cost per successful task rather than cost per call?

### Chapter 4 · Security reviews and questionnaires (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 How reviews work | Vendor risk management; questionnaires (Shared Assessments SIG, CSA CAIQ); evidence (SOC 2 Type II, ISO/IEC 27001, penetration test summaries); timelines | Map a review timeline backwards from a go-live date |
| 4.2 Data-flow diagrams | Every data store, processor, sub-processor and region; trust boundaries | Draw the DFD for your Chapter 2 design |
| 4.3 AI-specific questions | Is customer data used for training? Retention and zero-retention options; logging of prompts; model provenance; prompt injection defences (OWASP Top 10 for LLM Applications 2025) | Answer 20 AI-specific questionnaire items for your design, with evidence references |
| 4.4 Threat modelling an AI deployment | Indirect prompt injection through documents and emails, excessive agency, data exfiltration via tools; mitigations | Threat-model the purchase-order agent; list controls and residual risks |
| 4.5 Management systems | ISO/IEC 42001 (AI management system) and NIST AI RMF as what customers' auditors increasingly reference | Map five of your controls to NIST AI RMF functions |

**Check your understanding:** Why do security reviews often take longer than the build, and how do you shorten them? What evidence answers "do you train on our data?" Which OWASP LLM risk grows when you give an agent write tools?

### Chapter 5 · Data residency and regulation (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 India's DPDP regime | DPDP Act 2023 and Rules 2025: notices, consent, purpose limitation, 18-month phased compliance; data fiduciary and processor roles | Write the consent notice and purpose statement for an AI feature |
| 5.2 Financial sector | RBI: payment system data stored only in India (2018); FREE-AI report (Aug 2025) with seven principles, 26 recommendations, board-approved AI policies and disclosure to customers when they deal with AI | Check a bank deployment design against the payment-data rule and three FREE-AI recommendations |
| 5.3 Incident reporting | CERT-In directions (28 Apr 2022): reporting cyber incidents within six hours | Add the reporting step to an incident runbook |
| 5.4 Other regimes | EU AI Act (Regulation (EU) 2024/1689) risk categories; GDPR transfers; US health data (HIPAA business associate agreements) | Classify three deployments under the EU AI Act categories |
| 5.5 Residency in practice | Model region, vector store region, logs and backups, support access from abroad | Produce a residency matrix for every data copy in your design |

**Check your understanding:** Where do copies of customer data hide in an AI system? Why does a support engineer's remote access count for residency? Which FREE-AI recommendation most changes a bank chatbot's design?

### Chapter 6 · Guardrails and human-in-the-loop (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Where humans stay | Approval before irreversible or external actions; review sampling; four-eyes rules in regulated work | Mark human checkpoints in three workflows and justify each |
| 6.2 Confidence routing | Routing by model confidence, rules and uncertainty signals; calibration checks | Route 200 extraction results; measure errors that slipped past review |
| 6.3 Output controls | Grounding and citations, refusal behaviour, input and output filters, policy checks | Add grounding checks to a policy-answering assistant and measure unsupported claims |
| 6.4 Liability lessons | Moffatt v. Air Canada: the company is responsible for what its chatbot says | Write the disclosure and escalation design for a customer-facing assistant |
| 6.5 Audit trails | Who asked, what the model saw, what it produced, who approved | Implement an audit log and reconstruct one decision from it |

**Check your understanding:** Why does human review fail when 98% of cases are correct? What makes an action reversible? What must an audit trail contain to settle a dispute?

### Chapter 7 · Rollout (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Shadow mode | Running AI alongside the current process without acting; comparing outputs | Run a shadow comparison on 300 historical cases |
| 7.2 Pilot cohorts and canaries | Choosing pilot users; feature flags; staged exposure; kill switches | Write a staged rollout plan with exit criteria per stage |
| 7.3 Monitoring | Traces, sampled online evaluation, drift in inputs, cost and latency budgets, user feedback | Define monitoring dashboards and alert thresholds |
| 7.4 Fallbacks | Model or provider outage, degraded mode, manual process | Test a provider outage and confirm the manual path works |

**Check your understanding:** Why can shadow mode overestimate production quality? What should trigger the kill switch? What does users' silence tell you during a pilot?

### Chapter 8 · Change management and adoption (weeks 9–10)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Why tools go unused | Workflow fit, trust, incentives, fear for jobs, extra steps | List adoption risks for three deployments from your discovery notes |
| 8.2 Change models | Prosci ADKAR (awareness, desire, knowledge, ability, reinforcement); Kotter's eight steps; use them as checklists | Write an ADKAR plan for a claims team |
| 8.3 Champions and training | Champions network, role-based training, office hours, quick reference guides in local languages | Build a 30-minute training session and run it with classmates |
| 8.4 Redesigning work | Changing targets, roles and approvals so the tool fits; involving staff representatives | Redesign one role's daily workflow with the AI step included |
| 8.5 Adoption metrics | Active use by intended users, task coverage, override rates, edits to AI drafts | Define four adoption metrics with denominators |

**Check your understanding:** Why can a deployment with high accuracy still fail? What does a rising override rate mean? Who should own adoption after the FDE leaves?

### Chapter 9 · Measuring return on investment (weeks 11–12)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Baselines | Time-and-motion samples, system timestamps, error audits before go-live | Design and run a baseline on a simulated workload |
| 9.2 Comparison designs | A/B by team or region, stepped-wedge rollout, difference-in-differences; why before/after alone misleads | Analyse an illustrative stepped-wedge dataset |
| 9.3 Full cost | Model and infrastructure, integration, human review time, support, change management, FDE time | Build a full-cost model for one deployment |
| 9.4 Quality-adjusted results | Throughput with error rates, rework and complaints; the Klarna lesson about cost-led evaluation | Compute quality-adjusted productivity for two scenarios |
| 9.5 Reporting to executives | Value cases with ranges and assumptions; what you do not know | Write a one-page ROI readout with confidence ranges |

**Check your understanding:** Why does a before/after comparison overstate gains during a period of growth? What costs are most often left out of AI ROI claims? How would you report a result that is positive but uncertain?

### Chapter 10 · Operating and handing over (weeks 13–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Service levels for AI | Quality, latency and availability objectives; ownership of each | Draft service-level objectives for the deployment |
| 10.2 Change control | Prompt, model, retrieval and data changes go through eval gates | Write a change process and run one change through it |
| 10.3 Vendor model changes | Deprecations and silent behaviour shifts; pinning versions; re-evaluation | Plan a model migration with a rollback |
| 10.4 Handover | Runbooks, owner training, support tiers, eval suite ownership | Hand over to a classmate team that must operate it for a week |

**Check your understanding:** Who owns the eval suite after handover, and why does it matter? What should happen when the vendor retires your model? What does a customer need to run the system without you?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Use-case scoring | Ranked use cases |
| 2 | 2 | Lab 2 · Architecture and placement | Architecture note |
| 3 | 3 | Lab 3 · Expert labelling session | — |
| 4 | 3 | Lab 3 (cont.): eval agreement and offline harness | **P1 due** |
| 5 | 4 | Lab 4 · Security review pack | — |
| 6 | 5 | Lab 5 · Residency and regulation matrix | — |
| 7 | 6 | Lab 6 · Confidence routing and audit | Mid-term (AI off): review and regulation case |
| 8 | 7 | Lab 7 · Shadow mode and rollout plan | — |
| 9 | 8 | Lab 8 · Change plan and training | — |
| 10 | 8 | Lab 8 (cont.) | **P2 due** |
| 11 | 9 | Lab 9 · Baseline and comparison design | — |
| 12 | 9 | Lab 9 (cont.): ROI model | ROI readout |
| 13 | 10 | Lab 10 · Change control and handover | — |
| 14 | Integration | P3 demo to a simulated steering committee | **P3 due** |
| 15 | Review | Oral defence of P3 | Final exam (AI off) |

## Working with AI in this course

- **Use AI for:** building prototypes and eval harnesses (Claude Code, Codex, Copilot); drafting questionnaire answers from your own architecture documents; generating adversarial test inputs; drafting training material that you then check with users.
- **Do without AI (drills):** use-case ranking and risk tiering; threat models; regulatory mapping; the ROI comparison design; the mid-term and final. These are judgement calls a customer holds you accountable for.
- **Verify AI output by:** checking every questionnaire answer against an actual control and evidence item (an unsupported "yes" is a contractual risk); calibrating any LLM judge against expert labels before using it in acceptance decisions; recomputing ROI numbers independently; reading regulation text rather than summaries.
- **Where AI still fails here (show it):** AI-drafted security answers that claim controls the system does not have; synthetic test cases easier than real ones; judges that reward fluent but wrong answers. Record at least one example of each in Labs 3–4.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (10) | 25% |
| Projects P1–P3 | 40% |
| Security review pack and residency matrix | 10% |
| Mid-term (AI off) | 10% |
| Final exam (AI off) + P3 defence | 15% |

**Mastery gate.** You pass when you can: (1) take an unfamiliar customer brief and, in one day, rank use cases, design the deployment with model placement, and write an evaluation agreement with thresholds; (2) produce a security review pack whose every claim is backed by a control or evidence item, and defend it to a panel playing the customer's CISO; (3) design a comparison that would credibly measure the deployment's value, and explain its weaknesses.

## Industry reality

Model companies and software vendors staff deployment teams for exactly this work: OpenAI's FDEs and Deployment Leads, Anthropic's FDEs and India-based Applied AI Architects who help customers "develop evaluation frameworks", Salesforce's Agentforce FDEs and Deployment Strategists. Regulators are setting expectations: the RBI's FREE-AI report (2025) for financial institutions, India's AI Governance Guidelines (November 2025), NIST's AI RMF and Generative AI Profile, ISO/IEC 42001, and the EU AI Act. Public failures (Air Canada's chatbot) and public reversals (Klarna's return to human agents) are now part of enterprise buyers' risk discussions.

**Interview questions from this course**

1. *A bank wants a customer-service assistant. Walk me through deployment.* Strong answer: use-case scoping and risk tier; data and residency (RBI rules); architecture with retrieval over approved content; evaluation with the bank's experts and thresholds; disclosure that customers are dealing with AI and escalation to humans (FREE-AI); staged rollout; monitoring; ROI design.
2. *The customer's security team asks if their data trains your model. How do you answer?* Strong answer: answers precisely from the contract and provider settings; describes retention, logging and sub-processors; provides evidence; never guesses; escalates if unsure.
3. *Your pilot hit 92% accuracy but nobody uses it. What now?* Strong answer: investigates workflow fit, trust and incentives; looks at override and edit data; interviews users; redesigns the step or the process; reconsiders the metric.
4. *How would you prove the deployment saved money?* Strong answer: baseline before go-live; comparison group or staggered rollout; full cost including human review and support; quality-adjusted outcomes; confidence ranges; independent recomputation.
5. *An agent will update records in the customer's ERP. What controls do you add?* Strong answer: narrow tools, least-privilege service account, approval for writes above a threshold, idempotency, audit log, rate limits, kill switch, prompt injection defences on inputs, regression evals.

## Resources (free first)

- **AI engineering depth (this university):** [AIE303 RAG](../../../ai_engineering/year_3/AIE303_retrieval_augmented_generation_and_search/README.md), [AIE304 Agents](../../../ai_engineering/year_3/AIE304_tool_use_and_ai_agents_loops_harnesses_memory/README.md), [AIE305 Evaluating LLM Systems](../../../ai_engineering/year_3/AIE305_evaluating_llm_systems/README.md), [AIE403 LLMOps](../../../ai_engineering/year_4/AIE403_llmops_observability_guardrails_cost_and_latency/README.md)
- **Practitioner guides:** Anthropic, "Building effective agents" — https://www.anthropic.com/engineering/building-effective-agents ; OpenAI, "A practical guide to building agents" — https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf ; Hamel Husain, "Your AI Product Needs Evals" — https://hamel.dev/blog/posts/evals/
- **Risk and security:** OWASP Top 10 for LLM Applications 2025 — https://genai.owasp.org/llm-top-10/ ; NIST AI RMF — https://www.nist.gov/itl/ai-risk-management-framework ; ISO/IEC 42001 — https://www.iso.org/standard/42001 ; CSA Cloud Controls Matrix and CAIQ — https://cloudsecurityalliance.org/research/cloud-controls-matrix ; Shared Assessments SIG — https://sharedassessments.org/sig/
- **Law and regulation (India and global):** DPDP Rules 2025 (PIB) — https://www.pib.gov.in/PressReleasePage.aspx?PRID=2190014 ; RBI, Storage of Payment System Data — https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=11244 ; RBI FREE-AI report — https://rbidocs.rbi.org.in/rdocs/PublicationReport/Pdfs/FREEAIR130820250A24FF2D4578453F824C72ED9F5D5851.PDF ; CERT-In directions — https://www.cert-in.org.in/Directions70B.jsp ; India AI Governance Guidelines (Nov 2025) — https://static.pib.gov.in/WriteReadData/specificdocs/documents/2025/nov/doc2025115685601.pdf ; EU AI Act — https://eur-lex.europa.eu/eli/reg/2024/1689/oj
- **Change management:** Prosci ADKAR — https://www.prosci.com/methodology/adkar ; Kotter's 8 steps — https://www.kotterinc.com/methodology/8-steps/

## Sources

- Stanford HAI, AI Index 2026 — https://hai.stanford.edu/assets/files/ai_index_report_2026.pdf (checked 2026-10)
- OpenAI, FDE (Tokyo) and Deployment Lead (SF) postings — https://openai.com/careers/forward-deployed-engineer-tokyo/ ; https://openai.com/careers/deployment-lead-fde-sf-san-francisco/ (checked 2026-10)
- Anthropic, Applied AI Architect, Bangalore — https://job-boards.greenhouse.io/anthropic/jobs/5390746008 (checked 2026-10)
- Klarna, "Klarna AI assistant handles two-thirds of customer service chats in its first month" (27 Feb 2024) — https://www.klarna.com/international/press/klarna-ai-assistant-handles-two-thirds-of-customer-service-chats-in-its-first-month/ ; Entrepreneur, reporting the CEO's Bloomberg interview (May 2025) — https://www.entrepreneur.com/business-news/klarna-ceo-reverses-course-by-hiring-more-humans-not-ai/491396 (checked 2026-10)
- CTV News on Moffatt v. Air Canada (Feb 2024) — https://www.ctvnews.ca/vancouver/article/air-canadas-chatbot-gave-a-bc-man-the-wrong-information-now-the-airline-has-to-pay-for-the-mistake/ (checked 2026-10)
- RBI FREE-AI Committee report and press release (13 Aug 2025), URL above; PIB DPDP Rules release, URL above; CERT-In directions (28 Apr 2022), URL above (checked 2026-10)

_Last reviewed: 2026-10_
