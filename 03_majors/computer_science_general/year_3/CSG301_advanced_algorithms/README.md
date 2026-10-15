# CSG301 · Advanced Algorithms

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 3 · 5 | 4 (≈ 120 hours) | L2 → L4 | [CS201](../../../../02_year_2_core_computer_science/semester_3/CS201_algorithms_and_complexity/README.md), [CS212](../../../../02_year_2_core_computer_science/semester_4/CS212_distributed_systems_i/README.md), [CS216](../../../../02_year_2_core_computer_science/semester_4/CS216_programming_languages_compilers_and_interpreters/README.md); draws on [FND116](../../../../01_year_1_foundations/semester_2/FND116_probability_and_statistics_i/README.md) and [FND113](../../../../01_year_1_foundations/semester_2/FND113_linear_algebra_and_calculus_for_computing/README.md) | [CSG401](../../year_4/CSG401_formal_methods_and_program_verification/README.md); recommended for [CSG402](../../year_4/CSG402_complexity_theory_and_theoretical_cryptography/README.md) and [CSG501](../../year_5/CSG501_frontier_seminar_ai_for_mathematics_science/README.md); supports [CAR301](../../../../05_shared_years_3_to_5/CAR301_career_lab_i_dsa_mastery_portfolio_and_open/README.md) and [THS501](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md) |

Part of the [Computer Science (Theory, Systems and Research) major](../../README.md). CS201 taught the classical toolkit (divide and conquer, greedy, DP, graphs, basic flows, NP-hardness, first approximation algorithms, Bloom filters and reservoir sampling). This course does not repeat it. It adds the tools researchers and senior engineers use when the classical toolkit runs out: probability with proofs, linear programming and duality, flows at depth, approximation with guarantees, online decisions, sublinear memory, parameterized complexity, and measurement on real hardware.

## Why this course matters now

Classical problems are still moving. In 2022 maximum flow was solved in almost-linear time ([Chen et al., FOCS 2022](https://arxiv.org/abs/2203.00671)); in 2025 Duan and co-authors broke Dijkstra's "sorting barrier" for directed single-source shortest paths ([arXiv 2504.17033](https://arxiv.org/abs/2504.17033), STOC 2025 best paper). The tools of this course run in production: Redis counts distinct elements with HyperLogLog in at most 12 KB per key with a standard error of 0.81% ([Redis docs](https://redis.io/docs/latest/develop/data-types/probabilistic/hyperloglogs/)), NGINX offers "power of two choices" load balancing (`random two`) ([NGINX docs](https://nginx.org/en/docs/http/ngx_http_upstream_module.html#random)), and SciPy's `linprog` uses the open-source HiGHS solver by default ([SciPy docs](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.linprog.html)). AI has entered the field as a research instrument: AlphaEvolve found a 48-multiplication scheme for 4×4 complex matrices ([arXiv 2506.13131](https://arxiv.org/abs/2506.13131)), and FunSearch evolved new constructions and bin-packing heuristics ([Nature, 2023](https://www.nature.com/articles/s41586-023-06924-6)). Yet on LiveCodeBench Pro the best tool-free model solved 0% of hard contest problems, failing on subtle case analysis ([arXiv 2506.11928](https://arxiv.org/abs/2506.11928)), and on 77 classical algorithms with formal contracts, the best model produced a verified Lean implementation 7.8% of the time ([AlgoVeri, arXiv 2602.09464](https://arxiv.org/abs/2602.09464)). What stays valuable is the person who can prove a guarantee, find the instance that breaks a heuristic, and tell a real speed-up from a measurement artefact.

## Learning outcomes

By the end you can:

1. **Prove** tail bounds (Markov, Chebyshev, Chernoff–Hoeffding, union bound) for randomized algorithms, and **choose** between Las Vegas and Monte Carlo designs with explicit failure probabilities.
2. **Formulate** optimization problems as linear programs, **write** the dual, and **use** complementary slackness and duality certificates to prove optimality.
3. **Implement** Dinic, push-relabel and min-cost flow, and **reduce** scheduling, assignment and segmentation problems to flows with lower bounds and demands.
4. **Design** approximation algorithms by greedy, local search, LP rounding, primal-dual and semidefinite programming, and **prove** their ratios.
5. **Analyse** online algorithms by competitive ratio, and **design** learning-augmented algorithms that are both consistent (good with good predictions) and robust (safe with bad ones).
6. **Build** streaming sketches (Misra–Gries, Count-Min, AMS, HyperLogLog) with stated (ε, δ) guarantees, and **verify** the guarantees empirically.
7. **Solve** NP-hard problems exactly for small parameters with kernels, bounded search trees, colour coding and treewidth DP.
8. **Engineer** algorithms for real machines (caches, SIMD, parallelism) and **report** results with reproducible benchmarks.
9. **Evaluate** AI-proposed algorithms and proofs with counterexample search, certificates and formal checks.

## Chapters and lessons

### Chapter 1 · Probability for algorithm designers (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Expectation and indicators | Linearity of expectation without independence; coupon collector; expected comparisons in randomized quicksort (proof, not recap) | Derive the expected number of fixed points of a random permutation; confirm by simulation |
| 1.2 Concentration | Markov, Chebyshev, Chernoff (multiplicative and additive forms), Hoeffding; when each is tight | Bound the probability that 10⁶ fair coin flips deviate by 1%; compare all four bounds with simulation |
| 1.3 Union bound and amplification | Boosting success probability by repetition and majority vote; median trick | Turn a 2/3-correct estimator into a 1−10⁻⁹ one; count the repetitions needed |
| 1.4 Balls into bins | Max load Θ(log n / log log n); power of two choices gives Θ(log log n) | Lab 1: simulate both up to n = 10⁷ and fit the curves |
| 1.5 Random walks and Markov chains | Hitting and cover times; random-walk 2-SAT; stationary distributions; PageRank as a Markov chain | Implement random-walk 2-SAT; measure steps against the O(n²) bound |

**Check your understanding:** (1) Why does Chernoff need independence (or negative dependence) when linearity of expectation does not? (2) Why does checking only *two* random servers already collapse the maximum load so much? (3) You have an algorithm correct with probability 0.51; how many runs reach 0.999, and what assumption are you making?

### Chapter 2 · Randomized algorithms for graphs, hashing and identity testing (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Karger's min cut | Contraction, success ≥ 2/n², Karger–Stein recursion; the count of min cuts as a corollary | Lab 2: implement Karger–Stein; compare with deterministic Stoer–Wagner |
| 2.2 Hash families | Universal, k-wise independent and tabulation hashing; what each guarantees | Show a linear-probing slowdown with a 2-independent family on structured keys |
| 2.3 Cuckoo and perfect hashing | Worst-case O(1) lookups; FKS two-level scheme; failure and rehash probability | Build a static perfect hash for 10⁶ keys; measure space |
| 2.4 Algebraic fingerprints | Schwartz–Zippel lemma; polynomial identity testing; randomized matrix and string equality | Test equality of two 10⁸-byte files across a "network" with O(log n) bits |
| 2.5 Derandomization and the local lemma | Method of conditional expectations (MAX-SAT ≥ 7/8 for 3-CNF); Lovász Local Lemma; Moser–Tardos algorithmic LLL | Derandomize a random MAX-3SAT assignment; run Moser–Tardos on a k-SAT instance |

**Check your understanding:** (1) Why does Karger's algorithm get better when you stop contracting early and recurse? (2) What breaks in cuckoo hashing if the two hash functions are correlated? (3) Why is polynomial identity testing easy with randomness but not known to be easy deterministically?

### Chapter 3 · Linear programming and duality (weeks 3–4)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Modelling | Variables, constraints, objectives; standard and slack forms; modelling diet, transport, scheduling and max-flow as LPs | Model a 20-city transport problem and solve it with HiGHS |
| 3.2 Geometry and simplex | Polyhedra, vertices, basic feasible solutions; pivoting; degeneracy and Bland's rule; Klee–Minty worst case | Run simplex by hand on a 3-variable LP; draw the path |
| 3.3 Duality | Weak and strong duality, complementary slackness; dual variables as prices; Farkas' lemma | Write the dual of max-flow and show it is min-cut |
| 3.4 Integrality | Integer programs vs LP relaxations; integrality gaps; total unimodularity (bipartite matching, flows) | Prove bipartite matching LP is integral; find a graph where non-bipartite matching LP is not |
| 3.5 Solving at scale | Interior-point methods and the ellipsoid method (ideas and complexity); separation oracles; open-source solvers (HiGHS, OR-Tools) | Lab 3: solve a 10⁵-variable LP; verify optimality from the dual certificate yourself |
| 3.6 Multiplicative weights | Experts problem; MWU as a meta-algorithm for approximately solving LPs and zero-sum games (Arora–Hazan–Kale) | Approximate a zero-sum game equilibrium with MWU; compare with the LP solution |

**Check your understanding:** (1) A solver returns "optimal": how do you check it without trusting the solver? (2) Why is LP in P while integer LP is NP-hard, and why does total unimodularity close that gap for flows? (3) What does a dual variable equal to zero tell you about its primal constraint?

### Chapter 4 · Network flows in depth (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Blocking flows | Dinic's algorithm, level graphs, O(V²E) and O(E√V) for unit capacities; Hopcroft–Karp | Implement Dinic; count phases on unit-capacity graphs |
| 4.2 Push-relabel | Preflows, heights, FIFO and highest-label rules, global relabelling and gap heuristics | Lab 4: push-relabel vs Dinic on DIMACS-format instances |
| 4.3 Min-cost flow | Successive shortest paths with potentials, cycle cancelling, the optimality condition (no negative residual cycle) | Solve an assignment problem as min-cost flow and check against the Hungarian algorithm |
| 4.4 Circulations | Demands, lower bounds, feasibility; survey design and airline crew style reductions | Model a hospital shift rota with minimum and maximum staffing as a circulation |
| 4.5 Cuts beyond s–t | Global min cut, Gomory–Hu trees; min-cut image segmentation | Segment a 512×512 image with a graph cut; compare edge weights |
| 4.6 The frontier | Electrical flows and interior-point ideas; almost-linear-time max flow (2022) at the level of "what changed" | Read the introduction of Chen et al. (2022) and summarise its key idea in one page |

**Check your understanding:** (1) Why does push-relabel often beat augmenting-path methods in practice despite similar worst-case bounds? (2) How do potentials let Dijkstra run on graphs with negative reduced costs? (3) Why are lower bounds on edges handled by a reduction to a circulation with demands?

### Chapter 5 · Approximation I: greedy, local search and LP rounding (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Ratios and lower bounds | Why you need a lower bound on OPT; the approximation ratio as a theorem | Write the lower bound used in five known approximation proofs |
| 5.2 Greedy with analysis | Set cover H(n) via charging; k-center 2-approximation; submodular maximization (1 − 1/e) | Lab 5: greedy set cover vs ILP optimum on 200 instances |
| 5.3 Local search | Max-cut ½, k-median local search (ratio statement), facility location | Implement local search for max-cut; find an instance where it stops at ½ |
| 5.4 Deterministic LP rounding | Vertex cover via LP (threshold ½); weighted set cover with frequency f | Prove the f-approximation; show the integrality gap example |
| 5.5 Randomized rounding | Set cover with O(log n); MAX-SAT combining two algorithms for ¾ | Implement randomized rounding with Chernoff-based repetition |

**Check your understanding:** (1) Why can't an LP-rounding algorithm beat the integrality gap of its LP? (2) Your greedy rule is "usually within 5% of optimum": what experiment would convince a referee? (3) Why does submodularity make greedy work?

### Chapter 6 · Approximation II: primal-dual, SDP, schemes and hardness (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Primal-dual | Growing duals until constraints go tight; vertex cover, Steiner forest (statement) | Implement primal-dual vertex cover and print the dual certificate |
| 6.2 Semidefinite programming | Goemans–Williamson MAX-CUT with random hyperplane rounding (0.878) | Lab 6: GW with CVXPY on graphs up to 300 nodes; compare with local search |
| 6.3 Approximation schemes | Knapsack FPTAS recap → PTAS by shifting (Baker's technique); Euclidean TSP PTAS idea (Arora) | Implement a PTAS for a geometric covering problem with ε = 0.5, 0.25 |
| 6.4 Metric TSP today | Christofides 1.5; the 2020 Karlin–Klein–Oveis Gharan improvement below 1.5 (what it means, not the proof) | Implement Christofides with a matching library; measure ratios against Concorde-solved optima |
| 6.5 Hardness of approximation | Gap reductions; PCP theorem (statement); Unique Games Conjecture and why 0.878 might be optimal | Prove a gap-preserving reduction for a simple problem |

**Check your understanding:** (1) In primal-dual, what plays the role of the lower bound on OPT? (2) Why does random hyperplane rounding produce exactly the arccos ratio? (3) What would it mean for practice if the Unique Games Conjecture were false?

### Chapter 7 · Online algorithms and algorithms with predictions (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Competitive analysis | Adversaries (oblivious, adaptive); ski rental: 2 deterministic, e/(e−1) randomized | Prove the deterministic lower bound for ski rental |
| 7.2 Paging and caching | LRU and FIFO are k-competitive; the marking algorithm is O(log k) randomized; Belady's offline optimum | Lab 7: replay a real cache trace; measure LRU, FIFO, marking and Belady |
| 7.3 Online matching and ad allocation | Karp–Vazirani–Vazirani RANKING (1 − 1/e); the AdWords problem (Mehta et al.) | Simulate RANKING vs greedy on adversarial and random-order inputs |
| 7.4 Learning-augmented algorithms | Consistency vs robustness; caching with predicted next-arrival (Lykouris–Vassilvitskii); ski rental with predictions | Add an ML predictor to Lab 7; show both good- and bad-prediction regimes |
| 7.5 Online learning link | Regret, experts, MWU from Chapter 3 as an online algorithm | Run MWU on a stock-picking toy and plot regret |

**Check your understanding:** (1) Why is a competitive ratio a guarantee against *any* future, and why is that sometimes too pessimistic? (2) A learned eviction policy beats LRU on your trace: what must you show before shipping it? (3) Why does random arrival order help online matching?

### Chapter 8 · Streaming and sketching (weeks 9–10)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 The streaming model | One pass, polylog memory; (ε, δ) guarantees; lower bounds by communication complexity (idea) | Prove exact distinct counting needs Ω(n) bits for deterministic algorithms (sketch) |
| 8.2 Heavy hitters | Misra–Gries (deterministic, εN error); Count-Min and Count-Sketch; heavy hitters with a heap | Lab 8: top-100 pages from a Wikimedia pageviews hour with 1 MB of memory |
| 8.3 Distinct elements | Flajolet–Martin, HyperLogLog, HLL++ bias correction; merging sketches | Implement HLL; plot error vs register count; merge sketches from 8 "shards" |
| 8.4 Frequency moments | AMS sketch for F₂; median-of-means | Estimate F₂ of a Zipf stream; compare with exact |
| 8.5 Dimensionality reduction | Johnson–Lindenstrauss; random projections; sparse JL; link to vector search | Project 10⁴ embeddings to 256 dimensions; measure distance distortion |
| 8.6 Production sketches | Apache DataSketches, Redis HyperLogLog; quantile sketches (KLL, t-digest) and their error models | Compare KLL and exact p99 latency over a 10⁷-sample stream |

**Check your understanding:** (1) Why can Count-Min only overestimate, and when is Count-Sketch better? (2) Why can HyperLogLog sketches be merged but a sample-based estimator often cannot? (3) A dashboard shows p99 from a sketch: what error should it display?

### Chapter 9 · Parameterized complexity basics (week 11)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 FPT | Running time f(k)·poly(n); vertex cover in O(2^k · n) by bounded search trees, then better branching | Implement branching vertex cover; measure against k |
| 9.2 Kernelization | Buss kernel (k² edges); crown and LP-based 2k kernels | Lab 9: kernel + branching vs an ILP on PACE-style instances |
| 9.3 Colour coding | k-path in 2^O(k) · poly(n) time; derandomization by perfect hash families (idea) | Find a 10-vertex path in a 10⁵-edge graph |
| 9.4 Treewidth | Tree decompositions; DP for independent set on bounded treewidth; why road networks have small separators | Compute a decomposition with a heuristic; run the DP |
| 9.5 Hardness | W[1]-hardness of clique (statement); ETH and SETH-based lower bounds | Explain why "k-clique in n^o(k)" would refute ETH |

**Check your understanding:** (1) Why is vertex cover FPT but clique (believed) not, when they are closely related? (2) What does a polynomial kernel guarantee in practice? (3) Why does small treewidth make NP-hard problems easy?

### Chapter 10 · Algorithm engineering (weeks 12–13)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 The cycle | Design → analyse → implement → experiment → refine (Sanders); benchmark suites (DIMACS, SNAP, PACE) | Pick a benchmark suite and justify it for one problem |
| 10.2 Memory hierarchy | External-memory and cache-oblivious models; van Emde Boas and Eytzinger layouts; branchless binary search | Lab 10: four binary-search layouts on 10⁸ keys with `perf stat` |
| 10.3 Parallel algorithms | Work–span model; parallel prefix sums; parallel BFS (direction-optimizing); work stealing | Parallel BFS on a 10⁷-edge graph; measure speed-up to 16 cores |
| 10.4 Beyond worst case | Smoothed analysis (why simplex works); instance optimality; universal optimality of Dijkstra (2024) | Generate inputs that make your algorithm's worst case appear; explain why real inputs don't |
| 10.5 Honest experiments | Warm-up, variance, confidence intervals, fixed seeds, reporting medians and spreads; artifact evaluation | Rerun a classmate's experiment from their README alone |

**Check your understanding:** (1) Why can an O(n log n) algorithm with random memory access lose to an O(n log² n) one with sequential access? (2) What does a speed-up curve that flattens at 4 cores tell you? (3) What does a reviewer need from your artifact to reproduce a number?

### Chapter 11 · AI-assisted algorithm discovery (week 14)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Search over programs | FunSearch and AlphaEvolve: LLM proposes code, evaluator scores, population evolves; what "discovered" means | Lab 11: evolve a bin-packing heuristic with an open-source evolver (OpenEvolve) against Best-Fit |
| 11.2 Evaluators are the science | Overfitting to the evaluation set; held-out instances; the cost of each evaluation | Hold out 30% of instances; report the gap |
| 11.3 Verifying claimed improvements | Certificates (dual solutions, cuts), exhaustive small cases, Lean statements for small lemmas | Check an AI-claimed bound by brute force for n ≤ 12 |
| 11.4 Where models fail | Case analysis, invariants, off-by-one in amortization; your error log from the semester | Present your three most instructive AI failures |

**Check your understanding:** (1) What is the difference between an evolved heuristic that wins on a benchmark and a new algorithm? (2) Why must the evaluator be cheap and hard to game? (3) What would convince you that an AI-found construction is new?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Balls, bins and two choices | Concentration problem set |
| 2 | 2 | Lab 2 · Min cut, randomized vs deterministic | — |
| 3 | 3 | Lab 3 · LP modelling and certificates | P1 starts |
| 4 | 3 | Lab 3 (cont.) | Duality proofs; **P1 due** |
| 5 | 4 | Lab 4 · Flow engines | — |
| 6 | 5 | Lab 5 · Approximation ratios in practice | P2 starts |
| 7 | 6 | Lab 6 · SDP MAX-CUT | Mid-term (AI off) |
| 8 | 7 | Lab 7 · Caching with and without predictions | — |
| 9 | 8 | Lab 8 · Heavy hitters | — |
| 10 | 8 | Lab 8 (cont.): HLL and quantiles | **P2 due** |
| 11 | 9 | Lab 9 · FPT vs ILP | P3 proposal |
| 12 | 10 | Lab 10 · Memory layouts | — |
| 13 | 10 | Parallel BFS | P3 midpoint review |
| 14 | 11 | Lab 11 · Evolving heuristics | **P3 due** |
| 15 | Review | Oral defence of P3 | Final exam (AI off) |

## Working with AI in this course

- **Use AI for:** explaining a step in a published proof, then checking each line yourself; generating LP and ILP models in HiGHS, OR-Tools or PuLP that you then audit constraint by constraint; writing benchmark harnesses, instance generators and plotting code; searching for counterexamples to a conjecture by brute force; running program-search experiments (Chapter 11). Claude, ChatGPT and Gemini work well as proof tutors; Claude Code, OpenAI Codex or GitHub Copilot can scaffold harnesses.
- **Do without AI (drills):** every proof of a ratio, bound or competitive ratio; writing duals; Chernoff calculations; kernel arguments; weekly 90-minute problem sets; the mid-term and final. You cannot referee an argument you could not have made.
- **Verify AI output by:** (1) checking LP answers against your own dual certificate; (2) brute-forcing small instances (n ≤ 12) for any claimed ratio or optimality; (3) simulating randomized claims with enough trials to see the tail; (4) running streaming code under a memory cap so linear-memory "sketches" fail loudly; (5) for proofs, asking which lemma each step uses and checking that lemma's hypotheses.
- **Where AI still fails here (show it):** LiveCodeBench Pro (2025) and AlgoVeri (2026) document failures on case analysis and on verified implementations of classical algorithms. In Lab 5 and Lab 8 you will ask two assistants for (a) an approximation ratio proof and (b) a sketch with stated guarantees, then grade them. Typical failures to look for: ratios that silently assume a metric, Chernoff bounds applied to dependent variables, "sketches" that store every key, and LP models with a missing constraint that makes the optimum look better.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (11, write-ups with plots and certificates) | 25% |
| Projects P1 / P2 / P3 | 5% / 15% / 20% |
| Proof sets (weekly, AI off) | 10% |
| Mid-term (AI off) | 10% |
| Final exam (AI off) + P3 oral | 15% |

**Mastery gate.** You pass when you can, with AI off: (1) design and prove an approximation algorithm (with its LP or combinatorial lower bound) for a covering or packing problem you have not seen, in 60 minutes; (2) derive a Chernoff-based failure probability for an unseen randomized algorithm and choose the repetition count; (3) given an AI-written "optimal" LP model or sketch with one planted flaw, find the flaw and a failing instance within 20 minutes; and (4) defend a P3 benchmark result under questioning about variance, instance choice and baselines.

## Industry reality

Where this is used (public sources): HyperLogLog in Redis and Google's HyperLogLog++ for cardinality at scale; Apache DataSketches in data platforms; two-choice load balancing in NGINX; LP and min-cost flow in logistics and dispatch (DoorDash moved dispatch to mixed-integer programming, see [CS201](../../../../02_year_2_core_computer_science/semester_3/CS201_algorithms_and_complexity/README.md)); online matching theory behind ad allocation (the AdWords problem); algorithms with predictions in caching research; AlphaEvolve's heuristic for Google's data-centre scheduling, which Google reports recovers about 0.7% of fleet-wide compute ([Google DeepMind, May 2025](https://deepmind.google/discover/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/)). Research engineers and quant developers are interviewed on exactly this material.

**Interview questions from this course**

1. *Count distinct users per country per hour across 10¹⁰ events with 1 MB per counter.* Strong answer: HyperLogLog with error ≈ 1.04/√m; mergeable per shard and per hour; sparse representation for small counts; bias correction; why exact counting needs linear memory.
2. *Our 200 servers get uneven load from random assignment. Fix it cheaply.* Strong answer: power of two choices; max load drops from Θ(log n/log log n) to Θ(log log n); stale load information and herding; least-connections variants.
3. *Find the top 100 search queries in a stream with 1 GB of memory.* Strong answer: Misra–Gries or Count-Min plus a heap; εN error bound with chosen ε; second pass for exact counts if allowed; distributed merge.
4. *We assign delivery partners to orders every 30 seconds. How would you formulate it, and what would you prove?* Strong answer: bipartite matching / min-cost flow or LP; integrality from total unimodularity; dual prices as marginal values; online aspects (batching window as a competitive-ratio trade-off); fallback when constraints break unimodularity.
5. *A model suggests a new eviction policy that beats LRU on last week's trace. Ship it?* Strong answer: held-out traces, worst-case robustness (competitive ratio), consistency/robustness framing from learning-augmented algorithms, fallback to LRU, metrics and A/B test.

## Resources (free first)

- **Lecture notes:** Tim Roughgarden, [CS261 Optimization and Algorithmic Paradigms](https://timroughgarden.org/w16/w16.html) (LP, duality, flows, approximation, online) and [CS264 Beyond Worst-Case Analysis](https://timroughgarden.org/f14/f14.html); MIT [6.854J Advanced Algorithms (OCW)](https://ocw.mit.edu/courses/6-854j-advanced-algorithms-fall-2008/); Amit Chakrabarti, [Data Stream Algorithms notes](https://www.cs.dartmouth.edu/~ac/Teach/data-streams-lecnotes.pdf); Jeff Erickson, [Algorithms and extra notes on randomized algorithms](https://jeffe.cs.illinois.edu/teaching/algorithms/).
- **Free books:** Williamson and Shmoys, [The Design of Approximation Algorithms](http://www.designofapproxalgs.com/); Cygan et al., [Parameterized Algorithms](https://www.mimuw.edu.pl/~malcin/book/parameterized-algorithms.pdf); Arora, Hazan and Kale, [The Multiplicative Weights Update Method](https://theoryofcomputing.org/articles/v008a006/).
- **NPTEL:** [Parameterized Algorithms](https://onlinecourses.nptel.ac.in/noc22_cs81/preview); [Selected Topics in Algorithms](https://onlinecourses.nptel.ac.in/noc23_cs63/preview) (approximation, randomized and parameterized algorithms, IIT Kharagpur).
- **Papers:** [Almost-linear-time max flow](https://arxiv.org/abs/2203.00671); [Breaking the sorting barrier for directed SSSP](https://arxiv.org/abs/2504.17033); [Universal optimality of Dijkstra](https://arxiv.org/abs/2311.11793); [A (slightly) improved approximation for metric TSP](https://arxiv.org/abs/2007.01409); [Competitive caching with machine-learned advice](https://arxiv.org/abs/1802.05399); [Algorithms with Predictions (survey)](https://arxiv.org/abs/2006.09123); [AlphaEvolve](https://arxiv.org/abs/2506.13131); [FunSearch](https://www.nature.com/articles/s41586-023-06924-6).
- **Tools:** [HiGHS](https://highs.dev/), [Google OR-Tools](https://developers.google.com/optimization), [CVXPY](https://www.cvxpy.org/), [NetworkX](https://networkx.org/), [Apache DataSketches](https://datasketches.apache.org/), [PySAT](https://pysathq.github.io/), [OpenEvolve](https://github.com/codelion/openevolve), [Wikimedia pageview dumps](https://dumps.wikimedia.org/other/pageviews/).
- **Practice:** [PACE challenge](https://pacechallenge.org/), [Codeforces](https://codeforces.com/), [AtCoder](https://atcoder.jp/), [Kiran Kedlaya's Putnam archive](https://kskedlaya.org/putnam-archive/) (for probability and combinatorics proofs).
- **Paid, optional:** Mitzenmacher and Upfal, *Probability and Computing* (2nd ed.); Motwani and Raghavan, *Randomized Algorithms*. The free notes above cover the syllabus.

## Sources

All checked 12 Oct 2026.

- Chen, Kyng, Liu, Peng, Probst Gutenberg, Sachdeva, "Maximum Flow and Minimum-Cost Flow in Almost-Linear Time" (FOCS 2022) — https://arxiv.org/abs/2203.00671
- Duan et al., "Breaking the Sorting Barrier for Directed Single-Source Shortest Paths" (STOC 2025) — https://arxiv.org/abs/2504.17033
- Haeupler et al., "Universal Optimality of Dijkstra via Beyond-Worst-Case Heaps" (FOCS 2024) — https://arxiv.org/abs/2311.11793
- Karlin, Klein, Oveis Gharan, "A (Slightly) Improved Approximation Algorithm for Metric TSP" (STOC 2021) — https://arxiv.org/abs/2007.01409
- Redis documentation, HyperLogLog — https://redis.io/docs/latest/develop/data-types/probabilistic/hyperloglogs/
- NGINX `ngx_http_upstream_module`, `random` directive — https://nginx.org/en/docs/http/ngx_http_upstream_module.html#random
- SciPy `linprog` documentation (HiGHS methods) — https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.linprog.html
- Novikov et al., "AlphaEvolve" (arXiv 2506.13131) — https://arxiv.org/abs/2506.13131 ; Google DeepMind, AlphaEvolve announcement (14 May 2025) — https://deepmind.google/discover/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/
- Romera-Paredes et al., FunSearch, *Nature* (Dec 2023) — https://www.nature.com/articles/s41586-023-06924-6
- Zheng et al., "LiveCodeBench Pro" (arXiv 2506.11928) — https://arxiv.org/abs/2506.11928
- AlgoVeri (arXiv 2602.09464, Feb 2026) — https://arxiv.org/abs/2602.09464
- Lykouris and Vassilvitskii (ICML 2018) — https://arxiv.org/abs/1802.05399 ; Mitzenmacher and Vassilvitskii, "Algorithms with Predictions" — https://arxiv.org/abs/2006.09123

_Last reviewed: 2026-10_
