# SEC501 · Frontier Seminar: Threat Intelligence and Security Research

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 5 · 9 | 4 (≈ 120 hours) | L4 → L5 | [SEC401](../../year_4/SEC401_detection_engineering_and_threat_hunting/README.md), [SEC403](../../year_4/SEC403_malware_analysis_for_defenders/README.md); taken alongside [RES501](../../../../05_shared_years_3_to_5/RES501_research_methods_and_scientific_writing/README.md) | [RES502](../../../../05_shared_years_3_to_5/RES502_reading_reproducing_and_extending_papers/README.md), [THS501](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md) → [THS502](../../../../05_shared_years_3_to_5/THS502_thesis_or_capstone_ii/README.md), [LCH502](../../../../05_shared_years_3_to_5/LCH502_career_launch_and_founder_studio/README.md) |

Part of the [Cybersecurity Defense major](../../README.md). A seminar: each week you read primary sources, present and critique them, and advance a research or intelligence project. Collection stays within the law and your institution's ethics rules: open sources, your own sensors and honeypots, and data you are licensed to use. You do not join criminal forums, buy stolen data, interact with threat actors, or access systems without authorisation.

## Why this course matters now

Threat intelligence is knowledge about adversaries, collected and analysed to support a decision: what to detect, what to patch, whom to warn. Security research creates new knowledge about attacks, defences and the systems in between. Both face new conditions in 2025–26. The vulnerability data pipeline is strained: in April 2026 NIST said CVE submissions grew 263% from 2020 to 2025 and moved to enriching mainly CVEs in CISA's Known Exploited Vulnerabilities catalogue, federal software and critical software; the MITRE-run CVE programme survived a funding scare in April 2025 only through a contract extension to March 2026. Adversaries changed: Mandiant's M-Trends 2026 reports access hand-offs in 22 seconds and voice phishing as the second most common initial vector; Anthropic documented an espionage campaign in which an AI agent did 80–90% of the tactical work, which MITRE ATT&CK now tracks as campaign C0062; Google tracked the first malware querying a language model in live operations. Intelligence standards matured (STIX/TAXII 2.1, TLP 2.0, ATT&CK v19 with Detection Strategies), and language models now extract techniques from reports and draft intelligence, with measurable errors (CTIBench, CyberSOCEval). The frontier needs people who can collect and analyse rigorously, state confidence honestly, design studies that hold up, and tell a real trend from a vendor narrative.

## Learning outcomes

By the end you can:

1. **Run** the intelligence lifecycle for a named consumer: write priority intelligence requirements (PIRs), collect, process, analyse, disseminate and get feedback.
2. **Apply** structured analytic techniques (analysis of competing hypotheses, key assumptions check), source grading (Admiralty system) and calibrated estimative language (ICD 203 standards).
3. **Model** intrusions with the Kill Chain, the Diamond Model and ATT&CK v19, and **pivot** from one indicator to related infrastructure using open sources.
4. **Produce and share** intelligence in STIX 2.1 over TAXII 2.1, in MISP or OpenCTI, under TLP 2.0.
5. **Critique** security papers and vendor reports for data, method and evaluation flaws (dataset artefacts, concept drift, base rates, selection bias).
6. **Design and execute** a reproducible security study with an ethics review (Menlo Report principles) and a data management plan.
7. **Evaluate** language models on intelligence tasks and **report** their error modes.
8. **Identify** open problems in defence and **write** a research proposal or intelligence assessment fit for peer review.

## Chapters and lessons

### Chapter 1 · Intelligence foundations (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 What intelligence is | Data vs information vs intelligence; strategic, operational and tactical levels; consumers and decisions | Classify ten artefacts (a hash list, a sector report, an advisory) by level and consumer |
| 1.2 The lifecycle | Direction, collection, processing, analysis, dissemination, feedback; FIRST CTI SIG curriculum | Map a real CERT-In advisory to the lifecycle |
| 1.3 Requirements | PIRs and specific intelligence requirements for an Indian bank and a SaaS company | Write five PIRs with their decision owners |
| 1.4 Intelligence in India | CERT-In advisories and vulnerability notes, sectoral CSIRTs, NCIIPC for critical information infrastructure; how Indian organisations consume and share intelligence | Compare one CERT-In advisory with the vendor report it draws on |

**Check your understanding:** Why is a feed of indicators not intelligence? Who should write PIRs? What happens to a CTI team with no feedback loop?

### Chapter 2 · Analytic tradecraft (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Cognitive bias | Heuer's *Psychology of Intelligence Analysis* (CIA, free): anchoring, confirmation, mirror-imaging | Find three biases in a published vendor report |
| 2.2 Structured techniques | Analysis of competing hypotheses, key assumptions check, devil's advocacy | Run ACH on an attribution question from a public case |
| 2.3 Sources and confidence | Admiralty grading of source reliability and information credibility; ICD 203 analytic standards and estimative language | Rewrite five vague statements into calibrated judgements |
| 2.4 Writing key judgements | Bottom line up front, separating facts from assessments, stating what would change your mind | Rewrite a long vendor blog post as five key judgements |

**Check your understanding:** Why does "possibly" mean different things to different readers? What evidence would most change your ACH result? Why grade the source and the information separately?

### Chapter 3 · Models of intrusion (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Kill chain | Hutchins, Cloppert and Amin (Lockheed Martin, 2011): intelligence-driven defence and courses of action | Apply the kill chain to the 2024 Snowflake customer intrusions |
| 3.2 Diamond Model | Caltagirone, Pendergast and Betz (2013): adversary, capability, infrastructure, victim; activity threads | Build activity threads for two related public incidents |
| 3.3 ATT&CK as a research object | v19 (April 2026): 15 tactics, 222 techniques, the Stealth/Defense Impairment split; groups, software and campaigns (for example C0062) | Analyse how the v19 split changes a published technique-frequency statistic |
| 3.4 Intelligence that imposes cost | Pyramid of Pain (Bianco, 2013): which intelligence makes adversaries change behaviour; feeding detection backlogs ([SEC401](../../year_4/SEC401_detection_engineering_and_threat_hunting/README.md)) | Rank the indicators in a public report by pyramid level and propose two behaviour detections |

**Check your understanding:** Where does the kill chain fit poorly (cloud, identity, insiders)? What does the Diamond Model add to an ATT&CK mapping? Why are ATT&CK frequency counts biased by who reports?

### Chapter 4 · Standards, platforms and sharing (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 STIX 2.1 and TAXII 2.1 | Domain objects, relationships, cyber-observables, bundles; collections and API roots | Model one public campaign as a STIX bundle and validate it |
| 4.2 Platforms | MISP and OpenCTI: ingestion, correlation, enrichment, export to detection tools | Load your bundle into OpenCTI and MISP and compare |
| 4.3 Sharing rules | TLP 2.0 (FIRST, 2022), Permissible Actions Protocol, legal limits, personal data in intelligence (DPDP Act) | Write a sharing policy for a sector group |
| 4.4 Automating intelligence flow | Feeds into SIEM and EDR, indicator expiry, false-positive feedback from the SOC | Build an expiry and feedback rule for indicators in your OpenCTI or MISP instance |

**Check your understanding:** Why separate observables from indicators in STIX? What does TLP:AMBER+STRICT allow? When can sharing an indicator harm a victim?

### Chapter 5 · Collection and pivoting (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Open sources | Vendor and government reports, CERT-In and CISA advisories, certificate transparency, passive DNS, internet scan data, malware repositories | Build a collection plan for one PIR |
| 5.2 Your own sensors | Honeypots, sinkholes, your SOC's telemetry; ethics and legal review | Deploy a low-interaction honeypot on your own cloud account and analyse a week of data |
| 5.3 Pivoting | From a domain to certificates, hosting, registration patterns and related infrastructure; confidence at each hop | Pivot from one indicator in a public report and grade every link |
| 5.4 Legal and ethical limits | IT Act, DPDP Act and terms of service; why buying leaked data or joining criminal forums is off limits for this course; protecting sources and victims | Write collection rules of engagement for a student CTI team |

**Check your understanding:** Why does each pivot lower confidence? What must an ethics review say before you run a honeypot? Which collection sources are off limits, and why?

### Chapter 6 · Attribution, geopolitics and adversary economics (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Attribution | Rid and Buchanan, "Attributing Cyber Attacks" (2015); technical, operational and strategic layers; why vendors' names for groups differ | Build a name-mapping table for three groups across vendors |
| 6.2 State and criminal ecosystems | Espionage vs ransomware economics, initial access brokers, malware-as-a-service, North Korean IT-worker schemes (M-Trends 2026: 122-day median dwell) | Write a two-page strategic assessment for an Indian board |
| 6.3 Takedowns and their effects | Emotet (2021), Operation Endgame (2024), Lumma (2025); measuring disruption | Assess one takedown's effect using public data and state your confidence |
| 6.4 India-relevant threat profiles | Building sector profiles from public reporting on attacks against Indian organisations (for example AIIMS 2022 and C-Edge 2024) | Build a threat profile for Indian co-operative banks from public sources |

**Check your understanding:** Why is attribution a judgement, not a fact? What would show a takedown worked? Why do boards need strategic, not tactical, intelligence?

### Chapter 7 · AI and adversaries (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Documented misuse | Anthropic's GTG-1002 report (Nov 2025), Google's AI Threat Tracker (Nov 2025), OpenAI's *Disrupting malicious uses of AI* reports (latest February 2026); experimental vs operational | Build an evidence table: claim, source, status, confidence |
| 7.2 Measuring capability | METR time horizons and their limits (see the [market map](../../../../06_career_and_market_readiness/01_market_map/README.md)), cyber evaluations in model system cards | Critique one AI-capability claim for method |
| 7.3 Implications for defence | Speed, scale, cost of attacks; what changes for detection and intelligence | Write a one-page forecast with explicit uncertainty |
| 7.4 Recording AI-enabled campaigns | How ATT&CK records campaigns (C0062) and software; MITRE ATLAS for attacks on AI systems; gaps in both | Map GTG-1002, as publicly described, to ATT&CK and ATLAS and list the gaps |

**Check your understanding:** Why did Mandiant say 2025 breaches were not mainly "the direct result of AI" while Anthropic documented an AI-run campaign? How would you measure AI uplift for attackers? What would falsify your forecast?

### Chapter 8 · Research methods for security (weeks 8–9)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Study types | Measurement studies, system papers, user studies, evaluations; threats to validity | Classify ten recent USENIX Security or IEEE S&P papers by type |
| 8.2 Datasets and their traps | Labelling errors and artefacts in intrusion datasets; concept drift (Pendlebury et al., TESSERACT, USENIX Security 2019); pitfalls catalogue (Arp et al., USENIX Security 2022) | Find two pitfalls in a published ML-for-security paper |
| 8.3 Ethics | Menlo Report (2012): respect for persons, beneficence, justice, respect for law and public interest; disclosure; data protection | Write an ethics section for your project |
| 8.4 Reproducibility | Artifact evaluation, code and data release, seeds, environment capture | Reproduce one figure from a paper with released artefacts |

**Check your understanding:** Why do random train/test splits overstate malware detector accuracy? What makes a measurement study ethical? Why does artifact evaluation matter for defenders who adopt research?

### Chapter 9 · Research on detection and triage (week 10)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Alert fatigue | Alahmadi et al., "99% False Positives" (USENIX Security 2022) | Design a study to measure alert quality in a SOC |
| 9.2 Provenance and correlation | NoDoze (NDSS 2019) and Tactical Provenance Analysis (IEEE S&P 2020): ranking alerts by causal context | Summarise the evaluation method and its limits |
| 9.3 LLMs for triage and intelligence | CTIBench (NeurIPS 2024), CyberSOCEval (2025), ExCyTIn-Bench (2025), Microsoft's Phishing Triage Agent RCT (2025) | Compare the four evaluation designs in a table |
| 9.4 Human factors research | Studying analyst trust in AI tools, workload and deskilling; interview and survey methods | Draft an interview protocol on AI tool trust for SOC analysts |

**Check your understanding:** What would convince a SOC to adopt a research triage method? Why are benchmark scores hard to compare across papers? What is missing from all four LLM evaluations?

### Chapter 10 · LLMs for intelligence work (week 11)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Extraction | Turning reports into ATT&CK techniques, indicators and STIX; precision and recall against human labels | Extract techniques from 20 reports with a model and score against your labels |
| 10.2 Synthesis and hallucination | Summaries, assessments, invented sources and techniques; grounding with retrieval | Count unsupported claims in model-written assessments |
| 10.3 Trust and adoption | Calibration, provenance of every claim, analyst workflow | Propose an evaluation standard for AI-assisted intelligence products |
| 10.4 Disclosing AI use | Labelling AI-assisted content, recording models and prompts, reproducibility of AI-assisted analysis | Write the AI-use disclosure for your P3 |

**Check your understanding:** Why does technique extraction look easy but score poorly on edge cases? How can retrieval reduce, but not remove, invented sources? What should every AI-assisted intelligence product disclose?

### Chapter 11 · Open problems (week 12)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Ecosystem strain | NVD enrichment backlog and the April 2026 change; CVE programme funding and governance; vulnerability volume | Propose a prioritisation research question and how to test it |
| 11.2 Hard visibility problems | Edge-device implants that survive upgrades (CISA ED 25-03), SaaS and OAuth token abuse, dwell times beyond retention | Write a problem statement with a measurable success criterion |
| 11.3 Agents as attack surface and as defenders | Prompt injection without a complete fix, agent identity and accountability, evaluation of agentic defence | Draft a threat model for an autonomous SOC agent |
| 11.4 Measuring defence | Detection coverage that reflects reality, cost-effectiveness of controls, the human factors of analysts working with AI | Pick one problem for your project and justify it |

**Check your understanding:** Which open problem matters most for India's banks, and why? What would a good metric for "detection coverage" look like? Which problem can a single student make progress on in 14 weeks?

### Chapter 12 · Writing, review and presentation (weeks 13–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 12.1 Writing | Paper structure, intelligence assessment structure, abstract and key judgements | Draft your paper or assessment |
| 12.2 Peer review | Reviewing like a programme committee: soundness, novelty, ethics, reproducibility | Write two full reviews of classmates' drafts |
| 12.3 Venues and community | USENIX Security, IEEE S&P, ACM CCS, NDSS, RAID, DFRWS, FIRST CTI, Virus Bulletin; India: Nullcon and c0c0n; preprints and responsible publication | Choose a target venue and adapt your draft to its format |
| 12.4 Responsible publication | Dual-use findings, coordinated disclosure, embargoes, removing sensitive details, ethics boards | Assess your P3 draft for dual-use risk and record your decisions |

**Check your understanding:** What makes a reviewer reject a sound result? How do you publish findings that could help attackers responsibly? Why present to practitioners as well as academics?

## Weekly rhythm

| Week | Chapter | Seminar and lab | Deliverable |
|---|---|---|---|
| 1 | 1 | PIR workshop | PIRs; project topic shortlist |
| 2 | 2 | ACH workshop | ACH matrix |
| 3 | 3 | Model application | Activity threads; **P1 due** |
| 4 | 4 | STIX/OpenCTI lab | Validated bundle |
| 5 | 5 | Collection and honeypot (ethics approval first) | Collection plan |
| 6 | 6 | Attribution debate | Strategic assessment |
| 7 | 7 | AI and adversaries panel | Evidence table; project proposal |
| 8 | 8 | Pitfalls hunt | Paper critique |
| 9 | 8 | Reproduction lab | Reproduced figure; **P2 due** |
| 10 | 9 | Triage research seminar | Study design |
| 11 | 10 | LLM extraction lab | Extraction scores |
| 12 | 11 | Open problems seminar | Problem statement |
| 13 | 12 | Peer review | Two reviews |
| 14 | 12 | Conference-style presentations | **P3 due** |
| 15 | Review | Oral examination on the reading list and P3 | Final |

## Working with AI in this course

- **Use AI for:** finding and summarising related work (then reading the papers yourself), extracting techniques and indicators for comparison with your labels, drafting STIX objects, writing analysis code, and critiquing your drafts.
- **Do without AI (drills):** ACH and source grading; your key judgements and confidence statements; peer reviews; the oral examination. An analyst who cannot reason without the model cannot detect when the model reasons badly.
- **Verify AI output by:** opening every cited source and checking the quote or number; scoring extraction against human labels; requiring a source for every claim in an intelligence product; disclosing AI use in your methods section.
- **Where AI still fails here (show it, do not assume it):** in Lab 11 you measure extraction precision and recall and count invented sources. Published evaluations (CTIBench, CyberSOCEval) show models still struggle with applied threat-intelligence reasoning, and Anthropic's own report on an AI-run intrusion describes the agent overstating and inventing findings.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Weekly reading responses and seminar leadership | 20% |
| Projects P1 / P2 / P3 | 10% / 15% / 30% |
| Peer reviews | 10% |
| Oral examination on the reading list and P3 | 15% |

**Mastery gate.** You pass when you can: (1) produce, in one working day and without AI tools, an intelligence assessment on an unseen public incident with PIR linkage, graded sources, competing hypotheses and calibrated key judgements; (2) defend a research contribution (a reproduction with a new finding, a measurement study or a new evaluation) whose data and code another student can rerun; (3) identify the main methodological flaw in an unseen security paper in a 30-minute oral.

## Industry reality

Threat intelligence analysts work at CERTs (CERT-In, sector CSIRTs), banks, technology companies, security vendors and governments; security researchers work in industry labs, universities and vendors. Senior defensive roles increasingly expect research skills: reading papers, designing evaluations of tools (especially AI tools), and publishing. Public anchors in this course: M-Trends 2026, Anthropic's GTG-1002 report and ATT&CK campaign C0062, Google's AI Threat Tracker, NIST's April 2026 NVD change, and the STIX/TAXII and TLP standards.

**Interview questions from this course**

1. *Our CEO asks if we are at risk from a group in the news. How do you answer?* Strong answer: PIR-driven; checks relevance (sector, technology, geography), the group's observed techniques against our telemetry and controls, gives a calibrated judgement, recommended actions, and what would change the assessment.
2. *How do you judge the reliability of a vendor threat report?* Strong answer: source access and incentives, evidence shown vs asserted, consistency with independent reports, confidence language, sample bias; Admiralty-style grading.
3. *What is wrong with evaluating a malware detector on a random split?* Strong answer: temporal leakage and concept drift; time-aware splits; realistic class balance; cites TESSERACT and the pitfalls literature.
4. *Would you trust an LLM to build our intelligence reports?* Strong answer: useful for extraction and drafting; measured precision and recall; invented sources; human review of every claim; disclosure; confidentiality of collection.
5. *Pick an open problem in defence and tell me how you would make progress.* Strong answer: precise problem statement, why it matters, measurable success criterion, data available legally, a feasible first study, threats to validity.

## Resources (free first)

- **Tradecraft:** [Heuer, *Psychology of Intelligence Analysis* (CIA)](https://www.cia.gov/resources/csi/books-monographs/psychology-of-intelligence-analysis-2/) · [ICD 203 Analytic Standards](https://www.dni.gov/files/documents/ICD/ICD-203.pdf) · [FIRST CTI SIG curriculum](https://www.first.org/global/sigs/cti/curriculum/)
- **Models:** [Hutchins, Cloppert and Amin (2011)](https://www.lockheedmartin.com/content/dam/lockheed-martin/rms/documents/cyber/LM-White-Paper-Intel-Driven-Defense.pdf) · [Diamond Model (2013)](https://www.activeresponse.org/wp-content/uploads/2013/07/diamond.pdf) · [MITRE ATT&CK](https://attack.mitre.org/)
- **Standards and platforms:** [STIX 2.1](https://docs.oasis-open.org/cti/stix/v2.1/stix-v2.1.html) · [TAXII 2.1](https://docs.oasis-open.org/cti/taxii/v2.1/taxii-v2.1.html) · [FIRST TLP 2.0](https://www.first.org/tlp/) · [MISP](https://www.misp-project.org/) · [OpenCTI](https://github.com/OpenCTI-Platform/opencti)
- **Research reading list (all free):** [Sommer and Paxson (IEEE S&P 2010)](https://ieeexplore.ieee.org/document/5504793) · [TESSERACT (USENIX Security 2019)](https://www.usenix.org/conference/usenixsecurity19/presentation/pendlebury) · [NoDoze (NDSS 2019)](https://www.ndss-symposium.org/ndss-paper/nodoze-combatting-threat-alert-fatigue-with-automated-provenance-triage/) · [Tactical Provenance Analysis (IEEE S&P 2020)](https://sts.cs.illinois.edu/papers/paper/TacticalProvenanceAn20200518.html) · [Arp et al. (USENIX Security 2022)](https://www.usenix.org/conference/usenixsecurity22/presentation/arp) · [Alahmadi et al. (USENIX Security 2022)](https://www.usenix.org/conference/usenixsecurity22/presentation/alahmadi) · [CTIBench (NeurIPS 2024)](https://proceedings.neurips.cc/paper_files/paper/2024/hash/5acd3c628aa1819fbf07c39ef73e7285-Abstract.html) · [CyberSOCEval (2025)](https://arxiv.org/abs/2509.20166) · [ExCyTIn-Bench (2025)](https://arxiv.org/abs/2507.14201) · [Menlo Report (2012)](https://www.dhs.gov/sites/default/files/publications/CSD-MenloPrinciplesCORE-20120803_1.pdf) · Rid and Buchanan, ["Attributing Cyber Attacks" (2015)](https://www.tandfonline.com/doi/full/10.1080/01402390.2014.977382)
- **Current threat reporting:** [M-Trends 2026](https://cloud.google.com/blog/topics/threat-intelligence/m-trends-2026) · [Verizon DBIR](https://www.verizon.com/business/resources/reports/dbir/) · [Anthropic GTG-1002 report](https://www.anthropic.com/news/disrupting-AI-espionage) · [GTIG AI Threat Tracker](https://cloud.google.com/blog/topics/threat-intelligence/threat-actor-usage-of-ai-tools) · [CERT-In advisories](https://www.cert-in.org.in/)

## Sources

All checked 12 Oct 2026.

- NIST, "NIST updates NVD operations to address record CVE growth" (15 Apr 2026) — https://www.nist.gov/news-events/news/2026/04/nist-updates-nvd-operations-address-record-cve-growth
- The Record, "CISA extends CVE program contract with MITRE" (Apr 2025) — https://therecord.media/cisa-extends-cve-program-contract-with-mitre
- Google Cloud / Mandiant, *M-Trends 2026* — https://cloud.google.com/blog/topics/threat-intelligence/m-trends-2026
- Anthropic, GTG-1002 report (13 Nov 2025) — https://www.anthropic.com/news/disrupting-AI-espionage ; MITRE ATT&CK campaign C0062 — https://attack.mitre.org/campaigns/C0062/
- Google Threat Intelligence Group, *AI Threat Tracker* (Nov 2025) — https://cloud.google.com/blog/topics/threat-intelligence/threat-actor-usage-of-ai-tools
- OpenAI, *Disrupting malicious uses of AI* (report series; latest 25 Feb 2026) — https://openai.com/index/disrupting-malicious-ai-uses
- MITRE ATT&CK, Updates April 2026 (v19) — https://attack.mitre.org/resources/updates/updates-april-2026/
- Verizon, 2026 DBIR summary page — https://www.verizon.com/business/resources/reports/dbir/
- CISA ED 25-03 (Sep 2025) — https://www.cisa.gov/news-events/directives/ed-25-03-identify-and-mitigate-potential-compromise-cisco-devices
- Microsoft, Lumma disruption (May 2025) — https://blogs.microsoft.com/on-the-issues/2025/05/21/microsoft-leads-global-action-against-favored-cybercrime-tool/ ; Europol, Operation Endgame (May 2024) — https://www.europol.europa.eu/media-press/newsroom/news/largest-ever-operation-against-botnets-hits-dropper-malware-ecosystem

_Last reviewed: 2026-10_
