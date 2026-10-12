# SWE501 · Labs and projects

Project tiers L1–L3 follow the standard project template (size and polish); the skill level of the whole course is L4 → L5. This is a research seminar. Labs are short, focused experiments that build the skills the projects need. All agent runs use containers with no access to real credentials; security experiments are defensive and sandboxed. Every experiment records model names and versions, dates, prompts or scaffolds, seeds, number of runs, and cost. Budget: agree a compute and API budget with the instructor before P2; cheaper open-weight models are acceptable when the research question allows.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Enumerative synthesiser and pass@k | A small programming-by-example synthesiser for string transformations; unbiased pass@k for a model's samples on 30 problems | Code, success table, pass@k curves for k = 1, 5, 10 | 4 h |
| 2 · Benchmark teardown | Run one open-source agent on 20 SWE-bench Verified or Lite tasks; inspect every pass and every failure manually | Per-task verdicts (true pass, false pass, false fail, true fail) with reasons | 6 h |
| 3 · Contamination probes | File-path recall, verbatim-fix reproduction and issue-text completion probes on 30 tasks from an older and a newer benchmark | Probe results per benchmark and a short interpretation of what they can and cannot show | 4 h |
| 4 · Agent ablations | Remove or change one interface tool in mini-SWE-agent or SWE-agent; compare with an Agentless-style pipeline | Success, cost and variance over 3 runs per condition, with intervals | 6 h |
| 5 · Environments and graders | Build 10 executable tasks from a repository's history; write a grader that resists test special-casing, test deletion and grader edits | Task set, grader, and a red-team report of three attempted hacks | 6 h |
| 6 · Test generation with filters | Reimplement build/pass-repeatedly/coverage filters (TestGen-LLM style) on an open project; add a mutation-score filter | Acceptance rate per filter stage and mutation-score change | 5 h |
| 7 · Dafny and LLM proofs | Verify 3 small programs by hand; then run a model on 20 DafnyBench tasks | Hand proofs; model results with a failure classification (wrong invariant, weakened spec, timeout) | 6 h |
| 8 · Study design | Pre-registration document for a study of agent use on a mature codebase, including power analysis and selection-effect controls | Pre-registration and a peer critique | 4 h |
| 9 · Defence evaluation (sandboxed) | Fixed set of 30 injected instructions placed in issues and files of a sandbox repository; evaluate an agent with and without a containment design | Attack success rate and task success rate in both conditions, with intervals | 5 h |

## Projects

### P1 · Benchmark audit (L1, ~6 hours)

**Real-world inspiration:** OpenAI's February 2026 audit of SWE-bench Verified, which found many problems with test design or problem descriptions among the hardest tasks, and "The SWE-Bench Illusion" (2025) on memorisation.

**What to build:** audit 30 tasks from one public benchmark (SWE-bench Verified, SWE-bench Pro public split, SWE-bench Live, Terminal-Bench or another approved one). For each task, judge whether the problem statement is sufficient, whether the hidden tests accept all reasonable correct solutions and reject plausible wrong ones, and whether there are signs of contamination.

**Acceptance criteria:**
- Written rubric applied to all 30 tasks; a second student independently audits 10 of them, and agreement is reported.
- For every task judged flawed, a concrete demonstration: a correct alternative patch that fails, or a wrong patch that passes, or a missing requirement.
- A 3-page report: method, findings with counts and intervals, comparison with published audits, implications for scores.

**Stretch goals:** submit corrections or issues to the benchmark maintainers.

**What it proves to an employer:** you can tell a meaningful number from a misleading one, which every AI-tooling and evaluation team needs.

### P2 · Reproduction of a published result (L2, ~15 hours)

**Real-world inspiration:** reproducibility tracks at ICSE, FSE and NeurIPS, where independent reruns frequently find that results depend on unreported details.

**What to build:** reproduce the main result (or a clearly defined subset) of one paper from the course list, for example an Agentless-style pipeline on a SWE-bench subset, a TestGen-LLM-style filter pipeline, a DafnyBench evaluation, or a METR-style time-horizon fit on a small task set. Agree the scope with the instructor.

**Acceptance criteria:**
- A one-command artefact (container plus scripts) that a classmate reruns successfully, with logs.
- Results reported with the same metrics as the paper, with variance over at least 3 runs where the paper allows.
- Every deviation from the paper's setup listed, with its likely effect; if the result does not reproduce, a careful analysis of why.
- A 4-page reproduction report in a standard paper template, citing exact versions and dates.

**Stretch goals:** contact the authors with your findings; contribute fixes to their artefact.

**What it proves to an employer:** you can run rigorous experiments on AI systems and report honestly, the core of research-engineer roles.

### P3 · Workshop paper: an extension with a new hypothesis (L3, portfolio-grade, ~30 hours)

**Real-world inspiration:** workshop papers at venues such as the LLM4Code workshop (co-located with ICSE) and NeurIPS or ICLR workshops on code and agents, where students often publish their first paper.

**What to build:** extend your P2 reproduction (or another approved base) with a new experiment that tests a falsifiable hypothesis tied to one of the open problems in Chapter 10. Examples: does adding a specification-generation step reduce false passes on your audited tasks? Does a mutation-score filter change which agent patches maintainers accept? Does restricting network egress reduce injection success without reducing task success? Does a contamination-resistant task set reorder agent rankings?

**Acceptance criteria:**
- A pre-registered hypothesis and analysis plan (submitted before running the main experiment), and a clear statement of any deviation.
- Statistically sound analysis: intervals or tests appropriate to the design; no claim beyond what the data support.
- A 6–8 page paper with abstract, introduction, related work (all citations checked), method, results, threats to validity, limitations and an AI-use statement.
- An artefact that reproduces every figure and table from one command.
- Two conference-style peer reviews received and answered in a response letter; a 15-minute talk with questions.

**Stretch goals:** submit to a workshop or arXiv with instructor approval; release the dataset or tool under an open licence.

**What it proves to an employer or graduate school:** you can create new knowledge in a fast-moving field with rigour, which is the bar for research engineering roles, PhD admissions and senior AI-tooling work.

## Feeds into

- [RES502 Reading, Reproducing and Extending Papers](../../../../05_shared_years_3_to_5/RES502_reading_reproducing_and_extending_papers/README.md): P2 and P3 can satisfy its reproduction requirement.
- [THS501 Thesis or Capstone I](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md) and [THS502](../../../../05_shared_years_3_to_5/THS502_thesis_or_capstone_ii/README.md): P3 is designed to grow into a thesis.
- [OV12 Agent Infrastructure and Platform Engineering](../../../../04_overlaps/OV12_agent_infrastructure_platform/README.md): evaluation harnesses and containment research in production settings.
- [LCH502 Career Launch and Founder Studio](../../../../05_shared_years_3_to_5/LCH502_career_launch_and_founder_studio/README.md): a published artefact or benchmark is a strong signal for research-engineer and developer-tools roles, or for a founder building tools in this space.
