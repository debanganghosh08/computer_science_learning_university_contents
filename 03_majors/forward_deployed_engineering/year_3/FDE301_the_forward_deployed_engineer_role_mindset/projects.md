# FDE301 · Labs and projects

Every claim about a named company must link to a primary source (the company's own blog, job posting or documentation) with the date you checked it. Scenarios you invent are labelled "illustrative". Any work with a real organisation needs its written consent, and no personal data leaves that organisation.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Job-posting teardown | Extract tasks, travel, experience, tools and stated success measures from 10 current FDE-type postings (at least 3 India-based) | Comparison table with links and check dates; five patterns you found | 4 h |
| 2 · Engagement economics model | Model a 12-month engagement: FDE cost, contract value, time to first value, conversion and expansion scenarios (illustrative numbers) | Spreadsheet with formulas visible; one-page reading of the results | 4 h |
| 3 · Lifecycle map and pilot charter | Map qualification → discovery → pilot → production → expansion → handover with entry and exit criteria; write a pilot charter for an illustrative logistics customer | Lifecycle diagram; one-page charter with success and kill criteria | 4 h |
| 4 · Metric design and baseline plan | Turn OpenAI's stated FDE and Deployment Lead success measures into metrics with numerators, denominators and data sources; plan a two-week baseline | Metric specification; baseline plan | 3 h |
| 5 · Core-versus-custom memos | Write decision memos for three illustrative feature requests (a custom report, a new connector, a workflow change) | Three one-page memos with cost, reuse potential and recommendation | 4 h |
| 6 · Cadence simulation | Run a four-week simulated engagement with a classmate playing the customer: weekly status, decision log, risk register, one escalation | Status reports, logs, the escalation, a reflection on what slipped | 6 h over 2 weeks |
| 7 · Data-access and AI-tool policy | Design minimum access for a pilot and an AI-tool usage policy for the team | Access request; policy mapped to DPDP obligations and contract terms | 3 h |
| 8 · Ethics scenarios | Respond to five illustrative scenarios (covert monitoring, cross-customer reuse, hiding errors, credential sharing, a request outside scope) | Written responses with the rule or principle each relies on | 3 h |
| 9 · AI-assisted versus manual connector | Build the same small API connector twice, once by hand and once with a coding agent; log time, defects and fixes | Both versions, tests, a defect log, an honest comparison | 5 h |
| 10 · Practitioner interview | Interview one person in a customer-facing engineering role (with consent; anonymise) about a real deployment | Interview notes (approved by the interviewee) and a 500-word synthesis | 3 h |

## Projects

### P1 · Role and engagement teardown (L1, ~6 hours)

**Real-world inspiration.** Palantir's posts distinguish Deltas from Devs and Echos from Deltas (2019, 2022); OpenAI, Anthropic, Salesforce, Razorpay and Sarvam AI publish FDE postings with explicit tasks and success measures (2026).

**What to build.** A public, sourced report that explains the FDE role to a first-year student: definitions, how it differs from six neighbouring roles, what employers say they measure, and a lifecycle diagram of a typical engagement.

**Acceptance criteria**
- At least 12 primary sources, each with a link and the date checked; no claim about a company without one.
- A comparison table of seven roles across five dimensions (owns code, owns customer, owns revenue, typical deliverable, success measure).
- A lifecycle diagram with entry and exit criteria for every stage.
- A reviewer from another group finds no unsourced company claim (record their check).

**Stretch goals.** Add an India section comparing three Indian employers' postings with three global ones.

**What it proves to an employer.** You understand the job you are applying for, from primary evidence rather than hype.

### P2 · A three-week mini-engagement with a real organisation (L2, ~15 hours)

**Real-world inspiration.** Palantir describes 4–12 week pilots where deployment strategists and Deltas co-create workflows with the customer (2022); OpenAI's Deployment Leads "set impact hypotheses, baselines, and KPIs" and run pre- and post-deployment measurement.

**What to build.** With written consent, run a three-week engagement with a small real organisation: a college office, a local clinic's front desk, an NGO, a small shop. Qualify the problem, agree a pilot charter, build a small tool (a spreadsheet automation, a form-to-database flow, a simple dashboard), and measure one outcome against a baseline. No personal data leaves the organisation; use their machines or anonymised extracts.

**Acceptance criteria**
- Signed one-page charter with a success metric, a baseline measured before the tool went live, and a kill criterion.
- Weekly status notes and a decision log kept for all three weeks.
- The tool is used by the intended users for at least five working days; usage and the outcome metric are reported with the baseline.
- A handover note the organisation confirms they can follow without you.
- A data-handling statement listing every data item you touched and where it stayed.

**Stretch goals.** Write a field report proposing one generic product feature from what you learned.

**What it proves to an employer.** You can take a vague request to something used and measured, with a real stakeholder, ethically.

### P3 · An FDE operating playbook for an AI startup (L3, portfolio-grade, ~30 hours)

**Real-world inspiration.** a16z's best practices for first services teams (2025): sell smart, align incentives, design for integration, leave a trail, automate the services motion, create feedback loops, be present. OpenAI and Anthropic ask FDEs to codify patterns; Razorpay sets a 2-hour acknowledgement rule for merchant issues.

**What to build.** For an illustrative AI startup selling document-processing agents to Indian mid-size manufacturers, write and test a complete FDE operating playbook: team structure and roles, engagement lifecycle with templates (qualification, charter, readiness checklist, handover), success metrics with definitions, customer cadence and escalation rules, data-access and AI-tool policies aligned with the DPDP Rules, the core-versus-custom decision process, and a field-to-product reporting loop. Test it by running two simulated engagements (classmates as customers) and revising it.

**Acceptance criteria**
- Every template is used at least once in the simulations; the revision log shows at least eight changes driven by what went wrong.
- Metrics include definitions, data sources, owners and review frequency; at least one leading and one lagging metric per lifecycle stage.
- The data policy maps each rule to a DPDP obligation or a contract clause.
- A product manager (a classmate or industry mentor) reads two field reports produced with the playbook and rates them actionable, with written reasons.
- A one-page economics summary shows the cost per engagement and the break-even contract value under stated assumptions.

**Stretch goals.** Add a partner-handover kit so a systems integrator could run the same engagement; test it with a group that did not write it.

**What it proves to an employer.** You can think like a founding FDE or deployment lead: you can build the system that makes deployments repeatable, not just do one.

## Feeds into

- [FDE302 Customer Discovery](../FDE302_customer_discovery_and_requirements_engineering/README.md) and [FDE305 Technical Communication](../FDE305_technical_communication_in_the_field_demos/README.md): the charter, cadence and field report templates are reused.
- [FDE401 Data Integration and Ontology Modeling](../../year_4/FDE401_data_integration_and_ontology_modeling/README.md): engagements from P2 often become the data problems of FDE401.
- [FDE404 Field Studio](../../year_4/FDE404_field_studio_three_simulated_customer/README.md): the P3 playbook is the operating model for all three simulated deployments.
- [FDE501 Frontier Seminar](../../year_5/FDE501_frontier_seminar_productizing_field_patterns/README.md) and [IND401 Industry Co-op Studio](../../../../05_shared_years_3_to_5/IND401_industry_co_op_studio/README.md).
