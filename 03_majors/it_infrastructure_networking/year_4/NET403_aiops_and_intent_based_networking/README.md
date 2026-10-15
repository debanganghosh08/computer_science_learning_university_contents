# NET403 · AIOps and Intent-Based Networking

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 4 · 8 | 4 (≈ 120 hours) | L2 → L4 | [NET303](../../year_3/NET303_network_automation_and_netdevops/README.md); [CS214](../../../../02_year_2_core_computer_science/semester_4/CS214_machine_learning_foundations/README.md) helpful | [NET501](../../year_5/NET501_frontier_seminar_5g_satellite_internet/README.md); compare with [OPS403](../../../devops_sre_platform_engineering/year_4/OPS403_aiops_and_agentic_operations/README.md) |

OPS403 covers AIOps for software services in general. This course is about networks: network telemetry, topology-aware correlation, verification of network intent, network digital twins, and agents that touch routers and switches.

## Why this course matters now

Every major network vendor now sells AI operations. HPE completed its acquisition of Juniper Networks, whose Mist platform is built around AI-driven operations, in July 2025. In February 2026 Cisco announced "AgenticOps" agents that apply "reasoning from telemetry to root cause", "autonomously" tune RF, QoS and paths in campus and branch networks, and run "risk-aware agentic assessments" of changes, with data-centre agents in controlled availability from June 2026. The research is more cautious: Mondal et al. (2023) found GPT-4's router configurations full of "egregious errors" until automated verifiers fed back each mistake, and NetConfEval (2024) found that generating low-level network configuration was only feasible with the largest models. The biggest outages of 2025 came from automation itself: an AWS DNS automation race that emptied a regional endpoint's record, and a Cloudflare configuration file that grew past a limit. Intent-based networking, defined by the IRTF in RFC 9315 (2022), offers the missing discipline: state what the network must do, verify it continuously, and only let automation act inside proven limits. This course teaches you to build and judge these systems, so you are the person who decides how much autonomy a network gets, rather than the person whose tickets the agent closes.

## Learning outcomes

By the end you can:

1. **Build** a network telemetry pipeline (gNMI, flows, BMP, syslog, synthetic probes) with aligned time, topology context and bounded cardinality.
2. **Detect** anomalies in network metrics and logs with seasonal baselines, robust statistics and isolation forests, and **evaluate** detectors with precision, recall and detection delay on labelled incidents.
3. **Correlate** alerts using topology and dependencies to find a probable root cause, and **measure** how much noise the correlation removes.
4. **Express** network intent as testable assertions and **verify** it with control-plane and data-plane analysis (Batfish, header-space style reasoning).
5. **Build** a network digital twin from a source of truth and **use** it for what-if analysis, stating its fidelity limits.
6. **Build** an LLM-based network diagnosis assistant with read-only tools and **evaluate** it on planted faults against human baselines.
7. **Design** closed-loop automation with an action catalogue, blast-radius limits, approval tiers, hysteresis and rollback.
8. **Assess** vendor AIOps claims with your own measurements and **write** an adoption decision with evidence.

## Chapters and lessons

### Chapter 1 · Network AIOps, honestly (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Definitions | AIOps, assurance, intent-based networking, closed loop, agentic operations; automation vs augmentation | Classify 10 vendor feature descriptions into these categories |
| 1.2 The vendor landscape | Juniper Mist (HPE), Cisco AgenticOps and AI Assistant, and other controller-based platforms: what each claims and what evidence is public | Build a claims-vs-evidence table for two vendors from their own documents |
| 1.3 What the research says | Mondal et al. (2023), NetConfEval (2024), verification-guided generation | Summarise each paper's method and the limits of its conclusion |
| 1.4 Measuring value | MTTD, MTTR, noise reduction, change failure rate, operator hours; baselines before any tool | Define the 5 metrics you will use all semester and baseline your lab |

**Check your understanding:** Why is "AI found the root cause" not evidence without a baseline? Which vendor claim in your table is easiest to test, and which is hardest? Why did verifiers matter so much in the Mondal et al. results?

### Chapter 2 · Network telemetry as data (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Sources | gNMI streams, SNMP, syslog, IPFIX/sFlow flows, BGP Monitoring Protocol, synthetic probes, wireless client events | Inventory every signal your NET303 lab emits |
| 2.2 Pipelines | Collectors (gnmic, Telegraf), a message bus (Kafka), stores (Prometheus, InfluxDB, ClickHouse); retention and cost | Build a pipeline that keeps raw data 7 days and rollups 180 days |
| 2.3 Context | Joining telemetry with NetBox: device role, site, links, tenants; topology from LLDP | Enrich every metric with site and role labels |
| 2.4 Data quality | Clock skew, gaps, counter wraps and resets, cardinality explosions | Detect and repair 4 planted data-quality problems |

**Check your understanding:** Why is context (site, role, neighbour) worth more than more metrics? What does a counter reset do to a naive rate calculation? Why must every signal share the same clock?

### Chapter 3 · Anomaly detection on network metrics (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Baselines | Daily and weekly seasonality, STL decomposition, EWMA, Holt-Winters | Baseline a month of interface utilisation and flag deviations |
| 3.2 Robust statistics | Median and MAD z-scores, percentiles; why mean and standard deviation mislead on bursty traffic | Compare z-score and MAD detectors on the same data |
| 3.3 Multivariate methods | Isolation forest and simple autoencoders on combined interface, error and latency features | Train an isolation forest on lab data with planted incidents |
| 3.4 Evaluation | Labelled incidents, precision, recall, F1, detection delay, alert budget per day | Pick a threshold that meets an alert budget of 5 per day |

**Check your understanding:** Why does a static threshold on link utilisation fire every Monday morning? What is the cost of a detector with 99% accuracy on rare events? Why does detection delay matter as much as recall?

### Chapter 4 · Logs and routing events (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Log templates | Log parsing into templates (for example the Drain algorithm), rare-template detection | Parse a week of lab syslog into templates; find the rare ones |
| 4.2 Routing signals | BGP update rates, withdrawals, path changes from BMP; OSPF SPF runs; flapping detection | Detect a planted BGP flap and a route leak in the lab from BMP data |
| 4.3 Flow anomalies | Traffic shifts, new top talkers, unusual ports (defensive monitoring of your own network) | Flag a traffic shift caused by a failed link |
| 4.4 External signals | Public routing views (RIPE RIS, RouteViews) and outage trackers for issues outside your network | Correlate a public BGP event with your lab's view (simulated) |

**Check your understanding:** Why are rare log templates more useful than frequent ones for detection? Why can BGP update counts rise without any problem? How do you tell an internal fault from an upstream one?

### Chapter 5 · Topology-aware correlation and root cause (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 The graph | Building a topology and dependency graph from NetBox, LLDP and routing state | Generate the lab graph automatically |
| 5.2 Correlation | Grouping alerts by time and topology; suppression of downstream symptoms | Reduce 200 alerts from a core failure to 1 incident |
| 5.3 Root-cause ranking | Graph-based scoring, recent-change correlation, evidence lists | Rank causes for 5 planted incidents; measure top-1 and top-3 accuracy |
| 5.4 Limits | Correlation vs causation, missing topology, shared-risk links (same conduit, same power) | Plant a shared-risk failure your graph does not know about; observe |

**Check your understanding:** Why does a change log improve root-cause accuracy so much? What happens to topology-based correlation when the source of truth is wrong? Why report top-3 causes with evidence rather than one answer?

### Chapter 6 · Intent-based networking (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Concepts | RFC 9315: intent, fulfilment and assurance, the intent lifecycle; RFC 9316 intent classification | Write 10 intents for your lab in plain language |
| 6.2 From intent to policy | Translating business intent ("guest never reaches finance") to network policy and tests | Translate your 10 intents into Batfish assertions |
| 6.3 Assurance | Continuous checking that intent still holds after every change and every failure | Run assertions on every pipeline change and every 15 minutes |
| 6.4 Products and practice | How controller platforms implement intent; what remains manual | Map one vendor's intent feature to the RFC 9315 lifecycle |

**Check your understanding:** Why is "configure VLAN 30 on port 12" not an intent? What is the difference between fulfilment and assurance? Why must intent be re-checked after failures, not only after changes?

### Chapter 7 · Network verification (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Control-plane verification | Batfish (Fogel et al., NSDI 2015) and Minesweeper (Beckett et al., SIGCOMM 2017): deriving routes and checking properties across failures | Prove reachability holds under any single link failure |
| 7.2 Data-plane verification | Header Space Analysis (Kazemian et al., NSDI 2012), forwarding loops and black holes | Find a forwarding loop from dumped FIBs |
| 7.3 Differential analysis | Before/after snapshots: exactly which flows a change adds or removes | Show the full flow diff of a proposed ACL change |
| 7.4 What verification cannot prove | Model fidelity, unsupported features, runtime state, hardware bugs | List 5 failure types your verifier would miss |

**Check your understanding:** Why does checking all single-link failures matter more than checking the current state? What does differential analysis give a change reviewer? Why can a verified network still fail?

### Chapter 8 · Network digital twins (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Kinds of twin | Model twin (configuration analysis), emulation twin (Containerlab with real NOS images), simulation; IRTF NMRG digital-twin concepts | Build both a model twin and an emulation twin of the lab |
| 8.2 Building from the source of truth | Generating the twin from NetBox and backups automatically | Rebuild the twin nightly from data |
| 8.3 What-if analysis | Failure scenarios, capacity changes, migration rehearsal | Answer 3 what-if questions with evidence from the twin |
| 8.4 Fidelity | Where twins differ: scale, hardware, timers, traffic; how to state confidence | Write a fidelity statement for your twin |

**Check your understanding:** When is an emulation twin worth its cost over a model twin? Why must the twin be rebuilt from data rather than hand-maintained? What would make you distrust a twin's answer?

### Chapter 9 · LLM assistants for network operations (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Patterns | Retrieval over runbooks, configurations and past incidents; tool use through Model Context Protocol servers; read-only diagnosis | Build retrieval over your lab's runbooks and configs |
| 9.2 Tools | Read-only `show` commands, telemetry queries, NetBox queries, Batfish queries; tool descriptions and limits | Give an assistant 4 read-only tools and log every call |
| 9.3 Failure modes | Invented commands, wrong vendor syntax, confident wrong root cause, stale knowledge, over-long investigations | Collect and classify 20 assistant failures from the lab |
| 9.4 Security of assistants | Untrusted text in logs, interface descriptions or tickets acting as instructions (prompt injection); configuration and credential leakage; least-privilege tool credentials | Plant an instruction in an interface description and show your guardrails ignore it |

**Check your understanding:** Why should diagnosis tools be read-only by default? How can text inside a device configuration influence an assistant, and what stops it? Why is a confident wrong root cause worse than "I don't know"?

### Chapter 10 · Building and evaluating a diagnosis agent (week 10)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Benchmark design | Planted faults across layers (link, MTU, OSPF, BGP policy, ACL, DNS, Wi-Fi), ground truth, scoring rules | Build a benchmark of 25 faults with ground truth |
| 10.2 The agent | Planning, tool calls, evidence collection, a structured answer with confidence and evidence | Implement the agent with a tool budget per fault |
| 10.3 Evaluation | Top-1 accuracy, time to diagnosis, tool calls, cost, unsafe suggestions; comparison with student engineers | Run the benchmark three times; report variance |
| 10.4 Improving | Better tools, better retrieval, verifier feedback (the Mondal et al. pattern), refusing when evidence is weak | Add a verifier step and measure the change in accuracy |

**Check your understanding:** Why run the benchmark more than once? What does a tool-call budget protect? Which fault class did your agent fail most, and is the fix a better model or a better tool?

### Chapter 11 · Closed-loop automation with guardrails (week 11)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Control loops | Observe, decide, act, verify; loop timing; oscillation and hysteresis | Build a loop that shifts traffic off a degraded link and back, without flapping |
| 11.2 The action catalogue | Allowed actions, preconditions, blast-radius caps, rate limits, approval tiers by risk | Write a catalogue of 10 actions with tiers |
| 11.3 Lessons from automation failures | AWS October 2025 (race between automation instances), Cloudflare November 2025 (generated file grew past a limit) | Add locks, version checks and size checks to your loop |
| 11.4 Kill switches and audit | Global stop, per-action disable, logs linking every action to evidence and approval | Demonstrate the kill switch stopping a runaway loop within 5 seconds |

**Check your understanding:** Why can two correct automations be dangerous together? What makes an action safe enough for no human approval? Why does every closed loop need hysteresis?

### Chapter 12 · Governance, adoption and capstone (weeks 12–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 12.1 Running AI systems | Model and prompt versioning, drift, re-evaluation after upgrades, cost tracking | Re-run your benchmark after changing the model; report the difference |
| 12.2 Accountability and data | Who is accountable for an agent's action; personal data in logs and India's DPDP Act; what may be sent to external models | Write a data-handling policy for your assistant |
| 12.3 Adoption decisions | Pilot design, success criteria, autonomy levels earned by evidence | Write an adoption recommendation for a vendor AIOps feature |
| 12.4 Skills and roles | How network operations roles change; what operators should still practise without AI | Write a 1-page training plan for a NOC adopting AI |
| 12.5 Capstone review | P3 demonstrations and defence | Defend your system to a panel |

**Check your understanding:** What evidence would justify moving an action from "approval required" to "automatic"? Why must a model upgrade trigger re-evaluation? Which skills must a NOC keep practising even if an agent handles most incidents?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Claims vs evidence and baselines | Metric baseline |
| 2 | 2 | Lab 2 · Telemetry pipeline with context | — |
| 3 | 3 | Lab 3 · Anomaly detectors and evaluation | **P1 due** |
| 4 | 4 | Lab 4 · Log templates and BMP routing events | — |
| 5 | 5 | Lab 5 · Topology-aware correlation | — |
| 6 | 6 | Lab 6 · Intents as assertions | Mid-term (AI off) |
| 7 | 7 | Lab 7 · Verification under failures | — |
| 8 | 8 | Lab 8 · Digital twins and what-if | — |
| 9 | 9 | Lab 9 · Assistant with read-only tools | **P2 due** |
| 10 | 10 | Diagnosis benchmark runs | Benchmark report |
| 11 | 11 | Lab 10 · Closed loop with guardrails | — |
| 12 | 12 | Re-evaluation after model change | — |
| 13 | 12 | P3 | — |
| 14 | 12 | Capstone review | **P3 due** |
| 15 | Review | Oral defence of P3 | Final exam (AI off) |

## Working with AI in this course

- **Use AI for:** building the assistant itself; drafting detectors, Batfish queries and pipeline code; summarising papers (then reading them); generating synthetic incident descriptions for testing.
- **Do without AI (drills):** reading telemetry and logs to diagnose faults by hand (your human baseline for the benchmark); writing intents as assertions; designing the action catalogue and approval tiers; the mid-term and final.
- **Verify AI output by:** the benchmark with ground truth; verifiers (Batfish, lab tests) on every proposed fix; repeated runs to measure variance; logs of every tool call; comparison with human diagnosis times.
- **Where AI still fails here:** in this course you produce the evidence yourself. Expect, and measure, wrong-vendor syntax, invented commands, confident wrong root causes when telemetry is missing, sensitivity to injected text in logs, and variation between identical runs. Your P2 and P3 reports must state failure rates with the number of trials.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (10) | 25% |
| Projects P1–P3 | 35% |
| Mid-term (AI off) | 10% |
| Final exam (AI off) + P3 oral defence | 30% |

**Mastery gate.** You pass when you can, without AI: (1) diagnose 4 planted faults from telemetry, logs and topology in 60 minutes; (2) write 5 intents for an unseen network as executable assertions and show which hold under single failures; (3) given a proposed autonomous action, write its catalogue entry (preconditions, blast radius, approval tier, rollback, kill switch) and defend it.

## Industry reality

Where this is used: vendor platforms (Juniper Mist under HPE, Cisco's AgenticOps and AI Assistant, and others) in campus, branch and data-centre networks; large operators and cloud providers with in-house verification and automation; managed network service providers in India competing on outcome-based contracts. Network automation and AIOps engineers increasingly sit between network engineering, software engineering and ML.

**Interview questions from this course**

1. *How would you evaluate a vendor's claim that its AI cuts MTTR by half?* Strong answer: baseline first, define MTTR precisely, pilot with control sites, collect incidents, compare, check for selection bias, include false root causes and operator effort.
2. *Design anomaly detection for 10,000 interfaces.* Strong answer: seasonal baselines per interface class, robust statistics, topology-aware grouping, an alert budget, evaluation on labelled incidents, cardinality and cost control.
3. *What is intent-based networking, really?* Strong answer: declarative intent, translation to policy, fulfilment and assurance (RFC 9315), continuous verification; distinguishes marketing from mechanism.
4. *Would you let an AI agent roll back a change automatically?* Strong answer: depends on action class and evidence; rollback is lower risk than new change but can still harm; preconditions, blast radius, verification, audit, kill switch; autonomy earned by measured performance.
5. *Your closed loop moved traffic back and forth every minute. Why, and how do you fix it?* Strong answer: missing hysteresis or hold-down, measurement noise, loop interacting with another automation; fix with thresholds, dampening, locks and coordination.

## Resources (free first)

- **Standards and drafts:** RFC 9315 (Intent-Based Networking: Concepts and Definitions), RFC 9316 (Intent Classification) — https://www.rfc-editor.org/ ; IRTF Network Management Research Group (digital twin and intent work) — https://datatracker.ietf.org/rg/nmrg/about/
- **Papers:** Fogel et al., Batfish (NSDI 2015) — https://www.usenix.org/conference/nsdi15/technical-sessions/presentation/fogel ; Kazemian et al., Header Space Analysis (NSDI 2012) — https://www.usenix.org/conference/nsdi12/technical-sessions/presentation/kazemian ; Mondal et al. (2023) — https://arxiv.org/abs/2307.04945 ; NetConfEval — https://github.com/NetConfEval/NetConfEval
- **Tools:** Batfish — https://batfish.org/ ; gnmic — https://gnmic.openconfig.net/ ; Prometheus — https://prometheus.io/ ; scikit-learn anomaly detection (IsolationForest) — https://scikit-learn.org/stable/modules/outlier_detection.html ; statsmodels STL — https://www.statsmodels.org/stable/examples/notebooks/generated/stl_decomposition.html ; Model Context Protocol — https://modelcontextprotocol.io/
- **Routing data:** RIPE RIS — https://ris.ripe.net/ ; RouteViews — https://www.routeviews.org/
- **Paid, optional:** vendor AIOps training (Juniper Mist, Cisco) if your employer uses those platforms.

## Sources

- HPE, "Hewlett Packard Enterprise closes acquisition of Juniper Networks" (2 Jul 2025) — https://www.hpe.com/us/en/newsroom/press-release/2025/07/hewlett-packard-enterprise-closes-acquisition-of-juniper-networks-to-offer-industry-leading-comprehensive-cloud-native-ai-driven-portfolio.html (checked 2026-10)
- Cisco newsroom, "Cisco Expands AgenticOps Innovations Across Portfolio" (10 Feb 2026) — https://newsroom.cisco.com/content/r/newsroom/en/us/a/y2026/m02/cisco-expands-agenticops-innovations-across-portfolio.html (checked 2026-10)
- Mondal et al., "What do LLMs need to Synthesize Correct Router Configurations?" (arXiv 2307.04945, Jul 2023) — https://arxiv.org/abs/2307.04945 (checked 2026-10)
- Wang et al., "NetConfEval: Can LLMs Facilitate Network Configuration?" (Proc. ACM Netw., CoNEXT 2024) — https://github.com/NetConfEval/NetConfEval (checked 2026-10)
- AWS DynamoDB us-east-1 post-event summary (Oct 2025) — https://aws.amazon.com/message/101925/ ; Cloudflare outage report (18 Nov 2025) — https://blog.cloudflare.com/18-november-2025-outage/ (checked 2026-10)
- RFC 9315, Intent-Based Networking — Concepts and Definitions (Oct 2022) — https://www.rfc-editor.org/rfc/rfc9315 (checked 2026-10)

_Last reviewed: 2026-10_
