# SAR301 · Labs and projects

Every artefact lives in one Git repository: diagrams as code, ADRs, requirements in YAML, OSCAL files and review notes. All systems named below are *illustrative scenarios* unless a source is given. Labs 4 and 5 are done without AI assistants. No lab touches a system you do not own.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · CSRB case dissection | Read the CSRB report on the 2023 Exchange Online intrusion and extract each architectural decision that failed | A table: decision, flaw, principle violated, control that would have broken the chain, owner who should have decided | 3 h |
| 2 · Principle hunt | Find one 2024–2026 public incident per Saltzer–Schroeder principle (plus "assume breach" and "blast radius"), from primary sources | Ten rows with a link, the violated principle and a one-line design fix | 3 h |
| 3 · Common-mode failure | Take a provided three-layer design and find what the layers share (identity provider, vendor, operator, code) | Blast-radius maps for one key, one role and one CI token; a redesign that removes one shared dependency | 4 h |
| 4 · Requirements and abuse cases (no AI) | Write security requirements for an illustrative ticket-booking flow | 20 testable requirements with verification method, 10 abuse cases, and a traceability matrix to threats | 4 h |
| 5 · CSF 2.0 profile (no AI) | Map 10 CSF 1.1 subcategories to 2.0 with NIST's reference tool; write a target profile for one product line | Mapping table with tool screenshots or exports; target profile with gaps | 4 h |
| 6 · Controls as code | Write an OSCAL component definition for one service and validate it with NIST's `oscal-cli` or `compliance-trestle` | Validated OSCAL JSON, validator output, and a short note on what OSCAL could not express | 5 h |
| 7 · Assurance case | Argue "tenant data cannot cross tenants" for a multi-tenant SaaS in Goal Structuring Notation | GSN diagram with every leaf tied to evidence (test, config export, review record) | 4 h |
| 8 · SABSA attributes | Build a business attributes profile for an illustrative hospital records system | 12 attributes with measurable definitions, traced to at least two controls each | 4 h |
| 9 · Architecture as code | Model a telemedicine app in Structurizr DSL or Mermaid with four security overlays | C4 levels 1–3, overlays (data classes, identity flows, key hierarchy, network zones) and five ADRs | 4 h |
| 10 · AI mapping audit | Ask two assistants to map a design to CSF 2.0 and SP 800-53 Rev. 5 | An error log: wrong IDs, retired IDs, missing controls, unsupported "compliant" claims, each checked in CPRT | 3 h |

## Projects

### P1 · Security architecture brief for a small clinic app (L1, ~6 hours)

**Real-world inspiration:** small healthcare providers in India now handle digital personal data under the DPDP Act 2023 and its Rules (notified November 2025), which require "reasonable security safeguards" ([PIB](https://www.pib.gov.in/PressReleasePage.aspx?PRID=2190014)). The app is an *illustrative scenario*: appointment booking, prescriptions and payments for a three-doctor clinic.

**What to build:** a five-page architecture brief: C4 context and container diagrams, a data classification table, three trust boundaries with the threats that cross them, 15 testable security requirements, three ADRs and one risk acceptance.

**Acceptance criteria:**
- Every requirement has a threshold or a pass/fail condition and a verification method (test, inspection, analysis or demonstration).
- Every requirement traces to a named threat or a legal source (DPDP section or rule, CERT-In direction).
- At least one ADR records a rejected option and why it was rejected.
- The risk acceptance names an owner, compensating controls, an expiry date and a re-review trigger.
- A classmate, given only your brief, can list the three highest risks you identified within 10 minutes.

**Stretch goals:** an abuse-case table for the payment step; an ASVS 5.0 level choice with justification.

**What it proves to an employer:** you can turn a vague product into a reviewable security design on one sitting's work.

### P2 · Data protection pattern pack for a regulated fintech (L2, ~15 hours)

**Real-world inspiration:** UIDAI's Circular 14 of 2025 and its Aadhaar Data Vault FAQ (November 2025) require entities that store Aadhaar numbers to keep them in a vault in a restricted network zone, refer to them by reference keys that cannot be derived by hashing, and hold signing and e-KYC decryption keys in an HSM ([UIDAI FAQ](https://uidai.gov.in/images/FAQs_Aadhaar_Data_Vault_03112025_v10.pdf)). RBI's directions on authentication for digital payments took effect in April 2026 (summary: [Khaitan & Co](https://khaitanco.com/thought-leadership/RBI-Authentication-Mechanisms-for-Digital-Payments-Transactions-Directions)). The lender is an *illustrative scenario*.

**What to build:** a reusable pattern pack for an illustrative digital lender:
- an Aadhaar Data Vault pattern following the UIDAI documents, with reference-key design, HSM use and access paths;
- a tokenization pattern for PAN and bank account numbers;
- a key hierarchy (root, key-encryption keys, data keys) with rotation and ownership;
- data zoning (restricted, confidential, internal) with allowed flows;
- OSCAL component definitions for the vault and tokenizer;
- a traceability matrix from requirement to control to test.

**Acceptance criteria:**
- Each pattern has: intent, context, forces, structure diagram, consequences, known misuses and a test that proves it works.
- The vault pattern cites the specific UIDAI requirement for each design choice; anything you could not confirm is marked "(unconfirmed)".
- Both OSCAL files validate with zero errors, and every referenced SP 800-53 control exists in Release 5.2.0.
- A reviewer can trace 100% of "high" requirements to a control and a test.
- A peer review by another student finds no unreferenced data flow between zones.

**Stretch goals:** a SABSA attributes profile for the lender that drives the pattern choices; a cost estimate for HSM options (on-premises, MeitY-recognised cloud, HSM as a service).

**What it proves to an employer:** you can design data protection that meets Indian regulation in a form other teams can reuse.

### P3 · Architecture review pack for a UPI-style payments app (L3, portfolio-grade, ~30 hours)

**Real-world inspiration:** architects at payment companies run reviews like this before launch. The app is an *illustrative scenario*: a consumer payments app on UPI rails with a merchant QR flow, a wallet, a partner API and a fraud engine. You receive a 12-page "as-designed" document with ten planted flaws (one per principle family).

**What to build:**
- a SABSA attributes profile and a CSF 2.0 target profile for the product;
- C4 diagrams with four overlays, in diagrams-as-code;
- a threat-informed requirement set using ASVS 5.0 (level 2, level 3 for payment paths) and abuse cases;
- a tailored SP 800-53 moderate baseline in OSCAL, with justified removals;
- a written design review of the as-designed document: findings ranked by risk with fixes;
- ten ADRs for the corrected design;
- an ARB decision memo, two risk acceptances and a one-page executive summary;
- an AI comparison: the findings of two AI design reviews against yours.

**Acceptance criteria:**
- You find at least 8 of the 10 planted flaws, each with the principle named and a fix that a second reviewer accepts.
- Every control and CSF identifier validates against NIST CPRT or the OSCAL catalogue; zero invented IDs.
- 100% of high and critical threats trace to requirements, controls and tests.
- The executive summary fits one page, uses no jargon a non-specialist must look up, and states the decision required.
- The AI comparison table lists at least five AI findings you rejected, with reasons, and every planted flaw the AI missed.
- You defend the pack in a 20-minute oral with questions; the panel can change one assumption and you re-rank risks live.

**Stretch goals:** an assurance case in GSN for "a payment cannot be initiated without the user's second factor"; an ARB metrics dashboard design.

**What it proves to an employer:** this is the work product of a security architect: a review that finds real flaws, decisions that are written down, and a summary an executive can act on. It is ready to discuss in the design-review round of an architect interview.

## Feeds into

- [SAR302 Threat Modeling](../SAR302_threat_modeling/README.md): the threat models behind your requirements become full STRIDE, PASTA and LINDDUN models.
- [SAR401 Cloud Security Architecture](../../year_4/SAR401_cloud_security_architecture/README.md): invariants and guardrails from Chapter 3 become landing-zone policies.
- [SAR404 Resilience and Security Strategy](../../year_4/SAR404_resilience_business_continuity_and_security/README.md): risk acceptances and executive summaries grow into strategy and board reporting.
- [OV01 Cloud Security](../../../../04_overlaps/OV01_cloud_security/README.md) and the [flagship industry project](../../../../06_career_and_market_readiness/05_industry_projects/SAR_security_architecture.md): P3's review pack is the template for the flagship's architecture dossier.
