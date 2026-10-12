# SEC404 · AI in Security Operations

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 4 · 8 | 4 (≈ 120 hours) | L3 → L4 | [SEC304](../../year_3/SEC304_endpoint_and_operating_system_security/README.md) (catalogue prerequisite); [SEC302](../../year_3/SEC302_security_operations_soc_siem_and_monitoring/README.md) and [CS214](../../../../02_year_2_core_computer_science/semester_4/CS214_machine_learning_foundations/README.md) strongly recommended | [SEC501](../../year_5/SEC501_frontier_seminar_threat_intelligence/README.md), [OV05 AI Security and Safety Engineering](../../../../04_overlaps/OV05_ai_security_safety/README.md), [THS501](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md) |

Part of the [Cybersecurity Defense major](../../README.md). This course is about **using AI to defend** and **defending the AI you use**. Prompt-injection and misuse topics are taught from the defender's side: you test only your own assistants and lab systems, and you never target third-party AI services. Attacking AI systems as a discipline is covered, with authorisation rules, in [OFF403 AI and LLM Red Teaming](../../../ethical_hacking_offensive_security/year_4/OFF403_ai_and_llm_red_teaming/README.md).

## Why this course matters now

AI moved from demos to daily SOC work in 2025–26. Microsoft made Security Copilot and a set of AI agents part of Microsoft 365 E5 in November 2025; Google's Security Operations "Triage and Investigation agent" investigates alerts in about a minute and reached general availability in 2026; Elastic's Attack Discovery groups alerts into attack narratives with a language model. ISC2's 2025 study found 28% of organisations had integrated AI security tools and 41% of professionals named AI as their top skills need. The evidence is mixed and must be read carefully. A Microsoft-run randomised trial found analysts with the Phishing Triage Agent produced up to 6.5 times as many true positives per minute, mostly through better queue ordering; but on ExCyTIn-Bench, which tests multi-step investigations over 57 Microsoft Sentinel log tables, the best model scored 0.606, and CyberSOCEval (Meta and CrowdStrike, 2025) found models far from saturating malware-analysis and threat-intelligence reasoning. The assistants are also a new attack surface: EchoLeak (CVE-2025-32711, June 2025) showed a crafted email could make Microsoft 365 Copilot leak data with no user click, and Google found malware carrying prompts aimed at AI analysis tools. Attackers use AI too: Anthropic reported in November 2025 that a state-sponsored group used an AI agent for 80–90% of an espionage campaign's tactical work. The people who will be hardest to replace are those who can build, measure, secure and govern these systems, and still do the investigation themselves when the AI is wrong.

## Learning outcomes

By the end you can:

1. **Explain** how language models, retrieval, tool use and agents work, and **predict** their failure modes (hallucination, non-determinism, context limits, sycophancy) in security tasks.
2. **Build** a grounded alert-triage assistant that returns structured verdicts with evidence citations, using read-only tools and a local or approved model.
3. **Evaluate** AI security tools with labelled datasets, appropriate metrics (precision, recall, calibration, abstention, time saved), randomised comparisons and public benchmarks, and **report** error types.
4. **Use** AI to draft detections, queries and incident reports, and **verify** them with tests and evidence checks.
5. **Threat-model** AI-enabled SOC tooling against the OWASP Top 10 for LLM Applications (2025), the OWASP Top 10 for Agentic Applications (2026) and MITRE ATLAS, and **implement** defences against indirect prompt injection and excessive agency.
6. **Design** autonomy levels and approval gates for SOC agents, with logging, rollback and blast-radius limits.
7. **Detect** adversary use of AI (LLM-calling malware, AI-assisted phishing and voice fraud, agentic intrusions) from observable evidence.
8. **Govern** AI use in security operations (data handling, NIST AI RMF, ISO/IEC 42001, NIST IR 8596 draft) and **write** a procurement evaluation.

## Chapters and lessons

### Chapter 1 · Where AI sits in security operations (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 The task map | Enrichment, triage, investigation, query writing, detection drafting, hunting, reporting, phishing analysis, vulnerability prioritisation | Rate 20 SOC tasks by automation potential and risk |
| 1.2 Products in 2026 | Microsoft Security Copilot and agents, Google SecOps Triage and Investigation agent, Elastic Attack Discovery, CrowdStrike Charlotte AI, SentinelOne Purple AI, Security Onion's assistant, open-source stacks | Compare four products' documented inputs, actions and limits |
| 1.3 Evidence vs claims | Vendor claims, Microsoft's RCT (authors are Microsoft staff), benchmarks; what each kind of evidence can show | Classify ten public claims as measured, self-reported or marketing |
| 1.4 What humans keep | Containment decisions, novel investigations, accountability, regulator reporting | Write the human-ownership list for your SOC |

**Check your understanding:** Why does a vendor-authored RCT still need independent replication? Which SOC tasks are low-risk for automation, and why? What does "the AI closed it" mean for accountability?

### Chapter 2 · LLM fundamentals for defenders (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 How models produce text | Tokens, context windows, sampling and temperature, training cut-offs | Show the same question giving different answers at different temperatures |
| 2.2 Retrieval and grounding | Retrieval-augmented generation over runbooks, past cases and schemas; chunking and citation | Build a small retrieval index over five runbooks |
| 2.3 Tools and agents | Function calling, the Model Context Protocol (MCP), agent loops, planning | Give a model one read-only SIEM search tool in the lab |
| 2.4 Failure modes | Hallucination, sycophancy, anchoring on the first hypothesis, silent truncation of long logs | Reproduce each failure in the lab and record it |
| 2.5 Local vs hosted models | Open-weights models (for example through Ollama) vs APIs; confidentiality, cost, latency, quality | Run the same triage prompt on a local and a hosted model |

**Check your understanding:** Why does a long log export make hallucination more likely? What does retrieval fix, and what does it not? Why is a model's training cut-off a security problem?

### Chapter 3 · Building a grounded triage assistant (weeks 3–4)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Inputs and enrichment | Alert, entity context, asset and identity data, history, threat intelligence | Design the input schema for five alert types |
| 3.2 Structured outputs | JSON schemas: verdict, confidence, evidence list (event IDs, query results), next steps, "insufficient evidence" option | Implement schema validation and retries |
| 3.3 Evidence checking | A deterministic checker that rejects claims not backed by provided evidence | Build the checker and measure how often it rejects outputs |
| 3.4 Tools, read-only | Query tools with fixed scopes, rate limits, no write or containment permission | Add two read-only tools and log every call |
| 3.5 Cost and latency | Token budgets, caching, batching, when not to call a model | Measure cost and time per alert |

**Check your understanding:** Why must "insufficient evidence" be an allowed answer? Why should the evidence checker be deterministic code, not another model? What is the risk of giving a triage assistant a "run any query" tool?

### Chapter 4 · Evaluating AI security tools (weeks 5–6)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Datasets | Labelled alert sets from your lab and public datasets (OTRF, BOTS); leakage and contamination; hard cases | Build a 100-alert labelled set with at least 20 hard cases |
| 4.2 Metrics | Precision and recall for "escalate", calibration, abstention rate, citation accuracy, time per alert, disagreement with humans | Compute all metrics for your Chapter 3 assistant |
| 4.3 Study design | A/B tests and randomised trials with analysts; what Microsoft's Phishing Triage Agent RCT measured (queue prioritisation produced 83% of the gain) | Design a small within-class trial and run it |
| 4.4 Public benchmarks | CTIBench (NeurIPS 2024), CyberSOCEval (2025), ExCyTIn-Bench (2025), Meta CyberSecEval; what benchmarks miss | Run one benchmark subset and compare with your own evaluation |
| 4.5 Regression testing | Re-running evaluations on every model or prompt change; LLM-as-judge pitfalls; evaluation frameworks such as Inspect | Put the evaluation in CI |

**Check your understanding:** Why can a tool that never escalates look 95% accurate? Why might queue ordering matter more than verdict quality? Why re-evaluate after a vendor silently updates its model?

### Chapter 5 · AI-assisted detection writing and hunting (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Natural language to query | KQL, SPL and ES\|QL generation with schema context; checking results against hand-written queries | Generate 15 queries and grade them |
| 5.2 Drafting detections | Sigma drafts tested in the [SEC401](../SEC401_detection_engineering_and_threat_hunting/README.md) pipeline; common errors | Measure the pass rate with and without schema and examples |
| 5.3 Hunting assistance | Hypothesis generation from intelligence reports; agentic hunting with read-only access | Have an assistant propose five hunts and execute the two best yourself |
| 5.4 Retrieval over your rule library | Indexing existing detections and ADS documents so drafts follow conventions and avoid duplicates | Measure duplicate and convention errors with and without retrieval |

**Check your understanding:** Why do AI-written queries fail silently? What context most improves AI-drafted detections? Who decides a hunt's conclusion?

### Chapter 6 · Incident summarisation and reporting (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Faithful summaries | Summaries of timelines and cases; faithfulness checks against source events | Score three AI summaries for unsupported claims |
| 6.2 Audience-specific drafts | Executive, engineer, regulator; consistency across versions | Generate three versions and diff their facts |
| 6.3 Confidentiality | Personal data under the DPDP Act, legal privilege, approved tools, retention of prompts and outputs | Write the data-handling rules for AI use in incidents |
| 6.4 One fact base | Executive, regulator and customer drafts generated from one verified timeline; automated diffing of facts between versions | Write a script that flags facts that differ between two drafts |

**Check your understanding:** Why must a regulator draft be checked line by line against the timeline? What should never be pasted into an unapproved AI tool? How do you detect a summary that is fluent but wrong?

### Chapter 7 · Securing AI in the SOC (weeks 9–10)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Threat model | OWASP Top 10 for LLM Applications 2025 (prompt injection, sensitive information disclosure, improper output handling, excessive agency, system prompt leakage), OWASP Top 10 for Agentic Applications 2026 (agent goal hijack), MITRE ATLAS | Threat-model your Chapter 3 assistant |
| 7.2 Indirect prompt injection | Attacker-controlled text in emails, log fields, file contents, tickets and web pages; EchoLeak (2025); FRUITSHELL and the Check Point sample (2025) | Insert test instructions into your own lab data and measure obedience |
| 7.3 Defences | Separating data from instructions, quoting untrusted content, output validation, least-privilege tools, human approval for actions, monitoring for anomalous tool use; why no defence is complete | Implement three defences and re-measure |
| 7.4 Data leakage and poisoning | Retrieval over sensitive data, access control in retrieval, poisoned knowledge bases | Show that your retrieval respects user permissions |

**Check your understanding:** Why does prompt injection stay unsolved even with better prompts? Which defence reduces impact most when injection succeeds? Why must retrieval enforce the user's permissions?

### Chapter 8 · Agents and automation with guardrails (week 11)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Autonomy levels | Assist → recommend → act with approval → act within limits; mapping actions to levels | Assign autonomy levels to 15 response actions |
| 8.2 Guardrails | Allow-listed actions, rate limits, blast-radius limits, dry runs, rollback, kill switch | Build an approval workflow for "revoke sessions" |
| 8.3 Agent observability | Logging prompts, tool calls and decisions; detecting an agent behaving abnormally; agent identities ([SEC303](../../year_3/SEC303_identity_and_access_management/README.md)) | Write detections for unusual agent tool use |
| 8.4 Failure drills | What the SOC does when the AI tool is down, wrong or compromised; manual fallback runbooks | Run a 30-minute triage drill with the assistant disabled |

**Check your understanding:** Why should containment actions require approval even when the agent is usually right? What would you log to reconstruct an agent's decision? How do you stop a misbehaving agent quickly?

### Chapter 9 · Adversaries using AI (week 12)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 What is documented | Anthropic's GTG-1002 report (AI did 80–90% of tactical work; it also hallucinated credentials); GTIG's AI Threat Tracker (PROMPTSTEAL in operations, PROMPTFLUX experimental); Mandiant's view that 2025 breaches were not mainly "the direct result of AI" | Summarise what is proven vs speculative |
| 9.2 Detectable evidence | Calls to model APIs from unexpected hosts, stolen AI API keys, local AI CLI tools abused by malware (QUIETVAULT), machine-speed activity patterns | Write three detections and test them in the lab |
| 9.3 Social engineering at scale | AI-written phishing and voice cloning; voice phishing at 11% of Mandiant's 2025 intrusions; verification procedures | Update a help-desk verification procedure for voice cloning |
| 9.4 Protecting your own AI accounts | Model API keys and agent credentials as secrets; usage-spike monitoring; rotation and revocation | Add usage monitoring and an alert for your lab model account |

**Check your understanding:** What evidence would distinguish an AI-orchestrated intrusion from a fast human operator? Why do stolen AI API keys matter to defenders? Which control defeats a cloned voice?

### Chapter 10 · Governance, procurement and people (weeks 13–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Frameworks | NIST AI RMF and its generative AI profile (NIST AI 600-1), NIST IR 8596 Cyber AI Profile (preliminary draft, December 2025), ISO/IEC 42001 | Map your assistant to AI RMF functions |
| 10.2 Procurement | Evaluation on your data, data residency and retention, model update notices, audit logs, exit plans | Write a 25-question procurement evaluation |
| 10.3 Skills and deskilling | Training juniors when AI does Tier 1; AI-off drills; automation bias; a 2025 study (cited in Stanford's AI Index 2026) found learning penalties from heavy AI reliance | Design a 6-month analyst development plan with AI-off milestones |
| 10.4 Communicating AI risk | Explaining tool limits and evaluation results to leadership and auditors in plain language | Write a one-page AI tool status report for a CISO |

**Check your understanding:** What should a vendor tell you before changing the model behind your tool? Why keep AI-off drills in an AI-first SOC? Who signs off that an AI tool is fit for purpose?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Task map and product comparison | Ratings and comparison |
| 2 | 2 | Lab 2 · Failure-mode reproduction | Failure log |
| 3 | 3 | Lab 3 · Triage assistant v1 | Working assistant |
| 4 | 3 | Lab 3 (cont.) · Evidence checker and tools | Rejection rates; **P1 due** |
| 5 | 4 | Lab 4 · Labelled dataset and metrics | Evaluation report |
| 6 | 4 | Lab 4 (cont.) · Trial and benchmark | Trial results |
| 7 | 5 | Lab 5 · AI-drafted queries and detections | Pass rates; mid-term (AI off) |
| 8 | 6 | Lab 6 · Summarisation faithfulness | Scored summaries |
| 9 | 7 | Lab 7 · Threat model and injection tests | Obedience rates |
| 10 | 7 | Lab 7 (cont.) · Defences | Before/after; **P2 due** |
| 11 | 8 | Lab 8 · Approval workflow and agent logging | Workflow and detections |
| 12 | 9 | Lab 9 · Detecting adversary AI use | Three detections |
| 13 | 10 | Procurement evaluation | Questionnaire |
| 14 | 10 | P3 demos | **P3 due** |
| 15 | Review | Practical exam (AI off) and oral defence of P3 | Final exam |

## Working with AI in this course

- **Use AI for:** everything this course builds, as long as you measure it. Claude, ChatGPT, Gemini, local open-weights models and the vendor tools above are all fair game; Claude Code, GitHub Copilot or OpenAI Codex can help write the assistant, the checker and the evaluation harness.
- **Do without AI (drills):** a weekly 45-minute manual triage set (the human baseline for your evaluations); labelling the evaluation dataset; threat-modelling the assistant; the mid-term and the final practical. You cannot judge AI triage without being able to triage.
- **Verify AI output by:** the evidence checker, the labelled evaluation set, re-running queries, and injection test cases kept in CI. Track the metrics over time, not single impressions.
- **Where AI still fails here (show it, do not assume it):** your own measurements are the point of this course. Expect to find invented evidence, over-confident benign verdicts on low-volume attacks, instructions obeyed from data, and performance changes after model updates. Compare your findings with ExCyTIn-Bench and CyberSOCEval results and explain differences.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs 1–9 | 25% |
| Projects P1 / P2 / P3 | 5% / 15% / 20% |
| Mid-term (AI off) | 10% |
| Final practical (AI off) + oral defence of P3 | 25% |

**Mastery gate.** You pass when you can: (1) with AI off, triage 15 alerts correctly in 60 minutes (the human baseline); (2) given an unfamiliar AI triage tool and a labelled set, produce in three hours an evaluation with correct metrics, at least five classified error examples and a deploy/do-not-deploy recommendation; (3) find and fix two planted weaknesses (one prompt-injection path, one excessive permission) in a provided assistant design.

## Industry reality

Roles using this material include SOC engineers, detection engineers, security automation engineers and the new "AI security operations" or "security AI engineering" roles; the [SEC market page](../../../../06_career_and_market_readiness/01_market_map/roles/SEC_cybersecurity_defense.md) lists securing AI systems and AI skills as growing in value. Real anchors: Security Copilot in Microsoft 365 E5 (November 2025), Google's Triage and Investigation agent (2026), Microsoft's Phishing Triage Agent RCT, EchoLeak, Anthropic's GTG-1002 report and GTIG's AI Threat Tracker.

**Interview questions from this course**

1. *How would you decide whether to let an AI agent auto-close alerts?* Strong answer: labelled evaluation on your data, metrics including recall on true positives and abstention, staged rollout by alert type, daily sampling, injection tests, rollback, ownership.
2. *What is indirect prompt injection and how would it hit a SOC assistant?* Strong answer: instructions hidden in data the model reads (emails, logs, files, tickets); examples (EchoLeak, FRUITSHELL); defences focus on limiting impact: no write tools, approvals, output validation, evidence checks.
3. *Design a triage assistant for phishing reports.* Strong answer: inputs and enrichment, structured output with evidence, read-only tools, retrieval over runbooks, evaluation set, confidentiality, cost, human approval for remediation.
4. *A vendor says its AI reduces MTTR by 50%. What do you ask?* Strong answer: study design, baseline, which alerts, who measured, false-negative rate, your-data trial, model update policy, data handling.
5. *How do attackers use AI today, and what can a defender actually detect?* Strong answer: documented cases (GTG-1002, PROMPTSTEAL, AI phishing and voice), separates proven from speculative, lists observable evidence (LLM API traffic, stolen keys, AI CLI abuse, machine-speed patterns).

## Resources (free first)

- **Security of AI systems:** [OWASP Top 10 for LLM Applications](https://genai.owasp.org/llm-top-10/) · [OWASP Top 10 for Agentic Applications for 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/) · [MITRE ATLAS](https://atlas.mitre.org/) · [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework) · [NIST IR 8596 (preliminary draft)](https://csrc.nist.gov/pubs/ir/8596/iprd)
- **Benchmarks and evaluation:** [CTIBench](https://github.com/maveryn/cti-bench) · [CyberSOCEval, arXiv 2509.20166](https://arxiv.org/abs/2509.20166) · [ExCyTIn-Bench, arXiv 2507.14201](https://arxiv.org/abs/2507.14201) · [Meta PurpleLlama / CyberSecEval](https://github.com/meta-llama/PurpleLlama) · [Inspect evaluation framework](https://inspect.aisi.org.uk/)
- **Building blocks:** [Model Context Protocol](https://modelcontextprotocol.io/) · [Ollama](https://ollama.com/) · [Google SecOps Triage and Investigation agent docs](https://docs.cloud.google.com/chronicle/docs/secops/triage-investigation-agent)
- **Threat reporting:** [Anthropic, GTG-1002 report](https://www.anthropic.com/news/disrupting-AI-espionage) · [Google Threat Intelligence Group, AI Threat Tracker](https://cloud.google.com/blog/topics/threat-intelligence/threat-actor-usage-of-ai-tools)
- **Studies:** [Phishing Triage Agent RCT, arXiv 2511.13860](https://arxiv.org/abs/2511.13860) · [Stanford AI Index 2026](https://hai.stanford.edu/assets/files/ai_index_report_2026.pdf)

## Sources

All checked 12 Oct 2026.

- Microsoft Security blog, Security Copilot with Microsoft 365 E5 (18 Nov 2025) — https://www.microsoft.com/en-us/security/blog/2025/11/18/agents-built-into-your-workflow-get-security-copilot-with-microsoft-365-e5/
- Google Cloud documentation, Triage and Investigation agent — https://docs.cloud.google.com/chronicle/docs/secops/triage-investigation-agent
- Elastic, Attack Discovery GA — https://www.elastic.co/blog/production-ready-ai-capabilities
- ISC2, 2025 Cybersecurity Workforce Study (4 Dec 2025) — https://www.isc2.org/Insights/2025/12/2025-ISC2-Cybersecurity-Workforce-Study
- Randomized Controlled Trials for Phishing Triage Agent, arXiv 2511.13860 (Nov 2025) — https://arxiv.org/abs/2511.13860
- ExCyTIn-Bench, arXiv 2507.14201 — https://arxiv.org/abs/2507.14201 ; CyberSOCEval, arXiv 2509.20166 — https://arxiv.org/abs/2509.20166 ; CTIBench, NeurIPS 2024 — https://proceedings.neurips.cc/paper_files/paper/2024/hash/5acd3c628aa1819fbf07c39ef73e7285-Abstract.html
- The Hacker News, EchoLeak zero-click flaw in Microsoft 365 Copilot, CVE-2025-32711 (12 Jun 2025) — https://thehackernews.com/2025/06/zero-click-ai-vulnerability-exposes.html
- Anthropic, "Disrupting the first reported AI-orchestrated cyber espionage campaign" (13 Nov 2025) — https://www.anthropic.com/news/disrupting-AI-espionage
- Google Threat Intelligence Group, *AI Threat Tracker* (Nov 2025) — https://cloud.google.com/blog/topics/threat-intelligence/threat-actor-usage-of-ai-tools
- Check Point Research, embedded prompt injection sample (25 Jun 2025) — https://research.checkpoint.com/2025/ai-evasion-prompt-injection/
- Google Cloud / Mandiant, *M-Trends 2026* — https://cloud.google.com/blog/topics/threat-intelligence/m-trends-2026
- OWASP, Top 10 for Agentic Applications for 2026 (9 Dec 2025) — https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/
- NIST IR 8596 preliminary draft (16 Dec 2025) — https://csrc.nist.gov/pubs/ir/8596/iprd ; NIST AI 600-1 (Jul 2024) — https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence

_Last reviewed: 2026-10_
