# AIE305 · Labs and projects

Every lab and project ships the dataset (with version and labelling guide), the grader code or judge prompt, raw outputs, and an analysis notebook that recomputes every headline number. Any comparison reports a confidence interval. Red-teaming work is done only against systems you own or are explicitly authorised to test, inside a sandbox, with a written scope.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Success criteria, trace viewer and failure taxonomy | Turn a vague product goal into measurable criteria; build a one-page trace viewer; annotate 100 traces and build a taxonomy with counts | Criteria document, viewer code, taxonomy with examples and priorities | 6 h |
| 2 · Golden set with agreement | Draw a stratified 200-case sample; generate 100 synthetic cases from a dimension grid and reject unrealistic ones; two annotators label 60 cases | Versioned set, rejection rate, κ before and after guideline revision | 5 h |
| 3 · Code graders and execution grading | Write 15 assertions for an extraction task; grade 100 text-to-SQL outputs by execution; meta-test your graders | Grader code, meta-tests, three cases where ROUGE misranks | 4 h |
| 4 · Judge biases and calibration | Measure position bias (swap order on 100 pairs) and length bias; calibrate a binary judge on 80 human labels; re-calibrate after switching judge model | Bias measurements, TPR/TNR before and after iteration, judge-change report | 7 h |
| 5 · Paired comparisons and power | Report 95% CIs; compare two versions with a paired bootstrap and McNemar's test; decompose sampling variance; compute sample size for a 3-point effect | Notebook, a one-paragraph decision with evidence | 4 h |
| 6 · CI eval gate | Implement a 50-case suite in two tools (promptfoo, Inspect, DeepEval or OpenAI Evals); add a GitHub Actions gate with thresholds, caching and a cost cap; quarantine flaky cases | Workflow file, run history, flakiness report | 5 h |
| 7 · RAG and agent evaluation | Evaluate an AIE303 pipeline by layer; write state-based checkers for 20 agent tasks; report pass@1 and pass^5; grade 30 trajectories with a rubric | Layer metrics, failure attribution, reliability numbers, rubric agreement | 7 h |
| 8 · Benchmark critique and contamination check | Audit one public agent benchmark against a rigour checklist; design a contamination check for a private set | Critique essay (≤ 1,500 words) and the check | 4 h |
| 9 · Human side-by-side and A/B plan | Blind side-by-side with three reviewers; define five online metrics with denominators; plan an A/B test with power and stopping rules | Agreement stats, metric spec, experiment plan | 4 h |
| 10 · Scoped red-team of your own system | Write a scoped plan mapped to the OWASP LLM Top 10; run garak or PyRIT against your own sandboxed app; triage; turn five findings into regression tests | Signed scope, triaged findings, tests in CI | 5 h |

## Projects

### P1 · Error analysis and a golden set for a real LLM feature (L1, ~6 hours)

**Real-world inspiration.** Practitioners repeatedly report that looking at real outputs and building a failure taxonomy beats starting from generic metrics (Husain, "Your AI Product Needs Evals", 2024, and "A Field Guide to Rapidly Improving AI Products"). LinkedIn's team tracked quality, hallucination rate, responsible-AI violations, coherence and style with daily human annotation (2024).

**What to build.** Pick one LLM feature you can run: your AIE302 triage prompt, your AIE303 RAG system, or an open-source app. Collect 150 traces from realistic inputs. Build a failure taxonomy, then a versioned 120-case golden set stratified by the taxonomy, with a labelling guide.

**Acceptance criteria**
- Taxonomy with at least 6 categories, counts, and two examples each, built from open-coded notes (submitted).
- Golden set covers every category with at least 8 cases; a hidden test split of 40 cases.
- Two annotators label 50 cases; κ ≥ 0.6, or a documented revision cycle that reaches it.
- A one-page priority list: which category to fix first and why (frequency × severity × cost to fix).

**Stretch goals.** Add 40 synthetic cases from a dimension grid and show how their difficulty differs from real ones.

**What it proves to an employer.** You start from data, not from vanity metrics, and can build an evaluation asset a team can trust.

### P2 · A calibrated judge and a regression gate (L2, ~15 hours)

**Real-world inspiration.** DoorDash's support system uses an LLM judge over five aspects (retrieval correctness, response accuracy, grammar, coherence and relevance) (2024). The MT-Bench study found GPT-4 judges agree with humans over 80% of the time, but with position, verbosity and self-enhancement biases (Zheng et al., 2023). Promptfoo, an open-source eval tool OpenAI announced it would acquire in March 2026, and the UK AI Security Institute's Inspect are widely used for CI evals.

**What to build.** For your P1 feature: judges for three criteria (for example faithfulness, policy compliance, tone), each calibrated against at least 80 human labels; bias measurements; and a CI regression suite in GitHub Actions that runs code graders and judges on every change, compares with the main branch using paired statistics, and blocks merges below threshold.

**Acceptance criteria**
- Each judge reports TPR and TNR on a held-out human-labelled set; at least two judges reach ≥ 0.85 on both, and the third has a documented reason and mitigation.
- Position bias measured (order-swap flip rate) and reduced by a stated mitigation; length bias measured.
- The CI job posts a report with per-criterion scores, CIs, and newly failing examples with outputs.
- A planted regression (prompt change that breaks one category) is caught and blocks the merge; an unchanged run passes 10 times in a row (flakiness under control).
- Cost per CI run is capped and reported.

**Stretch goals.** A panel of small judges vs one large judge; automatic re-calibration when the judge model changes.

**What it proves to an employer.** You can make quality a release criterion with automated, validated graders. This is the bottleneck in most AI teams.

### P3 · An evaluation programme for an agent or RAG product (L3, portfolio-grade, ~30 hours)

**Real-world inspiration.** OpenAI built SWE-bench Verified by having 93 professional developers screen 1,699 samples down to 500 (Aug 2024), and later research found memorisation signals on it (Liang et al., 2025). τ-bench introduced pass^k to capture reliability (2024). Governance frameworks such as NIST AI 600-1 expect documented measurement. The product below is your own; the programme design is what matters.

**What to build.** A complete evaluation programme for your AIE304 agent or AIE303 RAG system, documented like a model card plus an eval report: offline layered evals (component and end-to-end), agent reliability (pass^k, cost per success, trajectory rubric), a contamination-resistant private test set with a refresh plan, a calibrated judge suite in CI, a scoped red-team with findings turned into tests, an online monitoring plan (sampled judges, drift, canaries), and a statistical plan for future comparisons.

**Acceptance criteria**
- At least 250 offline cases across strata, with a stratum-level results table and CIs.
- For an agent: pass^5 reported on ≥ 20 tasks with state-based checkers; for RAG: retrieval and generation metrics per stratum.
- At least 10 red-team findings triaged, with 5 converted into CI tests (scope document signed by the instructor).
- A benchmark-validity self-audit using a published checklist (Zhu et al., 2025) with every item answered.
- An external reviewer (another student) reproduces your headline numbers from the repository in under 2 hours.

**Stretch goals.** Port the suite to Inspect and publish it openly; add a human side-by-side study for one criterion.

**What it proves to an employer.** You can design evaluation that leadership, auditors and engineers all rely on. Eval leads and AI quality roles are built around this.

## Feeds into

- [OV05 AI Security and Safety Engineering](../../../../04_overlaps/OV05_ai_security_safety/): red-teaming, safety evals and governance build directly on Labs 4 and 10 and P3.
- [AIE403 LLMOps](../../year_4/AIE403_llmops_observability_guardrails_cost_and_latency/README.md): online evaluation, canaries and release gates.
- [AIE402 Fine-Tuning and Small Models](../../year_4/AIE402_fine_tuning_and_small_models_for_products/README.md): equal-cost comparisons and regression suites for fine-tunes.
- [OV12B Agent Evaluation and Reliability Engineering](../../../../04_overlaps/OV12_agent_infrastructure_platform/OV12B_agent_evaluation_and_reliability_engineering/README.md): agent evaluation at platform scale.

## Sources

- Husain, "Your AI Product Needs Evals" (Mar 2024) — https://hamel.dev/blog/posts/evals/ ; "A Field Guide to Rapidly Improving AI Products" — https://hamel.dev/blog/posts/field-guide/ (checked 2026-10)
- LinkedIn Engineering (Apr 2024) — https://www.linkedin.com/blog/engineering/generative-ai/musings-on-building-a-generative-ai-product ; DoorDash (Sept 2024) — https://careersatdoordash.com/blog/large-language-modules-based-dasher-support-automation/ (checked 2026-10)
- Zheng et al. (2023) — https://arxiv.org/abs/2306.05685 ; Liang et al. (2025) — https://arxiv.org/abs/2506.12286 ; Yao et al., τ-bench (2024) — https://arxiv.org/abs/2406.12045 ; Zhu et al. (2025) — https://arxiv.org/abs/2507.02825 (checked 2026-10)
- OpenAI, "Introducing SWE-bench Verified" (Aug 2024) — https://openai.com/index/introducing-swe-bench-verified/ ; OpenAI, "OpenAI to acquire Promptfoo" (Mar 2026) — https://openai.com/index/openai-to-acquire-promptfoo/ ; Inspect — https://inspect.aisi.org.uk/ (checked 2026-10)
- NIST AI 600-1 — https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf ; OWASP LLM Top 10 2025 — https://genai.owasp.org/llm-top-10/ ; garak — https://github.com/NVIDIA/garak ; PyRIT — https://github.com/Azure/PyRIT (checked 2026-10)
