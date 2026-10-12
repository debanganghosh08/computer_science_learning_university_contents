# FDE403 · Labs and projects

Every financial figure comes from a spreadsheet or notebook with visible formulas and a dated assumptions register. Vendor prices are quoted with the page and the date checked. Customers, RFPs and numbers are illustrative unless sourced. Contract documents you write are teaching exercises, not legal advice; a reviewer checks them against the course template.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Options and ADRs | Three architecture options for an illustrative insurer's claims assistant; Generative AI Lens review; ADRs for the three costliest decisions; mock architecture board | Options document, review findings, ADRs, board notes | 4 h |
| 2 · Reference architectures and deployment models | Reference architectures with latency and cost budgets for a retrieval assistant, a document pipeline and an agent; compare SaaS, single-tenant, customer-cloud and on-premises models | Diagrams with budgets, comparison table | 6 h |
| 3 · Build-buy-partner matrix | Weighted matrix with sensitivity; exit-cost estimate; self-host break-even volume | Matrix, sensitivity chart, break-even calculation | 4 h |
| 4 · TCO and unit economics | Full TCO for your FDE304 deployment; cost per successful task including review and retries; cost allocation with tags | TCO model, unit cost, allocation report | 5 h |
| 5 · Pricing designs | Seat, usage (with caps), outcome and hybrid prices for one product; an auditable outcome definition tested on simulated logs | Price sheets, outcome definition, log test results | 6 h |
| 6 · NPV, ranges and Monte Carlo | NPV, payback and IRR for three scenarios; Monte Carlo on three drivers; rewrite an overclaiming case | Model, range chart, rewritten case | 4 h |
| 7 · RFP response and procurement timeline | Respond to a short illustrative RFP section; build a backward timeline from go-live with legal, security and finance reviews; list GeM steps for a public buyer | Response, timeline, GeM checklist | 4 h |
| 8 · Security review plan and answer library | Plan a high-sensitivity review; build a reusable answer library with evidence links; remediation plan for three findings | Plan, library, remediation plan | 4 h |
| 9 · SOW and change control | SOW for a six-week pilot with assumptions and acceptance criteria; process two change requests | SOW, change records | 4 h |
| 10 · Multi-customer refactor | Refactor a single-customer design for ten customers with tenant isolation and per-tenant cost tracking; regional deployment for India and EU | Design, isolation tests, cost dashboard | 5 h |

## Projects

### P1 · Costed reference architecture for an AI document pipeline (L1, ~6 hours)

**Real-world inspiration.** AWS publishes the Well-Architected Framework and a Generative AI Lens for reviewing AI workloads; FinOps practice allocates cloud costs by tags and unit metrics.

**What to build.** For an illustrative Ahmedabad-based textile exporter that processes 8,000 shipping and customs documents a month, design a document-extraction pipeline with human review, and cost it end to end.

**Acceptance criteria**
- Architecture diagram with latency and cost budgets per component; two alternatives with reasons for rejection.
- TCO for 12 months covering at least eight cost categories, including human review time.
- Cost per successfully processed document reported with a sensitivity chart on the top five drivers.
- Prices for every external service cited with page and date.

**Stretch goals.** Add the self-hosted model option and compute its break-even volume.

**What it proves to an employer.** You can tell a customer what a solution will really cost before they sign.

### P2 · Pricing and business case for an outcome-based offer (L2, ~15 hours)

**Real-world inspiration.** Intercom prices its AI agent per outcome and Salesforce prices Agentforce per conversation or per action through credits (October 2026); NASSCOM reports a shift to outcome-based, risk-sharing contracts in Indian IT services (2026).

**What to build.** An illustrative Indian SaaS company sells an AI collections-reminder assistant (voice and messaging) to non-banking finance companies. Design the price (compare seat, usage, outcome and hybrid), define the outcome so both sides can audit it, and build the customer's business case for a 50,000-loan portfolio using a provided baseline dataset.

**Acceptance criteria**
- Four pricing models compared on vendor revenue, customer cost predictability and incentive risks, with a recommendation.
- Outcome definition tested against 10,000 simulated interaction logs, including ambiguous cases; both "parties" (two classmates) reach the same count independently.
- Business case with NPV, payback and a Monte Carlo range; every assumption registered with an owner.
- A compliance note: customer-communication rules relevant to collections and AI disclosure for regulated lenders, each with a source, or marked "(unconfirmed)".
- A one-page summary a CFO reads in two minutes and answers four questions about correctly.

**Stretch goals.** Add a cap-and-floor structure to share risk and model its effect on both sides.

**What it proves to an employer.** You can design commercial terms for AI products that survive scrutiny from both finance and the customer.

### P3 · Full proposal and panel defence for an enterprise AI programme (L3, portfolio-grade, ~30 hours)

**Real-world inspiration.** OpenAI's Deployment Leads own value cases and ROI and report to executive sponsors; enterprise buyers run architecture, security, legal and procurement reviews before signing; Indian government buyers use the Government e-Marketplace (GeM).

**What to build.** Respond to an instructor-written RFP from an illustrative state power distribution company that wants AI for consumer complaint handling and field-work-order triage across Hindi, English and one regional language. Deliver: solution architecture with options and ADRs, deployment model and residency design, TCO, pricing proposal, business case with ranges, security review answer pack, SOW with assumptions and acceptance criteria, procurement timeline, and a risk register. Defend it before a panel (CFO, CISO, head of procurement, operations head) played by instructors or industry mentors.

**Acceptance criteria**
- Every RFP requirement traced to a section of the proposal (compliance matrix complete).
- TCO and business case reproduced from your files by a reviewer, with no formula errors.
- Security answers each linked to a control or evidence item; open gaps have remediation dates.
- SOW includes at least ten customer dependencies and their consequences, and contract-grade acceptance criteria.
- During the defence, at least two assumptions are challenged; you update the model live and explain the effect correctly.
- A written deal review memo states the conditions under which you would decline the deal.

**Stretch goals.** Produce a partner delivery model in which a systems integrator runs the deployment and your team provides FDE oversight; compare margins.

**What it proves to an employer.** You can work at the level of a solutions architect or field CTO: design, cost, price and defend an enterprise deal.

## Feeds into

- [FDE501 Frontier Seminar](../../year_5/FDE501_frontier_seminar_productizing_field_patterns/README.md): pricing and unit economics of productised field patterns.
- [LCH502 Career Launch and Founder Studio](../../../../05_shared_years_3_to_5/LCH502_career_launch_and_founder_studio/README.md): pricing and business cases for your own venture.
- [CAR401 Career Lab II](../../../../05_shared_years_3_to_5/CAR401_career_lab_ii_interviews_system_design_and_ai/README.md): solution-architecture and case interviews.
- [Flagship industry project](../../../../06_career_and_market_readiness/05_industry_projects/FDE_forward_deployed_engineering.md): the business case and ROI readout.
