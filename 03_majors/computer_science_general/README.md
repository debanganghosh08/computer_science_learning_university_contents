# Computer Science (Theory, Systems and Research) (CSG) · Learning path

| Code | Years | Entry requirements | Market page | Interview loop |
|---|---|---|---|---|
| CSG | 3–5 (after the common Years 1–2) | [CS201](../../02_year_2_core_computer_science/semester_3/CS201_algorithms_and_complexity/README.md), [CS212](../../02_year_2_core_computer_science/semester_4/CS212_distributed_systems_i/README.md), [CS216](../../02_year_2_core_computer_science/semester_4/CS216_programming_languages_compilers_and_interpreters/README.md) | [CSG roles and market](../../06_career_and_market_readiness/01_market_map/roles/CSG_computer_science_general.md) | [AI-driven interviews](../../06_career_and_market_readiness/04_ai_driven_interviews/) |

This is the generalist and research major. The other majors go deep into one layer of industry practice. This one goes deep into the ideas those layers are built from: algorithms and their limits, how programs are translated and proved correct, how machines agree with each other when some of them fail, how images are computed, how people use machines, what can be computed efficiently, what quantum computers change, and how to make new knowledge in all of these. It is the right major if you want to work in a research lab, do a PhD, build compilers, databases, distributed or verification systems, or simply want the strongest foundation this university offers.

## 1. Who this major is for, and the roles it leads to

Choose this major if you like proofs as much as programs, if "why does this work?" bothers you until you can answer it, and if you are willing to read papers that take a week to understand. You do not need to be a mathematical prodigy. You need patience, honesty about what you do not yet understand, and the habit of checking.

| Role | What people in it actually do | Where this major prepares you |
|---|---|---|
| Research Engineer (industry lab) | Implement and scale other people's research ideas, run experiments, build evaluation and training infrastructure, co-author papers | CSG301, CSG302, CSG303, RES502, OV11 |
| Research Scientist / Applied Scientist | Choose research questions, design experiments or proofs, publish, and turn results into products. Usually needs a PhD or an equivalent publication record | CSG501, RES501, THS501–THS502 |
| PhD student → postdoc → faculty | Research, teaching, supervision, grant writing. In India the entry point is often a Junior Research Fellowship | Whole major; §9 below |
| Compiler / ML-compiler engineer | Build parsers, IR passes, optimizers and code generators, increasingly for GPUs and AI accelerators (LLVM, MLIR, Triton-style stacks) | CSG302, CSG404, electives DLR404 and MLE404 |
| Distributed systems / database kernel engineer | Design replication, consensus, transactions and storage engines, and prove they survive failure | CSG303, CSG401, CS211 |
| Formal methods / verification engineer | Write specifications (TLA+, P, Lean, Rocq, Dafny, Verus) and prove or model-check that critical code meets them | CSG401, CSG404, CSG303 |
| Graphics / rendering engineer | Build real-time and offline renderers, GPU pipelines, and neural-rendering systems for games, film, maps, AR/VR and design tools | CSG304, DLR404 |
| Quantum software engineer | Write and compile quantum circuits, study error correction and resource estimates, and plan post-quantum migrations | CSG403, CSG402 |
| Cryptography engineer / researcher | Design and analyse protocols (zero-knowledge proofs, lattice schemes), implement them in constant time, and review others' proofs | CSG402, SAR304, OV07 |
| HCI / UX researcher | Run user studies and controlled experiments, design and evaluate interfaces, including AI interfaces | CSG305, DSC304 |
| Quant developer / HPC engineer | Write low-latency and numerical code where algorithms, systems and correctness all matter | CSG301, CSG303, SWE305, OV10 |
| Deep-tech founder | Turn a research result (a faster algorithm, a verified component, a new renderer) into a product | LCH502 |

**Market signals** (from the [CSG market page](../../06_career_and_market_readiness/01_market_map/roles/CSG_computer_science_general.md), checked October 2026):

- US computer and information research scientists: 38,600 jobs, projected +22% from 2025 to 2035; median pay $140,300 (May 2025). The typical entry education is a master's degree ([BLS](https://www.bls.gov/ooh/computer-and-information-technology/computer-and-information-research-scientists.htm)).
- In India, "Research Scientist" is the top-paying software title in Levels.fyi's data (median total pay ₹54.5 lakh, mostly large technology companies), while Payscale's whole-market average base for research scientists is ₹8.2 lakh (including academic and government labs). The gap is the difference between product-company research and the wider market ([Levels.fyi](https://www.levels.fyi/t/software-engineer/locations/india), [Payscale](https://www.payscale.com/research/IN/Job=Research_Scientist/Salary)).
- New AI PhDs in the US and Canada rose 22% from 2022 to 2024, and the extra graduates went into academia, not industry. Industry research hiring is competitive ([AI Index 2026](https://hai.stanford.edu/assets/files/ai_index_report_2026.pdf)).

## 2. How AI is changing computer science research and theory

All facts below were checked in October 2026. Paragraphs marked **Analysis** are interpretation.

### 2.1 AI for mathematics and theory: what has actually happened

| When | Result | What it shows |
|---|---|---|
| Dec 2023 | **FunSearch** (Nature): an LLM proposes programs, an evaluator scores them; found larger cap sets than previously known ([Nature](https://www.nature.com/articles/s41586-023-06924-6)) | Search over *programs* with an automatic scorer can produce new mathematical constructions |
| Jan 2024 | **AlphaGeometry** solves olympiad geometry with a language model plus a symbolic engine ([Nature](https://www.nature.com/articles/s41586-023-06747-5)) | Neural guesses + exact symbolic checking |
| Jul 2024 → Nov 2025 | **AlphaProof** (with AlphaGeometry 2) scores 28/42 at IMO 2024, one point below gold. The Nature paper (12 Nov 2025) describes reinforcement learning on millions of auto-formalized problems, with proofs checked in the **Lean** proof assistant; AlphaProof solved 3 of the 5 non-geometry problems ([DeepMind](https://deepmind.google/discover/blog/ai-solves-imo-problems-at-silver-medal-level/), [Nature](https://www.nature.com/articles/s41586-025-09833-y)) | Machine-checked proofs remove the need to trust the model |
| May 2025 | **AlphaEvolve** finds a 48-multiplication algorithm for 4×4 complex matrices ([arXiv 2506.13131](https://arxiv.org/abs/2506.13131)). In Nov 2025, Georgiev, Gómez-Serrano, Tao and Wagner applied it to 67 problems: it matched most best-known constructions and improved several, best when guided by experts ([arXiv 2511.02864](https://arxiv.org/abs/2511.02864)) | Evolutionary code search is now a research instrument |
| Jul 2025 | **Gemini Deep Think** reaches gold-medal standard at IMO 2025 in natural language ([DeepMind](https://deepmind.google/discover/blog/advanced-version-of-gemini-with-deep-think-officially-achieves-gold-medal-standard-at-the-international-mathematical-olympiad/)). **Aristotle** (Harmonic) produces Lean-verified solutions to 5 of 6 problems; the problem statements were formalized by hand ([arXiv 2510.01346](https://arxiv.org/abs/2510.01346)) | Olympiad problems are no longer a frontier; formalizing the statement is still human work |
| Dec 2025 – Aug 2026 | **Erdős problems.** A claimed AI solution of Erdős problem #333 was retracted when a 1977 solution by Erdős himself turned up. #728 was solved with GPT-5.2 Pro, with the logic checked using Aristotle (Jan 2026). A Google DeepMind team reported in May 2026 that its agent "autonomously resolved 9 of 353 open Erdős problems". On 20 May 2026 OpenAI announced a counterexample to Erdős's 1946 unit distance conjecture, which mathematicians called historically significant and then improved within weeks ([Quanta, 3 Aug 2026](https://www.quantamagazine.org/why-the-legendary-erdos-problems-are-falling-to-ai-20260803/)) | AI now contributes to real open problems. Literature search and human checking are the bottlenecks |
| Sep 2025 – Feb 2026 | **Verified code generation.** On the vericoding benchmark, off-the-shelf models produced verified programs about 82% of the time in Dafny, 44% in Verus (Rust) and 27% in Lean ([arXiv 2509.22908](https://arxiv.org/abs/2509.22908)). On 77 classical algorithms with identical contracts, the best rates fell to 40.3%, 24.7% and 7.8% ([AlgoVeri, arXiv 2602.09464](https://arxiv.org/abs/2602.09464)) | Proof-carrying code from AI works for easy specs and degrades fast on real algorithms |
| Jun 2026 | **Specifications.** The best of 30 language models wrote semantically correct TLA+ specifications from natural language 8.6% of the time ([arXiv 2606.05792](https://arxiv.org/abs/2606.05792)) | Writing the *right* specification remains a human skill |

**What stays human, with evidence:**

- **Choosing the question and the definition.** Erdős #728's intended wording was unclear at first; a Lean proof is only as good as the statement it proves ([Quanta](https://www.quantamagazine.org/why-the-legendary-erdos-problems-are-falling-to-ai-20260803/)).
- **Knowing the literature.** The #333 retraction happened because nobody had checked a 1977 paper.
- **Reading and judging.** Thomas Bloom, who maintains the Erdős problems database, said of many AI-generated papers: "No human has read it, and no human is going to read it" ([Quanta](https://www.quantamagazine.org/why-the-legendary-erdos-problems-are-falling-to-ai-20260803/)).
- **Specification and measurement in systems.** The TLA+ and AlgoVeri numbers above show that correct specifications and verified implementations of non-trivial algorithms are still mostly human work.

**Analysis.** AI has changed the economics of research. Exploration (searching constructions, drafting proofs, trying counterexamples, writing experiment code) has become cheap. Checking has not. The researchers who gain most are those who can turn a question into something a machine can check: a Lean statement, a TLA+ invariant, a benchmark with a held-out set, an experiment with a pre-registered analysis. The [AI Index 2026](https://hai.stanford.edu/assets/files/ai_index_report_2026.pdf) also reports "learning penalties" when engineers lean heavily on AI while learning, which is why every course in this major has AI-off drills and AI-off exams.

### 2.2 What is automated, what is augmented, what grows

| Mostly automated | Augmented (human decides) | Growing in value |
|---|---|---|
| Literature summaries, boilerplate experiment code, plotting, LaTeX, first drafts of related work, routine proof steps in Lean (`simp`, `omega`, tactic search) | Proof exploration, counterexample search, implementing algorithms from papers, translating code between languages, generating test programs for compilers | Formal specification and verification; evaluation design that cannot be gamed; compilers and systems for AI hardware; problem selection; taste in what is worth proving |

Source: the [CSG market page](../../06_career_and_market_readiness/01_market_map/roles/CSG_computer_science_general.md) and §2.1; the table is **analysis**.

## 3. The 5-year path

### Years 1–2: the common core

Every course in Years 1–2 is required. These matter most for this major:

| Course | Why it matters for CSG |
|---|---|
| [FND103 Discrete Mathematics](../../01_year_1_foundations/semester_1/FND103_discrete_mathematics_for_computing/README.md) | Proofs, logic, combinatorics: the language of every theory course |
| [FND113 Linear Algebra and Calculus](../../01_year_1_foundations/semester_2/FND113_linear_algebra_and_calculus_for_computing/README.md) | Quantum computing (CSG403) is linear algebra over ℂ; graphics (CSG304) is transforms; LP duality (CSG301) is linear algebra |
| [FND116 Probability and Statistics I](../../01_year_1_foundations/semester_2/FND116_probability_and_statistics_i/README.md) | Randomized algorithms, cryptographic security definitions, HCI experiments |
| [CS201 Algorithms and Complexity](../../02_year_2_core_computer_science/semester_3/CS201_algorithms_and_complexity/README.md) | Entry requirement. Proof habits, reductions, NP-hardness |
| [CS202 Computer Architecture and Systems Programming](../../02_year_2_core_computer_science/semester_3/CS202_computer_architecture_and_systems_programming/README.md) | Code generation targets, caches, GPUs |
| [CS211 Database Systems Internals](../../02_year_2_core_computer_science/semester_4/CS211_database_systems_internals/README.md) | Transactions and isolation, needed for CSG303 |
| [CS212 Distributed Systems I](../../02_year_2_core_computer_science/semester_4/CS212_distributed_systems_i/README.md) | Entry requirement. Raft, clocks, consistency models |
| [CS213 Security Foundations](../../02_year_2_core_computer_science/semester_4/CS213_security_foundations/README.md) | Applied cryptography before the theory in CSG402 |
| [CS216 Programming Languages, Compilers and Interpreters](../../02_year_2_core_computer_science/semester_4/CS216_programming_languages_compilers_and_interpreters/README.md) | Entry requirement. Interpreters, type checking, SSA |

### Years 3–5: the major

| Semester | Major courses | Shared courses | Other |
|---|---|---|---|
| 5 (Year 3) | [CSG301 Advanced Algorithms](year_3/CSG301_advanced_algorithms/README.md) · [CSG302 Compiler Construction](year_3/CSG302_compiler_construction/README.md) · [CSG303 Distributed Systems II: Consensus, Replication and Scale](year_3/CSG303_distributed_systems_ii_consensus_replication/README.md) | [PRO301 Professional Practice: Ethics, Law and Responsible AI](../../05_shared_years_3_to_5/PRO301_professional_practice_ethics_law_and_responsible/README.md) | 1 elective (DLR304 if you plan OV11) |
| 6 (Year 3) | [CSG304 Computer Graphics](year_3/CSG304_computer_graphics/README.md) · [CSG305 Human-Computer Interaction](year_3/CSG305_human_computer_interaction/README.md) | [CAR301 Career Lab I: DSA Mastery, Portfolio and Open Source](../../05_shared_years_3_to_5/CAR301_career_lab_i_dsa_mastery_portfolio_and_open/README.md) | 1–2 electives (DSC301 if you plan OV11) |
| 7 (Year 4) | [CSG401 Formal Methods and Program Verification](year_4/CSG401_formal_methods_and_program_verification/README.md) · [CSG402 Complexity Theory and Theoretical Cryptography](year_4/CSG402_complexity_theory_and_theoretical_cryptography/README.md) | [IND401 Industry Co-op Studio](../../05_shared_years_3_to_5/IND401_industry_co_op_studio/README.md) (a research-lab placement counts) | Overlap course A |
| 8 (Year 4) | [CSG403 Quantum Computing for Computer Scientists](year_4/CSG403_quantum_computing_for_computer_scientists/README.md) · [CSG404 Programming Language Theory and Type Systems](year_4/CSG404_programming_language_theory_and_type_systems/README.md) | [CAR401 Career Lab II: Interviews, System Design and AI-Driven Assessments](../../05_shared_years_3_to_5/CAR401_career_lab_ii_interviews_system_design_and_ai/README.md) | Overlap course B |
| 9 (Year 5) | [CSG501 Frontier Seminar: AI for Mathematics, Science and Theory](year_5/CSG501_frontier_seminar_ai_for_mathematics_science/README.md) | [RES501 Research Methods and Scientific Writing](../../05_shared_years_3_to_5/RES501_research_methods_and_scientific_writing/README.md) · [RES502 Reading, Reproducing and Extending Papers](../../05_shared_years_3_to_5/RES502_reading_reproducing_and_extending_papers/README.md) · [THS501 Thesis or Capstone I](../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md) | Graduate applications (autumn) |
| 10 (Year 5) | — | [THS502 Thesis or Capstone II](../../05_shared_years_3_to_5/THS502_thesis_or_capstone_ii/README.md) · [LCH502 Career Launch and Founder Studio](../../05_shared_years_3_to_5/LCH502_career_launch_and_founder_studio/README.md) | Electives; submit the thesis as a paper |

Catalog prerequisites inside the major: CSG301 → CSG401; CSG302 → CSG402; CSG303 → CSG403; CSG304 → CSG404; CSG401 + CSG403 → CSG501. Each course page also states the background it actually draws on (for example, CSG402 leans on CSG301's randomized algorithms, CSG403 on linear algebra, and CSG404 on CS216 and CSG302).

**Three ways through the major.** All ten courses are required; electives, overlap and thesis topic set the emphasis.

| Emphasis | Lean on | Electives | Typical thesis |
|---|---|---|---|
| Theory | CSG301, CSG402, CSG404, CSG401 | Extra mathematics (probability, algebra), CSG-style reading groups | A new bound, reduction or algorithm with proof, ideally formalized in Lean |
| Systems | CSG302, CSG303, CSG401 | SWE305, DLR404, MLE404 | A compiler pass, protocol or storage engine with verification and measurements |
| AI for science and research engineering | CSG501, OV11 | DLR301, DLR304, DSC301 | Reproduce and extend an AI-for-math or AI-for-science paper |

## 4. Skill map by level

| Level | You can… | Mastery gate (do it, don't describe it) |
|---|---|---|
| L0 → L1 (Year 1) | Write programs in Python, Java and TypeScript; write proofs by induction and contradiction; manipulate matrices and probabilities | Prove 10 unseen discrete-maths statements in writing, and implement and test the algorithm behind three of them |
| L2 (end of Year 2) | Analyse and prove algorithms; implement Raft; build an interpreter and a type checker | The CS201, CS212 and CS216 gates: an unseen NP-hardness reduction; Raft passing 500 runs; a new language feature added live |
| L3 (end of Year 3) | Analyse randomized and approximation algorithms; ship a compiler to native code; build and break replicated systems; write a renderer; run a controlled user study | Compile a 300-program test suite for a small typed language to RISC-V or x86-64 with a register allocator; find a seeded linearizability bug in a replicated store with your own fault-injection harness; prove an approximation ratio for a problem you have not seen |
| L4 (end of Year 4) | Mechanize proofs; model-check protocols; reason about complexity classes and security reductions; program and analyse quantum algorithms; prove type soundness | Mechanize type soundness of a small language in Lean or Rocq; write a security reduction for a scheme you have not seen; run Grover and phase estimation on a simulator and on real hardware, and explain the gap with a noise model |
| L5 (Year 5) | Read, reproduce and extend papers; use AI tools for exploration while keeping machine-checked or statistically sound results | Reproduce a published result within its stated error, extend it, and submit a workshop-quality paper with an artifact that passes an artifact-evaluation checklist |

## 5. Recommended overlaps and electives

**Primary overlap: [OV11 AI for Science and Research Engineering](../../04_overlaps/OV11_ai_for_science_research_engineering/README.md).** It is built from [DLR304](../deep_learning/year_3/DLR304_training_deep_networks_optimization/README.md), [DSC301](../data_science/year_3/DSC301_statistical_inference_and_modeling/README.md) and [MLE501](../machine_learning_engineering/year_5/MLE501_frontier_seminar_ml_research_engineering/README.md), with [OV11A Scientific Machine Learning and AI for Discovery](../../04_overlaps/OV11_ai_for_science_research_engineering/OV11A_scientific_machine_learning_and_ai_for_discovery/README.md) in semester 7 and [OV11B Research Software Engineering](../../04_overlaps/OV11_ai_for_science_research_engineering/OV11B_research_software_engineering/README.md) in semester 8. Both require DLR304 and DSC301, so take those as your Year 3 electives. OV11 pairs naturally with CSG501.

**Other overlaps that fit:**

| Overlap | Fits if you lean towards | Composed of |
|---|---|---|
| [OV07 Privacy Engineering](../../04_overlaps/OV07_privacy_engineering/README.md) | Cryptography (zero-knowledge proofs, secure computation, differential privacy) | DEN404, SEC305, PRO301 |
| [OV10 FinTech Systems Engineering](../../04_overlaps/OV10_fintech_systems_engineering/README.md) | Quant development, low-latency and ledger systems | BE401, SEC305, DEN303 |
| [OV05 AI Security and Safety Engineering](../../04_overlaps/OV05_ai_security_safety/README.md) | Verification and evaluation of AI systems | AIE305, OFF403, SAR403 |

**Electives** (any major's 300-level courses; pick 3–5):

- [DLR301 Neural Networks from Scratch](../deep_learning/year_3/DLR301_neural_networks_from_scratch_autograd/README.md) and [DLR304 Training Deep Networks](../deep_learning/year_3/DLR304_training_deep_networks_optimization/README.md): the deep-learning base for CSG501 and OV11.
- [DSC301 Statistical Inference and Modeling](../data_science/year_3/DSC301_statistical_inference_and_modeling/README.md) and [DSC304 Experimental Design and Causal Inference](../data_science/year_3/DSC304_experimental_design_and_causal_inference/README.md): for empirical research and CSG305.
- [SWE305 Concurrency and Performance Engineering](../software_engineering/year_3/SWE305_concurrency_and_performance_engineering/README.md): memory models and measurement, for systems research.
- [SWE303 Programming Languages in Practice: Go, Rust and the JVM](../software_engineering/year_3/SWE303_programming_languages_in_practice_go_rust/README.md): Rust before CSG401's Verus and CSG404's ownership types.
- [SAR304 Applied Cryptography and PKI](../security_architecture/year_3/SAR304_applied_cryptography_and_pki_for_architects/README.md): practice to pair with CSG402's theory.
- [MLE301 Machine Learning Algorithms from Scratch](../machine_learning_engineering/year_3/MLE301_machine_learning_algorithms_from_scratch/README.md): learning theory meets algorithms.
- [AIE305 Evaluating LLM Systems](../ai_engineering/year_3/AIE305_evaluating_llm_systems/README.md): evaluation design for anyone using AI in research.
- Year 4–5 options for the systems emphasis (check prerequisites): [DLR404 Efficient Deep Learning and GPU Programming](../deep_learning/year_4/DLR404_efficient_deep_learning_and_gpu_programming/README.md) and [MLE404 Efficient Inference: Quantization, Distillation and Compilers](../machine_learning_engineering/year_4/MLE404_efficient_inference_quantization_distillation/README.md).

## 6. Flagship industry project

The CSG flagship is described in [`05_industry_projects/CSG_computer_science_general.md`](../../06_career_and_market_readiness/05_industry_projects/CSG_computer_science_general.md). It is a research-grade artifact: one system component that you specify formally, implement, verify, measure against published baselines, and write up as a short paper with a reproducible artifact. Its parts come from CSG303 P3 (a replicated store tested under faults), CSG401 P3 (a verified component), CSG302 P3 or CSG301 P3 (a compiler or an engineered algorithm with measurements) and RES502 (reproduction discipline). Build it in Year 4, and use it in CAR401, graduate applications and LCH502.

## 7. Certifications: an honest note

Certifications are largely irrelevant for this major. No research lab, compiler team or PhD committee selects on them. What carries weight:

- **Papers and preprints**, even workshop papers, with code. An artifact that passes a conference's artifact evaluation (ACM's "Artifacts Available / Evaluated / Results Reproduced" badges) is a strong signal ([ACM badging policy](https://www.acm.org/publications/policies/artifact-review-and-badging-current)).
- **Merged open-source work** in serious projects: LLVM, MLIR, Lean's [Mathlib](https://leanprover-community.github.io/mathlib-overview.html), [Google DeepMind's Formal Conjectures](https://github.com/google-deepmind/formal-conjectures), etcd, Qiskit, Cirq, Blender, Godot.
- **Competitions:** [ICPC](https://icpc.global/) (Asia regionals are held in India), [IOI](https://ioinformatics.org/) (before university), the [International Mathematics Competition for University Students](https://www.imc-math.org.uk/) (open to universities worldwide), the Putnam (for students at US and Canadian universities; its past problems are free in [Kiran Kedlaya's archive](https://kskedlaya.org/putnam-archive/)), the [PACE challenge](https://pacechallenge.org/) (parameterized algorithm engineering) and the [SAT Competition](https://satcompetition.github.io/).
- **Reproductions:** a careful public reproduction of a known paper (RES502) often opens more doors than a certificate ever could.

## 8. The interview loop for this role

| Track | Typical rounds | Prepared by |
|---|---|---|
| Industry research (engineer or scientist) | Screening on publications, open source or reproduced papers; coding; a deep technical interview in your area; a research talk; team matching | CSG501, RES502, THS501 |
| Deep systems (compiler, database, distributed, verification) | DSA coding; a systems deep dive ("explain Raft leader election under a partition", "how does SSA make constant propagation easier?"); a design round; behavioural | CSG301–CSG303, CSG401, CAR401 |
| Graphics | Coding; linear algebra and rendering questions (transforms, BRDFs, BVHs); a GPU performance discussion; portfolio review | CSG304 |
| Graduate school | Statement of purpose, letters, research experience, sometimes an interview with a technical problem; in India, entrance or fellowship exams | §9, RES501 |

These loop shapes are the typical pattern described on the [market page](../../06_career_and_market_readiness/01_market_map/roles/CSG_computer_science_general.md); details vary by employer. Some employers ban AI in interviews ([Anthropic](https://www.anthropic.com/candidate-ai-guidance)) and others require it ([Canva](https://www.canva.dev/blog/engineering/yes-you-can-use-ai-in-our-interviews/)), so practise both ways. Simulations and question banks: [AI-driven interviews](../../06_career_and_market_readiness/04_ai_driven_interviews/).

## 9. The path to graduate school

**In India.**

- **GATE** (Graduate Aptitude Test in Engineering) is the main route into MTech, MS (Research) and many PhD programmes at the IITs and IISc, and into fellowships. GATE 2027 is organised by IIT Madras, with exam days in February 2027 ([GATE 2027](https://gate2027.iitm.ac.in/)). The CS paper's discrete maths, algorithms, theory of computation, compilers, OS, databases and networks are all covered in Years 1–3.
- **IISc and the IITs** admit to research programmes through GATE scores plus written tests and interviews run by each department ([IISc admissions](https://iisc.ac.in/admissions/)). Shortlisting rules change every year; read the current brochure.
- **TIFR** (Mumbai) and **CMI** (Chennai) run their own entrance examinations for theoretical computer science and mathematics research programmes ([TIFR](https://www.tifr.res.in/), [CMI admissions](https://www.cmi.ac.in/admissions/)).
- **The Prime Minister's Research Fellowship (PMRF)** offers a direct-entry route to a PhD for strong final-year students from listed institutions; eligibility, nomination and stipend rules change by notification, so check the official portal ([PMRF](https://pmrf.in/)) rather than second-hand summaries.
- **Pre-PhD research positions**, such as Microsoft Research India's Research Fellows programme, let graduates spend one to two years on research before applying ([MSR India](https://www.microsoft.com/en-us/research/academic-program/research-fellows-program-at-microsoft-research-india/)).

**Abroad.** In the US, most CS PhD programmes admit students directly after a bachelor's degree and fund them through assistantships; in much of continental Europe a PhD is a salaried position that usually expects a master's degree; UK PhDs are typically shorter, with competitive funding for international students (these are general patterns; check each programme). Use [CSRankings](https://csrankings.org/) to find active groups by research area, then read their last three papers before you write to anyone.

**What wins admission, in order:** research experience with a letter from someone who saw you do it; a reproduced and extended paper (RES502); a clear statement of what you want to work on and why; grades and test scores. This major's thesis (THS501–THS502) should be planned as a submission, not a report.

## 10. Fast track for working professionals

For engineers with 2–8 years of experience who want research-engineer, compiler, distributed-systems or verification roles. Budget 12–15 hours a week for about 15 months.

1. **Placement (weeks 1–2).** Attempt the mastery gates of CS201, CS212 and CS216. Fill gaps first; nothing in this major works without them.
2. **Months 1–4: pick your door.** CSG303 for infrastructure roles, CSG302 for compiler and ML-compiler roles, or CSG301 for research-engineer and quant roles. Apply each lab to a system you know from work (within your employer's rules).
3. **Months 5–8: verification.** CSG401. Specify one real protocol or component from your work in TLA+ or P and model-check it. This is often the fastest way to stand out inside your current company.
4. **Months 9–12: depth.** CSG404 (if compilers or languages) or CSG402 (if cryptography or theory) or CSG403 (if quantum).
5. **Months 13–15: evidence.** RES502-style reproduction of one paper in your area, published with code, plus one merged contribution to an open-source project in that area.
6. **Throughout.** One CSG501 paper discussion a fortnight (a reading group at work counts), and one timed DSA set a week from month 9 if you are interviewing.

## Sources

All checked October 2026.

- CSG market page and its sources (BLS, AI Index 2026, Levels.fyi, Payscale) — [roles/CSG_computer_science_general.md](../../06_career_and_market_readiness/01_market_map/roles/CSG_computer_science_general.md)
- US BLS, Computer and Information Research Scientists (2025–35; May 2025 pay) — https://www.bls.gov/ooh/computer-and-information-technology/computer-and-information-research-scientists.htm
- Stanford HAI, AI Index 2026 — https://hai.stanford.edu/assets/files/ai_index_report_2026.pdf
- Romera-Paredes et al., "Mathematical discoveries from program search with large language models" (FunSearch), *Nature* (Dec 2023) — https://www.nature.com/articles/s41586-023-06924-6
- Trinh et al., "Solving olympiad geometry without human demonstrations" (AlphaGeometry), *Nature* (Jan 2024) — https://www.nature.com/articles/s41586-023-06747-5
- Google DeepMind, "AI achieves silver-medal standard solving IMO problems" (25 Jul 2024) — https://deepmind.google/discover/blog/ai-solves-imo-problems-at-silver-medal-level/ ; Hubert et al., "Olympiad-level formal mathematical reasoning with reinforcement learning", *Nature* (12 Nov 2025) — https://www.nature.com/articles/s41586-025-09833-y
- Google DeepMind, Gemini Deep Think gold-medal standard at IMO 2025 (Jul 2025) — https://deepmind.google/discover/blog/advanced-version-of-gemini-with-deep-think-officially-achieves-gold-medal-standard-at-the-international-mathematical-olympiad/
- Harmonic, "Aristotle: IMO-level Automated Theorem Proving" (arXiv 2510.01346, Oct 2025) — https://arxiv.org/abs/2510.01346
- Novikov et al., "AlphaEvolve" (arXiv 2506.13131, Jun 2025) — https://arxiv.org/abs/2506.13131 ; Georgiev, Gómez-Serrano, Tao, Wagner, "Mathematical exploration and discovery at scale" (arXiv 2511.02864, Nov 2025) — https://arxiv.org/abs/2511.02864
- Quanta Magazine, "Why the Legendary Erdős Problems Are Falling to AI" (3 Aug 2026) — https://www.quantamagazine.org/why-the-legendary-erdos-problems-are-falling-to-ai-20260803/
- Bursuc et al., "A benchmark for vericoding: formally verified program synthesis" (arXiv 2509.22908, Sep 2025) — https://arxiv.org/abs/2509.22908 ; AlgoVeri (arXiv 2602.09464, Feb 2026) — https://arxiv.org/abs/2602.09464
- "Can LLMs Write Correct TLA+ Specifications?" (arXiv 2606.05792, Jun 2026) — https://arxiv.org/abs/2606.05792
- GATE 2027 (IIT Madras) — https://gate2027.iitm.ac.in/ ; IISc admissions — https://iisc.ac.in/admissions/ ; CMI admissions — https://www.cmi.ac.in/admissions/ ; TIFR — https://www.tifr.res.in/ ; PMRF — https://pmrf.in/
- Competitions: ICPC — https://icpc.global/ ; IOI — https://ioinformatics.org/ ; IMC — https://www.imc-math.org.uk/ ; PACE — https://pacechallenge.org/ ; SAT Competition — https://satcompetition.github.io/
- Anthropic candidate AI guidance — https://www.anthropic.com/candidate-ai-guidance ; Canva Engineering (11 Jun 2025) — https://www.canva.dev/blog/engineering/yes-you-can-use-ai-in-our-interviews/

_Last reviewed: 2026-10_
