# SEC305 · Governance, Risk and Compliance

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 3 · 6 | 4 (≈ 120 hours) | L2 → L3 | [CS213](../../../../02_year_2_core_computer_science/semester_4/CS213_security_foundations/README.md); pairs with [PRO301](../../../../05_shared_years_3_to_5/PRO301_professional_practice_ethics_law_and_responsible/README.md) | [OV07 Privacy Engineering](../../../../04_overlaps/OV07_privacy_engineering/README.md), [OV10 FinTech Systems Engineering](../../../../04_overlaps/OV10_fintech_systems_engineering/README.md), [SEC402](../../year_4/SEC402_digital_forensics_and_incident_response/README.md), [SAR404](../../../security_architecture/year_4/SAR404_resilience_business_continuity_and_security/README.md) |

Part of the [Cybersecurity Defense major](../../README.md). Legal content here explains what laws and regulations require so engineers and analysts can comply; it is not legal advice. Regulations change: every rule below carries a date, and you are expected to re-check the primary text.

## Why this course matters now

Governance, risk and compliance (GRC) decides what security a company must have, proves it has it, and explains residual risk to the people who own it. In India the obligations tightened sharply in 2025–26. The DPDP Rules were notified in November 2025: a data fiduciary must notify affected people of a personal data breach without delay and send the Data Protection Board a detailed report within 72 hours, with penalties up to ₹250 crore for failing to protect personal data. CERT-In issued binding Comprehensive Cyber Security Audit Policy Guidelines in July 2025, on top of its 2022 six-hour reporting rule. On 31 July 2026 the Reserve Bank of India issued Cybersecurity, Technology: Risk, Resilience and Assurance Framework Directions for commercial banks, effective immediately: vulnerability assessments every six months, disaster-recovery drills that run the DR site as primary for a full business day, and a CISO who reports to the risk executive rather than the head of IT. SEBI's Cybersecurity and Cyber Resilience Framework (August 2024) covers market intermediaries. Globally, NIST's Cybersecurity Framework 2.0 (February 2024) added a "Govern" function, and ISO/IEC 27001:2022 transitions closed in October 2025. AI is now everywhere in GRC: tools such as Vanta, Drata and Microsoft Purview Compliance Manager map controls, collect evidence and draft questionnaire answers with AI. What still needs a skilled person is judgement: deciding which risks matter, spotting evidence that looks complete but proves nothing, and telling a board the truth in plain language.

## Learning outcomes

By the end you can:

1. **Explain** governance vs management, the three lines model and the CISO's role, and **draft** a security governance charter.
2. **Map** an organisation's controls to NIST CSF 2.0, ISO/IEC 27001:2022 Annex A and CIS Controls v8.1, and **find** gaps.
3. **Run** a risk assessment (asset, threat, vulnerability, likelihood, impact), **quantify** a top risk with a FAIR-style Monte Carlo model, and **choose** a treatment.
4. **Build** the core of an ISO 27001 ISMS: scope, risk methodology, Statement of Applicability, policies, internal audit plan.
5. **Test** controls for design and operating effectiveness, and **judge** whether audit evidence is sufficient.
6. **Assess** a third party's security and **write** contract clauses that matter.
7. **Apply** Indian obligations (IT Act, CERT-In Directions and audit guidelines, DPDP Act and Rules, RBI and SEBI frameworks) and key global ones (GDPR, NIS2, DORA, US SEC rules) to a scenario, including reporting clocks.
8. **Design** a business continuity and disaster recovery test, and **report** risk to a board in one page.
9. **Govern** AI use (ISO/IEC 42001, NIST AI RMF) and **verify** AI-generated compliance work.

## Chapters and lessons

### Chapter 1 · What GRC is for (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Governance vs management | Board sets direction and risk appetite; management executes; accountability vs responsibility | Write a risk appetite statement for an illustrative digital lender |
| 1.2 Three lines | IIA Three Lines Model (2020): operations, risk and compliance, internal audit; why independence matters | Place 12 security activities in the right line |
| 1.3 The CISO and reporting lines | Why RBI's 2026 directions require bank CISOs to report to the risk executive, not the head of IT; quarterly board reporting | Argue for and against a CISO reporting to the CIO in 300 words |
| 1.4 GRC as engineering | Controls as code, continuous control monitoring, evidence pipelines | List five controls that can be checked automatically every day |

**Check your understanding:** Why is "compliant" not the same as "secure"? Who owns a risk: the CISO or the business? What breaks if internal audit reports to the CISO?

### Chapter 2 · Frameworks and control catalogues (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 NIST CSF 2.0 | Govern, Identify, Protect, Detect, Respond, Recover; categories, profiles, tiers; February 2024 | Build a current and target profile for a 50-person SaaS company |
| 2.2 ISO/IEC 27001 and 27002:2022 | ISMS clauses 4–10; Annex A's 93 controls in four themes (organisational, people, physical, technological); Amendment 1:2024 on climate | Classify 20 controls into the four themes |
| 2.3 CIS Controls v8.1 and NIST SP 800-53 Rev. 5 | Implementation groups (IG1–IG3); 800-53 control families for government and as a deep catalogue | Pick IG1 safeguards for a 20-person startup |
| 2.4 Mapping | Crosswalks (NIST OLIR), one control satisfying many frameworks, the "common control" library | Map 15 controls across CSF, ISO and CIS |

**Check your understanding:** Why did CSF 2.0 add Govern? When would you choose CIS Controls over ISO 27001? What is lost when one control is mapped to ten requirements?

### Chapter 3 · Risk assessment and quantification (weeks 3–4)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Qualitative risk | ISO/IEC 27005:2022 and NIST SP 800-30 Rev. 1; risk registers, likelihood × impact matrices and their flaws | Build a 15-risk register for an illustrative hospital |
| 3.2 Quantitative risk | Open FAIR: loss event frequency × loss magnitude; calibrated estimates; Monte Carlo simulation; loss exceedance curves | Model one ransomware risk in Python and plot its loss exceedance curve |
| 3.3 Using evidence | Base rates from M-Trends, Verizon DBIR, insurer and regulator data; why vendor statistics need care | Justify each input to your model with a source or say "(unconfirmed)" |
| 3.4 Treatment | Mitigate, transfer (cyber insurance), avoid, accept; acceptance with owner and expiry | Write a treatment plan with costs and residual risk |
| 3.5 Threat-informed risk | Linking risks to adversary behaviour (MITRE ATT&CK) and to detection coverage | Map your top five risks to the detections that would reveal them |

**Check your understanding:** Why can two "high" risks on a heat map differ by 100× in expected loss? What makes an estimate calibrated? Why must every accepted risk expire?

### Chapter 4 · Building an ISMS (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Scope and context | Interested parties, boundaries, interfaces; scoping traps (excluding the hard parts) | Write the ISMS scope for a payments startup |
| 4.2 Statement of Applicability | Selecting Annex A controls, justifying exclusions, linking to risks | Draft an SoA for 30 controls |
| 4.3 Documentation that people use | Required documented information vs paperwork; version control | Put the ISMS documents in Git with review rules |
| 4.4 Certification journey | Stage 1 and stage 2 audits, nonconformities, surveillance audits; internal audit (ISO 19011) | Plan an internal audit programme for one year |

**Check your understanding:** Why do auditors look hard at scope exclusions? What is a major vs a minor nonconformity? Why should the SoA trace back to the risk register?

### Chapter 5 · Policies, standards and exceptions (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 The hierarchy | Policy (why/what), standard (measurable rule), procedure (how), guideline | Rewrite a vague "use strong passwords" policy into a policy, standard and procedure aligned with NIST SP 800-63B-4 |
| 5.2 Writing for people | Plain language, owners, review dates, measurability | Peer-review three policies for testability |
| 5.3 Exceptions | Request, risk assessment, compensating controls, approval level, expiry | Process five exception requests |
| 5.4 Acceptable use and AI use policies | Rules for staff use of generative AI tools: data classes allowed, approved tools, logging | Draft an AI acceptable-use policy for a bank |

**Check your understanding:** Why should a standard be testable by a script? What makes an exception process trustworthy? What data should never go into a public AI tool, and how would you enforce that?

### Chapter 6 · Audits, assurance and evidence (weeks 7–8)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 SOC 2 | AICPA Trust Services Criteria (security, availability, processing integrity, confidentiality, privacy); Type I vs Type II; reading a SOC 2 report and its exceptions | Read a public SOC 2 bridge letter or sample report and list the carve-outs |
| 6.2 Control testing | Design vs operating effectiveness; inquiry, observation, inspection, re-performance; sampling | Test three access-control controls with samples from a provided dataset |
| 6.3 Evidence quality | Screenshots vs system exports vs automated checks; completeness and accuracy of populations | Find the flaw in five evidence packages |
| 6.4 Other assurance | PCI DSS v4.0.1 for card data; CERT-In empanelled audits under the July 2025 guidelines (at least annual comprehensive audit, auditor independence) | Compare PCI DSS and CERT-In audit expectations in a table |
| 6.5 Continuous compliance | GRC platforms (Vanta, Drata, Microsoft Purview Compliance Manager; open-source CISO Assistant and Eramba), APIs for evidence | Automate one evidence check (MFA enforced for all admins) with a script |

**Check your understanding:** Why can a control be well designed and still fail operating-effectiveness testing? What does a qualified SOC 2 opinion tell a customer? Why is a screenshot weak evidence?

### Chapter 7 · Third-party and supply-chain risk (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Why vendors dominate risk | C-Edge Technologies (2024, ~300 Indian co-operative and rural banks disrupted), CrowdStrike (2024), Salesloft Drift (2025); concentration risk | For each case, list the contract and monitoring controls that would have helped |
| 7.2 Assessing vendors | Tiering by data and criticality; questionnaires (Shared Assessments SIG, CSA CAIQ); SOC 2 and ISO certificates; SBOMs | Tier 20 vendors and pick an assessment depth for each |
| 7.3 Contracts | Security schedules, breach notification timelines, right to audit (RBI 2026 requires RBI audit rights in bank contracts), sub-processors, exit plans | Draft a security schedule for a cloud service provider |
| 7.4 Ongoing monitoring | Attack-surface ratings and their limits, reassessments, fourth parties | Design a monitoring cadence and its triggers |

**Check your understanding:** Why is a vendor's SOC 2 report not enough for a critical supplier? What clause would have mattered most in the C-Edge case? Why do security ratings disagree with each other?

### Chapter 8 · Indian law and regulators (weeks 10–11)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 IT Act, 2000 and CERT-In | Sections 43, 66, 70B, 72A (recap from CS213); CERT-In Directions (28 April 2022): report listed incidents within 6 hours, keep logs 180 days, sync clocks | Build a CERT-In reporting decision tree |
| 8.2 DPDP Act 2023 and Rules 2025 | Data fiduciary duties, reasonable security safeguards, Rule 7 breach notices (affected persons without delay; Board within 72 hours), phased commencement to about May 2027, penalties up to ₹250 crore | Draft both breach notices for a scenario |
| 8.3 RBI | Directions of 31 July 2026 for commercial banks (testing cadence, DR drills, DAKSH reporting in 6 hours, DMARC, privileged MFA, CISO independence); earlier 2023 IT governance master direction; outsourcing rules | Turn ten RBI requirements into testable controls |
| 8.4 SEBI and others | SEBI CSCRF (circular of 20 August 2024, compliance deadlines extended into 2025); NCIIPC for critical information infrastructure (section 70A) | Compare RBI and SEBI expectations for a broker that also lends |

**Check your understanding:** Which clocks start when a bank detects a breach of customer data, and who receives each report? Why is the 72-hour DPDP report different from the 6-hour CERT-In report? What does "effective immediately" mean for a bank's GRC team?

### Chapter 9 · Global regulation and reporting clocks (week 11)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 GDPR | Articles 32–34: security of processing, 72-hour notification to the authority, notification to individuals | Decide whether three scenarios need GDPR notification |
| 9.2 EU NIS2 and DORA | NIS2 (Directive 2022/2555): 24-hour early warning, 72-hour notification, one-month report; DORA (Regulation 2022/2554) for financial entities, applying since 17 January 2025 | Build a timeline for a multinational with EU operations |
| 9.3 United States | SEC Form 8-K Item 1.05: disclose material cybersecurity incidents within four business days of determining materiality | Write a materiality memo for a scenario |
| 9.4 Harmonising | One incident, many regulators: a single fact base, a reporting matrix, legal privilege | Build a reporting matrix for an Indian SaaS company with EU and US customers |

**Check your understanding:** Why do reporting rules start the clock at "awareness" or "determination" rather than at the breach? How do you avoid contradictory statements to different regulators? Why does a single fact base matter?

### Chapter 10 · Business continuity and resilience (week 12)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Business impact analysis | Critical processes, RTO, RPO, maximum tolerable downtime; ISO 22301 | Run a BIA for three processes of an illustrative hospital |
| 10.2 DR testing that proves something | Tabletop vs walkthrough vs full failover; RBI 2026 expectation to run DR as primary for a full business day and approach near-zero RPO for critical systems | Design a DR test plan with success criteria |
| 10.3 Ransomware resilience | Isolated recovery environments, restore testing, decision rights during outages | Write the "who decides" table for a ransomware outage |
| 10.4 Supplier dependencies in continuity | Concentration on one cloud or SaaS supplier; exit and substitution plans; testing resilience across interconnected vendor systems (an RBI 2026 expectation for banks) | Map one critical process's dependencies and mark single points of failure |

**Check your understanding:** Why does a successful backup job not prove recovery? What is the difference between RTO and MTD? Who decides to fail over, and with what information?

### Chapter 11 · Metrics and board reporting (week 13)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 KRIs and KPIs | Key risk indicators vs performance indicators; leading vs lagging | Define eight KRIs with thresholds |
| 11.2 Maturity scoring | CSF tiers, CMMI-style scales; why maturity scores get inflated | Score a provided company honestly and justify it |
| 11.3 The one-page board report | Risk in money and time, trend, decisions needed, no jargon | Write a board report and present it in five minutes |
| 11.4 Reporting to boards and supervisors | Quarterly CISO reporting (required for commercial banks by RBI's 2026 directions), audit committee oversight of IS audits, evidence packs | Draft the agenda and evidence pack for a quarterly board cyber review |

**Check your understanding:** Why is "number of blocked attacks" a poor board metric? What decision should every board report ask for? How do you report a risk the board has already accepted?

### Chapter 12 · AI governance and AI in GRC (week 14)
| Lesson | What you learn | Practice |
|---|---|---|
| 12.1 Governing AI systems | ISO/IEC 42001:2023 AI management systems, NIST AI RMF 1.0 and its generative AI profile, NIST IR 8596 Cyber AI Profile (preliminary draft, December 2025), EU AI Act (phased obligations) | Write an AI system inventory and risk-tiering method |
| 12.2 AI in GRC work | Control mapping, policy drafting, questionnaire answers, evidence summarisation; confidentiality of what you upload | Use an AI tool to draft answers to 30 questionnaire items and verify each against evidence |
| 12.3 Failure modes | Invented control IDs, outdated regulation text, confident answers without evidence, over-claiming compliance | Find the errors in a provided AI-generated SoA |
| 12.4 Governing AI features in security products | Vendor due diligence for AI: data use, model changes, logging, published evaluations (methods from [SEC404](../../year_4/SEC404_ai_in_security_operations/README.md)) | Add ten AI-specific questions to your Chapter 7 vendor questionnaire |

**Check your understanding:** Why is an AI-drafted questionnaire answer a legal statement once sent? How do you verify a regulation citation produced by AI? What belongs in an AI system inventory?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Governance charter | Charter and risk appetite |
| 2 | 2 | Lab 2 · CSF profile and mapping | Profile and crosswalk |
| 3 | 3 | Lab 3 · Risk register | Register |
| 4 | 3 | Lab 4 · FAIR Monte Carlo | Loss exceedance curve; **P1 due** |
| 5 | 4 | Lab 5 · Scope and SoA | SoA draft |
| 6 | 5 | Lab 6 · Policy rewrite and exceptions | Policy set |
| 7 | 6 | Lab 7 · Control testing | Test workpapers; mid-term (AI off) |
| 8 | 6 | Lab 7 (cont.) · Evidence automation | Script and output |
| 9 | 7 | Lab 8 · Vendor tiering and contract schedule | **P2 due** |
| 10 | 8 | Lab 9 · India reporting decision tree | Decision tree, breach notices |
| 11 | 8–9 | Lab 9 (cont.) · Reporting matrix | Matrix |
| 12 | 10 | Lab 10 · BIA and DR test plan | Plan |
| 13 | 11 | Board report | Five-minute presentation |
| 14 | 12 | AI-in-GRC verification | **P3 due** |
| 15 | Review | Written case exam and oral defence of P3 | Final exam |

## Working with AI in this course

- **Use AI for:** first drafts of policies and procedures; mapping controls across frameworks; summarising long regulations into checklists that you then verify; drafting questionnaire answers; writing the Monte Carlo code. Microsoft Purview Compliance Manager, GRC platforms' built-in assistants, Claude, ChatGPT and Gemini all help.
- **Do without AI (drills):** the risk register and the choice of treatments; reading primary regulation text (CERT-In Directions, DPDP Rules, RBI directions) and building the reporting decision tree; evidence evaluation; the board report; the mid-term and final.
- **Verify AI output by:** checking every cited clause, section or control ID against the primary text (Gazette, regulator site, ISO/NIST documents); checking the date of each rule (many changed in 2025–26); tracing every questionnaire answer to a piece of evidence; never uploading confidential audit evidence to tools your organisation has not approved.
- **Where AI still fails here (show it, do not assume it):** keep a log of invented control numbers, superseded regulations described as current (for example RBI circulars replaced in July 2026), wrong reporting deadlines, and "compliant" claims with no evidence. Models trained before a regulation changed will state the old rule confidently.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs 1–10 | 25% |
| Projects P1 / P2 / P3 | 5% / 15% / 20% |
| Mid-term (AI off) | 10% |
| Final written case exam (AI off, regulations provided as PDFs) + oral defence of P3 | 25% |

**Mastery gate.** You pass when you can, without AI tools and in three hours: (1) given an unseen company and incident, produce the full reporting matrix (CERT-In, DPDP Board and individuals, sector regulator, any foreign regulator) with correct deadlines and content; (2) build a five-risk register with one risk quantified and treated; (3) review an evidence package for three controls and correctly judge which pass, with reasons.

## Industry reality

GRC analysts, IT auditors, risk managers and CISOs do this work in banks, insurers, fintechs, IT services firms and SaaS companies; GRC is an entry path on the [SEC market page](../../../../06_career_and_market_readiness/01_market_map/roles/SEC_cybersecurity_defense.md). ISC2's 2025 study lists risk assessment among the top three skills needs (29%). Real anchors in this course: RBI's July 2026 directions, CERT-In's July 2025 audit guidelines, the DPDP Rules 2025, SEBI's CSCRF, NIST CSF 2.0 and ISO/IEC 27001:2022.

**Interview questions from this course**

1. *How would you start an ISO 27001 programme at a 150-person startup?* Strong answer: business driver and scope, leadership commitment, risk methodology, asset and risk register, SoA linked to risks, policies people use, evidence automation, internal audit, certification timeline; avoids scoping out the hard parts.
2. *A customer bank sends you a 300-question security questionnaire. How do you handle it?* Strong answer: tier the request, reuse a maintained answer library, attach SOC 2/ISO evidence, never over-claim, route gaps to owners with dates, legal review of commitments, track promises made.
3. *How do you quantify the risk of ransomware for the board?* Strong answer: FAIR-style decomposition, calibrated ranges, sources for base rates, Monte Carlo, loss exceedance curve, comparison with risk appetite, cost and effect of treatments.
4. *An Indian fintech with EU users discovers a breach of customer data at 2 a.m. Which reports are due, and when?* Strong answer: CERT-In within 6 hours for listed incidents; DPDP: affected persons without delay and detailed Board report within 72 hours; RBI if regulated; GDPR 72 hours to the lead authority if applicable; one fact base and legal review.
5. *What makes audit evidence good?* Strong answer: complete population, system-generated, time-stamped, tied to the control and period, re-performable; explains why screenshots and policy documents alone are weak.

## Resources (free first)

- **Frameworks:** [NIST CSF 2.0](https://www.nist.gov/cyberframework) · [CIS Controls v8.1](https://www.cisecurity.org/controls/v8-1) · [NIST SP 800-53 Rev. 5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) · [NIST SP 800-30 Rev. 1](https://csrc.nist.gov/pubs/sp/800/30/r1/final) · [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework) · [NIST IR 8596 (preliminary draft)](https://csrc.nist.gov/pubs/ir/8596/iprd) · [ISO/IEC 27001 overview](https://www.iso.org/standard/27001) (the standard itself is paid) · [ISO/IEC 42001 overview](https://www.iso.org/standard/42001) · [The Open Group, Open FAIR](https://www.opengroup.org/certifications/openfair) · [IIA Three Lines Model](https://www.theiia.org/en/content/position-papers/2020/the-iias-three-lines-model-an-update-of-the-three-lines-of-defense/)
- **India (primary texts):** [CERT-In Directions, 28 Apr 2022](https://www.cert-in.org.in/PDF/CERT-In_Directions_70B_28.04.2022.pdf) · [CERT-In Comprehensive Cyber Security Audit Policy Guidelines (25 Jul 2025, copy hosted by Delhi IT department)](https://it.delhi.gov.in/sites/default/files/IT/generic_multiple_files/comprehensive.pdf) · [DPDP Act 2023](https://www.meity.gov.in/static/uploads/2024/06/2bf1f0e9f04e6fb4f8fef35e82c42aa5.pdf) · [PIB: DPDP Rules notified](https://www.pib.gov.in/PressReleasePage.aspx?PRID=2190014) · [SEBI CSCRF circular (20 Aug 2024)](https://www.sebi.gov.in/legal/circulars/aug-2024/cybersecurity-and-cyber-resilience-framework-cscrf-for-sebi-regulated-entities-res-_85964.html) · [RBI notifications](https://www.rbi.org.in/Scripts/NotificationUser.aspx)
- **Global:** [GDPR text](https://eur-lex.europa.eu/eli/reg/2016/679/oj) · [NIS2 Directive](https://eur-lex.europa.eu/eli/dir/2022/2555/oj) · [DORA](https://eur-lex.europa.eu/eli/reg/2022/2554/oj) · [US SEC cybersecurity disclosure rule](https://www.sec.gov/newsroom/press-releases/2023-139) · [PCI Security Standards Council](https://www.pcisecuritystandards.org/)
- **Tools:** [CISO Assistant (open source)](https://github.com/intuitem/ciso-assistant-community) · [Eramba community edition](https://www.eramba.org/)
- **Paid, optional:** Douglas Hubbard and Richard Seiersen, *How to Measure Anything in Cybersecurity Risk*, 2nd ed. (Wiley, 2023).

## Sources

All checked 12 Oct 2026.

- PIB, DPDP Rules 2025 notified (14 Nov 2025) — https://www.pib.gov.in/PressReleasePage.aspx?PRID=2190014 ; DPDP Rules, Rule 7 text — https://dpdpa.com/dpdparules/rule7.html ; DPDP Act penalties schedule — https://www.meity.gov.in/static/uploads/2024/06/2bf1f0e9f04e6fb4f8fef35e82c42aa5.pdf
- MediaNama, CERT-In cybersecurity audit guidelines (Jul 2025) — https://www.medianama.com/2025/07/223-cert-in-cybersecurity-audit-rules-india/
- DSCI brief on RBI (Commercial Banks – Cybersecurity, Technology: Risk, Resilience and Assurance Framework) Directions, 2026 (31 Jul 2026) — https://www.dsci.in/files/content/knowledge-centre/2026/dsci-brief-on-rbi-cybersecurity-commercial-banks-directions-2026.pdf ; KPMG India summary (Sep 2026) — https://kpmg.com/in/en/insights/2026/09/rbis-technology-focused-master-directions-issued-on-31-july-2026.html
- Taxmann, SEBI extends CSCRF deadline to 31 Aug 2025 — https://www.taxmann.com/post/blog/sebi-extends-cscrf-deadline-for-regulated-entities
- NIST CSF 2.0 (26 Feb 2024) — https://www.nist.gov/cyberframework
- Bright Defense, ISO/IEC 27001:2022 transition deadline of 31 Oct 2025 under IAF MD 26 — https://www.brightdefense.com/news/iso-270012022-deadline-puts-legacy-certificates-at-risk/
- CSO Online, C-Edge ransomware and about 300 Indian banks (Aug 2024) — https://www.csoonline.com/article/3480250/over-300-indian-banks-suffer-payment-disruption-from-ransomware-attack.html
- NIST IR 8596 Cyber AI Profile, preliminary draft (16 Dec 2025) — https://csrc.nist.gov/pubs/ir/8596/iprd
- ISC2, 2025 Cybersecurity Workforce Study — https://www.isc2.org/Insights/2025/12/2025-ISC2-Cybersecurity-Workforce-Study
- EUR-Lex texts of GDPR, NIS2 and DORA; US SEC press release 2023-139 (26 Jul 2023) — links above.

_Last reviewed: 2026-10_
