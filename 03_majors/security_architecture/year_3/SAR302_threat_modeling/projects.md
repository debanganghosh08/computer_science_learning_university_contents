# SAR302 · Labs and projects

All systems are *illustrative scenarios* unless a source is given. You model and test only systems you build yourself or are given as documents. Agent tests use benign canary instructions (for example, a document that asks the agent to reply with a marker word) to check that untrusted content cannot trigger actions; no lab builds or uses real attack payloads. Labs 3 and 4 are done without AI assistants.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Manifesto critique and first session | Critique three published threat models against the Threat Modeling Manifesto, then facilitate a 45-minute session on a college attendance app | Critique table; session notes with owned actions; feedback from two participants | 3 h |
| 2 · DFD repair | Fix a deliberately wrong DFD (missing admin path, batch job, third-party callback, shared cache) | Corrected DFD and a list of each fix with the threat it exposes | 3 h |
| 3 · STRIDE per interaction (no AI) | Run STRIDE-per-interaction on a payment initiation flow | Threat list in "actor, action, asset, impact" form, mapped to CAPEC where possible | 4 h |
| 4 · Attack tree (no AI) | Build an attack tree for "move money without the account holder's consent" in a wallet app | Tree with cost, skill and detectability; five leaves mapped to ATT&CK techniques and the log source that would reveal them | 4 h |
| 5 · PASTA stages 1–4 | Apply PASTA to an illustrative insurance claims portal | Business objectives, scope, decomposition and threat analysis, with impact in rupees and hours | 5 h |
| 6 · LINDDUN GO | Run the card-based method on a fitness app that shares data with an insurer | Privacy threats mapped to DPDP duties, and one redesigned flow | 4 h |
| 7 · Mitigations to tests | Turn 15 mitigations into requirements and automated tests | Passing test suite and a mapping file threat → requirement → test | 5 h |
| 8 · Threat model as code | Rewrite a model in pytm or Threagile and add a CI job that fails when an external flow appears without a model update | Repository, CI run logs showing one failing and one passing pull request | 5 h |
| 9 · Event pipeline | Threat-model a Kafka-based payment events pipeline (producers, broker, consumers, schema registry) | Model, ranked threats and three design changes | 4 h |
| 10 · Agents and AI tools | Model a multi-agent workflow with MAESTRO and STRIDE; then generate models with two AI tools and score them against yours | Your model, trifecta audit, and a precision/recall table with every AI error classified | 5 h |

## Projects

### P1 · Threat model of a college placement portal (L1, ~6 hours)

**Real-world inspiration:** placement portals hold résumés, marks, phone numbers and recruiter accounts, which makes them personal-data systems under India's DPDP Act. The portal is an *illustrative scenario*: students upload résumés, recruiters search and shortlist, the placement office approves companies.

**What to build:** a complete first threat model: system description, DFD with trust boundaries, STRIDE threats, a LINDDUN GO pass, ranked top five with mitigations, and an assumptions log.

**Acceptance criteria:**
- The DFD shows at least four trust boundaries, including the recruiter boundary and the admin path.
- At least 25 STRIDE threats and 5 privacy threats, each in "actor, action, asset, impact" form, with no duplicates.
- Ratings use written criteria that a classmate can apply and reach the same top five (checked by a peer re-rating).
- Each of the top five has a testable mitigation and a named owner role.
- The assumptions log lists at least five assumptions and how each would be checked.

**Stretch goals:** an attack tree for "a recruiter downloads all résumés"; a pytm version of the model.

**What it proves to an employer:** you can run the full method end to end on a real-shaped system and produce something an engineering team can act on.

### P2 · Health records exchange threat model (L2, ~15 hours)

**Real-world inspiration:** India's Ayushman Bharat Digital Mission builds consent-based exchange of health records between hospitals, labs and personal health record apps ([ABDM](https://abdm.gov.in/)). Hospital ransomware and records exposure are recurring incidents worldwide. The hospital system here is an *illustrative scenario*: a hospital information system that shares records with patients' apps and with other providers after consent.

**What to build:**
- a layered system model (context DFD, two level-1 DFDs, sequence diagrams for consent and record fetch);
- STRIDE per interaction on the exchange paths, LINDDUN PRO on the consent and records flows, and an attack tree for "an unauthorised person reads a patient's records";
- PASTA impact analysis for the top ten threats (patient harm, regulatory exposure, downtime);
- mitigations as requirements, with at least ten automated tests against a small prototype of the consent service you build;
- the model as code (pytm or Threagile) with a CI check.

**Acceptance criteria:**
- Every consent-related flow has threats in at least three LINDDUN categories, each mapped to a DPDP duty.
- The attack tree has at least 15 leaves; the three cheapest-to-cut leaves are identified and the design change is shown.
- At least ten automated tests pass and each fails when its mitigation is removed (demonstrate two).
- The CI check blocks a pull request that adds an unmodelled external flow.
- A peer reviewer finds no trust boundary missing from your level-1 DFDs.

**Stretch goals:** a break-glass emergency-access design for clinicians with its own threat model; a comparison of your model with an AI-generated one.

**What it proves to an employer:** you can threat-model a regulated, privacy-heavy system with several methods and turn the result into tested controls.

### P3 · Threat model of an LLM agent platform (L3, portfolio-grade, ~30 hours)

**Real-world inspiration:** the Five Eyes guide *Careful adoption of agentic AI services* (2026) asks organisations to limit agent privileges and keep human approval for decision-making steps ([CISA](https://www.cisa.gov/news-events/news/cisa-us-and-international-partners-release-guide-secure-adoption-agentic-ai)). The MCP security best practices describe confused-deputy, token passthrough and SSRF risks for connector servers ([MCP](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices)). The platform is an *illustrative scenario*: a bank's internal agent platform where agents read customer emails and tickets, query account data through MCP servers, draft replies and can propose refunds that a human approves.

**What to build:**
- a system model covering the agent runtime, model provider, MCP servers, identity provider, data stores, approval service and logging;
- STRIDE plus MAESTRO layer analysis, with every OWASP Agentic Top 10 entry (ASI01–ASI10) assessed as relevant or not, with reasons;
- attack trees for three goals: unauthorised refund, customer data leaving the bank, and an agent acting outside its assigned task;
- a mitigation architecture: tool permission scopes, per-action approval, sandboxing, egress allow-lists, token audience checks, memory controls, audit logs;
- a small prototype (any agent framework and a local or hosted model) with at least 15 abuse-case tests using benign canary documents;
- an evaluation of two AI threat modeling tools against your model;
- a continuous process: pull-request template, model-as-code check and a review trigger list.

**Acceptance criteria:**
- Against the instructor's reference model, your model reaches recall of at least 85% and precision of at least 80% on high and critical threats.
- In 50 canary documents placed in emails and tickets, zero cause a tool call or a refund proposal; show the logs.
- Every MCP server in the design validates token audience and never forwards client tokens downstream (show the configuration or code).
- The AI-tool evaluation reports precision, recall and at least ten classified errors per tool.
- You defend the model in a 25-minute oral; the panel adds one new tool to the agent and you update the model and ranking live.

**Stretch goals:** a CaMeL-style split where the planner never reads untrusted text; an assurance case for "no refund without human approval".

**What it proves to an employer:** you can reason about a new system class from first principles and show evidence, which is the scarce skill in AI security architecture.

## Feeds into

- [SAR402 Identity Architecture at Scale](../../year_4/SAR402_identity_architecture_at_scale/README.md): identity flows and token threats from P2 and P3.
- [SAR403 Security Architecture for AI Systems and Agents](../../year_4/SAR403_security_architecture_for_ai_systems_and_agents/README.md): P3 is the starting model for its projects.
- [SAR305 Secure SDLC and DevSecOps Architecture](../SAR305_secure_sdlc_and_devsecops_architecture/README.md): models as code become a pipeline stage.
- [OV05 AI Security and Safety](../../../../04_overlaps/OV05_ai_security_safety/README.md), with [OFF403 AI and LLM Red Teaming](../../../ethical_hacking_offensive_security/year_4/OFF403_ai_and_llm_red_teaming/README.md) testing what you modelled under authorization.
- The [flagship industry project](../../../../06_career_and_market_readiness/05_industry_projects/SAR_security_architecture.md) uses P3's method for its threat model.
