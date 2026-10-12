# MLE302 · Labs and projects

Design work is graded on written documents, diagrams and small working prototypes. Every design states its assumptions and numbers, and every number has a derivation. Use public data (NYC TLC trip records, the Olist Brazilian e-commerce dataset, Criteo or Avazu click logs, MovieLens) for the prototypes. Any figure you assume for a real company is labelled illustrative unless it comes from that company's published material.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Framing and metric trees | Frame 4 product requests (one should not use ML); ask an AI assistant for a design and mark every unsupported number and missing failure mode | Framing table; metric trees; the annotated AI design | 3 h |
| 2 · Estimation and latency budgets | QPS, storage and embedding-memory estimates; split a 100 ms budget across 5 stages | Calculation sheet; a budget table with p99 targets | 3 h |
| 3 · Labels, delay and position bias | Define a fraud label with a maturity window; simulate position bias in logged clicks and correct it with inverse propensity weighting | Label spec; bias simulation with before/after estimates | 4 h |
| 4 · Point-in-time joins and skew | Build a point-in-time feature join in SQL (DuckDB) on NYC taxi data; plant and detect 3 skew bugs | Join code with tests; a skew-detection report | 4 h |
| 5 · Losses and distributional outputs | Train MAE, quantile and asymmetric losses for an ETA target; predict p50 and p90 | Calibration of quantiles (share of trips under p90); a recommendation of what to show users | 4 h |
| 6 · Multi-stage serving and p99 | A two-stage retrieval + ranking service (FastAPI) with a cache and a fallback; load-test it | p50/p99 latency under load, before and after optimisation; fallback test | 5 h |
| 7 · Experiment design | Power calculations; an interleaving simulation; a switchback design for a rider-assignment change | Experiment plans with randomisation units, metrics and guardrails | 3 h |
| 8 · Feedback-loop simulation | A popularity recommender over 10 simulated rounds, with and without exploration | Coverage and Gini plots; the cost of exploration in clicks | 4 h |
| 9 · Build vs buy and cost model | Compare 3 serving options for one model on cost per 1,000 predictions and operational load | A 1-page memo with a cost table | 3 h |
| C1–C3 · Case-study critiques (3 assignments) | For Swiggy/Zomato/Uber ETA, Stripe/Google/Facebook fraud and ads, Airbnb/Flipkart/Meesho ranking: redraw the system, list the evidence, list 5 open questions and 3 risks | Three 2-page critiques citing the original posts | 3 h each |

## Projects

### P1 · Design document: delivery-time promise for a food or grocery app (L1, ~6 hours)

**Real-world inspiration.** Swiggy decomposes delivery time into assignment, first mile, preparation and last mile, and has moved to predicting full distributions (Swiggy Bytes, 2018–2026). Zomato predicts food-preparation time with dish embeddings and quantile losses (2020, 2022). Uber's DeepETA predicts a correction on top of a routing engine (2022).

**What to build.** A 4–6 page design document for the delivery-time promise shown at checkout for a quick-commerce or food-delivery app in an Indian city (illustrative scenario), using the course template.

**Acceptance criteria**
- Framing separates the prediction (a distribution of delivery time) from the decision (the promise shown) and states the cost of early and late errors.
- At least 15 features, each labelled batch, streaming or on-demand, with its freshness requirement and point-in-time rule.
- A latency budget for scoring 300 stores or restaurants per listing page, with the arithmetic shown.
- An offline plan (time-based backtests, quantile calibration) and an online plan that addresses marketplace interference (switchback or geo-randomisation).
- A monitoring section with at least 5 alerts and a fallback for each failure of a dependency.
- Every claim about a real company cites its post.

**Stretch goals.** A 1-page "alternatives considered" section with a residual model vs end-to-end model comparison.

**What it proves to an employer.** You can write the design document that starts every ML project, with numbers, trade-offs and failure modes.

### P2 · Real-time fraud scoring prototype (L2, ~15 hours)

**Real-world inspiration.** Stripe Radar scores each payment using more than 1,000 characteristics in under 100 ms and moved from a Wide & Deep model to a DNN-only architecture in 2022 (Stripe, 2023). Google's ad-click system showed how online learning keeps models fresh (McMahan et al., 2013).

**What to build.** On a public fraud dataset (for example IEEE-CIS Fraud Detection or the synthetic PaySim mobile-money data), build a working prototype: an event stream replayed from files, streaming velocity features (counts and amounts per card or account over 1 h and 24 h), a GBDT model, a scoring API, a rules layer, and a decision log. Write the design document alongside.

**Acceptance criteria**
- Features are computed identically offline (for training) and online (for scoring); a test replays 10,000 events and shows zero mismatches.
- The scoring API meets p99 under 50 ms at 200 requests per second on a laptop, measured with a load-testing tool, with the hardware stated.
- Labels use a maturity window, and the design explains the selection bias from blocked transactions and how you would measure it.
- Evaluation reports precision and recall at a fixed review capacity, by time week, with confidence intervals.
- A fallback (rules-only) path activates when the model service times out, and a test proves it.
- The design document covers retraining cadence, drift alerts and an adversarial-adaptation plan.

**Stretch goals.** An exploration slice (a small random share of low-risk transactions allowed through to collect labels) with its expected cost; shadow scoring of a second model.

**What it proves to an employer.** You can build an ML service that meets latency and correctness requirements, not just a notebook, which is the core of most ML engineering jobs.

### P3 · End-to-end multi-stage ranking system with an experiment plan (L3, portfolio-grade, ~30 hours)

**Real-world inspiration.** Instagram Explore uses retrieval, a two-tower first stage, a multi-task second stage and final re-ranking (Meta, 2023). Meesho's feed ranker predicts both click and purchase probabilities (2023), and Flipkart ranks ads and organic results with one model (2025). Netflix showed interleaving can need over 100× fewer users than A/B tests (2017).

**What to build.** On the Olist e-commerce data or MovieLens, a working ranking system: embedding-based candidate retrieval, a ranking model with a multi-objective value function (for example click and purchase, or watch and rating), business re-ranking rules (diversity, freshness), a serving API with a latency budget, offline evaluation, and a simulated online evaluation comparing A/B testing with interleaving on synthetic users.

**Acceptance criteria**
- A design document (8–10 pages) with framing, estimates, data and labels, features, models, serving, evaluation, monitoring and feedback loops.
- Retrieval recall@100 and ranking NDCG@10 reported on a time-based test split, with bootstrap CIs, against a popularity baseline.
- End-to-end p99 latency under 150 ms for one request on a laptop, with a per-stage latency breakdown.
- The value function's weights are justified, and a sensitivity analysis shows how ranking changes as they move.
- The simulation reports how many synthetic users each method (A/B vs interleaving) needs to detect a planted improvement.
- A feedback-loop analysis: catalogue coverage after 10 simulated retraining rounds, with and without exploration.
- A recorded 15-minute design review (or live presentation) answering reviewers' questions.

**Stretch goals.** Position-bias correction in training data; a cold-start path for new items; a cost model for serving at 10 million daily users.

**What it proves to an employer.** You can design, build and evaluate a multi-stage ML system end to end and defend it in a design review, which is the bar for mid-level and senior ML engineers.

## Feeds into

- [MLE402 Distributed Training](../../year_4/MLE402_distributed_training_and_large_scale_ml/README.md): the scale estimates from Chapter 2 become real cluster plans.
- [MLE403 Ranking and Recommendation](../../year_4/MLE403_ranking_and_recommendation_systems_at_scale/README.md): P3 grows into a production-scale recommender.
- [MLE401 MLOps](../../year_4/MLE401_mlops_deployment_monitoring_and_retraining/README.md): P2's service gets CI/CD, canaries and monitoring.
- [CAR401 Career Lab II](../../../../05_shared_years_3_to_5/CAR401_career_lab_ii_interviews_system_design_and_ai/README.md): your mock-interview record and design documents feed interview preparation.
- [IND401 Industry Co-op Studio](../../../../05_shared_years_3_to_5/IND401_industry_co_op_studio/README.md): the design-document template is used for the co-op project.
