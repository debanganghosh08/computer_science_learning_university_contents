# SEC305 · Labs and projects

GRC work is judged by evidence, so every lab and project is submitted as a Git repository of documents in Markdown (or exported PDFs), scripts and data, with a change history. Scenarios are illustrative unless a public source is cited. Use primary legal texts for every regulatory claim and note the date you checked them. Where a lab uses a cloud account or identity tenant for evidence automation, use your own free-tier or test account.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Governance charter | Charter, risk appetite statement and RACI for security in an illustrative digital lender | Charter, appetite statement, RACI with three lines marked | 3 h |
| 2 · CSF profile and mapping | Current and target NIST CSF 2.0 profiles for a 50-person SaaS company; crosswalk 15 controls to ISO 27001 Annex A and CIS Controls v8.1 | Profiles, crosswalk table, top five gaps | 4 h |
| 3 · Risk register | 15 risks for an illustrative hospital with owners, likelihood, impact and treatment | Register with reasons for each rating | 3 h |
| 4 · FAIR Monte Carlo | Quantify one ransomware risk with calibrated ranges and 10,000 simulations; compare two treatments | Python notebook, loss exceedance curve, sources or "(unconfirmed)" for each input | 5 h |
| 5 · Scope and SoA | ISMS scope for a payments startup; SoA for 30 Annex A controls linked to risks | Scope statement, SoA | 4 h |
| 6 · Policies and exceptions | Rewrite a weak password policy into policy, standard and procedure; process five exception requests; draft an AI acceptable-use policy | Policy set, exception decisions with expiry, AI policy | 5 h |
| 7 · Control testing and evidence automation | Test three access controls with samples from a provided user and access export; write a script that proves MFA is enforced for all admins in your test tenant | Workpapers with sample selection, script and its output | 6 h |
| 8 · Vendor tiering and contract schedule | Tier 20 vendors; choose assessment depth; draft a security schedule with breach notice, audit rights and exit terms | Tiering sheet, schedule | 4 h |
| 9 · Reporting decision tree and matrix | CERT-In, DPDP and sector-regulator decision tree; matrix for an Indian SaaS company with EU and US customers | Decision tree, matrix, two breach notices | 5 h |
| 10 · BIA and DR test plan | BIA for three hospital processes; DR test plan with success criteria | BIA table, test plan | 3 h |

## Projects

### P1 · Indian incident reporting kit (L1, ~6 hours)

**Real-world inspiration.** CERT-In's Directions of 28 April 2022 require listed incidents to be reported within 6 hours; the DPDP Rules 2025 require notice to affected persons without delay and a detailed report to the Data Protection Board within 72 hours; RBI's July 2026 directions require commercial banks to report on DAKSH within 6 hours. Companies often lose hours working out who must be told what.

**What to build.** A kit an on-call team can use at 2 a.m.: (1) a decision tree (Markdown plus a small script or spreadsheet) that asks yes/no questions and outputs every report due, its recipient, its deadline from a given detection time, and the content required; (2) templates for the CERT-In report, the DPDP Board report and the notice to individuals; (3) a one-page "first hour" checklist.

**Acceptance criteria**
- On 10 test scenarios written by a classmate (including a bank, a hospital, a SaaS company with EU users, and a non-personal-data outage), the kit's outputs match the reviewer's answers on at least 9, and each mismatch is explained.
- Every rule in the tree cites the primary text (section, rule or paragraph) and the date checked.
- Deadlines are computed correctly across midnight and in IST.
- The notice to individuals is written in plain language at about a Class 8 reading level and avoids admitting facts not yet established.

**Stretch goals.** Add GDPR, NIS2 and SEC Item 1.05 branches; translate the notice template into one Indian language besides English.

**What it proves to an employer.** You can turn law into an operational tool that works under pressure, which is what incident managers and compliance teams need.

### P2 · ISMS starter kit with automated evidence (L2, ~15 hours)

**Real-world inspiration.** Startups that sell to banks and large enterprises are routinely asked for ISO/IEC 27001 certification or a SOC 2 report, and RBI's 2026 directions push banks to demand audit rights and baseline controls from technology suppliers. GRC platforms now automate much of the evidence; this project builds the core yourself so you understand what those platforms do.

**What to build.** For an illustrative 40-person B2B SaaS company: ISMS scope, risk methodology and register (12 risks), a Statement of Applicability for all 93 Annex A controls (applicable/excluded with reasons), 8 core policies, an internal audit plan, and **five automated evidence checks** against your own test environment (for example: MFA enforced for all administrators; storage buckets block public access; audit logging enabled; backups exist and were restored in the last 90 days; offboarded users have no active accounts). Each check runs on a schedule and stores dated results.

**Acceptance criteria**
- Every applicable control in the SoA links to at least one risk and one piece of evidence or a planned action with an owner and date.
- The five checks run with one command, produce machine-readable output with timestamps, and fail correctly when you deliberately break each control.
- A classmate acting as an auditor samples five controls and records findings; you respond with corrective actions.
- All policies have an owner, a review date and measurable requirements.

**Stretch goals.** Map the same evidence to SOC 2 Trust Services Criteria; load the controls into CISO Assistant and compare its view with yours.

**What it proves to an employer.** You can build compliance that is real and testable, not paperwork, which is what fast-growing companies need from their first GRC hire.

### P3 · Third-party cyber risk programme for a bank's technology suppliers (L3, portfolio-grade, ~30 hours)

**Real-world inspiration.** In July 2024 a ransomware attack on C-Edge Technologies, a supplier to co-operative and regional rural banks, led NPCI to isolate it from retail payments and disrupted about 300 small banks for days. The July 2024 CrowdStrike update and the August 2025 Salesloft Drift token theft showed how one supplier can affect thousands of customers at once. RBI's July 2026 directions for commercial banks require RBI audit rights in contracts, baseline controls for providers such as ATM switch operators, and resilience testing across interconnected vendor systems. The bank below is illustrative.

**What to build.** A complete programme for an illustrative mid-size commercial bank with 120 technology suppliers:
1. a tiering model (data access, criticality, substitutability, concentration) applied to a provided supplier list;
2. an assessment questionnaire of at most 60 questions mapped to RBI's 2026 requirements, ISO/IEC 27001 Annex A and NIST CSF 2.0, with the evidence expected for each answer;
3. a contract security schedule (breach notice within a stated number of hours, right to audit including the regulator, sub-processor control, exit and data return);
4. a continuous monitoring design with triggers for reassessment;
5. a quantified concentration-risk model: Monte Carlo of losses if one of the top three suppliers is unavailable for 1, 3 or 7 days;
6. a supplier-ransomware tabletop including the decision to disconnect a supplier from payment systems;
7. a two-page board report with decisions requested.

**Acceptance criteria**
- Every supplier in the provided list has a tier with a one-line justification; the top tier is under 15% of suppliers or the deviation is explained.
- Every questionnaire item maps to at least one cited requirement, and at least 20 items require system-generated evidence rather than a yes/no answer.
- The concentration model states every input with a source or "(unconfirmed)", reports the 50th and 95th percentile losses, and compares two treatments (dual-sourcing vs contractual and testing controls).
- The tabletop report records who had authority to disconnect the supplier, the time to decision, the communications to customer banks and regulators, and three improvements.
- The board report fits on two pages, uses money and time, and asks for specific decisions.

**Stretch goals.** Run your questionnaire on a real vendor's public trust centre and SOC 2 bridge letter (only public documents) and record how many answers can be evidenced from public material.

**What it proves to an employer.** You can manage the supply-chain risk regulators now focus on, with quantified reasoning and controls that hold up in an audit. This is senior GRC and technology-risk work in banks and fintechs.

## Feeds into

- [OV07 Privacy Engineering](../../../../04_overlaps/OV07_privacy_engineering/README.md): DPDP obligations become privacy-by-design engineering.
- [OV10 FinTech Systems Engineering](../../../../04_overlaps/OV10_fintech_systems_engineering/README.md): RBI and SEBI requirements applied to payment and lending systems.
- [SEC402 Digital Forensics and Incident Response](../../year_4/SEC402_digital_forensics_and_incident_response/README.md): P1's reporting kit is used in incident simulations.
- [SEC404 AI in Security Operations](../../year_4/SEC404_ai_in_security_operations/README.md): AI governance and evaluation of AI tools.
- [IND401 Industry Co-op Studio](../../../../05_shared_years_3_to_5/IND401_industry_co_op_studio/README.md): GRC projects are common co-op placements.
