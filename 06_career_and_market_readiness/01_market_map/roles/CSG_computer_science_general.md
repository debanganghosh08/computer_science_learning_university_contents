# CSG · Computer Science (Theory, Systems and Research): roles and market (2026)

| Learning path | Interview loop | AI impact | Market overview |
|---|---|---|---|
| [Computer Science (Theory, Systems and Research) major](../../../03_majors/computer_science_general/README.md) | [AI-driven interviews](../../04_ai_driven_interviews/) | [Matrix row](../ai_impact_matrix.md) | [Market map](../README.md) |

All figures were checked in October 2026. Paragraphs marked **Analysis** are interpretation, not measurement.

## Role titles and seniority ladder

This major leads to two kinds of careers: **research** (in industry labs or universities) and **deep systems engineering** (compilers, databases, distributed systems, verification), where theory is used every day.

| Track | Entry | Mid | Senior |
|---|---|---|---|
| Industry research | Research Intern, Research Engineer, PhD Resident | Research Scientist, Applied Scientist | Senior/Principal Research Scientist, Lab Director |
| Academia | PhD student, Research Assistant (Junior Research Fellow in India) | Postdoctoral Researcher, Assistant Professor | Associate Professor, Professor |
| Deep systems engineering | Compiler Engineer, Database Kernel Engineer, Systems Software Engineer | Senior Compiler/Database/Distributed Systems Engineer | Staff/Principal Engineer |
| Verification and security research | Formal Methods Engineer, Verification Engineer | Senior Verification Engineer, Cryptography Engineer | Principal Engineer, Research Lead |

Quantum software (CSG403) and computer graphics (CSG304) form smaller specialist tracks.

## What the work looks like day to day

- **Researchers** read papers, form hypotheses, design experiments or proofs, implement prototypes, measure them, write papers and review others' work (RES501, RES502).
- **Compiler and language engineers** build parsers, optimisation passes and code generators, often in LLVM or MLIR-based toolchains (CSG302, CSG404).
- **Distributed systems engineers** design consensus, replication and storage layers and prove they behave correctly under failure (CSG303).
- **Formal methods engineers** write specifications (for example in TLA+, Coq/Rocq, Lean or Dafny) and prove that critical code meets them (CSG401).
- **Academics** also teach, supervise students and write grant proposals.

## Demand signals

- **US projections.** Computer and information research scientists: 38,600 jobs, projected +22% from 2025 to 2035. The typical entry education is a master's degree ([BLS](https://www.bls.gov/ooh/computer-and-information-technology/computer-and-information-research-scientists.htm)).
- **Industry dominates frontier AI.** Industry produced over 90% of notable frontier AI models in 2025 ([AI Index 2026](https://hai.stanford.edu/assets/files/ai_index_report_2026.pdf)).
- **PhD market.** New AI PhDs in the US and Canada rose 22% from 2022 to 2024, and the PhDs making up that increase took academic jobs, not industry jobs ([AI Index 2026](https://hai.stanford.edu/assets/files/ai_index_report_2026.pdf)). That suggests industry research hiring did not expand as fast as the supply of PhDs (**analysis**).
- **Undergraduate supply.** US enrolment in computer science as an undergraduate major fell 11% from 2024 to 2025 ([AI Index 2026](https://hai.stanford.edu/assets/files/ai_index_report_2026.pdf)).
- **Pay signal in India.** "Research Scientist" is the top-paying software title in Levels.fyi's India data (median total pay ₹54.5 lakh), and "HPC Engineer" (high-performance computing) is second ([Levels.fyi](https://www.levels.fyi/t/software-engineer/locations/india)).

## How AI is changing the role

**Automated or mostly automated.** Literature search and summaries, boilerplate experiment code, plotting, LaTeX formatting, and first drafts of related-work sections.

**Augmented.** Proof exploration with proof assistants and AI suggestions, implementing algorithms from papers, generating test cases and counterexamples, translating code between languages.

**Growing in value.**

- **Formal verification.** As AI generates more code, machine-checked guarantees for critical components become more valuable (**analysis**; covered in CSG401 and CSG501).
- **Evaluation science.** Designing benchmarks and measurements that cannot be gamed. Even the AI Index's own summary of SWE-bench Verified shows how easily a headline can overstate a raw score; see the [market map](../README.md#10-where-sources-disagree).
- **Systems for AI**: compilers for accelerators, distributed training systems, efficient inference.
- **Original problem selection.** AI can help answer questions; choosing the right question remains human work.

**Analysis.** Frontier AI capability is itself the product of computer science research, and METR's measurements show AI agents handling longer and longer research-engineering tasks ([METR](https://metr.org/time-horizons/)). Research careers now reward people who use AI to run more experiments while keeping the mathematical and experimental rigour to tell real results from artefacts. The [AI Index 2026](https://hai.stanford.edu/assets/files/ai_index_report_2026.pdf) also cites evidence of "learning penalties" when engineers rely heavily on AI while learning, which is why this major keeps proofs and implementations done by hand.

## Pay (indicative)

| Market | Role in source | Figure | Type | Source |
|---|---|---|---|---|
| US | Computer and information research scientists | Median $140,300; 10th $82,200; 90th $230,630 (May 2025) | Official survey | [BLS](https://www.bls.gov/ooh/computer-and-information-technology/computer-and-information-research-scientists.htm) |
| India | Research Scientist | Average base ₹8.2 lakh; base range ₹3.0–30 lakh (212 profiles, May 2026) | Self-reported, whole market (includes academic and government labs) | [Payscale](https://www.payscale.com/research/IN/Job=Research_Scientist/Salary) |
| India | Research Scientist (title within software engineering) | Median total pay ₹54.5 lakh (Oct 2026) | Self-reported, mostly large technology companies | [Levels.fyi](https://www.levels.fyi/t/software-engineer/locations/india) |

Academic salaries in India follow government pay scales and fellowship rates, which change by notification; check the current rates from the funding body or institution rather than relying on a figure here.

## The hiring loop

**Industry research (typical):** screening on publications, open-source or reproduced papers; a coding interview; a deep technical interview in your area; a research talk; and team matching.

**Deep systems engineering (typical):** DSA coding; a systems deep dive (for example, "how does MVCC work in PostgreSQL?" or "explain Raft leader election under a network partition"); a design round; behavioural.

**Graduate school (PhD):** statement of purpose, recommendation letters, research experience and, in India, entrance or fellowship examinations such as GATE where applicable.

See [AI-driven interviews](../../04_ai_driven_interviews/).

## Durable skills that make you hard to replace

- Mathematical maturity: proofs, discrete maths, probability, linear algebra.
- Algorithms and complexity at depth.
- Systems intuition: operating systems, compilers, distributed systems.
- Experimental design and honest measurement.
- Reading, reproducing and extending papers.
- Scientific writing and presenting.

## Adjacent roles and transitions

- **Deep learning research** ([DLR](DLR_deep_learning.md)).
- **Software engineering** in performance-critical or infrastructure teams ([SWE](SWE_software_engineering.md)).
- **Security research and cryptography** ([SAR](SAR_security_architecture.md), [OFF](OFF_ethical_hacking_offensive_security.md)).
- **Machine learning engineering** ([MLE](MLE_machine_learning_engineering.md)).
- **AI for science**: overlap OV11.
- **Founding a deep-tech startup** (LCH502).

## Sources

All checked October 2026.

- BLS, Occupational Outlook Handbook: Computer and Information Research Scientists (2025–35; May 2025 pay; modified 27 Aug 2026). https://www.bls.gov/ooh/computer-and-information-technology/computer-and-information-research-scientists.htm
- Stanford HAI, AI Index 2026. https://hai.stanford.edu/assets/files/ai_index_report_2026.pdf
- METR, Time horizons (updated 8 Sep 2026). https://metr.org/time-horizons/
- Levels.fyi India, Software Engineer; Payscale India, Research Scientist (self-reported; 12 Oct 2026). https://www.levels.fyi/t/software-engineer/locations/india ; https://www.payscale.com/research/IN/Job=Research_Scientist/Salary

_Last reviewed: 2026-10_
