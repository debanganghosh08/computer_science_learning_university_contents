# DAN404 · Labs and projects

All personal data in this course is synthetic or already public and aggregated. Never use real customer data from an employer or a leaked source. Every legal statement cites the DPDP Act, 2023, the DPDP Rules, 2025 or an official government summary, with the section or page. Every access-control claim is proved with test users, and every "anonymised" table comes with a measured re-identification check.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Incident case and RACI | Write up one public data-error case; build a RACI for 10 governance decisions | Case summary with sources; RACI table | 3 h |
| 2 · Glossary and certified metrics | 20 glossary terms linked to columns and semantic-layer metrics; 8 certified definitions using the full template | Glossary, definitions, and a change-control log with one processed change | 4 h |
| 3 · Revenue reconciliation | Reconcile a "product" revenue figure to a "finance" figure for one month on your DAN304 warehouse | Step-by-step bridge, tolerance policy, and automated cross-system tests | 4 h |
| 4 · Quality checks and scorecard | 20 checks across the six quality dimensions in dbt tests, Great Expectations or Soda; KPI anomaly alerts | Checks, a scorecard dashboard, and the measured false-alarm rate of your alerts | 5 h |
| 5 · Incident simulation | A classmate breaks an upstream column; you detect, triage, assess impact through lineage, communicate and fix | Incident timeline, impact report, blameless post-mortem with owned actions | 4 h |
| 6 · RLS, masking and access review | Row-level security in Power BI or the warehouse, a masked column, and a quarterly access review of an illustrative grants list | Test-user evidence for 3 roles; review findings and revocations | 4 h |
| 7 · Re-identification, k-anonymity and DP | Measure uniqueness of quasi-identifiers in a synthetic Indian customer table; reach 5-anonymity; release noisy counts with OpenDP at two budgets | Uniqueness before/after, information loss, DP error by budget | 5 h |
| 8 · DPDP rights query pack | Queries that find every copy of one person's data across warehouse tables, marts, snapshots and extracts; an erasure procedure | Query pack, erasure run log, and proof that downstream marts no longer contain the person | 4 h |
| 9 · Suppression and minimised marts | Apply small-cell and complementary suppression to a district table; build a minimised churn-analysis mart with retention dates | Suppressed table with rule; mart DDL with column-by-column justification | 3 h |
| 10 · Reproduce or fail | Rerun 5 public notebooks and log failures; make one past project rebuild from scratch; assemble an audit file for one board-pack metric | Failure log, a clean rebuild in a container, and the audit file | 5 h |

## Projects

### P1 · Certified metric catalogue with reconciliation (L1, ~6 hours)

**Real-world inspiration.** When Eternal moved its primary operating metric from GOV to NOV in 2026, every downstream comparison needed a definition note and a reconciliation. Internal metric changes in any company need the same discipline.

**What to build.** On your DAN304 warehouse (or Olist in DuckDB): a catalogue of 10 certified metrics with full definitions, owners and versions; a reconciliation between two legitimately different versions of one metric (for example, gross vs net revenue, or order-date vs delivery-date revenue); and a change-control record for one definition change, including a restatement note.

**Acceptance criteria**
- Each definition specifies formula, grain, filters, exclusions, time zone, owner, source of record and version.
- Each certified metric is implemented once (semantic layer or a single model) and a test proves dashboards use that implementation.
- The reconciliation bridge explains 100% of the difference in named steps, or states the unexplained residual and why it is accepted.
- The restatement note shows old and new values for at least 6 periods.

**Stretch goals.** Publish the catalogue as a docs site with lineage links; add an automated check that flags any dashboard computing a certified metric locally.

**What it proves to an employer.** You can end "which number is right?" arguments with definitions, ownership and arithmetic.

### P2 · Privacy review and safe data release (L2, ~15 hours)

**Real-world inspiration.** Analysts are often asked to share data with a partner, a vendor, a research team or the public. Re-identification research (Sweeney, 2000; Narayanan and Shmatikov, 2008) shows that removing names is not enough. The DPDP framework adds legal duties on purpose, minimisation and retention.

**What to build.** Generate a realistic synthetic customer dataset for an illustrative Indian lender or retailer (names, mobile numbers, pincodes, dates of birth, gender, transactions) of at least 200,000 people. Then produce:
1. A data classification of every column (direct identifier, quasi-identifier, sensitive, non-personal).
2. A re-identification risk assessment: uniqueness of quasi-identifier combinations, and a demonstration (on your synthetic data only) that unkeyed hashes of mobile numbers can be reversed by enumeration.
3. Two releases for a stated purpose: a minimised, generalised and suppressed microdata extract meeting k ≥ 5, and an aggregate table with differentially private noise.
4. A DPDP review memo: purpose, notice and consent assumptions, minimisation, retention period, rights handling, breach handling, with citations.

**Acceptance criteria**
- Uniqueness of the quasi-identifier combination is reported before and after treatment; the released extract has k ≥ 5 on the declared quasi-identifiers, verified by script.
- Information loss is measured (for example, the change in 3 analysis results computed on original vs released data).
- The DP release reports error at two privacy budgets and states which budget you recommend, and why.
- The hash-reversal demonstration runs only on your own synthetic data and concludes with the safe alternative (keyed tokenisation or no identifier at all).
- Every legal statement in the memo cites the Act, the Rules or the PIB summary.

**Stretch goals.** Add l-diversity on one sensitive attribute; generate synthetic data from the released extract and test it for copied records.

**What it proves to an employer.** You can share data usefully without exposing people, and explain the legal and technical reasoning to a privacy officer.

### P3 · Governance programme for an analytics team (L3, portfolio-grade, ~30 hours)

**Real-world inspiration.** Fintechs and consumer companies in India are building governance into their analytics during the DPDP phased-compliance window, while also rolling out AI copilots over their data. The company below is illustrative; build on your DAN304 P3 payments warehouse.

**What to build.**
1. **Definitions:** a glossary and 12 certified metrics in the semantic layer, with owners, versions and change control.
2. **Quality:** at least 40 checks across all six dimensions, anomaly alerts on 5 KPIs, a scorecard dashboard by dataset and owner.
3. **Access:** roles for at least 4 user groups, row-level security, masked columns for personal data, an access-request and quarterly-review procedure, and test-user evidence.
4. **Privacy:** data classification, minimised marts with retention dates, a DPDP rights query pack, and an erasure test that proves propagation to every downstream table.
5. **AI governance:** an AI-use policy, a data-flow diagram for one copilot or assistant (including where prompts are processed), a verified-answer approval workflow, and logging.
6. **Incidents and audit:** one simulated incident with a post-mortem, and an audit file for one board-pack metric that a second person reproduces independently.
7. **Programme:** governance metrics, a 90-day plan, and a 5-minute leadership pitch.

**Acceptance criteria**
- All checks, tests and the erasure test pass in CI from a clean clone.
- Test users for each role demonstrate correct access and denial on at least 10 queries each, including through the BI tool and through any AI assistant from DAN401.
- The scorecard shows quality scores for every public model, with an owner for each.
- The board-pack metric is reproduced by a classmate from your audit file alone, to the paisa.
- The AI-use policy names permitted tools, permitted data classes and logging requirements, and the data-flow diagram is consistent with vendor documentation.
- The leadership pitch states 3 measurable goals for the next 90 days.

**Stretch goals.** Add data contracts with the (simulated) upstream engineering team; integrate OpenMetadata or another catalogue; measure the time to answer a rights request end to end.

**What it proves to an employer.** You can run the trust layer of an analytics function: definitions, quality, access, privacy, reproducibility and AI use. That is what analytics leads and heads of data are hired to own.

## Feeds into

- [DAN501 Frontier Seminar](../../year_5/DAN501_frontier_seminar_decision_intelligence/README.md): governance of automated insights and decision systems.
- [OV07 Privacy Engineering](../../../../04_overlaps/OV07_privacy_engineering/README.md): privacy-enhancing technologies and data protection law in depth.
- [OV06B Semantic Layers and Self-Serve Analytics with AI](../../../../04_overlaps/OV06_data_platform_analytics_engineering/OV06B_semantic_layers_and_self_serve_analytics_with_ai/README.md): governed self-serve analytics at platform scale.
- [THS501 Thesis or Capstone I](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md): privacy-utility trade-offs on Indian public data are a strong research topic.
- [LCH502 Career Launch and Founder Studio](../../../../05_shared_years_3_to_5/LCH502_career_launch_and_founder_studio/README.md): DPDP-ready data practices for your own product.
