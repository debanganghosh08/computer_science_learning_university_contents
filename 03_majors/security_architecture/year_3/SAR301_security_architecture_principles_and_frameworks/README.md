# SAR301 · Security Architecture Principles and Frameworks

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 3 · 5 | 4 (≈ 120 hours) | L2 → L3 | [CS213](../../../../02_year_2_core_computer_science/semester_4/CS213_security_foundations/README.md), [CS212](../../../../02_year_2_core_computer_science/semester_4/CS212_distributed_systems_i/README.md) | [SAR401](../../year_4/SAR401_cloud_security_architecture/README.md), [SAR404](../../year_4/SAR404_resilience_business_continuity_and_security/README.md), [OV01 Cloud Security](../../../../04_overlaps/OV01_cloud_security/README.md) |

Part of the [Security Architecture major](../../README.md). Taken alongside [SAR302 Threat Modeling](../SAR302_threat_modeling/README.md) and [SAR303 Zero Trust Architecture](../SAR303_zero_trust_architecture/README.md). CS213 taught the principles by name; this course turns them into decisions, documents and review processes that a whole organisation builds on. Governance programmes and audits are covered in [SEC305](../../../cybersecurity_defense/year_3/SEC305_governance_risk_and_compliance/README.md); here frameworks are used as design inputs, not as compliance checklists.

## Why this course matters now

A security architect decides, before code exists, where trust boundaries sit, which controls are mandatory and which risks a business may accept. The cost of getting this wrong shows in the US Cyber Safety Review Board's report on the 2023 Exchange Online intrusion: a consumer signing key could be used to forge tokens that enterprise mailboxes accepted, and the Board judged the intrusion preventable and Microsoft's security culture inadequate ([CSRB, March 2024](https://www.cisa.gov/sites/default/files/2025-03/CSRBReviewOfTheSummer2023MEOIntrusion508.pdf)). That is an architecture failure: a key from one trust domain was valid in another. Frameworks keep moving too. NIST CSF 2.0 (February 2024) added a Govern function, and NIST SP 800-53 Release 5.2.0 (August 2025) added controls for secure software updates ([NIST](https://www.nist.gov/news-events/news/2025/08/nist-revises-security-and-privacy-control-catalog-improve-software-update)). AI tools now draft control mappings and review designs: AWS Security Agent previewed design review in December 2025, checking design documents against requirement packs such as NIST CSF and PCI DSS ([AWS](https://aws.amazon.com/blogs/aws/new-aws-security-agent-secures-applications-proactively-from-design-to-deployment-preview/)). What still needs a person is deciding which requirement matters for *this* system, defending that decision to engineers and executives, and owning the risk that remains.

## Learning outcomes

By the end you can:

1. **Apply** the Saltzer–Schroeder principles and their modern extensions (secure defaults, minimised trust, blast-radius limits, assume breach) to find design flaws in an unseen architecture.
2. **Design** layered controls and **explain** where layers share a failure mode, so that "defense in depth" is real rather than decorative.
3. **Write** testable security requirements, abuse cases and acceptance criteria, traced to threats, regulations and OWASP ASVS 5.0 levels.
4. **Use** NIST CSF 2.0, SP 800-53 Rev. 5 and ISO/IEC 27001:2022 Annex A as design libraries, and **produce** a machine-readable control set in OSCAL.
5. **Model** an enterprise security architecture with SABSA layers and attributes, and **integrate** security into a TOGAF 10 architecture cycle.
6. **Document** an architecture with C4 diagrams, security overlays and architecture decision records (ADRs) that a reviewer can check.
7. **Run** a design review and an architecture review board (ARB) intake, and **write** a risk acceptance with owner, compensating controls and expiry.
8. **Audit** AI-generated control mappings and design reviews, and **show** at least three errors they contain.

## Chapters and lessons

### Chapter 1 · What security architects actually do (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Architecture vs engineering vs operations | Architects set structure and constraints others build on; engineers implement; operations run and detect. Decision rights, and why an architect without them only writes documents | Map 15 security activities at an illustrative bank to architect, engineer or operator |
| 1.2 The artefacts | Reference architectures, patterns, standards, security requirements, ADRs, threat models, risk acceptances; who reads each | Collect one public example of each (vendor reference architectures, open ADR repositories) |
| 1.3 Vocabulary that prevents arguments | Asset, trust boundary, attack surface, control objective vs control, security invariant ("no data store is reachable from the internet"), residual risk | Rewrite five vague statements from a design doc as testable invariants |
| 1.4 Case study: the 2023 Exchange Online intrusion | Key scope, token validation across trust domains, crash-dump handling, logging available only at a premium tier; the CSRB recommendations | Write a one-page architecture lesson list from the CSRB report: decision, flaw, principle violated |

**Check your understanding:** (1) Why is "encrypt all data" a control objective rather than a design? (2) Which artefact would have caught the Exchange Online key-scope flaw earliest, and who would have needed authority to act on it? (3) What makes a security invariant testable?

### Chapter 2 · Design principles in depth (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Saltzer and Schroeder (1975), revisited | The eight principles plus work factor and compromise recording; which still hold exactly and which need reinterpretation for cloud and AI agents | For each principle, find one 2024–2026 public incident that violated it |
| 2.2 Least privilege and least common mechanism | Shared mechanisms as shared fate (a shared admin plane, a shared CI runner, a shared signing key) | Redesign a deployment pipeline where one runner builds both public and payment code |
| 2.3 Secure defaults and economy of mechanism | Fail-closed vs fail-open with real costs; small trusted computing bases; complexity as attack surface | Decide fail-open or fail-closed for six controls (WAF, fraud scoring, authorization service, DLP, rate limiter, payment tokenizer) and justify each |
| 2.4 Modern additions | Minimise trust, limit blast radius, assume breach, design for recovery; the IEEE Center for Secure Design's top ten design flaws (2014); NCSC secure design principles | Score a provided design against the NCSC principles |
| 2.5 Psychological acceptability today | Usability as security: approval fatigue, exception sprawl, "shadow" workarounds | Find the workaround users will invent for three over-strict controls |

**Check your understanding:** (1) When does fail-closed reduce security overall? (2) Why is a shared signing key a least-common-mechanism violation even if access to it is tightly controlled? (3) Which principle does "assume breach" most change in practice?

### Chapter 3 · Defense in depth and control design (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Control types | Preventive, detective, corrective, deterrent, compensating; technical, administrative, physical | Classify 30 controls from a real policy set |
| 3.2 Correlated failure | Layers that share identity, code, vendor or operator fail together; common-mode failure; the "Swiss cheese" model and its limits | Find the common-mode failure in a provided three-layer design |
| 3.3 Control effectiveness | Coverage, bypassability, operating cost, false-positive burden; evidence that a control works | Rate five controls on these axes with evidence |
| 3.4 Guardrails, gates and invariants | Preventive guardrails (organisation policies, admission control) vs review gates; continuously checked invariants | Express eight invariants as policy-as-code checks |
| 3.5 Blast radius engineering | Account, network, key, tenant and identity boundaries as the units that limit damage | Draw blast-radius maps for one key, one role and one CI token |

**Check your understanding:** (1) Two layers both rely on the same identity provider. Are they two layers? (2) When is a detective control the better choice than a preventive one? (3) What evidence would convince you a control works in production?

### Chapter 4 · Security requirements engineering (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Where requirements come from | Threats, laws (India's DPDP Act 2023 "reasonable security safeguards", CERT-In 180-day log retention), contracts, data classification, business attributes | Build a requirement source register for an illustrative lending app |
| 4.2 Writing testable requirements | "Shall" statements, measurable thresholds, verification method (test, inspection, analysis, demonstration) | Rewrite 15 untestable requirements |
| 4.3 Catalogues | OWASP ASVS 5.0 (May 2025) levels as a requirement library; mobile (MASVS); cloud benchmarks | Select ASVS requirements for a level-2 web app and justify omissions |
| 4.4 Abuse and misuse cases | Abuse cases next to use cases; "evil user stories"; acceptance criteria that fail when the abuse succeeds | Write ten abuse cases for a ticket-booking flow inspired by IRCTC (illustrative) |
| 4.5 Traceability | Threat → requirement → control → test → evidence; keeping the chain alive as designs change | Build a traceability matrix in a spreadsheet or YAML |

**Check your understanding:** (1) Why is "the system shall be secure" not a requirement? (2) Which requirement sources change without any code change? (3) What breaks when traceability stops at the control?

### Chapter 5 · NIST CSF 2.0 as an architecture input (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Structure | Six functions (Govern, Identify, Protect, Detect, Respond, Recover), categories, subcategories, implementation examples; what changed from 1.1 (Govern; PR.AC split into PR.AA and others) | Map ten CSF 1.1 subcategory IDs to their 2.0 equivalents using NIST's reference tool |
| 5.2 Profiles and tiers | Current and target organisational profiles; tiers describe governance rigour, not maturity of a system | Write a target profile for one product line |
| 5.3 From outcomes to architecture | Which architectural decisions satisfy which outcomes (for example, PR.DS data security outcomes → key hierarchy and data zoning) | Link 12 CSF outcomes to the artefacts that would evidence them |
| 5.4 The risk management stack | SP 800-37 Rev. 2 (Risk Management Framework), SP 800-30 Rev. 1 (risk assessment), and where CSF sits | Draw the stack and mark where the architect contributes |

**Check your understanding:** (1) Why do CSF outcomes not tell you which control to build? (2) What does the Govern function demand from architects specifically? (3) Why are tiers a poor score for a single system?

### Chapter 6 · Control catalogues as design libraries (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 NIST SP 800-53 Rev. 5 | 20 control families, enhancements, baselines (SP 800-53B), Release 5.2.0 (August 2025: SA-24 design for cyber resiliency, SI-02(07) root cause analysis of flaws) | Tailor the moderate baseline for one service and justify five removals |
| 6.2 ISO/IEC 27001:2022 Annex A | 93 controls in four themes; Statement of Applicability as a design record | Compare Annex A and 800-53 coverage for access control |
| 6.3 CIS Controls v8.1 and CSA Cloud Controls Matrix | Implementation groups; cloud-specific mappings | Pick IG2 safeguards for a 200-person SaaS firm |
| 6.4 Machine-readable controls | OSCAL catalogs, profiles, component definitions and system security plans; NIST's Cybersecurity and Privacy Reference Tool (CPRT) | Write an OSCAL component definition for one service and validate it |
| 6.5 Crosswalks | NIST OLIR mappings; one control satisfying several frameworks; mapping drift | Map 15 controls across CSF 2.0, 800-53 and ISO 27001 with sources |

**Check your understanding:** (1) Why is tailoring a baseline an architecture decision? (2) What can OSCAL automate, and what can it not? (3) Why do crosswalks go stale?

### Chapter 7 · Systems security engineering (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 SP 800-160 Vol. 1 Rev. 1 (2022) | Engineering trustworthy secure systems: protection needs, loss-driven engineering, life-cycle processes, the design principles appendix | Derive protection needs for a hospital records system (illustrative) |
| 7.2 Cyber resiliency engineering | SP 800-160 Vol. 2 Rev. 1 (2021): goals, objectives, techniques (diversity, segmentation, non-persistence, deception, redundancy) | Choose three techniques for a payment switch and state what each costs |
| 7.3 Assurance cases | Claims, arguments, evidence; Goal Structuring Notation | Build an assurance case for "tenant data cannot cross tenants" |
| 7.4 Trust and the trusted computing base | What must be trusted, how to make it small, how to verify it | List the trusted computing base of a CI/CD system and shrink it by one component |

**Check your understanding:** (1) What is the difference between a security requirement and a protection need? (2) Why does non-persistence help against attackers who already got in? (3) What makes evidence in an assurance case weak?

### Chapter 8 · Enterprise security architecture frameworks (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 SABSA | Business attributes profiling; six layers (contextual, conceptual, logical, physical, component, service management) against what/why/how/who/where/when | Build a SABSA attributes profile for a UPI-style payments app (illustrative) |
| 8.2 From attributes to controls | Traceability down the layers; measurable attribute definitions | Trace two attributes ("available", "non-repudiable") to components |
| 8.3 TOGAF Standard, 10th Edition | The Architecture Development Method; where security requirements, risk and controls enter each phase; The Open Group's "Integrating Risk and Security" guidance | Annotate an ADM cycle with security inputs and outputs |
| 8.4 Other reference models | Open Security Architecture patterns, Microsoft Cybersecurity Reference Architectures (MCRA), NIST SP 1800 practice guides | Compare two reference models for one capability |
| 8.5 Choosing a framework | Fit to organisation size, regulation and existing EA practice; the cost of framework theatre | Recommend a framework for three organisations and defend it |

**Check your understanding:** (1) What does SABSA give that a control catalogue does not? (2) Where in the ADM is security usually added too late? (3) When is a heavyweight framework harmful?

### Chapter 9 · Documenting architecture so others can check it (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 C4 and data-flow diagrams | Context, container, component levels; DFDs with trust boundaries | Draw C4 levels 1–3 for an illustrative telemedicine app |
| 9.2 Security overlays | Data classification, identity flows, key hierarchy, network zones as separate views of one model | Produce four overlays for the same system |
| 9.3 Architecture decision records | Context, decision, status, consequences (Nygard format); decision logs; superseding decisions | Write five ADRs, including one that rejects an option |
| 9.4 Diagrams as code | Structurizr DSL, Mermaid, PlantUML; reviewable diffs; generating diagrams from infrastructure | Keep your model in Git and review a change by diff |

**Check your understanding:** (1) Why should an ADR record the rejected options? (2) What does a key-hierarchy view reveal that a network diagram hides? (3) Why do hand-drawn diagrams drift from reality?

### Chapter 10 · Reference architectures and patterns (weeks 10–11)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Edge and ingress | Gateway, WAF, bot defence, mTLS termination, token validation at the edge vs in the service | Design ingress for a public API with partner and mobile clients |
| 10.2 Identity and token patterns | Central identity provider, token exchange, backend-for-frontend, service identity | Choose patterns for three client types with ADRs |
| 10.3 Data protection patterns | Tokenization vaults, field-level encryption, data zoning; the Aadhaar Data Vault pattern (reference keys, HSM-held keys, restricted zone) required by UIDAI Circular 14 of 2025 | Design a data vault for a fintech that stores Aadhaar numbers, following the UIDAI FAQ |
| 10.4 Administrative and break-glass access | Separate admin plane, privileged access workstations, break-glass with monitoring | Design break-glass for a cloud estate and its alerting |
| 10.5 Anti-patterns | Shared service accounts, flat networks, "god" tokens, security by obscurity in mobile apps, secrets in config | Find seven anti-patterns in a provided architecture |

**Check your understanding:** (1) Why does UIDAI forbid hashing Aadhaar numbers to make reference keys? (2) When should token validation happen in the service even if the gateway validated it? (3) What makes break-glass access safe to keep?

### Chapter 11 · Design reviews and architecture review boards (weeks 12–13)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Review models | Lightweight self-review, paired review, full review; risk-tiered intake so effort follows risk | Write an intake questionnaire that routes 80% of designs to lightweight review |
| 11.2 Running a review | Preparation, walk-through, findings with severity and rationale, agreed actions and owners | Run a 60-minute review of a classmate's design and write the findings |
| 11.3 Risk acceptance | Who may accept which risk, compensating controls, expiry and re-review; exception sprawl | Write two risk acceptances and one refusal |
| 11.4 The ARB as an operating model | Membership, decision rights, service levels, escalation, metrics (lead time, share of designs reviewed before build, findings closed before launch) | Design an ARB charter for a 500-engineer company |
| 11.5 Influence without authority | Security champions, paved roads, office hours; how to say no with an alternative | Role-play a review where the delivery team pushes back |

**Check your understanding:** (1) Why do review boards that see every change become bottlenecks, and what replaces them? (2) What must a risk acceptance contain to be defensible a year later? (3) How do you measure whether reviews change outcomes?

### Chapter 12 · AI in architecture work (week 14)
| Lesson | What you learn | Practice |
|---|---|---|
| 12.1 What AI does well here | Summarising long standards, first-draft requirements, first-pass mappings, diagram-to-text extraction | Generate a first-draft requirement set and mark which items you keep |
| 12.2 Design review agents | AWS Security Agent design review (preview) checking documents against managed and custom requirement packs; general assistants with your own checklists | Run an assistant review of a design you already reviewed by hand; compare findings |
| 12.3 Failure modes | Invented or retired control IDs, CSF 1.1 identifiers presented as 2.0, missing system context, confident "compliant" verdicts without evidence | Find the errors in a provided AI-generated control mapping |
| 12.4 Confidentiality of what you upload | Architecture documents are sensitive; approved tools, data classes, retention | Write the AI-use rule for your ARB |

**Check your understanding:** (1) Why is a design review agent's "pass" weaker evidence than its "fail"? (2) How do you check a control ID cheaply? (3) What context does an assistant usually lack in a design review?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · CSRB case dissection | Lesson list |
| 2 | 2 | Lab 2 · Principle hunt | Principle-to-incident table |
| 3 | 3 | Lab 3 · Common-mode failure | Blast-radius maps |
| 4 | 4 | Lab 4 · Requirements and abuse cases | Requirement set; **P1 due** |
| 5 | 5 | Lab 5 · CSF 2.0 target profile | Profile and artefact links |
| 6 | 6 | Lab 6 · OSCAL component definition | Validated OSCAL file |
| 7 | 7 | Lab 7 · Assurance case | Claims-arguments-evidence diagram; mid-term (AI off) |
| 8 | 8 | Lab 8 · SABSA attributes | Attributes profile |
| 9 | 9 | Lab 9 · Architecture as code | C4 model in Git, five ADRs |
| 10 | 10 | Data vault design workshop | Vault design; **P2 due** |
| 11 | 10 | Anti-pattern review | Findings list |
| 12 | 11 | Design review practice | Review findings |
| 13 | 11 | ARB simulation | Charter and decisions |
| 14 | 12 | Lab 10 · AI mapping audit | Error log; **P3 due** |
| 15 | Review | Oral defence of P3 | Final exam |

## Working with AI in this course

- **Use AI for:** summarising long standards before you read the relevant section yourself; drafting requirement sets and abuse cases that you then prune; converting your control list into OSCAL skeletons; generating C4 or Mermaid diagrams from your text; producing a second-opinion design review. Claude, ChatGPT and Gemini all handle this; AWS Security Agent's design review (preview) works on uploaded design documents.
- **Do without AI (drills):** principle-based flaw finding on an unseen design (weekly, 30 minutes); writing risk acceptances; the CSF 1.1 to 2.0 mapping lab; the mid-term and final exam; the ARB role-play.
- **Verify AI output by:** checking every control ID in NIST CPRT or the ISO standard text; confirming the revision and release (SP 800-53 Release 5.2.0, CSF 2.0, ASVS 5.0); asking for the threat each requirement answers and checking it exists in your threat model; never accepting "compliant" without named evidence.
- **Where AI still fails here (show it):** ask three assistants for the CSF 2.0 subcategory that covers identity proofing and record how many answer with retired 1.1 identifiers; ask for SP 800-53 controls covering software update integrity and check whether the 2025 additions appear; give an assistant a design with a cross-tenant key-scope flaw like the Exchange Online case and record whether it finds it unprompted.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs 1–10 | 25% |
| Projects P1 / P2 / P3 | 5% / 15% / 25% |
| Mid-term (AI off): principles and requirements | 10% |
| Final: written design review of an unseen system (AI off) plus oral defence of P3 | 20% |

**Mastery gate.** You pass when you can, without AI and in three hours: (a) review an unseen two-page architecture and find at least five of the seven planted principle violations, each with the principle named and a fix; (b) write ten testable security requirements for it, traced to threats and to CSF 2.0 or SP 800-53 identifiers that you can show are correct; and (c) write one risk acceptance that a reviewer judges complete (owner, scope, compensating controls, expiry, re-review trigger).

## Industry reality

- **Microsoft** launched its Secure Future Initiative after the 2023 intrusion; the CSRB report is now required reading for anyone who designs token signing or key scope.
- **India's regulators write architecture into rules.** UIDAI's Circular 14 of 2025 requires requesting entities to keep Aadhaar numbers in an Aadhaar Data Vault, reference them by non-derivable keys, and hold signing and decryption keys in an HSM ([UIDAI FAQ, Nov 2025](https://uidai.gov.in/images/FAQs_Aadhaar_Data_Vault_03112025_v10.pdf)). RBI's 2026 directions for commercial banks set CISO independence and resilience expectations (see [SEC305](../../../cybersecurity_defense/year_3/SEC305_governance_risk_and_compliance/README.md)).
- **Reference architectures are public**: the AWS Security Reference Architecture, Microsoft's MCRA and Google Cloud's enterprise foundations blueprint are used as starting points in real reviews.
- Hiring loops for architects include a design review exercise and a risk-communication scenario ([market map](../../../../06_career_and_market_readiness/01_market_map/roles/SAR_security_architecture.md)).

**Interview questions from this course**

1. *"Walk me through how you would review a new payments service design."* Strong answer: scope and data classification first; C4 and DFD with trust boundaries; threats per boundary; requirement and control check against a standard; findings ranked by risk with fixes; who decides on residual risk; follow-up before launch.
2. *"What does defense in depth mean, and how can it fail?"* Strong answer: independent layers; common-mode failure through shared identity, vendor or operator; an example; how to test independence.
3. *"How do you write a security requirement developers will actually meet?"* Strong answer: testable, with threshold and verification method, linked to a threat, sized to the risk tier, with a paved-road implementation.
4. *"An engineering director wants to launch with a known high-severity finding. What do you do?"* Strong answer: quantify the risk in business terms, propose compensating controls and a fix date, route to the right risk owner, write an expiring acceptance, monitor the exposure.
5. *"When would you use SABSA or TOGAF, and when not?"* Strong answer: attribute-driven traceability for large regulated enterprises; integration with an existing EA practice; avoid heavyweight frameworks for small teams; give an example of a lighter alternative.

## Resources (free first)

- **Foundational reading:** Saltzer and Schroeder, [The Protection of Information in Computer Systems](https://web.mit.edu/Saltzer/www/publications/protection/) (1975); Ross Anderson, [Security Engineering, 3rd edition](https://www.cl.cam.ac.uk/archive/rja14/book.html) (chapters free); Google, [Building Secure and Reliable Systems](https://sre.google/books/) (free online); IEEE Center for Secure Design, [Avoiding the Top 10 Software Security Design Flaws](https://ieeecs-media.computer.org/media/technical-activities/CYBSI/docs/Top-10-Flaws.pdf).
- **Standards:** [NIST CSF 2.0](https://www.nist.gov/cyberframework); [SP 800-53 Rev. 5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final); [SP 800-160 Vol. 1 Rev. 1](https://csrc.nist.gov/pubs/sp/800/160/v1/r1/final); [SP 800-160 Vol. 2 Rev. 1](https://csrc.nist.gov/pubs/sp/800/160/v2/r1/final); [SP 800-37 Rev. 2](https://csrc.nist.gov/pubs/sp/800/37/r2/final); [OSCAL](https://pages.nist.gov/OSCAL/); [CPRT](https://csrc.nist.gov/Projects/cprt); [OWASP ASVS](https://owasp.org/www-project-application-security-verification-standard/); [NCSC secure design principles](https://www.ncsc.gov.uk/collection/cyber-security-design-principles).
- **Frameworks:** [The SABSA Institute](https://sabsa.org/) (white papers free; courses paid); [TOGAF Standard](https://www.opengroup.org/togaf) (free download for personal use after registration; check the licence terms); [Open Security Architecture](https://www.opensecurityarchitecture.org/); [Microsoft Cybersecurity Reference Architectures](https://learn.microsoft.com/en-us/security/adoption/mcra).
- **Documentation tools:** [C4 model](https://c4model.com/); [ADR resources](https://adr.github.io/); [Structurizr](https://docs.structurizr.com/); [Mermaid](https://mermaid.js.org/).
- **Paid, optional:** Sherwood, Clark and Lynas, *Enterprise Security Architecture: A Business-Driven Approach* (the SABSA book, 2005). The free SABSA white papers cover the core ideas.

## Sources

All checked 12 Oct 2026.

- CSRB, *Review of the Summer 2023 Microsoft Exchange Online Intrusion* (20 Mar 2024) — https://www.cisa.gov/sites/default/files/2025-03/CSRBReviewOfTheSummer2023MEOIntrusion508.pdf
- NIST, CSF 2.0 (26 Feb 2024) — https://www.nist.gov/cyberframework
- NIST, SP 800-53 Release 5.2.0 (27 Aug 2025) and summary of changes — https://www.nist.gov/news-events/news/2025/08/nist-revises-security-and-privacy-control-catalog-improve-software-update ; https://csrc.nist.gov/files/projects/Risk-Management/800-53%20Comment%20Site/SP800-53-r5.2.0-changes.pdf
- AWS, Security Agent preview with design review (Dec 2025) — https://aws.amazon.com/blogs/aws/new-aws-security-agent-secures-applications-proactively-from-design-to-deployment-preview/
- UIDAI, Circular No. 14 of 2025 — https://uidai.gov.in/images/Circular-No.14_of-2025.pdf ; Aadhaar Data Vault FAQ (3 Nov 2025) — https://uidai.gov.in/images/FAQs_Aadhaar_Data_Vault_03112025_v10.pdf
- OWASP ASVS 5.0.0 release (30 May 2025) — https://github.com/OWASP/ASVS/releases/tag/v5.0.0_release
- The SABSA Institute, certification and framework pages — https://sabsa.org/certification/
- The Open Group, TOGAF certifications and the "Integrating Risk and Security" credential — https://www.opengroup.org/certifications/togaf
- Market facts: [SAR market page](../../../../06_career_and_market_readiness/01_market_map/roles/SAR_security_architecture.md) (checked Oct 2026)

_Last reviewed: 2026-10_
