# DSC403 · Labs and projects

All offline results use **one shared evaluation harness**: a global temporal split, full-catalogue ranking metrics, user-level bootstrap intervals and at least three tuned baselines (popularity, item-kNN, EASE or ALS). Any model that has not been compared in this harness is not reported. Record compute time for every model.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Objectives, signals and baselines | Objectives and guardrails for three products; signal maps for MIND and Yambda; global, recent and segment popularity, item-kNN with sparse matrices and EASE on MovieLens 32M | Objective sheets; signal table; metrics with intervals; memory and time per model | 5 h (2 weeks) |
| 2 · MF from scratch | Biased MF with SGD and with ALS on explicit ratings | Validation curves; speed comparison | 4 h |
| 3 · Implicit ALS vs BPR | `implicit` ALS with confidence weights vs BPR; three negative-sampling schemes | Ranking metrics and popularity lift for each | 3 h |
| 4 · Evaluation harness (AI off for the split design) | Build the shared harness; compare random vs temporal splits and sampled vs full metrics; log assistant-generated harness flaws | Harness with tests; a documented ranking reversal | 5 h (2 weeks) |
| 5 · Cold start on MIND | Title-embedding content model vs CF vs hybrid on new articles | Cold-start slice metrics with intervals | 3 h |
| 6 · Two-tower in PyTorch | In-batch negatives with and without sampling-bias correction; approximate nearest-neighbour retrieval | Recall@100 by item popularity bucket; retrieval latency | 4 h |
| 7 · Bandit simulation | ε-greedy, UCB, Thompson sampling and LinUCB in a simulated news environment | Regret curves; recommended exploration budget | 3 h |
| 8 · Off-policy evaluation and interleaving | IPS, SNIPS, direct method and doubly robust on the Open Bandit Dataset; team-draft interleaving vs A/B sensitivity for two rankers | Estimates with intervals and support diagnostics; samples needed to detect a difference in each online design | 5 h (2 weeks) |
| 9 · Feedback-loop simulation | Retrain a recommender for 20 rounds on its own outputs; track homogeneity and utility | Plots and a mitigation tested | 3 h |
| 10 · LLM re-ranking | Re-rank top-50 candidates with an LLM; test position bias by shuffling inputs | Metric change, cost per 1,000 users, position-bias rate | 3 h |

## Projects

### P1 · Honest baselines on MovieLens 32M (L1, ~6 hours)

**Real-world inspiration.** The reproducibility study by Ferrari Dacrema et al. (2019) found that tuned simple methods often beat published neural recommenders. Every recommender team needs a trustworthy baseline before any complex model.

**What to build.** A temporal-split evaluation of five baselines (global popularity, recent popularity, item-kNN, EASE, implicit ALS) on MovieLens 32M, treating ratings of 4 or more as positive interactions, with a short report.

**Acceptance criteria**
- The split is global in time (training before a cut-off date, testing after), and the report shows how much a random split inflates Recall@20 and NDCG@10.
- Metrics are computed against the full catalogue for every test user, with user-level bootstrap intervals.
- Each baseline is tuned on a validation period that precedes the test period.
- Coverage and popularity lift are reported alongside accuracy.
- The harness is packaged so later labs and projects reuse it unchanged.

**Stretch goals.** Show a ranking reversal between full and sampled metrics; add a sequential baseline (most recent items' neighbours).

**What it proves to an employer.** You can set up recommender evaluation that the rest of a team can trust.

### P2 · News recommendation with cold start (L2, ~15 hours)

**Real-world inspiration.** News articles are always new, so collaborative filtering alone fails. Microsoft's MIND dataset, built from Microsoft News logs, contains about 160,000 English articles and more than 15 million impression logs from 1 million users, with clicked and non-clicked items in each impression.

**What to build.** A news recommender that ranks the candidates in each impression using content embeddings of titles and abstracts, user histories and recency, compared with popularity and CF baselines, with special attention to articles unseen in training.

**Acceptance criteria**
- Results on the MIND validation set use the standard impression-level metrics (AUC, MRR, nDCG@5, nDCG@10).
- Performance is reported separately for impressions whose candidates are all new articles.
- At least two embedding models are compared, with cost and latency to embed 100,000 articles.
- An ablation shows the contribution of history, content and recency features with intervals.
- A one-page product note proposes how the model would be tested online (metric, guardrails, interleaving or A/B) and what novelty effects to expect.

**Stretch goals.** A contextual-bandit layer for exploration on new articles, evaluated in simulation; a diversity re-ranker and its accuracy cost.

**What it proves to an employer.** You can build personalization that works when items are always new, the hardest case for recommenders.

### P3 · Music recommendation and its feedback loop (L3, portfolio-grade, ~30 hours)

**Real-world inspiration.** Music streaming services recommend from catalogues of millions of tracks, and much listening is itself caused by recommendations. Yandex's Yambda dataset (up to 4.79 billion interactions from 1 million users over 9.39 million tracks) marks whether each interaction was organic or recommendation-driven and includes audio embeddings, which makes the feedback loop measurable on real data.

**What to build.** Using a released subset of Yambda or a documented user sample, build and compare three recommender families (item-kNN or EASE, implicit ALS, a two-tower model using audio embeddings), then study how training on recommendation-driven vs organic interactions changes accuracy, popularity bias and catalogue coverage. Finish with a re-ranking that improves calibration or long-tail exposure and quantify its cost.

**Acceptance criteria**
- The shared harness is used with a global temporal split; data volume, sampling method and hardware are documented.
- All three families are tuned and reported with full-catalogue metrics and user-level intervals.
- The organic-vs-all training comparison reports accuracy on organic test interactions, popularity lift and coverage, with interpretation.
- Audio embeddings are shown to help (or not) for tracks with few interactions.
- The re-ranking experiment reports the accuracy–diversity or accuracy–calibration trade-off curve.
- A product review document recommends a model and an online test plan with retention guardrails, and states the limits of what offline data can show about feedback loops.

**Stretch goals.** A simulation calibrated to your data that projects homogeneity after repeated retraining; an LLM-based re-ranker evaluated for cost and position bias; a privacy review of the features used.

**What it proves to an employer.** You can build competitive recommenders on industrial-scale data and reason about their effects on users and the catalogue, which is the job of a senior personalization data scientist.

## Feeds into

- [DSC501 Frontier Seminar](../../year_5/DSC501_frontier_seminar_bayesian_methods_causal_ml/README.md): off-policy evaluation and policy learning connect to causal ML.
- [MLE403 Ranking and Recommendation Systems at Scale](../../../machine_learning_engineering/year_4/MLE403_ranking_and_recommendation_systems_at_scale/README.md): P3's models become candidates for a production multi-stage system.
- [OV08B Product Analytics and Growth for AI Apps](../../../../04_overlaps/OV08_full_stack_ai_product_engineering/OV08B_product_analytics_and_growth_for_ai_apps/README.md): online testing of personalization features.
- [THS501 Thesis or Capstone I](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md): feedback loops with organic/recommended labels are an open research topic.
