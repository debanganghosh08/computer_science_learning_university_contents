# SEC501 · Labs and projects

This is a seminar, so labs are short, focused workshops and the projects are intelligence and research products. All collection uses open sources, data you are licensed to use, and sensors you own (for example a honeypot in your own cloud account after ethics approval). You never interact with threat actors, enter criminal marketplaces, buy or download leaked data, or scan systems you do not own. Every project includes a methods section, an ethics statement and a data management plan, and states any AI use.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · PIR workshop | Write five priority intelligence requirements for an illustrative Indian bank and a SaaS company, each with a decision owner | PIRs and the decisions they support | 2 h |
| 2 · ACH workshop | Analysis of competing hypotheses on an attribution question from a public case | ACH matrix, key assumptions, diagnostic evidence | 3 h |
| 3 · Models in practice | Kill chain and Diamond Model activity threads for two related public incidents | Threads with sources | 3 h |
| 4 · STIX and OpenCTI | Model one public campaign as a validated STIX 2.1 bundle; load it into OpenCTI and MISP | Bundle, validation output, platform screenshots | 4 h |
| 5 · Collection and honeypot | Collection plan for one PIR; after ethics approval, run a low-interaction honeypot in your own cloud account for one week | Plan, approval, dataset summary with your analysis | 6 h |
| 6 · Pivoting | Pivot from one indicator in a public report through certificate transparency, passive DNS and hosting data; grade every link | Pivot graph with confidence per edge | 3 h |
| 7 · Pitfalls hunt | Find methodological pitfalls in a published ML-for-security paper using Arp et al.'s list | Two-page critique | 3 h |
| 8 · Reproduction | Reproduce one figure or table from a paper with released artefacts | Notebook, environment file, comparison with the original | 6 h |
| 9 · LLM extraction | Extract ATT&CK techniques from 20 public reports with a model; score against your own labels | Labels, model outputs, precision/recall, invented-technique count | 5 h |
| 10 · Peer review | Programme-committee-style reviews of two classmates' drafts | Two reviews with scores and reasons | 3 h |

## Projects

### P1 · Strategic intelligence assessment: voice phishing and help-desk social engineering against Indian financial firms (L1, ~6 hours)

**Real-world inspiration.** Mandiant's M-Trends 2026 found voice phishing rose to 11% of intrusions in 2025, second only to exploits, and warned that interactive social engineering often bypasses traditional MFA. CISA's Scattered Spider advisory (AA23-320A, updated July 2025) describes help-desk impersonation in detail. RBI's July 2026 directions tighten identity and incident reporting rules for commercial banks.

**What to build.** A four-page assessment for the board and CISO of an illustrative Indian private bank: PIRs answered, key judgements with calibrated likelihood words, graded sources, alternative hypotheses considered, indicators that would change the assessment, and recommended decisions.

**Acceptance criteria**
- Every factual statement cites a source graded for reliability and credibility; at least eight independent sources are used.
- Key judgements use a stated estimative-language scale and a confidence level, with reasons.
- At least one alternative hypothesis is analysed and the reason for rejecting or retaining it is explained.
- A reviewer outside security can state the three decisions you recommend after one reading.

**Stretch goals.** Add a short annex for the SOC with detection and help-desk procedure recommendations mapped to ATT&CK v19.

**What it proves to an employer.** You can turn public reporting into decisions for leadership, with honest uncertainty.

### P2 · Reproduce and extend a security paper (L2, ~15 hours)

**Real-world inspiration.** Pendlebury et al. (TESSERACT, USENIX Security 2019) and Arp et al. (USENIX Security 2022) showed that many machine-learning security results do not survive realistic, time-aware evaluation. CTIBench (NeurIPS 2024) and CyberSOCEval (2025) released datasets so others can test new models.

**What to build.** Choose one paper with public artefacts (for example: a time-aware re-evaluation of a malware classifier on a public feature dataset such as EMBER, or a CTIBench task re-run on newer open models). Reproduce one headline result, then extend it in one clearly stated way (newer data, a newer model, a time-aware split, or a new metric).

**Acceptance criteria**
- The reproduction matches the paper's reported number within a tolerance you state in advance, or the report explains the discrepancy with evidence.
- The extension is pre-registered in a one-paragraph plan before you run it.
- Code, environment and data references let a classmate rerun everything with one command; the classmate confirms it.
- The write-up (four to six pages) includes threats to validity and an ethics note.

**Stretch goals.** Contact the original authors with your findings in a respectful, factual note; submit to an artifact track or a student workshop.

**What it proves to an employer.** You can check other people's claims rigorously, which is the core research skill and protects organisations from adopting tools that do not work.

### P3 · Research project on an open defensive problem (L3, portfolio-grade, ~30 hours)

**Real-world inspiration.** Open problems from this seminar's sources include: vulnerability prioritisation after NIST's April 2026 decision to enrich mainly KEV-listed, federal and critical-software CVEs; intrusions whose dwell times exceed log retention (M-Trends 2026); and AI agents in the SOC that remain exposed to prompt injection (EchoLeak 2025; FRUITSHELL 2025).

**What to build.** A short research paper (8–12 pages in a target venue's format) on one question you can study legally with available data in 14 weeks. Example directions:
1. **Measurement:** how quickly do your own internet-facing honeypots see exploitation attempts for vulnerabilities after they are added to the CISA KEV catalogue (own cloud sensors, ethics approval, no interaction beyond logging)?
2. **Evaluation:** how accurately do current open models extract ATT&CK techniques and indicators from Indian and international advisories, and how often do they invent techniques?
3. **Robustness:** how often do AI triage assistants change verdicts when alerts contain instruction-like text, and which defences reduce it (lab data only)?

**Acceptance criteria**
- The paper states a research question, related work (at least 12 primary sources), method, results with uncertainty (confidence intervals or equivalent), threats to validity, ethics and a reproducibility statement.
- Data and code are released (or, where data cannot be shared, a synthetic sample and exact collection scripts), and a classmate reproduces at least one main result.
- An ethics review form is completed before data collection and is attached.
- You respond in writing to two peer reviews and revise the paper.
- A 12-minute conference-style talk with questions is delivered.

**Stretch goals.** Submit to a workshop, a student track or a practitioner venue (for example FIRST CTI, Nullcon or c0c0n); extend the work in [THS501](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md).

**What it proves to an employer.** You can create new, checked knowledge in security, which marks the move from expert practitioner to researcher, and is the path into industry research labs, CERT analysis teams and graduate study.

## Feeds into

- [RES502 Reading, Reproducing and Extending Papers](../../../../05_shared_years_3_to_5/RES502_reading_reproducing_and_extending_papers/README.md): P2 is a model for that course's reproductions.
- [THS501 Thesis or Capstone I](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md) and [THS502 Thesis or Capstone II](../../../../05_shared_years_3_to_5/THS502_thesis_or_capstone_ii/README.md): P3 is a thesis pilot.
- [LCH502 Career Launch and Founder Studio](../../../../05_shared_years_3_to_5/LCH502_career_launch_and_founder_studio/README.md): intelligence products and evaluation tooling are common security start-up ideas.
