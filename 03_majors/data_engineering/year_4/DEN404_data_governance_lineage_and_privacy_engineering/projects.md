# DEN404 · Labs and projects

All personal data in these labs is synthetic. A provided generator creates an Indian consumer-app dataset with names, addresses, mobile numbers, PAN-format and Aadhaar-format numbers (with valid check digits), UPI addresses and free-text support tickets. Never use real personal data for coursework. The stack: PostgreSQL, a warehouse free tier, Iceberg on MinIO with Trino, Kafka, Airflow, dbt, Marquez, OpenMetadata or DataHub, and Presidio. Labs 7 and 9 are done without AI assistants.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Policies to controls | Turn 5 written policies into controls with automated evidence queries | Control table and the queries | 3 h |
| 2 · Catalog deployment | Deploy OpenMetadata or DataHub; ingest warehouse, dbt and Airflow metadata; set owners and tags | Catalog with coverage report for tier-1 assets | 5 h |
| 3 · PII discovery | Presidio plus custom recognisers for Indian identifiers on tables and tickets; compare with an AI classifier | Precision/recall per identifier type; misses analysed | 5 h |
| 4 · OpenLineage end to end | Emit lineage from Airflow, Spark and dbt into Marquez | Lineage graph and the events for one run | 4 h |
| 5 · Column lineage and gaps | Column lineage for 40 dbt models; find undeclared copies from query history | Lineage export; list of undeclared copies with evidence | 4 h |
| 6 · Policies in two engines | Tag-based masking and row policies on a warehouse and on Trino over Iceberg; test as 6 personas | Per-persona test results; one bypass found and fixed | 5 h |
| 7 · Tokenisation and hashing pitfalls | Build a token vault with reference keys; brute-force unsalted phone-number hashes; fix with keyed hashing | Vault code, recovery rate before and after the fix | 5 h |
| 8 · Crypto-shredding | Per-customer keys for a Kafka event archive and its backup; shred one customer | Proof that the shredded customer's events are unreadable everywhere | 4 h |
| 9 · DPDP control mapping | Map DPDP Rules 6, 7, 8 and 13, the RBI 2018 directive and UIDAI Circular 14 of 2025 to controls, owners and evidence | Mapping table citing rule numbers from the primary text | 4 h |
| 10 · GDPR records and subject access | Generate a record of processing from catalog and lineage; build a subject-access export | RoPA document and one complete export | 4 h |
| 11 · Erasure across stores | Erase one user from warehouse, Iceberg (with snapshots), Kafka compacted topic and a vector index | Erasure certificate and a scan report | 5 h |
| 12 · Consent and purpose | Consent as events, purpose tags, purpose-based access; withdraw consent and trace effects | Withdrawal trace across pipelines | 4 h |
| 13 · Audit evidence pack | Produce an evidence pack for a simulated audit within 1 hour | The pack and a timing log | 3 h |

## Projects

### P1 · Personal-data discovery for an Indian consumer app (L1, ~6 hours)

**Real-world inspiration:** every privacy programme starts with an inventory of where personal data lives, and under the DPDP Rules 2025 security safeguards such as masking and access control depend on knowing which columns to protect. Indian identifiers need validation logic, not just patterns. The dataset is synthetic.

**What to build:** a scanner that samples every table and text column in the synthetic app database (about 40 tables) and detects:

- names, mobile numbers, email addresses, PAN-format and Aadhaar-format numbers (with check-digit validation), UPI addresses, IFSC codes and postal addresses;
- the same identifiers inside free-text support tickets.

The scanner writes classification tags to the catalog.

**Acceptance criteria:**
- On a provided labelled set of 500 columns and 2,000 ticket snippets, precision is at least 0.9 and recall at least 0.85 for each structured identifier type. Free-text results are reported honestly with an error analysis.
- Aadhaar-format detection rejects numbers that fail the check digit; this is shown with test cases.
- Hashed and concatenated derivatives of identifiers are tagged as personal data.
- A coverage report shows the share of columns scanned, sampled rows per table and run time.

**Stretch goals:** an AI classifier as a second opinion, with agreement measured; incremental scanning that only re-scans changed tables.

**What it proves to an employer:** you can find personal data reliably, which every governance control depends on.

### P2 · Lineage-driven access control (L2, ~15 hours)

**Real-world inspiration:** platforms with hundreds of tables cannot be governed by hand-written grants. Tag-based policies, applied by the engine and propagated through lineage, are how cloud platforms (Snowflake masking policies, BigQuery policy tags, Databricks column masks) and open stacks (Apache Ranger) scale access control.

**What to build:** governance for your DEN304 P3 platform, or a provided equivalent:

- OpenLineage from Airflow, Spark and dbt into Marquez;
- column-level tag propagation from P1's classifications;
- tag-based masking and row-level policies on one warehouse and on Trino over Iceberg;
- an access-request workflow with expiry and approval;
- audit-log queries;
- a detector for undeclared copies of sensitive tables, using query history.

**Acceptance criteria:**
- **Propagation:** every downstream column derived from a tagged column carries the tag, verified on 40 models. Each failure, such as an unresolved UDF, is listed with a manual fix.
- **Enforcement:** for 6 personas × 20 sensitive columns, each persona sees exactly the intended values (clear, masked or no access) on both engines. The test runs in CI.
- **Bypass resistance:** three provided bypass attempts (a join to an unmasked copy, an aggregate that reveals a single row, a view created by a privileged user) are blocked or detected.
- **Access hygiene:** temporary access expires automatically and is visible in a review report.
- **Audit:** the query "who read customer X's row in the last 30 days" returns a correct answer in under 1 minute.
- **Copies:** at least 2 planted undeclared copies are found from query history.

**Stretch goals:** purpose-based access for one dataset; publishing lineage and tags to a second catalog.

**What it proves to an employer:** you can make access control automatic, testable and auditable across engines.

### P3 · DPDP-ready data platform (L3, portfolio-grade, ~30 hours)

**Real-world inspiration:** India's DPDP Rules 2025 bring most data-fiduciary duties into force in May 2027: security safeguards, breach reporting, retention and erasure (including three-year inactivity erasure with a 48-hour warning for e-commerce, social media and gaming platforms above set user counts), and children's data protections. Sector rules already apply: RBI's payment-data localisation and UIDAI's Aadhaar Data Vault requirements (Circular 14 of 2025). The company and data here are illustrative and synthetic. Treat the scenario as a large e-commerce platform within the Third Schedule thresholds.

**What to build:** governance controls for the synthetic app's platform (PostgreSQL, Kafka, Iceberg, a warehouse, a vector index for support search, and backups):

- consent and purpose as event data, with purpose-based access and withdrawal propagation;
- a token vault so that Aadhaar-format numbers exist only in an encrypted vault, with business tables holding non-hash reference keys;
- crypto-shredding for the event archive and backups;
- retention as code for 10 data classes, including the 1-year minimum for processing logs;
- the inactivity-erasure workflow (track last interaction, send the 48-hour intimation, erase unless the user returns);
- an erasure orchestrator for data principal requests across every store;
- a breach drill that drafts the Board report from logs and lineage;
- an automated evidence pack.

**Acceptance criteria:**
- **Vault:** a scan of all business tables, logs and topics finds zero Aadhaar-format numbers outside the vault. Reference keys cannot be reversed without the vault: no hashes are used, and a test proves it.
- **Erasure:** for 5 data principals (2 by request, 3 by inactivity), the orchestrator removes or crypto-shreds their data in every store, including Iceberg snapshots, the compacted topic, the vector index and backups. Scans find no readable trace. Processing logs required by retention rules are kept and marked as such.
- **Inactivity workflow:** with a simulated clock, users who return within 48 hours of the intimation are not erased. Users who do not return are erased on schedule. Edge cases (time zones, retries of failed intimations) are tested.
- **Consent:** a withdrawal stops all purpose-bound pipelines for that user within 1 hour (simulated), shown in run history.
- **Breach drill:** from a simulated exfiltration of one table, the platform produces within 2 hours a draft report listing affected principals, data categories, time window and containment steps, drawn from audit logs and lineage.
- **Evidence:** an evidence pack (policy versions, access reviews, lineage snapshot, erasure certificates, retention runs) is generated in under 1 hour. Every control maps to a cited rule or article.
- **Write-up:** design document, the control-to-rule mapping, a threat model, and a 5-minute recorded walkthrough of an erasure with its proof.

**Stretch goals:** a DPIA for the platform as a significant data fiduciary; differential-privacy aggregates for one analytics table (preview of [OV07A](../../../../04_overlaps/OV07_privacy_engineering/OV07A_privacy_by_design_and_privacy_enhancing/README.md)); RBI-compliant residency checks for payment tables in CI.

**What it proves to an employer:** you can turn privacy law into working, provable platform controls. As the DPDP deadlines approach, Indian employers have few people who can do this.

## Feeds into

- [OV07A Privacy by Design and Privacy-Enhancing Technologies](../../../../04_overlaps/OV07_privacy_engineering/OV07A_privacy_by_design_and_privacy_enhancing/README.md) and [OV07B Data Protection Law for Engineers in Practice](../../../../04_overlaps/OV07_privacy_engineering/OV07B_data_protection_law_for_engineers_in_practice/README.md): this course is their entry requirement.
- [DEN501 Frontier Seminar](../../year_5/DEN501_frontier_seminar_real_time_ai_data_systems/README.md): governance for real-time AI data systems.
- [OV10 FinTech Systems Engineering](../../../../04_overlaps/OV10_fintech_systems_engineering/README.md): RBI and UIDAI controls in payment systems.
- [LCH502 Career Launch and Founder Studio](../../../../05_shared_years_3_to_5/LCH502_career_launch_and_founder_studio/README.md): compliance tooling for DPDP is a credible product area for founders.
