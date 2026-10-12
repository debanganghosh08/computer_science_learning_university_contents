# DSC404 · Labs and projects

The projects reuse your own earlier work: a model from DSC302 or DSC305 and a forecasting or text system from DSC401 or DSC402. Every deliverable has three parts: **an artefact that runs** (one command, pinned environment), **evidence it is right** (tests, monitoring with a measured false-alarm rate) and **a document a decision-maker reads** (memo, model card or runbook). Deploy only on free tiers or your own machine; no paid infrastructure is required.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Outputs, owners, debt and packaging | Classify deliverables and write a RACI; find technical-debt patterns; package a past project with `uv`, config, logging, pandera checks and behaviour tests, registered in MLflow | RACI; debt list with fixes; a repository a classmate installs and runs in under 10 minutes | 6 h (2 weeks) |
| 2 · Batch scorer, API and shadow mode | Nightly scorer with idempotent writes, run metadata and backfill; FastAPI service with input validation and p95 latency; shadow comparison against the batch model | Test proving re-runs do not duplicate scores; latency report; decision-agreement rate in shadow mode | 7 h (2 weeks) |
| 3 · Drift alerts with false-alarm budgets | PSI and KS drift checks across 50 features on stable data and on injected shifts | False-alarm rate before and after multiple-testing control; detection delay | 3 h |
| 4 · Performance before labels | Estimate performance with NannyML's confidence-based method during simulated label delay; compare with realised performance | Estimated vs actual curves; when the estimate failed and why | 3 h |
| 5 · Holdouts and attribution | Analyse a supplied post-launch dataset with a holdout, seasonality and a concurrent campaign | Attribution memo with an interval | 3 h |
| 6 · Decision dashboard and AI analytics test | Build a decision dashboard (Streamlit, Shiny or Quarto) with uncertainty; test an AI analytics assistant on ten questions | Dashboard link or screenshots; assistant error log | 4 h |
| 7 · Scoping and stakeholder role-play | Intake, scoping and a decline note for three requests | Intake forms; two-week plan; decline note | 2 h |
| 8 · Fairness and privacy review | Fairness metrics and a DPDP-based privacy checklist for a past model | Review document with decisions and sign-off roles | 3 h |
| 9 · Incident drill and post-mortem | A surprise upstream schema change breaks your scorer; detect, roll back, communicate | Incident timeline; blameless post-mortem | 3 h |
| 10 · Agent governance | Score two assistants on 20 team tasks; reproduce one agent analysis from its audit trail; draft a team policy | Score sheet; reproduction notes; one-page policy | 3 h |

## Projects

### P1 · Ship a model properly (L1, ~6 hours)

**Real-world inspiration.** Many models never reach users because they cannot be rerun, tested or explained by anyone except their author. Google's "Rules of Machine Learning" and the ML Test Score rubric list what production readiness requires.

**What to build.** Take your DSC302 or DSC305 P3 model and ship it as a nightly batch scorer with tests, a model registry entry, a model card and a runbook.

**Acceptance criteria**
- One command installs the pinned environment and produces scores for a given date; re-running the same date produces identical output.
- Tests cover feature logic, schema validation and at least three behavioural expectations (for example, monotonicity in a key feature).
- The MLflow entry links model, code commit and data version.
- The model card states intended use, out-of-scope uses, metrics by slice and known limitations.
- The runbook says how to roll back to the previous version in under 5 minutes, and a classmate does it successfully from the runbook alone.

**Stretch goals.** Add a real-time endpoint with measured p95 latency; score the ML Test Score rubric for your system and close two gaps.

**What it proves to an employer.** Your work can be run, trusted and maintained by others, which is the threshold for being given production responsibility.

### P2 · Monitoring through a regime change (L2, ~15 hours)

**Real-world inspiration.** Credit models trained in calm years faced very different default rates in 2008–2009; forecasting models broke during the 2020 lockdowns. Monitoring must detect such shifts before labels arrive, without flooding teams with false alarms.

**What to build.** Replay a historical stream month by month through your deployed model (the Freddie Mac loan-level data from DSC305 P3 across 2005–2010, or NYC TLC data across 2019–2021) with realistic label delay, and build monitoring that detects data drift, estimates performance before labels arrive, tracks calibration and triggers documented actions.

**Acceptance criteria**
- The replay respects label delay (for example, 12-month default labels become available 12 months later).
- Drift alerts have a measured false-alarm rate on a stable period of at most one per month, after multiple-testing control.
- Estimated performance before labels is plotted against realised performance, and the gap is explained.
- At least one alert leads to a documented action (recalibrate, retrain, fall back to rules or do nothing), with evidence that the action helped or a reasoned explanation if it did not.
- A one-page monitoring specification lists metrics, thresholds, owners and responses.

**Stretch goals.** Compare scheduled vs triggered retraining over the replay; add a fairness metric to monitoring and show how it moves during the shift.

**What it proves to an employer.** You can keep a model honest after launch, including during the kind of shock that breaks most models.

### P3 · An end-to-end decision system (L3, portfolio-grade, ~30 hours)

**Real-world inspiration.** The best public evidence on data science in production (Booking.com's 150 models; post-mortems such as Zillow Offers) shows that value comes from the whole loop: framing, modelling, deployment, measurement and communication. This project is the main building block of the major's [flagship industry project](../../../../06_career_and_market_readiness/05_industry_projects/DSC_data_science.md).

**What to build.** Turn one earlier system into a complete decision product for a named (real or illustrative) decision-maker: for example, the DSC401 P2 air-quality forecaster as a daily advisory service, the DSC401 P3 forecaster as a replenishment recommender, or the DSC402 P1 classifier as a complaint-triage service. Deliver the running system, monitoring, a dashboard, an impact-measurement plan, a privacy and fairness review, an incident drill and a six-page narrative memo.

**Acceptance criteria**
- The system runs on a schedule (free tier or local) for at least two weeks before the deadline, with logs proving it.
- Monitoring covers data quality, drift, model performance (or its estimate) and the decision metric, with measured false-alarm rates.
- The dashboard is decision-first: each view states the question it answers and shows uncertainty.
- An impact-measurement plan specifies a holdout, randomized rollout or quasi-experimental design (from DSC304), the primary metric and the minimum detectable effect.
- A privacy and fairness review applies the DPDP principles (purpose, consent, minimisation, retention) and documents decisions.
- An unannounced incident drill run by the instructor is handled with rollback within the documented time and a post-mortem.
- A six-page narrative memo is read silently by a panel and defended in a 20-minute discussion; the panel's questions and your answers are appended.

**Stretch goals.** A real external user (a club, NGO, small business or campus office) uses the system for two weeks and gives written feedback; an agent-assisted maintenance workflow governed by your Lab 10 policy.

**What it proves to an employer.** You can own a data science product from question to measured outcome, which is what senior and lead data scientists are hired to do, and what a founder needs to do alone.

## Feeds into

- [Flagship industry project](../../../../06_career_and_market_readiness/05_industry_projects/DSC_data_science.md): P3 is its core.
- [THS501](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md) and [THS502](../../../../05_shared_years_3_to_5/THS502_thesis_or_capstone_ii/README.md): an industry capstone can extend P3 with a real partner.
- [LCH502 Career Launch and Founder Studio](../../../../05_shared_years_3_to_5/LCH502_career_launch_and_founder_studio/README.md): the memo and system are portfolio centrepieces; a decision product with a real user is a founder's first proof point.
