# DSC404 · Data Science in Production: Deployment, Monitoring and Communication

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 4 · 8 | 4 (≈ 120 hours) | L3 → L4 | [DSC304](../../year_3/DSC304_experimental_design_and_causal_inference/README.md) (uses [DSC302](../../year_3/DSC302_applied_machine_learning_for_data_scientists/README.md), [DSC303](../../year_3/DSC303_data_wrangling_at_scale_pandas_polars_and_spark/README.md) and [DSC305](../../year_3/DSC305_feature_engineering_and_model_evaluation/README.md)) | [THS501](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md), [THS502](../../../../05_shared_years_3_to_5/THS502_thesis_or_capstone_ii/README.md), [LCH502](../../../../05_shared_years_3_to_5/LCH502_career_launch_and_founder_studio/README.md), flagship project ([DSC industry project](../../../../06_career_and_market_readiness/05_industry_projects/DSC_data_science.md)) |

Part of the [Data Science major](../../README.md). This course is about getting data science into decisions and keeping it right once it is there. Building ML platforms and serving infrastructure belongs to the ML Engineering major ([MLE401](../../../machine_learning_engineering/year_4/MLE401_mlops_deployment_monitoring_and_retraining/README.md)); this course teaches what a data scientist must own when their model, forecast or analysis goes live.

## Why this course matters now

Most of the value, and most of the damage, of data science happens after the notebook. Booking.com's study of about 150 customer-facing models found that success came from an iterative, hypothesis-driven process integrated with other disciplines, validated by randomized trials, and that offline model performance was not strongly correlated with business gains (Bernardi et al., 2019). Google's engineers described how ML systems accumulate "hidden technical debt" through data dependencies and feedback loops (Sculley et al., 2015). Failures are often framing failures: a widely used US health algorithm that predicted cost as a proxy for need reduced the number of Black patients identified for extra care by more than half (Obermeyer et al., 2019). Rules are tightening: India's Digital Personal Data Protection Rules, 2025 were notified in November 2025 with an 18-month phased compliance window, and the EU AI Act (Regulation 2024/1689) sets obligations for high-risk systems. AI assistants now draft dashboards, reports and monitoring code in minutes. That makes the human parts scarcer and more valuable: deciding what goes into a decision, designing monitoring that catches the failure you have not seen yet, and writing the memo that changes a leader's mind. Amazon's 2017 shareholder letter describes replacing slide decks with "narratively structured six-page memos"; the ability to write one is a core skill here.

## Learning outcomes

By the end you can:

1. **Choose** the right production form for a data-science output (batch scores, real-time API, rule, report, dashboard, one-off decision) and **justify** it to engineers and stakeholders.
2. **Package** an analysis or model as a tested, reproducible artefact with pinned environments, configuration and a model registry entry.
3. **Deploy** batch and real-time scoring with shadow mode, canary and champion–challenger patterns, and **define** a fallback.
4. **Monitor** data, predictions and outcomes, including performance estimation before labels arrive, and **set** alert thresholds with a known false-alarm rate.
5. **Measure** post-launch impact with holdouts and guardrails, and **attribute** business changes honestly.
6. **Build** decision-focused dashboards that show uncertainty and lead to an action.
7. **Write** analyses and memos that change decisions, and **present** them to executives.
8. **Run** problem intake, scoping and stakeholder management, including saying no with evidence.
9. **Apply** ethics, fairness and privacy law (DPDP Act and Rules, EU AI Act, NIST AI RMF) to a live system, and **lead** a blameless post-mortem.

## Chapters and lessons

### Chapter 1 · What "production" means for data science (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Forms of output | Batch scores, APIs, rules, reports, dashboards, one-off decisions; who consumes each | Classify ten data-science deliverables by form and consumer |
| 1.2 Decision owners | Who acts, who is accountable, what "done" means | Write a RACI for a churn-model launch |
| 1.3 Lessons from Booking.com | Hypothesis-driven iteration, RCT validation, offline vs business performance (Bernardi et al., 2019) | Summarise the six lessons and map each to a later chapter |
| 1.4 Technical debt in ML systems | Entanglement, hidden feedback loops, undeclared consumers (Sculley et al., 2015) | Find three debt patterns in a supplied project |

**Check your understanding:** (1) When is a well-maintained rule better than a model? (2) Why does an undeclared consumer of your scores make change risky? (3) What does "done" mean for an analysis vs for a model?

### Chapter 2 · Packaging and reproducibility (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 From notebook to package | Modules, entry points, configuration files, logging | Turn your DSC305 P3 notebook into a package |
| 2.2 Environments | `uv` lockfiles, containers, pinned model and data versions | Rebuild the package on a clean machine |
| 2.3 Tests for data science code | Unit tests, data tests (pandera), model behaviour tests, regression tests on scores | Add tests that fail if feature logic changes |
| 2.4 Model registry and lineage | MLflow tracking and registry; linking model, data and code versions | Register two model versions with full lineage |

**Check your understanding:** (1) What must be versioned to reproduce a score from three months ago? (2) What is a behavioural test for a model? (3) Why is a model registry not enough without data versions?

### Chapter 3 · Deployment patterns (weeks 3–4)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Batch scoring | Scheduled jobs with DuckDB or Spark, idempotency, backfills, writing scores with metadata | Build a nightly batch scorer with idempotent writes |
| 3.2 Real-time scoring | A FastAPI service, input validation, latency budgets, feature parity with training | Serve a model with p95 latency under 50 ms locally |
| 3.3 Safe rollout | Shadow mode, canary, champion–challenger, kill switches, rule fallbacks | Run a shadow deployment and compare decisions |
| 3.4 Handover to engineering | Interfaces, SLAs, runbooks, what MLEs need from you | Write a handover document and runbook |
| 3.5 Analyses as products | Scheduled reports, parameterised notebooks, Quarto publishing | Publish a parameterised weekly report |

**Check your understanding:** (1) Why must a batch job be idempotent? (2) What do you compare during shadow mode? (3) What belongs in a runbook for a model?

### Chapter 4 · Monitoring models and data (weeks 5–6)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 What to monitor | Data quality, input drift, prediction drift, outcome metrics, business metrics; label delay | Draw a monitoring map for a credit model |
| 4.2 Drift tests and their false alarms | Population stability index, KS and chi-square tests, multiple testing across features | Tune drift alerts to fewer than one false alarm a month on stable data |
| 4.3 Performance before labels | Confidence-based performance estimation (NannyML), proxy labels | Estimate accuracy before labels arrive and compare with truth later |
| 4.4 Calibration and threshold drift | Base-rate shifts, recalibration triggers | Detect calibration drift in a simulated shift |
| 4.5 Retraining decisions | Scheduled vs triggered retraining; when retraining hurts (feedback loops, label leakage) | Decide retraining policy for three models |

**Check your understanding:** (1) Why can input drift be harmless and stable inputs still hide a failure? (2) How does testing 200 features for drift every day create alarms? (3) When should you not retrain automatically?

### Chapter 5 · Measuring impact after launch (weeks 6–7)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Holdouts and guardrails | Long-term holdout groups, guardrail metrics, ramp schedules | Design the holdout for a pricing model |
| 5.2 Attribution | Separating model effects from seasonality, marketing and mix shifts (links to DSC304) | Attribute a revenue change in a supplied scenario |
| 5.3 Decision logs | Recording what was decided, on what evidence, and the expected outcome | Start a decision log for P3 |
| 5.4 Value of information | Estimating whether an analysis or experiment is worth running | Compute the value of a two-week test for a pricing decision |

**Check your understanding:** (1) Why keep a holdout after a successful launch? (2) What would make you doubt a post-launch "win"? (3) When is an analysis not worth doing?

### Chapter 6 · Decision dashboards (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Decision-first design | Each chart answers a question tied to an action; metric trees | Redesign a vanity dashboard into a decision dashboard |
| 6.2 Uncertainty on screen | Intervals, fan charts, small-sample warnings, annotations for known events | Add honest uncertainty to a KPI dashboard |
| 6.3 Building them | Streamlit, Shiny for Python, Quarto dashboards; data freshness and access control | Build a decision dashboard for the P3 system |
| 6.4 Self-serve and AI-assisted analytics | Semantic layers and text-to-SQL assistants (depth in DAN304 and DAN401); where they mislead | Test an AI analytics assistant on ten questions and log errors |

**Check your understanding:** (1) What makes a dashboard a decision tool? (2) How do you show that a daily change is noise? (3) What should an AI analytics assistant never answer without a human check?

### Chapter 7 · Writing analyses that change decisions (weeks 9–10)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 The memo | Question, answer first, evidence, uncertainty, recommendation, what would change the conclusion | Rewrite a 30-slide deck as a two-page memo |
| 7.2 Narrative memos | Amazon's six-page narrative format; silent reading; appendices for methods | Write a six-page memo for P3 |
| 7.3 Presenting to executives | The first two minutes; handling "just give me the number"; disagreement with senior opinion | Present P3 in five minutes to a mock leadership panel |
| 7.4 Reviewing AI-drafted reports | Hallucinated numbers, overclaiming, missing caveats | Audit an assistant-drafted analysis report line by line |

**Check your understanding:** (1) Why put the recommendation first? (2) How do you present a result that contradicts a leader's belief? (3) Which sentences in an AI-drafted report must be traced to a number?

### Chapter 8 · Stakeholders, intake and scoping (weeks 10–11)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Problem intake | Intake forms, decision statements, success criteria | Run intake for three real requests from classmates' projects |
| 8.2 Scoping and estimation | Breaking work into checkable milestones; estimating effort | Scope a request into a two-week plan |
| 8.3 Saying no and saying "not yet" | Prioritisation by value and feasibility | Write a decline note with an alternative |
| 8.4 Working with product, engineering and legal | Shared vocabulary, review gates, documentation | Map review gates for a model touching personal data |

**Check your understanding:** (1) What three questions must every intake answer? (2) How do you decline a request without losing trust? (3) When must legal review a model?

### Chapter 9 · Ethics, fairness and accountability (week 12)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Proxy labels and harm | Cost as a proxy for need (Obermeyer et al., 2019); label choice as an ethical decision | Find the proxy problem in three supplied model specs |
| 9.2 Fairness reviews | Group metrics, documentation, mitigation decisions and who signs them | Run a fairness review of the P3 system |
| 9.3 Privacy law in practice | DPDP Act 2023 and DPDP Rules 2025 (consent, purpose limitation, data minimisation, phased compliance); EU AI Act risk tiers; NIST AI Risk Management Framework | Write a compliance checklist for P3 |
| 9.4 Documentation | Model cards and datasheets as living documents | Update the model card after the fairness review |

**Check your understanding:** (1) Why is the choice of label an ethical decision? (2) Which DPDP principles constrain feature selection? (3) Who should sign off a fairness trade-off?

### Chapter 10 · Incidents and post-mortems (week 13)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Failure modes | Silent data bugs, upstream schema changes, feedback loops, forecast regime changes (Zillow Offers, 2021) | Classify ten public incidents by failure mode |
| 10.2 Incident response | Detection, rollback, fallback, communication | Run a live incident drill on your P3 system |
| 10.3 Blameless post-mortems | Timeline, contributing factors, actions, follow-up | Write the post-mortem for the drill |
| 10.4 Prevention | Recurring causes across incidents; data contracts with upstream teams, canary scoring, input validation at the boundary | Turn three post-mortems into two preventive controls and test them |

**Check your understanding:** (1) What made Zillow's forecast error a business-level failure? (2) What is your fastest safe rollback for each P3 component? (3) Why are post-mortems blameless?

### Chapter 11 · AI agents in the data science workflow (week 14)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Governing agent-generated analysis | Review requirements, provenance, reproducibility, who is accountable | Write a team policy for agent-generated analyses |
| 11.2 Audit trails | Logging prompts, code, data versions and outputs | Reproduce an agent's analysis from its trail |
| 11.3 Evaluating assistants for your team | Task-specific test sets, error logs, cost | Score two assistants on 20 team tasks |
| 11.4 Your role in an agent-heavy team | Designer of evaluations, reviewer of analyses, owner of decisions; which skills to keep sharp without AI | Write a personal one-year AI-off practice plan |

**Check your understanding:** (1) Who is accountable for an analysis an agent wrote? (2) What must an audit trail contain to reproduce a number? (3) How would you decide whether an assistant is good enough for a task?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Outputs, owners and debt | RACI |
| 2 | 2 | Lab 1 (cont.): Notebook to package | — |
| 3 | 3 | Lab 2 · Batch scorer | — |
| 4 | 3 | Lab 2 (cont.): API and shadow mode | **P1 due** |
| 5 | 4 | Lab 3 · Drift alerts with false-alarm budgets | — |
| 6 | 4–5 | Lab 4 · Performance before labels | — |
| 7 | 5 | Lab 5 · Holdouts and attribution | Mid-term (AI off) |
| 8 | 6 | Lab 6 · Decision dashboard | — |
| 9 | 7 | Memo clinic I | — |
| 10 | 7–8 | Memo clinic II; intake simulation | **P2 due** |
| 11 | 8 | Lab 7 · Scoping and stakeholder role-play | — |
| 12 | 9 | Lab 8 · Fairness and privacy review | P3 checkpoint |
| 13 | 10 | Lab 9 · Incident drill and post-mortem | — |
| 14 | 11 | Lab 10 · Agent governance | **P3 due** |
| 15 | Review | Leadership panel on P3 | Final exam (AI off) |

## Working with AI in this course

- **Use AI for:** packaging boilerplate, FastAPI and test scaffolding, monitoring code (Evidently, NannyML), dashboard layouts, first drafts of runbooks and memo structure. Claude Code, GitHub Copilot, ChatGPT and the Databricks Assistant help; AI analytics assistants are studied as tools in Lesson 6.4.
- **Do without AI (drills):** the decision statement and recommendation of every memo; alert-threshold reasoning; incident triage in the live drill; the five-minute executive presentation; ethics and privacy judgements. The mid-term and final are AI-off.
- **Verify AI output by:** (1) tracing every number in a drafted report to a query or notebook cell; (2) running generated monitoring on known-stable data to measure its false-alarm rate; (3) reproducing generated analyses from the audit trail; (4) testing generated services against the training pipeline for feature parity.
- **Where AI still fails here:** drafted reports can state numbers that appear nowhere in the data and omit caveats; text-to-SQL assistants can answer a different question than the one asked. In Labs 6 and 10 you will log each such error you find, by type, and use the log to write your team's agent policy.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (10) | 20% |
| Projects P1–P3 | 40% |
| Memo and presentation assignments | 10% |
| Mid-term (AI off) | 10% |
| Final exam (AI off) + leadership panel on P3 | 20% |

**Mastery gate.** You pass when you can: (1) take a trained model to a monitored deployment with a rollback plan and alerting whose false-alarm rate you measured; (2) handle a live incident drill end to end, including rollback, stakeholder communication and a post-mortem; (3) write a memo that a panel of non-specialists can act on, with the recommendation, evidence, uncertainty and conditions for reversal, and defend it in five minutes.

## Industry reality

Public accounts of data science in production include Booking.com's 150-model study (2019), Google's papers on ML technical debt (Sculley et al., 2015) and the ML Test Score rubric for production readiness (Breck et al., 2017), and Google's "Rules of Machine Learning" guide. Zillow's 2021 wind-down of its home-buying business (8-K, 2 Nov 2021) is a public case of forecast risk becoming business risk; Obermeyer et al. (2019) is the standard case of label choice causing harm. In India, the DPDP Act and Rules now shape what personal data a model may use and for what purpose.

**Interview questions from this course**

1. *Your churn model's precision dropped 20% last month. Walk me through it.* Strong answer: checks data pipeline and schema changes first, then input and prediction drift, label definition and delay, seasonality and campaign effects; compares with holdout; decides rollback vs retrain; communicates.
2. *How would you deploy a model that scores loan applications?* Strong answer: real-time vs batch need; feature parity; shadow mode then canary; fallback rules; monitoring incl. calibration and fairness; documentation and approvals; audit logging.
3. *The model launched and revenue went up 3%. Did the model do it?* Strong answer: asks about holdouts and guardrails; separates seasonality, marketing and mix shifts; uses the holdout or a DiD design; reports an interval.
4. *Tell me about an analysis that changed a decision.* Strong answer: clear decision statement, the evidence, how uncertainty was communicated, stakeholder resistance and how it was handled, and the measured outcome.
5. *What would make you stop a model launch?* Strong answer: guardrail breaches, fairness or privacy findings, proxy-label problems, monitoring gaps, missing rollback, or evidence that offline gains will not transfer; explains who decides.

## Resources (free first)

- **Guides:** Google, "Rules of Machine Learning" — https://developers.google.com/machine-learning/guides/rules-of-ml ; Breck et al., "The ML Test Score" — https://research.google/pubs/the-ml-test-score-a-rubric-for-ml-production-readiness-and-technical-debt-reduction/ ; Sculley et al., "Hidden Technical Debt in Machine Learning Systems" — https://papers.nips.cc/paper/5656-hidden-technical-debt-in-machine-learning-systems
- **Tools:** MLflow — https://mlflow.org/docs/latest/ ; Evidently — https://docs.evidentlyai.com/ ; NannyML — https://nannyml.readthedocs.io/ ; FastAPI — https://fastapi.tiangolo.com/ ; Streamlit — https://docs.streamlit.io/ ; Shiny for Python — https://shiny.posit.co/py/ ; Quarto — https://quarto.org/ ; uv — https://docs.astral.sh/uv/ ; pandera — https://pandera.readthedocs.io/
- **Communication:** Claus Wilke, *Fundamentals of Data Visualization* — https://clauswilke.com/dataviz/ ; Amazon 2017 letter to shareholders (six-page narratives) — https://www.sec.gov/Archives/edgar/data/1018724/000119312518121161/d456916dex991.htm
- **Ethics and law:** Mitchell et al., model cards — https://arxiv.org/abs/1810.03993 ; Gebru et al., datasheets — https://arxiv.org/abs/1803.09010 ; DPDP Rules 2025 (PIB) — https://www.pib.gov.in/PressReleasePage.aspx?PRID=2190014 ; EU AI Act — https://eur-lex.europa.eu/eli/reg/2024/1689/oj ; NIST AI RMF — https://www.nist.gov/itl/ai-risk-management-framework
- **Paid, optional:** Chip Huyen, *Designing Machine Learning Systems* (O'Reilly); Barbara Minto, *The Pyramid Principle*.

## Sources

- Bernardi, Mavridis and Estevez, KDD 2019 — https://doi.org/10.1145/3292500.3330744 ; The Morning Paper summary — https://blog.acolyer.org/2019/10/07/150-successful-machine-learning-models/ (checked 2026-10)
- Sculley et al., NeurIPS 2015 — https://papers.nips.cc/paper/5656-hidden-technical-debt-in-machine-learning-systems (checked 2026-10)
- Obermeyer et al., *Science* 366 (2019) — https://doi.org/10.1126/science.aax2342 (checked 2026-10)
- Zillow Group Form 8-K Exhibit 99.1 (2 Nov 2021) — https://www.sec.gov/Archives/edgar/data/1617640/000161764021000085/q32021991.htm (checked 2026-10)
- Amazon.com, 2017 Letter to Shareholders, Form 8-K Exhibit 99.1 (filed 18 Apr 2018) — https://www.sec.gov/Archives/edgar/data/1018724/000119312518121161/d456916dex991.htm (checked 2026-10)
- Press Information Bureau, "Government notifies DPDP Rules" (Nov 2025) — https://www.pib.gov.in/PressReleasePage.aspx?PRID=2190014 (checked 2026-10)
- Regulation (EU) 2024/1689 (AI Act) — https://eur-lex.europa.eu/eli/reg/2024/1689/oj ; NIST AI Risk Management Framework — https://www.nist.gov/itl/ai-risk-management-framework (checked 2026-10)

_Last reviewed: 2026-10_
