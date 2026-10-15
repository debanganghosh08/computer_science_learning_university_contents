# OV07B · Data Protection Law for Engineers in Practice

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 4 · 8 | 4 (≈ 120 hours) | L3 → L4 | [SEC305](../../../03_majors/cybersecurity_defense/year_3/SEC305_governance_risk_and_compliance/README.md), [PRO301](../../../05_shared_years_3_to_5/PRO301_professional_practice_ethics_law_and_responsible/README.md), [DEN301](../../../03_majors/data_engineering/year_3/DEN301_data_modeling_and_warehousing/README.md); co-requisite [DEN404](../../../03_majors/data_engineering/year_4/DEN404_data_governance_lineage_and_privacy_engineering/README.md) (same semester); [OV07A](../OV07A_privacy_by_design_and_privacy_enhancing/README.md) recommended | [THS501](../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md), [LCH502](../../../05_shared_years_3_to_5/LCH502_career_launch_and_founder_studio/README.md) |

> This course teaches engineers how data protection law shapes systems. It is not legal advice. Summaries of statutes and cases here are for engineering orientation; the notified texts and qualified counsel govern real decisions.

## Why this course matters now

India's Digital Personal Data Protection (DPDP) Act, 2023 and the DPDP Rules, 2025 (notified 13 November 2025) give most data-fiduciary duties a start date of 13 May 2027, with consent managers from 13 November 2026, and penalties of up to ₹250 crore for failing to take reasonable security safeguards. GDPR enforcement shows what happens when systems and law diverge: Ireland's Data Protection Commission fined Meta €1.2 billion in 2023 over transfers to the US, and the Dutch authority fined Uber €290 million in 2024 for the same class of failure. AI assistants now draft privacy notices, DPIAs, records of processing and responses to access requests; they also cite repealed provisions, invent article numbers, merge GDPR concepts into DPDP (which has no "legitimate interests" basis), and describe what a system should do rather than what it does. The engineer who can read the Act, read the code, and show where they disagree is the one regulators, lawyers and auditors need. [DEN404](../../../03_majors/data_engineering/year_4/DEN404_data_governance_lineage_and_privacy_engineering/README.md) builds the platform controls; this course teaches the legal reasoning behind them and the operations around them: rights requests, consent interfaces, transfers, breaches, vendors, AI and enforcement.

## Learning outcomes

By the end you can:

1. **Read** a statute, its rules and a regulator's guidance as a layered specification, and **extract** testable requirements with citations to the exact section, rule or article.
2. **Map** an organisation's processing to DPDP roles and grounds (consent or a listed legitimate use) and to GDPR lawful bases, and **explain** where the two regimes differ.
3. **Operate** data-principal and data-subject rights at scale: identity verification, discovery across systems, response, and evidence, within the legal timelines.
4. **Design** consent and cookie interfaces that meet DPDP, GDPR/ePrivacy and India's 2023 dark-pattern guidelines, and **test** them with users.
5. **Write** a DPIA that an independent reviewer accepts, with risks traced to controls and residual risk owned.
6. **Plan** cross-border data flows under GDPR Chapter V, DPDP section 16 and sector localisation rules, and **architect** systems that comply.
7. **Run** a breach response that meets the DPDP Rules, GDPR and CERT-In clocks from one fact base.
8. **Assess** an AI system's data-protection risks (training data, prompts and logs, outputs, automated decisions) and **document** the decisions.

## Chapters and lessons

### Chapter 1 · Reading law like a specification (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Layers of law | Constitution (*Justice K.S. Puttaswamy v Union of India*, 2017: privacy is a fundamental right), statute, rules, regulator guidance, case law, contracts | Place 10 documents in the hierarchy and say which wins on conflict |
| 1.2 Definitions as types | "Personal data", "processing", "data fiduciary", "data principal"; scope clauses as preconditions | Encode DPDP section 2 definitions as a typed data model |
| 1.3 Normative words | Shall, may, reasonable, without delay; obligations with and without deadlines | Turn five provisions into requirements with owners and tests |
| 1.4 Working with counsel | What to ask a lawyer, what to bring (data maps, flows, code facts), privilege, writing decisions down | Draft a question memo to counsel about one ambiguous provision |

**Check your understanding:** Why does a guideline from a regulator bind your design even if it is not a statute? What makes "reasonable security safeguards" testable at all? When should an engineer refuse to interpret a provision alone?

### Chapter 2 · DPDP I: scope, grounds, notice and consent (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Scope | Digital personal data; processing outside India when offering goods or services to people in India; personal and domestic use excluded; data made public by the person (section 3) | Decide scope for six illustrative products, including a foreign SaaS and a scraper |
| 2.2 Grounds | Consent (section 6) or a listed legitimate use (section 7); no general "legitimate interests" ground as in GDPR | Assign a ground to every processing activity of a lending app |
| 2.3 Notice | Section 5 and Rule 3: itemised data and purposes, how to withdraw and complain, in clear language; English or Eighth Schedule languages | Rewrite a real-style notice into a compliant, itemised one (illustrative) |
| 2.4 Valid consent | Free, specific, informed, unconditional, unambiguous, clear affirmative action; withdrawal as easy as giving | Build consent and withdrawal flows with event logging |
| 2.5 Consent managers | Registered consent managers (Rule 4, from 13 Nov 2026; Indian company, net worth at least ₹2 crore); interoperability; the RBI-regulated Account Aggregator model and NITI Aayog's DEPA (2020) as precedents | Sequence diagram of consent via a consent manager and via an Account Aggregator |

**Check your understanding:** A GDPR-trained engineer proposes "legitimate interests" for fraud analytics in India. What do you check in section 7 instead? Why can bundled consent fail the "specific" test? What changes for engineers when consent is managed by a third party?

### Chapter 3 · DPDP II: duties, rights, the Board and penalties (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 General duties | Section 8: accuracy, safeguards (Rule 6), breach intimation (Rule 7), erasure when purpose ends (Rule 8), contact person, grievance redressal; processors under contract | Turn section 8 into a control matrix with evidence queries (pairs with DEN404) |
| 3.2 Significant data fiduciaries | Section 10 and Rule 13: DPO in India, independent auditor, periodic DPIA and audit, algorithmic due diligence (Rule 13(3)), traffic-data restriction (Rule 13(4)) | Write the algorithmic due-diligence record for a credit model |
| 3.3 Rights | Access (s.11), correction and erasure (s.12), grievance (s.13), nomination (s.14); Rule 14(3)'s 90-day outer limit for responses | Design rights intake with SLAs well inside the limit |
| 3.4 The Board and penalties | Data Protection Board as a digital-first body; inquiries; voluntary undertakings; Schedule penalties (up to ₹250 crore for safeguards failures, ₹200 crore for breach-notice and children's duties) | Rank your control gaps by penalty exposure and likelihood |
| 3.5 Timelines and change | Phased commencement (13 Nov 2025, 13 Nov 2026, 13 May 2027); the 2026 consultation on shortening the window (status unconfirmed); the RTI Act amendment by section 44(3) | Build a compliance timeline with dated milestones and re-check triggers |

**Check your understanding:** Why does the penalty schedule make security safeguards the top engineering priority? What evidence shows a regulator you "erased" data? How would you know if a commencement date changed?

### Chapter 4 · GDPR in operation (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Lawful bases | Article 6's six bases; legitimate-interests assessments; Article 9 special categories | Write a legitimate-interests assessment for product analytics |
| 4.2 Accountability | Records of processing (Article 30), DPO (Article 37), by design and by default (Article 25) | Generate an Article 30 record from your data catalog |
| 4.3 Automated decisions | Article 22; the CJEU's *SCHUFA* judgment (C-634/21, Dec 2023): a credit score can itself be an automated decision; the Dutch authority's €824.99 million fine on Uber for fully automated driver deactivations and inadequate information (published 8 Oct 2026, under appeal) | Decide whether three model-driven flows fall under Article 22 |
| 4.4 Fines and enforcement | Article 83 (up to €20 million or 4% of global turnover); one-stop shop; GDPRhub and enforcement trackers | Summarise three decisions: facts, violated articles, the engineering failure |

**Check your understanding:** Why does the choice of lawful basis change which rights apply? What made the *SCHUFA* score a "decision"? Which Article 30 fields can only engineers fill correctly?

### Chapter 5 · Rights operations at scale (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Intake and identity | Verifying requesters without collecting more data; fraudulent requests as an attack on other people's data | Threat-model a DSAR portal; add step-up verification |
| 5.2 Discovery | Finding a person across OLTP, warehouse, logs, tickets, backups and vector stores using lineage and identifiers | Build a discovery job over five stores using DEN404 lineage |
| 5.3 Responses | Access exports (machine-readable, explained), correction propagation, portability (GDPR Article 20), timelines (GDPR one month, extendable; DPDP Rule 14) | Produce a complete access export for a test user in under 10 minutes |
| 5.4 Erasure exceptions | Legal holds, other laws requiring retention (tax, KYC, Rule 8(3) logs), backups and crypto-shredding | Write the decision table for "erase, restrict or retain" |
| 5.5 Metrics and evidence | Volume, time to complete, error rate, complaints; audit trails | Dashboard for a month of simulated requests |

**Check your understanding:** Why is an access request a security risk? What must an erasure confirmation honestly say about backups? When can you lawfully refuse or delay?

### Chapter 6 · Consent interfaces, cookies and dark patterns (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 ePrivacy and cookies | Storage-and-access consent (ePrivacy Directive Article 5(3)); *Planet49* (C-673/17, 2019): pre-ticked boxes are not consent | Audit a test site's tags and cookies before any click |
| 6.2 Consent frameworks | IAB Europe's TCF; the CJEU (C-604/22, Mar 2024) held its consent string can be personal data; Global Privacy Control signals | Implement GPC handling and a consent string store |
| 6.3 Dark patterns in law | India's Guidelines for Prevention and Regulation of Dark Patterns, 2023 (13 specified patterns, notified 30 Nov 2023); EDPB Guidelines 03/2022 on deceptive design | Find and fix 5 dark patterns in a provided checkout and consent flow |
| 6.4 Testing consent UX | Usability tests with 5–8 participants, comprehension questions, refusal rates by design variant | Run a small study on two banner designs; report comprehension |

**Check your understanding:** Why is "reject all" placement a legal question, not only a design choice? What does a consent string reveal about a user? How do you prove a consent flow is not a dark pattern?

### Chapter 7 · Children's data and age assurance (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 DPDP section 9 | Children are under 18; verifiable parental consent; no processing likely to cause detrimental effect; no tracking, behavioural monitoring or targeted advertising at children | Find every tracking path in a learning app that touches minors |
| 7.2 Verifiable consent methods | Rule 10: using reliable age and identity details already held or provided, or a virtual token from an authorised entity; exemptions in the Fourth Schedule | Design two Rule 10 flows and compare data collected |
| 7.3 Other regimes | GDPR Article 8 (13–16 by member state); the UK Age Appropriate Design Code (2021) | Map one app's features against the UK Code's 15 standards |
| 7.4 Privacy-preserving age assurance | Estimation vs verification; selective-disclosure credentials (OV07A Chapter 9); error rates and exclusion | Specify an age check that reveals only "18 or over" |

**Check your understanding:** Why can age verification create a bigger privacy risk than the one it solves? What does "detrimental effect" require you to measure? How do you handle a user who turns 18?

### Chapter 8 · DPIAs and privacy reviews in practice (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 When a DPIA is required | GDPR Article 35 triggers and regulator lists; DPDP periodic DPIA for significant data fiduciaries | Screen 8 projects for DPIA need |
| 8.2 Writing it | Description, necessity and proportionality, risks to people, measures, residual risk, sign-off; ICO template | Full DPIA for an illustrative telehealth feature |
| 8.3 From threat model to DPIA | LINDDUN outputs (OV07A) as risk input; linking each risk to a control and a test | Trace 10 risks to controls and evidence |
| 8.4 Keeping it alive | Change triggers, versioning, review cadence, linking to release gates | Add a DPIA check to a CI pipeline |

**Check your understanding:** Why is "risk to the organisation" the wrong risk in a DPIA? What makes a residual risk acceptable, and who decides? What change to a system should reopen its DPIA?

### Chapter 9 · Cross-border transfers and localisation (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 GDPR Chapter V | Adequacy, Standard Contractual Clauses (2021), transfer impact assessments after *Schrems II* (C-311/18, 2020) | Write a transfer impact assessment for a US analytics vendor |
| 9.2 The EU–US Data Privacy Framework | Adequacy decision (July 2023); the General Court upheld it in *Latombe v Commission* (T-553/23, 3 Sept 2025) | List what your design does if the framework falls |
| 9.3 India | DPDP section 16 (transfers allowed unless restricted by notification) and Rule 15; RBI's 2018 payment-data localisation; CERT-In's 2022 log rules | Classify 12 data flows of a fintech by the rule that governs them |
| 9.4 Architecture | Regional data cells, key residency, processing abroad with data returned, metadata leakage through logs and support tools | Redesign a support tool so tickets stay in-region |

**Check your understanding:** Why are transfer rules about access, not only storage location? What breaks if a vendor's support team abroad can read production logs? Which India data flows are governed by sector rules rather than DPDP?

### Chapter 10 · Breach response (week 10)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 The clocks | DPDP Rule 7 (affected people without delay; detailed report to the Board within 72 hours); GDPR Articles 33–34 (72 hours to the authority); CERT-In (6 hours for listed incidents); sector regulators | Build one reporting matrix for a payments company |
| 10.2 Facts under uncertainty | Scoping, logs as evidence, what you can say at hour 6 vs hour 72 | Write the hour-6 and hour-72 versions of the same notice |
| 10.3 Notifying people | Content, channels, languages, avoiding panic and avoiding understatement | Draft affected-person notices in English and one Indian language |
| 10.4 Tabletop | Roles, decision log, legal review, regulator questions | Full tabletop on a simulated leaked analytics export |

**Check your understanding:** Why should the breach-notice system share one fact base across regulators? What do you say when you do not yet know whether data was exfiltrated? Which logs would you wish you had kept?

### Chapter 11 · Processors, vendors and AI (weeks 11–12)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Processor contracts | GDPR Article 28 clauses; DPDP's requirement that fiduciaries engage processors under a valid contract; sub-processors and audits | Review a sample data processing agreement against a checklist |
| 11.2 AI training data | EDPB Opinion 28/2024 on AI models (anonymity of models is not presumed; legitimate-interest tests); Italy's Garante fined OpenAI €15 million (Dec 2024); DPDP's publicly-available-data exclusion and its limits | Write a lawful-basis and data-source register for a fine-tuning dataset |
| 11.3 Prompts, logs and outputs | Personal data in prompts and traces, retention, vendor training opt-outs, regional processing | Set retention and redaction rules for an LLM feature's traces |
| 11.4 Models and rights | Access and erasure when personal data may be in model weights or retrieval indexes; output accuracy (GDPR Article 5(1)(d)) | Decide and document how your system answers an erasure request for a RAG assistant |
| 11.5 Automated decisions in India | No Article 22 equivalent in DPDP; RBI and sector expectations; explanations as good practice | Draft a user-facing explanation for an automated loan decline |

**Check your understanding:** When is a model itself personal data? What should a vendor contract say about training on your data? How does a RAG system make erasure easier than fine-tuning does?

### Chapter 12 · Enforcement, evidence and the privacy programme (weeks 13–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 12.1 Case studies | Meta €1.2 bn (transfers, 2023); Uber €290 m (transfers, 2024); TikTok €530 m (transfers to China, 2025); OpenAI €15 m in Italy (training data and transparency, 2024); Uber €824.99 m (automated decisions, 2026, under appeal) | For each, name the system design that would have prevented it |
| 12.2 What regulators ask for | Evidence of controls operating over time; how to answer a notice; preserving records | Build an evidence pack from logs for one control |
| 12.3 Running the programme | Privacy roles, RACI with legal and security, metrics, budgets | One-page programme plan for a 300-person company |
| 12.4 Capstone review | Present P3 to a panel acting as Board, counsel and auditor | Defend your decisions under questioning |

**Check your understanding:** What do the three transfer fines have in common in engineering terms? Why are evidence systems cheaper than evidence projects? Which decision in your P3 would you defend least confidently, and why?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Requirements extraction | Requirement register for 20 provisions |
| 2 | 2 | Lab 2 · Grounds and notices | Notice and grounds map |
| 3 | 3 | Lab 3 · Section 8 control matrix | **P1 due** |
| 4 | 4 | Lab 4 · GDPR records and LIA | Article 30 record |
| 5 | 5 | Lab 5 · Rights operations | Access export demo |
| 6 | 6 | Lab 6 · Consent and dark-pattern audit | Fixed flow |
| 7 | 7 | Lab 7 · Age assurance design | Mid-term (open statute, AI off) |
| 8 | 8 | Lab 8 · DPIA | DPIA draft |
| 9 | 9 | Lab 9 · Transfer mapping | **P2 due** |
| 10 | 10 | Breach tabletop | Notices and reporting matrix |
| 11 | 11 | Lab 10 · AI data register | — |
| 12 | 11 | Lab 10 (cont.) | AI DPIA addendum |
| 13 | 12 | Evidence pack | — |
| 14 | 12 | Panel defence | **P3 due** |
| 15 | Review | Oral exam on an unseen scenario | Final exam (open statute, AI off) |

## Working with AI in this course

- **Use AI for:** first drafts of notices, records of processing, DPIA sections and request responses; summarising long guidance documents (then reading the cited passages yourself); translating notices into Indian languages for a native speaker to check; generating test scenarios for rights workflows. Claude, ChatGPT, Gemini and Microsoft Copilot are all used in compliance teams for this.
- **Do without AI (drills):** requirement extraction from primary text in Lab 1; the mid-term and final (open statute, AI off); the breach tabletop decisions; every citation in your projects. You must be able to find the provision yourself.
- **Verify AI output by:** (1) opening every cited section, rule, article or case and checking that it exists and says what is claimed; (2) checking commencement: is the provision in force on the date that matters; (3) checking regime confusion, especially GDPR terms in DPDP analysis; (4) comparing claims about "what the system does" with logs, code or lineage; (5) asking counsel when the answer depends on interpretation.
- **Where AI still fails here (collect your own evidence):** keep a log of AI legal errors you catch during the course: invented or misnumbered provisions, out-of-date dates, GDPR concepts in DPDP answers, overconfident conclusions where regulators have not ruled. Your log is part of P3.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (10) | 20% |
| Projects P1–P3 | 40% |
| Breach tabletop performance | 5% |
| Mid-term (open statute, AI off) | 10% |
| Final oral exam on an unseen scenario (open statute, AI off) | 25% |

**Mastery gate.** You pass when you can, with the statute and rules open but AI off: (1) take an unseen product description and produce, in 90 minutes, a correct map of DPDP grounds, duties and rights with exact citations, flagging the two highest-risk gaps; (2) run the first six hours of a breach scenario and produce the correct notices and reporting matrix; (3) defend a DPIA you wrote against a reviewer's questions without overstating what the system does.

## Industry reality

Where this work happens: privacy and data-protection teams at product companies, banks and payment firms (which also answer to RBI localisation and CERT-In rules), health and edtech companies (children's data), and in GDPR programmes at Indian firms serving European clients. Enforcement in Europe repeatedly targets engineering decisions: international transfers (Meta 2023, Uber 2024, TikTok 2025), automated decisions (Uber, 2026, under appeal) and AI training data (OpenAI in Italy, 2024). In India, the Data Protection Board's practice is still forming in 2026; engineers who design for evidence now will have it when the first inquiries arrive (**analysis**).

**Interview questions from this course**

1. *Our app collects location for delivery. Marketing wants to use it for ads. What do you need?* Strong answer: purpose limitation; under DPDP a new specific consent with itemised notice (no GDPR-style legitimate interests); purpose tags so pipelines enforce it; withdrawal path; children excluded from targeting.
2. *Design an access-request system for a company with 40 data stores.* Strong answer: verified intake, lineage-driven discovery, per-store connectors, export format, exceptions, SLA under Rule 14 and GDPR timelines, audit trail, and abuse prevention.
3. *We had a breach at 2 a.m. Walk me through the first 72 hours.* Strong answer: contain and preserve evidence; CERT-In 6-hour report for listed incidents; DPDP intimation to affected people without delay and detailed Board report within 72 hours; GDPR authority within 72 hours if EU data; one fact base; legal review; honest updates.
4. *Can we fine-tune a model on support tickets?* Strong answer: identifies ground and notice coverage, minimisation and redaction, vendor terms, retention, rights handling for data in weights, DPIA, and alternatives such as retrieval with access control.
5. *How do you know our consent banner is lawful?* Strong answer: tests before-consent behaviour, symmetry of accept and reject, granular purposes, withdrawal, records; checks against India's 2023 dark-pattern guidelines and EDPB guidance; runs a comprehension test.

## Resources (free first)

- **Primary law:** DPDP Act, 2023 (MeitY PDF) — https://www.meity.gov.in/static/uploads/2024/06/2bf1f0e9f04e6fb4f8fef35e82c42aa5.pdf ; MeitY data protection framework page (Act and Rules) — https://www.meity.gov.in/data-protection-framework ; PRS Legislative Research bill page — https://prsindia.org/billtrack/digital-personal-data-protection-bill-2023 ; GDPR text — https://gdpr-info.eu/
- **Guidance:** EDPB guidelines — https://www.edpb.europa.eu/our-work-tools/general-guidance/guidelines-recommendations-best-practices_en ; ICO DPIA guidance — https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/accountability-and-governance/data-protection-impact-assessments-dpias/ ; ICO Children's code — https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/childrens-information/childrens-code-guidance-and-resources/
- **Case law and enforcement:** GDPRhub (noyb) — https://gdprhub.eu/ ; CMS GDPR Enforcement Tracker — https://www.enforcementtracker.com/
- **Paid, optional:** IAPP certifications (CIPP/E, CIPP/A, CIPT) are recognised in privacy hiring; useful later, not required here.

## Sources

All checked October 2026.

- DPDP Act, 2023 (Act 22 of 2023), MeitY copy — https://www.meity.gov.in/static/uploads/2024/06/2bf1f0e9f04e6fb4f8fef35e82c42aa5.pdf
- DPDP Rules, 2025 (G.S.R. 846(E), 13 Nov 2025), commencement, Rule 8(3), Rule 13(3)–(4), Rule 14(3) 90 days: S.S. Rana & Co. (Nov 2025) — https://ssrana.in/articles/meity-notifies-final-digital-personal-data-protection-rules-2025/ ; consent manager net worth (₹2 crore): see the [DEN404](../../../03_majors/data_engineering/year_4/DEN404_data_governance_lineage_and_privacy_engineering/README.md) sources and the Rules' First Schedule
- MeitY consultation on a shorter timeline (Feb 2026) — https://ssrana.in/articles/meity-plans-to-cut-short-dpdp-compliance-timeline-and-notify-cross-border-restrictions-for-sdfs/
- EDPB, Irish DPC decision on Meta (€1.2 bn, 22 May 2023) — https://www.edpb.europa.eu/news/news/2023/12-billion-euro-fine-facebook-result-edpb-binding-decision_en ; EDPB, Dutch SA fine on Uber for transfers (€290 m, 2024) — https://www.edpb.europa.eu/news/dutch-sa-imposes-a-fine-of-290-million-euro-on-uber-because-of-transfers-of-drivers-data-to_en ; Irish DPC, TikTok (€530 m, 2 May 2025) — https://www.dataprotection.ie/en/news-media/latest-news/irish-data-protection-commission-fines-tiktok-eu530-million-and-orders-corrective-measures-following ; EDPB, Dutch DPA fine on Uber for automated decision-making (€824,990,000, 8 Oct 2026, under appeal) — https://www.edpb.europa.eu/news/dutch-dpa-fines-uber-eur-824-990-000-for-unlawful-automated-decision-making-and-insufficient_en
- Garante, OpenAI (€15 m, Dec 2024) — https://www.garanteprivacy.it/home/docweb/-/docweb-display/docweb/10085432 ; EDPB Opinion 28/2024 on AI models (Dec 2024) — https://www.edpb.europa.eu/our-work-tools/our-documents/opinion-board-art-64/opinion-282024-certain-data-protection-aspects_en
- CJEU: *Planet49* C-673/17 (2019); *Schrems II* C-311/18 (2020); *SCHUFA* C-634/21 (2023); *IAB Europe* C-604/22 (2024), via https://curia.europa.eu/ ; General Court, *Latombe v Commission* T-553/23 (3 Sept 2025), summarised by Lewis Silkin — https://www.lewissilkin.com/insights/2025/09/03/transatlantic-trouble-not-this-time-latombes-challenge-to-eu-us-data-transfers-fails
- Central Consumer Protection Authority, Guidelines for Prevention and Regulation of Dark Patterns, 2023 (30 Nov 2023), summarised by JSA — https://www.jsalaw.com/newsletters-and-updates/ccpa-issues-guidelines-for-prevention-and-regulation-of-dark-patterns-2023/
- CERT-In Directions (28 Apr 2022) and RBI payment-data storage (2018): see the [SEC305](../../../03_majors/cybersecurity_defense/year_3/SEC305_governance_risk_and_compliance/README.md) and DEN404 sources.

_Last reviewed: 2026-10_
