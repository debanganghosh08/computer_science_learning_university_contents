# CS201 · Algorithms and Complexity

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 2 · 3 | 4 (≈ 120 hours) | L1 → L3 | [FND112](../../../01_year_1_foundations/semester_2/FND112_data_structures_and_algorithms_i/README.md) | [CS211](../../semester_4/CS211_database_systems_internals/README.md), [CS216](../../semester_4/CS216_programming_languages_compilers_and_interpreters/README.md), [CAR301](../../../05_shared_years_3_to_5/CAR301_career_lab_i_dsa_mastery_portfolio_and_open/README.md), [CSG301](../../../03_majors/computer_science_general/year_3/CSG301_advanced_algorithms/README.md), [SWE305](../../../03_majors/software_engineering/year_3/SWE305_concurrency_and_performance_engineering/README.md) |

## Why this course matters now

Algorithms decide whether a system costs one server or a thousand. Git still computes diffs with Myers' algorithm by default, Python hashes strings with a keyed hash, SipHash (PEP 456), so attackers cannot force every key into one bucket, and DoorDash rebuilt its courier dispatch from the Hungarian matching algorithm to a mixed-integer program when matching alone stopped scaling (2020). AI systems now solve contest problems at a very high level: Gemini 2.5 Deep Think solved 10 of 12 problems at the 2025 ICPC World Finals. Yet on the LiveCodeBench Pro benchmark (June 2025), the best model without tools solved 0% of the hard problems, and its failures clustered on problems that needed careful case analysis. The skill that stays valuable is turning a messy real problem into a clean model, proving the solution is correct and fast enough, and catching a confident wrong answer before it ships, whether a human or a model wrote it.

## Learning outcomes

By the end you can:

1. **Prove** an algorithm correct with a loop invariant, an exchange argument or induction, and **find** the counterexample when the proof fails.
2. **Analyse** running time with recurrences, the master theorem and amortized analysis (aggregate, accounting, potential), then **confirm** the analysis with a doubling experiment.
3. **Design** solutions with divide and conquer, greedy, dynamic programming and graph modelling, and **explain** why the other paradigms fail on the same problem.
4. **Implement** BFS/DFS, topological sort, strongly connected components, Dijkstra, Bellman-Ford, Floyd-Warshall, Kruskal/Prim with union-find, Edmonds-Karp and KMP, each tested against a brute-force oracle.
5. **Reduce** one problem to another, and **prove** NP-hardness for a new problem by reduction from 3-SAT, vertex cover or subset sum.
6. **Choose** a coping strategy for an NP-hard problem (exact solver, approximation with a proven ratio, heuristic with a lower bound) and **measure** its gap from optimal.
7. **Solve** unseen interview problems in 35–45 minutes: state constraints, pick a complexity budget, code, test and explain trade-offs aloud.
8. **Audit** AI-generated algorithmic code with stress tests, invariants and complexity checks.

## Chapters and lessons

### Chapter 1 · Correctness, models and growth (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 The RAM and word-RAM models | What a "step" costs; why `x in list` is O(n) but `x in set` is expected O(1); input size measured in bits | Count the exact operations of insertion sort on 5 inputs; predict, then time |
| 1.2 Loop invariants and induction | Initialisation, maintenance, termination; strong induction on recursive code | Write invariants for binary search and partition; break each with one changed line |
| 1.3 Asymptotic notation | O, Ω, Θ, o; limits test; common traps (O(n) + O(n²) inside loops, log bases) | Rank 15 functions by growth; prove three orderings formally |
| 1.4 Measuring versus analysing | Doubling experiments, log-log plots, warm-up and noise, `timeit`/Google Benchmark | Fit the exponent of three mystery functions from timings |

**Check your understanding:** Why can an O(n log n) algorithm lose to an O(n²) one on real inputs, and how would you show where the crossover is? What invariant does binary search keep, and which off-by-one bug breaks it? If doubling n multiplies time by 8, what do you conclude, and what could fool you?

### Chapter 2 · Divide and conquer, sorting and randomisation (weeks 2–3)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Recurrences | Recursion trees, substitution, master theorem and its gaps (e.g. T(n)=2T(n/2)+n log n) | Solve 10 recurrences; verify two numerically |
| 2.2 Merge sort, Karatsuba, closest pair | Combine step cost; Karatsuba's 3 multiplications instead of 4 (n^1.585) | Implement Karatsuba; find the size where it beats schoolbook multiplication |
| 2.3 Quicksort and quickselect | Expected O(n log n) via indicator variables; median-of-medians worst-case O(n) selection | Build an input that makes first-element-pivot quicksort quadratic |
| 2.4 Lower bounds and linear sorts | Ω(n log n) decision-tree bound for comparison sorts; counting and radix sort | Radix-sort 10⁷ 32-bit keys; compare with `sorted()` |
| 2.5 Randomised algorithms | Las Vegas vs Monte Carlo; reservoir sampling; Freivalds' matrix check | Implement reservoir sampling; test uniformity with a chi-square test |

**Check your understanding:** Why does the decision-tree argument not forbid radix sort from running in linear time? Quickselect is O(n) expected; what input distribution or adversary makes it slow, and how does randomisation defend against it? When is a Monte Carlo answer acceptable in production?

### Chapter 3 · Hashing, amortization and union-find (weeks 3–4)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Hash tables | Chaining vs open addressing, load factor, universal hashing, why Python and Rust use keyed hashes (SipHash) | Implement linear probing; measure probe length at load 0.5, 0.7, 0.9 |
| 3.2 Hash flooding | Adversarial collisions turn O(1) into O(n); keyed hashing as the defence | Show the slowdown with a fixed weak hash on your own table, then fix it |
| 3.3 Amortized analysis | Aggregate, accounting, potential method; dynamic array doubling vs growing by +k | Prove O(1) amortized append; measure both growth policies |
| 3.4 Union-find | Union by rank, path compression, inverse Ackermann α(n) bound (stated, intuition only) | Count connected components of 10⁶ random edges |
| 3.5 Probabilistic sketches | Bloom filters (false-positive rate), count-min sketch | Size a Bloom filter for 10⁷ keys at 1% false positives; verify empirically |

**Check your understanding:** Why does "amortized O(1)" not guarantee that every single append is fast, and when does that matter (think latency targets)? What breaks if a Bloom filter must support deletion? Why must a hash used on attacker-controlled keys be keyed and secret?

### Chapter 4 · Greedy algorithms (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Exchange arguments | Proving greedy-choice and optimal substructure; "greedy stays ahead" | Prove earliest-finish-time for interval scheduling |
| 4.2 Scheduling | Minimising maximum lateness (earliest deadline first); weighted completion time (Smith's rule) | Implement and verify against brute force for n ≤ 8 |
| 4.3 Huffman coding | Prefix codes, optimality proof, link to entropy (see [CS206](../CS206_mathematics_for_machine_learning/README.md)) | Compress a text file; compare bits/char with its entropy |
| 4.4 When greedy fails | Coin change with {1, 3, 4}; 0/1 knapsack; matroids as the structure behind greedy success | Find the smallest counterexample for three plausible greedy rules |

**Check your understanding:** A greedy rule passes 1,000 random tests. Why is that not a proof, and what kind of input do random tests rarely produce? Why does greedy work for fractional knapsack but not 0/1 knapsack? What would you check first if an AI says "greedy is optimal here"?

### Chapter 5 · Dynamic programming (weeks 6–7)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Designing the state | Subproblem = "answer for a prefix/suffix/interval/subset"; recurrence before code | Write the recurrence for 5 problems before any code |
| 5.2 Classic sequences | Longest increasing subsequence (O(n log n) patience method), edit distance, longest common subsequence | Reconstruct the actual edit script, not just the cost |
| 5.3 Knapsack and pseudo-polynomial time | Why O(nW) is not polynomial in the input size; subset sum | Show the running time explode by adding digits to W |
| 5.4 DP on trees, DAGs and intervals | Tree DP (independent set), longest path in a DAG, matrix-chain / interval DP | Solve 3 CSES tree/interval DP problems |
| 5.5 Bitmask DP and optimisation | Held-Karp TSP O(2ⁿn²); rolling arrays for memory; top-down vs bottom-up trade-offs | Held-Karp for n = 18; measure memory before and after rolling |

**Check your understanding:** How do you know your DP state is complete (contains everything the future depends on)? Why is knapsack NP-hard even though it has an O(nW) algorithm? Memoised recursion overflows the stack at n = 10⁵: name two fixes.

### Chapter 6 · Graph structure and traversal (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Modelling with graphs | Adjacency lists vs matrices; implicit graphs (grids, puzzle states); multi-source BFS | Model a metro map as a graph; answer "fewest interchanges" |
| 6.2 BFS and DFS | Edge classification, discovery/finish times, bipartiteness, cycle detection, 0-1 BFS | Implement iterative DFS (no recursion limit) |
| 6.3 Topological sort | Kahn's algorithm vs DFS finish order; detecting impossible schedules | Course-prerequisite planner over this university's [catalog.json](../../../catalog.json) |
| 6.4 Strongly connected components | Kosaraju and Tarjan; condensation DAG; 2-SAT as an SCC application | Solve a 2-SAT instance with 10⁵ clauses |

**Check your understanding:** Why does BFS give shortest paths in unweighted graphs but DFS does not? What does a back edge in a directed DFS tell you? How does the condensation of a graph turn a cyclic problem into a DAG problem?

### Chapter 7 · Shortest paths and spanning trees (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Dijkstra | Invariant, binary-heap O((V+E) log V), lazy deletion; why negative edges break it | Run on an OpenStreetMap road graph of an Indian city via OSMnx |
| 7.2 Bellman-Ford and negative cycles | Relaxation rounds, detecting arbitrage cycles (log of exchange rates) | Detect an arbitrage loop in a currency table |
| 7.3 All pairs and heuristics | Floyd-Warshall O(V³); A* with admissible, consistent heuristics; bidirectional search | Compare nodes settled by Dijkstra vs A* on the same queries |
| 7.4 Minimum spanning trees | Cut property; Kruskal with union-find; Prim; MST as a TSP lower bound | Prove the cut property; build the MST of 10⁵ points |

**Check your understanding:** Why does adding a constant to every edge weight change shortest paths but not the MST? When is A* no faster than Dijkstra? What fails if Dijkstra's priority queue holds stale entries and you do not skip them?

### Chapter 8 · Network flow and matching (week 10)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Max-flow | Residual graphs, augmenting paths, Ford-Fulkerson, Edmonds-Karp O(VE²) | Implement Edmonds-Karp; trace one run by hand |
| 8.2 Max-flow min-cut | The theorem and what a min cut means in practice (bottleneck, segmentation) | Find the bottleneck links in a small network |
| 8.3 Bipartite matching | Matching as flow; Hall's theorem (intuition); assignment and Hungarian algorithm (overview) | Assign 200 students to lab slots with capacities |
| 8.4 Reductions to flow | Project selection, edge-disjoint paths, baseball elimination | Model and solve two problems as flows |

**Check your understanding:** Why do integer capacities guarantee an integer max flow, and why does that matter for assignment problems? How would you turn "each courier takes at most 2 orders" into a flow network? Why did DoorDash leave pure matching for a mixed-integer program?

### Chapter 9 · String algorithms (week 11)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Exact matching | Prefix function (KMP) and Z-algorithm, both O(n + m) | Implement both; cross-check on 10⁵ random cases |
| 9.2 Rolling hashes | Rabin-Karp, collision probability, double hashing; plagiarism and duplicate detection | Find repeated 50-char blocks across two source files |
| 9.3 Tries and Aho-Corasick | Multi-pattern matching in one pass; autocomplete | Match 10⁴ banned words in a 100 MB log |
| 9.4 Suffix arrays | O(n log n) construction by prefix doubling, LCP array, longest repeated substring | Build a suffix array for a genome sample |

**Check your understanding:** Why is naive matching O(nm) in the worst case, and which input shows it? When is a hash-based match acceptable without verification? What does the LCP array let you answer in O(1) or O(log n) that a trie cannot cheaply?

### Chapter 10 · Intractability, reductions and approximation (weeks 12–13)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 P, NP and certificates | Decision vs optimisation; verifiers; what P = NP would mean | Write polynomial verifiers for 4 problems |
| 10.2 Reductions | Karp reductions; Cook-Levin (statement); the chain 3-SAT → independent set → vertex cover → set cover; subset sum | Prove one new problem NP-complete in writing |
| 10.3 Exact methods that work in practice | SAT solvers (CDCL), integer linear programming, branch and bound | Encode Sudoku and an exam timetable as SAT with PySAT |
| 10.4 Approximation with guarantees | 2-approx vertex cover, greedy set cover (ln n), metric TSP 2-approx via MST, knapsack FPTAS | Measure actual ratio vs ILP optimum on 100 instances |
| 10.5 Heuristics and bounds | Local search, simulated annealing; always report a lower bound so the gap is known | Improve a TSP tour with 2-opt; report the gap to the MST bound |

**Check your understanding:** Why must the reduction go from the known-hard problem to your problem, not the other way? A colleague's heuristic "usually finds the optimum": what would you ask for before trusting it? If a problem is NP-hard, why can a SAT solver still finish instantly on your real instances?

### Chapter 11 · Interview-grade problem solving and algorithm engineering (week 14)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Constraints set the budget | n ≤ 20 → exponential; n ≤ 10³ → O(n²); n ≤ 10⁶ → O(n log n); ~10⁸ simple operations per second as a rough guide | Classify 20 problems by budget before solving |
| 11.2 The stress-test loop | Brute-force oracle, random generator, shrink to a minimal counterexample (Hypothesis) | Find the planted bug in 5 "accepted-looking" solutions |
| 11.3 Thinking aloud | Clarify, examples, brute force first, optimise, test, analyse; common interview patterns (two pointers, monotonic stack, sliding window, binary search on the answer) | Three recorded 40-minute mock interviews |
| 11.4 Theory meets hardware | Cache misses, branch misprediction and constant factors; when a linear scan beats a tree | Compare binary search on a sorted array vs `std::set` for 10⁷ lookups |

**Check your understanding:** Your O(n log n) solution times out at n = 10⁶ in Python; list three causes other than the algorithm. Why should you write the brute force even when you know the optimal approach? How do you explain a trade-off between memory and time to an interviewer in two sentences?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Doubling experiments | Invariant proofs for 3 algorithms |
| 2 | 2 | Lab 2 · Stress-test harness | Recurrence problem set |
| 3 | 2–3 | Lab 3 · Hash tables under attack | — |
| 4 | 3 | Lab 3 (cont.) | **P1 due** |
| 5 | 4 | Lab 4 · Greedy proofs and counterexamples | Greedy proof write-up |
| 6 | 5 | Lab 5 · DP gauntlet | — |
| 7 | 5 | Lab 5 (cont.) | Mid-term (closed book, AI off) |
| 8 | 6 | Lab 6 · Graph modelling | — |
| 9 | 7 | Lab 7 · Shortest paths on real maps | — |
| 10 | 8 | Lab 8 · Matching and flow | **P2 due** |
| 11 | 9 | Lab 9 · String matching at scale | — |
| 12 | 10 | Lab 10 · SAT and ILP encodings | NP-hardness proof |
| 13 | 10 | Lab 10 (cont.) | Approximation-ratio report |
| 14 | 11 | Mock interviews | **P3 due** |
| 15 | Review | Timed problem sets, oral defence of P3 | Final exam |

## Working with AI in this course

- **Use AI for:** explaining a proof step you are stuck on; generating brute-force oracles and random test generators (they are easy to check by reading); suggesting edge cases; translating your solution between Python, C++ and Java; reviewing your complexity argument. Claude, ChatGPT and Gemini all do this well; Claude Code, GitHub Copilot or OpenAI Codex can wire up the stress-test harness.
- **Do without AI (drills):** every proof (invariants, exchange arguments, reductions); every recurrence; weekly timed sets of 3 problems in 90 minutes; whiteboard mock interviews. You cannot verify what you cannot derive, and the exams in this course are AI-off.
- **Verify AI output by:** (1) a stress test against a brute force on thousands of small random inputs plus hand-made edge cases (empty, one element, all equal, maximum values); (2) a doubling experiment to confirm the claimed complexity; (3) asking for the invariant or exchange argument and checking each step yourself; (4) for "NP-hard" claims, checking the reduction's direction and that it runs in polynomial time.
- **Where AI still fails here:** LiveCodeBench Pro (June 2025) reports 0% pass@1 for the best tool-free model on hard problems, with errors concentrated in problems that need subtle case analysis; the same models were strong on implementation-heavy problems. In this course you will collect your own evidence: log every AI solution that passes the sample tests but fails your stress test, and classify why (wrong greedy rule, missing DP state, overflow, wrong complexity).

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (10, auto-graded tests plus short write-ups) | 25% |
| Projects P1–P3 | 30% |
| Proof write-ups (invariant, greedy, NP-hardness) | 10% |
| Mid-term (AI off) | 10% |
| Final exam (AI off) + oral defence of P3 | 25% |

**Mastery gate.** You pass when you can, with AI tools off: (1) solve 2 of 3 unseen problems of LeetCode-medium to hard difficulty in 90 minutes, each with a stated complexity and a passing stress test; (2) write a correct NP-hardness reduction for a problem you have not seen; (3) given an AI-generated solution with a planted bug, find a failing input within 15 minutes.

## Industry reality

Where this shows up (all public): Git's default diff is Myers' O(ND) algorithm (git-diff documentation); CPython's string hashing became keyed SipHash in Python 3.4 to stop collision-flooding attacks (PEP 456); DoorDash described moving dispatch from Hungarian bipartite matching to a mixed-integer program solved by a commercial solver (2020); DeepMind's AlphaDev found sorting routines for short sequences that were merged into LLVM's libc++ (Nature, 2023), and AlphaEvolve found a 48-multiplication method for 4×4 complex matrices (2025). The hiring side of this material (DSA rounds and how AI-assisted interview formats work) is covered in [CAR301](../../../05_shared_years_3_to_5/CAR301_career_lab_i_dsa_mastery_portfolio_and_open/README.md) and [06_career_and_market_readiness](../../../06_career_and_market_readiness/) in depth.

**Interview questions from this course**

1. *Return the k largest values from a stream of 10⁹ numbers.* Strong answer: min-heap of size k, O(n log k) time, O(k) memory; contrasts with quickselect (needs all data in memory); mentions ties and what "stream" rules out.
2. *Given course prerequisites, can a student finish, and in what order?* Strong answer: model as a directed graph; Kahn's algorithm or DFS finish order; cycle means impossible; O(V + E); returns one valid order and explains how to report the cycle.
3. *Cheapest flight from A to B with at most k stops.* Strong answer: explains why plain Dijkstra is wrong (the state must include stops); offers Bellman-Ford limited to k+1 rounds or Dijkstra on (city, stops) states; gives both complexities.
4. *Design an LRU cache with O(1) get and put.* Strong answer: hash map + doubly linked list; walks through eviction; discusses thread safety and what amortized versus worst case means for latency.
5. *Our delivery batching problem looks hard. Is it, and what would you ship?* Strong answer: recognises a vehicle-routing / set-cover structure, sketches a reduction showing NP-hardness, proposes an ILP for small instances plus a heuristic with a reported lower bound, and defines the metric for "good enough".

## Resources (free first)

- **Primary text:** Jeff Erickson, *Algorithms* (free PDF) — https://jeffe.cs.illinois.edu/teaching/algorithms/
- **Courses:** MIT 6.006 Introduction to Algorithms (Spring 2020) — https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/ ; MIT 6.046J Design and Analysis of Algorithms (Spring 2015) — https://ocw.mit.edu/courses/6-046j-design-and-analysis-of-algorithms-spring-2015/ ; NPTEL Design and Analysis of Algorithms (Madhavan Mukund, CMI) — https://nptel.ac.in/courses/106106131 ; Tim Roughgarden's free lecture videos — https://www.algorithmsilluminated.org/
- **Reference:** Antti Laaksonen, *Competitive Programmer's Handbook* (free) — https://cses.fi/book/book.pdf ; cp-algorithms — https://cp-algorithms.com/ ; Pat Morin, *Open Data Structures* — https://opendatastructures.org/ ; VisuAlgo animations — https://visualgo.net/
- **Practice:** CSES Problem Set — https://cses.fi/problemset/ ; USACO Guide — https://usaco.guide/ ; Codeforces — https://codeforces.com/ ; AtCoder — https://atcoder.jp/ ; LeetCode — https://leetcode.com/ ; Kattis — https://open.kattis.com/
- **Tools:** Hypothesis — https://hypothesis.readthedocs.io/ ; NetworkX — https://networkx.org/ ; OSMnx — https://osmnx.readthedocs.io/ ; PySAT — https://pysathq.github.io/ ; Google OR-Tools — https://developers.google.com/optimization
- **Paid, optional:** Cormen, Leiserson, Rivest and Stein, *Introduction to Algorithms*, 4th ed. (MIT Press, 2022); Kleinberg and Tardos, *Algorithm Design*. Erickson covers the same ground for free.
- **Curriculum benchmark:** ACM/IEEE-CS/AAAI Computer Science Curricula 2023 — https://csed.acm.org/

## Sources

- Git diff algorithms (Myers is the default), git-diff documentation — https://git-scm.com/docs/git-diff (checked 2026-10)
- PEP 456, Secure and interchangeable hash algorithm — https://peps.python.org/pep-0456/ (checked 2026-10)
- DoorDash Engineering, "Next-Generation Optimization for Dasher Dispatch" (Feb 2020) — https://careersatdoordash.com/blog/next-generation-optimization-for-dasher-dispatch-at-doordash/ (checked 2026-10)
- Google DeepMind, "Gemini achieves gold-medal level at the ICPC World Finals" (Sep 2025) — https://deepmind.google/blog/gemini-achieves-gold-medal-level-at-the-international-collegiate-programming-contest-world-finals/ (checked 2026-10)
- Zheng et al., "LiveCodeBench Pro: How Do Olympiad Medalists Judge LLMs in Competitive Programming?" (arXiv 2506.11928, Jun 2025; NeurIPS 2025 Datasets and Benchmarks) — https://arxiv.org/abs/2506.11928 (checked 2026-10)
- Mankowitz et al., "Faster sorting algorithms discovered using deep reinforcement learning", *Nature* 618 (2023) — https://www.nature.com/articles/s41586-023-06004-9 (checked 2026-10)
- Novikov et al., "AlphaEvolve: A coding agent for scientific and algorithmic discovery" (arXiv 2506.13131, Jun 2025) — https://arxiv.org/abs/2506.13131 (checked 2026-10)

_Last reviewed: 2026-10_
