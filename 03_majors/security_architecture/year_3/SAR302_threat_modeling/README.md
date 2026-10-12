# SAR302 · Threat Modeling

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 3 · 5 | 4 (≈ 120 hours) | L2 → L4 | [CS213](../../../../02_year_2_core_computer_science/semester_4/CS213_security_foundations/README.md), [CS212](../../../../02_year_2_core_computer_science/semester_4/CS212_distributed_systems_i/README.md) | [SAR402](../../year_4/SAR402_identity_architecture_at_scale/README.md), [SAR403](../../year_4/SAR403_security_architecture_for_ai_systems_and_agents/README.md), [OV05 AI Security and Safety](../../../../04_overlaps/OV05_ai_security_safety/README.md) |

Part of the [Security Architecture major](../../README.md). Taken alongside [SAR301](../SAR301_security_architecture_principles_and_frameworks/README.md) and [SAR303](../SAR303_zero_trust_architecture/README.md). CS213 Chapter 2 introduced the four questions, data-flow diagrams and STRIDE in one week. This course makes threat modeling a method you can run on any system, teach to others, scale across an organisation and check when an AI tool does it for you. It is defensive analysis: you reason about what could go wrong in order to design it out, and you never build or run attacks.

## Why this course matters now

Threat modeling is the cheapest security control there is: a flaw removed from a diagram costs nothing to patch later. It is also being automated fast. AWS added STRIDE threat modeling from design documents or source code to AWS Security Agent in public preview on 17 June 2026, usable from IDEs such as Kiro and Claude Code ([AWS](https://aws.amazon.com/about-aws/whats-new/2026/06/aws-security-agent-threat-modeling/)), and open-source tools such as AWS Labs' Threat Designer and STRIDE GPT generate threat models from diagrams with a large language model. The evidence on quality is sobering. In one study, five LLMs classifying six 5G threats with STRIDE reached at most 72% accuracy ([arXiv 2505.04101](https://arxiv.org/abs/2505.04101)); a May 2026 study of 52 configurations across 8 models found gains from larger or domain-adapted models "neither consistent nor sufficient for reliable threat modelling" ([arXiv 2605.10808](https://arxiv.org/abs/2605.10808)). Meanwhile new system classes need new methods: the Cloud Security Alliance published MAESTRO for agentic AI in February 2025, and OWASP published its Top 10 for Agentic Applications in December 2025. The human work that remains is deciding what the system really is, which threats matter for this business, and whether the mitigations actually hold.

## Learning outcomes

By the end you can:

1. **Model** a system as data-flow diagrams, sequence diagrams and trust boundaries at the right level of detail, including its cloud control plane, CI/CD and third parties.
2. **Elicit** threats with STRIDE (per element and per interaction), attack trees, PASTA and LINDDUN, and **explain** which method fits which question.
3. **Rate** and **prioritise** threats with a stated, repeatable method, and **say** why DREAD-style scores mislead.
4. **Design** mitigations, turn them into requirements and tests, and **verify** them with evidence.
5. **Threat-model** ML, LLM and agentic systems using MITRE ATLAS, NIST AI 100-2, the OWASP LLM and Agentic Top 10 lists and CSA MAESTRO.
6. **Run** a threat modeling session with an engineering team in 90 minutes and leave with owned actions.
7. **Build** threat models as code (pytm, Threagile) and **wire** them into pull-request workflows so models stay current.
8. **Evaluate** an AI-generated threat model for precision and recall against a reference model, and **document** its failure modes.

## Chapters and lessons

### Chapter 1 · Why, when and how much (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 The four questions in depth | What are we working on, what can go wrong, what are we going to do about it, did we do a good job; the Threat Modeling Manifesto's values and anti-patterns (the "hero threat modeler", admiration for the problem) | Critique three published threat models against the Manifesto |
| 1.2 Triggers and scope | New system, significant change, new data type, incident, new regulation; time-boxing; "just enough" models | Write a trigger policy for a 40-team engineering organisation |
| 1.3 Outputs that get used | Threat list, mitigation backlog, assumptions log, residual-risk statement; where each lives (tracker, repository, ADR) | Convert a 30-row threat spreadsheet into tracker issues with owners |
| 1.4 Sessions with people | Facilitation, roles (driver, scribe, devil's advocate), keeping engineers engaged, remote whiteboards | Facilitate a 45-minute session with classmates and get feedback |

**Check your understanding:** (1) Why does a threat model with no owners fail even if every threat is correct? (2) When is skipping a threat model the right call? (3) What should the assumptions log contain?

### Chapter 2 · Modelling the system (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Data-flow diagrams done right | Processes, stores, external entities, flows, trust boundaries; levels of decomposition; common mistakes (missing admin paths, missing batch jobs) | Redraw a deliberately wrong DFD and list each fix |
| 2.2 Other views | Sequence diagrams for protocols, state machines for workflows, deployment views for infrastructure | Draw the OAuth authorization-code flow of a partner integration as a sequence diagram |
| 2.3 Trust boundaries | Where privilege, ownership, network zone or tenant changes; boundaries inside one process (plugins, sandboxes) | Mark every boundary in a multi-tenant SaaS diagram |
| 2.4 Modelling from artefacts | Deriving the model from code, OpenAPI specs and infrastructure as code; detecting drift | Generate a draft DFD from a Terraform plan and correct it by hand |

**Check your understanding:** (1) Why do most serious threats sit on boundaries? (2) What is usually missing from a DFD drawn by the team that built the system? (3) How do you know a model is detailed enough?

### Chapter 3 · STRIDE as a method, not a mnemonic (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 STRIDE per element and per interaction | Which threat types apply to processes, stores, flows and entities; the property each threat breaks | Run STRIDE-per-interaction on a payment initiation flow |
| 3.2 Threat libraries | MITRE CAPEC attack patterns as prompts for defenders; vendor and internal libraries | Map 15 of your threats to CAPEC entries |
| 3.3 Games and prompts | Elevation of Privilege and OWASP Cornucopia card decks; structured brainstorming | Play one round of each on the same system and compare coverage |
| 3.4 Avoiding laundry lists | Collapsing duplicates, writing threats as "actor, action, asset, impact", killing irrelevant threats with stated reasons | Reduce a 120-item generated list to the 25 that matter |

**Check your understanding:** (1) Why does "information disclosure" on a data flow often turn into a requirement about the endpoint, not the wire? (2) What makes a threat statement actionable? (3) Why can card games find threats a checklist misses?

### Chapter 4 · Attack trees and adversary models (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Attack trees | Schneier's AND/OR trees (1999); annotating cost, skill and detectability; attack-defense trees | Build a tree for "move money without the account holder's consent" in a wallet app |
| 4.2 Adversary models | Capability, access and motivation; insiders; supply-chain adversaries; what an attacker already holds (stolen session, partner credential) | Write three adversary profiles for one system and show how each changes the tree |
| 4.3 MITRE ATT&CK as defender vocabulary | Tactics and techniques used to ask "would we detect this?"; linking threats to detections owned by the SOC | Map five tree leaves to ATT&CK techniques and the log source that would reveal them |
| 4.4 Kill-chain thinking for design | Where in a chain a design control breaks it earliest and cheapest | Choose the single cheapest control that cuts the most leaves of your tree |

**Check your understanding:** (1) Why do OR nodes deserve more design attention than AND nodes? (2) What does an insider adversary change about trust boundaries? (3) Why map threats to detections in a design course?

### Chapter 5 · PASTA: risk-centric threat modeling (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 The seven stages | Business objectives, technical scope, decomposition, threat analysis, weakness analysis, attack modelling, risk and impact | Run stages 1–3 for an illustrative insurance claims portal |
| 5.2 Business impact first | Linking threats to money, regulation and customers; using SABSA attributes from SAR301 | Write impact statements in rupees and hours for five threats |
| 5.3 Threat intelligence inputs | Using public threat reports and sector advisories (CERT-In, CISA) responsibly; base rates | Justify three likelihood estimates with public sources or mark them "(unconfirmed)" |
| 5.4 When PASTA is worth it | Cost of the method against the value at risk; combining with STRIDE for elicitation | Decide which method to use for four systems and defend it |

**Check your understanding:** (1) What does PASTA add that STRIDE alone lacks? (2) Why is threat intelligence a weak input without base rates? (3) When is PASTA too heavy?

### Chapter 6 · Privacy threat modeling with LINDDUN (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Privacy is not confidentiality | Linking, identifying, non-repudiation (as a privacy harm), detecting, data disclosure, unawareness and unintervenability, non-compliance | Classify ten privacy harms from public cases into LINDDUN categories |
| 6.2 LINDDUN GO and PRO | Lightweight card-based elicitation vs systematic per-element analysis | Run LINDDUN GO on a fitness app that shares data with an insurer (illustrative) |
| 6.3 Mapping to law | India's DPDP Act 2023 and Rules 2025 (notice, consent, purpose limitation, erasure, breach notice), GDPR in outline | Map each privacy threat to the duty it would breach |
| 6.4 Privacy mitigations | Data minimisation, pseudonymisation, aggregation, consent records, retention limits, privacy-preserving analytics | Redesign one data flow to remove a linking threat |

**Check your understanding:** (1) Why can strong non-repudiation be a privacy problem? (2) Which privacy threat survives perfect encryption? (3) How does purpose limitation turn into a design constraint?

### Chapter 7 · Rating, ranking and stopping (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Why DREAD fails | Subjective scales, double counting, false precision | Score ten threats with DREAD twice, a week apart, and measure your own drift |
| 7.2 Better options | OWASP Risk Rating; simple likelihood × impact with written criteria; FAIR-style ranges for the top few; CVSS v4.0 for vulnerabilities, not threats | Re-rank the same ten threats with written criteria and compare stability |
| 7.3 Blast radius and reachability | Ranking by who can reach the threat and how far damage spreads | Add reachability to your ranking and see what moves |
| 7.4 Stopping rules | Coverage criteria per element, time boxes, diminishing returns | Write a stopping rule and apply it to a large model |

**Check your understanding:** (1) Why is CVSS the wrong tool for ranking design threats? (2) What makes a rating method repeatable? (3) How do you know you have done enough?

### Chapter 8 · From threats to mitigations and evidence (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Treatment options | Eliminate by design, mitigate, transfer, accept; why elimination beats mitigation | Find three threats you can eliminate by changing the design |
| 8.2 Mitigations as requirements | Writing the mitigation as a testable requirement (link to SAR301 Chapter 4) | Convert 15 mitigations into requirements with tests |
| 8.3 Validation | Security unit tests, abuse-case tests, configuration checks, review evidence; "did we do a good job?" | Write tests for five mitigations and run them |
| 8.4 Tracking and retrospectives | Mitigation backlog, residual risk sign-off, measuring escaped threats after incidents | Run a retrospective on a public post-incident report: which threat model question would have caught it? |

**Check your understanding:** (1) Why is "add monitoring" a weak mitigation on its own? (2) What evidence proves a mitigation exists in production, not only in the design? (3) How do escaped threats improve the method?

### Chapter 9 · Tools and threat models as code (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Diagramming tools | OWASP Threat Dragon (v2), Microsoft Threat Modeling Tool, AWS Threat Composer; strengths and lock-in | Model one system in two tools and compare outputs |
| 9.2 Models as code | OWASP pytm (Python), Threagile (YAML with risk rules); reports generated in CI | Rewrite your Chapter 3 model in pytm and generate the report |
| 9.3 Keeping models current | Pull-request templates with threat questions, model diffs, drift alerts when infrastructure changes | Add a CI job that fails when a new external flow appears without a model update |
| 9.4 Choosing for an organisation | Self-service vs expert-led, templates, integration with trackers | Write a one-page tooling recommendation for a 300-engineer company |

**Check your understanding:** (1) What does a model-as-code tool catch that a diagram tool does not? (2) Why do generated reports get ignored? (3) What is the minimum signal that a model is out of date?

### Chapter 10 · Distributed, cloud and supply-chain systems (weeks 10–11)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Microservices and meshes | Service identity, east-west traffic, sidecars, shared libraries; the authorization service as a single point of failure | Model a five-service order system with a service mesh |
| 10.2 Event-driven systems | Producers, brokers, consumers; poisoned events, replay, schema evolution, consumer privilege | Threat-model a Kafka-based payment events pipeline |
| 10.3 The cloud control plane | IAM, metadata services, management APIs and CI/CD as part of the system, not around it | Add the control plane to a model that ignored it and list the new threats |
| 10.4 Third parties and integrations | SaaS integrations holding OAuth tokens (the 2025 Salesloft Drift case), managed service providers, open-source dependencies | Model one SaaS integration and its token lifecycle |
| 10.5 Multi-tenant SaaS | Tenant isolation at data, compute, cache, queue and logging layers; noisy neighbours | Build a tenant-isolation threat checklist |

**Check your understanding:** (1) Why must CI/CD appear in a production system's threat model? (2) What new threats appear when a design moves from synchronous calls to events? (3) Where do multi-tenant systems most often leak?

### Chapter 11 · Threat modeling ML, LLM and agentic systems (week 12)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 ML threat taxonomies | NIST AI 100-2 E2025 (evasion, poisoning, privacy, misuse); MITRE ATLAS as a defender's map | Classify ten ML threats with both taxonomies |
| 11.2 LLM applications | OWASP Top 10 for LLM Applications 2025: prompt injection, sensitive information disclosure, supply chain, improper output handling, excessive agency, system prompt leakage, vector and embedding weaknesses | Model a retrieval-augmented support assistant and its data paths |
| 11.3 Agents and tools | OWASP Top 10 for Agentic Applications (ASI01 agent goal hijack to ASI10 rogue agents); the "lethal trifecta" of private data, untrusted content and an outbound channel | Find which agent designs in a provided set combine all three, and remove one leg from each |
| 11.4 MAESTRO | CSA's seven-layer reference model (foundation models to agent ecosystem) for locating threats in agent stacks | Model a multi-agent workflow with MAESTRO and STRIDE together |

**Check your understanding:** (1) Why does an LLM in the data path add a trust boundary inside a single process? (2) Which agent capability turns a disclosure threat into an integrity threat? (3) What does MAESTRO help you locate that a DFD alone does not?

### Chapter 12 · Continuous and AI-assisted threat modeling (weeks 13–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 12.1 Scaling to hundreds of teams | Risk-tiered triage, self-service templates, champions, expert review only for high-risk designs | Design the programme and its metrics for 300 teams |
| 12.2 AI tools in practice | AWS Security Agent threat modeling (preview), AWS Labs Threat Designer, STRIDE GPT, general assistants with your templates | Generate models for the same system with two tools |
| 12.3 Measuring AI output | Precision and recall against a reference model; duplicates, generic threats, missing boundaries, invented components | Score both AI models against your reference and publish the error table |
| 12.4 A human-in-the-loop workflow | AI drafts, human models the system, AI suggests threats, human ranks and decides; logging what AI added | Write your team's AI-assisted procedure with acceptance rules |

**Check your understanding:** (1) Why is recall harder to measure than precision for a threat model? (2) What should a team never delegate to an AI tool here? (3) Which metric would show the programme is working?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Manifesto critique and first session | Session notes and owned actions |
| 2 | 2 | Lab 2 · DFD repair | Corrected DFD and boundary list |
| 3 | 3 | Lab 3 · STRIDE-per-interaction (no AI) | Threat list; **P1 due** |
| 4 | 4 | Lab 4 · Attack tree | Tree with annotations |
| 5 | 5 | Lab 5 · PASTA stages 1–4 | Impact statements |
| 6 | 6 | Lab 6 · LINDDUN GO | Privacy threats mapped to DPDP |
| 7 | 7 | Rating drift experiment | Mid-term (AI off) |
| 8 | 8 | Lab 7 · Mitigations to tests | Passing security tests |
| 9 | 9 | Lab 8 · pytm in CI | CI job and report |
| 10 | 10 | Lab 9 · Event pipeline model | Model; **P2 due** |
| 11 | 10 | SaaS integration model | Token lifecycle diagram |
| 12 | 11 | Lab 10 · Agent model with MAESTRO | Model and trifecta audit |
| 13 | 12 | AI model scoring | Error table |
| 14 | 12 | Programme design | **P3 due** |
| 15 | Review | Live threat modeling exam and oral | Final exam |

## Working with AI in this course

- **Use AI for:** drafting a first DFD from a design document or Terraform plan (then correcting it); suggesting threats per element after you have built the model; deduplicating long lists; turning mitigations into test skeletons; generating pytm or Threagile boilerplate. Tools: AWS Security Agent threat modeling (preview), Threat Designer, STRIDE GPT, Claude, ChatGPT, Gemini.
- **Do without AI (drills):** the Lab 3 STRIDE-per-interaction exercise; the attack tree; every rating decision; the mid-term; the final live exam. A threat model you cannot produce yourself is one you cannot review.
- **Verify AI output by:** checking every component the AI names exists in your model; scoring precision (relevant threats ÷ all threats returned) and recall (reference threats found ÷ reference threats) against your own model; demanding a mitigation that is testable for each kept threat; checking framework identifiers (ATLAS, CAPEC, OWASP IDs) on the source site.
- **Where AI still fails here (show it):** measured STRIDE classification accuracy topped out at 72% in one study and larger models gave inconsistent gains in another (see Sources). In Lab 10 you will record, for two tools, invented components, threats on flows that do not exist, missed trust boundaries inside agent processes, and confident severity ratings with no stated method.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs 1–10 | 25% |
| Projects P1 / P2 / P3 | 5% / 15% / 25% |
| Mid-term (AI off): model and STRIDE an unseen system | 10% |
| Final: live facilitated session with an assessor playing the engineering team, plus oral defence of P3 | 20% |

**Mastery gate.** You pass when you can, without AI and in three hours: (a) model an unseen system that includes an LLM component (DFD with every trust boundary the assessor planted); (b) produce at least 20 threats across STRIDE and LINDDUN with written ratings, and the top five with testable mitigations; and (c) review a provided AI-generated threat model and find at least four of its five planted defects (missing boundary, invented component, mis-categorised threat, missing privacy threat, untestable mitigation).

## Industry reality

- Microsoft's Security Development Lifecycle has long required threat modeling at design time, and Microsoft publishes its free Threat Modeling Tool.
- OWASP maintains Threat Dragon, pytm and the Threat Modeling Cheat Sheet; AWS publishes Threat Composer and Threat Designer as open source.
- AI vendors and security agencies now expect threat models for agents: the Five Eyes guide *Careful adoption of agentic AI services* (April–May 2026) asks organisations to limit agent privileges and keep human approval for consequential steps ([CISA](https://www.cisa.gov/news-events/news/cisa-us-and-international-partners-release-guide-secure-adoption-agentic-ai)).
- In architect interview loops, a live threat-modeling session with an engineering team is a common round ([SAR market page](../../../../06_career_and_market_readiness/01_market_map/roles/SAR_security_architecture.md)).

**Interview questions from this course**

1. *"Threat-model a mobile app that links a bank account and pays merchants by QR code."* Strong answer: asks scope questions; draws the DFD with device, app backend, payment network, bank and merchant; names boundaries; covers QR tampering, device and SIM changes, session theft, collect-request fraud, partner API abuse, and repudiation; ranks with criteria; proposes testable mitigations.
2. *"STRIDE, PASTA, LINDDUN, attack trees: when do you use each?"* Strong answer: STRIDE for broad elicitation, attack trees for one high-value goal, PASTA when business impact must drive depth, LINDDUN for personal data; combines them.
3. *"How would you scale threat modeling to 300 teams?"* Strong answer: risk-tiered triggers, self-service templates, champions, models as code in pull requests, expert time reserved for high risk, and metrics such as escaped threats.
4. *"What changes when the system is an LLM agent with tools?"* Strong answer: untrusted content as instructions, trust boundary inside the model call, excessive agency, the lethal trifecta, tool permissions and approval, memory poisoning, OWASP Agentic Top 10 or MAESTRO as the frame.
5. *"An AI tool gave us 140 threats for this design. What now?"* Strong answer: check the system model first, deduplicate, discard generic threats with reasons, measure against a reference, rank with a method, convert the survivors into owned, testable mitigations, and record what the tool missed.

## Resources (free first)

- **Method:** [Threat Modeling Manifesto](https://www.threatmodelingmanifesto.org/); [OWASP Threat Modeling Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html); [Shostack + Associates free resources](https://shostack.org/resources); [Elevation of Privilege](https://github.com/adamshostack/eop); [OWASP Cornucopia](https://owasp.org/www-project-cornucopia/); [LINDDUN](https://linddun.org/).
- **Taxonomies:** [MITRE CAPEC](https://capec.mitre.org/); [MITRE ATT&CK](https://attack.mitre.org/); [MITRE ATLAS](https://atlas.mitre.org/); [NIST AI 100-2 E2025](https://csrc.nist.gov/pubs/ai/100/2/e2025/final); [OWASP Top 10 for LLM Applications](https://genai.owasp.org/llm-top-10/); [OWASP Top 10 for Agentic Applications](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/); [CSA MAESTRO](https://cloudsecurityalliance.org/blog/2025/02/06/agentic-ai-threat-modeling-framework-maestro); [CVSS v4.0](https://www.first.org/cvss/v4-0/); [OWASP Risk Rating](https://owasp.org/www-community/OWASP_Risk_Rating_Methodology).
- **Tools:** [OWASP Threat Dragon](https://owasp.org/www-project-threat-dragon/); [Microsoft Threat Modeling Tool](https://learn.microsoft.com/en-us/azure/security/develop/threat-modeling-tool); [OWASP pytm](https://github.com/OWASP/pytm); [Threagile](https://github.com/Threagile/threagile); [AWS Threat Composer](https://github.com/awslabs/threat-composer); [AWS Threat Designer](https://github.com/awslabs/threat-designer); [STRIDE GPT](https://github.com/mrwadams/stride-gpt).
- **Paid, optional:** Adam Shostack, *Threat Modeling: Designing for Security* (Wiley, 2014); Izar Tarandach and Matthew Coles, *Threat Modeling: A Practical Guide for Development Teams* (O'Reilly, 2020); Tony UcedaVélez and Marco Morana, *Risk Centric Threat Modeling* (Wiley, 2015) for PASTA. The free resources above cover the core methods.

## Sources

All checked 12 Oct 2026.

- AWS, "AWS Security Agent announces support for Threat Modeling" (17 Jun 2026) — https://aws.amazon.com/about-aws/whats-new/2026/06/aws-security-agent-threat-modeling/
- AbdulGhaffar and Matrawy, "LLMs' Suitability for Network Security: A Case Study of STRIDE Threat Modeling" (arXiv 2505.04101, 2025) — https://arxiv.org/abs/2505.04101
- Pourhanifeh, AbdulGhaffar and Matrawy, "Threat Modelling using Domain-Adapted Language Models" (arXiv 2605.10808, May 2026) — https://arxiv.org/abs/2605.10808
- Cloud Security Alliance, "Agentic AI Threat Modeling Framework: MAESTRO" (6 Feb 2025) — https://cloudsecurityalliance.org/blog/2025/02/06/agentic-ai-threat-modeling-framework-maestro
- OWASP GenAI Security Project, Top 10 for Agentic Applications (9 Dec 2025); entry names as summarised by Cycode — https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/ ; https://cycode.com/blog/owasp-top-10-agentic-applications/
- Willison, "The lethal trifecta for AI agents" (16 Jun 2025) — https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/
- CISA and partners, *Careful adoption of agentic AI services* (1 May 2026) — https://www.cisa.gov/news-events/news/cisa-us-and-international-partners-release-guide-secure-adoption-agentic-ai
- Mandiant, Salesloft Drift data theft (Aug 2025) — https://cloud.google.com/blog/topics/threat-intelligence/data-theft-salesforce-instances-via-salesloft-drift
- PIB, DPDP Rules 2025 notified (14 Nov 2025) — https://www.pib.gov.in/PressReleasePage.aspx?PRID=2190014

_Last reviewed: 2026-10_
