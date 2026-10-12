# DEN404 · Data Governance, Lineage and Privacy Engineering

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 4 · 8 | 4 (≈ 120 hours) | L3 → L4 | [DEN304](../../year_3/DEN304_orchestration_and_pipelines_airflow_and_dagster/README.md) | [OV07A](../../../../04_overlaps/OV07_privacy_engineering/OV07A_privacy_by_design_and_privacy_enhancing/README.md), [OV07B](../../../../04_overlaps/OV07_privacy_engineering/OV07B_data_protection_law_for_engineers_in_practice/README.md), [DEN501](../../year_5/DEN501_frontier_seminar_real_time_ai_data_systems/README.md) |

Part of the [Data Engineering major](../../README.md). Governance used to mean policy documents. On a modern data platform, it means controls in code: catalogs that know what every column contains, lineage that shows where personal data flows, access policies enforced by the engine, masking and tokenisation, retention jobs, and erasure pipelines that can prove they worked. This course builds those controls and maps them to India's Digital Personal Data Protection (DPDP) Act 2023 and Rules 2025, sectoral rules from the RBI and UIDAI, and the EU's GDPR. Ethics and law in general are taught in [PRO301](../../../../05_shared_years_3_to_5/PRO301_professional_practice_ethics_law_and_responsible/README.md), and compliance programmes in [SEC305](../../../cybersecurity_defense/year_3/SEC305_governance_risk_and_compliance/README.md). Analysts' governance duties are in [DAN404](../../../data_analysis/year_4/DAN404_data_governance_quality_and_privacy_for_analysts/README.md). This course is the engineering side. Nothing here is legal advice: engineers implement controls that lawyers and data protection officers interpret.

## Why this course matters now

India's privacy regime is arriving in stages. The DPDP Rules 2025 were notified on 13 November 2025. Data Protection Board provisions applied at once. Consent-manager obligations apply from November 2026. Most duties of data fiduciaries apply 18 months after notification, in May 2027. Those duties include security safeguards, breach reporting, retention and erasure, children's data, and the extra duties of significant data fiduciaries. Several duties land directly on data platforms. Processing logs must be kept for at least a year. Large e-commerce, gaming and social-media platforms must erase personal data three years after a user's last interaction, after warning the user at least 48 hours before. A detailed breach report is due to the Board within 72 hours. Sector rules are already in force. Since 2018, the RBI has required payment-system data to be stored only in India. UIDAI's Circular 14 of 2025 requires Aadhaar numbers to sit only in an encrypted Aadhaar Data Vault, with business systems holding reference keys, and it forbids using hashes of Aadhaar numbers as those keys. AI tools now classify columns, draft policies and propose lineage. None of them can be held accountable when a masked column leaks through a join or a deleted user survives in a lakehouse snapshot. Engineers who can build and prove these controls are scarce.

## Learning outcomes

By the end you can:

1. **Build** a metadata catalog with ownership, classification tags and a business glossary, and **keep** it accurate with automated scanning.
2. **Detect** personal data, including Indian identifiers, in tables and free text, with measured precision and recall, and **propagate** tags through lineage.
3. **Capture** table- and column-level lineage with OpenLineage across Airflow, Spark and dbt, and **answer** "where does this person's data flow?" from it.
4. **Implement** access control with RBAC, attribute- and tag-based policies, and row- and column-level security on a warehouse and a lakehouse, with access reviews and audit logs.
5. **Choose and implement** masking, tokenisation, format-preserving encryption, pseudonymisation and crypto-shredding for a stated threat, and **explain** what each leaks.
6. **Translate** DPDP Act and Rules 2025, RBI, UIDAI and GDPR obligations into concrete platform controls, with evidence an auditor can check.
7. **Engineer** retention and erasure end to end (warehouse, lakehouse snapshots, streams, backups, vector indexes, datasets), and **prove** completion.
8. **Model** consent and purpose as data, and **enforce** purpose-based access and consent withdrawal across pipelines.

## Chapters and lessons

### Chapter 1 · Governance as engineering (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Controls, not documents | Policy → control → evidence; preventive, detective and corrective controls; policy as code | Turn 5 written data policies into testable controls |
| 1.2 Roles | Data owner, steward, custodian, data protection officer; data fiduciary and processor (DPDP); controller and processor (GDPR) | Assign roles for every dataset in your DEN304 P3 platform |
| 1.3 Risk-based governance | Data inventories, classification tiers, threat models for data (insider misuse, over-broad access, re-identification, leaks through exports) | Threat-model a customer table and its 6 downstream copies |
| 1.4 What auditors ask for | Evidence: access logs, policy versions, lineage snapshots, deletion certificates, DPIA records | List the evidence your platform can produce today, and the gaps |

**Check your understanding:** (1) Why is a policy with no automated evidence weak in an audit? (2) Who is accountable for a dataset's classification, the owner or the engineer? (3) Which downstream copy of customer data is most often forgotten?

### Chapter 2 · Metadata, catalogs and classification (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Kinds of metadata | Technical, operational, business and social metadata; glossary terms vs physical columns | Map 20 glossary terms to physical columns across 3 systems |
| 2.2 Catalogs | DataHub, OpenMetadata, Unity Catalog, Apache Atlas; table catalogs (Polaris) vs governance catalogs | Deploy OpenMetadata or DataHub and ingest your warehouse, dbt and Airflow metadata |
| 2.3 Classification | Levels (public, internal, confidential, restricted), personal and sensitive data tags, tag inheritance | Design a classification scheme and tag 100 columns |
| 2.4 Keeping catalogs true | Automated ingestion, ownership checks, stale-asset detection, catalog quality metrics | Report the share of tier-1 assets with owner, description and classification |

**Check your understanding:** (1) Why do catalogs decay, and which automation slows it most? (2) What is the difference between a table catalog and a governance catalog? (3) Why should tags be inherited through lineage rather than applied by hand?

### Chapter 3 · Discovering personal data (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Detection methods | Patterns, checksums, context words, named-entity models; Microsoft Presidio; sampling strategies for large tables | Scan 50 tables with Presidio; measure precision and recall on a labelled sample |
| 3.2 Indian identifiers | Aadhaar (12 digits with a Verhoeff check digit), PAN format, mobile numbers, UPI addresses, IFSC codes, vehicle registration numbers | Write recognisers with validation; reduce false positives from phone-like numbers |
| 3.3 Free text and documents | PII in notes, tickets, PDFs and chat logs; scanning at scale with Spark; documents from [DEN403](../DEN403_data_engineering_for_ai_unstructured_data/README.md) | Scan 100,000 support tickets; report detections per type |
| 3.4 Tag propagation | Pushing classification through column-level lineage; derived columns (hashes, concatenations) that are still personal data | Show that a hashed mobile number column inherits the personal-data tag |

**Check your understanding:** (1) Why is a regular expression alone a poor Aadhaar detector? (2) Why is a hash of a 10-digit mobile number still personal data? (3) How do you choose a sample size for scanning a 5-billion-row table?

### Chapter 4 · Lineage (weeks 4–5)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 The OpenLineage model | Runs, jobs, datasets and facets; the event spec; an LF AI & Data project; Marquez as the reference backend | Emit lineage events by hand for a 3-step job; view them in Marquez |
| 4.2 Integrations | Airflow, Spark, dbt and Flink integrations; what each captures and misses | Instrument your DEN304 P3 platform end to end |
| 4.3 Column-level lineage | dbt v2 strict static analysis, SQL parsing with SQLGlot, Spark plan-based lineage; limits with UDFs and dynamic SQL | Build column lineage for 40 dbt models; find the 3 columns it cannot resolve |
| 4.4 Lineage for compliance | "Where does personal data flow?", records of processing, impact of a deletion or a policy change | Produce a personal-data flow map for one customer attribute |
| 4.5 Lineage gaps | Notebooks, spreadsheet exports, ad hoc scripts, reverse ETL; detecting unknown copies from query logs | Find 2 undeclared copies of a sensitive table from warehouse query history |

**Check your understanding:** (1) Why do runtime lineage events catch things SQL parsing misses, and the reverse? (2) What lineage do you need to prove that an erasure reached every copy? (3) Where do undeclared copies usually come from?

### Chapter 5 · Access control (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Models | RBAC, ABAC, tag-based policies, purpose-based access; least privilege; separation of duties | Design roles and policies for 6 personas, including an external auditor |
| 5.2 Enforcement in engines | Row access and column masking policies (Snowflake, BigQuery policy tags, Databricks row filters and column masks); Apache Ranger for Trino and Hadoop-era stacks | Implement the same policy on a warehouse and on Trino over Iceberg |
| 5.3 Requests, reviews and break-glass | Access requests with expiry, quarterly reviews, emergency access with logging | Build an access-request workflow with automatic expiry |
| 5.4 Audit logs | Who read what, when, through which tool; log retention (DPDP Rule 8 requires processing logs to be kept at least one year) | Answer "who queried this customer's row last month?" from audit logs |

**Check your understanding:** (1) Why does tag-based policy scale better than per-table grants? (2) How can a user defeat column masking through a join or an aggregate, and how do you prevent it? (3) What must a break-glass access leave behind?

### Chapter 6 · Masking, tokenisation and encryption (weeks 7–8)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Masking | Static vs dynamic masking, partial masking (last 4 digits), consistency across tables | Mask PAN and mobile numbers dynamically by role; verify each role's view |
| 6.2 Tokenisation | Token vaults, deterministic vs random tokens, detokenisation controls; UIDAI's Aadhaar Data Vault and reference keys (Circular 14 of 2025) | Build a token vault service; replace Aadhaar-like numbers with reference keys across 4 tables |
| 6.3 Encryption choices | Encryption at rest and in transit, envelope encryption with KMS, HSMs, format-preserving encryption (NIST SP 800-38G), deterministic encryption for joins and what it leaks | Implement deterministic encryption for a join key; show the frequency-analysis leak |
| 6.4 Hashing pitfalls | Low-entropy identifiers can be brute-forced from hashes; keyed hashes (HMAC) and their key management; why UIDAI forbids hashed Aadhaar numbers as reference keys | Recover phone numbers from unsalted SHA-256 hashes in a lab dataset; then fix it |
| 6.5 Pseudonymisation vs anonymisation | GDPR's distinction; re-identification by linkage; k-anonymity as an introduction (deeper methods in [OV07A](../../../../04_overlaps/OV07_privacy_engineering/OV07A_privacy_by_design_and_privacy_enhancing/README.md)) | Re-identify records in a "de-identified" dataset by linking quasi-identifiers |
| 6.6 Crypto-shredding | Per-subject keys; deleting the key to make backups and immutable copies unreadable | Implement per-customer keys for an event archive; shred one customer |

**Check your understanding:** (1) Why is "we hashed it" not anonymisation? (2) When is tokenisation better than encryption for analytics? (3) What does crypto-shredding solve that row deletion cannot, and what does it require from day one?

### Chapter 7 · India: DPDP Act 2023, DPDP Rules 2025 and sector rules (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 The DPDP model | Data principals, data fiduciaries, processors, consent managers, significant data fiduciaries, the Data Protection Board; consent and "legitimate uses"; notice | Map your platform's datasets to fiduciary and processor roles |
| 7.2 Timeline | Rules notified 13 Nov 2025; Board provisions immediate; consent managers from Nov 2026; most fiduciary duties from May 2027 | Build a compliance timeline for a mid-size Indian app (illustrative) |
| 7.3 Duties that hit the platform | Rule 6 security safeguards (encryption, masking or tokens, access control, logs); Rule 7 breach intimation (detailed report to the Board within 72 hours); Rule 8 retention (logs kept at least 1 year; Third Schedule erasure after 3 years of inactivity for e-commerce and social media with at least 2 crore users and online gaming with at least 50 lakh users, with a 48-hour warning); children's data (verifiable parental consent, no tracking or targeted ads); data principal rights | Turn each duty into a control, an owner and an evidence query |
| 7.4 Significant data fiduciaries | Periodic DPIA and audit, algorithmic due diligence, restrictions on moving certain data out of India (Rule 13) | Draft the data-platform section of a DPIA |
| 7.5 Sector rules | RBI's 2018 directive to store payment-system data only in India; UIDAI's Aadhaar Data Vault (AES-256 or stronger, HSMs at FIPS 140-2 Level 3, reference keys only in business systems) | Audit a sample fintech schema against RBI and UIDAI rules |

**Check your understanding:** (1) Which DPDP duties require changes to pipelines rather than to policies? (2) How do the 1-year log retention and the 3-year erasure rule interact for one user? (3) Why does UIDAI forbid hashed Aadhaar numbers as reference keys?

### Chapter 8 · GDPR and other regimes for data teams (week 10)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Principles | Lawfulness, purpose limitation, data minimisation, accuracy, storage limitation, integrity and confidentiality (Article 5); lawful bases (Article 6) | Check one pipeline against each principle |
| 8.2 Rights | Access, rectification, erasure (Article 17), restriction, portability (Article 20), objection; response handling at scale | Build a subject-access export from lineage and the catalog |
| 8.3 Engineering duties | Privacy by design and default (Article 25), records of processing (Article 30), security of processing (Article 32), breach notification to the authority within 72 hours (Article 33), DPIAs (Article 35), international transfers (Chapter V) | Generate a record of processing activities from catalog and lineage data |
| 8.4 Comparing regimes | DPDP vs GDPR: consent and legitimate uses vs six lawful bases, children's age thresholds, breach rules, transfers; AI-specific data-governance rules (EU AI Act Article 10 for high-risk systems; check its current application timeline) | Build a comparison table for a company operating in India and the EU |

**Check your understanding:** (1) Why does purpose limitation constrain reuse of data for AI training? (2) What is the engineering difference between restriction and erasure? (3) Which DPDP and GDPR duties can one control satisfy, and which need separate handling?

### Chapter 9 · Retention, deletion and erasure engineering (week 11)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Retention as code | Retention schedules per class of data, TTLs, partition expiry, legal holds, exceptions required by other laws | Implement retention for 10 tables with tests |
| 9.2 Erasure pipelines | Request intake and identity verification, discovery through lineage, deletion across stores, verification scans, certificates | Build an erasure orchestrator over warehouse, lakehouse and Kafka |
| 9.3 Hard places | Lakehouse snapshots and time travel ([DEN305](../../year_3/DEN305_lakehouse_architecture_parquet_iceberg_and_delta/README.md)), compacted topics, backups, caches, vector indexes and training datasets ([DEN403](../DEN403_data_engineering_for_ai_unstructured_data/README.md)) | Erase a user from an Iceberg table and its snapshots; prove absence in every data file |
| 9.4 Inactivity erasure | DPDP Third Schedule workflow: track last interaction, send the 48-hour intimation, erase unless the user returns, keep the required logs | Implement the workflow with a simulated clock and test edge cases |

**Check your understanding:** (1) Why must erasure verification scan data, not just check job status? (2) What do you do about personal data inside a model already trained? (3) How do legal holds override erasure, and how is that recorded?

### Chapter 10 · Consent and purpose as data (week 12)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Consent records | Versioned notices, purposes, timestamps, channel, withdrawal; consent as an append-only event log | Model consent as events and a current-state table |
| 10.2 Purpose tags | Purposes on columns, tables and pipelines; purpose-based access checks | Block a marketing pipeline from reading data collected only for fraud prevention |
| 10.3 Withdrawal propagation | Stopping processing, deleting or restricting downstream copies, honouring withdrawal within a set time | Withdraw consent for one user and trace every pipeline that stops |
| 10.4 Consent ecosystems | DPDP consent managers (registration from November 2026); the RBI-regulated Account Aggregator framework for consent-based financial data sharing | Sketch how a lender's data platform consumes Account Aggregator data with purpose and expiry |

**Check your understanding:** (1) Why should consent be stored as events rather than a boolean column? (2) What makes purpose-based access hard to enforce in SQL engines? (3) What must happen downstream within hours of a withdrawal?

### Chapter 11 · Governance for AI, audits and the capstone (weeks 13–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Training and retrieval data | Provenance, licences, consent and purpose for AI use; datasheets; excluding restricted data from embeddings and fine-tuning sets | Add AI-use flags to the catalog and enforce them in the DEN403 pipeline |
| 11.2 Processors and vendors | Contracts requiring equivalent safeguards, sub-processors, data-sharing agreements, residency | Review a vendor's data flow against your controls |
| 11.3 Automated audit evidence | Policy versions, access-review records, lineage snapshots, deletion certificates generated by the platform | Produce an evidence pack for a simulated audit in under 1 hour |
| 11.4 AI in governance work | Assistants classifying columns, drafting policies and DPIAs; measuring their accuracy and keeping humans accountable | Compare AI column classification with your labelled set |
| 11.5 Capstone review | Present P3 | Oral defence |

**Check your understanding:** (1) Which governance failure in an AI pipeline is hardest to undo? (2) What must an evidence pack show for an erasure claim to be believed? (3) Where is AI classification acceptable without review, if anywhere?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Policies to controls | Control list with evidence queries |
| 2 | 2 | Lab 2 · Catalog deployment | Catalog with ownership and tags |
| 3 | 3 | Lab 3 · PII discovery | Precision/recall report; **P1 due** |
| 4 | 4 | Lab 4 · OpenLineage end to end | Lineage graph |
| 5 | 4 | Lab 5 · Column lineage and gaps | Undeclared copies found |
| 6 | 5 | Lab 6 · Policies in two engines | Policy tests per persona |
| 7 | 6 | Lab 7 · Tokenisation and hashing pitfalls | Mid-term (AI off): controls and threats |
| 8 | 6 | Lab 8 · Crypto-shredding | Shredded customer proof |
| 9 | 7 | Lab 9 · DPDP control mapping | Duty → control → evidence table; **P2 due** |
| 10 | 8 | Lab 10 · GDPR records and subject access | RoPA and export |
| 11 | 9 | Lab 11 · Erasure across stores | Erasure certificate |
| 12 | 10 | Lab 12 · Consent and purpose | Withdrawal trace |
| 13 | 11 | Lab 13 · Audit evidence pack | Evidence pack |
| 14 | 11 | Capstone review | **P3 due** |
| 15 | Review | Oral defence of P3 | Final exam (AI off) |

## Working with AI in this course

- **Use AI for:** first-pass column classification and descriptions; drafting policy text and DPIA sections for human review; generating synthetic personal data for labs; summarising regulations as study notes, always checked against the primary text. Tools: Claude Code, GitHub Copilot, Cursor; catalog features that suggest classifications; warehouse assistants for metadata queries.
- **Do without AI (drills):** mapping a legal duty to a control and evidence (Lab 9); threat-modelling a masking or tokenisation design; reading the primary text of the DPDP Rules, GDPR articles and RBI and UIDAI circulars; the mid-term and final. Summaries of law drift from the text, and you must be able to check them.
- **Verify AI output by:** (1) labelled samples for every AI classification (precision and recall per class); (2) testing every policy from each persona's account, not by reading the policy; (3) scanning storage after any deletion; (4) quoting the primary legal text, with rule or article number, for every compliance claim.
- **Where AI still fails here (show it yourself):** in Lab 3 and Chapter 11, compare AI column classification with your labelled set and record the misses (hashed identifiers marked non-personal, free-text columns marked safe). In Lab 9, ask an assistant to summarise DPDP Rule 8 and Rule 7. Check every timeline and threshold against the notified text and record each discrepancy.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs 1–13 | 25% |
| Projects P1 / P2 / P3 | 5% / 12% / 18% |
| Mid-term (AI off) | 10% |
| Final exam (AI off) | 20% |
| Oral defence of P3 | 10% |

**Mastery gate.** You pass when you can, without AI: (1) given a platform and a list of DPDP, RBI and GDPR duties, produce the control, owner and evidence query for each, and defend the mapping to an examiner; (2) erase a named person from a provided platform (warehouse, lakehouse with snapshots, Kafka, a vector index, a backup) and prove absence by scanning; (3) find two planted governance defects (for example, a masked column exposed through a view, and an undeclared copy of a sensitive table) within 45 minutes using the catalog, lineage and audit logs.

## Industry reality

Data teams in India are preparing for the DPDP duties that apply from May 2027, alongside rules already in force: RBI's payment-data localisation since 2018 and UIDAI's Aadhaar Data Vault requirements, revised in November 2025. Common open-source building blocks include OpenLineage and Marquez for lineage, DataHub or OpenMetadata for catalogs, Unity Catalog OSS and Apache Polaris for table-level governance, Apache Ranger for policy enforcement in some stacks, and Presidio for PII detection. Engine-native policies (masking, row access, policy tags) on Snowflake, BigQuery and Databricks do most of the enforcement in cloud platforms.

**Interview questions from this course**

1. *"How would you handle PII on our data platform?"* A strong answer covers discovery with measured accuracy, classification and tag propagation, minimisation at ingestion, tokenisation or encryption by threat, dynamic masking by role, audit logs, retention and erasure, and the evidence each control produces.
2. *"Implement the right to erasure across a warehouse, a lakehouse and backups."* Cover identity resolution, lineage-driven discovery, deletes and snapshot expiry, compacted topics, crypto-shredding for backups, vector indexes and datasets, verification scans, and the certificate.
3. *"Masking, tokenisation or encryption: which and when?"* Cover the threat (insider, analyst, breach of storage), joinability needs, reversibility, key management, leakage from deterministic schemes, and examples such as UIDAI reference keys.
4. *"Design lineage for a platform with Airflow, Spark and dbt."* Cover OpenLineage events and facets, column-level lineage from dbt and plans, gaps (notebooks, exports), and uses for impact analysis and compliance.
5. *"What does the DPDP Act change for a data engineering team?"* Cover the roles, consent and notice, security safeguards, the 72-hour breach report, log retention and inactivity erasure, children's data, significant data fiduciary duties, the timeline to May 2027, and which pipelines must change.

## Resources (free first)

- **Primary legal texts:** [DPDP Act 2023](https://www.meity.gov.in/static/uploads/2024/06/2bf1f0e9f04e6fb4f8fef35e82c42aa5.pdf) (MeitY); DPDP Rules 2025 (G.S.R. 846(E), 13 Nov 2025; read the Gazette text); [GDPR](https://eur-lex.europa.eu/eli/reg/2016/679/oj) and article-by-article [gdpr-info.eu](https://gdpr-info.eu/art-17-gdpr/); RBI, [Storage of Payment System Data](https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=11244) (2018); UIDAI [Circular 14 of 2025](https://www.uidai.gov.in/images/Circular-No.14_of-2025.pdf) and [Aadhaar Data Vault FAQ](https://www.uidai.gov.in/images/FAQs_Aadhaar_Data_Vault_03112025_v10.pdf) (Nov 2025).
- **Standards:** NIST [SP 800-38G](https://csrc.nist.gov/pubs/sp/800/38/g/final) (format-preserving encryption).
- **Tools:** [OpenLineage](https://openlineage.io/docs/) and [facets](https://openlineage.io/docs/spec/facets/); [Marquez](https://marquezproject.ai/); [DataHub](https://github.com/datahub-project/datahub); [OpenMetadata](https://open-metadata.org/); [Apache Atlas](https://atlas.apache.org/); [Apache Ranger](https://ranger.apache.org/); [Unity Catalog OSS](https://docs.unitycatalog.io/); [Microsoft Presidio](https://microsoft.github.io/presidio/); [SQLGlot](https://github.com/tobymao/sqlglot).
- **Engine policies:** Snowflake [dynamic data masking](https://docs.snowflake.com/en/user-guide/security-column-ddm-intro); BigQuery [column data masking](https://cloud.google.com/bigquery/docs/column-data-masking-intro); Databricks [row filters and column masks](https://docs.databricks.com/aws/en/tables/row-and-column-filters).
- **Practitioner analysis (secondary, check against primary text):** S.S. Rana & Co., [notes on the DPDP Rules 2025](https://ssrana.in/articles/meity-notifies-final-digital-personal-data-protection-rules-2025/); Sansa Legal, [retention and erasure under the DPDP Rules](https://www.sansalegal.com/post/how-to-build-a-data-retention-and-erasure-schedule-under-the-dpdp-rules-2025).
- **Paid, worth it:** Nishant Bhajaria, *Data Privacy: A Runbook for Engineers* (Manning, 2022); Kleppmann and Riccomini, *Designing Data-Intensive Applications*, 2nd ed. (O'Reilly, 2026). Deeper privacy engineering continues in [OV07](../../../../04_overlaps/OV07_privacy_engineering/README.md).

## Sources

All checked October 2026. Legal summaries are for engineering orientation only; the notified texts govern.

- S.S. Rana & Co., "MeitY notifies final Digital Personal Data Protection Rules 2025": commencement on 13 Nov 2025 (Rules 1, 2, 17–21), 13 Nov 2026 (Rule 4), 13 May 2027 (Rules 3, 5–16, 22, 23); 72-hour breach limit; Rule 8(3) logs kept at least one year; Rule 13 significant data fiduciary duties. https://ssrana.in/articles/meity-notifies-final-digital-personal-data-protection-rules-2025/
- Sansa Legal, retention and erasure schedule under the DPDP Rules 2025: Third Schedule classes and thresholds (e-commerce and social media at least 2 crore registered users; online gaming at least 50 lakh), three-year period, Rule 8(2) 48-hour intimation, G.S.R. 843(E) and 846(E). https://www.sansalegal.com/post/how-to-build-a-data-retention-and-erasure-schedule-under-the-dpdp-rules-2025
- UIDAI, Circular No. 14 of 2025 (4 Nov 2025): Aadhaar Data Vault, reference keys only in business databases, hashing not allowed as reference keys, AES-256 or higher, HSMs FIPS 140-2 Level 3, supersedes the 25 Jul 2017 circular. https://www.uidai.gov.in/images/Circular-No.14_of-2025.pdf
- Reserve Bank of India, "Storage of Payment System Data", RBI/2017-18/153 (6 Apr 2018). https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=11244
- GDPR Articles 5, 6, 17, 20, 25, 30, 32, 33, 35. https://gdpr-info.eu/
- OpenLineage README (LF AI & Data Foundation graduate project; Marquez as an LF AI & Data project). https://github.com/OpenLineage/OpenLineage

_Last reviewed: 2026-10_
