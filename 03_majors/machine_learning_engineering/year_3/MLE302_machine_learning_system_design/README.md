# MLE302 · Machine Learning System Design

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 3 · 5 | 4 (≈ 120 hours) | L2 → L4 | [CS214](../../../../02_year_2_core_computer_science/semester_4/CS214_machine_learning_foundations/README.md), [CS205](../../../../02_year_2_core_computer_science/semester_3/CS205_software_engineering_i_design_testing/README.md) | [MLE402](../../year_4/MLE402_distributed_training_and_large_scale_ml/README.md), [MLE401](../../year_4/MLE401_mlops_deployment_monitoring_and_retraining/README.md), [MLE403](../../year_4/MLE403_ranking_and_recommendation_systems_at_scale/README.md), [CAR401](../../../../05_shared_years_3_to_5/CAR401_career_lab_ii_interviews_system_design_and_ai/README.md) |

## Why this course matters now

A model is a small part of an ML system. Uber's Michelangelo platform ran more than 5,000 production models and served up to 10 million real-time predictions per second at peak by 2024; Stripe Radar scores each payment on more than 1,000 characteristics in under 100 ms; Swiggy must show delivery-time estimates for 300–500 restaurants on a listing page that loads within half a second. Getting there means choosing what to predict, which data exists at serving time, how fresh features must be, where latency goes, and how the system's own outputs change its future training data. An assistant can draft a plausible design document in seconds, but it cannot know your label delay, your p99 budget or your feedback loops, and plausible designs fail on exactly those details. ML system design is also a standard interview round: Chip Huyen's *Machine Learning Interviews* book says of ML systems design questions, "Almost all companies I've talked to ask at least a question of this type."

## Learning outcomes

By the end you can:

1. **Frame** a business problem as an ML problem (or decide it should not be one), with a prediction target, a decision, and offline, online and guardrail metrics.
2. **Estimate** load, storage, feature-fetch cost and latency with back-of-envelope arithmetic, and **allocate** a latency budget across stages.
3. **Design** data and label pipelines that handle delayed, noisy and biased labels and logged-policy bias.
4. **Design** batch, streaming and on-demand features with point-in-time correctness, and **prevent** training–serving skew.
5. **Choose** model families, losses and output types (point, quantile, distribution, multi-task) to fit the decision and the latency budget.
6. **Design** serving architectures (batch precompute, online, streaming, multi-stage funnels) with caching and fallbacks.
7. **Plan** offline evaluation, shadow deployment, A/B tests, interleaving and switchback experiments, and **explain** interference.
8. **Identify** feedback loops and hidden technical debt, and **design** monitoring and retraining.
9. **Analyse** published systems from India and abroad (Swiggy, Zomato, Flipkart, Meesho, Uber, DoorDash, Stripe, Airbnb, Netflix, Meta) and **critique** their trade-offs.
10. **Deliver** a 45-minute ML system design interview to a hiring-bar standard.

## Chapters and lessons

### Chapter 1 · From business problem to ML problem (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Do you need ML? | Rules first, heuristics as baselines (Google's Rules of ML, rule #1); cost of an ML system | Argue for and against ML for 4 product requests |
| 1.2 Prediction vs decision | What the model predicts vs what the product does with it; proxy targets | Separate prediction and decision for surge pricing, fraud blocking and feed ranking |
| 1.3 Framing types | Classification, regression, ranking, retrieval, forecasting; one framing can hide a better one | Reframe "predict delivery time" three ways |
| 1.4 Metrics stack | Offline metric, online metric, guardrails, north-star metric | Metric tree for an ETA feature |

**Check your understanding:** Why might a heuristic beat a model at launch? Why is "maximise clicks" a dangerous objective? Which metric would make you roll back a model even if the main metric improved?

### Chapter 2 · Requirements and estimation (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Non-functional requirements | p50/p99 latency, QPS, freshness, availability, cost per 1,000 predictions | Write requirements for a checkout fraud check |
| 2.2 Back-of-envelope estimates | Requests per second from daily users; feature bytes per request; embedding table sizes | Estimate memory for 100 M user embeddings of dimension 64 in fp32 and fp16 |
| 2.3 Latency budgets | Network, feature fetch, model, post-processing; tail latency and fan-out | Split a 100 ms budget across 5 stages |
| 2.4 The design document | Context, goals, non-goals, design, alternatives, risks, rollout | Turn a rough idea into a 2-page design doc |

**Check your understanding:** Why does p99 latency, not the average, set the budget for a page that calls 10 services? Why do non-goals belong in a design doc? What changes when QPS grows 10×?

### Chapter 3 · Data and labels (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Sources and logging | Event logging, schemas, what to log at serving time (Rules of ML #29) | Design the prediction log for an ETA model |
| 3.2 Label definition and delay | Chargebacks arriving weeks later; "delivered" timestamps that riders press early | Define the fraud label and its maturity window |
| 3.3 Implicit feedback and bias | Clicks, dwell, purchases; position bias; selection bias from the current policy | Show how logged data from a ranker under-represents low-ranked items |
| 3.4 Sampling and imbalance | Negative sampling, down-sampling with re-weighting, stratification | Down-sample negatives and correct the predicted probabilities |
| 3.5 Labels at scale | Human labelling, LLM-assisted labelling with human audit (Flipkart's relevance-labelling model, 2025) | Design a labelling pipeline with a quality-control loop |

**Check your understanding:** Why can a model trained only on approved loans not learn about rejected applicants? How does label delay change your retraining schedule? Why must down-sampled probabilities be corrected before use in pricing?

### Chapter 4 · Features and training–serving skew (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Feature types | Batch, streaming (near-real-time) and on-demand features; embeddings as features | Classify 15 features of a food-delivery ETA model by type and freshness |
| 4.2 Point-in-time correctness | Joining features as of the prediction timestamp; leakage from future data | Write a point-in-time join in SQL and test it |
| 4.3 Feature stores | Offline and online stores; Michelangelo's shared feature store; Instacart's Kafka → Flink → feature-store pipeline | Sketch the feature store for your ETA design |
| 4.4 Training–serving skew | Different code paths, stale joins, defaults; Rules of ML #31, #32 and #37 | Find 3 sources of skew in a provided design |

**Check your understanding:** Why does a "restaurant load in the last 10 minutes" feature need a streaming pipeline? What is the simplest way to avoid skew from duplicated feature code? Why can a feature that is perfectly correct offline be wrong online?

### Chapter 5 · Models, losses and outputs (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Model choice under constraints | Linear, GBDT, deep models; latency, update frequency, explainability | Pick a model for 3 scenarios with different budgets |
| 5.2 Residual and hybrid models | Uber's DeepETA predicts a correction on top of a routing engine's ETA | Design a residual model for a physics or rules baseline |
| 5.3 Loss choice | Asymmetric Huber (DeepETA), quantile losses (Zomato preparation time), cost-weighted losses | Choose a loss when late is worse than early |
| 5.4 Distributions and uncertainty | Predicting a full distribution (Swiggy, 2026; DoorDash's Weibull head, 2024) | Turn a predicted distribution into a promise shown to users |
| 5.5 Multi-task models | Multi-output heads (Swiggy's MIMO network; Zomato's prep-time, rider-wait and hand-off heads) | Decide which tasks to share a model across |

**Check your understanding:** Why predict a residual instead of the full ETA? Why might a company show the 80th percentile instead of the mean? When does multi-task learning hurt?

### Chapter 6 · Serving architectures (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Batch, online, streaming | Precompute nightly vs predict per request vs update on events | Choose a pattern for 4 products |
| 6.2 Multi-stage funnels | Retrieval → first-stage ranking → second-stage ranking → re-ranking (Instagram Explore, 2023) | Size each stage for 1 M candidates and a 200 ms budget |
| 6.3 Latency engineering | Model size vs latency (DeepETA chose a linear transformer for latency), caching, request batching, timeouts | Profile a toy service and cut p99 by half |
| 6.4 Fallbacks and degradation | Default predictions, stale caches, rule fallbacks, circuit breakers | Design the fallback when the feature store is down |
| 6.5 Cost | Cost per 1,000 predictions, CPU vs GPU serving, precompute vs on-demand | Compare monthly costs of two serving designs |

**Check your understanding:** Why do ranking systems use a cheap model before an expensive one? What should a fraud check return if it times out? When is batch precompute strictly better than online inference?

### Chapter 7 · Offline and online evaluation (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Offline evaluation | Backtesting on time splits, replay, counterfactual evaluation limits | Backtest an ETA model by week |
| 7.2 Shadow and canary | Shadow traffic, canary percentages, comparing live predictions | Plan a shadow launch with success criteria |
| 7.3 A/B tests | Randomisation units, power, guardrails, novelty effects | Compute the sample size for a 1% conversion lift |
| 7.4 Interleaving | Netflix found interleaving needs over 100× fewer users than its most sensitive A/B metric | Explain when interleaving answers the right question |
| 7.5 Interference | Marketplaces and networks; switchback tests (DoorDash, 2018); cluster randomisation (LinkedIn, 2019) | Design an experiment for a new rider-assignment model |

**Check your understanding:** Why can a user-level A/B test give the wrong answer for a delivery-assignment model? What does interleaving measure that an A/B test does not? Why run a shadow deployment before a canary?

### Chapter 8 · Feedback loops, monitoring and debt (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Feedback loops | Degenerate loops (a model shapes its own training data); popularity spirals | Simulate a recommender's feedback loop for 10 rounds |
| 8.2 Exploration | Contextual bandits and exploration traffic (Netflix artwork personalisation, 2017) | Add epsilon-greedy exploration and measure its cost |
| 8.3 Monitoring | Input, prediction and outcome monitoring; delayed-label proxies | Define 6 alerts for a fraud model and their thresholds |
| 8.4 Hidden technical debt | Entanglement, undeclared consumers, glue code, pipeline jungles (Sculley et al., 2015); the ML Test Score (Breck et al., 2017) | Score a provided system on the ML Test Score rubric |

**Check your understanding:** Why does a fraud model that blocks transactions destroy its own labels? Why is exploration a cost you choose to pay? What is an "undeclared consumer", and why is it dangerous?

### Chapter 9 · Case studies: ETA, logistics, fraud and risk (weeks 9–10)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Food-delivery time | Swiggy's decomposition, delivery time = max(assignment delay + first mile, prep time) + last mile; its MIMO model; its 2026 probabilistic framework | Redraw Swiggy's system from the posts; list open questions |
| 9.2 Preparation time | Zomato's dish embeddings and LSTM over recent orders (MAE 4.64 → 4.13 min, 2020); quantile loss and multi-output heads (2022) | Critique: what would you monitor first? |
| 9.3 Ride and delivery ETA | Uber DeepETA (2022); DoorDash's mixture-of-experts ETA (2024); Lyft's ETA reliability classifier (2024) | Compare three answers to the same problem |
| 9.4 Payments fraud | Stripe Radar: 1,000+ characteristics, under 100 ms, move from Wide & Deep to a DNN-only model (2023) | Design UPI-scale fraud scoring (illustrative scenario) |
| 9.5 Ads click prediction | Google's FTRL-Proximal online learning (2013); Facebook's boosted trees + logistic regression (2014) | Explain why calibration matters for ad auctions |

**Check your understanding:** Why does Swiggy take a max() of two paths? What does a fraud system lose when it trains only on transactions it allowed? Why are ad CTR models updated online?

### Chapter 10 · Case studies: search, feeds and marketplaces (week 11)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Search ranking | Airbnb's move from GBDT to deep networks (first DNN booking-neutral; final 2-layer DNN on ~1.7 B pairs) | List what Airbnb tried that failed, and why that matters |
| 10.2 Embeddings for personalisation | Airbnb listing embeddings: similar-listing CTR +21% (2018) | Design "similar items" for a marketplace |
| 10.3 Ads and organic together | Flipkart's unified ranking: organic orders +1.36%, ad revenue +3.4% (2025) | Explain the trade-off a unified score must encode |
| 10.4 Feed ranking in India | Meesho's feed ranker predicting pCTR and pCVR (+3.5% conversion in A/B tests, 2023) and quality re-ranking (2025) | Write the value function for a social-commerce feed |

**Check your understanding:** Why did Airbnb's first neural network not beat the GBDT? Why combine pCTR and pCVR instead of ranking by one? What can go wrong when ads and organic results share one ranking?

### Chapter 11 · Platforms and ML in the LLM era (week 12)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 ML platforms | Michelangelo from 2017 (shared feature store, sub-10 ms serving) to 2024 (5,000+ models; deep learning in over 60% of tier-1 projects) | Map Michelangelo's components to open-source tools |
| 11.2 Build vs buy | Managed platforms vs open source vs in-house; team size and cost | Write a build-vs-buy memo for a 10-person startup |
| 11.3 Foundation models in classic systems | LLMs as labellers (Flipkart), as feature or embedding sources, foundation models for recommendation (Netflix, 2025) | Decide where an LLM belongs in your ETA design, if anywhere |
| 11.4 Cost and carbon | GPU vs CPU cost, batch vs real-time, cost per decision | Cost model for adding an LLM call to every search |

**Check your understanding:** What problems does a platform team solve that a single model team cannot? When is an LLM a better labeller than a better model? Why might a foundation model raise serving cost more than it raises accuracy?

### Chapter 12 · The ML system design interview (weeks 13–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 12.1 The structure | Clarify → metrics → data and labels → features → model → serving → evaluation → monitoring → iteration | Run the template on "design a news-feed ranker" |
| 12.2 Depth on demand | Going deep on the part the interviewer cares about; trade-offs out loud | 3 timed deep dives (features, serving, experiments) |
| 12.3 Common prompts | ETA, fraud, feed, search, ads CTR, recommendations, content moderation | 6 mock interviews with peers |
| 12.4 AI-era interviews | AI-assisted rounds (Canva, 2025; Meta's reported AI-enabled coding round); explaining and checking AI output | A mock where you must critique an AI-generated design |

**Check your understanding:** Why should you ask about latency and scale before naming a model? How do you recover when you realise mid-interview that your label is leaky? What makes a design answer "senior"?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Framing and metric trees | — |
| 2 | 2 | Lab 2 · Estimation and latency budgets | — |
| 3 | 3 | Lab 3 · Labels, delay and position bias | **P1 due** |
| 4 | 4 | Lab 4 · Point-in-time joins and skew | — |
| 5 | 5 | Lab 5 · Losses and distributional outputs | — |
| 6 | 6 | Lab 6 · Multi-stage serving and p99 | — |
| 7 | 7 | Lab 7 · Experiment design | Mid-term (AI off) |
| 8 | 8 | Lab 8 · Feedback-loop simulation | **P2 due** |
| 9 | 9 | Case-study critique 1 (ETA) | — |
| 10 | 9 | Case-study critique 2 (fraud, ads) | — |
| 11 | 10 | Case-study critique 3 (search, feed) | — |
| 12 | 11 | Lab 9 · Build vs buy and cost model | — |
| 13 | 12 | Mock interviews (round 1) | — |
| 14 | 12 | Mock interviews (round 2) | **P3 due** |
| 15 | Review | P3 design review | Final exam (AI off, whiteboard design) |

## Working with AI in this course

- **Use AI for:** a first-draft design to critique; generating alternative architectures; checking your estimates; playing the interviewer (ask Claude, ChatGPT or Gemini to run a 45-minute mock and to push on weak spots); summarising long engineering posts, then checking the summary against the post.
- **Do without AI (drills):** frame a problem and choose metrics in 5 minutes; back-of-envelope estimates; latency budgets; the full 45-minute whiteboard design. The mid-term, final and mock interviews are AI-off unless the interview format says otherwise.
- **Verify AI output by:** asking for every number's derivation and redoing it; checking that each feature is available at prediction time; checking each case-study claim against the original post; asking "what breaks at 10× load?" and "what if the label arrives 30 days late?"
- **Where AI still fails here:** AI-generated designs tend to be generic (the same feature-store-plus-model diagram for every problem); they skip label delay, interference in marketplaces and feedback loops; they invent precise figures for real companies. In Lab 1 you ask an assistant for a design and mark every unsupported number and every missing failure mode.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (9) and case-study critiques (3) | 20% |
| Projects P1–P3 | 40% |
| Mock interviews (2 rounds, rubric-scored) | 10% |
| Final exam (AI off, whiteboard design) | 30% |

**Mastery gate.** You pass when, without AI, in 45 minutes, for a prompt you have not seen, you produce a design that two reviewers score at least 80% on the course rubric: a clear framing and metric stack; labels with delay and bias handled; features with freshness and point-in-time correctness; a model and loss justified by the decision; a serving design that meets a stated latency budget with estimates; an offline and online evaluation plan that accounts for interference; monitoring, feedback loops and a rollback plan.

## Industry reality

Every company that ships ML at scale has published versions of these designs: delivery-time prediction at Swiggy, Zomato, Uber, DoorDash and Lyft; fraud at Stripe; search and ranking at Airbnb, Flipkart and Meesho; experimentation at Netflix, DoorDash and LinkedIn. Interviews for ML engineers, applied scientists and ML platform engineers usually include a design round of this kind, and some employers now run AI-assisted rounds: Canva expects machine-learning candidates to use AI tools in interviews (2025), and Meta told staff it would let some coding candidates use an AI assistant (reported July 2025).

**Interview questions from this course**

1. *Design delivery-time estimates for a food-delivery app.* Strong answer: decomposes into assignment, first mile, preparation and last mile; real-time restaurant-load features; quantile or distributional output; asymmetric cost of lateness; latency for hundreds of restaurants per listing page; backtesting and switchback experiments.
2. *Design real-time fraud detection for payments.* Strong answer: label delay and maturity windows; selection bias from blocked transactions; streaming velocity features; sub-100 ms budget; rules + model; precision at review capacity; adversarial drift and fast retraining.
3. *Design CTR prediction for ads.* Strong answer: huge sparse features; online learning; calibration for auctions; negative down-sampling with correction; freshness; normalised cross-entropy or log loss; guardrails on revenue and user experience.
4. *Design "similar items" or search ranking for a marketplace.* Strong answer: candidate generation by embeddings, then a ranker; training data from sessions; position bias; cold start; NDCG offline and conversion online; interleaving.
5. *Offline AUC improved but the A/B test is flat. Why?* Strong answer: training–serving skew; metric misalignment; latency increase; calibration shift; novelty or interference; underpowered test; the gain is in segments that don't convert.

## Resources (free first)

- **Courses:** Stanford CS329S Machine Learning Systems Design — https://stanford-cs329s.github.io/ ; Full Stack Deep Learning (2022) — https://fullstackdeeplearning.com/course/2022/ ; Made With ML — https://madewithml.com/ ; Google ML Crash Course, production ML systems — https://developers.google.com/machine-learning/crash-course/production-ml-systems
- **Guides and books:** Google, Rules of Machine Learning — https://developers.google.com/machine-learning/guides/rules-of-ml ; Chip Huyen, *Machine Learning Interviews* (free) — https://huyenchip.com/ml-interviews-book/ ; Chip Huyen, ML systems design notes — https://github.com/chiphuyen/machine-learning-systems-design ; *Machine Learning Systems* (open textbook) — https://mlsysbook.ai/ ; Eugene Yan, "System Design for Recommendations and Search" — https://eugeneyan.com/writing/system-design-for-discovery/ ; Evidently AI, database of ML system design case studies — https://www.evidentlyai.com/ml-system-design ; Lakshmanan, Robinson and Munn, *Machine Learning Design Patterns* (O'Reilly, paid) — https://research.google/pubs/machine-learning-design-patterns/
- **Papers:** Sculley et al., "Hidden Technical Debt in Machine Learning Systems" (2015) — https://proceedings.neurips.cc/paper_files/paper/2015/hash/86df7dcfd896fcaf2674f757a2463eba-Abstract.html ; Breck et al., "The ML Test Score" (2017) — https://research.google/pubs/the-ml-test-score-a-rubric-for-ml-production-readiness-and-technical-debt-reduction/ ; Shankar et al., "Operationalizing Machine Learning: An Interview Study" (2022) — https://arxiv.org/abs/2209.09125
- **Case studies:** listed under Sources; read each original post, not a summary.

## Sources

- Uber, "Meet Michelangelo" (5 Sep 2017) — https://www.uber.com/blog/michelangelo-machine-learning-platform/ ; "From Predictive to Generative – How Michelangelo Accelerates Uber's AI Journey" (2 May 2024) — https://www.uber.com/blog/from-predictive-to-generative-ai/ ; "DeepETA: How Uber Predicts Arrival Times" (10 Feb 2022) — https://www.uber.com/blog/deepeta-how-uber-predicts-arrival-times/ ; DeeprETA paper — https://arxiv.org/abs/2206.02127 (checked 2026-10)
- Swiggy Bytes: "The Swiggy Delivery Challenge (Part One)" (27 Sep 2018) — https://medium.com/swiggy-bytes/the-swiggy-delivery-challenge-part-one-6a2abb4f82f6 ; "Predicting Food Delivery Time at Cart" (11 Aug 2023) — https://medium.com/swiggy-bytes/predicting-food-delivery-time-at-cart-cda23a84ba63 ; "Solving Regional Consistency of Delivery ETA with a Deep Probabilistic Framework" (8 Oct 2026) — https://medium.com/swiggy-bytes/solving-regional-consistency-of-delivery-eta-with-a-deep-probabilistic-framework-8d82d6abdf41 (checked 2026-10)
- Zomato: "The Deep Tech Behind Estimating Food Preparation Time" (4 Feb 2020) — https://www.zomato.com/blog/food-preparation-time/ ; "Predicting your order's Food Preparation Time" (22 Jun 2022) — https://www.zomato.com/blog/predicting-fpt-optimally/ (checked 2026-10)
- DoorDash, "Precision in Motion: Deep learning for smarter ETA predictions" (1 Oct 2024) — https://careersatdoordash.com/blog/deep-learning-for-smarter-eta-predictions/ ; "Switchback Tests and Randomized Experimentation Under Network Effects" (13 Feb 2018) — https://careersatdoordash.com/blog/switchback-tests-and-randomized-experimentation-under-network-effects-at-doordash/ ; Lyft, "ETA Reliability at Lyft" (20 Jun 2024) — https://eng.lyft.com/eta-estimated-time-of-arrival-reliability-at-lyft-d4ca2720bda8 (checked 2026-10)
- Stripe, "How we built it: Stripe Radar" (29 Mar 2023) — https://stripe.com/blog/how-we-built-it-stripe-radar ; McMahan et al., "Ad Click Prediction: a View from the Trenches" (KDD 2013) — https://research.google/pubs/ad-click-prediction-a-view-from-the-trenches/ ; He et al. (Facebook, 2014) — https://quinonero.net/Publications/predicting-clicks-facebook.pdf (checked 2026-10)
- Airbnb: "Applying Deep Learning to Airbnb Search" — https://arxiv.org/abs/1810.09591 ; "Real-time Personalization using Embeddings for Search Ranking" (KDD 2018) — https://www.kdd.org/kdd2018/accepted-papers/view/real-time-personalization-using-embeddings-for-search-ranking-at-airbnb ; listing embeddings post (13 Mar 2018) — https://medium.com/airbnb-engineering/listing-embeddings-for-similar-listing-recommendations-and-real-time-personalization-in-search-601172f7603e (checked 2026-10)
- Flipkart: "The Science of Unified Ranking" (4 Nov 2025) — https://blog.flipkart.tech/the-science-of-unified-ranking-integrating-ads-and-organic-recommendations-8cc24113ef21 ; "LLMs for Relevance" (2025) — https://blog.flipkart.tech/llms-for-relevance-automating-high-quality-product-relevance-labeling-in-flipkart-search-ddd5ca50b584 ; Meesho on AWS, generalised feed ranker (20 Oct 2023) — https://aws.amazon.com/blogs/machine-learning/how-meesho-built-a-generalized-feed-ranker-using-amazon-sagemaker-inference/ ; Meesho, "Quality Focused Feed Re-ranking" (1 Jul 2025) — https://www.meesho.io/blog/quality-focused-feed-re-ranking (checked 2026-10)
- Instacart, "Lessons Learned: The Journey to Real-Time Machine Learning at Instacart" (6 Sep 2022) — https://tech.instacart.com/lessons-learned-the-journey-to-real-time-machine-learning-at-instacart-942f3a656af3 ; Meta, "Scaling the Instagram Explore recommendations system" (9 Aug 2023) — https://engineering.fb.com/2023/08/09/ml-applications/scaling-instagram-explore-recommendations-system/ ; Netflix, "Interleaving in Online Experiments" (29 Nov 2017) — https://medium.com/netflix-techblog/interleaving-in-online-experiments-at-netflix-a04ee392ec55 ; "Artwork Personalization at Netflix" (7 Dec 2017) — https://medium.com/netflix-techblog/artwork-personalization-c589f074ad76 (checked 2026-10)
- Chip Huyen, *Machine Learning Interviews* (2021) — https://huyenchip.com/ml-interviews-book/ ; Canva, "Yes, You Can Use AI in Our Interviews" (11 Jun 2025) — https://www.canva.dev/blog/engineering/yes-you-can-use-ai-in-our-interviews/ ; 404 Media, "Meta Is Going to Let Job Candidates Use AI During Coding Tests" (29 Jul 2025) — https://www.404media.co/meta-is-going-to-let-job-candidates-use-ai-during-coding-tests/ (checked 2026-10)

_Last reviewed: 2026-10_
