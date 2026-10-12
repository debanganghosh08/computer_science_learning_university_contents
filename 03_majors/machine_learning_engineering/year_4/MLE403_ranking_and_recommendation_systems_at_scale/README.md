# MLE403 · Ranking and Recommendation Systems at Scale

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 4 · 8 | 4 (≈ 120 hours) | L3 → L4 | [MLE303](../../year_3/MLE303_training_pipelines_feature_stores_and_experiment/README.md) (and [MLE302](../../year_3/MLE302_machine_learning_system_design/README.md) in practice) | [MLE501](../../year_5/MLE501_frontier_seminar_ml_research_engineering/README.md), [IND401](../../../../05_shared_years_3_to_5/IND401_industry_co_op_studio/README.md), [THS501](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md) |

## Why this course matters now

Feeds, search results, product listings, ads and notifications are ranked by models; Airbnb reported that search ranking and similar-listing recommendations "drive 99% of conversions" (2018). The field is changing fast. Meta's generative recommenders (HSTU) reached 1.5 trillion parameters and reported a 12.4% gain in online A/B tests (2024); Netflix described a foundation model trained on user-action sequences with GPT-style next-token prediction (2025); Flipkart replaced fixed ad slots with one model ranking ads and organic results together, reporting +1.36% organic orders and +3.4% ad revenue (2025); and Flipkart also fine-tuned an LLM to label search relevance more accurately than human annotators on its benchmark (2025). Assistants write a two-tower model in minutes. Choosing the objective, avoiding feedback loops and position bias, keeping features fresh, measuring in marketplaces where users interfere with each other, and serving 1,000 candidates in 100 ms are the engineering problems this course is about. A cautionary result keeps everyone honest: of 18 recent neural recommendation papers, only 7 could be reproduced with reasonable effort, and 6 of those were often beaten by simple tuned baselines (Ferrari Dacrema et al., 2019).

## Learning outcomes

By the end you can:

1. **Design** a multi-stage recommender (candidate generation, ranking, re-ranking) with a latency budget per stage and a value function that encodes business objectives.
2. **Build** training data from impression logs, handling position bias, negative sampling, delayed conversions and policy bias.
3. **Implement and tune** strong baselines (popularity, item-item, implicit ALS, BM25) and **evaluate** with time-based splits and ranking metrics.
4. **Train** two-tower retrieval models with in-batch negatives and sampling-bias correction, and **serve** them with approximate nearest-neighbour indexes.
5. **Train** ranking models (LambdaMART, Wide & Deep, DCN-V2, DLRM, multi-task MMoE) and **calibrate** them where scores feed auctions or value models.
6. **Apply** sequential and generative recommenders (SASRec-style transformers, semantic IDs, generative retrieval) and **judge** when they beat simpler models.
7. **Design** re-ranking for diversity, freshness, quality, fairness and ads/organic blending.
8. **Engineer** real-time features and cold-start paths, and **reason** about embedding freshness at scale.
9. **Run** online experiments that account for interleaving, interference and long-term effects.
10. **Assess** feedback loops, popularity bias and regulatory duties such as the EU Digital Services Act's non-profiling option.

## Chapters and lessons

### Chapter 1 · The recommendation problem (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Tasks and surfaces | Feed, search, related items, notifications, ads; retrieval vs ranking; Eugene Yan's offline/online × retrieval/ranking framework | Map 5 surfaces of a shopping app to tasks |
| 1.2 The funnel | Candidate generation → ranking (YouTube, Covington et al., 2016) → re-ranking; Instagram Explore's stages (2023) | Size each stage for 10 M items and a 150 ms budget |
| 1.3 Objectives | Clicks vs purchases vs long-term value; value models (Explore's weighted sum of predicted actions) | Write a value function for a social-commerce feed |
| 1.4 Strong baselines first | Simple methods often win (Ferrari Dacrema et al., 2019) | List the baselines any new model must beat |

**Check your understanding:** Why does optimising clicks alone degrade a feed? Why separate retrieval from ranking? Why must every new model be compared against a tuned simple baseline?

### Chapter 2 · Logs, labels and bias (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Impression logging | Impressions, clicks, dwell, purchases; logging the serving context and model version | Design an impression log schema |
| 2.2 Position and selection bias | Position bias, examination models, inverse propensity weighting, randomised slots | Estimate position bias from a small randomisation experiment |
| 2.3 Negatives | Unclicked impressions vs random negatives vs hard negatives | Compare 3 negative-sampling schemes |
| 2.4 Delayed and multi-step labels | Conversions after days; attribution windows | Build labels with a 7-day conversion window |

**Check your understanding:** Why are unclicked items at position 20 weak negatives? What does logging the propensity enable later? Why does a conversion window delay retraining?

### Chapter 3 · Baselines and offline evaluation (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Neighbourhood and popularity | Item-item similarity, recency-weighted popularity | Item-item recommender on MovieLens |
| 3.2 Implicit matrix factorisation | ALS with confidence weights (`implicit` library) | Tune ALS; beat popularity on recall@50 |
| 3.3 Lexical search baselines | BM25 for product search | BM25 over Amazon Reviews 2023 product titles |
| 3.4 Offline metrics | Recall@k, NDCG@k, MRR, coverage, novelty; time-based splits; leakage in recommender evaluation | Evaluate 3 baselines with CIs on a time split |

**Check your understanding:** Why does a random split overstate recommender quality? What does coverage capture that NDCG does not? Why can a model with higher NDCG offline lose online?

### Chapter 4 · Candidate generation (weeks 4–5)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Two-tower models | User and item towers, dot-product scoring, in-batch negatives | Train a two-tower model on MovieLens or Amazon data |
| 4.2 Sampling-bias correction | Popular items over-sampled as in-batch negatives; logQ correction with streaming frequency estimates (Yi et al., 2019) | Show recall gains for tail items with the correction |
| 4.3 Approximate nearest neighbours | HNSW graphs, IVF and product quantisation (FAISS, ScaNN); recall vs latency | Build two indexes; plot recall@100 vs p99 latency |
| 4.4 Multiple retrievers | Embedding, co-visitation, graph-based (PinSage on 3 B nodes and 18 B edges), rules; merging and quotas | Merge 3 retrievers; measure added recall |
| 4.5 Embedding freshness | Re-indexing cadence, new items, model–index version skew | Design a refresh plan for 1 M new items a day |

**Check your understanding:** Why can't a two-tower model use user–item cross features? Why does in-batch sampling penalise popular items? What breaks when the index and the user tower come from different model versions?

### Chapter 5 · Ranking models (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Learning to rank | Pointwise, pairwise, listwise losses; LambdaMART (Burges, 2010) with LightGBM | LambdaMART ranker over retrieved candidates |
| 5.2 Feature crosses | Wide & Deep (+3.9% app acquisitions on Google Play, 2016); DCN-V2 cross layers; LinkedIn's LiRank (2024) | Train DCN-V2 vs GBDT on the same features |
| 5.3 Large sparse models | DLRM: embedding tables plus MLPs; TorchRec | Train a DLRM-style ranker on Criteo samples |
| 5.4 Multi-task ranking | Shared-bottom vs MMoE (Ma et al., 2018); predicting click, like, purchase, hide | Train MMoE with 3 tasks; compare with separate models |
| 5.5 Calibration | Calibrated probabilities for value models and ad auctions | Calibrate and measure the effect on the value function |

**Check your understanding:** Why does a GBDT ranker remain competitive (ShareChat's 2023 comparison found GBDTs reaching similar accuracy at lower cost in their setting)? When does multi-task learning cause negative transfer? Why must predicted click probabilities be calibrated before entering an auction?

### Chapter 6 · Sequential and generative recommenders (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Session models | GRU4Rec (2015), SASRec (2018), BERT4Rec (2019) | SASRec on a session dataset (OTTO or KuaiRand) |
| 6.2 Long-term user representations | PinnerFormer's dense all-action loss (Pinterest, 2022) | Train user embeddings predicting next-week actions |
| 6.3 Generative recommenders | HSTU and scaling laws for recommendation (Meta, 2024); Netflix's foundation model (2025) | Read and present one paper's design and evidence |
| 6.4 Semantic IDs | Generative retrieval with semantic item IDs (TIGER, 2023) | Build semantic IDs by residual quantisation of item embeddings |
| 6.5 LLMs in recommendation | LLMs as labellers (Flipkart relevance, 2025), as feature extractors, as rankers; cost and latency | Compare an LLM relevance judge with human labels on 200 pairs |

**Check your understanding:** What do sequence models capture that a two-tower model with averaged history does not? What evidence would convince you a generative recommender is worth its serving cost? Why use an LLM to label rather than to rank in production?

### Chapter 7 · Re-ranking and multiple objectives (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Diversity and novelty | Maximal marginal relevance (Carbonell and Goldstein, 1998), determinantal point processes, category quotas | Add MMR; plot relevance vs diversity |
| 7.2 Quality and trust | Down-ranking low-quality sellers (Meesho's quality re-ranking, 2025) | Add a quality penalty; measure the trade-off offline |
| 7.3 Ads and organic | Unified ranking with one value scale (Flipkart, 2025); auction interactions | Design a unified score for ads and organic items |
| 7.4 Fairness to providers | Exposure fairness for sellers and creators; popularity bias | Measure exposure Gini before and after a fairness constraint |
| 7.5 Exploration | Epsilon-greedy and Thompson sampling slots; cost of exploration | Simulate exploration's long-run effect on catalogue coverage |

**Check your understanding:** Why is diversity a ranking-level, not item-level, property? What can go wrong when ads and organic scores are on different scales? Why is some exploration necessary for a healthy catalogue?

### Chapter 8 · Features, real time and cold start (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Feature families | User, item, context and cross features; counting features over windows | Build 20 features with point-in-time correctness (from MLE303) |
| 8.2 Real-time personalisation | Session features updated in seconds; Airbnb's real-time embedding personalisation (2018) | Add in-session features; measure NDCG gain |
| 8.3 Real-time training | ByteDance's Monolith: collisionless embedding tables, expirable embeddings, online training (2022) | Explain which parts of your system need online updates |
| 8.4 Cold start | Content features, popularity priors, explore slots; Meesho's Cold-Warm Net (2025) | A cold-start path for new users and new items |

**Check your understanding:** Why do hashed embedding tables suffer collisions, and why does that matter? Which features must be real-time for a short-video feed? How do you evaluate a cold-start model offline?

### Chapter 9 · Serving at scale (week 10)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Latency budgets | Per-stage budgets, fan-out, caching, precomputed candidates | Build a 3-stage service; meet p99 < 150 ms |
| 9.2 Embedding infrastructure | Sharded embedding tables, embedding caches, GPU vs CPU ranking | Estimate memory and QPS for 100 M users |
| 9.3 An open-sourced system | X's recommendation algorithm repository: candidate sources, light and heavy rankers, filters | Trace one tweet from candidate source to timeline |
| 9.4 Degradation and safety | Fallback lists, timeouts per stage, content filters | Kill the ranker; serve a sensible fallback |

**Check your understanding:** Where does most latency go in a 3-stage recommender? Why cache candidates but not final rankings? What should the system show if the ranker times out?

### Chapter 10 · Experiments for recommenders (week 11)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 A/B testing pitfalls | Novelty, carryover, metric choice, guardrails | Design an A/B test for a new ranker |
| 10.2 Interleaving | Team-draft interleaving; Netflix's >100× sensitivity gain over its A/B metric | Simulate interleaving vs A/B on synthetic users |
| 10.3 Interference | Marketplaces and networks; LinkedIn's cluster-randomised experiment over 10,000 clusters; DoorDash switchbacks | Choose a randomisation unit for a seller-side change |
| 10.4 Long-term effects | Holdbacks, surrogate metrics, user-learning effects | Plan a 6-month holdback and its readouts |
| 10.5 Off-policy evaluation | Inverse propensity scoring and its variance | Estimate a new policy's value from logs with IPS |

**Check your understanding:** Why can a ranker win an A/B test by stealing exposure from control in a marketplace? When is interleaving the wrong test? Why do off-policy estimates need logged propensities?

### Chapter 11 · Responsible recommendation (week 12)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Feedback loops and popularity bias | How rankers reinforce popular items; measuring concentration | Simulate 20 retraining rounds; measure coverage |
| 11.2 User control and transparency | Explanations, "not interested", controls that change the model | Add a user control and measure its effect on ranking |
| 11.3 Regulation | EU Digital Services Act: very large platforms must offer at least one recommender option not based on profiling (Article 38) | Design a non-profiling feed that is still useful |
| 11.4 Harm and integrity | Down-ranking borderline content, protecting minors, integrity signals | Write integrity guardrails for a teen-heavy surface |

**Check your understanding:** Why does a non-profiling feed still need a ranking model? How would you show that a ranker is reducing catalogue diversity? Who should decide integrity trade-offs?

### Chapter 12 · Integration and case synthesis (weeks 13–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 12.1 Case comparison | YouTube, Instagram Explore, Pinterest, X, Flipkart, Meesho: what is common, what differs | A comparison table with sources |
| 12.2 Building P3 | End-to-end recommender with experiments | P3 build |
| 12.3 Review | Design review with peers acting as product, legal and SRE | P3 review |
| 12.4 Operating a recommender | On-call dashboards, ranker rollback, failed index rebuilds, stale embeddings | Write the runbook for P3 |

**Check your understanding:** Which design choices recur across every published system? Which choices depend on the product? What would you build first with a team of three?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Funnel sizing and value functions | — |
| 2 | 2 | Lab 1 (continued): logs, position bias and negatives | — |
| 3 | 3 | Lab 2 · Baselines and time-split evaluation | **P1 due** |
| 4 | 4 | Lab 3 · Two-tower with bias correction | — |
| 5 | 4 | Lab 3 (continued): ANN indexes and multiple retrievers | — |
| 6 | 5 | Lab 4 · LambdaMART, DCN-V2, MMoE | Mid-term (AI off) |
| 7 | 6 | Lab 5 · Sequential models and semantic IDs | — |
| 8 | 7 | Lab 6 · Re-ranking and exploration | **P2 due** |
| 9 | 8 | Lab 7 · Real-time features and cold start | — |
| 10 | 9 | Lab 8 · Serving under a latency budget | — |
| 11 | 10 | Lab 9 · Interleaving, interference and IPS | — |
| 12 | 11 | Lab 10 · Feedback loops and a non-profiling feed | — |
| 13 | 12 | P3 build | — |
| 14 | 12 | P3 review | **P3 due** |
| 15 | Review | P3 presentation | Final exam (AI off) |

## Working with AI in this course

- **Use AI for:** model and data-loader boilerplate; FAISS and TorchRec configuration; summarising papers and engineering posts (then checking the claims against the source); generating synthetic users for simulations; LLM relevance judgements, after measuring agreement with human labels.
- **Do without AI (drills):** size a funnel and a latency budget; write a value function; choose negatives; compute NDCG and recall by hand; choose a randomisation unit; explain logQ correction. The mid-term and final are AI-off.
- **Verify AI output by:** comparing every new model against tuned baselines on a time split with CIs; checking for leakage (future interactions in training features); testing the same model–index version at serving; validating LLM labels against a human gold set; reproducing any paper number you rely on.
- **Where AI still fails here:** assistants default to random splits, report metrics without baselines, ignore position bias, use random negatives only, and recommend architectures from papers that were never shown to beat tuned baselines. In Lab 2 you ask an assistant for a "state-of-the-art" recommender and test it against item-item and ALS.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (10) | 25% |
| Projects P1–P3 | 45% |
| Mid-term (AI off) | 10% |
| Final exam (AI off) | 20% |

**Mastery gate.** You pass when you can: (1) without AI, in 45 minutes, design a recommender for an unseen surface with a sized funnel, value function, training data plan, serving budget and experiment plan; (2) build, on a public dataset, a two-stage recommender that beats tuned item-item and ALS baselines on a time split with non-overlapping CIs; (3) explain one of HSTU, Monolith or the two-tower sampling-bias correction to a peer and answer questions on its evidence.

## Industry reality

Public write-ups describe how ranking and recommendation are built at YouTube (2016, 2019), Meta (DLRM 2019, Instagram Explore 2023, HSTU 2024), Pinterest (PinSage, PinnerFormer), ByteDance (Monolith), LinkedIn (LiRank), Netflix (2025), Airbnb (2018), and in India at Flipkart (2025), Meesho (2023, 2025) and ShareChat (2023).

**Interview questions from this course**

1. *Design the home feed for a social-commerce app.* Strong answer: funnel with multiple retrievers; multi-task ranker with a value function (click, purchase, quality); re-ranking for diversity and seller fairness; real-time session features; cold start; latency budget; interleaving and interference-aware experiments.
2. *How do you train a two-tower retrieval model?* Strong answer: positives from engagement; in-batch and hard negatives; logQ correction; temperature; evaluation by recall@k on a time split; index refresh and versioning.
3. *Your new ranker wins offline NDCG but loses the A/B test. Why?* Strong answer: position bias in training data; offline metric not matching the value function; skew between offline and online features; latency increase; novelty; interference; calibration change in downstream auctions.
4. *How do you handle cold-start items?* Strong answer: content embeddings, popularity priors, exploration slots with a budget, fast feature updates, a separate cold-start model or gating, and how to evaluate it.
5. *How would you reduce popularity bias without hurting engagement?* Strong answer: measure exposure concentration; logQ correction in retrieval; re-ranking with diversity or exposure constraints; exploration; long-term holdbacks to measure the effect on retention.

## Resources (free first)

- **Courses and guides:** Google, Recommendation Systems course — https://developers.google.com/machine-learning/recommendation ; Eugene Yan, "System Design for Recommendations and Search" — https://eugeneyan.com/writing/system-design-for-discovery/ ; Microsoft Recommenders (code examples) — https://github.com/recommenders-team/recommenders ; RecBole — https://recbole.io/
- **Libraries:** FAISS — https://github.com/facebookresearch/faiss ; ScaNN — https://github.com/google-research/google-research/tree/master/scann ; `implicit` — https://github.com/benfred/implicit ; TorchRec — https://github.com/pytorch/torchrec ; LightGBM ranking objectives — https://lightgbm.readthedocs.io/en/stable/Parameters.html
- **Datasets:** MovieLens — https://grouplens.org/datasets/movielens/ ; Amazon Reviews 2023 — https://amazon-reviews-2023.github.io/ ; KuaiRand — https://kuairand.com/ ; MIND news — https://msnews.github.io/ ; OTTO session recommendations — https://www.kaggle.com/competitions/otto-recommender-system ; H&M fashion recommendations — https://www.kaggle.com/competitions/h-and-m-personalized-fashion-recommendations ; RecSys Challenge — https://www.recsyschallenge.com/
- **Open system:** X's recommendation algorithm — https://github.com/twitter/the-algorithm

## Sources

- Covington et al., YouTube DNN recommendations (RecSys 2016) — https://research.google/pubs/deep-neural-networks-for-youtube-recommendations/ ; Yi et al., sampling-bias-corrected two-tower (RecSys 2019) — https://research.google/pubs/sampling-bias-corrected-neural-modeling-for-large-corpus-item-recommendations/ ; Cheng et al., Wide & Deep — https://arxiv.org/abs/1606.07792 ; Wang et al., DCN-V2 — https://arxiv.org/abs/2008.13535 ; Ma et al., MMoE (KDD 2018) — https://research.google/pubs/modeling-task-relationships-in-multi-task-learning-with-multi-gate-mixture-of-experts/ (checked 2026-10)
- Naumov et al., DLRM — https://arxiv.org/abs/1906.00091 ; Zhai et al., "Actions Speak Louder than Words" (HSTU, ICML 2024) — https://arxiv.org/abs/2402.17152 ; Meta, "Scaling the Instagram Explore recommendations system" (9 Aug 2023) — https://engineering.fb.com/2023/08/09/ml-applications/scaling-instagram-explore-recommendations-system/ ; Liu et al., Monolith — https://arxiv.org/abs/2209.07663 ; Ying et al., PinSage — https://arxiv.org/abs/1806.01973 ; Pancha et al., PinnerFormer — https://arxiv.org/abs/2205.04507 ; Borisyuk et al., LiRank — https://arxiv.org/abs/2402.06859 (checked 2026-10)
- Netflix, "Foundation Model for Personalized Recommendation" (21 Mar 2025) — https://medium.com/netflix-techblog/foundation-model-for-personalized-recommendation-1a0bd8e02d39 ; Netflix, interleaving (2017) — https://medium.com/netflix-techblog/interleaving-in-online-experiments-at-netflix-a04ee392ec55 ; Grbovic and Cheng, Airbnb embeddings (KDD 2018) — https://www.kdd.org/kdd2018/accepted-papers/view/real-time-personalization-using-embeddings-for-search-ranking-at-airbnb (checked 2026-10)
- Flipkart, "The Science of Unified Ranking" (4 Nov 2025) — https://blog.flipkart.tech/the-science-of-unified-ranking-integrating-ads-and-organic-recommendations-8cc24113ef21 ; Flipkart, "LLMs for Relevance" (2025) — https://blog.flipkart.tech/llms-for-relevance-automating-high-quality-product-relevance-labeling-in-flipkart-search-ddd5ca50b584 ; Meesho on AWS (2023) — https://aws.amazon.com/blogs/machine-learning/how-meesho-built-a-generalized-feed-ranker-using-amazon-sagemaker-inference/ ; Meesho, quality re-ranking (2025) — https://www.meesho.io/blog/quality-focused-feed-re-ranking ; Meesho, cold start (2025) — https://www.meesho.io/blog/personalization-from-day-one-solving-the-cold-start-problem-at-meesho ; ShareChat, GBDTs vs neural rankers (FIRE 2023) — https://arxiv.org/abs/2312.01760 (checked 2026-10)
- LinkedIn, "Detecting interference: An A/B test of A/B tests" (2019) — https://www.linkedin.com/blog/engineering/ab-testing-experimentation/detecting-interference-an-a-b-test-of-a-b-tests ; DoorDash, switchback tests (2018) — https://careersatdoordash.com/blog/switchback-tests-and-randomized-experimentation-under-network-effects-at-doordash/ (checked 2026-10)
- Ferrari Dacrema, Cremonesi and Jannach (RecSys 2019) — https://arxiv.org/abs/1907.06902 ; Rajput et al., TIGER (semantic IDs) — https://arxiv.org/abs/2305.05065 ; Kang and McAuley, SASRec — https://arxiv.org/abs/1808.09781 ; Hidasi et al., GRU4Rec — https://arxiv.org/abs/1511.06939 ; Sun et al., BERT4Rec — https://arxiv.org/abs/1904.06690 ; Malkov and Yashunin, HNSW — https://arxiv.org/abs/1603.09320 ; Burges, LambdaMART overview — https://www.microsoft.com/en-us/research/publication/from-ranknet-to-lambdarank-to-lambdamart-an-overview/ ; Carbonell and Goldstein, MMR — https://www.cs.cmu.edu/~jgc/publication/The_Use_MMR_Diversity_Based_LTMIR_1998.pdf (checked 2026-10)
- EU Digital Services Act, Regulation (EU) 2022/2065, Article 38 — https://eur-lex.europa.eu/eli/reg/2022/2065/oj/eng (reproduced at https://www.springlex.eu/en/packages/dsa/dsa-regulation/article-38/) (checked 2026-10)

_Last reviewed: 2026-10_
