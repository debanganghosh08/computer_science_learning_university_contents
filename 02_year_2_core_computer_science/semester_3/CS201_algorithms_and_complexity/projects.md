# CS201 · Labs and projects

Every lab and project ships with three things: code, a test suite that includes a brute-force oracle, and a short write-up with measured numbers. Python is fine for most labs; use C++, Java, Go or Rust where a time limit says so.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Doubling experiments | Predict and then measure the growth rate of insertion sort, merge sort, `sorted()` and a hash-set build | Log-log plots, fitted exponents, one paragraph on where the measurements disagree with theory and why | 3 h |
| 2 · Stress-test harness | Build a reusable harness: random generator + brute force + candidate + automatic shrinking to the smallest failing input (Hypothesis or your own) | Harness repo; 5 buggy solutions (provided) each with the minimal failing input it found | 4 h |
| 3 · Hash tables under attack | Implement chaining and linear probing; show probe lengths by load factor; craft collisions against a fixed, unkeyed hash on *your own* table, then switch to a keyed hash | Benchmarks before and after; explanation linked to PEP 456 | 5 h |
| 4 · Greedy proofs and counterexamples | For 6 scheduling and covering rules, prove optimality or find the smallest counterexample by exhaustive search | Proofs (exchange argument) and counterexamples with the search script | 3 h |
| 5 · DP gauntlet | Solve 10 CSES dynamic programming problems; write the state and recurrence *before* code | Accepted submissions + a one-page "state design" sheet per problem | 6 h |
| 6 · Graph modelling | Turn 5 word problems (metro interchanges, prerequisite planning over this repo's `catalog.json`, 2-SAT) into graphs and solve them | Code, models drawn as diagrams, complexity of each | 4 h |
| 7 · Shortest paths on real maps | Load a city's OpenStreetMap road graph with OSMnx; run Dijkstra, A* and bidirectional Dijkstra; compare nodes settled and query time | Results table over 500 random queries; correctness check against NetworkX | 5 h |
| 8 · Matching and flow | Implement Edmonds-Karp; solve student-to-lab-slot assignment with capacities and a project-selection problem | Code, the flow networks, and the min cut explained in plain English | 4 h |
| 9 · String matching at scale | Implement KMP, Z, Rabin-Karp and Aho-Corasick; match 10⁴ patterns in a 100 MB log | Benchmarks against Python `re` and `grep -F`; analysis of where each wins | 4 h |
| 10 · SAT and ILP encodings | Encode Sudoku and a small exam timetable as SAT (PySAT) and as an ILP (OR-Tools); compare with your own backtracking | Encodings, solve times by instance size, and a 1-page note on why solvers beat worst-case theory on these inputs | 5 h |

## Projects

### P1 · Live contest leaderboard (L1, ~6 hours)

**Real-world inspiration.** Programming-contest platforms such as Codeforces, CodeChef and AtCoder update standings live for thousands of contestants; ICPC rankings sort by problems solved, then by penalty time.

**What to build.** A leaderboard library and CLI that processes `submit(user, problem, minute, verdict)` events with ICPC-style scoring (solved count, then penalty: minute of first accept + 20 per earlier wrong attempt) and answers `rank(user)`, `top(k)` and `count_ahead(score)`. Choose the data structure (Fenwick tree over a score key, a balanced BST or a skip list) and justify it.

**Acceptance criteria**
- Matches a brute-force re-sort oracle on 10,000 random event sequences (including ties and repeated accepts).
- Processes 10⁶ events and 10⁵ queries in under 3 s in Python or under 0.5 s in a compiled language, on a stated machine.
- `rank` and `top(k)` run in O(log n) and O(k + log n); the README proves both and shows a doubling experiment.
- Clean edge-case handling: unknown user, accept after accept, zero submissions.

**Stretch goals.** A "scoreboard freeze" for the last hour with a replayable reveal; persistent snapshots so any past minute can be queried.

**What it proves to an employer.** You pick data structures from the operation mix, not from habit, and you prove correctness with an oracle before claiming speed.

### P2 · City route planner (L2, ~15 hours)

**Real-world inspiration.** Navigation products such as Google Maps, Mappls (MapmyIndia) and the open-source OSRM answer shortest-path queries on road graphs with millions of edges. This project uses OpenStreetMap data for an Indian city of your choice.

**What to build.** Download a drivable road network (e.g. Pune or Bengaluru) with OSMnx; weight edges by travel time from length and speed tags; implement Dijkstra, bidirectional Dijkstra and A* with an admissible heuristic (straight-line distance divided by the maximum speed); expose a CLI or small HTTP endpoint that returns the route and ETA.

**Acceptance criteria**
- Graph has at least 100,000 nodes; loading and preprocessing are scripted and reproducible.
- On 1,000 random origin–destination pairs, every algorithm returns the same travel time as NetworkX's reference implementation (within 10⁻⁶).
- Median query time is reported for each algorithm; in a compiled language it is under 50 ms, in Python under 300 ms.
- The report shows nodes settled per algorithm and explains, with a plot, why A* helps on some queries and not on others.
- Unreachable destinations and one-way streets are handled and tested.

**Stretch goals.** ALT (landmarks + triangle inequality) or contraction hierarchies; time-of-day edge weights; k alternative routes with limited overlap.

**What it proves to an employer.** You can take messy real data, apply the right graph algorithm, and back every speed claim with measurements and a correctness reference.

### P3 · Delivery dispatch optimiser (L3, portfolio-grade, ~30 hours)

**Real-world inspiration.** Food and quick-commerce delivery (Swiggy, Zomato, Zepto, DoorDash, Uber Eats) must assign orders to couriers every few seconds. DoorDash has publicly described moving its dispatch from Hungarian bipartite matching to a mixed-integer program because matching alone did not scale and could not express multi-order routes (DoorDash Engineering, 2020). The scenario below is illustrative; it does not reproduce any company's system.

**What to build.** A simulator plus optimiser. Orders (restaurant, customer, ready time) and couriers (position, capacity 2) arrive over a simulated evening on the P2 road graph or a Euclidean grid. Every tick, the optimiser:
1. assigns single orders by minimum-cost bipartite matching (Hungarian algorithm or min-cost flow);
2. considers batching two orders per courier, solved exactly with an ILP (OR-Tools CP-SAT) for small ticks and with a greedy + local-search heuristic for large ticks;
3. reports a lower bound (LP relaxation or matching bound) so the optimality gap is always known.

**Acceptance criteria**
- For ticks with ≤ 12 orders, the ILP result equals a brute-force optimum on 200 random instances.
- With 500 open orders and 150 couriers per tick, the heuristic decides in under 1 s (p95) on a stated machine.
- The gap between heuristic and lower bound is measured on at least 50 instances and reported as a distribution, with the worst case explained.
- Runs are reproducible from a seed; metrics reported: mean and p90 delivery time, courier idle time, orders per courier-hour.
- The write-up contains a short NP-hardness argument for the batched version (reduction sketch from a known NP-hard problem) and explains which constraints you relaxed.

**Stretch goals.** Rolling re-optimisation when orders get delayed; a fairness constraint (cap on orders per courier per hour) and its cost in delivery time; a map visualisation of one evening.

**What it proves to an employer.** You can recognise an NP-hard business problem, ship an exact method where it is affordable and a fast heuristic where it is not, and quantify the trade-off honestly. Marketplace, logistics and operations-research teams hire for exactly this.

## Feeds into

- [CS211 Database Systems Internals](../../semester_4/CS211_database_systems_internals/README.md): B+tree analysis, hash and sort-merge joins, and dynamic-programming join ordering in query optimisers.
- [CS216 Programming Languages, Compilers and Interpreters](../../semester_4/CS216_programming_languages_compilers_and_interpreters/README.md): parsing algorithms, graph colouring for register allocation, dataflow on control-flow graphs.
- [CAR301 Career Lab I](../../../05_shared_years_3_to_5/CAR301_career_lab_i_dsa_mastery_portfolio_and_open/README.md) and [06_career_and_market_readiness](../../../06_career_and_market_readiness/): timed DSA practice and interview loops build directly on Chapter 11.
- [CSG301 Advanced Algorithms](../../../03_majors/computer_science_general/year_3/CSG301_advanced_algorithms/README.md): LP duality, randomised and online algorithms extend Chapters 8 and 10.
- [SWE305 Concurrency and Performance Engineering](../../../03_majors/software_engineering/year_3/SWE305_concurrency_and_performance_engineering/README.md): Lesson 11.4's "theory meets hardware" becomes a full course on measured performance.
