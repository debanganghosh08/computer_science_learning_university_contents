# SEC401 · Detection Engineering and Threat Hunting

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 4 · 7 | 4 (≈ 120 hours) | L3 → L4 | [SEC301](../../year_3/SEC301_network_security_and_defense/README.md) (and [SEC302](../../year_3/SEC302_security_operations_soc_siem_and_monitoring/README.md), [SEC304](../../year_3/SEC304_endpoint_and_operating_system_security/README.md) strongly recommended) | [SEC501](../../year_5/SEC501_frontier_seminar_threat_intelligence/README.md), [SEC404](../SEC404_ai_in_security_operations/README.md), [THS501](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md) |

Part of the [Cybersecurity Defense major](../../README.md). Detections are validated by emulating adversary behaviour **only in your own isolated lab or an authorised purple-team exercise with written scope** ([OFF401](../../../ethical_hacking_offensive_security/year_4/OFF401_red_teaming_adversary_emulation_and_purple/README.md) covers the offensive side). This course describes validation tools and methods conceptually and never gives attack procedures.

## Why this course matters now

Detection engineering is the practice of building, testing and maintaining the rules and analytics that turn logs into alerts, treated as software: written as code, reviewed, tested and versioned. Threat hunting is the proactive search for attackers that existing detections missed, starting from a hypothesis. Both are changing quickly. MITRE ATT&CK, the shared map of attacker behaviour, replaced its per-technique detection notes with "Detection Strategies" and "Analytics" in v18 (October 2025), and in v19 (April 2026) split Defense Evasion into two tactics, Stealth and Defense Impairment, so rule libraries and coverage maps need updating. Attackers move faster: Mandiant measured access hand-offs between criminal groups in 22 seconds in 2025, and found median dwell times of 122 days for espionage and North Korean IT-worker cases. Living-off-the-land activity defeats signature matching, so detections must target behaviour. AI now drafts Sigma rules and queries in seconds (Microsoft Security Copilot, Google SecOps, Elastic AI Assistant, general models), and vendors are shipping agentic hunting features. What makes a detection engineer hard to replace is knowing *which* behaviour to detect, proving a rule fires on the real thing and stays quiet on normal activity, and keeping hundreds of rules healthy as data sources change.

## Learning outcomes

By the end you can:

1. **Run** the detection lifecycle (requirement, research, build, test, deploy, tune, retire) and **document** each rule with the Alerting and Detection Strategies (ADS) framework.
2. **Assess** data-source coverage against ATT&CK data components and **close** the most important gaps.
3. **Write** portable detections in Sigma (specification 2.x, including correlation rules and filters) and **convert** them with pySigma/sigma-cli to at least two SIEM languages.
4. **Build** a detection-as-code pipeline: Git, peer review, unit tests with recorded events, CI validation and automated deployment.
5. **Validate** detections against emulated behaviour in an isolated lab and **record** expected vs observed telemetry.
6. **Tune** detections with measured precision and alert volume, and **choose** robust detection logic using the Pyramid of Pain and CTID's Summiting the Pyramid.
7. **Plan, run and document** hypothesis-driven hunts with the PEAK or TaHiTI framework, and **convert** findings into detections.
8. **Measure** detection coverage and health honestly, and **verify** AI-generated rules before deployment.

## Chapters and lessons

### Chapter 1 · Detection engineering as a discipline (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 What a detection is | Signal, logic, context, response; alert vs hunt query vs dashboard | Classify 20 items from a SIEM export |
| 1.2 The lifecycle | Requirement from threat model or intelligence, research, build, test, deploy, tune, retire | Map one existing rule through every stage and find the gaps |
| 1.3 ADS framework | Goal, categorisation, strategy abstract, technical context, blind spots, false positives, validation, priority, response (Palantir) | Write a full ADS for a rule you wrote in SEC302 |
| 1.4 ATT&CK as the shared map | v18 Detection Strategies and Analytics; v19 split of Defense Evasion into Stealth (TA0005) and Defense Impairment (TA0112); ATT&CK Navigator | Update ten rule mappings to v19 |

**Check your understanding:** Why should a detection document its blind spots? What breaks when ATT&CK splits a tactic? Why is "map everything to ATT&CK" not a detection strategy?

### Chapter 2 · Telemetry and data engineering for detection (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Data components | Which ATT&CK data components (process creation, command execution, logon session, network traffic flow, cloud API calls) each technique needs | For 15 techniques, list the data components and your lab sources |
| 2.2 Coverage of data | DeTT&CT for data-source quality scoring | Score your lab's data sources with DeTT&CT |
| 2.3 Schemas and fields | ECS, OCSF, ASIM, Sigma taxonomy; field-mapping pipelines | Write a pySigma processing pipeline for one custom log source |
| 2.4 Data health | Volume baselines, parsing failures, schema drift, agent coverage | Build alerts for a 50% volume drop per source |

**Check your understanding:** Why is a rule on a source that silently stopped worse than no rule? What does a schema change do to 300 detections? Which data component gives the most coverage per byte in a Windows estate?

### Chapter 3 · Writing detections in Sigma and native languages (weeks 3–4)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Sigma rules | `logsource`, `detection` selections and conditions, modifiers (`contains`, `endswith`, `re`, `cidr`), `falsepositives`, `level`, tags | Write 10 Sigma rules for behaviours you can generate in your lab |
| 3.2 Correlation and filters | Sigma 2.x correlation rules (event count, value count, temporal) and global filters | Express "many failures then success" as a correlation rule |
| 3.3 Conversion | pySigma backends and pipelines, sigma-cli; what does not convert cleanly | Convert your rules to KQL and SPL or ES\|QL and diff the semantics |
| 3.4 Native analytics | When to write in KQL/SPL/ES\|QL directly (joins, statistics, enrichment), Elastic and Splunk open rule repositories as references | Re-implement two SigmaHQ rules natively with an improvement |
| 3.5 Other detection layers | Suricata for network, YARA for files ([SEC403](../SEC403_malware_analysis_for_defenders/README.md)), cloud-native rules | Pick the right layer for eight behaviours and justify |

**Check your understanding:** Why does Sigma need processing pipelines? When is a correlation rule better than a single-event rule? Which behaviours cannot be expressed in Sigma at all?

### Chapter 4 · Detection as code (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Repository design | One rule per file, metadata, owners, status (experimental, test, stable, deprecated) | Structure a repository for 50 rules |
| 4.2 Tests | Unit tests with recorded positive and negative events (OTRF Security-Datasets, your lab logs), schema validation, linting | Write tests that fail when a field name changes |
| 4.3 CI/CD | GitHub Actions or GitLab CI: lint, convert, test, deploy via SIEM API; rollback | Build the pipeline end to end |
| 4.4 Review | Peer review checklists, change records, emergency changes | Review three classmates' pull requests with the checklist |

**Check your understanding:** What does a negative test prove that a positive test does not? Why should deployment be automated but approval not? How do you roll back a detection that floods the queue?

### Chapter 5 · Validating detections in a lab (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Why validate | Rules that never fired; rules that cannot fire because data is missing | Find three "dead" rules in a provided library |
| 5.2 Emulation tools (concepts) | Atomic Red Team test library, MITRE Caldera, breach-and-attack simulation products; authorisation, isolation, clean-up | Write the authorisation and isolation plan for your lab validation |
| 5.3 Expected vs observed telemetry | Recording what each test should produce; comparing with SIEM results; Summiting the Pyramid's robustness levels | Validate 10 of your rules and record results |
| 5.4 Purple teaming | Working with authorised red teams; feedback loops; reporting gaps ([OFF401](../../../ethical_hacking_offensive_security/year_4/OFF401_red_teaming_adversary_emulation_and_purple/README.md)) | Run a 2-hour lab purple exercise with a classmate under written scope |

**Check your understanding:** Why can a passing emulation test still overstate protection? What must be agreed in writing before any purple-team exercise? Why validate after every log-pipeline change?

### Chapter 6 · Tuning and robustness (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Measuring quality | Precision, recall, alert volume per day, analyst time per alert; base-rate effects | Compute precision for five rules from labelled alerts |
| 6.2 Tuning without blinding | Narrow logic vs allow-lists; allow-lists with owners and expiry; risk-based alerting | Tune two noisy rules and prove the test cases still fire |
| 6.3 Robust logic | Pyramid of Pain (Bianco, 2013): hashes and IPs vs tools and behaviours; Summiting the Pyramid: detections attackers cannot easily evade | Rewrite a hash-based rule as a behaviour-based rule |
| 6.4 Alert budgets | Capacity planning: alerts per analyst per shift; retiring low-value rules | Set an alert budget for a 6-analyst SOC and fit your rule set to it |

**Check your understanding:** Why does an allow-list without expiry become a backdoor? Why is a behaviour detection more expensive to build but cheaper to maintain? How does base rate affect what "99% accurate" means?

### Chapter 7 · Behavioural and statistical detection (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Baselines | First-seen, rare-in-environment, peer-group comparison, time-of-day | Build a "first time this user ran this admin tool" analytic |
| 7.2 Stacking and long-tail analysis | Count by value across hosts; the rare tail as a lead, not a verdict | Stack scheduled tasks across 50 lab hosts (simulated) |
| 7.3 Machine learning pitfalls | Sommer and Paxson (2010) on why ML struggles in intrusion detection; Arp et al. (USENIX Security 2022) on dataset and evaluation pitfalls | Critique one vendor's "AI detection" claim using these papers |
| 7.4 UEBA | User and entity behaviour analytics, risk scoring, explainability | Explain three UEBA alerts from documentation and list their blind spots |

**Check your understanding:** Why is an anomaly not an attack? What evaluation mistake makes many ML detection papers look better than they are? When would you choose a simple threshold over a model?

### Chapter 8 · Threat hunting foundations (weeks 9–10)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 What hunting is | Hypothesis-driven, baseline (exploratory) and model-assisted hunting; PEAK framework (Splunk, 2023); TaHiTI (Dutch financial sector) | Write three hypotheses from three different sources (intelligence, ATT&CK, a recent incident) |
| 8.2 Planning a hunt | Scope, data needed, time window, success criteria, stop conditions | Write a hunt plan for one hypothesis |
| 8.3 Executing | Pivoting, stacking, visualisation, notebooks (Jupyter with SIEM APIs) | Execute the plan on OTRF datasets or a CyberDefenders threat-hunting lab |
| 8.4 Outcomes | Found something → incident; found nothing → document coverage; always → new detections or data requests | Write the hunt report and one new detection |

**Check your understanding:** Why is "found nothing" still a useful hunt result? What makes a hypothesis testable? When should a hunt stop?

### Chapter 9 · Hunting across identity, endpoint, network and cloud (weeks 10–11)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Identity hunts | New OAuth grants, token use from new networks, MFA method changes, Kerberos anomalies ([SEC303](../../year_3/SEC303_identity_and_access_management/README.md)) | Hunt for risky consents in a sample tenant export |
| 9.2 Endpoint hunts | Rare parent-child pairs, built-in tools in unusual contexts, persistence created outside change windows | Stack parent-child pairs across a dataset |
| 9.3 Network hunts | Beacon-like timing, rare destinations, long connections, DNS anomalies ([SEC301](../../year_3/SEC301_network_security_and_defense/README.md)) | Hunt beaconing in Zeek logs |
| 9.4 Cloud and SaaS hunts | Unusual API calls, new access keys, mass exports, disabled logging; the Salesloft Drift case (2025) | Hunt a CloudTrail dataset for key misuse |

**Check your understanding:** Which hunt type has the best yield in a SaaS-first company, and why? What benign activity looks most like beaconing? Why hunt in identity logs even when endpoints are clean?

### Chapter 10 · Coverage, metrics and programme management (week 12)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Coverage honestly | ATT&CK heatmaps and their traps (one weak rule turns a cell green); coverage × validation × robustness | Re-score a provided heatmap with validation evidence |
| 10.2 Threat-informed prioritisation | MITRE Center for Threat-Informed Defense resources, sector threat profiles, top techniques from your own incidents | Build a prioritised detection backlog of 20 items |
| 10.3 Detection health | Silent failures, last-fired dates, test pass rates, mean time to fix broken rules | Build a detection health dashboard |
| 10.4 Team practice | Intake from SOC and intelligence, SLAs, documentation, on-call for broken rules | Write a one-page detection engineering charter |

**Check your understanding:** Why is "percent of ATT&CK covered" misleading? What should a detection backlog be sorted by? Which health metric would reveal a broken log pipeline first?

### Chapter 11 · AI-assisted detection engineering and hunting (weeks 13–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 AI drafting | Generating Sigma, KQL and SPL from descriptions; converting between languages; explaining legacy rules | Generate 10 rules with an assistant and test each with your harness |
| 11.2 Failure modes | Invented fields and log sources, wrong event IDs, overly broad conditions, rules that cannot fire, outdated ATT&CK IDs | Classify every error from 11.1 |
| 11.3 Agentic hunting | Vendor agents that propose and run hunts; read-only permissions, logging and review | Design guardrails for a hunting agent with SIEM access |
| 11.4 Grounding | Giving the model your schema, examples and tests; retrieval over your rule library | Measure how schema context changes the pass rate of AI-drafted rules |

**Check your understanding:** Why does schema context reduce invented fields? What must an AI-drafted rule pass before review? Why should a hunting agent never have write access to the SIEM?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · ADS and ATT&CK v19 mapping | ADS document |
| 2 | 2 | Lab 2 · Data-source scoring | DeTT&CT scores, pipeline |
| 3 | 3 | Lab 3 · Sigma rules | 10 rules |
| 4 | 3 | Lab 3 (cont.) · Conversion and correlation | Converted rules; **P1 due** |
| 5 | 4 | Lab 4 · Detection-as-code pipeline | Working CI |
| 6 | 5 | Lab 5 · Lab validation | Validation records |
| 7 | 6 | Lab 6 · Tuning | Precision before/after; mid-term (AI off) |
| 8 | 7 | Lab 7 · Behavioural analytics | First-seen analytic |
| 9 | 8 | Lab 8 · Hunt plan | Plan |
| 10 | 8–9 | Lab 8 (cont.) · Hunt execution | Hunt report; **P2 due** |
| 11 | 9 | Lab 9 · Cross-domain hunts | Two hunt reports |
| 12 | 10 | Lab 10 · Coverage and health | Dashboard, backlog |
| 13 | 11 | AI drafting study | Error classification |
| 14 | 11 | P3 demos | **P3 due** |
| 15 | Review | Practical exam and oral defence of P3 | Final exam |

## Working with AI in this course

- **Use AI for:** drafting Sigma and native rules from a behaviour description; converting rules; writing test harness code and CI; summarising intelligence reports into hunt hypotheses; explaining an unfamiliar rule. Security Copilot, Google SecOps, Elastic AI Assistant, Claude, ChatGPT and Gemini all do this; Claude Code or GitHub Copilot can build the pipeline.
- **Do without AI (drills):** the first 10 Sigma rules; writing hunt hypotheses and plans; precision calculations; ADS documents for your P3 rules; the mid-term and final.
- **Verify AI output by:** running every AI-drafted rule through your test harness with positive and negative events; checking field names against your schema; checking ATT&CK IDs against v19; requiring an ADS with blind spots before merge.
- **Where AI still fails here (show it, do not assume it):** Lab 11 asks you to measure it yourself. Record the pass rate of AI-drafted rules on your tests with and without schema context, and the error types. ExCyTIn-Bench (2025) shows even the best model scoring 0.606 on multi-step investigation tasks, which is a reminder that hunting conclusions need human review.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs 1–10 | 25% |
| Projects P1 / P2 / P3 | 5% / 15% / 20% |
| Mid-term (AI off) | 10% |
| Final practical (AI off) + oral defence of P3 | 25% |

**Mastery gate.** You pass when you can, without AI tools and in four hours: (1) given a written intelligence report and a lab dataset, write three behaviour-based Sigma rules with tests that pass on positive events and stay silent on a day of baseline data; (2) plan and run one hypothesis-driven hunt on an unseen dataset and produce a report with at least one new detection or a documented visibility gap; (3) review a 20-rule pull request and find the planted defects (wrong fields, dead logic, over-broad allow-lists).

## Industry reality

Detection engineers and threat hunters are senior SOC roles (see the [SEC market page](../../../../06_career_and_market_readiness/01_market_map/roles/SEC_cybersecurity_defense.md)); "detection engineering as software engineering" is listed there as growing in value. Public anchors: SigmaHQ's open rule repository, Elastic's and Splunk's open detection repositories, MITRE ATT&CK v19 and its Detection Strategies, MITRE CTID's Summiting the Pyramid, and the Dutch financial sector's TaHiTI hunting methodology.

**Interview questions from this course**

1. *Walk me through how you would build a detection for a new technique from an intelligence report.* Strong answer: extract behaviour not indicators, check data availability, write logic and ADS, create positive and negative test events, validate in a lab, deploy as experimental, measure precision, promote.
2. *How do you know your detections work?* Strong answer: tests in CI, lab validation after pipeline changes, last-fired and health monitoring, purple-team results, precision tracking; admits heatmaps overstate coverage.
3. *Your rule fires 500 times a day. Tune it without losing the real attack.* Strong answer: analyse what fires, narrow logic on behaviour, scoped allow-lists with expiry, risk-based aggregation, keep and rerun positive tests, measure before/after.
4. *What is a good hunting hypothesis?* Strong answer: specific behaviour, data source, time window and expected evidence; based on intelligence, ATT&CK or environment change; testable; stop conditions; outcome becomes detection or data request.
5. *An AI tool generated 50 Sigma rules for us. Can we deploy them?* Strong answer: not directly; schema check, tests, ATT&CK ID check, false-positive review, experimental stage with measurement, ownership and ADS for each.

## Resources (free first)

- **Frameworks and methods:** [MITRE ATT&CK](https://attack.mitre.org/) and its [v18](https://attack.mitre.org/resources/updates/updates-october-2025/) and [v19](https://attack.mitre.org/resources/updates/updates-april-2026/) release notes · [ATT&CK Navigator](https://mitre-attack.github.io/attack-navigator/) · [Palantir ADS framework](https://github.com/palantir/alerting-detection-strategy-framework) · [Pyramid of Pain (Bianco, 2013)](https://detect-respond.blogspot.com/2013/03/the-pyramid-of-pain.html) · [Summiting the Pyramid (MITRE CTID)](https://center-for-threat-informed-defense.github.io/summiting-the-pyramid/) · [PEAK threat hunting framework (Splunk)](https://www.splunk.com/en_us/blog/security/peak-threat-hunting-framework.html) · [TaHiTI whitepaper](https://www.betaalvereniging.nl/wp-content/uploads/2026/03/TaHiTI-Threat-Hunting-Methodology-whitepaper.pdf) · [MITRE CAR](https://car.mitre.org/) · [MITRE Center for Threat-Informed Defense](https://ctid.mitre.org/)
- **Rules and tools:** [SigmaHQ rules](https://github.com/SigmaHQ/sigma) · [Sigma specification](https://github.com/SigmaHQ/sigma-specification) · [pySigma](https://github.com/SigmaHQ/pySigma) · [sigma-cli](https://github.com/SigmaHQ/sigma-cli) · [Elastic detection-rules](https://github.com/elastic/detection-rules) · [Splunk security_content](https://github.com/splunk/security_content) · [DeTT&CT](https://github.com/rabobank-cdc/DeTTECT)
- **Validation (isolated lab only):** [Atomic Red Team](https://github.com/redcanaryco/atomic-red-team) · [MITRE Caldera](https://caldera.mitre.org/)
- **Datasets and practice:** [OTRF Security-Datasets](https://github.com/OTRF/Security-Datasets) · [Splunk BOTS v3](https://github.com/splunk/botsv3) · [CyberDefenders threat hunting labs](https://cyberdefenders.org/) · [Blue Team Labs Online](https://blueteamlabs.online/)
- **Research:** [Sommer and Paxson, "Outside the Closed World" (IEEE S&P 2010)](https://ieeexplore.ieee.org/document/5504793) · [Arp et al., "Dos and Don'ts of Machine Learning in Computer Security" (USENIX Security 2022)](https://www.usenix.org/conference/usenixsecurity22/presentation/arp)

## Sources

All checked 12 Oct 2026.

- MITRE ATT&CK, Updates October 2025 (v18: Detection Strategies and Analytics, data sources deprecated) — https://attack.mitre.org/resources/updates/updates-october-2025/
- MITRE ATT&CK, Updates April 2026 (v19, 28 Apr 2026: Stealth TA0005 and Defense Impairment TA0112; Enterprise 15 tactics, 222 techniques, 475 sub-techniques) — https://attack.mitre.org/resources/updates/updates-april-2026/
- Google Cloud / Mandiant, *M-Trends 2026* (22-second hand-off; 122-day median dwell for espionage and DPRK IT-worker cases) — https://cloud.google.com/blog/topics/threat-intelligence/m-trends-2026
- CISA and partners, living-off-the-land guidance (Feb 2024) — https://www.cisa.gov/resources-tools/resources/identifying-and-mitigating-living-land-techniques
- Google Threat Intelligence Group, Salesloft Drift data theft (Aug 2025) — https://cloud.google.com/blog/topics/threat-intelligence/data-theft-salesforce-instances-via-salesloft-drift
- ExCyTIn-Bench, arXiv 2507.14201 — https://arxiv.org/abs/2507.14201
- Sigma specification repository (rules, correlation rules, filters) — https://github.com/SigmaHQ/sigma-specification

_Last reviewed: 2026-10_
