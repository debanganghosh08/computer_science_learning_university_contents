# FDE404 · Field Studio: Three Simulated Customer Deployments

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 4 · 8 | 4 (≈ 120 hours) | L3 → L4 | [FDE304](../../year_3/FDE304_deploying_ai_in_the_enterprise/README.md); assumes [FDE302](../../year_3/FDE302_customer_discovery_and_requirements_engineering/README.md), [FDE303](../../year_3/FDE303_rapid_integration_engineering_apis_legacy/README.md), [FDE305](../../year_3/FDE305_technical_communication_in_the_field_demos/README.md), [FDE401](../FDE401_data_integration_and_ontology_modeling/README.md), [FDE402](../FDE402_debugging_and_operating_in_customer_environments/README.md) | [THS501](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md), [CAR401](../../../../05_shared_years_3_to_5/CAR401_career_lab_ii_interviews_system_design_and_ai/README.md), [LCH502](../../../../05_shared_years_3_to_5/LCH502_career_launch_and_founder_studio/README.md), [FDE501](../../year_5/FDE501_frontier_seminar_productizing_field_patterns/README.md) |

## Why this course matters now

Forward deployed work is learned by doing deployments, and employers hire on evidence of deployments done. Palantir describes deployment strategists working on "4–12 week pilot engagements" across industries (2022); OpenAI's FDEs "own technical delivery across multiple deployments from first prototype to stable production"; Anthropic's FDEs "travel frequently (25-50%) to customer sites to build in person". This studio compresses that experience into one semester: three end-to-end deployments for three simulated customers in three industries (a hospital, a logistics company and a bank; all illustrative), each with discovery, integration, an AI workflow, evaluation, security review, a demo to decision-makers and a handover. The customers are played by instructors, industry mentors and classmates working from confidential briefs that include hidden constraints, changing priorities and injected incidents. AI coding agents are allowed and expected for building; they make each build faster, which leaves more of the grade on what AI cannot do for you: finding the real problem, earning trust, deciding what is good enough, and leaving the customer able to run the system.

## Learning outcomes

By the end you can:

1. **Run** three complete deployments in different regulated industries, each within four weeks, from first meeting to signed handover.
2. **Discover** hidden constraints and the real problem behind each customer's request, using interviews, observation and data.
3. **Integrate** realistic customer systems (FHIR servers, logistics and e-way bill APIs, core-banking extracts, SSO) under time pressure without sacrificing idempotency or security.
4. **Deploy** an AI workflow per customer with a customer-specific evaluation agreement, human-in-the-loop controls and a security and compliance pack mapped to the sector's rules.
5. **Handle** injected incidents, scope changes and difficult stakeholders while keeping a weekly cadence and an honest status.
6. **Demonstrate** value to decision-makers with a measured outcome and an honest readout.
7. **Hand over** each deployment so another team can operate it without you.
8. **Extract** patterns across the three deployments and **propose** what should become product (feeding FDE501).

## Chapters and lessons

### Chapter 1 · Studio operating model (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Teams and roles | Teams of four; rotating roles per deployment (lead FDE, integration FDE, AI/eval FDE, deployment strategist) | Write your team charter and rotation plan |
| 1.2 The simulated customers | How briefs work: public brief, confidential stakeholder briefs, hidden constraints, scripted incidents; what you may and may not ask instructors | Read the first public brief; list questions for the first meeting |
| 1.3 Toolkit | Your FDE301 playbook, FDE302 templates, FDE303 connectors, FDE304 eval harness, FDE402 diagnostic tool, FDE305 demo checklist | Assemble and test your team's toolkit repository |
| 1.4 Grading | Customer satisfaction (scored by the customer panel against a rubric), measured outcome, quality of artefacts, handover test, peer review | Read the rubric; map each artefact to its criteria |
| 1.5 AI use in the studio | Coding agents allowed; customer data only in approved tools; AI use logged; final readouts and role-plays without AI | Write the team's AI-use policy and log format |

**Check your understanding:** Why rotate roles between deployments? Which artefacts from earlier courses will save the most time? What will the customer panel reward that a code review would not?

### Chapter 2 · Deployment A: a hospital — discovery and integration (weeks 2–3)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 The customer | Illustrative 400-bed private hospital in Pune; sponsor wants "AI to cut discharge delays"; stakeholders include the medical superintendent, ward nurses, billing, IT and the insurance desk | First meeting; agree a two-week discovery plan |
| 2.2 Discovery on the ward | Observing discharge as performed (summary drafting, pharmacy, billing, insurer approval); finding where the hours go | Map the discharge workflow with measured waits |
| 2.3 Health data integration | A HAPI FHIR server loaded with Synthea synthetic patients (adapted to Indian names and settings); Patient, Encounter, Observation, MedicationRequest resources; ABDM context | Pull encounters and observations incrementally; build the patient timeline |
| 2.4 Identity and access | Hospital SSO (Keycloak as stand-in); role-based access for doctors, nurses and billing; audit logs | Integrate SSO with role mapping and audit |
| 2.5 Consent and data protection | DPDP consent and purpose, health data sensitivity, what leaves the hospital (nothing) | Write the data-handling plan and get IT's sign-off |

**Check your understanding:** Which part of discharge delay is not about documents at all? Why must audit logs exist before the AI step does? What did the hidden constraint in your brief turn out to be?

### Chapter 3 · Deployment A: AI deployment, demo and handover (weeks 4–5)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 The AI step | Drafting discharge summaries from structured data and notes for doctor review; never auto-sending | Build the drafting workflow with a review screen |
| 3.2 Clinical evaluation | Evaluation agreement with the "clinician" panel; error severities (an omitted allergy versus a style issue); labelled set | Run the evaluation; report severity-weighted results |
| 3.3 Safety and review controls | Mandatory review, highlighted uncertain fields, edit tracking, disclosure | Measure edit rates and missed errors in a simulated week |
| 3.4 Demo to the medical superintendent | Measured change in discharge time on the simulated workload; honest limits | Deliver the demo and readout |
| 3.5 Handover | Runbooks, support tiers, eval ownership with the hospital's quality team | Hand over to another team; they operate for three days |

**Check your understanding:** Why weight errors by clinical severity? What does the doctors' edit rate tell you that accuracy does not? What would make you recommend not going live?

### Chapter 4 · Deployment B: a logistics company — discovery and integration (weeks 6–7)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 The customer | Illustrative third-party logistics firm in Bhiwandi serving e-commerce sellers; sponsor wants "an agent that handles delivery exceptions"; stakeholders include the control tower, hub managers, finance and the sales team | First meeting and discovery plan |
| 4.2 Exceptions as data | Exception categories, frequency, handling time, who decides; process mining on a shipment event log | Mine variants and measure exception handling time |
| 4.3 Integrations | Shipment API, GPS pings, an e-way bill sandbox, customer messages (simulated messaging channel), a legacy warehouse database | Build incremental, idempotent connectors with reconciliation |
| 4.4 Canonical model | Shipment, consignment, hub, vehicle, seller and consignee entities; resolving consignee addresses and phone numbers | Build the canonical model and resolve consignees |
| 4.5 Scope change | The sponsor changes priority mid-engagement (scripted); negotiating scope with change control | Process the change request and re-plan |

**Check your understanding:** Which exceptions should the agent never handle alone? Why does address resolution matter for an exceptions agent? How did you protect the pilot's success criteria when scope changed?

### Chapter 5 · Deployment B: agent, ROI and handover (weeks 8–9)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 The agent | Narrow tools (look up shipment, reschedule delivery, notify consignee, raise claim) with approval on costly actions | Build the agent with tool permissions and audit |
| 5.2 Reliability | pass^k on scripted exception scenarios; cost per resolved exception including human time | Report reliability and cost per resolution |
| 5.3 Injected incident | A partner API changes its schema at night (scripted); detection, mitigation, communication | Run the incident with the customer and write the postmortem |
| 5.4 ROI readout | Baseline versus pilot on handling time and customer complaints; full cost; ranges | Deliver the ROI readout to the operations head and CFO |
| 5.5 Handover | Runbooks for connector failures; support model; partner handover notes | Hand over; the receiving team handles one incident |

**Check your understanding:** Why report cost per resolved exception rather than per agent run? What did the schema-change incident teach you about your connectors? Which number in your ROI readout was most uncertain, and how did you show it?

### Chapter 6 · Deployment C: a bank — discovery and integration (weeks 10–11)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 The customer | Illustrative small finance bank in Jaipur; sponsor wants faster, fairer complaint resolution; stakeholders include the principal nodal officer for grievances, branch heads, compliance, the CISO and IT | First meeting under strict access rules |
| 6.2 Regulation first | RBI payment data storage in India; RBI FREE-AI recommendations (board-approved AI policy, telling customers when they deal with AI); DPDP; CERT-In reporting | Map requirements to controls before design |
| 6.3 Integrations | Core-banking extracts by SFTP, complaint system API, an Account Aggregator mock for consented financial data, SSO with strict conditional access | Build connectors inside a restricted replica network |
| 6.4 Security review | CISO questionnaire, data-flow diagram, threat model including prompt injection through complaint text | Complete the security pack; resolve the CISO's blocking findings |
| 6.5 On-premises constraint | The bank requires the model to run inside its environment (scripted) | Serve an open-weight model on premises and compare quality with the hosted baseline |

**Check your understanding:** Why design from regulation backwards in a bank? What does prompt injection through complaint text look like, and how do you contain it? What did the on-premises model cost you in quality, and was it acceptable?

### Chapter 7 · Deployment C: complaint triage, risk committee and handover (weeks 12–13)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 The AI workflow | Classify complaints, extract facts, check against policy, draft responses for officer approval; route vulnerable customers to humans | Build the workflow with routing rules and approvals |
| 7.2 Fairness and consistency | Checking outcomes across languages, regions and customer groups; documenting limits | Run a consistency analysis across Hindi and English complaints |
| 7.3 Risk committee | Presenting to a model-risk or AI governance committee: evaluation, controls, monitoring, fallback | Present and answer the committee's questions |
| 7.4 Go-live decision | Go, conditional go or no-go with evidence | Write and defend the decision memo |
| 7.5 Handover | Monitoring, change control through eval gates, ownership with compliance | Hand over; the receiving team processes one change |

**Check your understanding:** What would make the risk committee refuse? How do you show consistency across languages without overclaiming fairness? Why might "conditional go" be the honest answer?

### Chapter 8 · Patterns across deployments (week 14)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Retrospective | What repeated, what differed, what cost the most time in each deployment | Run a structured retrospective across all three |
| 8.2 Field reports | Turning repetition into product proposals with evidence (Razorpay's "2+ merchants" rule; OpenAI's and Anthropic's codification expectations) | Write two field reports with evidence from at least two deployments each |
| 8.3 Reusable kit | Connectors, eval harnesses, review screens, runbook templates that generalise | Package one reusable component and test it on a fourth, small brief |
| 8.4 Your portfolio | Case studies with measured outcomes, written for hiring managers | Write one public case study (all customers illustrative) |

**Check your understanding:** Which of your components worked unchanged in all three deployments? What should never be generalised? How would a product team judge your field report?

## Weekly rhythm

| Week | Chapter | Customer milestone | Deliverable |
|---|---|---|---|
| 1 | 1 | Team charter, toolkit, first brief | Toolkit repository |
| 2 | 2 | Hospital: discovery | Discovery readout |
| 3 | 2 | Hospital: integrations and SSO | Data-handling plan signed |
| 4 | 3 | Hospital: AI workflow and evaluation | Evaluation results |
| 5 | 3 | Hospital: demo and handover | **Deployment A complete** |
| 6 | 4 | Logistics: discovery and process mining | Discovery readout |
| 7 | 4 | Logistics: integrations, canonical model, scope change | Change record |
| 8 | 5 | Logistics: agent and injected incident | Postmortem |
| 9 | 5 | Logistics: ROI readout and handover | **Deployment B complete** |
| 10 | 6 | Bank: discovery and regulation mapping | Requirements-to-controls map |
| 11 | 6 | Bank: integrations, security review, on-premises model | Security pack approved |
| 12 | 7 | Bank: workflow and consistency analysis | Evaluation and consistency report |
| 13 | 7 | Bank: risk committee and handover | **Deployment C complete** |
| 14 | 8 | Retrospective and reusable kit; solo deployment (P3) begins | Field reports, case study |
| 15 | Review | Solo deployment readout; individual oral examination and live role-play | **P3 due**; final assessment |

## Working with AI in this course

- **Use AI for:** building connectors, review screens, eval harnesses and infrastructure code with coding agents; drafting documents from your notes; generating synthetic test cases (labelled as synthetic); summarising long briefs.
- **Do without AI (drills):** customer meetings, interviews and role-plays; readouts and committee presentations; go-live decisions; the individual final role-play. Each team also completes one integration in each deployment AI-off and records the time difference.
- **Verify AI output by:** running every evaluation against expert-labelled data, never AI-labelled data alone; reviewing every generated security answer against an actual control; chaos-testing AI-written connectors; reading every customer-facing message before it is sent.
- **Where AI still fails here (show it):** keep a team log of AI failures across the three deployments (invented API fields, wrong regulatory claims, unsafe suggested actions, generic customer communication) with the cost of each in hours. The log is graded.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Deployment A (hospital) | 18% |
| Deployment B (logistics) | 18% |
| Deployment C (bank) | 18% |
| P1 and P2 (deployment kit, reusable component, field reports) | 10% |
| P3 solo deployment and case study | 16% |
| Individual oral examination and role-play (AI off) | 20% |

Each deployment grade combines the customer panel's rubric score, the measured outcome against the agreed criteria, the artefacts (charter, evaluation agreement, security pack, runbooks), the handover test (the receiving team's success operating it) and peer review of your contribution.

**Mastery gate.** You pass when: (1) all three deployments reach a recorded go, conditional go or justified no-go decision with an evaluation agreement signed before results; (2) all three handovers pass the receiving team's operation test; (3) in the individual oral exam you can explain every design and commercial decision in your deployments and handle a 20-minute role-play with a hostile stakeholder you have not met.

## Industry reality

The studio mirrors how deployment roles are described by employers: short, outcome-focused pilots (Palantir, 2022), ownership "from first prototype to stable production" (OpenAI), in-person building with customers (Anthropic), and feeding repeated patterns back to product (OpenAI, Anthropic, Razorpay). The three industries are among those named in current FDE postings: OpenAI lists healthcare and financial services FDE roles; Salesforce lists public sector roles; Razorpay embeds FDEs with merchants. Regulated-industry constraints in the studio come from public sources (RBI, DPDP Rules, CERT-In, ABDM).

**Interview questions from this course**

1. *Tell me about a deployment where the customer's ask was not their real problem.* Strong answer: a specific case from the studio; how discovery revealed it; the evidence; how the scope changed; the measured outcome.
2. *Describe an incident during a deployment and how you handled it.* Strong answer: detection, mitigation first, communication cadence, root cause, postmortem actions, what changed in your connectors or process.
3. *How did you decide whether the bank's complaint triage could go live?* Strong answer: evaluation agreement, severity-weighted results, consistency across languages, controls, risk committee feedback, conditional go with monitoring, or no-go with reasons.
4. *What did you reuse across your three deployments, and what did you have to rebuild?* Strong answer: concrete components, measured time saved, what did not generalise and why, the field report submitted.
5. *A sponsor changes priorities halfway through a pilot. What do you do?* Strong answer: change request with impact on time, cost and success criteria; renegotiates the charter; protects the decision the pilot must produce; documents it.

## Resources (free first)

- **Health data:** HL7 FHIR — https://hl7.org/fhir/ ; HAPI FHIR server — https://hapifhir.io/ ; Synthea — https://synthetichealth.github.io/synthea/ ; ABDM — https://abdm.gov.in/
- **Logistics and tax systems:** NIC e-invoice and e-way bill API sandbox — https://einv-apisandbox.nic.in/ ; e-way bill portal — https://ewaybillgst.gov.in/ ; GS1 standards — https://www.gs1.org/standards
- **Banking and finance:** RBI FREE-AI report (Aug 2025) — https://rbidocs.rbi.org.in/rdocs/PublicationReport/Pdfs/FREEAIR130820250A24FF2D4578453F824C72ED9F5D5851.PDF ; RBI, Storage of Payment System Data — https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=11244 ; Sahamati (Account Aggregator) — https://sahamati.org.in/
- **Law and incidents:** DPDP Rules 2025 (PIB) — https://www.pib.gov.in/PressReleasePage.aspx?PRID=2190014 ; CERT-In directions — https://www.cert-in.org.in/Directions70B.jsp
- **Methods (this university):** your FDE301 playbook, [FDE302](../../year_3/FDE302_customer_discovery_and_requirements_engineering/README.md), [FDE303](../../year_3/FDE303_rapid_integration_engineering_apis_legacy/README.md), [FDE304](../../year_3/FDE304_deploying_ai_in_the_enterprise/README.md), [FDE305](../../year_3/FDE305_technical_communication_in_the_field_demos/README.md), [FDE401](../FDE401_data_integration_and_ontology_modeling/README.md), [FDE402](../FDE402_debugging_and_operating_in_customer_environments/README.md); [AIE305 Evaluating LLM Systems](../../../ai_engineering/year_3/AIE305_evaluating_llm_systems/README.md)

## Sources

- Palantir, "A Day in the Life of a Palantir Deployment Strategist" (8 Mar 2022) — https://blog.palantir.com/a-day-in-the-life-of-a-palantir-deployment-strategist-951cb59a5a96 (checked 2026-10)
- OpenAI, Forward Deployed Engineer (Tokyo) — https://openai.com/careers/forward-deployed-engineer-tokyo/ ; careers search "forward deployed" (12 Oct 2026) — https://openai.com/careers/search/?q=forward%20deployed (checked 2026-10)
- Anthropic, Forward Deployed Engineer, London — https://job-boards.greenhouse.io/anthropic/jobs/5423029008 (checked 2026-10)
- Razorpay, Forward Deployed Engineer (Aug 2026) — https://portfoliojobs.tcv.com/companies/razorpay/jobs/89918935-forward-deployed-engineer (checked 2026-10)
- Salesforce careers search (12 Oct 2026) — https://salesforce.wd12.myworkdayjobs.com/External_Career_Site (checked 2026-10)
- RBI, DPDP and CERT-In sources as listed under Resources (checked 2026-10)

_Last reviewed: 2026-10_
