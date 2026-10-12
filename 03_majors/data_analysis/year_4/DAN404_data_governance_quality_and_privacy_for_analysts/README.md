# DAN404 · Data Governance, Quality and Privacy for Analysts

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 4 · 8 | 4 (≈ 120 hours) | L2 → L4 | [DAN304](../../year_3/DAN304_analytics_engineering_dbt_modeling_and_semantic/README.md) | [DAN501](../../year_5/DAN501_frontier_seminar_decision_intelligence/README.md), [OV07](../../../../04_overlaps/OV07_privacy_engineering/README.md), [THS501](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md) |

Part of the [Data Analysis major](../../README.md). Builds on the tests, contracts, semantic layer and model governance from DAN304, and on the ethics and law foundations in [PRO301](../../../../05_shared_years_3_to_5/PRO301_professional_practice_ethics_law_and_responsible/README.md). Platform-level governance (catalogues, lineage systems, privacy-enhancing infrastructure) is engineered in [DEN404](../../../data_engineering/year_4/DEN404_data_governance_lineage_and_privacy_engineering/README.md) and [OV07](../../../../04_overlaps/OV07_privacy_engineering/README.md). This course covers what analysts and analytics leads own: definitions people agree on, numbers that reconcile, quality they can measure, access they can justify, personal data they handle lawfully, and analyses others can reproduce.

## Why this course matters now

The value of an analyst is that their numbers are trusted, and trust is lost faster than it is earned. In dbt Labs' 2025 survey, poor data quality was the most-cited challenge for data teams (over 56%), and increasing trust in data was their top objective. In India, the Digital Personal Data Protection Act, 2023 became fully operational when its Rules were notified on 14 November 2025, with an 18-month window for phased compliance. Under the Act, failing to maintain reasonable security safeguards can attract penalties up to ₹250 crore, and failing to notify a breach up to ₹200 crore. Analysts handle more personal data than most engineers: extracts, joins, spreadsheets on laptops, files pasted into AI tools. AI makes governance harder and more urgent. Power BI's Copilot is disabled by default for tenants outside the US and EU data boundary until an administrator allows processing outside the region. Chat interfaces can expose any number a user can ask for. AI answers are only as consistent as the definitions underneath them. Reproducibility is weak even without AI: in a study of 1.4 million public Jupyter notebooks, about 24% ran without errors and about 4% reproduced their original results (Pimentel et al., 2019). Governance done well is what lets a business move fast with data without breaking trust or the law.

## Learning outcomes

By the end you can:

1. **Write and maintain** a business glossary and certified metric definitions, with owners, change control and a restatement policy.
2. **Reconcile** the same metric across systems (finance, product, BI) to an agreed tolerance, and **explain** every remaining difference.
3. **Measure** data quality along its dimensions (accuracy, completeness, consistency, timeliness, validity, uniqueness) with tests and scorecards. **Run** a data incident from detection to post-mortem.
4. **Design** least-privilege access with roles, row-level and column-level security and masking, and **run** an access review.
5. **Classify** personal data, identifiers and quasi-identifiers. **Show** why naive pseudonymisation and hashing fail, and **apply** aggregation, suppression, k-anonymity checks and basic differential privacy.
6. **Apply** the DPDP Act, 2023 and Rules, 2025 to everyday analysis: notice and consent, purpose limitation, minimisation, retention, data-principal rights, breach duties and children's data.
7. **Make** analyses reproducible and auditable: versioned code, data snapshots, environments, review checklists and audit trails for board-level numbers.
8. **Govern** AI use in analytics: tool and data-flow policies, data residency, verified answers, logging and incident handling.

## Chapters and lessons

### Chapter 1 · Why governance is an analyst's job (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 The cost of wrong numbers | Public examples: Public Health England's 2020 row-limit loss, the Reinhart–Rogoff error; internal costs (bad decisions, rework, lost trust) | Write a one-page incident summary of one public case |
| 1.2 Roles | Data owner, steward, custodian, analyst, consumer; who decides definitions and access | RACI for 10 governance decisions in an illustrative company |
| 1.3 Operating models | Central, federated and embedded governance; lightweight governance for a 50-person startup | Recommend a model for two organisations |
| 1.4 Frameworks | DAMA-DMBOK knowledge areas in outline; where analysts fit | Map your DAN304 project to the knowledge areas |

**Check your understanding:** Why is governance usually blamed for slowing teams down, and when is that fair? Who should own the definition of "active customer", and why not the data team? What is the minimum governance a startup needs?

### Chapter 2 · Glossaries and metric definitions (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Glossary vs dictionary vs semantic layer | Business meaning, technical structure and executable definition; keeping them linked | Link 10 glossary terms to columns and semantic-layer metrics |
| 2.2 The definition template | Name, purpose, formula, grain, filters, exclusions, time zone, owner, source, caveats, version | Write 8 certified metric definitions |
| 2.3 Change control | Proposals, impact analysis through lineage and exposures, approvals, effective dates | Process a definition change end to end |
| 2.4 Restatement | When to restate history; communicating changes (Eternal's 2026 move from GOV to NOV as a public example) | Restatement note and a reconciliation table |

**Check your understanding:** Why must a definition include a time zone and exclusions? What makes a definition change safe to roll out? When should history be restated, and when should a break be marked instead?

### Chapter 3 · Metric consistency and reconciliation (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Why systems disagree | Different definitions, cut-offs, time zones, refunds, currencies, late data, test accounts | List causes for 5 provided mismatches |
| 3.2 Reconciliation method | Bridge from one number to the other, step by step; tolerance policies | Reconcile product revenue to finance revenue for one month |
| 3.3 Agreed sources | One authoritative source per metric instead of "one source of truth" for everything | A source-of-record table for 15 metrics |
| 3.4 Automated consistency tests | Cross-system tests in dbt; alerting on drift | Tests that fail when two systems diverge beyond tolerance |

**Check your understanding:** Why is a reconciliation bridge more useful than a single "difference" number? When is a small persistent difference acceptable? Who should be alerted when cross-system tests fail?

### Chapter 4 · Measuring data quality (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Quality dimensions | Accuracy, completeness, consistency, timeliness, validity, uniqueness; fitness for a specific use | Score a dataset on each dimension for two different uses |
| 4.2 Profiling | Distributions, null rates, cardinality, pattern checks, referential checks | Profile a messy public dataset |
| 4.3 Tests as code | dbt data tests, Great Expectations, Soda; thresholds and severity | Implement 20 checks in one tool |
| 4.4 Metric anomaly detection | Seasonal baselines, control limits, alert fatigue | Alerts on a daily KPI with a target false-alarm rate |
| 4.5 Scorecards | Quality scores per dataset and owner; trends; what leaders should see | A quality scorecard dashboard |

**Check your understanding:** Why does "quality" depend on the use? Which dimension is hardest to test automatically, and why? How do you keep anomaly alerts useful rather than noisy?

### Chapter 5 · Data incidents and contracts (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Incident lifecycle | Detect, triage, contain, communicate, fix, post-mortem | Run a simulated incident with roles |
| 5.2 Impact analysis | Which dashboards, decisions and people were affected (lineage and exposures from DAN304) | Impact report for a broken upstream column |
| 5.3 Blameless post-mortems | Timeline, contributing factors, action items with owners | Write one for your simulated incident |
| 5.4 Upstream agreements | Data contracts and freshness SLOs with engineering teams; what analysts should ask for | Draft a contract for an event stream |

**Check your understanding:** Why should the first message in a data incident go out before the root cause is known? What makes a post-mortem "blameless", and why does that improve quality? What should an analyst ask an engineering team to guarantee?

### Chapter 6 · Access management (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Least privilege | Role-based and attribute-based access; access by purpose; service accounts | Design roles for 6 user groups |
| 6.2 Row and column security | Power BI row-level security, BigQuery column-level security with policy tags, Snowflake dynamic masking | Implement RLS and a masked column; test with 3 users |
| 6.3 Requests and reviews | Access request workflows, approvals, expiry, quarterly access reviews | Run an access review on an illustrative grants list |
| 6.4 Shadow data | Exports to spreadsheets, personal drives and chat; controls that work | Find and fix 5 shadow-data risks in a scenario |

**Check your understanding:** Why does row-level security in the BI tool not protect data exported from the warehouse? What should expire automatically? Which shadow-data risk is the hardest to control, and what would you do?

### Chapter 7 · Personal data and anonymisation (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 What is personal data | Direct identifiers, quasi-identifiers, sensitive attributes; national identifiers such as Aadhaar and their legal restrictions | Classify every column in 3 datasets |
| 7.2 Re-identification | ZIP + gender + birth date identify most Americans (Sweeney, 2000); the Netflix Prize de-anonymisation (Narayanan and Shmatikov, 2008) | Measure uniqueness of quasi-identifier combinations in a synthetic Indian dataset |
| 7.3 Why hashing is not anonymisation | Small identifier spaces (10-digit mobile numbers) can be enumerated; keyed hashing and tokenisation as pseudonymisation | Explain in writing why an unkeyed hash of a phone number is still personal data |
| 7.4 k-anonymity and its limits | Generalisation and suppression; l-diversity; linkage with outside data | Make a table 5-anonymous; show what it still leaks |
| 7.5 Differential privacy basics | Noise calibrated to sensitivity; privacy budget; the US Census Bureau's 2020 disclosure avoidance system; OpenDP | Release noisy counts at two privacy budgets; compare accuracy |

**Check your understanding:** Why is a dataset with names removed often still personal data? What does k-anonymity fail to protect against? Why did the US Census Bureau move to differential privacy for 2020?

### Chapter 8 · DPDP Act and Rules for analysts (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 The framework | Act enacted 11 Aug 2023; Rules notified 14 Nov 2025; 18-month phased compliance; Data Fiduciary, Data Processor, Data Principal, Consent Manager, Data Protection Board | One-page summary in your own words, with sources |
| 8.2 Principles in analysis | Consent and notice, purpose limitation, data minimisation, accuracy, storage limitation, security safeguards, accountability | Review an analysis plan against each principle |
| 8.3 Rights and requests | Access, correction, updating, erasure and nomination; responses within 90 days; propagating erasure to analytics tables and extracts | A query pack that finds every copy of one person's data in your warehouse |
| 8.4 Breaches, children and SDFs | Breach notification to the Board and affected people; verifiable parental consent for children's data; Significant Data Fiduciaries' audits and impact assessments; penalties up to ₹250 crore | Tabletop: an analyst's laptop with a customer extract is lost |
| 8.5 Global comparison | GDPR concepts analysts meet (lawful bases, DPIAs, anonymisation standard) | Map 5 DPDP duties to their GDPR counterparts |

**Check your understanding:** How does purpose limitation constrain reusing marketing data for a credit model? Why is erasure hard in analytics systems, and how do you design for it? What would you do in the first hour after discovering a customer extract was emailed to the wrong person?

### Chapter 9 · Privacy-preserving analysis in practice (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Aggregation rules | Minimum cell sizes, complementary suppression, rounding; publishing tables safely | Apply a suppression policy to a district-level table |
| 9.2 Minimised datasets | Purpose-built analysis tables without direct identifiers; retention dates | Build a minimised mart for a churn analysis |
| 9.3 Synthetic data | Uses for testing and teaching; memorisation and leakage risks | Generate synthetic data; test for copied records |
| 9.4 Clean rooms and secure sharing | Aggregate-only joins between companies; query restrictions | Design a clean-room analysis between a retailer and an advertiser (illustrative) |

**Check your understanding:** Why does suppressing one small cell often require suppressing others? When is synthetic data not safe to share? What does a clean room protect, and what can still leak?

### Chapter 10 · Reproducibility and auditability (weeks 10–11)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Why analyses fail to reproduce | Hidden notebook state, missing dependencies, changed data (Pimentel et al., 2019) | Try to rerun 5 public notebooks; log why each fails |
| 10.2 Reproducible by design | Git, lock files, containers, parameterised notebooks, data snapshots and as-of queries, seeds | Make one of your past projects rebuild from scratch |
| 10.3 Review | Analysis review checklists, second-analyst replication for high-stakes numbers | Replicate a classmate's key result independently |
| 10.4 Audit trails | For numbers that go to boards, regulators or investors: source, query, version, approver | An audit file for one board-pack metric |
| 10.5 Documentation | Methods notes, decision logs, The Turing Way practices | A methods note for your P3 |

**Check your understanding:** Why does "it worked on my machine" not satisfy an auditor? What is the cheapest step that gives the most reproducibility? Which numbers deserve independent replication before they are published?

### Chapter 11 · Governing AI in analytics (week 12)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 AI use policy | Which data may go to which AI tools; enterprise vs consumer accounts; logging; prohibited uses | Write a one-page policy for an analytics team |
| 11.2 Data flows and residency | Where prompts and data are processed; Power BI's cross-region processing setting; DPDP implications | Data-flow diagram for one copilot deployment |
| 11.3 Governing AI answers | Verified answers, certified metrics, labels on AI-generated numbers, approval and expiry | An approval workflow for verified answers |
| 11.4 Risk frameworks | NIST AI Risk Management Framework (AI 100-1) and ISO/IEC 42001 in outline; what applies to an analytics team | Map your policy to NIST AI RMF functions (govern, map, measure, manage) |

**Check your understanding:** Why is pasting a customer extract into a consumer AI chat a governance incident? Who approves a verified answer, and how often should it be reviewed? What does "measure" mean in the NIST AI RMF for an analytics assistant?

### Chapter 12 · Running a governance programme (weeks 13–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 12.1 Measuring governance | Certified datasets, quality scores, incident counts and time to resolve, access-review completion | A governance metrics page |
| 12.2 Prioritising | Start with the metrics that reach leadership and regulators; avoid boiling the ocean | A 90-day governance plan |
| 12.3 Making the case | Governance framed as speed and trust; cost of incidents | A 5-minute pitch to a leadership panel |
| 12.4 Final review | P3 presentation and defence | Panel review |

**Check your understanding:** Which governance metric would convince a CFO? Why should a governance programme start small? What would make you stop a governance initiative?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Incident case and RACI | — |
| 2 | 2 | Lab 2 · Glossary and certified metrics | — |
| 3 | 3 | Lab 3 · Revenue reconciliation | **P1 due** |
| 4 | 4 | Lab 4 · Quality checks and scorecard | — |
| 5 | 5 | Lab 5 · Incident simulation | Post-mortem |
| 6 | 6 | Lab 6 · RLS, masking and access review | Mid-term (AI off) |
| 7 | 7 | Lab 7 · Re-identification and k-anonymity | — |
| 8 | 8 | Lab 8 · DPDP rights query pack | — |
| 9 | 9 | Lab 9 · Suppression and minimised marts | **P2 due** |
| 10 | 10 | Lab 10 · Reproduce or fail | — |
| 11 | 10 | Lab 10 (cont.) · Audit file | — |
| 12 | 11 | AI policy and data flows | Policy |
| 13 | 12 | Governance plan | — |
| 14 | 12 | Leadership pitch | **P3 due** |
| 15 | Review | Panel defence | Final exam (AI off): cases |

## Working with AI in this course

- **Use AI for:** first drafts of glossary entries and metric definitions (then corrected by owners); generating synthetic test data; drafting policies you then check against the DPDP Act and Rules; writing quality-check code; summarising long regulatory texts, with every claim traced to the primary text.
- **Do without AI (drills):** classifying personal data; reconciliation bridges; deciding suppression; incident triage; reading the Act and Rules yourself for the sections you cite; the mid-term and final.
- **Verify AI output by:**
  - checking every legal statement against the primary text or an official government summary, never a blog;
  - testing access controls with real test users rather than trusting configuration screenshots;
  - running k-anonymity and uniqueness checks on any table an assistant calls "anonymised";
  - rerunning analyses from a clean environment.
- **Where AI still fails here:** assistants confidently describe privacy law from other jurisdictions as if it applied in India, call hashed identifiers "anonymous", and invent compliance deadlines. In this course, every legal claim needs a primary source, and every "anonymised" table needs a measured re-identification check. Log each AI error you find.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (10) | 20% |
| Projects P1 · P2 · P3 | 10% · 20% · 25% |
| Mid-term (AI off) | 10% |
| Final exam (AI off): governance cases + viva | 15% |

**Mastery gate.** You pass when you can, with AI off: (1) reconcile two systems' versions of a metric and present the bridge in 45 minutes; (2) classify the personal data in an unseen dataset, explain the re-identification risk, and propose a minimised, suppressed release in 30 minutes; (3) walk through the DPDP duties that apply to a described analysis (notice, purpose, retention, rights requests, breach handling) with references to the Act or Rules; (4) rebuild a provided analysis from scratch and document why it did or did not reproduce.

## Industry reality

Banks, insurers, fintechs and healthcare organisations in India already work under sector rules (for example, RBI's 2018 directive on storage of payment system data) and now the DPDP framework. Product companies are building consent, retention and deletion into their analytics stacks during the phased-compliance window. Analytics leads are expected to own certified metrics, quality scorecards and access reviews, and increasingly AI-use policies. Interviewers for senior analyst and analytics-engineering roles ask about data quality incidents, definition conflicts and handling personal data.

**Interview questions from this course**

1. *"Two dashboards show different revenue for last month. Walk me through it."* Strong answer: gets both definitions and queries; builds a reconciliation bridge (refunds, taxes, cut-off, time zone, currency, test orders); fixes the source or definition; certifies one metric; communicates the change.
2. *"We hashed phone numbers, so the dataset is anonymous, right?"* Strong answer: no; the space of mobile numbers is small enough to enumerate, so an unkeyed hash is reversible; at best it is pseudonymous personal data; proposes keyed tokenisation, minimisation and aggregation.
3. *"A customer asks us to delete their data. What happens in analytics?"* Strong answer: locate all copies (warehouse, marts, extracts, BI caches, backups policy); delete or anonymise per policy; keep proof of action; design pipelines so erasure propagates; respond within DPDP timelines.
4. *"How do you know your data is good enough?"* Strong answer: fitness for a specific use; quality dimensions with tests and thresholds; scorecards; incident history; reconciliation to trusted sources.
5. *"Can I paste this customer file into an AI tool to clean it?"* Strong answer: depends on the tool's contract, data residency and the team's AI policy; prefer an approved enterprise tool with no training on inputs; minimise and remove identifiers first; log the use; if in doubt, don't.

## Resources (free first)

- **Law and policy:** [MeitY data protection framework](https://www.meity.gov.in/data-protection-framework) (DPDP Act, 2023 and Rules, 2025); PIB, [DPDP Rules, 2025 Notified](https://static.pib.gov.in/WriteReadData/specificdocs/documents/2025/nov/doc20251117695301.pdf) (17 Nov 2025); [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework).
- **Quality and governance tools:** [dbt data tests](https://docs.getdbt.com/docs/build/data-tests); [Great Expectations](https://docs.greatexpectations.io/docs/); [Soda](https://docs.soda.io/); [OpenMetadata](https://open-metadata.org/); [OpenLineage](https://openlineage.io/).
- **Access control:** [Power BI row-level security](https://learn.microsoft.com/en-us/fabric/security/service-admin-row-level-security); [BigQuery column-level security](https://cloud.google.com/bigquery/docs/column-level-security-intro); [Snowflake dynamic data masking](https://docs.snowflake.com/en/user-guide/security-column-ddm-intro).
- **Privacy:** Sweeney, [Simple Demographics Often Identify People Uniquely](https://dataprivacylab.org/projects/identifiability/paper1.pdf) (2000); Narayanan and Shmatikov, [Netflix Prize de-anonymisation](https://arxiv.org/abs/cs/0610105); [US Census Bureau disclosure avoidance](https://www.census.gov/programs-surveys/decennial-census/decade/2020/planning-management/process/disclosure-avoidance.html); [OpenDP](https://opendp.org/).
- **Reproducibility:** [The Turing Way](https://book.the-turing-way.org/); Pimentel et al., [A Large-scale Study about Quality and Reproducibility of Jupyter Notebooks](https://2019.msrconf.org/details/msr-2019-papers/36/A-Large-scale-Study-about-Quality-and-Reproducibility-of-Jupyter-Notebooks) (MSR 2019).
- **Paid, optional:** DAMA International, *DAMA-DMBOK: Data Management Body of Knowledge*, 2nd ed.

## Sources

All checked 12 Oct 2026.

- PIB, "DPDP Rules, 2025 Notified" backgrounder (17 Nov 2025): notification on 14 Nov 2025, Act enacted 11 Aug 2023, 18-month phased compliance, penalties, 90-day response to rights requests — https://static.pib.gov.in/WriteReadData/specificdocs/documents/2025/nov/doc20251117695301.pdf
- dbt Labs, 2025 State of Analytics Engineering — https://www.getdbt.com/resources/state-of-analytics-engineering-2025
- Microsoft Learn, Copilot for Power BI overview (tenant setting for processing outside the geographic region) — https://learn.microsoft.com/en-us/power-bi/create-reports/copilot-introduction
- Pimentel, Murta, Braganholo and Freire, MSR 2019 — https://2019.msrconf.org/details/msr-2019-papers/36/A-Large-scale-Study-about-Quality-and-Reproducibility-of-Jupyter-Notebooks
- Kotak Neo, Eternal Q1 FY27 results (GOV to NOV) (22 Jul 2026) — https://www.kotakneo.com/news/stocks/eternal-q1-fy27-results-net-profit-rs-92-crore-revenue-rs-20211-crore-blinkit-growth/
- RBI, Storage of Payment System Data (6 Apr 2018) — https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=11244
- NIST, AI Risk Management Framework (AI 100-1) — https://www.nist.gov/itl/ai-risk-management-framework

_Last reviewed: 2026-10_
