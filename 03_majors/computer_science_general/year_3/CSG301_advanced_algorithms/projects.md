# CSG301 · Labs and projects

Use Python for exploration and C++ or Rust where performance is measured. Every experimental claim states the machine, compiler or interpreter version, input source, number of runs and spread (median and interquartile range, or a 95% confidence interval). Every optimality claim comes with a certificate (a dual solution, a cut, or an exhaustive check on small inputs). Proof parts of labs are AI-off; code parts may use assistants, but you must be able to explain every line in the oral.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Balls, bins and two choices | Simulate one-choice and two-choice allocation up to n = 10⁷; fit max load against log n / log log n and log log n | Plots with fitted curves; a half-page proof sketch of the one-choice bound (AI off) | 4 h |
| 2 · Min cut, randomized vs deterministic | Implement Karger–Stein and Stoer–Wagner; run on 20 graphs (random, planted cut, road-network sample) | Success-probability table vs repetitions; runtime comparison; the instance where Karger needed the most trials | 5 h |
| 3 · LP modelling and certificates | Model a transport problem and a shift-scheduling problem; solve with HiGHS; write and solve the duals; check complementary slackness yourself | Models, dual models, a script that verifies optimality from primal + dual without calling the solver | 6 h |
| 4 · Flow engines | Dinic and FIFO push-relabel with global relabelling; DIMACS max-flow format; instances from 10³ to 10⁶ edges | Runtime table, operation counts (pushes, relabels, phases), min-cut certificate checks | 6 h |
| 5 · Approximation ratios in practice | Greedy set cover, LP rounding (deterministic and randomized), and ILP optimum on 200 generated and 20 real instances | Observed ratio distributions vs proven bounds; the worst instance for each method; AI-graded proof exercise | 5 h |
| 6 · SDP MAX-CUT | Goemans–Williamson with CVXPY and random hyperplanes; compare with local search and the SDP upper bound | Cut values, SDP bounds, ratio histogram over 1,000 roundings | 4 h |
| 7 · Caching with and without predictions | Replay a public cache or block trace with LRU, FIFO, marking, Belady; add a next-arrival predictor with tunable noise | Miss-rate table; consistency/robustness plot as prediction noise grows | 5 h |
| 8 · Heavy hitters, HLL and quantiles | One hour of Wikimedia pageviews: exact counts vs Misra–Gries, Count-Min, HLL and KLL under a 1 MB cap | Error vs memory plots against the theoretical (ε, δ) curves; AI-graded sketch exercise | 6 h |
| 9 · FPT vs ILP | Vertex cover: Buss kernel + branching vs an ILP solver on PACE-style instances | Instances solved within 60 s per method; kernel sizes; where each method wins | 5 h |
| 10 · Memory layouts | Sorted array, Eytzinger, B-tree-like blocks and branchless search on 10⁸ keys | Throughput and `perf stat` cache-miss counters; a one-paragraph explanation per layout | 4 h |
| 11 · Evolving heuristics | Run OpenEvolve (or a 100-line evolver you write) to evolve an online bin-packing rule; compare against First-Fit and Best-Fit on held-out instances | Training vs held-out results, total LLM calls and cost, the evolved code with your explanation of why it works (or why it overfits) | 5 h |

## Projects

### P1 · Sketches for a real stream (L1, ~6 hours)

**Real-world inspiration:** cardinality and heavy-hitter queries in analytics systems are answered from sketches (Redis HyperLogLog, Apache DataSketches) because exact answers would need memory proportional to the data.

**What to build:** a small library with Misra–Gries, Count-Min and HyperLogLog, each with `update`, `query` and `merge`, plus a command-line tool that reads a Wikimedia pageviews file and reports the top-100 pages and the number of distinct pages.

**Acceptance criteria:**
- Total memory for all sketches ≤ 1 MB, measured, not estimated.
- Top-100 recall ≥ 95% against exact counts on three different hours of data.
- HLL relative error within twice the theoretical standard error (1.04/√m) in at least 19 of 20 seeded runs.
- `merge` of 8 shard sketches gives the same estimate (HLL) or an estimate within the stated bound (Count-Min) as a single sketch over all data, shown by tests.
- A two-page report connecting each observed error to its theoretical guarantee.

**Stretch goals:** add Count-Sketch and compare with Count-Min on a heavy-tailed stream; add a KLL quantile sketch and report p50/p99 error.

**What it proves to an employer:** you can trade memory for bounded error and explain the bound, which data-platform and analytics-infrastructure teams need.

### P2 · A certified flow and matching toolkit (L2, ~15 hours)

**Real-world inspiration:** assignment, dispatch and scheduling engines (see DoorDash's dispatch write-up in CS201) depend on flow and LP solvers whose answers must be trusted when money or people are allocated.

**What to build:** a C++ or Rust library with Dinic, push-relabel, Hopcroft–Karp and successive-shortest-path min-cost flow, Python bindings, and an **independent checker** that verifies every answer: a min cut equal to the flow value for max-flow, and feasible dual potentials with complementary slackness for min-cost flow. Use it to solve a realistic assignment of 2,000 students to lab slots with capacities, minimum class sizes (lower bounds) and preference costs.

**Acceptance criteria:**
- The checker accepts the output on 10,000 random instances and rejects every one of 50 deliberately corrupted outputs.
- Agreement with Google OR-Tools on all DIMACS-format test instances you choose (at least 30, up to 10⁶ edges).
- Runtime within 3× of OR-Tools on the largest instances, with a profile explaining the remaining gap.
- The lab-slot assignment respects every lower and upper bound and reports the dual prices of the three most contested slots, with a one-paragraph interpretation.
- Property-based tests (Hypothesis or proptest) for conservation and capacity constraints.

**Stretch goals:** a cost-scaling min-cost flow; incremental re-solving when ten students change preferences; a formal proof in CSG401 that the checker is correct.

**What it proves to an employer:** you build optimization code whose outputs can be audited, a habit valued in logistics, fintech and infrastructure teams.

### P3 · An engineered solver for an NP-hard problem with certified gaps (L3, portfolio-grade, ~30 hours)

**Real-world inspiration:** the PACE challenge each year asks teams to solve an NP-hard problem exactly or heuristically on public instances; industrial routing and covering problems are solved the same way, by combining exact methods, approximation and local search with lower bounds. Choose either a recent PACE track (check [pacechallenge.org](https://pacechallenge.org/) for the current problems) or an **illustrative scenario**: choosing locations for 40 dark stores in a city to cover 95% of 50,000 order points within a 2 km radius (a weighted set-cover / facility-location problem built on OpenStreetMap data).

**What to build:** a solver with four layers: (1) reductions and kernelization; (2) an exact method for small or low-parameter instances (branch and bound, FPT branching or ILP); (3) an approximation algorithm with a proven ratio; (4) a local-search heuristic for large instances. Every run reports a **lower bound** (LP relaxation or dual) so the optimality gap is known. Optionally add an AI program-search stage (Lab 11) and compare it fairly.

**Acceptance criteria:**
- A held-out instance set (at least 30% of instances) that was never used for tuning; all headline numbers come from it.
- Every reported solution is checked for feasibility by an independent checker; every gap is computed from a valid bound.
- All instances with the chosen parameter ≤ k (state k) solved to proven optimality within the time limit.
- On the remaining held-out instances, the median gap to the lower bound is reported with its interquartile range, and compared against at least two baselines (plain ILP with the same time limit, and the approximation algorithm alone).
- If an AI-evolved component is used: total compute and calls reported, held-out gain stated with a confidence interval, and the evolved code explained in prose.
- One command reproduces every table and figure from raw instances; a 6–8 page report in paper format (problem, related work, method, proofs, experiments, threats to validity).

**Stretch goals:** submit to the live PACE track if open; parallel portfolio of solvers with work stealing; a short preprint.

**What it proves to an employer or lab:** you can take an NP-hard problem from theory to a measured, honest, reproducible solver, which is the core of research-engineer, operations-research and quant-developer work.

## Feeds into

- [CSG401 Formal Methods and Program Verification](../../year_4/CSG401_formal_methods_and_program_verification/README.md): P2's checker and small lemmas from P3 become verification targets.
- [CSG402 Complexity Theory and Theoretical Cryptography](../../year_4/CSG402_complexity_theory_and_theoretical_cryptography/README.md): concentration bounds, hashing and PCP-based hardness reappear.
- [CSG501 Frontier Seminar](../../year_5/CSG501_frontier_seminar_ai_for_mathematics_science/README.md): Lab 11 is the first step towards AI-assisted discovery projects.
- [CAR301 Career Lab I](../../../../05_shared_years_3_to_5/CAR301_career_lab_i_dsa_mastery_portfolio_and_open/README.md) and [THS501 Thesis or Capstone I](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md): P3 is a strong thesis seed.
- [CSG flagship industry project](../../../../06_career_and_market_readiness/05_industry_projects/CSG_computer_science_general.md): P3 can be its algorithmic core.
