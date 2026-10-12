# MLE304 · Model Evaluation, Fairness and Robustness

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 3 · 6 | 4 (≈ 120 hours) | L2 → L4 | [CS214](../../../../02_year_2_core_computer_science/semester_4/CS214_machine_learning_foundations/README.md), [CS205](../../../../02_year_2_core_computer_science/semester_3/CS205_software_engineering_i_design_testing/README.md) | [MLE404](../../year_4/MLE404_efficient_inference_quantization_distillation/README.md), [MLE401](../../year_4/MLE401_mlops_deployment_monitoring_and_retraining/README.md), [MLE403](../../year_4/MLE403_ranking_and_recommendation_systems_at_scale/README.md), [OV05](../../../../04_overlaps/OV05_ai_security_safety/README.md) |

## Why this course matters now

A model is only as trustworthy as the evidence behind it, and regulators now ask for that evidence. The EU AI Act lists credit scoring of natural persons as high-risk (Annex III, point 5(b)); after the Digital Omnibus (Regulation (EU) 2026/1744), those obligations apply from 2 December 2027. In India, the Reserve Bank's FREE-AI committee report (August 2025) sets out 7 "Sutras" and 26 recommendations and proposes that AI credit assessments be auditable rather than a black box, and the RBI's draft model-risk guidance (June 2026) asks lenders to define explainability thresholds for every AI model. Real failures show why: a widely used US health algorithm used cost as a proxy for need, and correcting it would raise the share of Black patients flagged for extra care from 17.7% to 46.5% (Obermeyer et al., 2019). AI assistants compute any metric you ask for, and libraries such as Fairlearn make fairness metrics one line of code. Deciding which metric reflects the decision, which fairness definition applies, whether a 0.3-point gain is real, and whether the model will survive next quarter's data is still the engineer's job.

## Learning outcomes

By the end you can:

1. **Choose** metrics that match the decision a model supports, for classification, regression, ranking and forecasting, and **justify** the choice to a non-specialist.
2. **Quantify** uncertainty with bootstrap confidence intervals, paired tests and seed variance, and **decide** whether a difference is real.
3. **Measure and fix** calibration (reliability diagrams, Brier score, Platt, isotonic and temperature scaling), and **produce** prediction sets with conformal prediction.
4. **Find** failing slices with slice analysis and behavioural tests, including intersectional slices.
5. **Compute** group fairness metrics, **explain** why calibration and equalised odds cannot both hold in general, and **apply** pre-, in- and post-processing mitigations while reporting the trade-off.
6. **Map** a model's evaluation evidence to the EU AI Act, RBI guidance, India's DPDP Act and the NIST AI RMF.
7. **Detect** distribution shift with two-sample and classifier-based tests, and **stress-test** models for underspecification.
8. **Explain** adversarial examples and robustness at the level of threat models and defences, and **evaluate** a model's robustness with standard benchmarks.
9. **Write** a model card and an evaluation report that another team could audit.

## Chapters and lessons

### Chapter 1 · Evaluation design (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 What evaluation is for | Offline metrics as proxies for decision value; the ladder: unit tests → offline → shadow → online experiment | Write the evaluation plan for a loan-approval model before training |
| 1.2 Baselines | Majority class, current rules, last year's model, a simple linear model | Show a "90% accurate" model losing to the majority baseline |
| 1.3 Test sets as contracts | Frozen holdouts, golden sets, time-based holdouts, never tuning on test | Design a holdout policy for a team of 5 |
| 1.4 Metric hygiene | Aggregation (micro, macro, weighted), denominators, metrics that can be gamed | Compute macro and micro F1 on an imbalanced set and explain the gap |

**Check your understanding:** Why is "the current rule-based system" often the right baseline? What breaks when a team tunes on the test set "just once"? Why can macro F1 fall while accuracy rises?

### Chapter 2 · Metrics by task (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Classification | Precision, recall, F-beta, ROC-AUC vs PR-AUC, log loss, Brier score | Pick metrics for spam, cancer screening and fraud review |
| 2.2 Regression and forecasting | MAE, RMSE, MAPE's failure at zero, quantile (pinball) loss, MASE | Show MAPE exploding on low-volume items |
| 2.3 Ranking | Precision@k, recall@k, MRR, MAP, NDCG with graded relevance | Compute NDCG@10 by hand, then in code |
| 2.4 Cost-sensitive evaluation | Expected cost, decision curves, capacity-constrained thresholds | Convert a confusion matrix into rupees for a lending scenario (illustrative) |
| 2.5 Metric to business link | Proxy metrics, guardrail metrics, offline–online gaps | Write the metric tree for a food-delivery ETA model |

**Check your understanding:** Why does ROC-AUC hide poor performance at the top of a ranked list? When is quantile loss the right choice for an ETA? Why is a metric that improves offline but not online still informative?

### Chapter 3 · Uncertainty and significance (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Bootstrap intervals | Percentile bootstrap for any metric; stratified and grouped bootstrap | 95% CI for AUC on 2,000 test rows |
| 3.2 Comparing two models | Paired bootstrap, McNemar's test, DeLong (concept) | Is model B's +0.4 AUC real? |
| 3.3 Variance from training | Seeds, data order, initialisation; benchmark conclusions that flip (Bouthillier et al., 2021) | Train 10 seeds; plot the spread against the claimed gain |
| 3.4 Multiple comparisons | Garden of forking paths, Bonferroni and Holm, pre-registration of the primary metric | Simulate 20 null comparisons; count false wins |
| 3.5 Online experiments (preview) | A/B tests, sample-ratio mismatch, variance reduction with CUPED (Kohavi, Tang and Xu, 2020) | Compute the sample size to detect a 1% lift |

**Check your understanding:** Why must a bootstrap for a user-level model resample users, not rows? Why is an improvement smaller than seed variance not evidence? What does a sample-ratio mismatch tell you before you look at results?

### Chapter 4 · Calibration and conformal prediction (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 What calibration means | Reliability diagrams, expected calibration error and its binning sensitivity, Brier decomposition | Reliability diagrams for logistic regression, a GBDT and a deep net |
| 4.2 Recalibration | Platt scaling, isotonic regression, temperature scaling (Guo et al., 2017); fitting on held-out data | Recalibrate each model; compare Brier score and ECE |
| 4.3 Calibration after resampling | Correcting probabilities after undersampling or class weights | Fix a fraud model's probabilities after 1:10 undersampling |
| 4.4 Conformal prediction | Split conformal, coverage guarantees, exchangeability (Angelopoulos and Bates, 2021); MAPIE | 90% prediction sets; check empirical coverage by slice |
| 4.5 Abstention | Selective prediction, coverage–risk curves, routing to humans | Pick an abstention threshold that halves errors |

**Check your understanding:** Why does calibration matter for pricing and expected-loss decisions but not for pure ranking? Why must recalibration data be separate from training data? What does conformal coverage not guarantee for a specific subgroup?

### Chapter 5 · Slices, behavioural tests and error analysis (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Slice analysis | Segment metrics with confidence intervals, minimum slice size, intersectional slices | Worst-5 slices of a credit model with CIs |
| 5.2 Simpson's paradox | Aggregate vs within-group trends | Construct a case where model A wins overall but loses in every slice |
| 5.3 Behavioural testing | CheckList (Ribeiro et al., 2020): minimum functionality, invariance and directional tests | 30 CheckList tests for a sentiment model; report failure rates |
| 5.4 Model regression tests | Golden sets, per-slice thresholds as release gates | Write a pytest suite that fails if any key slice drops more than 2 points |

**Check your understanding:** Why can a model improve on average and still be a worse release? Why do small slices need confidence intervals before anyone acts? Which invariances should a credit model satisfy?

### Chapter 6 · Fairness: definitions and impossibility (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Sources of harm | Historical bias, representation bias, measurement bias and proxies (Obermeyer et al., 2019); Gender Shades error gaps (Buolamwini and Gebru, 2018) | Find the proxy label problem in 3 case descriptions |
| 6.2 Group metrics | Demographic parity, equal opportunity and equalised odds (Hardt, Price and Srebro, 2016), predictive parity, calibration within groups | Compute all of them with Fairlearn's `MetricFrame` |
| 6.3 Impossibility | Kleinberg, Mullainathan and Raghavan (2016); Chouldechova (2017): calibration and equal error rates conflict when base rates differ | Reproduce the conflict on synthetic data with different base rates |
| 6.4 Individual and counterfactual fairness | Similar people treated similarly; limits of "fairness through unawareness" | Show a model rebuilding a removed attribute from proxies |
| 6.5 The Indian context | Attributes that matter (gender, caste, religion, region, language, disability) are often not collected; proxies such as PIN code, language and device | Write a measurement plan for a lender that does not store caste or religion |

**Check your understanding:** Why does removing the protected attribute not remove bias? Why can't a risk score be calibrated and have equal false-positive rates across groups with different base rates? Who should choose the fairness definition?

### Chapter 7 · Fairness mitigation, law and governance (weeks 7–8)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Pre-processing | Reweighing, resampling, label review | Reweigh and measure the change in each metric |
| 7.2 In-processing | Reductions approach (Agarwal et al., 2018) with Fairlearn's `ExponentiatedGradient` | Plot accuracy vs equalised-odds difference |
| 7.3 Post-processing | Group-specific thresholds (`ThresholdOptimizer`) and when law or policy forbids them | Compare with in-processing on the same frontier |
| 7.4 Regulation | EU AI Act high-risk duties for credit scoring and the 2027 timeline; RBI FREE-AI (2025) and the draft model-risk guidance (2026); RBI Digital Lending Directions (2025); DPDP Act 2023 and Rules 2025; US adverse-action reasons and the withdrawn CFPB Circular 2022-03 as history | Map one model's evidence to each framework in a table |
| 7.5 Frameworks | NIST AI RMF (Govern, Map, Measure, Manage); ISO/IEC 42001 management systems | Fill in the "Measure" function for your P2 model |

**Check your understanding:** Why is the fairness–accuracy trade-off a policy decision rather than a tuning problem? What changes for an Indian lender when the DPDP Rules' substantive duties start? Why should mitigation be evaluated on held-out data, slice by slice?

### Chapter 8 · Explanations and reason codes (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Global explanations | Permutation importance, partial dependence, accumulated local effects | Explain a credit model globally; spot a non-monotone effect |
| 8.2 Local explanations | SHAP values and their behaviour under correlated features | Compare SHAP with and without a duplicated feature |
| 8.3 Reason codes | Turning attributions into principal reasons for an adverse decision; monotonic constraints | Generate top-4 reasons for 20 declined applicants; check stability |
| 8.4 Counterfactuals | Minimal changes that flip a decision (Wachter et al., 2017); actionability | Produce counterfactuals that use only changeable features |

**Check your understanding:** Why can two near-identical applicants receive different reason codes? When are counterfactual explanations misleading? Why do monotonic constraints help explanations?

### Chapter 9 · Distribution shift (weeks 10–11)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Kinds of shift | Covariate, label (prior) and concept shift; subpopulation shift | Classify 8 production incidents by shift type |
| 9.2 Detecting shift | Two-sample tests, MMD, classifier-based detection; tests on learned representations (Rabanser et al., 2019) | Detect a simulated shift with three methods; compare power |
| 9.3 Benchmarks of real shift | WILDS (Koh et al., 2021); new test sets for old benchmarks (Recht et al., 2019) | Train on one WILDS domain and evaluate on another |
| 9.4 Underspecification | Same validation score, different behaviour (D'Amour et al., 2020); stress tests | 10 seeds, one stress test: show divergent behaviour |
| 9.5 Responses | Importance weighting, label-shift correction, retraining policy | Correct a label shift and measure recovered accuracy |

**Check your understanding:** Why can a model's accuracy drop with no change in input distribution? Why can a shift detector fire on harmless changes? What does underspecification imply for choosing between equally scored models?

### Chapter 10 · Robustness and adversarial examples, conceptually (week 12)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Natural robustness | Corruptions and perturbations (Hendrycks and Dietterich, 2019) | Evaluate your vision model on CIFAR-10-C |
| 10.2 Adversarial examples | What they are, threat models (white-box, black-box, budgets), the linearity explanation (Goodfellow et al., 2014) | Discussion: which threat model fits a fraud system vs a photo filter? |
| 10.3 Defences and their evaluation | Adversarial training (Madry et al., 2017) and its accuracy cost; certified robustness by randomised smoothing (Cohen et al., 2019); why weak evaluations mislead | Compare standard and robust models from RobustBench on the same benchmark |
| 10.4 Data-side threats | Poisoning and label manipulation as concepts; data provenance as a defence | Write the data-integrity checks for a crowdsourced labelling pipeline |

**Check your understanding:** Why does adversarial robustness usually cost clean accuracy? Why must a defence be evaluated against an adaptive attacker? What is the most realistic threat to a model trained on user reports?

### Chapter 11 · Documentation and audit (weeks 13–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Model cards | Intended use, factors, metrics, evaluation data, caveats (Mitchell et al., 2019) | Write a model card for your P2 model |
| 11.2 Datasheets | Motivation, composition, collection, consent (Gebru et al., 2018) | Write a datasheet for one course dataset |
| 11.3 Evaluation reports | Evidence tables, confidence intervals, slice results, known failures, sign-off | Draft a 4-page evaluation report |
| 11.4 Audit and review | Independent validation, reproducibility of evaluation, review checklists | Audit a classmate's report and file findings |

**Check your understanding:** What belongs in "out-of-scope uses", and why does it protect users? What makes an evaluation reproducible by an auditor? Which claims in a model card need a confidence interval?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Baselines and holdout policy | — |
| 2 | 2 | Lab 2 · Metric choice | — |
| 3 | 3 | Lab 3 · Bootstrap, seeds and paired tests | **P1 due** |
| 4 | 4 | Lab 4 · Calibration and conformal prediction | — |
| 5 | 5 | Lab 5 · Slices and CheckList | — |
| 6 | 6 | Lab 6 · Fairness metrics and impossibility | Mid-term (AI off) |
| 7 | 7 | Lab 7 · Mitigation frontier | — |
| 8 | 7 | Regulation mapping (part of P2) | — |
| 9 | 8 | Lab 8 · Reason codes and counterfactuals | **P2 due** |
| 10 | 9 | Lab 9 · Shift detection | — |
| 11 | 9 | Lab 9 (continued): WILDS and stress tests | — |
| 12 | 10 | Lab 10 · Robustness benchmarks | — |
| 13 | 11 | Evaluation harness (P3) | — |
| 14 | 11 | Evaluation report and audit (P3) | **P3 due** |
| 15 | Review | P3 presentation | Final exam (AI off) |

## Working with AI in this course

- **Use AI for:** writing metric and plotting code; explaining a paper's proof sketch; drafting model cards and datasheets from your notes; summarising regulatory texts (then reading the source paragraphs yourself); generating CheckList test cases. Claude, ChatGPT, Gemini and coding agents all handle these tasks.
- **Do without AI (drills):** compute precision, recall, NDCG and expected cost from small tables by hand; derive the base-rate conflict between calibration and equal error rates; choose a fairness definition for a scenario and argue for it; read a reliability diagram. The mid-term and final are AI-off.
- **Verify AI output by:** recomputing every metric with a second implementation (scikit-learn, Fairlearn, your own); checking a CI with a simulation where the truth is known; quoting the exact paragraph of any law or guideline an assistant summarises; checking that conformal coverage holds empirically.
- **Where AI still fails here:** assistants confidently state outdated regulatory facts. The CFPB withdrew Circular 2022-03 in May 2025, and the EU high-risk dates moved in 2026, so ask an assistant about either and compare its answer with the source. They also bootstrap rows when users repeat, compute fairness metrics on training data, and treat "drop the protected attribute" as a fix. Lab 6 includes a log of such errors.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (10) | 25% |
| Projects P1–P3 | 40% |
| Mid-term (AI off) | 10% |
| Final exam (AI off) | 25% |

**Mastery gate.** You pass when you can, for a model you have not seen before and within 3 hours: (1) produce an evaluation report with the right metrics, bootstrap CIs, a calibration assessment and the worst 3 slices; (2) compute and interpret at least 3 group-fairness metrics, state which definition you recommend and why, and show one mitigation's trade-off; (3) run a shift test against a later data sample and recommend ship, fix or retrain, with evidence. Without AI, you can explain the calibration–equalised-odds conflict on a whiteboard.

## Industry reality

Evaluation and fairness work is done by ML engineers, model-risk and validation teams in banks and fintechs, trust-and-safety teams, and applied scientists. Lending in India and the EU now has explicit governance expectations (RBI FREE-AI, RBI's draft model-risk guidance, the EU AI Act). Public failures shape practice: Gender Shades found error rates up to 34.7% for darker-skinned women against at most 0.8% for lighter-skinned men in commercial gender classifiers, and the Obermeyer study showed how a proxy label creates bias without any protected attribute in the model.

**Interview questions from this course**

1. *Accuracy is 99.5% on fraud. Is the model good?* Strong answer: base rate; PR-AUC and recall at the review capacity; cost-weighted evaluation; calibration if scores feed rules; a baseline comparison; CIs.
2. *Model B beats model A by 0.3 AUC points. Ship it?* Strong answer: paired bootstrap CI; seed variance; slice regressions; latency and cost; offline–online gap; the decision depends on the metric's link to value.
3. *Can a credit model be both calibrated and have equal false-positive rates across groups?* Strong answer: not in general when base rates differ (Kleinberg et al.; Chouldechova); what to measure; who decides; how to report the trade-off.
4. *How do you detect that a deployed model's data has shifted, and what do you do?* Strong answer: feature and prediction drift tests, classifier-based detection, label-delay strategies, performance proxies, thresholds that avoid alarm fatigue, retrain vs fix vs roll back.
5. *How would you explain a loan rejection to a customer and to a regulator?* Strong answer: reason codes from attributions with stability checks; monotonic constraints; counterfactuals limited to changeable features; documentation (model card) and an audit trail; the relevant RBI or EU expectations.

## Resources (free first)

- **Books:** Barocas, Hardt and Narayanan, *Fairness and Machine Learning* (MIT Press, 2023; free online) — https://fairmlbook.org/ ; Molnar, *Interpretable Machine Learning* — https://christophm.github.io/interpretable-ml-book/ ; Kohavi, Tang and Xu, *Trustworthy Online Controlled Experiments* (book site; the book is paid) — https://experimentguide.com/
- **Courses and explainers:** Google ML Crash Course, fairness module — https://developers.google.com/machine-learning/crash-course/fairness ; MLU-Explain (visual explainers of metrics and calibration) — https://mlu-explain.github.io/
- **Tools:** scikit-learn calibration — https://scikit-learn.org/stable/modules/calibration.html ; Fairlearn — https://fairlearn.org/ ; MAPIE — https://mapie.readthedocs.io/ ; CheckList — https://github.com/marcotcr/checklist ; InterpretML — https://interpret.ml/ ; WILDS — https://wilds.stanford.edu/ ; RobustBench — https://robustbench.github.io/ ; Folktables (US census tasks replacing UCI Adult) — https://github.com/socialfoundations/folktables
- **Regulation and frameworks:** RBI FREE-AI report — https://www.rbi.org.in/Scripts/PublicationReportDetails.aspx?UrlPage=&ID=1306 ; RBI draft model-risk guidance (press release) — https://www.rbi.org.in/scripts/BS_PressReleaseDisplay.aspx?prid=63006 ; RBI Digital Lending Directions 2025 — https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=12848 ; EU AI Act Annex III — https://artificialintelligenceact.eu/annex/3/ ; NIST AI RMF — https://www.nist.gov/itl/ai-risk-management-framework ; ISO/IEC 42001 — https://www.iso.org/standard/81230.html

## Sources

- EU AI Act, Annex III point 5(b) (creditworthiness and credit scoring as high-risk) — https://artificialintelligenceact.eu/annex/3/ ; Digital Omnibus on AI, Regulation (EU) 2026/1744, Annex III obligations from 2 Dec 2027 (summary by Cuatrecasas) — https://www.cuatrecasas.com/en/global/intellectual-property/art/digital-omnibus-ai-has-been-published (checked 2026-10)
- RBI press release on the FREE-AI committee report (13 Aug 2025): 7 Sutras, 26 recommendations — https://rbi.org.in/Scripts/BS_PressReleaseDisplay.aspx?prid=61018 ; report — https://www.rbi.org.in/Scripts/PublicationReportDetails.aspx?UrlPage=&ID=1306 (checked 2026-10)
- RBI draft "Guidance on Regulatory Principles for Model Risk Management, 2026" (24 Jun 2026; draft, comments closed 24 Jul 2026) — https://www.rbi.org.in/scripts/BS_PressReleaseDisplay.aspx?prid=63006 (checked 2026-10)
- RBI (Digital Lending) Directions, 2025 (8 May 2025) — https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=12848 (checked 2026-10)
- PIB, DPDP Rules 2025 notified (14 Nov 2025) with an 18-month phased timeline — https://www.pib.gov.in/PressReleasePage.aspx?PRID=2190014 (checked 2026-10)
- CFPB, list of withdrawn guidance (Circular 2022-03 withdrawn 12 May 2025) — https://www.consumerfinance.gov/compliance/guidance/withdrawn-guidance/ (checked 2026-10)
- Obermeyer et al., *Science* 366:447 (2019) — https://www.science.org/doi/10.1126/science.aax2342 ; Buolamwini and Gebru, Gender Shades (PMLR 81, 2018) — https://proceedings.mlr.press/v81/buolamwini18a.html (checked 2026-10)
- Hardt et al. — https://arxiv.org/abs/1610.02413 ; Kleinberg et al. — https://arxiv.org/abs/1609.05807 ; Chouldechova — https://arxiv.org/abs/1703.00056 ; Agarwal et al. — https://arxiv.org/abs/1803.02453 ; Guo et al. — https://arxiv.org/abs/1706.04599 ; Nixon et al. on ECE — https://arxiv.org/abs/1904.01685 ; Angelopoulos and Bates — https://arxiv.org/abs/2107.07511 ; Bouthillier et al. — https://arxiv.org/abs/2103.03098 ; Ribeiro et al. — https://arxiv.org/abs/2005.04118 ; Wachter et al. — https://arxiv.org/abs/1711.00399 ; Rabanser et al. — https://arxiv.org/abs/1810.11953 ; Koh et al. (WILDS) — https://arxiv.org/abs/2012.07421 ; Recht et al. — https://arxiv.org/abs/1902.10811 ; D'Amour et al. — https://arxiv.org/abs/2011.03395 ; Hendrycks and Dietterich — https://arxiv.org/abs/1903.12261 ; Goodfellow et al. — https://arxiv.org/abs/1412.6572 ; Madry et al. — https://arxiv.org/abs/1706.06083 ; Cohen et al. — https://arxiv.org/abs/1902.02918 ; Mitchell et al. — https://arxiv.org/abs/1810.03993 ; Gebru et al. — https://arxiv.org/abs/1803.09010 ; Ding et al. (Folktables) — https://arxiv.org/abs/2108.04884 (all checked 2026-10)
- Fairlearn 0.15.0 (released 12 Oct 2026) and MAPIE 1.5.0 (Aug 2026) on PyPI — https://pypi.org/ (checked 2026-10)

_Last reviewed: 2026-10_
