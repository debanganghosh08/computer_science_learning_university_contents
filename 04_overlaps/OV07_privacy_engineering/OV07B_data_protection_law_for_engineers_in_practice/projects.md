# OV07B · Labs and projects

Labs and projects use an illustrative company, **"Sehat Ledger"**, a fictional Indian health-and-payments app with 2 million users, an EU customer segment, three cloud vendors and an LLM-based support assistant. All data is synthetic. Legal outputs are graded on correct citation, sound reasoning and honest statements about what the system does; they are coursework, not legal advice. Lab 1, the mid-term and the final are done without AI assistants.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Requirements extraction (no AI) | Turn 20 provisions of the DPDP Act and Rules into requirements with exact citations, owners and test ideas | Requirement register (CSV) checked against the instructor key | 5 h |
| 2 · Grounds and notices | Map every processing activity to a DPDP ground (consent or section 7 use) and a GDPR lawful basis; rewrite the notice as itemised Rule 3 notices | Processing map; two notices; a list of activities with no valid ground | 5 h |
| 3 · Section 8 control matrix | Controls, evidence queries and owners for each section 8 duty, built with DEN404's platform | Matrix plus 10 working evidence queries | 6 h |
| 4 · GDPR records and LIA | Generate an Article 30 record from the catalog; write one legitimate-interests assessment | Record export; LIA | 4 h |
| 5 · Rights operations | Intake, verification, discovery across 5 stores, export, correction and erasure with exceptions | Working pipeline; timing report for 100 simulated requests | 8 h |
| 6 · Consent and dark-pattern audit | Audit a provided web and app flow for pre-consent tracking, asymmetry and the 13 patterns in India's 2023 guidelines | Findings with screenshots; fixed flow; before/after tag inventory | 5 h |
| 7 · Age assurance design | Two Rule 10 verifiable-consent flows and one selective-disclosure age check | Data-collected comparison; threat notes | 4 h |
| 8 · DPIA | Full DPIA for the LLM support assistant | DPIA reviewed by another student | 6 h |
| 9 · Transfer mapping | Classify 25 data flows by governing rule (GDPR Chapter V, DPDP s.16, RBI, CERT-In); write one transfer impact assessment | Flow register; TIA | 5 h |
| 10 · AI data register | Data-source and lawful-basis register for a fine-tuning set and a RAG index; retention rules for traces | Register; retention config; erasure procedure for RAG | 5 h |

## Projects

### P1 · DPDP readiness assessment with evidence (L1, ~6 hours)

**Real-world inspiration:** the phased DPDP commencement (13 Nov 2026 for consent managers, 13 May 2027 for most duties) and Rule 8(3)'s one-year log retention.

**What to build:** a readiness assessment for Sehat Ledger: a gap register against the Act and Rules, a dated remediation plan, and an evidence script that checks five controls automatically (for example log retention ≥ 1 year, encryption at rest on tagged tables, notice versioning, grievance contact published, erasure job running).

**Acceptance criteria:**
- Every gap cites a section or rule and is rated by penalty exposure (Schedule) and likelihood, with an owner and a date before 13 May 2027.
- At least 25 requirements assessed; at least 5 checked by a script that exits non-zero on failure and runs in CI.
- No regime confusion: a reviewer finds zero GDPR-only concepts presented as DPDP duties.
- A one-page summary for a non-technical executive states the top three risks and their cost to fix.

**Stretch goals:** a dashboard of control status over time; a change log that flags when a commencement date or rule changes.

**What it proves to an employer:** you can turn a new law into an engineering plan with evidence, not a slide deck.

### P2 · Data-principal rights service (L2, ~15 hours)

**Real-world inspiration:** DPDP sections 11–14 and Rule 14(3)'s 90-day limit; GDPR Articles 12, 15, 17 and 20 (one month, extendable).

**What to build:** a rights service for Sehat Ledger that handles access, correction, erasure, portability and grievances across at least six stores (PostgreSQL, warehouse, lakehouse with time travel, object storage, search index, vector index), with verified intake, lineage-driven discovery, exceptions (KYC and tax retention, legal hold, Rule 8(3) logs) and audit evidence.

**Acceptance criteria:**
- **Timeliness:** 500 simulated requests complete with p95 under 7 days and none over 30 days; the report compares this with the legal limits.
- **Completeness:** for 50 seeded test users, discovery finds 100% of planted records across all stores, including two planted in free-text fields.
- **Correct exceptions:** a decision table decides erase, restrict or retain; 20 edge cases (loan under KYC retention, legal hold, minor who turned 18) are handled as the table says, verified by tests.
- **Security:** a fraudulent-request test (wrong person requesting another's data) is blocked in 10 of 10 attempts; requests are rate-limited and logged.
- **Evidence:** every request produces an audit record that an auditor script can verify without access to the underlying personal data.

**Stretch goals:** consent-manager integration for withdrawal events; a nominee flow (section 14); a multilingual response template reviewed by a native speaker.

**What it proves to an employer:** you can operate the rights that most companies will be asked about first.

### P3 · Privacy case file for an AI feature (L3, portfolio-grade, ~30 hours)

**Real-world inspiration:** EDPB Opinion 28/2024 on AI models; Italy's Garante decision on OpenAI (Dec 2024); the Dutch authority's 2026 decision on Uber's automated deactivations (under appeal); DPDP Rule 13(3) algorithmic due diligence.

**What to build:** the complete case file for launching Sehat Ledger's LLM support assistant (retrieval over tickets plus a fine-tuned small model) in India and the EU: data map and lineage, grounds and lawful bases, notices, DPIA, transfer assessments for each vendor, processor-contract checklist, retention and redaction configuration for prompts and traces, rights handling for data in the index and the model, a breach playbook with a tabletop record, and an evidence pack. Then defend it before a panel acting as the Data Protection Board, counsel and an auditor.

**Acceptance criteria:**
- **Citations:** every legal statement cites the exact provision, rule, article or decision; a reviewer samples 30 and finds zero invented or misnumbered citations.
- **Truthfulness:** every claim about system behaviour links to code, configuration or a test; the panel picks 10 claims and each is demonstrated live.
- **DPIA quality:** at least 12 risks to people traced to controls and tests; residual risks have named owners; the reviewer accepts it after at most one revision.
- **Rights in AI:** an erasure request for a seeded user removes them from the retrieval index within 24 hours, with a test proving the assistant no longer retrieves their tickets; the document states honestly what happens to the fine-tuned model.
- **Breach readiness:** the tabletop produces the CERT-In report draft within 6 simulated hours and the DPDP detailed Board report within 72, from one fact base.
- **AI-error log:** at least eight documented AI legal errors you caught, each with the correct provision.

**Stretch goals:** a comparative memo on how the same feature would be treated under the UK GDPR; an automated check that blocks deployment when the DPIA is older than the last material change.

**What it proves to an employer:** you can take an AI feature through privacy review in two jurisdictions and stand behind every sentence.

## Feeds into

The OV07 capstone in the [overlap README](../README.md); [THS501](../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md) for a thesis on privacy compliance automation; [LCH502](../../../05_shared_years_3_to_5/LCH502_career_launch_and_founder_studio/README.md) for founders who must ship DPDP-ready products; and the interview loops in [06_career_and_market_readiness](../../../06_career_and_market_readiness/) for privacy and governance roles.
