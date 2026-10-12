# FND112 · Data Structures and Algorithms I

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 1 · 2 | 4 (≈ 120 hours) | L1 → L2 | [FND101](../../semester_1/FND101_programming_i_computational_thinking_with_python/README.md), [FND103](../../semester_1/FND103_discrete_mathematics_for_computing/README.md) | [CS201](../../../02_year_2_core_computer_science/semester_3/CS201_algorithms_and_complexity/README.md), later [CAR301](../../../05_shared_years_3_to_5/CAR301_career_lab_i_dsa_mastery_portfolio_and_open/README.md) |

## Why this course matters now

The data structure you choose decides whether a request costs microseconds or seconds: hash maps behind every cache, queues behind every job pipeline, heaps behind every scheduler, graphs behind every route planner and build tool. AI can now solve contest problems at an elite level: Google DeepMind's Gemini reached gold-medal level at the 2025 ICPC World Finals, solving 10 of 12 problems. So recalling a known solution is no longer what sets you apart. Hiring is shifting too: Canva replaced its computer-science fundamentals screen with an AI-assisted coding interview, and Meta was reported to be allowing AI in coding tests. What still needs a skilled human is choosing the right structure for a messy real problem, proving that a solution is correct and fast enough, and catching the solution that is almost right. This course trains those skills in Python and Java, from a blank file.

## Learning outcomes

By the end you can:

1. Analyse the time and space of iterative and recursive code with O, Θ and Ω, including amortised cost, and confirm each prediction with a timing experiment on a log-log plot.
2. Implement from scratch, in Python and Java, dynamic arrays, linked lists, stacks, deques, ring buffers, hash maps (chaining and open addressing), BSTs, binary heaps, tries and adjacency-list graphs, each with tests against the built-in equivalent.
3. Argue correctness with loop invariants and induction for binary search, partitioning, two-pointer and sliding-window algorithms.
4. Implement and compare six sorting algorithms, explain stability and the Ω(n log n) comparison lower bound, and describe what Python's and Java's built-in sorts actually do.
5. Solve problems with recursion and backtracking, convert recursion to iteration with an explicit stack, and add memoisation.
6. Use BFS, DFS and topological sort on grids and graphs to find components, unweighted shortest paths and valid orderings.
7. Recognise the core patterns in an unseen problem and present a solution in interview form: clarify, examples, brute force, optimise, code, test, analyse.
8. Check any solution, yours or an AI's, with a brute-force oracle, random stress tests and property-based tests.

## Chapters and lessons

### Chapter 1 · Cost models and Big-O (week 1)

| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Counting steps | The RAM model, primitive operations, best, worst and average case | Count operations in five snippets, then check by instrumenting the code |
| 1.2 O, Θ, Ω | Formal definitions with constants *c* and *n₀*; the growth ladder 1 < log n < n < n log n < n² < 2ⁿ < n! | Rank 12 functions; prove two bounds formally using [FND103](../../semester_1/FND103_discrete_mathematics_for_computing/README.md) |
| 1.3 Measuring | Python `timeit`, Java JMH (warm-up, dead-code elimination), why the slope of a log-log plot is the exponent | Time `list.insert(0, x)`, `list.append` and `deque.appendleft` for n = 10³…10⁶ and read off the slopes |
| 1.4 Hidden costs | Slicing copies (`a[1:]` is O(k)), string `+=` in loops, `x in list` vs `x in set`, recursion stack space | Find the hidden O(n²) in four short functions and fix it |
| 1.5 Amortised analysis | Aggregate method; why doubling gives O(1) appends and adding a constant gives O(n) | Plot `sys.getsizeof` of a growing Python list and explain the steps |

**Check your understanding:** (1) An O(n log n) algorithm runs slower than an O(n²) one on your data. How, and when does that stop being true? (2) Why does a log-log plot reveal an exponent? (3) A colleague says a loop is O(n) but it calls `list.pop(0)`. What is its real cost?

### Chapter 2 · Recursion and backtracking (week 2)

| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 The call stack | Base cases, frames, Python's default recursion limit of 1,000, Java `StackOverflowError` | Trace three recursive functions on paper, then hit the limit on purpose |
| 2.2 Recurrences | Correctness by induction; T(n) = T(n−1) + O(1) and T(n) = 2T(n/2) + O(n); recursion trees | Solve four recurrences with recursion trees and confirm by timing |
| 2.3 Divide and conquer | Recursive binary search, fast exponentiation in O(log n), a first look at merge sort | Implement `power_mod(x, n, m)` and test it against Python's `pow(x, n, m)` |
| 2.4 Memoisation | Overlapping subproblems, `functools.cache`, a `HashMap` memo in Java (dynamic programming continues in CS201) | Climbing stairs and grid paths: time before and after memoising |
| 2.5 Backtracking | Choose, explore, unchoose; pruning; subsets, permutations, N-Queens | Generate subsets and permutations; count N-Queens solutions for n ≤ 10 |

**Check your understanding:** (1) Why is naive recursive Fibonacci exponential, and what exactly does memoisation remove? (2) When must you convert a recursive DFS to an iterative one? (3) Does pruning improve the worst case or the typical case?

### Chapter 3 · Arrays, strings and prefix sums (week 3)

| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Memory layout | Contiguous memory, index arithmetic, cache locality; Java `int[]` vs `ArrayList<Integer>` (boxing) vs a Python list of references | Time summing 10⁷ integers in four representations, including a NumPy array |
| 3.2 A dynamic array from scratch | Capacity, growth factor, shrinking policy, amortised O(1) append | Build one in Python and Java; differential-test it against the built-in over 10⁵ random operations |
| 3.3 Prefix sums | O(1) range sums after O(n) preprocessing; difference arrays for range updates | Range Sum Query; Product of Array Except Self |
| 3.4 Strings | Immutability, `StringBuilder` and `"".join`, character counts, Unicode code points | Valid Anagram; measure `+=` vs `join` for 10⁵ pieces |
| 3.5 Grids | Row-major order, traversal orders, in-place rotation | Rotate Image; Spiral Matrix |

**Check your understanding:** (1) Why is summing an `int[]` faster than an `ArrayList<Integer>` with the same Big-O? (2) What breaks if a dynamic array shrinks to half as soon as it is half empty? (3) How do prefix sums turn an O(nq) workload into O(n + q)?

### Chapter 4 · Two pointers and sliding window (week 4)

| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Opposite-end pointers | Sorted input; the invariant that justifies discarding an element; why the loop is O(n) | Two Sum II; Container With Most Water |
| 4.2 Same-direction pointers | In-place compaction, partitioning, Dijkstra's Dutch national flag | Move Zeroes; Sort Colors |
| 4.3 Fixed windows | Keep an aggregate updated in O(1) per step | Maximum average subarray; Find All Anagrams in a String |
| 4.4 Variable windows | Expand, then shrink until the window is valid again; counts in a hash map | Longest Substring Without Repeating Characters; Minimum Window Substring |
| 4.5 Sort, then scan | Sorting first to enable pointers; skipping duplicates correctly | 3Sum, stress-tested against an O(n³) brute force |

**Check your understanding:** (1) State the invariant that makes Container With Most Water correct. (2) Why does a variable window stay O(n) even though it has a nested loop? (3) When does sliding window fail (hint: negative numbers)?

### Chapter 5 · Linked lists, stacks, queues and the LRU cache (week 5)

| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Linked lists | Singly and doubly linked lists, sentinel nodes, O(1) splice given a node, the cost of no random access | Implement both in Java with an `Iterator`; reverse a list iteratively and recursively |
| 5.2 Pointer techniques | Fast/slow pointers, Floyd's cycle detection, merging sorted lists | Linked List Cycle II; Merge Two Sorted Lists |
| 5.3 Stacks | LIFO, array-backed stacks, bracket matching, expression evaluation, monotonic stacks | Valid Parentheses; Evaluate Reverse Polish Notation; Daily Temperatures |
| 5.4 Queues and deques | FIFO, ring buffers, `collections.deque`, `ArrayDeque`; job queues in production (Zerodha's PDF pipeline) | A fixed-capacity ring buffer; Sliding Window Maximum with a monotonic deque |
| 5.5 LRU cache | Hash map plus doubly linked list; `LinkedHashMap` with access order; `OrderedDict` | LRU Cache with O(1) operations, differential-tested against `OrderedDict` |

**Check your understanding:** (1) Why does an LRU cache need both a hash map and a linked list? (2) What does a sentinel node remove from your code? (3) Why is a Python list a poor queue?

### Chapter 6 · Hash tables (week 6)

| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Hashing and chaining | Hash functions, buckets, collisions, load factor, resizing | Implement a separate-chaining map with `get`, `put`, `remove`, resize |
| 6.2 Open addressing | Linear probing, clustering, tombstones | Implement linear probing; plot average probe length for load factors 0.1–0.95 |
| 6.3 Real implementations | Python `dict` (open addressing, insertion order guaranteed since 3.7); Java `HashMap` (chaining; a bucket turns into a red-black tree once it holds 8 entries and the table has at least 64 buckets); the `equals`/`hashCode` contract | Read the treeification part of OpenJDK's `HashMap.java` and explain it in five sentences |
| 6.4 Adversarial input | Why a predictable hash lets attackers force worst-case behaviour; randomised SipHash in Python (PEP 456) as the defence | Show worst-case behaviour with a deliberately bad hash function of your own, then fix it |
| 6.5 Hashing patterns | Counting, deduplication, complements, grouping by a canonical key | Two Sum; Group Anagrams; Longest Consecutive Sequence; Top K Frequent Elements |

**Check your understanding:** (1) Why is lookup O(1) only "on average", and what is the worst case in Python and in Java? (2) Why must deletion in linear probing leave a tombstone? (3) What goes wrong if `hashCode` depends on a mutable field?

### Chapter 7 · Sorting and binary search (weeks 7–8)

| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Elementary sorts | Selection and insertion sort; why insertion sort is fast on nearly sorted data | Count comparisons on sorted, reversed and random inputs |
| 7.2 Merge sort and quicksort | Stability, O(n) extra space; Lomuto vs Hoare partition, random pivots, the O(n²) worst case, quickselect | Merge sort with inversion counting; Kth Largest Element with quickselect |
| 7.3 Limits and non-comparison sorts | The decision-tree Ω(n log n) bound; counting sort and radix sort | Radix-sort 10⁶ synthetic 10-digit phone numbers and compare with the built-in |
| 7.4 Sorts in the wild | Python's Timsort (runs, galloping, the powersort merge policy); Java's `Arrays.sort` (dual-pivot quicksort for primitives, a stable mergesort for objects); comparators and key functions | Sort records by three keys using stability; property-test your `Comparator` |
| 7.5 Binary search | The invariant, half-open intervals, `lower_bound`/`upper_bound`, `bisect` (with `key=`), Java's negative return value, `(lo + hi) >>> 1` | Find First and Last Position; Search in Rotated Sorted Array; test exhaustively on all arrays up to length 8 |
| 7.6 Search on the answer | Binary search over a monotone yes/no predicate | Koko Eating Bananas; Capacity to Ship Packages Within D Days |

**Check your understanding:** (1) Why can no comparison sort beat Ω(n log n), and why does radix sort not contradict this? (2) Why does Java use different algorithms for `int[]` and `Object[]`? (3) What property must a predicate have for "binary search on the answer" to work?

### Chapter 8 · Trees, BSTs and tries (week 9)

| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Traversals | Pre-, in-, post- and level-order; recursive and iterative versions | All four traversals both ways; Binary Tree Level Order Traversal |
| 8.2 Recursion on trees | Height, diameter, balance checks, returning more than one value | Diameter of Binary Tree; Balanced Binary Tree |
| 8.3 Binary search trees | Search, insert, delete (three cases); in-order is sorted; degenerate trees and why `TreeMap` uses a red-black tree | Implement a BST with delete; Validate Binary Search Tree; Lowest Common Ancestor |
| 8.4 Tries | Insert, search, prefix queries; memory cost against a hash set | Autocomplete over station names from the Indian Railways timetable on data.gov.in |
| 8.5 Trees everywhere | Serialising trees; JSON and the HTML DOM as trees | Serialize and Deserialize Binary Tree |

**Check your understanding:** (1) Why can a BST degrade to O(n), and which insertion order causes it? (2) When is a trie better than a sorted list with binary search? (3) Why is checking only `left < node < right` at each node not enough to validate a BST?

### Chapter 9 · Heaps and priority queues (week 10)

| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Binary heaps | A complete tree stored in an array, index arithmetic, sift-up and sift-down | Implement a min-heap in both languages and differential-test it against `heapq` |
| 9.2 Heapify and heapsort | Why bottom-up heapify is O(n), not O(n log n) | Prove it, then measure heapify against n pushes |
| 9.3 Top-k and merging | A size-k heap for the k largest in O(n log k); k-way merge | Kth Largest Element in a Stream; Merge k Sorted Lists |
| 9.4 Two heaps and scheduling | Running median; priority scheduling; `heapq`'s max-heap functions (new in Python 3.14); `PriorityQueue` with a comparator | Find Median from Data Stream; an illustrative ride-dispatch simulation |

**Check your understanding:** (1) Why use a min-heap to find the k largest items? (2) Why is a heap not a good structure for searching for an arbitrary element? (3) When would you choose sorting over a heap for top-k?

### Chapter 10 · Graphs (weeks 11–12)

| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Representations | Adjacency lists vs matrices vs edge lists; directed, undirected and weighted graphs; space costs | Build a station graph from the railway timetable dataset (consecutive stops are edges) |
| 10.2 Breadth-first search | Layers, unweighted shortest paths, multi-source BFS, grids as graphs | Number of Islands; Rotting Oranges; fewest stops between two stations |
| 10.3 Depth-first search | Recursive and iterative DFS, connected components, cycle detection with three colours | Course Schedule; count the connected components of the station graph |
| 10.4 Topological sort | Kahn's algorithm and DFS post-order; how build tools and package managers order work | Order the build of a module dependency graph and report any cycle found |
| 10.5 A look ahead | Weighted shortest paths (Dijkstra) and union-find, taught in full in CS201 | Run a provided Dijkstra on travel times and explain why BFS gives a different answer |

**Check your understanding:** (1) Why does BFS find shortest paths only when all edges have equal weight? (2) What does a back edge in DFS tell you? (3) Why does Kahn's algorithm detect a cycle for free?

### Chapter 11 · Patterns and interview craft (weeks 13–14)

| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 The pattern map | Signals to technique: sorted input → pointers or binary search; "k largest" → heap; contiguous subarray → window or prefix sums; "all combinations" → backtracking; "fewest steps" → BFS; dependencies → topological sort | Classify 40 unseen problems by pattern before solving any |
| 11.2 The interview method | Clarify, examples, brute force, optimise, code, test, analyse; thinking aloud | Four recorded mock interviews with peers, scored on a shared rubric |
| 11.3 Testing your own solution | Edge cases (empty, single, duplicates, negatives, overflow); a random generator plus a brute-force oracle; Hypothesis and jqwik | A reusable stress-test harness in Python and Java |
| 11.4 Interviews with AI in the room | AI-assisted rounds; explaining, testing and rejecting AI-written code | Solve three problems with an assistant allowed, then grade its code with your harness |

**Check your understanding:** (1) Which signal in a problem statement points you to a heap, and which to a sliding window? (2) Why should you state the brute force before optimising? (3) Your solution passes 50 hand-written tests. What does a stress test add?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Growth rates | Log-log plots with slopes |
| 2 | 2 | Lab 2 · Recursion and backtracking | Recursion-tree write-up |
| 3 | 3 | Lab 3 · Dynamic array | Differential tests in both languages |
| 4 | 4 | Lab 4 · Pointers and windows | Six solutions with stated invariants; P1 starts |
| 5 | 5 | Lab 5 · Lists, stacks, LRU | LRU cache |
| 6 | 6 | Lab 6 · Hash map from scratch | Probe-length plot; P1 due |
| 7–8 | 7 | Lab 7 · Sorting bake-off; Lab 8 · Binary search | Benchmark report; P2 starts |
| 9 | 8 | Lab 9 · Trees and tries | Trie autocomplete |
| 10 | 9 | Heap exercises | P2 due |
| 11–12 | 10 | Lab 10 · Graph search | Station graph BFS; P3 starts |
| 13–14 | 11 | Mock interviews | Stress-test harness, interview scores |
| 15 | Review and exam | Practical and whiteboard exam (AI off) | P3 due |

Every week also has a timed set of three problems (25 minutes each), done without AI.

## Working with AI in this course

- **Use AI for:** a second explanation of an algorithm after you have traced it yourself; random test generators and edge-case lists; a step-by-step trace to compare against yours; a mock interviewer that asks follow-up questions; reviewing a complexity argument you wrote first.
- **Do without AI (drills):** implement every structure in this course from a blank file, in both languages, with completion turned off; the weekly timed problem sets; complexity analysis written down before running any code; tracing by hand on paper.
- **Verify AI output by:** stress-testing against a brute-force oracle on 10,000 random small inputs; property-based tests (sorted output is a permutation of the input and non-decreasing); timing at several sizes to check the claimed complexity on a log-log plot; running the Java version with values near `Integer.MAX_VALUE`.
- **Where AI still fails here:** assistants solve standard problems well, so the failures that matter are subtle. Check and log, from your own stress tests: complexity claims contradicted by measurement (an "O(n)" loop that calls `list.pop(0)` or slices); solutions to the famous version of a problem when your constraints differ; integer overflow in Java; off-by-one boundaries in binary search. The Stack Overflow 2025 survey found that 66% of developers name "almost right" AI solutions as their top frustration, and this course trains you to catch them.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (10) | 20% |
| Weekly timed problem sets, AI off | 10% |
| Projects P1 · P2 · P3 | 10% · 10% · 20% |
| Final exam, AI off: 2-hour implementation plus 1-hour whiteboard | 30% |

**Mastery gate.** You pass when you can, with AI off: implement an open-addressing hash map, a binary heap and BFS on a grid from a blank file, in both Python and Java, with tests, in 90 minutes total; and solve two unseen medium problems in 45 minutes each while explaining the pattern, the invariant, the complexity and the edge cases aloud, then show a passing stress test.

## Industry reality

These structures are the inside of production systems. Python's `dict` and Java's `HashMap` sit under almost every service. Zerodha describes generating over 1.5 million PDF contract notes in about 25 minutes, down from 7–8 hours, with chained job queues on Redis. PhonePe describes moving about 100 billion events a day through Kafka, a distributed log that behaves like a very large queue. Build tools and package managers depend on topological order, and route planners on graph search. Interviews for most software roles still test this material, while the format is changing: some companies now allow, or require, AI during coding rounds.

**Interview questions from this course**

1. *"Design an LRU cache with O(1) `get` and `put`."* Hash map plus doubly linked list with sentinels; eviction from the tail; complexity of each operation; mention `LinkedHashMap`; note that it is not thread-safe as written; tests for capacity 1 and repeated keys.
2. *"Why is hash-map lookup O(1) only on average?"* Load factor and amortised resizing; collisions; worst case O(n) for chaining, O(log n) per bucket after Java's treeification; adversarial inputs and randomised hashing; why `hashCode` quality matters.
3. *"Return the k most frequent elements."* Count with a hash map, then compare a size-k heap (O(n log k)), bucket sort by frequency (O(n)) and a full sort (O(n log n)); ties; what changes for a stream.
4. *"Longest substring without repeating characters."* Brute force first; a sliding window with a last-seen map and the invariant "the window has no duplicates"; O(n) time and O(alphabet) space; empty string and Unicode edge cases.
5. *"Can all these courses be finished, given their prerequisites?"* Model as a directed graph; cycle detection with DFS colours or Kahn's algorithm; O(V + E); return a valid order or the cycle itself.

## Resources (free first)

- **Courses:** [MIT 6.006 Introduction to Algorithms (Spring 2020)](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/); [Berkeley CS61B Data Structures](https://fa26.datastructur.es/) (Java); [NPTEL Programming, Data Structures and Algorithms using Python](https://nptel.ac.in/courses/106106145) (Madhavan Mukund); [Stanford CS106B](https://web.stanford.edu/class/cs106b/) (C++, strong problem sets).
- **Free books:** [Open Data Structures](https://opendatastructures.org/) (Morin, with a Java edition); [Algorithms](https://jeffe.cs.illinois.edu/teaching/algorithms/) (Erickson); [Algorithms, 4th ed. booksite](https://algs4.cs.princeton.edu/home/) (Sedgewick and Wayne, Java code).
- **Documentation:** [Python TimeComplexity wiki](https://wiki.python.org/moin/TimeComplexity); [`heapq`](https://docs.python.org/3/library/heapq.html), [`bisect`](https://docs.python.org/3/library/bisect.html), [`collections`](https://docs.python.org/3/library/collections.html); [Java `Arrays`](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Arrays.html) and [`HashMap`](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/HashMap.html); [JMH](https://github.com/openjdk/jmh); [Hypothesis](https://hypothesis.readthedocs.io/en/latest/); [jqwik](https://jqwik.net/).
- **Visualisation and practice:** [VisuAlgo](https://visualgo.net/en); [LeetCode](https://leetcode.com/problemset/) (every problem named above is on its free tier); [Tech Interview Handbook and Grind 75](https://www.techinterviewhandbook.org/grind75/); [NeetCode solutions repository](https://github.com/neetcode-gh/leetcode) (Python and Java); [CP-Algorithms](https://cp-algorithms.com/).
- **Paid, optional:** *Introduction to Algorithms* (CLRS, 4th ed.); *The Algorithm Design Manual* (Skiena). The free books above cover this course.

## Sources

All checked 12 Oct 2026.

- Google DeepMind, Gemini at the ICPC World Finals (17 Sep 2025) — https://deepmind.google/discover/blog/gemini-achieves-gold-level-performance-at-the-international-collegiate-programming-contest-world-finals/
- Canva Engineering, "Yes, You Can Use AI in Our Interviews" (11 Jun 2025) — https://canva.dev/blog/engineering/yes-you-can-use-ai-in-our-interviews
- 404 Media, "Meta Is Going to Let Job Candidates Use AI During Coding Tests" (29 Jul 2025) — https://www.404media.co/meta-is-going-to-let-job-candidates-use-ai-during-coding-tests/
- Zerodha Tech, "1.5+ million PDFs in 25 minutes" (14 Feb 2024) — https://zerodha.tech/blog/1-5-million-pdfs-in-25-minutes/
- PhonePe Tech, "The Kafka Edge: Managing 100 Billion Daily Events at PhonePe" (31 Oct 2023) — https://tech.phonepe.com/the-kafka-edge-managing-100-billion-daily-events-at-phonepe/
- Python dict insertion order (Python docs, built-in types) — https://docs.python.org/3/library/stdtypes.html · `heapq` max-heap functions added in 3.14 — https://docs.python.org/3/library/heapq.html · PEP 456 (SipHash) — https://peps.python.org/pep-0456/ · CPython `listsort.txt` (Timsort, powersort) — https://github.com/python/cpython/blob/main/Objects/listsort.txt
- OpenJDK `HashMap.java` (treeification thresholds) — https://github.com/openjdk/jdk/blob/master/src/java.base/share/classes/java/util/HashMap.java · Java 25 `Arrays.sort` algorithms — https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/Arrays.html
- Indian Railways timetable dataset, Open Government Data Platform India — https://data.gov.in/resource/indian-railways-time-table-trains-available-reservation-01112017
- Stack Overflow Developer Survey 2025, AI section — https://survey.stackoverflow.co/2025/ai
- ACM/IEEE-CS/AAAI CS2023, Algorithmic Foundations knowledge area — https://csed.acm.org/algorithms-and-complexity/

_Last reviewed: 2026-10_
