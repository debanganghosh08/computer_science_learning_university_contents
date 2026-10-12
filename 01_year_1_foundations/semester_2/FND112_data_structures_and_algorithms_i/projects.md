# FND112 · Labs and projects

Every lab is done in Python and Java unless stated otherwise. Each solution ships with (a) a written complexity claim, (b) unit tests, and (c) a stress test against a brute-force oracle on random inputs with a fixed seed. A submission without the stress test is incomplete.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Growth rates | Time six operations (`append`, `insert(0)`, `in` on list vs set, `deque.appendleft`, string `+=`, `sorted`) for n = 10³…10⁶ with `timeit` and JMH | Log-log plots with fitted slopes, and the predicted vs measured exponent for each | 4 h |
| 2 · Recursion and backtracking | Recursion trees for four recurrences; memoised grid paths; subsets, permutations, N-Queens | Code, tests, a recursion-tree write-up, the N-Queens counts for n ≤ 10 | 4 h |
| 3 · Dynamic array | Build a dynamic array; compare growth factors 1.5, 2 and "+100" | Code, differential tests over 10⁵ random operations, a plot of time per append | 4 h |
| 4 · Pointers and windows | Six problems from Chapter 4, each with its invariant written above the code | Solutions, invariants, stress-test logs | 4 h |
| 5 · Lists, stacks, LRU | Doubly linked list with sentinels, ring buffer, LRU cache | Code and differential tests against `OrderedDict` and `LinkedHashMap` | 5 h |
| 6 · Hash map from scratch | Chaining and linear probing with tombstones and resize; a deliberately bad hash function | Code, a probe-length vs load-factor plot, a one-page explanation of the worst case and its defence | 5 h |
| 7 · Sorting bake-off | Insertion, merge, quick, heap, counting and radix sort on random, sorted, reversed and few-unique inputs | A benchmark report with comparisons and time, and stability tests | 5 h |
| 8 · Binary search | Three binary-search variants, tested exhaustively on every sorted array up to length 8; two search-on-the-answer problems | Code and the exhaustive test log | 3 h |
| 9 · Trees and tries | BST with delete and all traversals; a trie over railway station names | Code, tests, a timing comparison with sorted list plus `bisect` | 5 h |
| 10 · Graph search | Build the station graph from the timetable dataset; BFS for fewest stops; components; topological sort of a build graph | Code, results on 20 station pairs, tests | 5 h |

## Projects

### P1 · Your own collections library (L1, ~6 hours)

**Real-world inspiration.** Java's `java.util` and Python's built-in types are ordinary code you can read and rewrite. [Open Data Structures](https://opendatastructures.org/) shows each core structure in a few hundred lines.

**What to build.** In Python and Java, with the same API in both: `DynamicArray`, `RingDeque`, `OpenAddressingMap` (tombstones, resize at a load factor you choose) and `MinHeap`.

**Acceptance criteria**
- Differential tests: 10⁵ random operations per structure give exactly the same results as the built-in (`list`, `deque`, `dict`, `heapq`; `ArrayList`, `ArrayDeque`, `HashMap`, `PriorityQueue`), with fixed seeds.
- Append time per operation stays within 2× from n = 10³ to n = 10⁶, shown on a log-log plot.
- The hash map's average probe length is at most 2 at load factor 0.5 on random keys, and the README reports what happens at 0.9.
- No structure uses the built-in it replaces, and each is at most 150 lines per language.

**Stretch goals.** Robin Hood hashing; generic Java versions whose iterators fail fast on concurrent modification.

**What it proves to an employer.** You know what the built-ins do and what they cost, so you can predict performance instead of guessing.

### P2 · Station search: autocomplete with ranking (L2, ~15 hours)

**Real-world inspiration.** Train-booking and maps apps suggest stations as you type and rank common ones first. The data comes from the [Indian Railways timetable dataset](https://data.gov.in/resource/indian-railways-time-table-trains-available-reservation-01112017) on India's Open Government Data platform.

**What to build.** A library and CLI for prefix search over station names and codes. Matching ignores case and extra spaces, and the top k results are ranked by a popularity score you compute, such as the number of trains stopping. Build three implementations: a linear scan, a sorted list with `bisect`, and a trie that caches the top k at each node.

**Acceptance criteria**
- All three implementations return identical results for 1,000 random prefixes.
- A benchmark table gives p50 and p95 query latency on the real station list and on a synthetic list of 10⁵ names, plus build time and memory (`tracemalloc` in Python), and states your hardware.
- The trie answers prefix queries on 10⁵ names with a p95 under 1 ms in Java.
- Top-k uses a heap of size k, and a test confirms it equals the first k of a full sort.
- A one-page analysis gives the build and query complexity of each implementation and says when you would choose each one.

**Stretch goals.** Typo tolerance (edit distance 1); JMH benchmarks for the Java version; a small web front end in [FND114](../FND114_web_foundations_http_html_css_and_javascript/README.md).

**What it proves to an employer.** You choose data structures by measurement and can present the trade-offs clearly, which is how real performance work is done.

### P3 · Railway route planner (L3, portfolio-grade, ~30 hours)

**Real-world inspiration.** Rail and metro journey planners answer "how do I get there with the fewest changes?" Public transit data is increasingly open, for example Delhi's [Open Transit Data portal](https://otd.delhi.gov.in/), which publishes static and real-time data, including DMRC static data, under its own terms. This project uses the national timetable dataset above.

**What to build.** A route planner in Python and Java with identical outputs. Stations are nodes, and each train contributes edges between its consecutive stops. It answers four queries:
1. Fewest stops between two stations (BFS).
2. Fewest train changes: a search over (station, train) states, where staying on a train costs 0 and changing costs 1, solved with a 0-1 BFS on a deque.
3. All stations reachable within k changes.
4. Stations that cannot reach a given hub.

**Acceptance criteria**
- The parser loads the full dataset, prints counts of stations, trains and edges, and writes a report of malformed rows instead of crashing.
- On a 50-station subgraph, fewest-changes answers match an exhaustive search for 200 random pairs.
- The Python and Java versions give identical answers on 200 fixture queries checked in CI.
- p95 latency for fewest-changes queries on the full dataset is under 2 seconds in Python, and the benchmark method and hardware are documented.
- The README includes a diagram of the graph model, the complexity of each query, and its limits: 2017 data, no departure times, no running days.
- An AI log records each algorithm or fix an assistant suggested, and whether your tests confirmed or refuted it.

**Stretch goals.** Earliest arrival using departure times with Dijkstra (a preview of CS201); store the graph in SQLite and compare with a recursive CTE ([FND115](../FND115_databases_i_data_modeling_and_sql/README.md)); a web UI.

**What it proves to an employer.** You can model a messy real dataset as a graph, pick the right search for each question, verify it, and benchmark it. That is engineering judgement, not puzzle recall.

## Feeds into

- [CS201 Algorithms and Complexity](../../../02_year_2_core_computer_science/semester_3/CS201_algorithms_and_complexity/README.md): dynamic programming, greedy algorithms, Dijkstra, union-find and NP-hardness build on Chapters 2, 7 and 10.
- [CS211 Database Systems Internals](../../../02_year_2_core_computer_science/semester_4/CS211_database_systems_internals/README.md): B+ trees and hash indexes are the structures from Chapters 6 and 8, on disk.
- [CAR301 Career Lab I: DSA Mastery](../../../05_shared_years_3_to_5/CAR301_career_lab_i_dsa_mastery_portfolio_and_open/README.md): the stress-test harness and pattern map from Chapter 11 are reused for hiring preparation.
- [FND115 Databases I](../FND115_databases_i_data_modeling_and_sql/README.md): the same timetable data returns as a relational schema.
