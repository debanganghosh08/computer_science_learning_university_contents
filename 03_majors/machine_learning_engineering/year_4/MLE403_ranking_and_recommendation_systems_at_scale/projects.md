# MLE403 · Labs and projects

Use public data (MovieLens, Amazon Reviews 2023, KuaiRand, MIND, OTTO, H&M, Criteo samples) with PyTorch, TorchRec, LightGBM, `implicit` and FAISS. Every result is reported on a time-based split, against tuned baselines (popularity, item-item, implicit ALS), with bootstrap confidence intervals. Simulated online experiments use synthetic users whose preferences you define and document.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Funnel, logs and bias | Size retrieval, ranking and re-ranking for 10 M items and 150 ms; write a value function for a social-commerce feed; design an impression log; estimate position bias from a simulated randomisation slot; compare 3 negative-sampling schemes | Calculation sheet; value function; log schema; bias curve; negatives comparison | 7 h (2 weeks) |
| 2 · Baselines and time-split evaluation | Popularity, item-item, ALS and BM25; ask an assistant for a "state-of-the-art" recommender and test it against them | Metric table with CIs; a note on the AI model's result | 4 h |
| 3 · Two-tower retrieval and ANN serving | Two-tower model with in-batch negatives, with and without logQ correction; HNSW and IVF-PQ indexes in FAISS; merge embedding, co-visitation and popularity retrievers | Recall@k overall and for tail items; recall@100 vs p99 latency curves; added recall per retriever | 9 h (2 weeks) |
| 4 · LambdaMART, DCN-V2, MMoE | GBDT ranker with LambdaMART; DCN-V2; a 3-task MMoE; calibration | NDCG@10 per model with CIs; calibration plots | 6 h |
| 5 · Sequential models and semantic IDs | SASRec on OTTO or KuaiRand sessions; semantic IDs by residual quantisation of item embeddings | Next-item recall vs non-sequential baseline; ID collision statistics | 5 h |
| 6 · Re-ranking and exploration | MMR diversity, a quality penalty, exposure fairness for sellers, epsilon-greedy exploration | Relevance vs diversity vs exposure-Gini frontier; coverage over 20 simulated rounds | 4 h |
| 7 · Real-time features and cold start | In-session features; a cold-start path for new items and users | NDCG gain from session features; cold-start metrics on held-out new items | 4 h |
| 8 · Serving under a latency budget | 3-stage service (retrieve, rank, re-rank) with caches and per-stage timeouts; ranker failure test | p50/p99 per stage under load; fallback demonstration | 4 h |
| 9 · Interleaving, interference and IPS | Team-draft interleaving vs A/B on synthetic users; a marketplace simulation with interference; IPS off-policy estimate | Users needed per method; biased vs cluster-randomised estimates; IPS estimate with variance | 4 h |
| 10 · Feedback loops and a non-profiling feed | 20 retraining rounds with and without exploration; a feed that uses no personal profiling | Coverage and concentration plots; engagement proxy of the non-profiling feed vs personalised | 3 h |

## Projects

### P1 · Honest baselines for a real catalogue (L1, ~6 hours)

**Real-world inspiration.** Ferrari Dacrema et al. (2019) could reproduce only 7 of 18 recent neural recommendation papers, and 6 of those were often beaten by simple tuned baselines. Every serious recommendation team starts by establishing baselines it can trust.

**What to build.** On Amazon Reviews 2023 (one category) or MovieLens 25M, build a baseline suite: popularity (global and recency-weighted), item-item, implicit ALS and, for search, BM25, all evaluated on a time-based split with a documented protocol.

**Acceptance criteria**
- A written evaluation protocol: split dates, candidate sets, metrics (recall@k, NDCG@k, coverage), and how ties and cold items are handled.
- Every baseline is tuned with a fixed search budget on a validation period before the test period.
- Metrics are reported with bootstrap CIs; the best baseline is identified with a significance argument.
- A leakage test shows no training interaction occurs after the split date.
- One command reproduces all numbers.

**Stretch goals.** Report metrics separately for head and tail items; add a co-visitation baseline.

**What it proves to an employer.** You know how to measure recommendation quality honestly, which is the foundation every later model depends on.

### P2 · Two-stage recommender with a learned ranker (L2, ~15 hours)

**Real-world inspiration.** YouTube's two-stage design (Covington et al., 2016) and its sampling-bias-corrected two-tower retrieval (Yi et al., 2019); Meesho's feed ranker predicting both click and purchase probabilities (2023).

**What to build.** On your P1 data, a two-stage system: two-tower retrieval with logQ correction served from a FAISS index, merged with your best baseline retriever, followed by a ranker (LambdaMART or a multi-task neural ranker) over at most 500 candidates with features from P1 and session context.

**Acceptance criteria**
- Retrieval recall@500 beats the best single baseline retriever, with CIs.
- End-to-end NDCG@10 beats the P1 best baseline with non-overlapping 95% CIs.
- Tail-item recall is reported with and without logQ correction.
- The ranker's probabilities are calibrated (reliability plot), and the value function combining tasks is documented.
- A serving path returns top-10 for a user within p99 150 ms on a laptop, with per-stage timing.
- An ablation table shows the contribution of each retriever and feature group.

**Stretch goals.** Hard-negative mining; a DCN-V2 or DLRM ranker in TorchRec; position-bias correction in ranker training.

**What it proves to an employer.** You can build the core of a production recommender and show where every gain comes from.

### P3 · A production-style recommender with experiments and safeguards (L3, portfolio-grade, ~30 hours)

**Real-world inspiration.** Instagram Explore's multi-stage system and value model (Meta, 2023); Flipkart's unified ads-and-organic ranking (+1.36% organic orders, +3.4% ad revenue, 2025); Netflix's interleaving (2017); LinkedIn's cluster-randomised interference test (2019); the EU Digital Services Act's requirement that very large platforms offer a non-profiling option (Article 38).

**What to build.** Extend P2 into a feed or shopping-recommendation service with: real-time session features, a cold-start path, re-ranking for diversity, quality and seller exposure, an exploration slot, a non-profiling alternative feed, monitoring, and a simulation environment of synthetic users and sellers in which you run A/B, interleaving and cluster-randomised experiments.

**Acceptance criteria**
- A design document (8–10 pages) covering funnel sizing, value function, data and labels, features with freshness, serving budget, experiments, monitoring and responsible-recommendation choices.
- Offline: the full system beats P2 on NDCG@10 or on the value function without reducing catalogue coverage by more than 10% (or justifies the trade-off).
- Simulation: the report shows how many synthetic users A/B and interleaving each need to detect a planted improvement, and how a user-level A/B test is biased under seller-side interference while a cluster-randomised design is not.
- Feedback-loop analysis over 20 simulated retraining rounds, with and without exploration and diversity re-ranking.
- The non-profiling feed is implemented and its quality compared with the personalised feed.
- The service meets p99 under 200 ms end to end on stated hardware and degrades gracefully when the ranker is down.
- A 20-minute design review answering questions from peers acting as product, legal and SRE.

**Stretch goals.** A sequential (SASRec-style) or semantic-ID retriever as an extra candidate source; an LLM relevance judge validated against human labels and used to build training data; an off-policy (IPS) estimate of the new policy from logged data.

**What it proves to an employer.** You can own a recommender end to end, from modelling to experiments to responsible design, which is the profile of senior ranking and recommendation engineers.

## Feeds into

- [MLE501 Frontier Seminar](../../year_5/MLE501_frontier_seminar_ml_research_engineering/README.md): reproducing a recommendation paper against tuned baselines is a strong seminar project.
- [THS501 Thesis or Capstone I](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md): feedback loops, interference and generative recommenders are open research topics.
- [IND401 Industry Co-op Studio](../../../../05_shared_years_3_to_5/IND401_industry_co_op_studio/README.md): the design document and experiment plan carry into a real team.
- [MLE404 Efficient Inference](../MLE404_efficient_inference_quantization_distillation/README.md): ranker latency and embedding memory are prime targets for compression.
