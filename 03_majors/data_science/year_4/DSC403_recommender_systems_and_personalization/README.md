# DSC403 · Recommender Systems and Personalization

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 4 · 8 | 4 (≈ 120 hours) | L3 → L4 | [DSC303](../../year_3/DSC303_data_wrangling_at_scale_pandas_polars_and_spark/README.md) (uses [DSC302](../../year_3/DSC302_applied_machine_learning_for_data_scientists/README.md), [DSC304](../../year_3/DSC304_experimental_design_and_causal_inference/README.md) and [DSC305](../../year_3/DSC305_feature_engineering_and_model_evaluation/README.md)) | [DSC501](../../year_5/DSC501_frontier_seminar_bayesian_methods_causal_ml/README.md), [MLE403](../../../machine_learning_engineering/year_4/MLE403_ranking_and_recommendation_systems_at_scale/README.md), [OV08B](../../../../04_overlaps/OV08_full_stack_ai_product_engineering/OV08B_product_analytics_and_growth_for_ai_apps/README.md), [THS501](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md) |

Part of the [Data Science major](../../README.md). This course covers the modelling, evaluation and experimentation side of recommendation and personalization. Serving multi-stage recommenders at large scale (feature pipelines, approximate nearest-neighbour infrastructure, latency budgets) is the subject of [MLE403](../../../machine_learning_engineering/year_4/MLE403_ranking_and_recommendation_systems_at_scale/README.md).

## Why this course matters now

Recommendations decide much of what people watch, buy, read and hear, and their quality is judged by experiments on long-term behaviour, not by offline accuracy. Netflix describes improving its recommender through A/B tests focused on member retention and medium-term engagement, combined with offline experiments on historical data (Gomez-Uribe and Hunt, 2015). Offline evaluation is easy to get wrong: a systematic study of 18 neural top-n recommendation algorithms from top conferences could reproduce only 7 with reasonable effort, and 6 of those were often beaten by simple nearest-neighbour or graph heuristics (Dacrema et al., 2019); sampled ranking metrics, widely used to save compute, can even reverse which model looks better (Krichene and Rendle, 2020). Recommenders also change the data they learn from: simulations show feedback loops increasing homogeneity and lowering utility (Chaney et al., 2018). New public data make these problems studiable: MovieLens 32M (2024), Microsoft's MIND news data, the fully observed KuaiRec matrix, and Yandex's Yambda-5B with 4.79 billion music interactions that flag which listens came from recommendations. LLMs now generate item embeddings, re-rank candidates and power conversational recommenders. What remains human: choosing the objective, building evaluation you can trust, running the experiments, and owning effects on users and suppliers.

## Learning outcomes

By the end you can:

1. **Frame** a personalization problem: objective (short- and long-term), feedback signals, exposure, constraints and stakeholders (users, suppliers, the platform).
2. **Implement** strong baselines (popularity, item-kNN, EASE) and **explain** why they are often hard to beat.
3. **Build** matrix-factorization models for explicit and implicit feedback (ALS with confidence weights, BPR) and **tune** them correctly.
4. **Design** offline evaluation without leakage (temporal splits, full-catalogue ranking metrics, beyond-accuracy metrics) and **report** results with uncertainty.
5. **Solve** cold-start problems with content embeddings, hybrid models and exploration.
6. **Train** a two-tower retrieval model with in-batch negatives and sampling-bias correction, and **explain** a retrieval + ranking architecture.
7. **Use** contextual bandits for exploration and **evaluate** policies offline with inverse propensity scoring and doubly robust estimators.
8. **Run** online evaluation for recommenders (A/B tests, interleaving, long-term holdouts) and **interpret** effects on engagement, retention and diversity.
9. **Measure and mitigate** popularity bias, miscalibration and feedback loops, and **apply** privacy and consent constraints to personalization.

## Chapters and lessons

### Chapter 1 · Recommendation as a decision problem (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 What a recommender optimises | Clicks vs watch time vs retention vs revenue; proxy objectives and their failure modes | Write the objective and guardrails for a news, a music and a grocery recommender |
| 1.2 Feedback signals | Explicit ratings vs implicit views, plays, purchases; negative feedback; dwell time | Map signals in MIND and Yambda to their meaning and biases |
| 1.3 Exposure and selection | Users can only interact with what they were shown; missing-not-at-random feedback | Show how popularity of exposure shapes observed popularity |
| 1.4 Case study: Netflix | Personalisation across rows, A/B tests on retention, offline experiments (Gomez-Uribe and Hunt, 2015) | Summarise which decisions in that paper are statistical and which are product |

**Check your understanding:** (1) Why can optimising clicks harm retention? (2) What does a missing interaction mean in implicit data? (3) Who besides the user is affected by a recommendation?

### Chapter 2 · Baselines and neighbourhood methods (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Popularity and recency | Global, segment and time-decayed popularity | Build three popularity baselines on MovieLens 32M |
| 2.2 Item-to-item collaborative filtering | Co-occurrence and cosine similarity; Amazon's item-to-item approach (Linden et al., 2003) | Implement item-kNN with sparse matrices |
| 2.3 EASE and linear autoencoders | A closed-form item-item model (Steck, 2019) | Fit EASE and compare with item-kNN |
| 2.4 Why baselines win | Tuning baselines properly; the reproducibility study (Dacrema et al., 2019) | Tune item-kNN as carefully as a neural model and compare |

**Check your understanding:** (1) Why is item-to-item CF still common in production? (2) What does EASE's closed form cost in memory? (3) What makes a baseline comparison unfair?

### Chapter 3 · Matrix factorization (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Latent factors | User and item vectors, dot products, biases (Koren, Bell and Volinsky, 2009) | Implement biased MF with SGD on explicit ratings |
| 3.2 Regularization and tuning | L2 penalties, factors, learning rates, early stopping | Tune MF and plot validation curves |
| 3.3 ALS | Alternating least squares, parallelism, closed-form updates | Implement ALS and compare speed and accuracy with SGD |
| 3.4 MF vs neural models | "NCF vs MF revisited" (Rendle et al., 2020): dot products are hard to beat | Compare an MLP scorer with a tuned dot product |

**Check your understanding:** (1) What do user and item bias terms capture? (2) Why does ALS parallelise well? (3) What did the NCF-vs-MF study change in practice?

### Chapter 4 · Implicit feedback (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Confidence-weighted ALS | Preferences vs confidence (Hu, Koren and Volinsky, 2008) | Train implicit ALS on play counts with the `implicit` library |
| 4.2 Pairwise ranking | BPR loss, negative sampling strategies | Train BPR and compare with ALS |
| 4.3 Negative sampling | Uniform vs popularity-based vs hard negatives; their biases | Measure how negative sampling changes the learned popularity bias |
| 4.4 Organic vs recommended interactions | Learning from interactions the system caused; Yambda's organic flags | Train on organic-only vs all interactions and compare |

**Check your understanding:** (1) Why does implicit feedback need confidence weights? (2) What does popularity-based negative sampling do to recommendations? (3) Why does training on recommendation-driven plays create a loop?

### Chapter 5 · Offline evaluation done right (weeks 5–6)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Splits | Random vs leave-last-out vs global temporal splits; leakage from the future | Show how a random split inflates Recall@20 |
| 5.2 Ranking metrics | Recall@k, precision@k, NDCG, MRR, MAP; what each rewards | Compute all metrics by hand for three users |
| 5.3 Full vs sampled metrics | Why sampled metrics can reverse model rankings (Krichene and Rendle, 2020) | Reproduce a ranking reversal with 100 sampled negatives |
| 5.4 Beyond accuracy | Coverage, novelty, diversity, serendipity, popularity lift | Report five beyond-accuracy metrics for three models |
| 5.5 Uncertainty and significance | Bootstrap over users, paired tests, many-comparison caution | Decide whether model B beats A on NDCG@10 |

**Check your understanding:** (1) Why does leave-last-out still leak if splits are not global in time? (2) When can NDCG improve while users see worse recommendations? (3) Why bootstrap over users rather than interactions?

### Chapter 6 · Content, context and cold start (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Content-based models | Item text and image embeddings, user profiles from item vectors | Recommend MIND articles from title embeddings |
| 6.2 Hybrid models | Combining collaborative and content signals; factorization machines | Build a hybrid and measure gains for new items |
| 6.3 Cold start | New users (onboarding questions, popularity priors, context) and new items (content, exploration) | Evaluate on a cold-start slice separately |
| 6.4 Context | Time of day, device, location, session intent | Add session context and measure the change |

**Check your understanding:** (1) Why does pure CF fail for new items? (2) How do you evaluate cold start honestly? (3) When does context matter more than history?

### Chapter 7 · Two-tower retrieval and sequential models (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Retrieval and ranking stages | Candidate generation then ranking (Covington, Adams and Sargin, 2016) | Draw the stages for a video app and assign metrics to each |
| 7.2 Two-tower models | User and item towers, in-batch negatives, sampling-bias correction (Yi et al., 2019) | Train a two-tower model in PyTorch on MovieLens |
| 7.3 Sequential recommendation | Session-based and self-attentive models (SASRec) | Compare SASRec with item-kNN on next-item prediction |
| 7.4 Nearest-neighbour search | Exact vs approximate search; recall vs latency (infrastructure in MLE403) | Measure retrieval recall with an approximate index |

**Check your understanding:** (1) Why does in-batch negative sampling favour popular items, and how is it corrected? (2) Why separate retrieval from ranking? (3) When does a sequential model beat a static one?

### Chapter 8 · Bandits and exploration (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Explore vs exploit | ε-greedy, upper confidence bounds, Thompson sampling | Simulate three bandit strategies and compare regret |
| 8.2 Contextual bandits | LinUCB for news recommendation (Li et al., 2010) | Implement LinUCB on a simulated news environment |
| 8.3 Logging for learning | Propensities, randomisation in production, logging policies | Design the logging schema a bandit needs |
| 8.4 When not to explore | Costs of exploration, safety constraints, minimum quality bars | Set an exploration budget with a quality floor |

**Check your understanding:** (1) Why must you log the probability of each shown item? (2) What does Thompson sampling do with uncertainty? (3) Where is exploration unacceptable?

### Chapter 9 · Off-policy evaluation and online testing (weeks 10–11)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Off-policy estimators | IPS, self-normalised IPS, direct method, doubly robust; variance and support problems | Evaluate policies on the Open Bandit Dataset (ZOZOTOWN) |
| 9.2 A/B testing recommenders | Metrics, randomisation unit, interference through shared inventory, novelty effects | Design an A/B test for a new home-feed model |
| 9.3 Interleaving | Team-draft interleaving and its sensitivity (Chapelle et al., 2012) | Simulate interleaving vs A/B on the same pair of rankers |
| 9.4 Long-term effects | Holdouts, surrogate metrics, retention | Propose a surrogate for 6-month retention and say how to validate it |

**Check your understanding:** (1) Why does IPS fail when the new policy shows items the old one never showed? (2) Why is interleaving more sensitive than A/B testing? (3) How can a model win a 2-week test and lose over 6 months?

### Chapter 10 · Fairness, diversity and feedback loops (week 12)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Popularity bias | Rich-get-richer dynamics; measurement | Measure popularity lift of three models |
| 10.2 Calibrated recommendations | Matching the mix of a user's interests (Steck, 2018) | Re-rank for calibration and measure accuracy cost |
| 10.3 Provider fairness and diversity | Exposure fairness for sellers, artists or creators; diversity constraints | Re-rank to give long-tail sellers a minimum exposure share |
| 10.4 Feedback loops and filter bubbles | Algorithmic confounding (Chaney et al., 2018); simulation studies | Simulate 20 rounds of retraining and track homogeneity |

**Check your understanding:** (1) Why is "users clicked it" weak evidence that a recommendation was good? (2) What does calibration trade away? (3) How would you detect a feedback loop in production data?

### Chapter 11 · LLMs, privacy and the future of personalization (weeks 13–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 LLM embeddings and features | Item descriptions as embeddings; semantic IDs; cost | Compare LLM-embedding item vectors with CF vectors for cold-start items |
| 11.2 LLM re-ranking and conversational recommenders | Prompting with candidates; position bias; evaluation pitfalls | Re-rank top-50 candidates with an LLM and evaluate with interleaving simulation |
| 11.3 Privacy and consent | Personal data in interaction logs, purpose limitation and consent under the DPDP Act, on-device and federated approaches | Write a privacy review for a personalised feed |
| 11.4 Presenting recommender results | Reporting accuracy, beyond-accuracy and online results together | Present P3 to a mock product review |

**Check your understanding:** (1) Why can an LLM re-ranker look good offline and fail online? (2) What personalization would you switch off without consent? (3) What belongs in a recommender model card?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Objectives and signals | Objective statements |
| 2 | 2 | Lab 1 (cont.): Baselines on MovieLens 32M | — |
| 3 | 3 | Lab 2 · MF from scratch | — |
| 4 | 4 | Lab 3 · Implicit ALS vs BPR | **P1 due** |
| 5 | 5 | Lab 4 · Evaluation harness | — |
| 6 | 5 | Lab 4 (cont.): sampled vs full metrics | — |
| 7 | 6 | Lab 5 · Cold start on MIND | Mid-term (AI off) |
| 8 | 7 | Lab 6 · Two-tower in PyTorch | — |
| 9 | 8 | Lab 7 · Bandit simulation | — |
| 10 | 9 | Lab 8 · Off-policy evaluation | **P2 due** |
| 11 | 9 | Lab 8 (cont.): Interleaving simulation | — |
| 12 | 10 | Lab 9 · Feedback-loop simulation | P3 checkpoint |
| 13 | 11 | Lab 10 · LLM re-ranking | — |
| 14 | 11 | Product review rehearsal | **P3 due** |
| 15 | Review | Product review of P3 | Final exam (AI off) |

## Working with AI in this course

- **Use AI for:** sparse-matrix and PyTorch boilerplate; evaluation-harness code; simulation environments for bandits and feedback loops; LLM embeddings and re-ranking experiments; summarising papers. Claude Code, GitHub Copilot, ChatGPT and Gemini all help.
- **Do without AI (drills):** computing ranking metrics by hand; designing splits; deriving the IPS estimator and its variance; choosing objectives and guardrails; reviewing a recommender A/B test readout. The mid-term and final are AI-off.
- **Verify AI output by:** (1) a global temporal split and full-catalogue metrics, never only sampled metrics; (2) tuned baselines (popularity, item-kNN, EASE) run in the same harness; (3) user-level bootstrap intervals; (4) beyond-accuracy metrics alongside accuracy; (5) for off-policy estimates, a check of support and effective sample size.
- **Where AI still fails here:** published neural recommenders often failed to beat tuned simple baselines (Dacrema et al., 2019), and generated evaluation code commonly defaults to random splits and sampled metrics. In Lab 4 you will log every assistant-generated harness that uses a random split or sampled negatives and measure how much it changes model rankings.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (10) | 25% |
| Projects P1–P3 | 40% |
| Mid-term (AI off) | 10% |
| Final exam (AI off) + product review of P3 | 25% |

**Mastery gate.** You pass when you can: (1) given a new interaction log, build in one day a leakage-free evaluation harness with full-catalogue metrics and three tuned baselines, and report a candidate model's gain with user-level intervals; (2) AI off, design an online experiment for a new recommender, including metrics, guardrails, interference and long-term holdouts; (3) explain and estimate an off-policy value with IPS and doubly robust methods, stating when the estimate cannot be trusted.

## Industry reality

Streaming, e-commerce, food delivery, news and music companies run recommenders as core products. Public accounts include Netflix's recommender system paper (2015), YouTube's two-stage deep recommender (Covington et al., 2016) and two-tower retrieval with sampling-bias correction (Yi et al., 2019), Amazon's item-to-item collaborative filtering (Linden et al., 2003) and ZOZOTOWN's Open Bandit Dataset for off-policy evaluation (Saito et al., 2020). Production teams split the work: data scientists define objectives, evaluation and experiments; ML engineers build retrieval and serving (see MLE403).

**Interview questions from this course**

1. *Design recommendations for a grocery-delivery home screen.* Strong answer: objectives (basket value, retention, freshness), signals (repeat purchases dominate), candidate sources (buy-again, co-purchase, popular in area), ranking with context (time, store inventory), cold start, guardrails, A/B test design with inventory interference.
2. *Your new model improves NDCG@10 offline by 8%. Will it improve the product?* Strong answer: checks split, full vs sampled metrics, baselines, user-level intervals; notes offline–online gaps, exposure bias and novelty; proposes interleaving then an A/B test with retention guardrails.
3. *How do you handle new items with no interactions?* Strong answer: content embeddings, hybrid models, exploration budgets with bandits, popularity priors by category, separate cold-start evaluation.
4. *Explain inverse propensity scoring and when it breaks.* Strong answer: reweights logged rewards by the ratio of new to old policy probabilities; needs logged propensities and support; high variance with small propensities; mentions clipping, self-normalisation and doubly robust estimators.
5. *Sellers complain that only big brands get shown. What do you do?* Strong answer: measures exposure concentration and popularity lift; considers provider-fair re-ranking with an accuracy cost; tests online; discusses platform incentives and long-term marketplace health.

## Resources (free first)

- **Courses and guides:** Google's Recommendation Systems course — https://developers.google.com/machine-learning/recommendation ; Microsoft Recommenders (best-practice notebooks) — https://github.com/recommenders-team/recommenders
- **Libraries:** implicit — https://benfred.github.io/implicit/ ; LensKit — https://lenskit.org/ ; RecBole — https://recbole.io/
- **Data:** MovieLens (including 32M) — https://grouplens.org/datasets/movielens/ ; MIND — https://msnews.github.io/ ; KuaiRec — https://kuairec.com/ ; Yambda — https://huggingface.co/datasets/yandex/yambda ; Amazon Reviews 2023 — https://amazon-reviews-2023.github.io/ ; Open Bandit Dataset — https://research.zozo.com/data.html
- **Papers:** Koren, Bell and Volinsky — https://doi.org/10.1109/MC.2009.263 ; Hu, Koren and Volinsky — https://doi.org/10.1109/ICDM.2008.22 ; Rendle et al., BPR — https://arxiv.org/abs/1205.2618 ; Steck, EASE — https://arxiv.org/abs/1905.03375 ; Kang and McAuley, SASRec — https://arxiv.org/abs/1808.09781 ; Li et al., LinUCB — https://arxiv.org/abs/1003.0146 ; Dacrema et al. — https://arxiv.org/abs/1907.06902 ; Rendle et al., NCF vs MF — https://arxiv.org/abs/2005.09683 ; Krichene and Rendle — https://doi.org/10.1145/3394486.3403226 ; Chaney et al. — https://arxiv.org/abs/1710.11214 ; Saito et al., Open Bandit — https://arxiv.org/abs/2008.07146
- **Paid, optional:** Ricci, Rokach and Shapira (eds.), *Recommender Systems Handbook* (Springer); Falk, *Practical Recommender Systems* (Manning).

## Sources

- Gomez-Uribe and Hunt, "The Netflix Recommender System", *ACM TMIS* (2015) — https://doi.org/10.1145/2843948 (checked 2026-10)
- Ferrari Dacrema, Cremonesi and Jannach, "Are We Really Making Much Progress?" (arXiv 1907.06902; RecSys 2019) — https://arxiv.org/abs/1907.06902 (checked 2026-10)
- Krichene and Rendle, "On Sampled Metrics for Item Recommendation", KDD 2020 — https://doi.org/10.1145/3394486.3403226 (checked 2026-10)
- Chaney, Stewart and Engelhardt, "How Algorithmic Confounding in Recommendation Systems Increases Homogeneity and Decreases Utility" (arXiv 1710.11214; RecSys 2018) — https://arxiv.org/abs/1710.11214 (checked 2026-10)
- GroupLens, MovieLens 32M (released May 2024; 32 million ratings, 200,948 users) — https://grouplens.org/datasets/movielens/ ; Microsoft MIND — https://msnews.github.io/ ; KuaiRec — https://kuairec.com/ ; Yandex Yambda dataset card (4.79 billion interactions, organic vs recommendation flags) — https://huggingface.co/datasets/yandex/yambda (checked 2026-10)
- Linden, Smith and York (2003) — https://doi.org/10.1109/MIC.2003.1167344 ; Covington, Adams and Sargin (2016) — https://doi.org/10.1145/2959100.2959190 ; Yi et al. (2019) — https://doi.org/10.1145/3298689.3346996 ; Steck, calibrated recommendations (2018) — https://doi.org/10.1145/3240323.3240372 ; Chapelle et al. (2012) — https://doi.org/10.1145/2094072.2094078 (checked 2026-10)

_Last reviewed: 2026-10_
