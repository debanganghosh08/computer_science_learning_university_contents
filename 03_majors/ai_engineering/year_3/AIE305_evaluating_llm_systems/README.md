# AIE305 · Evaluating LLM Systems

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 3 · 6 | 4 (≈ 120 hours) | L1 → L3 | [CS214](../../../../02_year_2_core_computer_science/semester_4/CS214_machine_learning_foundations/README.md), [CS205](../../../../02_year_2_core_computer_science/semester_3/CS205_software_engineering_i_design_testing/README.md); assumes [FND116](../../../../01_year_1_foundations/semester_2/FND116_probability_and_statistics_i/README.md) and [AIE301](../AIE301_llm_fundamentals_for_engineers/README.md)–[AIE303](../AIE303_retrieval_augmented_generation_and_search/README.md) | [OV05 AI Security and Safety](../../../../04_overlaps/OV05_ai_security_safety/), [AIE403](../../year_4/AIE403_llmops_observability_guardrails_cost_and_latency/README.md), [AIE402](../../year_4/AIE402_fine_tuning_and_small_models_for_products/README.md), [OV12](../../../../04_overlaps/OV12_agent_infrastructure_platform/) |

## Why this course matters now

LLM output is open-ended and stochastic, so "it worked when I tried it" is not evidence. Evaluation is the skill that separates teams that improve from teams that guess. LinkedIn's generative AI team described the cost of slow evaluation: human annotators could review up to 500 conversations a day, and some metrics took three or more days per change (2024). Automated judges help, but they have measured biases. In the MT-Bench study, GPT-4 as a judge agreed with humans over 80% of the time, about as often as humans agree with each other, yet it showed position, verbosity and self-enhancement bias (Zheng et al., 2023). Public benchmarks are leaky too. On SWE-bench Verified, models identified the buggy file from the issue text alone up to 76% of the time, against up to 53% on repositories outside the benchmark, which points to memorisation (Liang et al., 2025). Evaluation tooling is now treated as strategic: OpenAI announced in March 2026 that it would acquire Promptfoo, an open-source eval and red-teaming tool. AI can write test cases, grade outputs and summarise failures. Deciding what "good" means for your users, checking that the grader agrees with people, and reading the evidence honestly is still your job.

## Learning outcomes

By the end you can:

1. **Run** an error analysis on raw traces (open coding → failure taxonomy → prioritised fixes) before choosing any metric.
2. **Build** a versioned golden set with labelling guidelines, stratification and measured inter-annotator agreement.
3. **Write** code-based graders (assertions, schema checks, execution checks) and **justify** when model-based grading is needed.
4. **Build** an LLM judge, **calibrate** it against human labels (true positive and true negative rates, κ), and **measure** its position, length and self-preference biases.
5. **Compare** two system versions with paired statistics, confidence intervals and adequate sample sizes, accounting for sampling variance.
6. **Operate** a regression eval suite in CI with thresholds, cost caps and deploy gates.
7. **Evaluate** RAG pipelines and agents (task success, trajectories, tool-call accuracy, pass^k, cost per success).
8. **Critique** a public benchmark claim for contamination, saturation, leaderboard gaming and construct validity.
9. **Plan** a scoped, authorised red-teaming exercise against your own system and turn its findings into regression tests (defensive only).

## Chapters and lessons

### Chapter 1 · Why evals, and what to measure (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 The eval-driven loop | Look at data → find failures → measure → change → re-measure; levels: unit assertions, model-graded, human review, online A/B (Husain, "Your AI Product Needs Evals", 2024) | Map the loop onto a real product feature of your choice |
| 1.2 Success criteria | Specific, measurable, achievable and relevant criteria; task fidelity, consistency, tone, latency, cost, safety (Anthropic, "Define success criteria") | Turn "the summary should be good" into five measurable criteria |
| 1.3 What can go wrong | Hallucination, omission, wrong format, unsafe content, refusal of valid requests, latency and cost regressions | Collect 30 real failures from a public demo or your AIE302 project and classify them |
| 1.4 Offline vs online | Pre-deploy test sets vs production monitoring; why both are needed | Design an eval plan with both layers for a support assistant |

**Check your understanding:** Why should error analysis come before choosing metrics? What is lost when you reduce quality to one number? Which criteria can be checked with code, and which need judgement?

### Chapter 2 · Error analysis (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Reading traces | Inputs, retrieved context, tool calls, outputs; building a simple annotation viewer | Build a one-page trace viewer; annotate 100 traces |
| 2.2 Open and axial coding | Free-text notes per failure, then grouping into categories; counting and prioritising (Husain, "A Field Guide to Rapidly Improving AI Products") | Produce a failure taxonomy with counts and examples |
| 2.3 Root causes | Spec gap vs prompt vs retrieval vs model vs tool vs data; fix the earliest stage | For the top 3 categories, propose and test one fix each |
| 2.4 Benevolent dictator labelling | One accountable domain expert for consistency early; when to add annotators | Write labelling guidelines that a second person can follow |

**Check your understanding:** Why do teams that skip error analysis often build the wrong metric? How many traces are enough to start a taxonomy? A failure category is rare but severe: how do you prioritise it?

### Chapter 3 · Golden sets and labelling (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Sampling | From logs (with consent and redaction), from documents, stratified by intent, language, difficulty and risk | Draw a stratified 200-case sample from a log export |
| 3.2 Synthetic data done carefully | Dimension grids (persona × scenario × constraint), adversarial and edge cases; checking realism against real traffic | Generate 100 cases from a grid; reject unrealistic ones by hand; record the rejection rate |
| 3.3 Agreement | Cohen's κ, Krippendorff's α, adjudication, ambiguous cases as a signal of spec gaps | Two annotators label 60 cases; compute κ; revise guidelines; repeat |
| 3.4 Dataset hygiene | Train/dev/test splits for prompts, versioning, leakage into prompts and few-shot examples, refresh cadence | Version the set; add a test that blocks any test case appearing in a prompt |

**Check your understanding:** Why does a synthetic test set often overestimate quality? What does a κ of 0.4 tell you about your task definition? How does a test case leak into a system, and why does it matter?

### Chapter 4 · Code-based graders (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Deterministic checks first | Exact match, normalised match, regex, JSON Schema, field-level F1, length and format rules | Write 15 assertions for an extraction task; measure coverage of the taxonomy |
| 4.2 Execution-based grading | Running generated code against tests, executing SQL and comparing result sets, checking tool calls against expected arguments | Grade 100 text-to-SQL outputs by execution, not string match |
| 4.3 Reference metrics and their limits | BLEU/ROUGE and embedding similarity; why they correlate poorly with quality on open-ended tasks | Show three cases where ROUGE ranks a worse answer higher |
| 4.4 Grader tests | Testing the graders themselves with known-good and known-bad outputs | Build a meta-test suite for your graders |

**Check your understanding:** When is exact match the right metric? Why grade SQL by execution? How do you know your grader is not the bug?

### Chapter 5 · LLM-as-judge (weeks 5–6)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Judge designs | Reference-based vs reference-free, binary pass/fail vs scales, pairwise comparison, rubric decomposition (G-Eval, Liu et al., 2023), panels of smaller judges (Verga et al., 2024) | Build binary and 1–5 judges for the same criterion; compare stability |
| 5.2 Known biases | Position, verbosity and self-enhancement (Zheng et al., 2023); self-preference correlated with self-recognition (Panickssery et al., 2024); length-controlled win rates (Dubois et al., 2024) | Measure position bias by swapping order on 100 pairs |
| 5.3 Calibration against humans | True positive and true negative rates on a labelled set; iterating the judge prompt; criteria drift as you read outputs (Shankar et al., 2024) | Calibrate a judge to ≥ 0.85 TPR and TNR on 80 human labels, or explain why you cannot |
| 5.4 Operating judges | Cost, latency, versioning the judge, re-calibration when the judge model changes | Re-run calibration after switching judge models; report the change |
| 5.5 When not to use a judge | High-stakes facts, maths, legal or medical correctness, anything checkable by code or by an expert | Write a policy listing which criteria may use a judge alone |

**Check your understanding:** Why do binary judges often beat 1–5 scales in practice? Your judge agrees 92% with humans, but humans marked 90% of cases as pass. Why is that number misleading? What changes when the system under test and the judge are the same model family?

### Chapter 6 · Statistics for evals (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Uncertainty | Standard errors and confidence intervals for accuracy; clustered questions (Miller, "Adding Error Bars to Evals", 2024) | Report a 95% CI for your system's accuracy on 200 cases |
| 6.2 Paired comparison | Paired differences, McNemar's test, bootstrap over cases | Decide whether v2 beats v1 with a paired bootstrap |
| 6.3 Sampling variance | Multiple samples per case; separating model randomness from question difficulty | Run each case 5 times; decompose the variance |
| 6.4 Sample size and power | How many cases to detect a 3-point change; multiple-comparison traps when testing many variants | Compute the sample size for your next experiment before running it |

**Check your understanding:** Two prompts score 81% and 83% on 150 cases. What can you claim? Why does testing 20 prompt variants and picking the best inflate results? When is a paired test more powerful than an unpaired one?

### Chapter 7 · Regression suites in CI (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Tools | promptfoo, UK AISI Inspect, OpenAI Evals, DeepEval; what each is good at | Implement the same 50-case suite in two tools |
| 7.2 Gating | Thresholds per criterion, blocking vs warning checks, cost caps, caching of unchanged cases | Add a GitHub Actions job that blocks merges below threshold |
| 7.3 Flakiness | Stochastic outputs, retry policies, tolerance bands, quarantining flaky cases | Measure each case's pass-rate stability over 10 runs; quarantine the unstable ones |
| 7.4 Reporting | Diff views between versions, failure examples next to scores, trend dashboards | Build a report that shows newly failing cases with their outputs |

**Check your understanding:** Why should a CI eval show failing examples and not only a score? How do you stop eval costs from growing with every pull request? What should happen when the model provider silently changes behaviour?

### Chapter 8 · Evaluating RAG and agents (weeks 9–10)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 RAG layers | Retrieval metrics vs generation metrics; faithfulness and answer relevance (Ragas, ARES); failure attribution | Evaluate your AIE303 system by layer; attribute 50 failures |
| 8.2 Agent outcomes | Task success checked by environment state, not the agent's claim; partial credit; cost per success (Kapoor et al., 2024) | Write state-based checkers for 20 agent tasks |
| 8.3 Reliability | pass@k vs pass^k (τ-bench); the gap as a product risk | Report pass@1 and pass^5 for your AIE304 agent |
| 8.4 Trajectories | Tool-call accuracy, redundant steps, policy violations, recovery from errors; simulated users (τ²-bench) | Grade 30 trajectories with a rubric; compare with outcome-only grading |
| 8.5 Building rigorous agent benchmarks | Task validity and outcome validity checklists (Zhu et al., 2025); environment resets; leakage | Audit one public agent benchmark against the checklist |

**Check your understanding:** An agent's final answer is right but it deleted a file on the way. Pass or fail? Why can outcome-only grading reward lucky trajectories? How would you simulate a difficult customer reproducibly?

### Chapter 9 · Benchmarks and their pitfalls (week 11)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Reading benchmarks | What MMLU, GPQA, Humanity's Last Exam, SWE-bench Verified, Terminal-Bench and BrowseComp measure; construct validity | For one benchmark, write what a high score does and does not imply for your product |
| 9.2 Contamination | Training-data overlap; GSM1k showed accuracy drops of up to 8% on fresh, similar problems (Zhang et al., 2024); memorisation signals on SWE-bench Verified (Liang et al., 2025) | Design a contamination check for your own private eval |
| 9.3 Arenas and leaderboards | Human-preference arenas (Chiang et al., 2024); private testing and data-access asymmetries ("The Leaderboard Illusion", 2025) | Write a critique of a recent leaderboard headline |
| 9.4 Saturation and harness effects | Scores near the ceiling; how harness, prompt and tool choices change agent scores; HELM's multi-metric reporting | Run one task set under two harnesses; report the difference |

**Check your understanding:** Why can a model's benchmark score rise without any change in your product's quality? What is the minimum you need to know about a harness before comparing two agent scores? How would you keep your own eval set from leaking into future training data?

### Chapter 10 · Human evaluation and online experiments (week 12)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Expert review | Side-by-side reviews, rubrics, annotation throughput and cost; LinkedIn's 500 conversations/day example | Run a blind side-by-side with three reviewers; compute agreement |
| 10.2 Online metrics | Task completion, escalation rate, edits to AI drafts, retention; guardrail metrics (latency, cost, complaints) | Define five online metrics precisely, including denominators |
| 10.3 A/B testing LLM features | Randomisation unit, novelty effects, sample ratio mismatch, long-term vs short-term effects | Plan an A/B test with power analysis and stopping rules |
| 10.4 Feedback biases | Thumbs-up/down response bias, silent failures, survivorship | List three ways users' feedback misleads; propose a correction for each |

**Check your understanding:** Why might offline quality improve while online metrics fall? What does "edits to AI drafts" tell you that thumbs do not? When should a human evaluation replace an automated one?

### Chapter 11 · Red-teaming basics (week 13)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Purpose and rules | Authorised, scoped testing of your own system; written scope, data handling and disclosure; harm taxonomies (MLCommons AILuminate hazards, NIST AI 600-1 risk list) | Write a red-team plan for your P2 system, signed off by the instructor |
| 11.2 Categories of risk | OWASP Top 10 for LLM Applications 2025 (prompt injection, sensitive information disclosure, excessive agency, misinformation, unbounded consumption and others) | Map each OWASP item to a test category for your system (no payloads) |
| 11.3 Automated scanning | Running open-source scanners (garak, PyRIT) and AgentDojo only against your own sandboxed system; triaging findings | Run one scanner; triage results into true and false positives |
| 11.4 From findings to regressions | Each confirmed finding becomes a test; severity, owner, fix verification | Convert five findings into CI regression tests |

**Check your understanding:** Why must red-teaming start with written scope and authorisation? What makes a finding reproducible enough to fix? Why do safety regressions need the same CI treatment as quality regressions?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Success criteria workshop | Eval plan |
| 2 | 2 | Lab 1 (cont.): Trace viewer and failure taxonomy | — |
| 3 | 3 | Lab 2 · Golden set with κ | **P1 due** |
| 4 | 4 | Lab 3 · Code graders and execution grading | — |
| 5 | 5 | Lab 4 · Judge biases | — |
| 6 | 5 | Lab 4 (cont.): judge calibration | Mid-term (AI off): statistics and judge design |
| 7 | 6 | Lab 5 · Paired comparisons and power | — |
| 8 | 7 | Lab 6 · CI eval gate | **P2 due** |
| 9 | 8 | Lab 7 · RAG layer evaluation | — |
| 10 | 8 | Lab 7 (cont.): agent pass^k and trajectories | — |
| 11 | 9 | Lab 8 · Benchmark critique and contamination check | Critique essay |
| 12 | 10 | Lab 9 · Side-by-side human eval and A/B plan | — |
| 13 | 11 | Lab 10 · Scoped red-team of your own system | Findings → tests |
| 14 | Integration | P3 demo day | **P3 due** |
| 15 | Review | Oral defence of P3 | Final exam (AI off) |

## Working with AI in this course

- **Use AI for:** generating candidate test cases from a dimension grid; drafting judge prompts and rubrics; clustering free-text failure notes; writing eval harness code with Claude Code, Cursor or Copilot; summarising long traces for a first pass.
- **Do without AI (drills):** hand-label at least 150 outputs across the semester; compute a confidence interval and a paired bootstrap on paper or in a spreadsheet; write a failure taxonomy from 50 traces; design a judge rubric from a product spec; critique a benchmark claim in a timed essay.
- **Verify AI output by:** calibrating every judge against your human labels before use and after every judge-model change; checking synthetic cases against real-traffic distributions; reading at least 20 raw failures per experiment; re-computing headline statistics independently.
- **Where AI still fails here (show it):** judges favour longer answers and the first option shown (measure both in Lab 4); judges from the same family favour their own outputs; generated test cases are easier and less diverse than real ones (compare difficulty in Lab 2); assistants report "significant improvements" from differences inside the noise (catch one in Lab 5).

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (10, each with data and analysis) | 25% |
| Projects P1–P3 | 35% |
| Golden set, judge calibration report, benchmark critique | 10% |
| Mid-term (AI off) | 10% |
| Final exam (AI off) + oral defence of P3 | 20% |

**Mastery gate.** You pass when you can: (1) given an unfamiliar LLM feature and 200 production traces, deliver in one working day a failure taxonomy, a 100-case golden set with κ ≥ 0.6, and a calibrated judge with reported TPR and TNR; (2) decide correctly, with a paired test and a confidence interval, whether a proposed change is an improvement; (3) read a vendor or paper benchmark claim and state, in writing, three specific threats to its validity.

## Industry reality

Evaluation is where AI products succeed or stall. DoorDash runs an LLM judge over five aspects of its support answers (2024), and LinkedIn reported building model-based evaluators because human review alone took a day or more per change (2024). Open-source tools are mainstream: promptfoo for CI assertions and red-teaming (OpenAI announced its acquisition in March 2026), Inspect from the UK AI Security Institute, OpenAI Evals and DeepEval. Agent benchmarks such as SWE-bench Verified, τ²-bench and Terminal-Bench 2.0 are standard reference points, alongside published evidence of contamination and leaderboard distortion. Governance frameworks expect evaluation evidence: NIST's Generative AI Profile (AI 600-1, July 2024) lists measurement actions across its risk categories. India's AI Governance Guidelines (Nov 2025) also emphasise accountability and risk management, which in practice means test evidence.

**Interview questions from this course**

1. *How would you evaluate a new LLM-powered support assistant before launch?* Strong answer: error analysis on pilot traces; success criteria with the product owner; stratified golden set with agreement checks; code graders where possible and calibrated judges elsewhere; RAG layer metrics; red-team pass; thresholds agreed in advance; online metrics and guardrails after launch.
2. *Can we just use GPT or Claude as the judge?* Strong answer: yes for some criteria, after calibration against human labels (TPR and TNR, not raw agreement); mitigate position and length bias; avoid same-family judging where possible; never as sole judge for high-stakes correctness; re-calibrate on judge-model change.
3. *Version B scored 2 points higher. Ship it?* Strong answer: asks for sample size, the confidence interval of the paired difference, variance across samples, per-segment breakdown (languages, intents), cost and latency changes, and whether the eval set leaked into prompts.
4. *How do you evaluate an agent?* Strong answer: environment-state checks, pass^k for reliability, cost per success, trajectory rubrics for safety and efficiency, simulated users, hidden tests to prevent reward hacking; benchmark results treated with harness and contamination caveats.
5. *A model tops a leaderboard. Should we switch?* Strong answer: explains contamination, arena distortions and harness effects; runs the candidate on the team's own golden set with the production harness; compares cost, latency and failure modes; then a shadow or A/B test.

## Resources (free first)

- **Practitioner guides:** Hamel Husain, "Your AI Product Needs Evals" — https://hamel.dev/blog/posts/evals/ ; "Using LLM-as-a-Judge for Evaluation" — https://hamel.dev/blog/posts/llm-judge/ ; "A Field Guide to Rapidly Improving AI Products" — https://hamel.dev/blog/posts/field-guide/ ; Eugene Yan, "Evaluating the Effectiveness of LLM-Evaluators" — https://eugeneyan.com/writing/llm-evaluators/ ; Anthropic, "Define success criteria and build evaluations" — https://platform.claude.com/docs/en/test-and-evaluate/develop-tests ; Anthropic, "A statistical approach to model evaluations" — https://www.anthropic.com/research/statistical-approach-to-model-evals
- **Tools:** promptfoo — https://github.com/promptfoo/promptfoo ; Inspect — https://inspect.aisi.org.uk/ ; OpenAI Evals — https://github.com/openai/evals ; DeepEval — https://github.com/confident-ai/deepeval ; lm-evaluation-harness — https://github.com/EleutherAI/lm-evaluation-harness ; Ragas — https://github.com/vibrantlabsai/ragas ; garak — https://github.com/NVIDIA/garak ; PyRIT — https://github.com/Azure/PyRIT
- **Benchmarks:** SWE-bench — https://www.swebench.com/ ; τ²-bench — https://github.com/sierra-research/tau2-bench ; Terminal-Bench — https://www.tbench.ai/ ; HELM — https://crfm.stanford.edu/helm/ ; MLCommons AILuminate — https://mlcommons.org/ailuminate/
- **Frameworks and standards:** OWASP Top 10 for LLM Applications 2025 — https://genai.owasp.org/llm-top-10/ ; NIST AI RMF — https://www.nist.gov/itl/ai-risk-management-framework ; NIST AI 600-1 — https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf
- **Paid, optional:** Chip Huyen, *AI Engineering* (O'Reilly, 2025), chapters 3–4 on evaluation.

## Sources

- LinkedIn Engineering, "Musings on building a Generative AI product" (25 Apr 2024) — https://www.linkedin.com/blog/engineering/generative-ai/musings-on-building-a-generative-ai-product (checked 2026-10)
- Zheng et al., "Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena" (2023) — https://arxiv.org/abs/2306.05685 ; Liu et al., G-Eval (2023) — https://arxiv.org/abs/2303.16634 ; Panickssery et al. (2024) — https://arxiv.org/abs/2404.13076 ; Dubois et al., length-controlled AlpacaEval (2024) — https://arxiv.org/abs/2404.04475 ; Verga et al., panels of judges (2024) — https://arxiv.org/abs/2404.18796 ; Shankar et al. (2024) — https://arxiv.org/abs/2404.12272 (checked 2026-10)
- Miller, "Adding Error Bars to Evals" (2024) — https://arxiv.org/abs/2411.00640 (checked 2026-10)
- Liang et al., "The SWE-Bench Illusion" (2025) — https://arxiv.org/abs/2506.12286 ; Zhang et al., GSM1k (2024) — https://arxiv.org/abs/2405.00332 ; Singh et al., "The Leaderboard Illusion" (2025) — https://arxiv.org/abs/2504.20879 ; Chiang et al., Chatbot Arena (2024) — https://arxiv.org/abs/2403.04132 ; Liang et al., HELM (2022) — https://arxiv.org/abs/2211.09110 (checked 2026-10)
- Hendrycks et al., MMLU (2020) — https://arxiv.org/abs/2009.03300 ; Rein et al., GPQA (2023) — https://arxiv.org/abs/2311.12022 ; Phan et al., Humanity's Last Exam (2025) — https://arxiv.org/abs/2501.14249 ; Wei et al., BrowseComp (2025) — https://arxiv.org/abs/2504.12516 ; Merrill et al., Terminal-Bench (2026) — https://arxiv.org/abs/2601.11868 (checked 2026-10)
- Yao et al., τ-bench (2024) — https://arxiv.org/abs/2406.12045 ; Barres et al., τ²-bench (2025) — https://arxiv.org/abs/2506.07982 ; Kapoor et al. (2024) — https://arxiv.org/abs/2407.01502 ; Zhu et al., "Establishing Best Practices for Building Rigorous Agentic Benchmarks" (2025) — https://arxiv.org/abs/2507.02825 (checked 2026-10)
- Es et al., Ragas (2023) — https://arxiv.org/abs/2309.15217 ; Saad-Falcon et al., ARES (2023) — https://arxiv.org/abs/2311.09476 ; Debenedetti et al., AgentDojo (2024) — https://arxiv.org/abs/2406.13352 (checked 2026-10)
- OpenAI, "OpenAI to acquire Promptfoo" (9 Mar 2026; completion not confirmed in a primary source) — https://openai.com/index/openai-to-acquire-promptfoo/ (checked 2026-10)
- DoorDash, LLM-based Dasher support automation (Sept 2024) — https://careersatdoordash.com/blog/large-language-modules-based-dasher-support-automation/ (checked 2026-10)
- NIST AI 600-1 (26 Jul 2024) — https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf ; OWASP Top 10 for LLM Applications 2025 — https://genai.owasp.org/llm-top-10/ ; India AI Governance Guidelines (Nov 2025) — https://static.pib.gov.in/WriteReadData/specificdocs/documents/2025/nov/doc2025115685601.pdf (checked 2026-10)

_Last reviewed: 2026-10_
