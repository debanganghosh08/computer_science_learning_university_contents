# DAN501 · Labs and projects

Every lab reproduces or tests a claim from the reading list, first on simulated data where the true answer is known and then on real data. Every project is a Git repository whose numbers rebuild from code, with a short paper-style write-up (question, method, results with uncertainty, threats to validity). Every citation is checked against the actual paper. Experiments on classmates (Labs 10 and P2 options) use informed, voluntary participation and collect no personal data beyond what the exercise needs.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Decision tree and EVPI | Model a pricing or launch decision; compute the expected value of perfect and sample information for a proposed A/B test | Decision tree, EVPI/EVSI calculation, and a recommendation on whether to test | 3 h |
| 2 · DoWhy refutations | Model, identify, estimate and refute an effect on an observational marketing dataset; add a sensitivity analysis | Notebook, estimand, refutation results, and bounds under unmeasured confounding | 4 h |
| 3 · Staggered diff-in-diff | Simulate a staggered rollout with heterogeneous effects; compare two-way fixed effects with Callaway–Sant'Anna | Bias of each against the known truth; an event-study plot | 4 h |
| 4 · Synthetic control and CausalImpact | Evaluate an illustrative intervention with a synthetic control and with CausalImpact on a public Indian series; placebo tests | Both estimates, placebo distribution, and prior-sensitivity analysis | 5 h |
| 5 · CATE and policy value | S-, T- and X-learners and a causal forest on the Criteo uplift data; held-out Qini curves; a budgeted targeting policy | Policy value table with intervals; an overfitting demonstration | 5 h |
| 6 · Surrogate index | Simulate short-term proxies and a long-term outcome; build a surrogate index; break its key assumption | Recovery of the long-term effect, and the failure case | 4 h |
| 7 · Insight engine on planted changes | Implement a contribution/drill-down finder (Adtributor-style); plant 20 changes in a KPI cube; score precision and recall | Code, scores, and a comparison with an LLM's explanations of the same changes | 5 h |
| 8 · LLM causal-reasoning tests | Write 20 correlation-vs-causation items in business settings; test two assistants; compare with Corr2Cause-style results | Item set, scores, error analysis | 3 h |
| 9 · Optimisation under uncertainty | Allocate a budget across channels with response curves from DAN403 using OR-Tools; compare expected-value and robust solutions | Allocations, regret under scenarios, value vs a simple heuristic | 4 h |
| 10 · Calibration, reliance and feedback loops | Run a calibration exercise (Brier scores) and a small reliance-on-algorithm experiment; simulate a credit policy that hides its own errors | Results with intervals; the simulation and a mitigation | 4 h |

## Projects

### P1 · Causal design memo for a real decision (L1, ~6 hours)

**Real-world inspiration.** Decision science teams write design memos before analysing a policy or product change, because the design, not the estimator, decides whether the answer can be trusted.

**What to build.** Pick a real, public decision with public data, for example a state-level policy change in India (data from MoSPI, RBI DBIE, NFHS or data.gov.in), or a company change visible in public metrics. Write a 3-page design memo: the decision, the estimand, the causal diagram, candidate designs (diff-in-diff, synthetic control, regression discontinuity, interrupted time series), the chosen design and its weakest assumption, falsification tests you will run, and the value of the information to the decision-maker.

**Acceptance criteria**
- The estimand is stated precisely (population, treatment, outcome, time).
- At least 3 designs are compared, with the assumptions each requires.
- At least 2 falsification or placebo tests are specified before any outcome data is analysed (committed to Git first).
- A short pilot analysis runs end to end on the real data.

**Stretch goals.** Complete the full analysis and include it as an appendix; pre-register it publicly (for example, on OSF).

**What it proves to an employer.** You can design a credible causal analysis for a real decision and say in advance what would prove you wrong.

### P2 · Evaluating an automated analyst (L2, ~15 hours)

**Real-world inspiration.** Vendors and internal teams are shipping automated insights and data agents; InsightBench, DABstep and BIRD-Interact show how hard end-to-end analysis remains. Organisations need people who can evaluate these systems on their own data.

**What to build.** Choose one: (a) an automated insight generator (your Lab 7 engine, an open-source agent such as InsightBench's baseline, or a BI tool's insight feature); or (b) an LLM data agent with code execution. Build an evaluation on a domain dataset from DAN403 with at least 30 planted changes or questions, including some with no real effect and some that require causal reasoning to answer correctly.

**Acceptance criteria**
- Ground truth is created independently of the system under test and documented.
- Precision and recall of insights (or accuracy of answers) are reported with intervals and repeated runs.
- At least 5 failure cases are analysed in depth, each classified (false discovery, causal error, wrong definition, missing context, arithmetic).
- At least one intervention (added context, a verification step, multiple-comparison control) is tested, and its effect is measured.
- The evaluation code and dataset are released so others can rerun them.

**Stretch goals.** Compare two systems; run a small user study on whether the insights changed participants' decisions.

**What it proves to an employer.** You can tell an organisation, with evidence, whether its automated analytics can be trusted and how to make it better. Few people can do this today.

### P3 · Reproduction-and-extension paper (L3, portfolio-grade research paper, ~30 hours)

**Real-world inspiration.** Research progress depends on reproduction and careful extension. Many published analytics methods have never been tested on Indian data, on modern AI agents, or against strong simple baselines.

**What to build.** Pick one paper from the reading list (for example: staggered diff-in-diff, synthetic control, the surrogate index, meta-learners, Adtributor, InsightBench, DABstep or Corr2Cause). Reproduce one key table or figure, then extend it in one direction:
- **New data:** apply the method to an Indian public or business dataset and report what changes.
- **Stronger baseline:** show whether a simple method matches the published one.
- **Failure analysis:** construct cases where the method breaks and explain why.
- **New evaluation:** for agent benchmarks, a domain-specific test set built with the benchmark's protocol.

Write a 6–8 page paper (introduction, related work, method, reproduction results, extension results, threats to validity, conclusion) and give a 15-minute public talk.

**Acceptance criteria**
- The reproduced result matches the paper within a stated tolerance, or every discrepancy is investigated and explained.
- The extension has a clearly stated contribution and at least one result with quantified uncertainty.
- Threats to validity name at least 3 specific risks and what you did about each.
- All code, data-access instructions and environment files are in the repository; a reviewer rebuilds the main figure from a clean clone.
- Every citation is verified; zero fabricated references.
- Viva (AI off): you defend the method and answer questions on its assumptions.

**Stretch goals.** Submit to a workshop or student research venue; release the extension dataset with a datasheet.

**What it proves to an employer.** You can read the frontier, test it honestly and add something new. Research teams, decision science groups and founders building decision products hire for this, and it is the core of your THS501 proposal.

## Feeds into

- [THS501 Thesis or Capstone I](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md) and [THS502 Thesis or Capstone II](../../../../05_shared_years_3_to_5/THS502_thesis_or_capstone_ii/README.md): P3 is designed to become your thesis proposal.
- [RES502 Reading, Reproducing and Extending Papers](../../../../05_shared_years_3_to_5/RES502_reading_reproducing_and_extending_papers/README.md): shared reproduction methods.
- [LCH502 Career Launch and Founder Studio](../../../../05_shared_years_3_to_5/LCH502_career_launch_and_founder_studio/README.md): decision products and causal measurement for your own venture.
