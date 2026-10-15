# OV07 · Privacy Engineering

| Composed of | Overlap courses | Typical entry majors | Market pages |
|---|---|---|---|
| [DEN404](../../03_majors/data_engineering/year_4/DEN404_data_governance_lineage_and_privacy_engineering/README.md) × [SEC305](../../03_majors/cybersecurity_defense/year_3/SEC305_governance_risk_and_compliance/README.md) × [PRO301](../../05_shared_years_3_to_5/PRO301_professional_practice_ethics_law_and_responsible/README.md) | [OV07A](OV07A_privacy_by_design_and_privacy_enhancing/README.md), [OV07B](OV07B_data_protection_law_for_engineers_in_practice/README.md) | DEN, SEC, DSC, DAN, BE, MOB, CSG | [DEN](../../06_career_and_market_readiness/01_market_map/roles/DEN_data_engineering.md) · [SEC](../../06_career_and_market_readiness/01_market_map/roles/SEC_cybersecurity_defense.md) · [Market map](../../06_career_and_market_readiness/01_market_map/README.md) |

## The job this overlap maps to

A privacy engineer turns a legal duty or a user promise into a property of a system that can be tested. "We only use location for delivery" becomes a purpose tag that blocks a marketing pipeline. "We delete your account" becomes an erasure workflow that reaches backups, search indexes and embeddings. "We publish only aggregate statistics" becomes a differential-privacy release with a budget someone can audit.

Common titles: **Privacy Engineer**, **Privacy Software Engineer**, **Data Protection Engineer**, **Privacy Architect**, **Privacy and Data Governance Engineer**, and, at the senior end, **Head of Privacy Engineering** or a technical track that works beside the **Data Protection Officer (DPO)**. In smaller companies the same work sits inside data engineering, security or platform teams.

Day to day the work looks like this:

- reviewing designs for privacy risk before they ship, and writing the technical part of a data protection impact assessment (DPIA);
- building consent and purpose records, erasure and access-request pipelines, retention jobs and audit evidence;
- choosing and implementing privacy-enhancing technologies (PETs): pseudonymisation, differential privacy, federated learning, secure computation, trusted execution, synthetic data;
- answering engineers' questions about what the law actually requires, and answering lawyers' questions about what the system actually does.

**Demand evidence (checked October 2026).**

- **The law creates the work in India.** The Digital Personal Data Protection (DPDP) Rules, 2025 were notified on 13 November 2025. Consent-manager provisions start on 13 November 2026, and most data-fiduciary duties (notice, security safeguards, breach intimation, retention and erasure, children's data, data-principal rights) start on 13 May 2027 ([S.S. Rana, Nov 2025](https://ssrana.in/articles/meity-notifies-final-digital-personal-data-protection-rules-2025/)). In January 2026 the Ministry of Electronics and IT consulted industry on shortening the 18-month window to 12 months, mainly for significant data fiduciaries ([S.S. Rana, Feb 2026](https://ssrana.in/articles/meity-plans-to-cut-short-dpdp-compliance-timeline-and-notify-cross-border-restrictions-for-sdfs/)); whether that change was notified is (unconfirmed) as of October 2026, so check the Gazette.
- **Data teams already carry the duty.** This university's data-engineering role page lists handling personal data under the DPDP Act as part of the job and names privacy engineering as a specialisation ([DEN role page](../../06_career_and_market_readiness/01_market_map/roles/DEN_data_engineering.md)).
- **Security and governance skills are in demand, but narrowly.** Employers surveyed by the World Economic Forum expect Security Management Specialists among the fastest-growing jobs in India and globally ([WEF Future of Jobs 2025](https://reports.weforum.org/docs/WEF_Future_of_Jobs_Report_2025.pdf)); ISC2 found that security hiring wants specific skills rather than generic certificates ([ISC2 2025](https://www.isc2.org/Insights/2025/12/2025-ISC2-Cybersecurity-Workforce-Study)).
- **No official statistics count privacy engineers separately.** Treat any headline number for "privacy jobs" with care and read who was surveyed.

**Analysis.** Before DPDP, privacy work in India was concentrated in companies serving European users (GDPR) and in regulated sectors (RBI's payment-data rules, UIDAI's Aadhaar Data Vault rules). From 2027 every Indian company that processes digital personal data has engineering duties. The scarce person is the one who can read the Rules and also build the erasure pipeline.

## Why the overlap exists

Privacy fails at the seams between three groups:

| Group | What it knows | What it usually misses |
|---|---|---|
| Data engineers ([DEN404](../../03_majors/data_engineering/year_4/DEN404_data_governance_lineage_and_privacy_engineering/README.md)) | Where data flows: lineage, catalogs, masking, deletion across stores | Which flows are lawful, and which statistical releases still leak |
| Security and GRC ([SEC305](../../03_majors/cybersecurity_defense/year_3/SEC305_governance_risk_and_compliance/README.md)) | Controls, risk registers, audits, breach clocks | Re-identification, inference and purpose limits, which encryption alone does not solve |
| Ethics and law ([PRO301](../../05_shared_years_3_to_5/PRO301_professional_practice_ethics_law_and_responsible/README.md)) | Duties, rights and accountability | How a duty becomes a test, a log line or a budget |

The overlap adds what none of the three teaches in depth: the mathematics and engineering of PETs ([OV07A](OV07A_privacy_by_design_and_privacy_enhancing/README.md)), and the practice of turning data protection law into running systems and defensible decisions ([OV07B](OV07B_data_protection_law_for_engineers_in_practice/README.md)).

## Composed courses and sequencing

[`catalog.json`](../../catalog.json) sets the rules: OV07A and OV07B both require SEC305, PRO301 and [DEN301](../../03_majors/data_engineering/year_3/DEN301_data_modeling_and_warehousing/README.md), and list DEN404 as a co-requisite. DEN404 runs in semester 8, alongside OV07B. OV07A (semester 7) therefore teaches pseudonymisation and de-identification from first principles, and DEN404 then builds the platform controls on top.

| Semester | Composed and prerequisite courses | Overlap course | Notes |
|---|---|---|---|
| 5 (Y3) | PRO301, DEN301 | — | Non-DEN majors take DEN301 as an elective |
| 6 (Y3) | SEC305 | — | SEC305's DPDP and GDPR lessons are the legal base |
| 7 (Y4) | Optional: [SAR304](../../03_majors/security_architecture/year_3/SAR304_applied_cryptography_and_pki_for_architects/README.md) (cryptography) or [CSG402](../../03_majors/computer_science_general/year_4/CSG402_complexity_theory_and_theoretical_cryptography/README.md) | **OV07A** Privacy by Design and PETs | Most mathematical semester of the overlap |
| 8 (Y4) | DEN404 | **OV07B** Data Protection Law for Engineers in Practice | DEN404 and OV07B share a capstone dataset |
| 9–10 (Y5) | [THS501](../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md), [THS502](../../05_shared_years_3_to_5/THS502_thesis_or_capstone_ii/README.md) | Capstone below | Can be the thesis |

**If you come from:** data science or analytics, take [DAN404](../../03_majors/data_analysis/year_4/DAN404_data_governance_quality_and_privacy_for_analysts/README.md) or [DSC301](../../03_majors/data_science/year_3/DSC301_statistical_inference_and_modeling/README.md) for the statistics OV07A leans on; backend or mobile, take [BE305](../../03_majors/backend_engineering/year_3/BE305_authentication_authorization_and_backend/README.md) for access-control depth; security, add DEN301 early because erasure and lineage are data-platform problems.

## The two overlap courses

| Course | Semester | What it adds | Projects |
|---|---|---|---|
| [OV07A · Privacy by Design and Privacy-Enhancing Technologies](OV07A_privacy_by_design_and_privacy_enhancing/README.md) | 7 | LINDDUN threat modelling, minimisation patterns, de-identification and its failures, differential privacy (central, local, shuffle), privacy attacks on ML, DP-SGD, federated learning, secure computation, homomorphic encryption, trusted execution, synthetic data | [labs and projects](OV07A_privacy_by_design_and_privacy_enhancing/projects.md) |
| [OV07B · Data Protection Law for Engineers in Practice](OV07B_data_protection_law_for_engineers_in_practice/README.md) | 8 | Reading statutes as specifications, DPDP Act and Rules section by section, GDPR in operation, consent and dark-pattern law, children's data and age assurance, cross-border transfers, breach response, processors, AI and data protection, enforcement cases | [labs and projects](OV07B_data_protection_law_for_engineers_in_practice/projects.md) |

## Capstone brief: a privacy-engineered data product

**Scenario (illustrative).** A mid-size Indian health-and-wellness app (2 million users, mobile and web) wants to (a) publish monthly city-level wellness statistics, (b) train a recommendation model on usage data, and (c) be ready for its DPDP obligations on 13 May 2027. Build the privacy layer for it on a synthetic but realistic dataset you generate (at least 1 million users and 50 million events), with no real personal data.

**What you build:**

1. A LINDDUN threat model and a DPIA for the three uses, reviewed by a peer and the instructor.
2. A consent and purpose service: versioned notices, consent events, withdrawal, purpose tags on tables and pipelines.
3. A differentially private statistics release with user-level contribution bounds and a tracked privacy budget.
4. A model-training pipeline with DP-SGD or federated learning, plus a membership-inference audit.
5. Data-principal rights tooling: access export, correction, erasure (including backups by crypto-shredding), grievance tracking.
6. A breach drill: detection, triage, and the intimations the DPDP Rules require, produced against a simulated clock.

**Acceptance criteria (all measured and shown in the final report):**

- **Purpose enforcement:** a test suite proves that every pipeline reading a purpose-tagged column is rejected unless its declared purpose matches; zero bypasses across 20 planted violations.
- **Withdrawal:** consent withdrawal for a user stops all processing for the affected purposes within 15 minutes (p99 over 1,000 withdrawals), shown from logs.
- **Erasure:** an erasure request completes across at least six stores (OLTP, warehouse, lakehouse with time travel, search index, vector index, backups) within an internal SLO of 72 hours; a verification scan finds zero residual identifiers, and crypto-shredded backups are unreadable.
- **DP release:** total privacy loss per user per quarter is at most ε = 1 (or an equivalent zCDP ρ stated with its conversion), computed by a library accountant (OpenDP or equivalent), not by hand; for cells with true count ≥ 1,000, the median relative error is ≤ 5%.
- **ML privacy:** the trained model's membership-inference advantage (LiRA-style attack you run on your own model) is ≤ 0.05 at the stated ε, with the non-private baseline reported for comparison; utility loss against the non-private model is reported with a confidence interval.
- **Breach drill:** the team produces the affected-person notice and the detailed Board report in the format and timeline the Rules require (72 hours for the detailed report), with an evidence pack generated from logs.
- **Review:** an external reviewer (another team) finds no unmitigated "high" threat in the LINDDUN model after fixes.

## Roles it leads to

| Role | What you would own | Entry route from this overlap |
|---|---|---|
| Privacy Engineer / Privacy Software Engineer | Privacy reviews, PET implementations, rights tooling | Capstone + OV07A P3 |
| Data Protection Engineer (data platform) | Lineage, purpose, retention and erasure controls at scale | DEN major + OV07 |
| Privacy Architect | Organisation-wide patterns and standards; DPIA sign-off with the DPO | After 4–6 years in the role above |
| Applied privacy researcher | New DP mechanisms, audits, privacy attacks and defences | Year 5 thesis; [RES502](../../05_shared_years_3_to_5/RES502_reading_reproducing_and_extending_papers/README.md) |
| GRC engineer with a privacy focus | Evidence automation, audits, regulator responses | SEC major + OV07 |
| DPO track (with further legal study) | Accountability to the Data Protection Board and management | OV07B + legal qualification; this overlap alone is not legal training |

## Sources

All checked October 2026.

- S.S. Rana & Co., "MeitY notifies final Digital Personal Data Protection Rules 2025" (Nov 2025): commencement dates 13 Nov 2025, 13 Nov 2026, 13 May 2027. https://ssrana.in/articles/meity-notifies-final-digital-personal-data-protection-rules-2025/
- S.S. Rana & Co., "MeitY plans to cut short DPDP compliance timeline…" (13 Feb 2026): consultation of 23 Jan 2026, comments by 4 Feb 2026. https://ssrana.in/articles/meity-plans-to-cut-short-dpdp-compliance-timeline-and-notify-cross-border-restrictions-for-sdfs/
- World Economic Forum, *Future of Jobs Report 2025*. https://reports.weforum.org/docs/WEF_Future_of_Jobs_Report_2025.pdf
- ISC2, *2025 Cybersecurity Workforce Study* (Dec 2025). https://www.isc2.org/Insights/2025/12/2025-ISC2-Cybersecurity-Workforce-Study
- This repository's [market map](../../06_career_and_market_readiness/01_market_map/README.md) and [DEN role page](../../06_career_and_market_readiness/01_market_map/roles/DEN_data_engineering.md).

_Last reviewed: 2026-10_
