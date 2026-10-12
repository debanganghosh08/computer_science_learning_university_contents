# SWE501 · Frontier Seminar: Agentic Software Engineering and Program Synthesis

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 5 · 9 | 4 (≈ 120 hours) | L4 → L5 | [SWE401](../../year_4/SWE401_large_scale_system_design/README.md), [SWE403](../../year_4/SWE403_reliability_observability_and_incident/README.md); strongly recommended [SWE304](../../year_3/SWE304_ai_assisted_software_engineering_agents/README.md) and [CSG401](../../../computer_science_general/year_4/CSG401_formal_methods_and_program_verification/README.md); taken with [RES501](../../../../05_shared_years_3_to_5/RES501_research_methods_and_scientific_writing/README.md) | [RES502](../../../../05_shared_years_3_to_5/RES502_reading_reproducing_and_extending_papers/README.md), [THS501](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md)/[THS502](../../../../05_shared_years_3_to_5/THS502_thesis_or_capstone_ii/README.md) |

## Why this course matters now

In five years, automatic code generation went from completing functions (HumanEval, 2021) to agents that resolve real GitHub issues, run for hours and open pull requests. METR estimates that the length of software task frontier models complete at 50% reliability has been doubling every few months; Claude Opus 4.6 reached about 12 hours of expert work at 50% success in February 2026, but only about 70 minutes at 80%. The evaluation science is struggling to keep up. In February 2026 OpenAI stopped reporting SWE-bench Verified, saying many of its hardest problems had flawed tests and that models could reproduce original fixes from memory, and recommended SWE-bench Pro. New benchmarks such as NL2Repo-Bench (generate a whole installable library from a requirements document; best agents below 40% test pass rate) and DeepSWE (113 original long-horizon tasks, built to avoid memorised GitHub fixes) try to measure longer, less contaminated work. Underneath all of it sits an old question with new urgency: how do we know a program is correct when nobody wrote it by hand? This seminar takes you to the research frontier: benchmarks and their validity, agent architectures and training, verification by testing and by proof, human factors, and security. You will reproduce a published result, extend it, and write it up at workshop quality.

## Learning outcomes

By the end you can:

1. **Trace** the lineage from deductive and inductive program synthesis to neural code models and software engineering agents, and **place** a new paper in it.
2. **Critique** a benchmark: construction, contamination risk, test adequacy, grader error, and what a score does and does not mean.
3. **Explain** and **compare** agent designs (agent–computer interfaces, fixed pipelines, sampling with verifier selection) and training methods (execution-feedback environments, synthetic task generation).
4. **Evaluate** verification approaches for AI-generated code: generated tests, mutation and property-based testing, differential testing, fuzzing, and formal proof in Dafny, Verus or Lean.
5. **Design** an empirical study of AI-assisted development that controls for selection, task choice and perception bias.
6. **Analyse** the security of coding agents (prompt injection, sandboxing, package hallucination) from a defensive research perspective.
7. **Reproduce** a published result within stated error, **extend** it with a new experiment, and **write** a workshop-quality paper with an artefact others can rerun.

## Chapters and lessons

### Chapter 1 · From program synthesis to code models (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Deductive and inductive synthesis | Synthesis from specifications; programming by example; FlashFill (Gulwani, POPL 2011) shipped in Excel | Implement a tiny enumerative synthesiser for string transformations |
| 1.2 Neural code generation | Codex and HumanEval (Chen et al., 2021); MBPP (Austin et al., 2021); pass@k and its estimator | Compute unbiased pass@k for a small model's samples |
| 1.3 Competition-level generation | AlphaCode (Li et al., 2022): massive sampling plus filtering and clustering | Reproduce sampling-then-filtering on 20 easy contest problems |
| 1.4 Reading a paper in this field | Claims, setup, baselines, ablations, threats to validity | One-page structured review of a recent paper |

**Check your understanding:** Why does pass@k reward sampling, and when is that misleading for real use? What did programming-by-example get right that LLMs still struggle with? Which parts of AlphaCode's pipeline are about verification rather than generation?

### Chapter 2 · Benchmarks and their validity (weeks 2–3)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 SWE-bench and its family | SWE-bench (Jimenez et al., ICLR 2024), Verified, Multimodal, Live, Pro (Deng et al., 2025); SWE-Lancer's dollar-valued tasks | Run one agent on 20 SWE-bench Lite/Verified tasks; inspect every "pass" |
| 2.2 Contamination | Memorisation of public fixes ("The SWE-Bench Illusion", Liang et al., 2025); OpenAI's Feb 2026 audit and decision | Design a contamination probe (file-path recall, verbatim fix reproduction) and run it |
| 2.3 Test adequacy and grading | Weak hidden tests; correct alternatives graded wrong; patch overfitting (Smith et al., FSE 2015, "Is the cure worse than the disease?") | Find a passing but wrong patch, and a correct but failing patch, in a benchmark run |
| 2.4 Longer horizons | METR time horizons (Kwa et al., 2025); NL2Repo-Bench; DeepSWE; Terminal-Bench | Compare what each measures; write the threats-to-validity section for one |

**Check your understanding:** Why can a benchmark score rise while real capability does not? What would convince you a model had not memorised a task's fix? Why is "the hidden tests pass" not the same as "the issue is resolved"?

### Chapter 3 · Agent architectures (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Agent–computer interfaces | SWE-agent (Yang et al., NeurIPS 2024): tool design as a first-class variable | Ablate one ACI tool (search or file viewer) and measure the effect |
| 3.2 Platforms | OpenHands (Wang et al., ICLR 2025) as an open research platform | Reproduce one OpenHands configuration on a small task set |
| 3.3 Fixed pipelines | Agentless (Xia et al., 2024): localise, repair, validate, with no free-form agent loop | Compare Agentless-style and agentic runs on the same tasks: success, cost, variance |
| 3.4 Test-time scaling | Multiple samples, verifier or test-based selection, self-consistency; cost curves | Plot success vs number of samples with and without a selector |

**Check your understanding:** Why can a simpler pipeline match a complex agent? What is the cost-optimal number of samples for your setup, and why? Which interface change gave the largest effect in your ablation?

### Chapter 4 · Training software engineering agents (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Execution environments | SWE-Gym (Pan et al., 2024): real repositories with runnable tests for training and verifiers | Build 10 executable task environments from a repository's history |
| 4.2 Synthetic task generation | SWE-smith (Yang et al., 2025): generating bug-fix tasks at scale | Generate 50 synthetic tasks by mutating a repo; check that tests detect each |
| 4.3 Reward hacking | Agents special-casing tests or editing graders; METR's 2025 observations | Design a grader that resists three known hacks; test it |
| 4.4 Data provenance | Licences, consent, contamination between training and evaluation | Write a data card for your Chapter 4 task set |

**Check your understanding:** Why does execution feedback make reward hacking more likely, not less? What makes a synthetic bug realistic? How would you keep your evaluation set out of future training data?

### Chapter 5 · Verification I: tests, mutation, fuzzing (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 LLM test generation in industry | Meta's TestGen-LLM (assured improvement filters) and mutation-guided generation (ACH) | Reimplement the filter pipeline (builds, passes repeatedly, adds coverage) on an open project |
| 5.2 Properties and oracles | LLM-proposed properties; differential testing against a reference | Have a model propose properties for a library; validate them against known bugs |
| 5.3 Fuzzing with LLMs | AI-generated fuzz targets in OSS-Fuzz (Google, Nov 2024) | Generate fuzz targets for an uncovered C library function; measure new coverage |
| 5.4 Patch correctness | Overfitting in automated repair; independent test suites; human judgement studies | Assess 20 agent patches with an independent test suite you write |

**Check your understanding:** Why do generated tests that "increase coverage" not guarantee they check anything? What is an oracle problem, and how do properties help? Why are fuzzers good at finding crashes and weak at finding wrong answers?

### Chapter 6 · Verification II: formal methods meet LLMs (weeks 7–8)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Verification-aware languages | Dafny, Verus (Rust), F*, Lean 4; specifications, invariants, termination | Verify binary search and a bounded queue in Dafny |
| 6.2 LLMs writing proofs | Baldur (First et al., 2023), LeanDojo (Yang et al., 2023), DafnyBench (Loughridge et al., 2024), AlphaVerus (Aggarwal et al., 2024), VERINA (Ye et al., 2025) | Run a model on 20 DafnyBench tasks; classify failures |
| 6.3 Specifications from intent | nl2postcond (Endres et al., 2023); Clover's consistency checks between code, spec and docs (Sun et al., 2023) | Generate postconditions from docstrings; measure how many catch planted bugs |
| 6.4 Industry practice | AWS's use of TLA+ (Newcombe et al., 2015); Cedar's verification-guided development (Cutler et al., 2024) | Write a one-page case analysis: what was proved, what was tested, what was assumed |

**Check your understanding:** If an LLM writes both the code and the specification, what has been verified? Why is specification the bottleneck rather than proof search? What trust does a proof checker give you that a test suite cannot?

### Chapter 7 · Repair, migration and translation research (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Automated program repair | GenProg (Le Goues et al., 2012) to LLM-based repair; overfitting | Compare a search-based and an LLM-based repair on 10 bugs |
| 7.2 Migration at scale | Google's experience report (2025); what "80% AI-authored" does and does not show | Write a methods critique of the report |
| 7.3 Translation and equivalence | C to Rust (C2Rust, DARPA TRACTOR, LLM-assisted idiomatic translation); differential testing and equivalence checking | Translate a small C module; check equivalence with differential fuzzing |
| 7.4 Repair benchmarks and maintainers | Defects4J-style benchmarks; whether maintainers accept machine patches, and why they reject them | Submit 3 agent-assisted fixes to open-source projects (with disclosure); record the maintainers' responses |

**Check your understanding:** Why is translating to idiomatic code harder than translating to equivalent code? What evidence would show a migration tool is safe to run unattended? How would you measure "idiomatic"?

### Chapter 8 · Human factors and productivity science (week 10)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Controlled trials | Peng et al. (2023), Paradis et al. (2024), METR (2025) and its 2026 redesign; field experiments (Cui et al.) | Compare designs: participants, tasks, outcome measures, blinding |
| 8.2 Perception and selection | Predicted vs measured speed-up; developers withholding tasks from no-AI arms | Propose a design that handles selection effects |
| 8.3 Usage-based evidence | Anthropic Economic Index (task success and automation share); survey data (Stack Overflow, DORA) | Reanalyse a public dataset (Anthropic Economic Index release) for software tasks |
| 8.4 Skill formation and security behaviour | Learning penalties under heavy AI use; Perry et al. on overconfidence in insecure code | Design a study on review skill retention under agent use |

**Check your understanding:** Why might the same tool produce speed-ups in one trial and slow-downs in another? What can usage data show that trials cannot, and the reverse? How would you measure skill atrophy ethically?

### Chapter 9 · Security of coding agents (week 11)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Insecure generated code | Pearce et al. (2021), Perry et al. (2022), Veracode (2025): methods and limits | Replicate a small CWE-scenario study with a current model |
| 9.2 Supply-chain risks | Package hallucination (Spracklen et al., USENIX Security 2025) | Measure hallucinated package rates for two models on 200 prompts |
| 9.3 Prompt injection and containment | Untrusted inputs to agents; sandboxing and permission research; evaluation of defences (defensive only, in sandboxes) | Evaluate one containment design against a fixed set of injected instructions in a sandbox |
| 9.4 The utility cost of safety | Least-privilege policies, approval prompts and audit logs; measuring how much task success a restriction costs | Measure task success on 20 tasks with and without network egress and write access outside the repo |

**Check your understanding:** Why is prompt injection hard to solve with better prompts alone? What makes a hallucinated package an attack vector? How should a defence paper report results to be convincing?

### Chapter 10 · Open problems and the research workshop (weeks 12–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Open problems | (1) Contamination-resistant evaluation; (2) semantic correctness beyond tests; (3) specification inference and agents that ask clarifying questions; (4) maintainability of agent-written code over time; (5) cost-optimal test-time compute; (6) verified migrations and translations; (7) agent security; (8) skill formation in human–agent teams; (9) design-level reasoning (architecture, trade-offs) | Pick one; write a 2-page proposal with a falsifiable hypothesis |
| 10.2 Reproduction | Rerunning a paper's main result; documenting deviations | P2 |
| 10.3 Extension and writing | New experiment, analysis, related work, limitations, artefact | P3 |
| 10.4 Peer review and talks | Conference-style reviewing (summary, strengths, weaknesses, questions, score); 15-minute research talks | Review two peers' drafts; give your talk and answer questions |

**Check your understanding:** What result would falsify your hypothesis? Which threat to validity worries you most, and what did you do about it? What would someone need to rerun your experiment?

## Weekly rhythm

| Week | Chapter | Seminar activity | Deliverable |
|---|---|---|---|
| 1 | 1 | Paper review practice | Review 1 |
| 2 | 2 | Benchmark teardown | — |
| 3 | 2 | Contamination probes | **P1 due** (benchmark audit) |
| 4 | 3 | Agent ablations | Review 2 |
| 5 | 4 | Environments and graders | — |
| 6 | 5 | Test generation and fuzzing | Review 3 |
| 7 | 6 | Dafny and Verus | — |
| 8 | 6 | LLM proof generation | Proposal draft |
| 9 | 7 | Repair and translation | — |
| 10 | 8 | Study design workshop | **P2 due** (reproduction) |
| 11 | 9 | Agent security (sandboxed) | — |
| 12 | 10 | Writing workshop | Full draft |
| 13 | 10 | Peer review (conference-style) | Reviews of two peers' drafts |
| 14 | 10 | Talks | **P3 due** (paper + artefact) |
| 15 | Review | Oral defence | Final oral exam |

## Working with AI in this course

- **Use AI for:** literature search and summarisation (then read the paper); writing experiment scaffolding and analysis scripts; generating candidate properties, specifications and proofs as research subjects; drafting related-work paragraphs that you then verify citation by citation.
- **Do without AI (drills):** structured paper reviews; the threats-to-validity sections; your own proofs of the warm-up Dafny exercises; peer reviews; the oral exam. Research judgement is the skill under assessment.
- **Verify AI output by:** checking every citation exists and says what is claimed (arXiv, DOI, venue); rerunning every number; separating model outputs used as data from model outputs used as tools, and reporting both; fixing random seeds and recording model versions and dates.
- **Where AI still fails here (show it):** you will keep a log of fabricated or mis-attributed citations, analysis code with silent errors, and proofs that "verify" because the specification was weakened. Each P3 paper includes a short appendix describing how AI tools were used and how their output was checked, as many venues now request.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Paper reviews (3) and seminar participation | 15% |
| P1 Benchmark audit | 15% |
| P2 Reproduction | 25% |
| P3 Paper and artefact | 30% |
| Conference-style peer reviews (2) | 5% |
| Oral defence | 10% |

**Mastery gate.** You pass when you can: (1) reproduce a published result in agentic software engineering within the paper's stated error (or document precisely why not), with an artefact that a classmate reruns from one command; (2) extend it with a new experiment that tests a stated hypothesis and reports uncertainty; (3) write a paper that two peer reviewers rate as acceptable for a workshop, and defend it orally, including its threats to validity.

## Industry reality

Where this is used (public sources): AI labs, developer-tool companies and large engineering organisations build evaluation harnesses, agent scaffolds and verification pipelines (SWE-bench Pro from Scale AI; DeepSWE from Datacurve; METR's evaluations; Meta's deployed test generation; Google's migration tooling; AWS's verification-guided development of Cedar). Research engineers in these teams are hired for the skills this seminar trains: running careful experiments on agents, building benchmarks, and proving or testing correctness.

**Interview questions from this course** (research engineer and AI-tooling roles)

1. *How would you evaluate a new coding agent fairly?* Strong answer: task selection and contamination checks, multiple runs and variance, cost and time, independent tests for patch correctness, failure taxonomy, comparison against strong simple baselines.
2. *A model scores 75% on SWE-bench Verified. What does that tell you?* Strong answer: what the benchmark measures (single-issue Python fixes with hidden tests), known flaws (test issues, contamination per OpenAI's 2026 audit), scaffold dependence, and why real-world success differs.
3. *How can we trust code no human wrote?* Strong answer: layers of evidence (specs, tests including properties and mutation, differential testing, fuzzing, formal verification where valuable), review focused on specifications, runtime safeguards, and staged rollout.
4. *Design an experiment to measure whether agents help developers on a mature codebase.* Strong answer: randomisation at task level, pre-registration, handling selection effects, outcome measures beyond time (rework, defects), perception vs measurement, power analysis.
5. *What are the main security risks of autonomous coding agents, and how would you study defences?* Strong answer: prompt injection via untrusted inputs, over-privileged tools, supply-chain risks; sandboxed evaluations with fixed attack sets, measured success rates, utility cost of defences.

## Resources (free first)

- **Benchmarks and harnesses:** SWE-bench — https://www.swebench.com/ ; SWE-agent and mini-SWE-agent — https://github.com/SWE-agent ; OpenHands — https://github.com/OpenHands/OpenHands ; Terminal-Bench — https://www.tbench.ai/ ; METR time horizons — https://metr.org/time-horizons/
- **Verification tools:** Dafny — https://dafny.org/ ; Verus — https://github.com/verus-lang/verus ; Lean 4 — https://lean-lang.org/ ; F* — https://fstar-lang.org/ ; TLA+ — https://lamport.azurewebsites.net/tla/tla.html
- **Key papers (arXiv):** HumanEval/Codex 2107.03374 — https://arxiv.org/abs/2107.03374 ; MBPP 2108.07732 — https://arxiv.org/abs/2108.07732 ; AlphaCode 2203.07814 — https://arxiv.org/abs/2203.07814 ; SWE-bench 2310.06770 — https://arxiv.org/abs/2310.06770 ; SWE-bench Multimodal 2410.03859 — https://arxiv.org/abs/2410.03859 ; SWE-bench Live 2505.23419 — https://arxiv.org/abs/2505.23419 ; SWE-Bench Pro 2509.16941 — https://arxiv.org/abs/2509.16941 ; SWE-Lancer 2502.12115 — https://arxiv.org/abs/2502.12115 ; The SWE-Bench Illusion 2506.12286 — https://arxiv.org/abs/2506.12286 ; NL2Repo-Bench 2512.12730 — https://arxiv.org/abs/2512.12730 ; DeepSWE 2607.07946 — https://arxiv.org/abs/2607.07946 ; METR long tasks 2503.14499 — https://arxiv.org/abs/2503.14499 ; SWE-agent 2405.15793 — https://arxiv.org/abs/2405.15793 ; OpenHands 2407.16741 — https://arxiv.org/abs/2407.16741 ; Agentless 2407.01489 — https://arxiv.org/abs/2407.01489 ; SWE-Gym 2412.21139 — https://arxiv.org/abs/2412.21139 ; SWE-smith 2504.21798 — https://arxiv.org/abs/2504.21798 ; TestGen-LLM 2402.09171 — https://arxiv.org/abs/2402.09171 ; ACH 2501.12862 — https://arxiv.org/abs/2501.12862 ; Baldur 2303.04910 — https://arxiv.org/abs/2303.04910 ; LeanDojo 2306.15626 — https://arxiv.org/abs/2306.15626 ; DafnyBench 2406.08467 — https://arxiv.org/abs/2406.08467 ; AlphaVerus 2412.06176 — https://arxiv.org/abs/2412.06176 ; VERINA 2505.23135 — https://arxiv.org/abs/2505.23135 ; Clover 2310.17807 — https://arxiv.org/abs/2310.17807 ; nl2postcond 2310.01831 — https://arxiv.org/abs/2310.01831 ; Cedar 2403.04651 — https://arxiv.org/abs/2403.04651 ; Google migrations 2501.06972 — https://arxiv.org/abs/2501.06972 ; Pearce et al. 2108.09293 — https://arxiv.org/abs/2108.09293 ; Perry et al. 2211.03622 — https://arxiv.org/abs/2211.03622
- **Other papers:** Gulwani, "Automating String Processing in Spreadsheets Using Input-Output Examples" (POPL 2011) — https://doi.org/10.1145/1926385.1926423 ; Le Goues et al., "GenProg" (IEEE TSE 2012) — https://doi.org/10.1109/TSE.2011.104 ; Smith et al., "Is the Cure Worse Than the Disease? Overfitting in Automated Program Repair" (FSE 2015) — https://doi.org/10.1145/2786805.2786825 ; Spracklen et al. (USENIX Security 2025) — https://www.usenix.org/conference/usenixsecurity25/presentation/spracklen
- **Industry reports:** OpenAI, "Why we no longer evaluate SWE-bench Verified" (Feb 2026) — https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/ ; Google Security Blog, "Leveling Up Fuzzing: Finding more vulnerabilities with AI" (Nov 2024) — https://security.googleblog.com/2024/11/leveling-up-fuzzing-finding-more.html ; METR blog — https://metr.org/blog/
- **Venues to follow:** ICSE, FSE, ASE, ISSTA, NeurIPS (Datasets and Benchmarks), ICLR, ICML, PLDI, CAV; the LLM4Code workshop.

## Sources

- METR, data file v1.1 (Claude Opus 4.6 horizons) — https://metr.org/assets/benchmark_results_1_1.yaml ; Kwa et al. (arXiv 2503.14499) — https://arxiv.org/abs/2503.14499 (checked 2026-10)
- OpenAI, "Why we no longer evaluate SWE-bench Verified" (23 Feb 2026), as summarised by Decrypt — https://decrypt.co/359012/openai-benchmark-measure-ai-coding-supremacy-contaminated (checked 2026-10)
- Ding et al., NL2Repo-Bench (arXiv 2512.12730; ICML 2026) — https://arxiv.org/abs/2512.12730 (checked 2026-10)
- Huang et al., DeepSWE (arXiv 2607.07946, Jul 2026) — https://arxiv.org/abs/2607.07946 (checked 2026-10)
- All arXiv identifiers in the resource list were checked against the arXiv API in October 2026.

_Last reviewed: 2026-10_
