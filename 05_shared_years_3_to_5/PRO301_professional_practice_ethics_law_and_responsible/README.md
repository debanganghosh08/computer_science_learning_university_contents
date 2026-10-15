# PRO301 · Professional Practice: Ethics, Law and Responsible AI

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 3 · 5 | 4 (≈ 120 hours) | L2 → L3 | [CS213](../../02_year_2_core_computer_science/semester_4/CS213_security_foundations/README.md) | [IND401](../IND401_industry_co_op_studio/README.md), [OV07A](../../04_overlaps/OV07_privacy_engineering/OV07A_privacy_by_design_and_privacy_enhancing/README.md), [OV07B](../../04_overlaps/OV07_privacy_engineering/OV07B_data_protection_law_for_engineers_in_practice/README.md), [THS501](../THS501_thesis_or_capstone_i/README.md), [LCH502](../LCH502_career_launch_and_founder_studio/README.md) |

> This course is educational and is **not legal advice**. Laws, rules and dates were checked in October 2026 against the sources listed at the end. Read the primary text before relying on any provision, and take decisions with a qualified lawyer.

## Why this course matters now

The engineer who designs a logging pipeline, a consent screen, a model-training job or a dependency upgrade decides, in practice, whether a company obeys the law. India's DPDP Rules were notified in November 2025 with most duties applying from May 2027, the EU AI Act is phasing in through 2028, and an IT Rules amendment in force since 20 February 2026 requires labelling of AI-generated media. General-purpose assistants (Claude, ChatGPT, Gemini) now draft privacy notices, summarise licences and red-line contracts in seconds, and licence scanners such as ScanCode and Syft flag dependencies automatically. They also cite draft rules as final, invent section numbers and call source-available software "open source". A professional who can read the primary text, turn it into engineering requirements, and say no in writing when something is wrong is hard to replace.

## Learning outcomes

By the end you can:

1. **Apply** the ACM Code of Ethics (2018) and the IEEE Code of Ethics to an unseen dilemma and **write** a defensible decision record.
2. **Explain** why named software failures happened (Therac-25, Horizon, Knight Capital, CrowdStrike 2024), separating technical, organisational and regulatory causes.
3. **Map** a product's data flows to duties under the DPDP Act 2023, the DPDP Rules 2025, the IT Act 2000, the CERT-In Directions and the GDPR, with the date each duty applies.
4. **Classify** an AI system under the EU AI Act and **build** a dated obligations calendar.
5. **Audit** a repository's licences, **detect** incompatible combinations and **produce** correct notices and an SBOM.
6. **Measure** a model's fairness with at least three metrics, **apply** one mitigation and **report** the trade-off honestly.
7. **Measure** the energy of an inference workload and **reduce** it with evidence.
8. **Audit** an interface against WCAG 2.2 AA and Indian accessibility law, and **fix** the barriers.
9. **Red-line** an employment contract (IP assignment, confidentiality, non-compete, bond) and **explain** what is enforceable in India.
10. **Escalate** a concern in writing through the right channel and **explain** what whistleblower protection does and does not exist.

## Chapters and lessons

### Chapter 1 · Professional codes and ethical reasoning (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Why software is a profession | Duty to the public above employer and client; ACM Code 2018 (principles 1.1–1.7, responsibilities 2.1–2.9, leadership 3.1–3.7); IEEE Code (Policy 7.8); the ACM/IEEE-CS Software Engineering Code's eight principles | Map 10 workplace dilemmas to the clause each triggers |
| 1.2 Frameworks as tools | Consequences, duties and rights, virtue, fairness (veil of ignorance), care; why one lens is never enough | Analyse "ship with a known minor data leak" under four lenses |
| 1.3 A decision procedure | Facts → stakeholders → options → tests (publicity, reversibility, "would I accept this as the user") → decision → record | Write a one-page decision record for a dark-pattern request |

**Check your understanding:** Two ACM principles conflict in your dilemma; how do you decide which wins, and how do you show your reasoning? Why is "it is legal" not the end of an ethical analysis? What evidence would make you change your decision record?

### Chapter 2 · When software harms: case studies (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Therac-25 (1985–87) | Race condition, hardware interlocks removed in favour of software, cryptic errors, slow incident reporting (Leveson and Turner) | Draw the causal chain: code, organisation, regulator |
| 2.2 Post Office Horizon (UK) | Software records treated as proof of theft; *Bates v Post Office* (2019); convictions quashed by the Post Office (Horizon System) Offences Act 2024; public inquiry | Mark each point where an engineer could have spoken |
| 2.3 Knight Capital (1 Aug 2012) | Repurposed flag reactivated dead code on one of eight servers; loss of over $460 million in about 45 minutes; SEC order (2013) | Write the deployment checklist that would have caught it |
| 2.4 Volkswagen defeat device | Emissions-test detection code; an engineer sentenced to 40 months in 2017; "I was told to" is not a defence | Draft your reply if asked to write such code |
| 2.5 CrowdStrike (19 July 2024) | A faulty content update crashed Windows hosts worldwide; kernel-level risk; staged rollout and validation lessons from the published root-cause analysis | Compare the RCA remediations with your own rollout design |

**Check your understanding:** In which of these cases was the code "correct" by its specification? Why do organisations keep trusting software records over people, and what design choices counter that? What one practice would have prevented two of the five failures?

### Chapter 3 · Indian cyber law for engineers: the IT Act and IT Rules (week 3)
Builds on [CS213](../../02_year_2_core_computer_science/semester_4/CS213_security_foundations/README.md) Chapter 11 (sections 43, 66, 70B, 72A).

| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Offences engineers meet | Sections 66C (identity theft), 66D (cheating by personation), 66E (privacy of images), 67/67A, 72A; what the 2008 amendment added | Classify 8 scenarios by section and say who is liable |
| 3.2 Intermediaries and safe harbour | Section 79; *Shreya Singhal v Union of India* (2015) struck down section 66A and read "actual knowledge" as a court or government order; IT Rules 2021 due diligence; significant social media intermediaries (50 lakh users) | List the duties of a hypothetical community app at 10 lakh and 60 lakh users |
| 3.3 Synthetic media rules (2026) | IT Rules amendment notified 10 Feb 2026, in force 20 Feb 2026: definition of synthetically generated information, labelling and provenance duties, 3-hour takedown of flagged unlawful content | Design the labelling and provenance pipeline for an image-generation feature |
| 3.4 Blocking and interception | Sections 69 and 69A; confidentiality of orders; what an engineer must and must not do on receiving one | Write an internal runbook for handling a lawful order |
| 3.5 CERT-In Directions as requirements | 28 April 2022 Directions: 20 incident types, report within 6 hours, 180-day logs kept in India, clocks synced to NIC/NPL NTP, 5-year subscriber records for VPN, VPS, cloud and data-centre providers | Turn each direction into an architecture requirement with a test |

**Check your understanding:** Why did the Supreme Court tie safe harbour to orders rather than complaints, and what does that mean for a takedown queue? Which CERT-In direction is hardest for a startup on a foreign cloud, and how would you meet it? Why does a 3-hour takedown duty change on-call design?

### Chapter 4 · The DPDP Act 2023 and DPDP Rules 2025 (weeks 4–5)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Actors and scope | Data principal, data fiduciary, data processor, consent manager, Significant Data Fiduciary (SDF); section 3 reach (processing in India, and abroad when offering goods or services to people in India) | Label every actor in an illustrative food-delivery app |
| 4.2 Notice and consent | Section 6 consent (free, specific, informed, unconditional, unambiguous, clear affirmative action); section 5 and Rule 3 notice; withdrawal as easy as giving; legitimate uses (section 7) | Build a notice and consent flow; prove withdrawal takes no more steps than consent |
| 4.3 Children | Under 18 is a child; verifiable parental consent (section 9, Rule 10); no tracking, behavioural monitoring or targeted advertising directed at children | Design age-gating with verifiable consent and list its failure modes |
| 4.4 Security, breach and retention | Reasonable security safeguards (section 8(5); Rule 6 includes logs kept at least one year); breach notice to each affected person and to the Board without delay, then a detailed report within 72 hours (Rule 7); erasure when purpose ends, with set inactivity periods for the largest platforms (Rule 8) | Build one breach timeline that meets CERT-In (6 hours), DPDP (72 hours) and GDPR (72 hours) |
| 4.5 Rights, Board and penalties | Rights of access, correction, erasure, grievance and nomination (sections 11–14); Schedule maxima: ₹250 crore (security safeguards), ₹200 crore (breach notice), ₹200 crore (children), ₹150 crore (SDF duties), ₹50 crore (other), ₹10,000 (duties of principals); section 44 removes IT Act section 43A | Price a described failure against the Schedule and argue mitigating factors |
| 4.6 Timeline | Rules notified 13 Nov 2025 (G.S.R. 846(E)); Board provisions immediate; consent-manager registration from Nov 2026; substantive duties from May 2027; until then section 43A and the 2011 SPDI Rules still apply | Build a startup compliance roadmap from today to May 2027 |

**Check your understanding:** Your analytics SDK sends device IDs to a processor abroad: who is the fiduciary, and what must the contract say? Why is "consent for everything" a weak design under section 6? What would you log to prove, a year later, that a given user consented to a given purpose?

### Chapter 5 · Global privacy and AI regulation (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 GDPR for Indian teams | Article 3(2) reach; lawful bases (Art. 6); special categories (Art. 9); data protection by design (Art. 25); processors (Art. 28); 72-hour breach notice (Art. 33); DPIA (Art. 35); automated decisions (Art. 22); fines up to €20 million or 4% of turnover (Art. 83) | Fill a 12-row DPDP vs GDPR comparison from the texts |
| 5.2 EU AI Act structure | Prohibited practices (Art. 5), high-risk (Annexes I and III), transparency (Art. 50), general-purpose AI; provider vs deployer; fines up to €35 million or 7% | Classify 8 systems (CV screening, support chatbot, credit scoring, emotion recognition at work, deepfake generator…) |
| 5.3 AI Act dates, as amended | In force 1 Aug 2024; prohibitions and AI literacy 2 Feb 2025; GPAI 2 Aug 2025; transparency Aug 2026; AI Omnibus in force 27 July 2026 moved Annex III high-risk to 2 Dec 2027 and Annex I to 2 Aug 2028 and added a ban on nudification apps from Dec 2026 | Build a dated calendar for an Indian SaaS selling an HR-screening model in the EU |
| 5.4 India's AI governance | India AI Governance Guidelines (MeitY, Nov 2025): non-statutory, principle-based, relies on existing law; RBI's FREE-AI framework for finance (Aug 2025) | Map five AI harms to the Indian law that would actually apply |
| 5.5 Standards | NIST AI RMF 1.0 (Govern, Map, Measure, Manage); ISO/IEC 42001:2023 AI management systems; how standards enter contracts | Write the RMF "Map" section for one feature |

**Check your understanding:** Why might a model be lawful to sell in India and high-risk in the EU? What changes for you as a deployer versus a provider? Which AI Act date would you plan against if the law changes again, and why?

### Chapter 6 · Intellectual property, contracts and your job (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Who owns code | Programs are literary works (Copyright Act 1957, s. 2(o)); employer is first owner of work made under a contract of service (s. 17); freelancers keep copyright unless assigned in writing (s. 19) | Review 3 clauses and find the assignment that fails |
| 6.2 Software and patents | Patents Act 1970, s. 3(k): "a mathematical or business method or a computer programme per se or algorithms" are not inventions; technical effect | Judge two claim drafts: "per se" or not |
| 6.3 AI output and authorship | US Copyright Office Part 2 report (Jan 2025): human authorship required; *Thaler v Perlmutter* (D.C. Cir. 2025); *ANI v OpenAI* filed in the Delhi High Court (Nov 2024), outcome (unconfirmed) | Write a team policy on provenance of AI-generated code |
| 6.4 Employment contracts | IP assignment and prior-inventions schedules; confidentiality; Indian Contract Act s. 27 makes post-employment non-competes generally void; non-solicit, moonlighting, training bonds, notice periods; Labour Codes in force 21 Nov 2025 (wages at least 50% of pay for gratuity and PF; gratuity after one year for fixed-term staff) | Red-line a sample offer letter; list five questions for HR |
| 6.5 Leaving a job cleanly | No standalone trade-secret statute in India (contract and breach of confidence instead); no code, documents or customer lists leave with you; clean-room rebuilds | Write your personal exit checklist |

**Check your understanding:** A friend builds your startup's app for free; who owns it? Why can a non-compete be void and still cost you a job offer? What would make an AI-assisted patch risky to merge into a GPL project?

### Chapter 7 · Open-source licences in depth (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Permissive licences | MIT, BSD-2/3-Clause; Apache-2.0 patent grant, patent-suit termination, NOTICE file, change statements | Produce correct notices for an app with 30 dependencies |
| 7.2 Copyleft | GPL-2.0-only vs -or-later; GPL-3.0 installation information and patent terms; LGPL relinking; MPL-2.0 file-level; AGPL-3.0 s. 13 network use | For SaaS, mobile, on-prem binary, internal tool, library and firmware, list triggered duties |
| 7.3 Compatibility | Apache-2.0 into GPL-3.0 yes, into GPL-2.0-only no; SPDX expressions (AND, OR, WITH) | Build an 8-licence compatibility matrix and check it against the FSF list |
| 7.4 Source-available and relicensing | HashiCorp to BSL 1.1 (2023) → OpenTofu; Redis to RSAL/SSPL (2024) → Valkey; Redis adds AGPLv3 (2025); Elasticsearch adds AGPL (2024); CLA vs DCO | Write a risk note on depending on a single-vendor project |
| 7.5 Compliance at scale, and AI | SBOMs (SPDX, CycloneDX); ScanCode, Syft, ORT, REUSE; model licences (OpenRAIL, Llama-style use restrictions); OSI Open Source AI Definition 1.0 (Oct 2024); project rules on AI contributions (Gentoo ban, Apr 2024; NetBSD; QEMU code provenance) | Scan a real repo and resolve every "unknown" licence |

**Check your understanding:** Why is the AGPL treated differently from the GPL by SaaS companies? What does a CLA let a company do that a DCO does not? Is a model with open weights and a use-restricted licence "open source"? Defend your answer with the OSI definition.

### Chapter 8 · Responsible AI I: fairness and transparency (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Sources of bias | Historical, representation, measurement and label bias; proxies; *Gender Shades* (2018): error up to 34.7% for darker-skinned women vs 0.8% for lighter-skinned men; Amazon's abandoned recruiting model (Reuters, 2018) | Audit the demographic make-up of a public dataset |
| 8.2 Metrics that conflict | Demographic parity, equal opportunity, equalised odds, calibration; impossibility results (Kleinberg et al. 2016; Chouldechova 2017); the COMPAS debate (ProPublica, 2016) | Compute four metrics with Fairlearn on folktables ACSIncome |
| 8.3 Mitigation and its cost | Reweighing, constrained training (exponentiated gradient), threshold post-processing; when not to deploy | Apply one method; report accuracy and fairness before and after |
| 8.4 Transparency artefacts | Model cards (Mitchell et al.), datasheets (Gebru et al.); SHAP and counterfactual explanations and their limits | Write the model card for your mitigated model |
| 8.5 Public-sector harm | Dutch childcare-benefits scandal (Amnesty, 2021): risk scoring with nationality as a factor; privacy as a fundamental right in India (*Puttaswamy*, 2017) | Write an algorithmic impact assessment for a welfare-eligibility model |

**Check your understanding:** Why can a perfectly calibrated model still have unequal false-positive rates? Who should choose the fairness metric, and how do you record that choice? When is the right answer "do not automate this"?

### Chapter 9 · Responsible AI II: safety and accountability for LLM systems (week 10)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Liability for wrong answers | *Moffatt v Air Canada* (2024): the airline was liable for its chatbot's wrong refund advice; *Mata v Avianca* (2023): lawyers sanctioned for fabricated ChatGPT citations | Design escalation and grounding for a support bot; list what disclaimers cannot fix |
| 9.2 Security harms | OWASP Top 10 for LLM Applications (prompt injection, sensitive information disclosure, excessive agency…); defence in depth | Red-team only your own RAG app against five risks; log fixes |
| 9.3 Evals, oversight and incidents | Pre-deployment evals, staged release, monitoring; automation bias and meaningful human review (GDPR Art. 22); AI Incident Database; blameless postmortems | Write a postmortem for one database incident |
| 9.4 Synthetic media | Deepfakes; India's 2026 labelling duty; EU Art. 50; C2PA content credentials and how metadata gets stripped | Add C2PA manifests to generated images; test what removes them |

**Check your understanding:** Why did "the chatbot is a separate entity" fail as a defence? What makes a human review "meaningful", in numbers you could measure? Which prompt-injection defence would you trust least, and why?

### Chapter 10 · The environmental cost of compute (week 11)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Scale | IEA: data centres used about 415 TWh in 2024 (~1.5% of world electricity), projected about 945 TWh by 2030, with AI the main driver | Estimate your own monthly AI energy use and state the uncertainty |
| 10.2 Training vs inference | Strubell et al. (2019); Patterson et al. (2021): model, hardware, PUE and grid carbon intensity; Luccioni et al. (2024): generative models cost far more per task than task-specific ones | Recompute one training estimate on an Indian vs a Nordic grid |
| 10.3 Reading disclosures | Google (Aug 2025): median Gemini Apps text prompt 0.24 Wh and 0.26 mL water, 33× less energy than a year earlier; what such figures exclude | Measure three inference set-ups with CodeCarbon |
| 10.4 Engineering for efficiency | Smaller and distilled models, quantisation, caching, batching, region and time shifting; rebound effects | Cut energy per request by 30% and prove it |

**Check your understanding:** Why is energy per prompt a poor proxy for total footprint? When does a smaller model cost more overall? What would you put in a design doc's sustainability section?

### Chapter 11 · Accessibility as an engineering duty (week 12)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Who is excluded | WHO: about 1.3 billion people (16%) live with significant disability; screen readers, switch access, captions | Use your product for 30 minutes with a screen reader only |
| 11.2 WCAG 2.2 | POUR; levels A/AA/AAA; new in 2.2: focus not obscured, dragging movements, target size (24×24 CSS px), consistent help, redundant entry, accessible authentication | Audit one flow against every new AA criterion |
| 11.3 Indian law | RPwD Act 2016 (ss. 40, 42); *Rajive Raturi v UoI* (8 Nov 2024): accessibility rules must be mandatory; *Pragya Prasun / Amar Jain v UoI* (30 Apr 2025): digital access is part of Art. 21, e-KYC must be accessible; GIGW 3.0 | Audit an e-KYC flow for blink-based liveness checks and short OTP timeouts |
| 11.4 Global and testing | EU Accessibility Act applies from 28 June 2025; US Section 508; axe-core catches only part of the problems; NVDA, TalkBack, keyboard-only testing; limits of AI-generated alt text | Fix 10 issues and verify with assistive technology |

**Check your understanding:** Why does an automated score of 100 not mean a page is accessible? What did the e-KYC cases change for fintech engineers? Which WCAG 2.2 criterion would most change your login page?

### Chapter 12 · Dissent, whistleblowing and your own line (weeks 13–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 12.1 Raising concerns inside | Escalation ladder, written records, vigil mechanism under Companies Act 2013 s. 177(9)–(10) | Write an escalation email for a privacy-violating feature |
| 12.2 Whistleblower law | India's Whistle Blowers Protection Act 2014 covers public servants and has never been brought into force; EU Directive 2019/1937; US SEC programme | Compare an engineer's protection in India, the EU and the US |
| 12.3 Cases of dissent | The Horizon sub-postmasters' decade-long fight (Chapter 2) seen from the engineers' side; the University of Minnesota "hypocrite commits" and the Linux kernel's ban (2021) as research misconduct; the dispute around "On the Dangers of Stochastic Parrots" (FAccT 2021) | Analyse one case: channels used, cost, what changed |
| 12.4 Your line | When to refuse work; documenting refusal; collective action; ACM 1.2 and 2.3 | Write your one-page professional ethics statement and defend it orally |

**Check your understanding:** What would you need in writing before you go outside the company? Why does India's lack of an operative whistleblower law change the order of your steps? What is one thing you will not build, and what would change your mind?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Decision records | Dilemma map |
| 2 | 2 | Lab 2 · Failure causal chains | Case analysis 1 |
| 3 | 3 | Lab 3 · IT Rules and CERT-In requirements | — |
| 4 | 4 | Lab 4 · Data map and notice | — |
| 5 | 4 | Lab 5 · Breach tabletop | **P1 due** |
| 6 | 5 | Lab 6 · AI Act classification | Obligations calendar |
| 7 | 6 | Lab 7 · Contract red-line | Mid-term (open statute, AI off) |
| 8 | 7 | Lab 8 · Licence audit and SBOM | — |
| 9 | 8 | Lab 9 · Fairness audit | — |
| 10 | 9 | Lab 10 · LLM red-team (own system) | **P2 due** |
| 11 | 10 | Lab 11 · Energy measurement | — |
| 12 | 11 | Lab 12 · Accessibility audit | — |
| 13 | 12 | Escalation writing | Case analysis 2 |
| 14 | 12 | Ethics statement | **P3 due** |
| 15 | Review | Oral defence of P3 | Final exam (open statute, AI off) |

## Working with AI in this course

- **Use AI for:** a first section map of a long statute (then check it line by line); test scenarios for a policy; first drafts of notices and runbooks; SBOM scripts; Fairlearn and CodeCarbon boilerplate.
- **Do without AI (drills):** both case analyses, the DPDP-GDPR comparison, the contract red-line, licence-obligation questions, the ethics statement and both exams.
- **Verify AI output by:** opening the primary text (India Code, the MeitY DPDP page, EUR-Lex, the CERT-In page) for every section number and date; checking that a rule is the **final** version, not the January 2025 draft; running ScanCode on any licence claim; recomputing every fairness number yourself.
- **Where AI still fails here:** models trained before late 2025 do not know the final DPDP Rules, the 2026 IT Rules amendment or the AI Omnibus dates; they confuse source-available with open source; they invent case citations, which is exactly what sanctioned the lawyers in *Mata v Avianca*. Keep a log of every wrong legal claim an assistant gives you during the term, with the correct source.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (12, short written or code deliverables) | 25% |
| Projects P1–P3 | 35% |
| Two case analyses and the ethics statement | 10% |
| Mid-term (open statute, AI off) | 10% |
| Final exam (open statute, AI off) and P3 oral defence | 20% |

**Mastery gate.** You pass when you can, in three hours with the statutes open and AI tools off: (1) take an unseen product description and produce a data map with every DPDP, CERT-In and GDPR duty, the correct section or rule, and the date it applies, with no invented provisions; (2) find every licence conflict in a 40-package dependency list for a stated distribution model; (3) write a one-page ethical analysis of an unseen case citing at least three ACM clauses and a concrete recommendation; (4) compute two fairness metrics from a confusion matrix by hand and explain the trade-off.

## Industry reality

Privacy engineering, trust and safety, responsible-AI review, open-source programme offices (OSPOs) and compliance engineering are distinct jobs at large firms; in startups they fall on whichever engineer understands them. The [privacy overlap](../../04_overlaps/OV07_privacy_engineering/) goes further.

**Interview questions from this course**

1. *A product manager wants full request bodies logged "for debugging". What do you do?* Strong answer: identifies personal data in bodies, proposes structured logs with field allow-lists and masking, ties retention to purpose (DPDP Rule 6 sets a one-year floor for some logs; CERT-In needs 180-day ICT logs), restricts access, documents the decision.
2. *Can we use an AGPL library in our SaaS backend? A GPL one?* Strong answer: distinguishes distribution from network use, explains AGPL s. 13, describes options (separate service with published source, alternatives, commercial licence), mentions scanning and legal sign-off.
3. *Design consent for a lending app under the DPDP Act.* Strong answer: purpose-specific itemised notice, separable consents, withdrawal as easy as consent, consent records with versions, children's handling, processor contracts, breach path, dates when duties apply.
4. *Our model approves women 20% less often. Walk me through your investigation.* Strong answer: checks base rates and label bias, computes several metrics by group, looks for proxies, tests mitigations, reports trade-offs, involves domain and legal owners, considers not deploying.
5. *You find a bug that exposes customer data a week before launch and your manager says to ship. What now?* Strong answer: quantifies the risk, proposes a fix or feature flag, escalates in writing, knows the 6-hour CERT-In and DPDP breach duties if data was already exposed, and knows the vigil-mechanism route.

## Resources (free first)

- **Codes:** ACM Code of Ethics — https://www.acm.org/code-of-ethics ; IEEE Code of Ethics — https://www.ieee.org/about/corporate/governance/p7-8.html ; Software Engineering Code — https://ethics.acm.org/code-of-ethics/software-engineering-code/
- **Indian law (primary):** India Code (IT Act 2000, Copyright Act 1957, Patents Act 1970, Contract Act 1872, RPwD Act 2016) — https://www.indiacode.nic.in/ ; MeitY data protection framework (DPDP Act and Rules) — https://www.meity.gov.in/data-protection-framework ; CERT-In Directions — https://www.cert-in.org.in/Directions70B.jsp ; *Shreya Singhal* — https://indiankanoon.org/doc/110813550/ ; *Puttaswamy* (2017) — https://indiankanoon.org/doc/91938676/ ; *Rajive Raturi* judgment — https://api.sci.gov.in/supremecourt/2005/9321/9321_2005_1_1503_56986_Judgement_08-Nov-2024.pdf
- **EU and global:** GDPR — https://eur-lex.europa.eu/eli/reg/2016/679/oj ; AI Act — https://eur-lex.europa.eu/eli/reg/2024/1689/oj and the Commission's timeline page — https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai ; GPAI Code of Practice — https://digital-strategy.ec.europa.eu/en/policies/contents-code-gpai ; NIST AI RMF — https://www.nist.gov/itl/ai-risk-management-framework
- **Licences:** SPDX licence list — https://spdx.org/licenses/ ; choosealicense — https://choosealicense.com/ ; REUSE — https://reuse.software/ ; OSI Open Source AI Definition — https://opensource.org/ai/open-source-ai-definition ; ScanCode — https://github.com/aboutcode-org/scancode-toolkit ; Syft — https://github.com/anchore/syft ; ORT — https://oss-review-toolkit.org/
- **Responsible AI:** Fairlearn — https://fairlearn.org/ ; AIF360 — https://github.com/Trusted-AI/AIF360 ; folktables — https://github.com/socialfoundations/folktables ; Model Cards — https://arxiv.org/abs/1810.03993 ; Datasheets — https://arxiv.org/abs/1803.09010 ; OWASP LLM Top 10 — https://owasp.org/www-project-top-10-for-large-language-model-applications/ ; AI Incident Database — https://incidentdatabase.ai/ ; C2PA — https://c2pa.org/
- **Energy:** CodeCarbon — https://codecarbon.io/ ; ML.ENERGY leaderboard — https://ml.energy/leaderboard/
- **Accessibility:** WCAG 2.2 — https://www.w3.org/TR/WCAG22/ and what's new — https://www.w3.org/WAI/standards-guidelines/wcag/new-in-22/ ; GIGW — https://guidelines.india.gov.in/ ; axe rules — https://www.dequeuniversity.com/rules/axe/ ; NVDA — https://www.nvaccess.org/
- **Paid, optional:** none needed; every primary text above is free.

## Sources

- CERT-In, Directions under s. 70B(6) (28 Apr 2022), PDF text read for the 6-hour, 180-day, NTP and 5-year requirements and the 20 incident types — https://www.cert-in.org.in/Directions70B.jsp (checked 2026-10)
- DPDP phased commencement (14 Nov 2025, 14 Nov 2026, 14 May 2027; s. 43A repeal on the last date) — Shardul Amarchand Mangaldas — https://www.amsshardul.com/insight/enforcement-of-the-dpdp-act-and-notification-of-the-dpdp-rules/ (checked 2026-10); note that summaries differ between 13 and 14 November for notification
- DPDP Rule 7 text (72 hours) — https://dpdpa.com/dpdparules/rule7.html (checked 2026-10)
- DPDP penalty figures and child age — PRS Legislative Research — https://prsindia.org/billtrack/digital-personal-data-protection-bill-2023 (checked 2026-10)
- IT Rules amendment on synthetically generated information (notified 10 Feb 2026, in force 20 Feb 2026) — Hogan Lovells — https://www.hoganlovells.com/en/publications/india-introduces-mandatory-labelling-for-ai-and-3hour-takedown-for-illegal-content (checked 2026-10)
- EU AI Act timeline and AI Omnibus (in force 27 July 2026) — European Commission — https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai ; summary of changed dates — https://www.regulation-ai.eu/en/changes/ (checked 2026-10)
- India AI Governance Guidelines (5 Nov 2025) — Mondaq summary — https://www.mondaq.com/article/1707626 (checked 2026-10)
- Labour Codes effective 21 Nov 2025 — KPMG — https://www.in.kpmg.com/taxflashnews/KPMG-Flash-News-GOI-notifies-implementation-of-Labour-Codes.pdf ; EY — https://www.ey.com/content/dam/ey-unified-site/ey-com/en-in/alerts-hub/2025/11/new-labour-codes-implemented-across-the-country-effective-21-november-2025.pdf (checked 2026-10)
- Whistle Blowers Protection Act 2014 not in force — Khaitan & Co guide (2026) — https://www.khaitanco.com/sites/default/files/2026-10/Guide%20to%20Whistleblowing.pdf (checked 2026-10)
- *Pragya Prasun / Amar Jain v UoI* (30 Apr 2025) — Vidhi Centre for Legal Policy — https://vidhilegalpolicy.in/blog/digital-access-as-a-fundamental-right/ (checked 2026-10)
- Therac-25: Leveson and Turner (1993) — https://web.stanford.edu/class/cs240/old/sp2014/readings/therac-25.pdf ; Horizon Inquiry — https://www.postofficehorizoninquiry.org.uk/ ; Post Office (Horizon System) Offences Act 2024 — https://www.legislation.gov.uk/ukpga/2024/14/contents ; Knight Capital SEC order — https://www.sec.gov/litigation/admin/2013/34-70694.pdf ; VW engineer sentencing (US DoJ, 2017) — https://www.justice.gov/opa/pr/volkswagen-engineer-sentenced-his-role-conspiracy-cheat-us-emissions-tests ; CrowdStrike remediation hub — https://www.crowdstrike.com/falcon-content-update-remediation-and-guidance-hub/ (all checked 2026-10)
- *Moffatt v Air Canada*, 2024 BCCRT 149 — https://decisions.civilresolutionbc.ca/crt/crtd/en/525448/1/document.do ; *Mata v Avianca* sanctions opinion (22 June 2023) — https://storage.courtlistener.com/recap/gov.uscourts.nysd.575368/gov.uscourts.nysd.575368.54.0_1.pdf (checked 2026-10)
- *Gender Shades* — https://proceedings.mlr.press/v81/buolamwini18a.html ; ProPublica "Machine Bias" — https://www.propublica.org/article/machine-bias-risk-assessments-in-criminal-sentencing ; Reuters on Amazon's recruiting tool (Oct 2018) — https://www.reuters.com/article/us-amazon-com-jobs-automation-insight-idUSKCN1MK08G ; Kleinberg et al. — https://arxiv.org/abs/1609.05807 ; Chouldechova — https://arxiv.org/abs/1610.07524 ; Amnesty, "Xenophobic Machines" — https://www.amnesty.org/en/latest/news/2021/10/xenophobic-machines-dutch-child-benefit-scandal/ (checked 2026-10)
- IEA, *Energy and AI* (Apr 2025) — https://www.iea.org/reports/energy-and-ai/executive-summary ; Strubell et al. — https://arxiv.org/abs/1906.02243 ; Patterson et al. — https://arxiv.org/abs/2104.10350 ; Luccioni et al. — https://arxiv.org/abs/2311.16863 ; Elsworth et al. (Google, Aug 2025) — https://arxiv.org/abs/2508.15734 (checked 2026-10)
- Licence events: Redis (Mar 2024) — https://redis.io/blog/redis-adopts-dual-source-available-licensing/ ; Redis AGPLv3 — https://redis.io/blog/agplv3/ ; Elastic — https://www.elastic.co/blog/elasticsearch-is-open-source-again ; HashiCorp BSL — https://www.hashicorp.com/en/blog/hashicorp-adopts-business-source-license ; Gentoo council (14 Apr 2024) — https://projects.gentoo.org/council/meeting-logs/20240414-summary.txt ; NetBSD — https://www.netbsd.org/developers/commit-guidelines.html ; QEMU — https://www.qemu.org/docs/master/devel/code-provenance.html (checked 2026-10)
- WHO disability fact sheet — https://www.who.int/news-room/fact-sheets/detail/disability-and-health ; LWN on the "hypocrite commits" — https://lwn.net/Articles/853717/ ; Bender, Gebru et al., "On the Dangers of Stochastic Parrots" (FAccT 2021) — https://dl.acm.org/doi/10.1145/3442188.3445922 ; US Copyright Office AI reports — https://www.copyright.gov/ai/ (checked 2026-10)

_Last reviewed: 2026-10_
