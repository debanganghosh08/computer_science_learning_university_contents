# FDE304 · Labs and projects

Use synthetic or public data unless a real organisation has agreed in writing, and keep any real data inside that organisation. Every project ships: an architecture note with model placement, an evaluation agreement signed before results were seen, the eval harness and raw results, a security review pack, a residency matrix, a rollout plan and a measured outcome. Customers and scenarios are illustrative unless stated otherwise.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Use-case scoring | Score 15 illustrative use cases on volume, verifiability, error cost, data access and risk tier; recommend three and reject three | Scoring sheet, recommendations, reasons for rejection | 3 h |
| 2 · Architecture and placement | Design permission-aware retrieval over two sources and an agent with narrow tools; decide model placement for a bank, a hospital and a retailer | Architecture diagrams, placement decisions with trade-offs | 4 h |
| 3 · Expert labelling and eval agreement | Run a labelling session with a classmate-expert on 60 cases; compute agreement; write an evaluation agreement; package an offline harness in a container | Labelled set, agreement statistic, signed agreement, harness | 7 h |
| 4 · Security review pack | Data-flow diagram; answer 60 questionnaire items (SIG/CAIQ style, 20 AI-specific) with evidence references; threat-model the agent | DFD, answers with evidence map, threat model | 6 h |
| 5 · Residency and regulation matrix | Map every data copy (prompts, embeddings, logs, backups, support access) to region and rule; check against DPDP, RBI payment data storage, FREE-AI and CERT-In | Matrix, gaps, fixes | 4 h |
| 6 · Confidence routing and audit | Route 200 extraction results by confidence; measure errors that slipped through; implement an audit log and reconstruct a decision | Routing analysis, audit log demo | 4 h |
| 7 · Shadow mode and rollout plan | Shadow-run on 300 historical cases; write a staged rollout plan with kill switch and outage test | Shadow comparison report, rollout plan, outage test evidence | 4 h |
| 8 · Change plan and training | ADKAR plan for a target team; deliver a 30-minute training session; collect feedback | Plan, training material, feedback summary | 5 h |
| 9 · Baseline, comparison and ROI | Run a baseline on a simulated workload; analyse a stepped-wedge dataset; build a full-cost ROI model with ranges | Baseline data, analysis notebook, ROI model and one-page readout | 6 h |
| 10 · Change control and handover | Push a prompt or model change through eval gates; hand over to another team for one week of operation | Change record, gate results, the other team's operations log | 4 h |

## Projects

### P1 · Customer-specific evaluation for a document workflow (L1, ~6 hours)

**Real-world inspiration.** OpenAI measures FDEs partly by "eval-driven feedback that changes product and model roadmaps"; Anthropic's Applied AI Architects help customers build evaluation frameworks for their use cases (2026).

**What to build.** For an illustrative Chennai-based logistics company that receives 2,000 delivery-exception emails a day, build a classifier-and-extractor (category, consignment number, requested action) using a hosted model, and a customer-specific evaluation: 150 realistic synthetic emails in English and Tamil-English mixed text, labelled by a classmate playing the operations lead, with an evaluation agreement signed before you run anything.

**Acceptance criteria**
- Evaluation agreement with per-field thresholds and error severities, dated before the first run.
- Labelled set with guidelines; agreement between two labellers reported on at least 40 items.
- Results per field with confidence intervals and a list of every failure category.
- A go/no-go recommendation that follows from the agreement, not from your preference.

**Stretch goals.** Compare two models at equal cost; report the paired difference.

**What it proves to an employer.** You measure AI quality the way a customer will judge it, before arguing about it.

### P2 · A deployable AI workflow with a security and compliance pack (L2, ~15 hours)

**Real-world inspiration.** Enterprise buyers run vendor risk reviews with standard questionnaires (SIG, CAIQ) and increasingly ask AI-specific questions about training on data, retention and prompt injection (OWASP Top 10 for LLM Applications 2025). India's DPDP Rules (2025) phase in consent and notice duties over 18 months.

**What to build.** For an illustrative third-party administrator in Bengaluru that processes cashless hospital claims, deploy a document-assistance workflow: extract fields from synthetic claim documents, check them against policy rules, and draft a query letter for missing items, with a human approving every letter. Integrate SSO (Keycloak as the customer IdP) and write back to a mock claims system idempotently. Produce the full review pack.

**Acceptance criteria**
- Evaluation on 200 synthetic claims against an agreed threshold, with field-level results and a severity-weighted error score.
- No letter can be sent without an approval recorded in the audit log; a test proves it.
- Security pack: DFD, 60 answered questionnaire items each mapped to a control or evidence item, threat model with prompt injection through uploaded documents tested on 20 crafted inputs (in your own sandbox only).
- Residency matrix covering every copy of data; DPDP consent notice drafted for the claimant-facing part.
- A reviewer playing the customer's CISO signs off or lists blocking issues; you resolve all blockers.

**Stretch goals.** Run the model on a self-hosted open-weight model in a container and compare quality, latency and cost with the hosted model.

**What it proves to an employer.** You can get an AI workflow through the gates that stop most enterprise pilots.

### P3 · Pilot to production with measured value (L3, portfolio-grade, ~30 hours)

**Real-world inspiration.** OpenAI's Deployment Leads "set impact hypotheses, baselines, and KPIs" and run pre- and post-deployment measurement; Klarna's 2024 claims and its 2025 change of course show why quality-adjusted measurement matters; the RBI's FREE-AI report (2025) recommends that customers be told when they are dealing with AI.

**What to build.** Choose one: (a) an illustrative cooperative bank in Maharashtra wants an assistant that helps branch staff answer customer questions about loan products and complaint procedures; (b) an illustrative hospital chain wants discharge-summary drafting for doctors' review. Run the full deployment over five simulated weeks with a team of classmates as users (scripted workloads provided by the instructor): use-case confirmation, architecture with model placement, evaluation agreement and golden set, security and residency pack, human-in-the-loop design, shadow mode, staged rollout with kill switch, change plan and training, baseline and stepped-wedge rollout across two user groups, ROI readout and handover.

**Acceptance criteria**
- Evaluation agreement signed before results; final results meet thresholds or the readout recommends not proceeding, with evidence.
- Stepped-wedge comparison shows effect on time per task and error rate, with confidence ranges and full cost including review time.
- Disclosure, escalation and audit designs present and tested; for option (a), mapped to at least five FREE-AI recommendations.
- Outage drill: provider failure switches to the manual path within five minutes, with no lost work.
- Handover accepted by the operating team after one week; their log shows at least one change processed through the eval gate.
- A 15-minute steering-committee readout and a written ROI report a non-technical executive can follow.

**Stretch goals.** Add an agentic step (for example, fetching a customer's loan status through a read-only tool) and show its effect on reliability with pass^k.

**What it proves to an employer.** You have done what FDE job postings describe: taken an AI system into production inside an organisation and proved, honestly, what it changed.

## Feeds into

- [FDE404 Field Studio](../../year_4/FDE404_field_studio_three_simulated_customer/README.md): each of the three simulated deployments repeats this cycle under time pressure.
- [FDE402 Debugging and Operating in Customer Environments](../../year_4/FDE402_debugging_and_operating_in_customer_environments/README.md): operating the deployed workflow in restricted environments.
- [FDE403 Solution Architecture, Pricing and ROI](../../year_4/FDE403_solution_architecture_pricing_and_roi/README.md): the ROI model becomes a business case and pricing proposal.
- [Flagship industry project](../../../../06_career_and_market_readiness/05_industry_projects/FDE_forward_deployed_engineering.md) and [OV12 Agent Infrastructure](../../../../04_overlaps/OV12_agent_infrastructure_platform/).
