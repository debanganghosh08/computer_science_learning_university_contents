# SEC404 · Labs and projects

Build everything in your own lab: the SIEM and data from SEC302/SEC304, a local open-weights model (for example through Ollama) and, where allowed, a vendor trial or API with your own account. Prompt-injection tests target **only your own assistants and data**. Never paste real personal data or real incident evidence into hosted AI services; use lab data and public datasets. Every lab and project ships code, an evaluation harness that runs in one command, and a results table.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Task map and product comparison | Rate 20 SOC tasks for automation potential and risk; compare four AI security products from their documentation | Rating table with reasons; comparison of inputs, actions, limits | 3 h |
| 2 · Failure-mode reproduction | Reproduce hallucination, non-determinism, sycophancy and long-context truncation on security tasks | Failure log with prompts, outputs and settings | 4 h |
| 3 · Triage assistant with evidence checker | Structured-output assistant for one alert type; deterministic checker that rejects unsupported claims; two read-only tools with call logging | Code, schema, rejection-rate measurement | 8 h |
| 4 · Labelled dataset, metrics and trial | 100-alert labelled set with hard cases; precision, recall, calibration, abstention, citation accuracy; a small within-class trial with and without the assistant | Dataset card, metrics report, trial results | 8 h |
| 5 · AI-drafted queries and detections | Generate 15 queries and 10 Sigma rules with and without schema context; run them through tests | Pass rates and error classification | 4 h |
| 6 · Summarisation faithfulness | Score three AI incident summaries against the source timeline; write data-handling rules for AI in incidents | Annotated summaries, rules | 3 h |
| 7 · Threat model, injection tests and defences | Threat-model the assistant (OWASP LLM and Agentic Top 10, MITRE ATLAS); insert test instructions into your lab data; implement three defences and re-measure | Threat model, test suite, before/after obedience rates | 8 h |
| 8 · Approval workflow and agent logging | Approval gate for "revoke sessions"; full logging of prompts, tool calls and decisions; detections for unusual agent tool use | Workflow, logs, tested detections | 4 h |
| 9 · Detecting adversary AI use | Three detections: model-API calls from unexpected hosts, use of stolen AI API keys, AI CLI tools invoked by unusual parents | Detections with lab tests | 4 h |

## Projects

### P1 · Grounded phishing-triage assistant (L1, ~6 hours)

**Real-world inspiration.** Microsoft shipped a Phishing Triage Agent in Security Copilot and published a randomised trial (arXiv 2511.13860, Microsoft authors) in which most of the productivity gain came from prioritising the queue. Google's Triage and Investigation agent returns verdicts with explanations for analysts to review.

**What to build.** An assistant that takes a reported email's parsed headers, indicators and enrichment (from your SEC302 P1 kit or a similar parser) and returns JSON: verdict (malicious, suspicious, benign, insufficient evidence), confidence, the evidence fields relied on, and recommended next steps. A deterministic checker rejects any claim not present in the input. A ranking mode orders a queue by predicted risk.

**Acceptance criteria**
- 100% of outputs on a 40-email labelled set are schema-valid after at most one retry.
- Every accepted claim cites an input field; the report states how many outputs the checker rejected.
- Recall for malicious emails is at least 90% on the labelled set; the report also gives precision and the abstention rate.
- The ranking mode places at least 80% of malicious emails in the top half of the queue.

**Stretch goals.** Compare a local model with a hosted one on the same set, including cost and latency.

**What it proves to an employer.** You can build an AI assistant that is useful and checkable, not just impressive in a demo.

### P2 · Independent evaluation of an AI security tool (L2, ~15 hours)

**Real-world inspiration.** Public evidence on AI in SOCs ranges from vendor-run randomised trials to independent benchmarks such as ExCyTIn-Bench (best model 0.606 on multi-step investigations) and CyberSOCEval (models far from saturating). Buyers rarely run their own evaluations, and vendors may change the model underneath without notice.

**What to build.** An evaluation of one AI triage or investigation tool (a vendor trial you are permitted to test, or your own assistant built on an open model) using: a 150-alert labelled dataset from your lab and public datasets, a subset of one public benchmark (CTIBench or CyberSOCEval), and a small randomised trial with at least four classmates triaging with and without the tool.

**Acceptance criteria**
- The dataset card documents sources, labelling method, inter-labeller agreement on a 30-alert overlap, and hard cases.
- Metrics include precision and recall for "escalate", calibration (a reliability plot), abstention, citation accuracy and time per alert, each with a confidence interval or spread.
- The trial uses random assignment of alerts or participants and reports the effect on both speed and accuracy.
- At least ten error cases are shown and classified; the report ends with a deploy / limited deploy / do-not-deploy recommendation and the conditions that would change it.
- The harness reruns the full evaluation in one command for regression testing.

**Stretch goals.** Re-run after changing the model or prompt and report the regression; compare your results with the published benchmark scores and explain differences.

**What it proves to an employer.** You can measure AI tools honestly, which security leaders need before trusting them with alerts.

### P3 · Secure agentic investigation workflow (L3, portfolio-grade, ~30 hours)

**Real-world inspiration.** EchoLeak (CVE-2025-32711, June 2025) showed that a crafted email could steer Microsoft 365 Copilot into leaking data with no user click. Google reported malware (FRUITSHELL) carrying prompts aimed at AI analysis tools, and Anthropic documented an agentic intrusion (GTG-1002, November 2025) in which the attacker's AI ran most of the operation. The OWASP Top 10 for Agentic Applications (December 2025) lists agent goal hijack first. A defender's agent must therefore be designed to fail safely.

**What to build.** An agent that investigates identity alerts (impossible travel, MFA fatigue, risky OAuth consent) in your lab:
1. read-only tools for SIEM queries and directory lookups, each with a fixed scope and rate limit;
2. a structured investigation report with evidence citations and an evidence checker;
3. a proposed containment action (revoke sessions, disable an OAuth grant) that executes only after a named human approves it, with dry-run and rollback;
4. a threat model (OWASP LLM and Agentic Top 10, MITRE ATLAS) and at least **30 injection test cases** placed in fields the agent reads (log messages, user-agent strings, email subjects, ticket text, app display names);
5. defences (data/instruction separation, output validation, tool allow-lists, approval gates, anomaly detection on tool use) and measurements before and after;
6. full logging of prompts, tool calls and decisions, plus SIEM detections for abnormal agent behaviour;
7. a governance pack: NIST AI RMF mapping, data-handling rules, a model-change procedure and an AI-off fallback runbook.

**Acceptance criteria**
- On a 60-alert labelled set, the agent's report is evaluated for verdict accuracy, citation accuracy and time saved versus a human baseline.
- On the 30 injection cases, the share that changed the agent's verdict or proposed action is reported before and after defences; no case results in an executed action without human approval.
- The agent has no credentials with write permissions; this is demonstrated by a test in which it tries a write call and is refused.
- Every agent action can be reconstructed from logs by a reviewer in under 10 minutes.
- The governance pack names the accountable owner, the conditions for suspending the agent, and how analysts keep their skills (AI-off drills).

**Stretch goals.** Add a second, independent model as a reviewer and measure whether it catches the first model's errors or repeats them; publish your injection test suite (lab data only) for others to reuse.

**What it proves to an employer.** You can put AI agents into security operations with evidence, guardrails and governance. Few people can yet do this well, and it is where SOC engineering roles are heading.

## Feeds into

- [SEC501 Frontier Seminar](../../year_5/SEC501_frontier_seminar_threat_intelligence/README.md): AI for threat intelligence and research on AI-enabled adversaries.
- [OV05 AI Security and Safety Engineering](../../../../04_overlaps/OV05_ai_security_safety/README.md): securing AI systems beyond the SOC.
- [THS501 Thesis or Capstone I](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md): evaluation of AI security tools and injection-resistant agent design are strong thesis topics.
- [LCH502 Career Launch and Founder Studio](../../../../05_shared_years_3_to_5/LCH502_career_launch_and_founder_studio/README.md): P3 is a credible seed for a security-AI product.
