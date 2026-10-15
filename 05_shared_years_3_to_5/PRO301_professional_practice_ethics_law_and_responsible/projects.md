# PRO301 · Labs and projects

Every lab and project produces an artefact a real company would use: a decision record, a data map, a runbook, an SBOM, an audit. Every legal claim in a submission must cite the section, rule or article and the source you read it in. A single invented provision fails the submission, whoever or whatever produced it. Security testing happens only on systems you built or legal practice environments.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Decision records | Resolve three dilemmas (dark-pattern request, skipping a test to hit a date, logging without consent) with the Chapter 1 procedure | Three one-page decision records citing ACM clauses | 2 h |
| 2 · Failure causal chains | Rebuild the causal chains of Therac-25 and Knight Capital from the primary reports | Two diagrams separating technical, organisational and regulatory causes, with page references | 3 h |
| 3 · IT Rules and CERT-In as requirements | Convert the CERT-In Directions and the 2026 IT Rules amendment into testable engineering requirements | A requirements table (requirement, source paragraph, design, test) with at least 12 rows | 3 h |
| 4 · Data map and notice | Map every personal-data field in a provided food-delivery app spec to purpose, legal ground, processor, retention and DPDP provision | Data map (spreadsheet) plus an itemised notice in English and one other Eighth Schedule language | 4 h |
| 5 · Breach tabletop | Run a timed scenario (leaked S3 bucket discovered at 23:10) in a team of four | Timeline, CERT-In 6-hour report, DPDP notices to affected people and the Board with the 72-hour detailed report, GDPR Art. 33 note for EU users | 3 h |
| 6 · AI Act classification | Classify eight described systems and build an obligations calendar for one | Classification table with article references; calendar using the post-Omnibus dates | 3 h |
| 7 · Contract red-line | Red-line a sample offer letter with IP assignment, non-compete, training bond and moonlighting clauses | Marked-up contract, notes on enforceability in India, five questions for HR | 2 h |
| 8 · Licence audit and SBOM | Generate an SBOM with Syft, scan with ScanCode, resolve unknowns | SPDX JSON SBOM, list of copyleft components with triggered duties, fixed notices | 4 h |
| 9 · Fairness audit | Train a classifier on folktables ACSIncome; compute demographic parity, equal opportunity, equalised odds and calibration by group | Notebook with metrics and bootstrap confidence intervals; one paragraph on which metric fits the use case and why | 4 h |
| 10 · LLM red-team (own system) | Attack your own small RAG app against five OWASP LLM Top 10 risks, then fix | Attack log, fixes, before/after success rates on a fixed test set | 4 h |
| 11 · Energy measurement | Measure energy per 1,000 requests for three configurations (full model, quantised, cached) with CodeCarbon | Results over at least three runs with variance; note on what the tool cannot see | 3 h |
| 12 · Accessibility audit | Audit a login and e-KYC-style flow against WCAG 2.2 AA with axe-core, keyboard only and NVDA or TalkBack | Issue list with criterion numbers, 10 fixes, a screen-reader walkthrough recording | 4 h |

## Projects

### P1 · Licence compliance kit for a real application (L1, ~6 hours)

**Real-world inspiration.** Open-source programme offices run licence compliance as a continuous process; the OpenChain specification became the international standard ISO/IEC 5230 for exactly this. Relicensing events (HashiCorp in 2023, Redis in 2024) showed that a dependency's licence can change under you.

**What to build.** Pick an open-source web application with at least 50 transitive dependencies (for example a Django or Next.js project). Generate an SBOM with Syft, scan the source with ScanCode, write the third-party notices, and add a CI check that fails when a dependency with a denied licence is added.

**Acceptance criteria**
- The SBOM is valid SPDX JSON (passes the SPDX tools validator).
- Every package has a concluded licence, or `NOASSERTION` with a written reason; zero unexplained unknowns.
- A compliance table lists the duties each copyleft component triggers under two models: SaaS and an on-premises binary.
- The CI check fails when an AGPL-3.0 test package is added and passes when it is removed (shown in two CI runs).
- The notices file includes every Apache-2.0 NOTICE text that must be reproduced.

**Stretch goals.** Track licence changes across versions by diffing two SBOMs; adopt the REUSE specification and pass `reuse lint`.

**What it proves to an employer.** You can ship without creating legal debt, and you automate compliance instead of relying on memory.

### P2 · DPDP-ready consent and rights service (L2, ~15 hours)

**Real-world inspiration.** The DPDP Act creates registered consent managers from November 2026, and India's Account Aggregator system already runs on machine-readable consent artefacts. Most products will need consent records that can be proved years later.

**What to build.** A small service (any stack) with: an append-only consent ledger (principal, purpose, notice version, timestamp, channel); withdrawal; endpoints for access, correction and erasure; erasure events propagated to two mock processors; a retention job; an audit log of every read of personal fields; and a breach runbook.

**Acceptance criteria**
- Consent records cannot be edited in place; a test proves that tampering is detected (hash chain or database constraint).
- Withdrawal takes no more steps than giving consent (UI test counts the steps).
- An erasure request reaches both mock processors and is confirmed within a stated time limit, checked by an automated test.
- Notices exist in English and one other Eighth Schedule language, each with a version ID referenced from the ledger.
- A one-page map links every feature to the DPDP section or rule it serves and the date that duty applies.
- In a timed drill, the team produces the CERT-In 6-hour report and the DPDP Rule 7 notices from the runbook.

**Stretch goals.** Verifiable parental consent for users under 18 with a documented threat model; export of consent artefacts in a format a consent manager could consume.

**What it proves to an employer.** You can turn a new law into working, tested software before the deadline, not after the first complaint.

### P3 · Responsible AI audit dossier (L3, portfolio-grade, ~30 hours)

**Real-world inspiration.** Model cards and datasheets became standard practice at major labs; the EU AI Act requires technical documentation and risk management for high-risk systems; buyers increasingly send AI questionnaires in procurement.

**What to build.** A full audit of an ML or LLM system you built in an earlier course (or a public model in a clearly stated use case): AI Act classification and dated obligations; DPDP and GDPR mapping; fairness audit with mitigation; model card and datasheet; red-team of your own system (OWASP LLM Top 10) or robustness tests for a non-LLM model; energy per 1,000 inferences; WCAG 2.2 AA audit of the interface; a risk register; a two-page summary for a non-technical decision-maker.

**Acceptance criteria**
- At least three fairness metrics for at least two groups, each with a bootstrap 95% confidence interval; one mitigation with before/after accuracy and fairness.
- Energy measured over at least three runs with the variance reported, plus one change that reduces it by at least 20%.
- Zero critical axe-core violations, a full keyboard-only pass and a screen-reader walkthrough recording.
- Every legal statement cites its article, section or rule; a peer from another major checks them and finds zero invented provisions.
- A reviewer can reproduce every number from the repository in under one hour by following the README.
- A 15-minute oral defence where you answer "should this system be deployed?" with conditions.

**Stretch goals.** Write the system's AI Act Annex IV-style technical documentation; add C2PA provenance to generated outputs.

**What it proves to an employer.** You can make an AI system defensible to a regulator, a buyer and a user, with evidence rather than slogans.

## Feeds into

- [OV07A Privacy by Design and Privacy-Enhancing Technologies](../../04_overlaps/OV07_privacy_engineering/OV07A_privacy_by_design_and_privacy_enhancing/README.md) and [OV07B Data Protection Law for Engineers in Practice](../../04_overlaps/OV07_privacy_engineering/OV07B_data_protection_law_for_engineers_in_practice/README.md): P2 is the starting point.
- [IND401 Industry Co-op Studio](../IND401_industry_co_op_studio/README.md): the client's NDA, data-handling rules and licence checks use Labs 7 and 8.
- [THS501 Thesis or Capstone I](../THS501_thesis_or_capstone_i/README.md): the ethics, data and licence review chapter reuses P1 and P3.
- [LCH502 Career Launch and Founder Studio](../LCH502_career_launch_and_founder_studio/README.md): the founder track builds the MVP compliant from day one using P2.
