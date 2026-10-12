# AIE501 · Labs and projects

This is a research seminar, so labs are short experiments that accompany each week's papers, and the projects build toward a reproduction and a thesis proposal. Every experiment states its hypothesis before it runs, fixes seeds and model snapshot IDs, reports the number of trials and confidence intervals, and archives traces. Security experiments run only in the official sandboxes of the benchmarks named (AgentDojo, OSWorld, WebArena) or in environments you own, and never against real third-party systems.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Time-horizon re-analysis | Re-plot METR's public data file; fit 50% and 80% horizons and a doubling time; test sensitivity to model selection and date range | Notebook, plots, a paragraph on how robust the trend is | 4 h |
| 2 · Multi-session harness experiment | Apply the initializer + incremental-session pattern to a 20-feature project; compare with a single long session | Features completed per session, tokens, failure notes | 5 h |
| 3 · Computer-use agent in a sandbox | Run an open agent on 20 OSWorld or WebArena tasks; compare accessibility-tree and screenshot observations on 10 | Success rates with CIs, action logs, failure categories | 5 h |
| 4 · AgentDojo evaluation | Measure your AIE304 agent's utility and attack success on AgentDojo; add one defence pattern and re-measure | Utility–security table before/after | 5 h |
| 5 · Trusted monitoring and resampling | Implement a toy control protocol on code tasks: a weaker trusted monitor, an audit budget and resampling of suspicious actions | Safety–usefulness curve across audit budgets | 5 h |
| 6 · Hidden-test reward-hacking study | Run an agent on 30 tasks with visible and hidden tests; classify hacks (special-casing, weakening tests) | Visible vs hidden pass rates; hack taxonomy; monitor prompt and its catch rate | 4 h |
| 7 · Benchmark audit and Inspect port | Audit one agent benchmark with a rigour checklist; port one of your evals to UK AISI Inspect | Audit report; Inspect task code and run log | 5 h |
| 8 · Memory evaluation | Run LongMemEval (or a subset) on two memory designs; add temporal validity and test contradictions | Accuracy by question type; contradiction-handling results | 4 h |
| 9 · A2A negotiation simulation and liability brief | Two agents from "different companies" negotiate a booking over A2A with authority limits; record failures; write a policy brief on agent liability | Logs, failure analysis, 2-page brief | 5 h |
| 10 · Reproduction plan and open-problem ranking | Select a paper to reproduce; scope compute and tolerances; rank open problems by one-year tractability | Reproduction plan, ranked list with reasons | 3 h |

## Projects

### P1 · How long can our agent work? A measurement note (L1, ~6 hours)

**Real-world inspiration.** METR measures capability as the human-time length of tasks an agent completes at a given success rate, and reports that its current tasks cannot measure reliably above 16 hours (checked 2026-10). Its 50% and 80% horizons differ by a large factor, which matters more to products than the headline.

**What to build.** Assemble 15 software tasks with human time estimates from 5 minutes to 4 hours (from public suites or tasks you time yourself). Run your AIE304 or AIE401 agent on each 5 times and fit a logistic success-vs-length curve to estimate your agent's 50% and 80% horizons with bootstrap intervals.

**Acceptance criteria**
- Human time estimates are documented (who timed them, how).
- 75 runs with traces; horizons reported with 90% bootstrap intervals.
- A threats-to-validity section with at least five specific threats (task selection, timing error, contamination, harness effects, grader errors).
- A one-paragraph product recommendation: which task lengths to automate, which to keep supervised.

**Stretch goals.** Repeat with a second model or harness and test whether the difference is significant.

**What it proves to an employer.** You can turn "how good is our agent?" into a careful measurement with honest uncertainty.

### P2 · Utility versus security for an agent that reads untrusted content (L2, ~15 hours)

**Real-world inspiration.** CaMeL achieved provable security on 77% of AgentDojo tasks against 84% utility without defence (Debenedetti et al., 2025). Beurer-Kellner et al. (2025) describe design patterns that trade capability for injection resistance, and Meta's Rule of Two (2025) limits agents to two of three risky properties. Teams must choose a point on this trade-off with data.

**What to build.** Take an agent that handles email-like or document-like tasks inside AgentDojo's environment (or an equivalent sandbox you build). Implement and compare at least three configurations: no defence, a classifier/prompt-level defence, and one architectural pattern (plan-then-execute, dual LLM, or a CaMeL-style capability layer). Measure utility, attack success rate, latency and cost.

**Acceptance criteria**
- All three configurations evaluated on the same task and attack sets with at least 3 runs each; results with CIs.
- The architectural configuration reduces attack success by at least 80% relative to no defence, or the report explains precisely why it could not.
- Utility loss of each defence is quantified per task category, with three illustrative traces.
- A design recommendation for a named product scenario (for example an assistant for a Bengaluru startup's support inbox) with residual-risk statement.
- No attack payloads beyond those shipped with the benchmark are published in the report.

**Stretch goals.** Combine an architectural pattern with a monitor and measure the marginal gain.

**What it proves to an employer.** You can quantify and defend agent security trade-offs. AI security, platform and safety teams value this rare skill.

### P3 · Reproduction and research proposal (L3, portfolio-grade, ~30 hours)

**Real-world inspiration.** Benchmarks built from real research tasks, such as PaperBench (2025) and RE-Bench (2024), show how hard faithful replication is even for experts. Contamination findings such as "The SWE-Bench Illusion" (2025) show why independent reproduction matters. Research engineering roles at labs, safety institutes and evaluation organisations expect candidates who have reproduced and extended published work.

**What to build.** Reproduce one central result from a paper on this course's reading list (for example a CaMeL utility/security number on a subset of AgentDojo, a τ-bench pass^k curve, a control-protocol safety–usefulness curve, or a LongMemEval comparison), using public code and a compute budget agreed with the instructor. Then write a research proposal that extends it, ready to become your [THS501](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md) thesis.

**Acceptance criteria**
- The reproduction states the original claim, your setting, the differences (model versions, subsets, compute) and the result with uncertainty; a match within the tolerance stated in your plan, or a documented discrepancy with diagnosis.
- All code, configs and traces are in a public or course repository, and another student reruns a key number in under 3 hours.
- The proposal (≤ 6 pages) contains a research question, hypothesis, method, evaluation with a contamination-resistant test set, baselines, compute budget, risks, and an ethics and safety review.
- A 20-minute symposium talk and a 45-minute oral defence.

**Stretch goals.** Contact the original authors with your discrepancy report; submit a workshop paper or an open-source evaluation.

**What it proves to an employer.** You can do research engineering at the frontier: read, reproduce, find the gap and propose a credible next step.

## Feeds into

- [THS501](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md) and [THS502](../../../../05_shared_years_3_to_5/THS502_thesis_or_capstone_ii/README.md): P3's proposal is the thesis plan.
- [RES502 Reading, Reproducing and Extending Papers](../../../../05_shared_years_3_to_5/RES502_reading_reproducing_and_extending_papers/README.md): shares reproduction methods and reporting standards.
- [OV05 AI Security and Safety Engineering](../../../../04_overlaps/OV05_ai_security_safety/): P2 maps directly onto agent-security engineering.
- [LCH502 Career Launch and Founder Studio](../../../../05_shared_years_3_to_5/LCH502_career_launch_and_founder_studio/README.md): research outputs become portfolio evidence for lab and evaluation roles.

## Sources

- METR time horizons and data file — https://metr.org/time-horizons/ and https://metr.org/assets/benchmark_results_1_1.yaml ; Kwa et al. (2025) — https://arxiv.org/abs/2503.14499 (checked 2026-10)
- Debenedetti et al., CaMeL (2025) — https://arxiv.org/abs/2503.18813 ; AgentDojo (2024) — https://arxiv.org/abs/2406.13352 ; Beurer-Kellner et al. (2025) — https://arxiv.org/abs/2506.08837 ; Meta, Agents Rule of Two (Oct 2025) — https://ai.meta.com/blog/practical-ai-agent-security/ (checked 2026-10)
- Starace et al., PaperBench (2025) — https://arxiv.org/abs/2504.01848 ; Wijk et al., RE-Bench (2024) — https://arxiv.org/abs/2411.15114 ; Liang et al., "The SWE-Bench Illusion" (2025) — https://arxiv.org/abs/2506.12286 (checked 2026-10)
- Wu et al., LongMemEval (2024) — https://arxiv.org/abs/2410.10813 ; Yao et al., τ-bench (2024) — https://arxiv.org/abs/2406.12045 ; Greenblatt et al., AI Control (2023) — https://arxiv.org/abs/2312.06942 ; Inspect — https://inspect.aisi.org.uk/ (checked 2026-10)
