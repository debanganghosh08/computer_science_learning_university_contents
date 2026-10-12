# SAR501 · Frontier Seminar: Post-Quantum Migration and Securing Autonomous Systems

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 5 · 9 | 4 (≈ 120 hours) | L4 → L5 | [SAR401](../../year_4/SAR401_cloud_security_architecture/README.md), [SAR403](../../year_4/SAR403_security_architecture_for_ai_systems_and_agents/README.md) (also recommended: [SAR304](../../year_3/SAR304_applied_cryptography_and_pki_for_architects/README.md)) | [THS501](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md), [THS502](../../../../05_shared_years_3_to_5/THS502_thesis_or_capstone_ii/README.md), [RES502](../../../../05_shared_years_3_to_5/RES502_reading_reproducing_and_extending_papers/README.md) |

Part of the [Security Architecture major](../../README.md). Taken alongside [RES501 Research Methods](../../../../05_shared_years_3_to_5/RES501_research_methods_and_scientific_writing/README.md), [RES502](../../../../05_shared_years_3_to_5/RES502_reading_reproducing_and_extending_papers/README.md) and [THS501](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md). This is a seminar: each week you read primary papers and standards, present and critique them, and run small experiments, and the semester ends with a research project written as a workshop paper. Two frontiers anchor it. The first is the migration of the world's public-key cryptography to post-quantum algorithms, which is now a programme with deadlines. The second is securing systems that act on their own, from AI agents to vehicles and industrial controllers. Confidential computing and automated reasoning connect the two. [CLD501](../../../cloud_engineering/year_5/CLD501_frontier_seminar_sovereign_cloud_confidential/README.md) covers confidential computing hardware in depth; here it is studied as an architectural trust mechanism.

## Why this course matters now

Post-quantum migration moved from research to deadlines. NIST standardised ML-KEM, ML-DSA and SLH-DSA in 2024 and its draft transition plan targets removal of quantum-vulnerable algorithms by 2035 ([NIST](https://csrc.nist.gov/projects/post-quantum-cryptography)); the UK, the EU and India's Department of Science and Technology have published migration timelines (see [SAR304](../../year_3/SAR304_applied_cryptography_and_pki_for_architects/README.md)). The estimated cost of breaking RSA-2048 keeps falling: a May 2025 paper estimated it could be factored in under a week with fewer than a million noisy qubits ([arXiv 2505.15917](https://arxiv.org/abs/2505.15917)), down from about 20 million in the same author's 2019 estimate. Nobody can give a reliable date for a cryptographically relevant quantum computer, so architects must reason under uncertainty about data that must stay secret for decades. At the same time, systems increasingly act without a human in each step. METR measured a 50% time horizon of about 12 hours for a February 2026 model on software tasks (see the [market map](../../../../06_career_and_market_readiness/01_market_map/README.md)); agents now pay, deploy and remediate; and national agencies published joint guidance on agentic AI (2026) and on AI in operational technology. DARPA's AI Cyber Challenge finalists found 77% of planted vulnerabilities and patched 61% ([DARPA](https://www.darpa.mil/news/2025/aixcc-results)). The open problems are architectural: how to give autonomous systems identities, bounded authority, verifiable behaviour and safe failure, and how to migrate cryptography across systems nobody fully inventoried. Both need people who can read the research, test claims and design what does not exist yet.

## Learning outcomes

By the end you can:

1. **Read**, **present** and **critique** primary research in applied cryptography, systems security and AI security, separating claims from evidence.
2. **Reason** about quantum-threat timelines under uncertainty with resource estimates and Mosca's inequality, and **defend** a migration priority order.
3. **Evaluate** post-quantum protocol designs (hybrid TLS, KEMTLS, Merkle tree certificates, PQ messaging protocols, hash-based firmware signatures) by measured cost and security.
4. **Design** a large-scale PQC migration programme with inventory, agility, testing and supplier strategy, grounded in current national guidance.
5. **Analyse** autonomous systems (AI agents, vehicles, OT) with threat models, control protocols and safety cases, and **design** bounded-authority architectures for them.
6. **Use** attestation and confidential computing as trust mechanisms, and **state** their limits.
7. **Apply** automated reasoning (SMT-based policy analysis, protocol verifiers) to an architectural question.
8. **Produce** an original, reproducible research contribution with an artefact, written as a workshop paper.

## Chapters and lessons

### Chapter 1 · Research in security architecture (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Reading papers | Three-pass reading; systematisation-of-knowledge (SoK) papers; threats to validity | Critique one SoK paper in one page |
| 1.2 Kinds of contribution | Measurement, design, formal analysis, empirical and user studies, systematisation | Classify ten recent papers by contribution type |
| 1.3 Ethics and law | Testing only your own systems, coordinated disclosure, dual-use results, ethics review | Write the ethics section for your project idea |
| 1.4 Reproducibility | Artefacts, environment capture, statistical reporting | Reproduce one figure from a paper's public artefact |

**Check your understanding:** (1) What makes an SoK useful rather than a literature list? (2) Which threats to validity are common in measurement papers? (3) When does a security result need coordinated disclosure?

### Chapter 2 · The quantum threat: evidence and uncertainty (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Resource estimates | How factoring and discrete-log cost estimates are built (logical vs physical qubits, error rates, run time); Gidney's 2019 and 2025 estimates | Summarise what changed between the two estimates and why |
| 2.2 Timelines | Expert surveys and their limits; why no date is reliable; harvest now, decrypt later | Write a one-page position on what an architect should assume |
| 2.3 Mosca's inequality in practice | Data shelf life + migration time vs time to threat; applying it to sectors | Apply it to health records, payment keys, firmware signing keys and state secrets |
| 2.4 Symmetric and hash security | Grover's algorithm and why AES-256 and SHA-2 remain adequate with care | Explain to a non-specialist why "quantum breaks all encryption" is wrong |

**Check your understanding:** (1) Why do falling resource estimates matter even without a date? (2) Which data types are already at risk today? (3) Why is the migration time term often underestimated?

### Chapter 3 · Migration programmes (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 National guidance compared | NIST IR 8547 (draft), NSA CNSA 2.0, UK NCSC milestones, the EU coordinated roadmap, India's DST task force report (2026) | Build a comparison table and find where they disagree |
| 3.2 Inventory at scale | CBOM generation, network and binary discovery, supplier attestations; CERT-In's BOM guidance | Evaluate two open-source discovery tools on a sample estate |
| 3.3 Crypto agility research | NIST CSWP 39; agility vs downgrade risk; algorithm negotiation | Design an agility test suite including downgrade attempts |
| 3.4 Programme design | Governance, funding, sequencing, supplier contracts, testing, success metrics | Draft the programme charter for an illustrative national payment network |

**Check your understanding:** (1) Why do national timelines differ? (2) What makes an inventory "complete enough"? (3) How can agility create vulnerabilities?

### Chapter 4 · Post-quantum protocols (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Hybrid TLS | X25519MLKEM768 deployment; packet size, middlebox and latency effects; published performance studies (for example Sikeridis et al., NDSS 2020) | Measure handshake cost on your hardware and compare with published numbers |
| 4.2 Rethinking authentication | KEMTLS (Schwabe, Stebila and Wiggers, CCS 2020); the certificate-size problem; Merkle tree certificates (IETF draft) | Estimate bytes on the wire for three authentication designs |
| 4.3 Other protocols | IKEv2 multiple key exchanges (RFC 9370), SSH hybrid key exchange, Signal's PQXDH and later post-quantum ratchet, Apple iMessage PQ3 | Compare the threat models and what each protects |
| 4.4 Open questions | PQ signatures at web scale, certificate transparency with large signatures, hybrid vs pure transitions | Write two research questions you could test |

**Check your understanding:** (1) Why is authentication harder to migrate than key exchange? (2) What does KEMTLS trade away? (3) Why did messaging apps migrate before the web's PKI?

### Chapter 5 · Constrained and long-lived systems (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Firmware and devices | Stateful hash-based signatures (LMS, XMSS; NIST SP 800-208); state management risks; secure boot chains | Sign and verify firmware with LMS in a lab and simulate state loss |
| 5.2 Implementation security | Timing and side-channel issues found in early ML-KEM implementations (for example the 2024 "KyberSlash" timing reports); constant-time engineering (study papers and advisories only) | Run a constant-time check tool on a toy implementation |
| 5.3 Verified implementations | Formally verified PQC code (for example libcrux) and what verification covers | Summarise what one verified implementation proves and assumes |
| 5.4 Long-lived infrastructure | Payment terminals, smart cards, satellites, industrial controllers; replace-or-wrap decisions | Write a migration decision for a fleet that cannot be updated |

**Check your understanding:** (1) Why is state loss dangerous for LMS and XMSS? (2) What does "formally verified" not guarantee? (3) When is wrapping a legacy system the only option?

### Chapter 6 · Securing autonomous AI agents: foundations (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Autonomy as a threat-model variable | Longer horizons, more tools, less supervision; OWASP Agentic Top 10 (goal hijack, rogue agents, cascading failures) | Threat-model the same task at three autonomy levels |
| 6.2 AI control | Protocols that stay safe even if the model is untrustworthy: trusted monitoring, editing and auditing (Greenblatt et al., 2023) | Design a control protocol for a deployment agent |
| 6.3 Capability-based designs | CaMeL and the design-pattern catalogue revisited; capability security's older history | Compare CaMeL's capabilities with classic object-capability systems |
| 6.4 Measuring defences | AgentDojo-style benchmarks; adaptive evaluation; what benchmark numbers do not show | Critique one agent-security evaluation's methodology |

**Check your understanding:** (1) Why does a control protocol assume the model may be adversarial? (2) What do capability systems offer that access-control lists do not? (3) Why can a defence look strong on a static benchmark and fail in deployment?

### Chapter 7 · Autonomous agents in production (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Accountability | Agent identity, delegation chains, signed action records, audit that survives disputes | Design a signed, verifiable action log for agent transactions |
| 7.2 Agents that pay | Agent payment protocols (for example Google's Agent Payments Protocol, AP2) and published security analyses of them | Present one analysis and its open issues |
| 7.3 Agent-to-agent protocols | Inter-agent communication standards, discovery and trust; where authentication and authorization sit | Map trust boundaries in a multi-agent protocol |
| 7.4 Safety cases | Structured arguments that an AI system is safe enough to deploy (Clymer et al., 2024); evidence from evaluations and control | Write a safety case outline for an agent with spending authority |

**Check your understanding:** (1) What makes an agent's action record usable in a dispute? (2) Where do agent payment protocols put the user's consent? (3) What evidence would make a safety case convincing?

### Chapter 8 · Cyber-physical autonomy (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Vehicles | UNECE Regulation No. 155 (cyber security management systems), ISO/SAE 21434, UL 4600 for autonomous products | Map a vehicle's update path to R155 and ISO/SAE 21434 activities |
| 8.2 Industrial and OT systems | IEC 62443 zones and conduits; joint agency principles for integrating AI into operational technology (2025) | Design where an AI advisor may and may not act in a water plant (illustrative) |
| 8.3 Drones and robots | Command-link security, geofencing, fail-safe behaviour | Write fail-safe requirements for a delivery drone fleet (illustrative) |
| 8.4 Long-lived safety-critical devices | Connected medical and industrial devices with decade-long lifetimes; patchability, end-of-support and decommissioning | Write the update and decommissioning plan for an illustrative infusion-pump fleet |

**Check your understanding:** (1) Why is "fail-safe" different from "fail-secure" in physical systems? (2) What must never be delegated to an AI in OT? (3) How do safety and security standards interact?

### Chapter 9 · Confidential computing and verifiable trust (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Attestation architecture | IETF RATS (RFC 9334): attesters, verifiers, relying parties; evidence and endorsements | Draw the attestation flow for a confidential inference service |
| 9.2 Attestation-gated keys | Releasing keys only to measured workloads; policy design; failure modes | Gate a key release on a confidential VM's attestation in a lab |
| 9.3 Verifiable AI privacy | Apple Private Cloud Compute (2024) as a design for verifiable server-side privacy; confidential GPUs | Critique PCC's claims and what an outsider can verify |
| 9.4 Limits | Side channels, supply chain of the TEE itself, operator trust that remains | List assumptions an auditor must accept |

**Check your understanding:** (1) What does attestation prove, and to whom? (2) Why must key release policies handle firmware updates? (3) What trust remains in the hardware vendor?

### Chapter 10 · Autonomous defence (week 10)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 AI vulnerability discovery and repair | DARPA AIxCC results; Google's Big Sleep; what AI-found bugs mean for patch pipelines | Read the AIxCC results and estimate effects on a patch SLA |
| 10.2 Autonomous security operations | Agents that triage, contain and remediate; bounded authority and approval | Design the authority model for a containment agent |
| 10.3 Governing defenders | Avoiding self-inflicted outages, audit, reversibility; joint agency statements on AI and cyber risk | Write a policy for autonomous containment actions |
| 10.4 Measuring autonomous defenders | Contest results vs production conditions, false-positive cost, human review load | Design an evaluation for a containment agent using incidents from your own lab |

**Check your understanding:** (1) Why can autonomous containment be more dangerous than the threat? (2) What changes in vulnerability management when discovery is cheap? (3) Which defender actions must be reversible?

### Chapter 11 · Automated reasoning for architecture (week 11)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Policy analysis with SMT | AWS's Zelkova approach (Backes et al., FMCAD 2018) behind IAM Access Analyzer; Cedar's analysable design (OOPSLA 2024) | Encode three access policies in Z3 and prove or refute a property |
| 11.2 Protocol verification | Tamarin and ProVerif; the role of formal analysis in TLS 1.3's design | Model a toy key-exchange protocol in Tamarin and find the planted flaw |
| 11.3 Specification of systems | TLA+ for distributed security mechanisms (revocation, key rotation) | Model a key-rotation protocol in TLA+ and check an invariant |
| 11.4 Choosing a method | When to test, when to model-check, when to prove; cost, expertise and integrating checks into CI | Write a one-page method choice for your project question |

**Check your understanding:** (1) What can an SMT-based policy check prove that tests cannot? (2) Why did TLS 1.3 benefit from formal analysis during design? (3) What does a model checker miss?

### Chapter 12 · Research project (weeks 12–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 12.1 Proposal | Research question, method, threats to validity, ethics | Two-page proposal, reviewed by peers |
| 12.2 Experiments and analysis | Running, measuring, statistics, negative results | Weekly progress notes with data |
| 12.3 Writing and presenting | Workshop-paper structure, figures, related work, artefact appendix; 15-minute talk | Paper draft, peer review, final talk |
| 12.4 Peer review | Reviewing papers constructively; responding to reviewers | Write two structured reviews and a response to the reviews you receive |

**Check your understanding:** (1) Is your result reproducible from your artefact alone? (2) What would make a reviewer reject your paper? (3) What is the smallest claim your evidence supports?

## Weekly rhythm

| Week | Chapter | Seminar and lab | Deliverable |
|---|---|---|---|
| 1 | 1 | SoK critique; figure reproduction | Critique |
| 2 | 2 | Resource estimates and Mosca workshop | Position paper; **P1 starts** |
| 3 | 3 | Guidance comparison; inventory tools | Comparison table |
| 4 | 4 | Lab 1 · Hybrid TLS measurement | Measurements; **P1 due** |
| 5 | 5 | Lab 2 · LMS firmware signing and state loss | Lab report |
| 6 | 6 | Lab 3 · Control protocol design | Protocol |
| 7 | 7 | Agent payments and safety cases seminar | Safety case outline; **P2 due** |
| 8 | 8 | Cyber-physical seminar | Requirements set |
| 9 | 9 | Lab 4 · Attestation-gated key release | Working gate |
| 10 | 10 | Autonomous defence seminar | Policy |
| 11 | 11 | Lab 5 · Z3, Tamarin or TLA+ | Proof or counterexample |
| 12 | 12 | Project | Data and draft |
| 13 | 12 | Peer review | Reviews given and received |
| 14 | 12 | Presentations | **P3 due** |
| 15 | Review | Oral examination | Final |

## Working with AI in this course

- **Use AI for:** first-pass summaries of long papers (then read the paper); finding related work (then check every citation exists); writing measurement scripts and plotting code; drafting formal models that you then verify; translating between notations.
- **Do without AI (drills):** paper critiques in seminar; Mosca analyses; the threat models in Chapters 6–8; the oral examination.
- **Verify AI output by:** checking every citation's title, authors, venue and year at the source (arXiv, ACM, IEEE, IETF, NIST); re-running scripts on fresh data; having a formal tool, not the AI, decide whether a property holds; recording which summaries misstated a paper's claims.
- **Where AI still fails here (show it):** ask an assistant for "recent papers on post-quantum certificate transparency" and record how many citations are invented or misattributed; ask for the current status of FIPS 206 and NIST IR 8547 and compare with NIST's pages; ask it to judge whether a Tamarin model is correct and compare with the tool's result.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Seminar presentations and critiques | 20% |
| Labs 1–5 | 15% |
| P1 / P2 | 10% / 15% |
| P3 research paper and artefact | 30% |
| Oral examination | 10% |

**Mastery gate.** You pass when you can: (a) present an unseen research paper in this area in 15 minutes and identify its main contribution, its strongest assumption and one threat to validity; (b) produce a research artefact that a peer can run from your instructions to reproduce your main figure; and (c) defend, in an oral examination without AI, a PQC migration priority order and an autonomy boundary for an agent, each grounded in cited evidence.

## Industry reality

- Banks, payment networks, telecoms and governments are staffing PQC migration programmes now, driven by NIST, NSA, NCSC, EU and Indian guidance; vendors ship hybrid key exchange by default in browsers and major libraries.
- Messaging providers (Signal, Apple) deployed post-quantum protocols before the web PKI, showing what migration looks like in practice.
- AI agent platforms, agent payment protocols and agentic security guidance are being designed now, with few established patterns; architects who can read the research and design bounded autonomy are rare.
- Automotive (UNECE R155) and OT standards already demand cybersecurity management for autonomous and connected systems.

**Interview questions from this course**

1. *"How would you decide what to migrate to post-quantum cryptography first?"* Strong answer: data shelf life and Mosca's inequality, exposure to capture, replaceability, supplier dependencies, hybrid key exchange first, authentication later, cited national timelines.
2. *"What is the hardest unsolved problem in PQ migration for the web?"* Strong answer: authentication and certificate size, CT and chain sizes, constrained clients, proposals such as KEMTLS and Merkle tree certificates, and measured costs.
3. *"How would you bound the authority of an autonomous agent that can spend money?"* Strong answer: separate identity, mandates with limits, signed and verifiable action records, approval thresholds, control protocols that assume the model can be wrong, kill switch, safety case with evidence.
4. *"What does remote attestation give you in a confidential AI service, and what doesn't it?"* Strong answer: proof of measured code to a verifier, key release on policy; not protection from side channels, bugs in the measured code or hardware vendor trust.
5. *"Tell me about a research result you reproduced and what you learned."* Strong answer: the claim, setup differences, numbers obtained, discrepancies explained, what it means for practice.

## Research reading list

Start here; each week adds papers chosen by the seminar.

- **Foundations:** Saltzer and Schroeder, [The Protection of Information in Computer Systems](https://web.mit.edu/Saltzer/www/publications/protection/) (1975); Thompson, [Reflections on Trusting Trust](https://dl.acm.org/doi/10.1145/358198.358210) (1984); Ward and Beyer, [BeyondCorp](https://research.google/pubs/beyondcorp-a-new-approach-to-enterprise-security/) (2014); Pang et al., [Zanzibar](https://www.usenix.org/conference/atc19/presentation/pang) (2019).
- **Quantum and PQC:** Mosca, [Cybersecurity in an era with quantum computers: will we be ready?](https://eprint.iacr.org/2015/1075) (2015); Gidney, [How to factor 2048 bit RSA integers with less than a million noisy qubits](https://arxiv.org/abs/2505.15917) (2025); Bernstein and Lange, [Post-quantum cryptography](https://www.nature.com/articles/nature23461) (Nature, 2017); Schwabe, Stebila and Wiggers, [Post-Quantum TLS Without Handshake Signatures](https://eprint.iacr.org/2020/534) (CCS 2020); Ott et al., [Identifying Research Challenges in Post Quantum Cryptography Migration and Cryptographic Agility](https://arxiv.org/abs/1909.07353) (2019); NIST [FIPS 203](https://csrc.nist.gov/pubs/fips/203/final), [SP 800-208](https://csrc.nist.gov/pubs/sp/800/208/final), [CSWP 39](https://www.nist.gov/news-events/news/2025/12/nist-publishes-cswp-39-considerations-achieving-crypto-agility); IETF [RFC 9370](https://www.rfc-editor.org/rfc/rfc9370).
- **Autonomous AI security:** Debenedetti et al., [CaMeL](https://arxiv.org/abs/2503.18813) (2025); Beurer-Kellner et al., [Design Patterns for Securing LLM Agents](https://arxiv.org/abs/2506.08837) (2025); Debenedetti et al., [AgentDojo](https://arxiv.org/abs/2406.13352) (2024); Greenblatt et al., [AI Control](https://arxiv.org/abs/2312.06942) (2023); Clymer et al., [Safety Cases](https://arxiv.org/abs/2403.10462) (2024); [Beyond the Mandate: A Systematic Security Analysis of AP2](https://arxiv.org/abs/2608.23858) (2026); CISA and partners, [Careful adoption of agentic AI services](https://www.cisa.gov/news-events/news/cisa-us-and-international-partners-release-guide-secure-adoption-agentic-ai) (2026).
- **Trust and verification:** IETF [RFC 9334 (RATS)](https://www.rfc-editor.org/rfc/rfc9334); Apple, [Private Cloud Compute](https://security.apple.com/blog/private-cloud-compute/) (2024); Backes et al., [Semantic-based Automated Reasoning for AWS Access Policies using SMT](https://www.amazon.science/publications/semantic-based-automated-reasoning-for-aws-access-policies-using-smt) (FMCAD 2018); [Tamarin prover](https://tamarin-prover.com/); [TLA+](https://lamport.azurewebsites.net/tla/tla.html).
- **Autonomous defence:** [DARPA AIxCC results](https://www.darpa.mil/news/2025/aixcc-results) (2025); Google Project Zero, [From Naptime to Big Sleep](https://googleprojectzero.blogspot.com/2024/10/from-naptime-to-big-sleep.html) (2024).

## Resources (free first)

- **Guidance:** [NIST PQC project](https://csrc.nist.gov/projects/post-quantum-cryptography); [UK NCSC PQC timelines](https://www.ncsc.gov.uk/guidance/pqc-migration-timelines); [EU PQC policy](https://digital-strategy.ec.europa.eu/en/policies/post-quantum-cryptography); [DST quantum-safe ecosystem report](https://dst.gov.in/sites/default/files/Quantum-Safe-Ecosystem-in-India.pdf); [OWASP Agentic Top 10](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/).
- **Tools:** [Open Quantum Safe](https://openquantumsafe.org/); [Z3](https://github.com/Z3Prover/z3); [Tamarin](https://tamarin-prover.com/); [TLA+ tools](https://github.com/tlaplus/tlaplus); [Confidential Computing Consortium](https://confidentialcomputing.io/).
- **Venues to follow:** IEEE S&P, USENIX Security, ACM CCS, NDSS, Real World Crypto, IACR ePrint, arXiv cs.CR.

## Sources

All checked 12 Oct 2026.

- NIST PQC project page (updated 5 Aug 2026) — https://csrc.nist.gov/projects/post-quantum-cryptography
- Gidney, *How to factor 2048 bit RSA integers with less than a million noisy qubits* (arXiv 2505.15917, May 2025); earlier 20-million-qubit estimate: Gidney and Ekerå (arXiv 1905.09749, 2019) — https://arxiv.org/abs/2505.15917 ; https://arxiv.org/abs/1905.09749
- METR time horizons, as reported in this curriculum's [market map](../../../../06_career_and_market_readiness/01_market_map/README.md) — https://metr.org/time-horizons/
- DARPA AIxCC results (Aug 2025): 77% found, 61% patched — https://www.darpa.mil/news/2025/aixcc-results
- CISA and partners, *Careful adoption of agentic AI services* (1 May 2026) — https://www.cisa.gov/news-events/news/cisa-us-and-international-partners-release-guide-secure-adoption-agentic-ai ; NSA and partners on integrating AI in operational technology — https://www.nsa.gov/Press-Room/Press-Releases-Statements/Press-Release-View/Article/4347041/nsa-cisa-and-others-release-guidance-on-integrating-ai-in-operational-technology/
- AP2 security analysis (arXiv 2608.23858, 2026) — https://arxiv.org/abs/2608.23858
- India DST task force report (Feb 2026) — https://dst.gov.in/sites/default/files/Report_TaskForce_PQMigration_4Feb26%20%28v1%29.pdf

_Last reviewed: 2026-10_
