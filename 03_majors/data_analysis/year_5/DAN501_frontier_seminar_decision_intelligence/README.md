# DAN501 · Frontier Seminar: Decision Intelligence and Causal Analytics

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 5 · 9 | 4 (≈ 120 hours) | L4 → L5 | [DAN401](../../year_4/DAN401_ai_augmented_analytics_text_to_sql_copilots/README.md), [DAN403](../../year_4/DAN403_domain_analytics_finance_marketing_operations/README.md) | [THS501](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md), [THS502](../../../../05_shared_years_3_to_5/THS502_thesis_or_capstone_ii/README.md), [LCH502](../../../../05_shared_years_3_to_5/LCH502_career_launch_and_founder_studio/README.md) |

Part of the [Data Analysis major](../../README.md). Taken alongside [RES501](../../../../05_shared_years_3_to_5/RES501_research_methods_and_scientific_writing/README.md), [RES502](../../../../05_shared_years_3_to_5/RES502_reading_reproducing_and_extending_papers/README.md) and [THS501](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md). It assumes the experimentation of [DAN302](../../year_3/DAN302_business_statistics_and_experimentation/README.md), the forecasting of [DAN402](../../year_4/DAN402_forecasting_for_business_decisions/README.md) and the governance of [DAN404](../../year_4/DAN404_data_governance_quality_and_privacy_for_analysts/README.md). Students who want the full econometric and machine-learning treatment of causal inference should also read the [DSC501](../../../data_science/year_5/DSC501_frontier_seminar_bayesian_methods_causal_ml/README.md) list. This seminar asks a narrower question: how do analysts and AI systems help organisations make better decisions, and how do we know?

## Why this course matters now

Analysis exists to improve decisions, yet most analytics work stops at a chart. Three research fronts are changing that. First, causal methods built for economics and medicine are now standard tools in business analytics: staggered difference-in-differences, synthetic control, Bayesian structural time series (CausalImpact) and heterogeneous-effect estimators (EconML, CausalML, DoWhy). Second, data agents are being benchmarked on end-to-end analysis rather than single queries: InsightBench (ICLR 2025) uses 100 business datasets with planted insights, DABstep reports 14.55% for the best agent on hard tasks, and BIRD-Interact shows frontier models struggling when they must ask clarifying questions. Third, research on human judgement shows that better numbers do not automatically produce better decisions. People avoid algorithms after seeing them err (Dietvorst, Simmons and Massey, 2015), and LLMs can mistake correlation for causation (Jin et al., 2024). This seminar teaches you to read, reproduce and extend this work, and to build decision systems that hold up under scrutiny. It is where analysts become people who can lead a decision science team, found a company around a decision product, or publish.

## Learning outcomes

By the end you can:

1. **Frame** a business decision formally: alternatives, uncertainties, values, information. **Compute** the value of information for a proposed analysis or experiment.
2. **Identify** causal effects with diagrams and potential outcomes, and **choose** among experiments, difference-in-differences (including staggered adoption), synthetic control, regression discontinuity, instrumental variables and Bayesian structural time series.
3. **Estimate and validate** heterogeneous treatment effects for targeting, with honest validation (Qini/AUUC, holdout policies).
4. **Evaluate** automated insight generation and data agents with benchmarks and your own gold sets, and **identify** where they fail.
5. **Build** prescriptive models that turn predictions into decisions (allocation, pricing, inventory) and **quantify** their value against simple policies.
6. **Explain** the human and organisational factors (algorithm aversion, automation bias, noise, incentives) that decide whether analytics changes decisions.
7. **Reproduce** a published result from the reading list and **extend** it in a direction that matters for Indian or global practice.
8. **Write** a research-grade paper or technical report with a defensible contribution, ready for THS501/THS502.

## Seminar format

Each week has 2–3 assigned readings, a one-page written response (what is claimed, what evidence, what you doubt, what you would test), and a student-led discussion. Every student leads two sessions. Labs reproduce a key figure or table from a reading. The semester ends with a reproduction-and-extension paper and a public talk.

## Chapters and lessons

### Chapter 1 · Decisions, not dashboards (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Decision analysis | Alternatives, uncertainties, preferences; decision trees; decision quality vs outcome quality | Model a pricing decision as a decision tree |
| 1.2 Value of information | Expected value of perfect and sample information; when an experiment is not worth running | Compute EVPI for an A/B test proposal from DAN302 |
| 1.3 Decision intelligence | Linking data, models and human judgement to decisions; decision logs | Start a decision log for your project |
| 1.4 Measuring decision impact | Counterfactual value of an analytics function; what to count | Propose a metric for "analytics impact" and critique it |

**Check your understanding:** Why can a good decision have a bad outcome, and why does that matter for reviewing analysts? When is the value of information from an experiment negative after costs? What would convince you that an analytics team improves decisions?

### Chapter 2 · Causal foundations (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Potential outcomes and DAGs | Two languages for the same problem; identification before estimation | Translate 3 business questions into estimands |
| 2.2 Back-door and front-door | Adjustment sets, colliders, mediators; do-calculus intuition | Find valid adjustment sets in 5 diagrams |
| 2.3 The DoWhy workflow | Model, identify, estimate, refute; sensitivity analysis | Run DoWhy on an observational marketing dataset; report refutations |
| 2.4 What observational data cannot do | Unmeasured confounding; partial identification; bounds | Report bounds for an effect you cannot identify |

**Check your understanding:** Why must the estimand be stated before choosing a method? What is a refutation test, and what does passing one prove? When should an analyst report bounds instead of a point estimate?

### Chapter 3 · Quasi-experiments in business (weeks 3–4)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Difference-in-differences, modern | Staggered adoption and why two-way fixed effects can mislead (Goodman-Bacon, 2021); Callaway and Sant'Anna (2021) | Re-estimate a staggered city rollout both ways |
| 3.2 Synthetic control | Building a weighted control from donor units (Abadie, 2021); placebo inference | Evaluate an illustrative state-level policy with a synthetic control |
| 3.3 Bayesian structural time series | CausalImpact (Brodersen et al., 2015) for interventions on a single series | Estimate the impact of a launch on a public Indian series; check sensitivity to priors |
| 3.4 Discontinuities and instruments | Regression discontinuity at eligibility thresholds; instruments and their fragility | Find a plausible discontinuity in a credit or subsidy rule (illustrative) |
| 3.5 Choosing a design | Assumptions you can test vs assumptions you must argue | A design memo with the weakest assumption stated first |

**Check your understanding:** Why can a two-way fixed-effects estimate have the wrong sign under staggered adoption? What does a synthetic control assume about the donor pool? When would you trust CausalImpact less than a simple diff-in-diff?

### Chapter 4 · Heterogeneous effects and targeting (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Conditional average treatment effects | Meta-learners (S, T, X; Künzel et al., 2019); causal forests (Wager and Athey, 2018) | Estimate CATEs on the Criteo uplift data with EconML or CausalML |
| 4.2 Validation | Qini and uplift curves, held-out policy value, calibration of CATE estimates | Compare 3 learners by policy value on held-out data |
| 4.3 Policy learning | From CATE to a targeting rule under a budget | Choose whom to treat under a fixed budget |
| 4.4 Pitfalls | Overfitting noise, segment fishing at scale, fairness of targeting | Show a learner that looks good in-sample and fails out of sample |

**Check your understanding:** Why is a high response rate not evidence of a high treatment effect? How do you validate a targeting policy without running it? What fairness questions arise when treatment is a discount or a loan offer?

### Chapter 5 · Long-term effects and surrogates (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Short-term metrics, long-term goals | Why experiments optimise what they can measure in two weeks | List 5 cases where short- and long-term effects conflict |
| 5.2 Surrogate indices | Combining short-term proxies to predict long-term effects (Athey, Chetty, Imbens and Kang, 2019) | Build a surrogate index on simulated data with a known long-term effect |
| 5.3 Holdouts and cumulative impact | Long-term holdouts; measuring a programme of many changes | Design a holdout for a year of product changes |
| 5.4 Metric validation | Checking that a north-star or surrogate actually predicts the outcome | Test whether a DAN305 activation metric predicts 6-month retention |

**Check your understanding:** What assumption makes a surrogate index valid, and how could it fail? Why might a team's experiment wins add up to less than the sum of their effects? How do you know a proxy metric still tracks the goal?

### Chapter 6 · Automated insight generation (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Explaining metric changes | Contribution and drill-down algorithms; Adtributor for multi-dimensional root cause (Bhagwan et al., NSDI 2014) | Implement a simple contribution finder; test on planted changes |
| 6.2 Insight platforms | Tableau Pulse's drivers, contributors and outliers; LLM summaries over pre-computed insights | Compare a platform's insights with your own analysis |
| 6.3 Evaluating insights | Precision and recall of planted insights; false discoveries; usefulness to a decision-maker | Score an insight generator on 20 planted changes |
| 6.4 InsightBench | 100 business datasets with planted insights; end-to-end agent evaluation (ICLR 2025) | Run one baseline agent on 5 InsightBench datasets; analyse failures |

**Check your understanding:** Why does an automated insight engine need multiple-comparison control? What is the difference between a correct insight and a useful one? How do planted-insight benchmarks miss real-world difficulty?

### Chapter 7 · Data agents and LLM reasoning about causes (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 The benchmark landscape | Spider 2.0, BIRD-Interact, DABstep, InsightBench: what each measures and misses | A one-page map of open problems |
| 7.2 LLMs and causality | Kıcıman et al. (2023) on LLMs for causal reasoning; Corr2Cause (Jin et al., 2024) and CLadder (Jin et al., 2023) on failures | Test an assistant on 20 correlation-vs-causation items you write |
| 7.3 Agent design for analysis | Planning, tool use, verification steps, asking clarifying questions, abstaining | Add a verification step to an agent; measure the change |
| 7.4 Evaluation as research | Building a benchmark that reflects your domain | Draft a benchmark proposal for Indian public data |

**Check your understanding:** Why can an LLM state causal knowledge fluently and still fail formal causal inference? Which agent behaviour would most improve real-world analytics accuracy, and how would you measure it? What makes a benchmark hard to game?

### Chapter 8 · From prediction to prescription (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Prescriptive analytics | Bertsimas and Kallus (2020): using predictions inside decisions | Inventory decisions with and without covariate information |
| 8.2 Optimisation for analysts | Linear and integer programming for allocation (Google OR-Tools) | Allocate a marketing budget across channels with response curves from DAN403 |
| 8.3 Decisions under uncertainty | Robust and stochastic formulations, simulation, regret | Compare robust vs expected-value allocations |
| 8.4 Value against simple policies | Always benchmark against a rule a manager would use | Quantify the value of your optimiser vs a heuristic |

**Check your understanding:** Why can the most accurate prediction lead to a worse decision? When is a robust decision better than an expected-value-maximising one? What makes a prescriptive model trustworthy to an operations head?

### Chapter 9 · People, organisations and judgement (week 10)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Algorithm aversion and automation bias | People abandon algorithms after seeing errors (Dietvorst et al., 2015), and also over-trust them | Design an experiment on algorithm reliance in your class |
| 9.2 Noise and calibration | Variability in human judgement; calibrated probability forecasts; pre-mortems (Klein, 2007) | Run a calibration exercise; score with the Brier score |
| 9.3 Incentives and Goodhart at scale | Metrics in performance reviews; gaming; organisational design | Analyse a case where a metric target distorted behaviour |
| 9.4 Communicating uncertainty for decisions | Formats that improve decisions (ranges, frequencies, scenarios) | A/B test two uncertainty formats on classmates |

**Check your understanding:** Why might a team ignore a better model? How would you measure whether your forecasts are calibrated? What organisational change would most improve decisions in a company you know?

### Chapter 10 · Responsible decision systems (week 11)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Fairness in targeting and credit | Group fairness metrics, trade-offs, legal context | Audit a targeting policy for disparate impact |
| 10.2 Feedback loops | Decisions that change the data used to evaluate them | Simulate a credit policy that hides its own errors |
| 10.3 Documentation | Model cards (Mitchell et al., 2019), datasheets (Gebru et al., 2021), decision records | Write a model card and a decision record for your project |
| 10.4 Governance | NIST AI RMF, DPDP duties, human review for consequential decisions | A governance plan for your decision system |

**Check your understanding:** Why can a policy that only approves "good" applicants never learn it was wrong? Which fairness metric fits a discount programme, and which fits credit? What must a decision record contain for a regulator?

### Chapter 11 · Research practice and the final paper (weeks 12–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Reproduction | Reproducing a table or figure from a reading; documenting discrepancies | Reproduction report |
| 11.2 Extension | A new dataset (Indian public or business data), a stronger baseline, or a failure analysis | Extension experiments |
| 11.3 Writing | Structure of a short paper; related work; threats to validity | Full paper draft |
| 11.4 Presenting | 15-minute talk, questions, and a public summary | Public talk and peer review |

**Check your understanding:** What counts as a contribution in a reproduction paper? Which threat to validity in your work is the most serious, and what did you do about it? Who outside academia should read your paper, and what would they do with it?

## Weekly rhythm

| Week | Chapter | Seminar and lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Decision trees and EVPI | Response 1 |
| 2 | 2 | DoWhy refutations | Response 2 |
| 3 | 3 | Staggered diff-in-diff | Response 3 |
| 4 | 3 | Synthetic control and CausalImpact | **P1 due** |
| 5 | 4 | CATE and policy value | Response 5 |
| 6 | 5 | Surrogate index simulation | Paper proposal |
| 7 | 6 | Insight engine on planted changes | Response 7 |
| 8 | 7 | LLM causal-reasoning tests | **P2 due** |
| 9 | 8 | Optimisation under uncertainty | Response 9 |
| 10 | 9 | Calibration and reliance experiment | Response 10 |
| 11 | 10 | Fairness and feedback-loop simulation | Model card |
| 12 | 11 | Reproduction | Reproduction report |
| 13 | 11 | Extension | Paper draft |
| 14 | 11 | Peer review | **P3 due** |
| 15 | Review | Public talks | Final paper and viva |

## Working with AI in this course

- **Use AI for:** literature search starting points (every citation verified against the actual paper); explaining derivations; scaffolding EconML, DoWhy and OR-Tools code; critiquing your paper draft as a hostile reviewer.
- **Do without AI (drills):** written responses to readings; causal diagrams and identification arguments; the design memo's assumptions; your own reviews of classmates' papers; the viva.
- **Verify AI output by:**
  - checking every cited paper exists and says what is claimed;
  - testing every causal method on simulated data with known effects before applying it to real data;
  - reproducing every number in your paper from code.
- **Where AI still fails here:** Corr2Cause and CLadder document LLM failures in formal causal reasoning; BIRD-Interact, DABstep and InsightBench document failures in end-to-end analysis. Fabricated or misattributed citations are a known risk of LLM literature help. In this seminar, one unverified citation in a submitted paper fails the assignment.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Weekly reading responses (10) | 15% |
| Leading two seminar sessions | 10% |
| Projects P1 · P2 | 15% · 15% |
| P3 · Reproduction-and-extension paper | 30% |
| Public talk and viva (AI off) | 15% |

**Mastery gate.** You pass when you can: (1) take an unseen business question, state the estimand, draw the diagram, choose and defend a design, and name its weakest assumption in 30 minutes with AI off; (2) reproduce a published result from the reading list and explain every discrepancy; (3) present an extension that a panel judges to be a genuine contribution (new data, stronger baseline or a documented failure mode), with all numbers reproducible from your repository.

## Industry reality

Decision science and causal analytics teams exist at large technology, e-commerce, fintech and consulting firms, and open-source tooling from industry labs (Microsoft's EconML, Uber's CausalML, the PyWhy community's DoWhy, Google's CausalImpact) is widely used. Benchmarks for data agents are being released by industry and academic groups together (Adyen and Hugging Face's DABstep, ServiceNow's InsightBench), which makes evaluation a live research area where analysts with domain knowledge can contribute. In India, public data from MoSPI, RBI, NFHS and data.gov.in offers many under-studied policy and market questions suited to quasi-experimental work.

**Interview questions from this seminar**

1. *"We rolled out a feature city by city over six months. Estimate its effect."* Strong answer: staggered difference-in-differences with heterogeneity-robust estimators; event-study plots; checks for pre-trends; why two-way fixed effects may mislead; placebo tests.
2. *"Should we run this experiment?"* Strong answer: value of information given the decision, costs and prior uncertainty; when to decide without testing.
3. *"How do you choose whom to send a discount?"* Strong answer: uplift, not response; CATE estimation; validation by policy value on held-out data; budget constraint; fairness check.
4. *"An AI tool generated 30 insights about last week. How do you know which are real?"* Strong answer: multiple-comparison control; verification of each against data; evaluate the tool on planted changes; usefulness judged by decisions changed.
5. *"Our managers ignore the model. What do you do?"* Strong answer: understand algorithm aversion and incentives; show calibrated performance; let users adjust within limits; decision logs and post-mortems; measure decisions, not model accuracy alone.

## Resources (free first)

- **Causal inference:** Hernán and Robins, [*Causal Inference: What If*](https://miguelhernan.org/whatifbook) (free); Matheus Facure, [*Causal Inference for the Brave and True*](https://matheusfacure.github.io/python-causality-handbook/landing-page.html) (free); Scott Cunningham, [*Causal Inference: The Mixtape*](https://mixtape.scunning.com/) (free).
- **Tools:** [DoWhy](https://www.pywhy.org/dowhy/); [EconML](https://github.com/py-why/EconML); [CausalML](https://github.com/uber/causalml); [CausalImpact](https://google.github.io/CausalImpact/CausalImpact.html); [Google OR-Tools](https://developers.google.com/optimization).
- **Readings, causal methods:** Goodman-Bacon, [Difference-in-differences with variation in treatment timing](https://www.nber.org/papers/w25018) (*J. Econometrics*, 2021); Callaway and Sant'Anna, [Difference-in-differences with multiple time periods](https://arxiv.org/abs/1803.09015) (2021); Abadie, [Using Synthetic Controls](https://www.aeaweb.org/articles?id=10.1257/jel.20191450) (*JEL*, 2021); Brodersen et al., CausalImpact (*Annals of Applied Statistics*, 2015); Künzel et al., [Meta-learners](https://arxiv.org/abs/1706.03461) (*PNAS*, 2019); Wager and Athey, [Causal forests](https://arxiv.org/abs/1510.04342) (*JASA*, 2018); Athey, Chetty, Imbens and Kang, [The Surrogate Index](https://www.nber.org/papers/w26463) (2019).
- **Readings, insights and agents:** Bhagwan et al., [Adtributor](https://www.usenix.org/conference/nsdi14/technical-sessions/presentation/bhagwan) (NSDI 2014); Sahu et al., [InsightBench](https://arxiv.org/abs/2407.06423) (ICLR 2025); Egg et al., [DABstep](https://arxiv.org/abs/2506.23719) (2025); [BIRD-Interact](https://bird-interact.github.io/); Kıcıman et al., [Causal Reasoning and Large Language Models](https://arxiv.org/abs/2305.00050) (2023); Jin et al., [Corr2Cause](https://arxiv.org/abs/2306.05836) (ICLR 2024); Jin et al., [CLadder](https://arxiv.org/abs/2312.04350) (NeurIPS 2023).
- **Readings, decisions and people:** Bertsimas and Kallus, [From Predictive to Prescriptive Analytics](https://arxiv.org/abs/1402.5481) (*Management Science*, 2020); Dietvorst, Simmons and Massey, "Algorithm Aversion" (*J. Experimental Psychology: General*, 2015); Klein, "Performing a Project Premortem" (*Harvard Business Review*, 2007); Mitchell et al., [Model Cards](https://arxiv.org/abs/1810.03993) (2019); Gebru et al., [Datasheets for Datasets](https://arxiv.org/abs/1803.09010) (2021).
- **Paid, optional:** Kahneman, Sibony and Sunstein, *Noise* (2021); Tetlock and Gardner, *Superforecasting* (2015).

## Sources

All checked 12 Oct 2026.

- Sahu et al., "InsightBench: Evaluating Business Analytics Agents Through Multi-Step Insight Generation" (arXiv 2407.06423; ICLR 2025) — https://arxiv.org/abs/2407.06423
- Egg et al., "DABstep" (arXiv 2506.23719, Jun 2025) — https://arxiv.org/abs/2506.23719
- BIRD-Interact results on the BIRD site (updated 9 Oct 2026) — https://bird-bench.github.io/
- Jin et al., "Can Large Language Models Infer Causation from Correlation?" (arXiv 2306.05836; ICLR 2024) — https://arxiv.org/abs/2306.05836
- Dietvorst, Simmons and Massey, "Algorithm Aversion: People Erroneously Avoid Algorithms After Seeing Them Err", *J. Exp. Psychol. Gen.* 144(1), 2015, doi:10.1037/xge0000033
- Tableau Help, Tableau Pulse insights — https://help.tableau.com/current/online/en-us/pulse_intro.htm
- Repositories: DoWhy — https://www.pywhy.org/dowhy/ ; EconML — https://github.com/py-why/EconML ; CausalML — https://github.com/uber/causalml ; CausalImpact — https://google.github.io/CausalImpact/CausalImpact.html

_Last reviewed: 2026-10_
