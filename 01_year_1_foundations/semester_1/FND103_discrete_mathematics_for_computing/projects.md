# FND103 · Labs and projects

The rule in every lab: a claim is checked twice, once by proof and once by code on small cases. When they disagree, find out which one is wrong before moving on.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Truth tables and Z3 | Decide equivalence and satisfiability two ways | `truth_table()` in Python; a puzzle solved in Z3; 5 equivalences verified both ways | 3 h |
| 2 · Specifications as code | Turn English into quantified statements | 10 specs written in logic and as `all`/`any` checks, with a test world where each is false | 3 h |
| 3 · Natural Number Game | First machine-checked proofs | Completion screenshots for worlds 1–3; one proof explained in plain English | 4 h |
| 4 · Sets and joins | Sets as the basis of relational data | Power set, Cartesian product and a join written with set comprehensions; proof that \|P(S)\| = 2ⁿ | 3 h |
| 5 · Relations and topological order | Properties of relations; DAGs | Property checker for relations; topological order of `catalog.json` from this repository | 4 h |
| 6 · Invariants | Prove and test code correctness | Loop invariant for binary search, written as a proof and as `assert` statements run 10,000 times | 3 h |
| 7 · Counting two ways | Formula vs brute force | 8 counting problems, each with a formula, a proof sketch and a brute-force program that agrees | 4 h |
| 8 · Probability by simulation | Exact answers vs Monte Carlo | Birthday, Bayes and expected-collision problems: exact value, simulation, and error vs sample size | 3 h |
| 9 · Graphs | Model and prove | Metro-map model in NetworkX; BFS hop counts; greedy exam-timetable colouring with a lower-bound argument | 4 h |
| 10 · AI proof audit | Find flaws in convincing proofs | 5 AI-generated proofs graded with a rubric: the faulty line, why it fails, a corrected proof or counterexample | 3 h |

## Projects

### P1 · `logicheck`: propositional logic checker (L1, ~6 hours)

**Real-world inspiration.** Hardware verification and program verification reduce questions to satisfiability. Microsoft's open-source Z3 solver is used for this, and AWS describes applying automated reasoning to identity, networking and storage policies.

**What to build.** A Python tool that parses formulas such as `(p -> q) & ~q -> ~p`, prints the truth table, decides tautology, contradiction or satisfiable, decides whether two formulas are equivalent, and prints a counterexample assignment when they are not.

**Acceptance criteria**
- A hand-written recursive-descent parser handles `~ & | -> <->` with correct precedence and parentheses; malformed input gets an error message naming the position.
- 25 standard equivalence laws (De Morgan, distribution, contrapositive, absorption…) verified as tautologies by your tool.
- Results agree with Z3 on 200 randomly generated formula pairs (a test runs both).
- Handles formulas with up to 12 variables in under 2 seconds.
- ≥ 30 `pytest` tests.

**Stretch goals.** Convert formulas to conjunctive normal form; output DIMACS CNF and solve it with an external SAT solver; minimise a formula with Karnaugh-map style grouping for up to 4 variables.

**What it proves to an employer.** You can build a parser, reason about logic precisely, and cross-check your work against an industrial tool.

### P2 · `pathplan`: prerequisite planner for this university (L2, ~15 hours)

**Real-world inspiration.** Build systems (Make, Bazel), package managers and university registration all solve the same problem: order tasks so every dependency comes first, detect impossible cycles, and use limited capacity well.

**What to build.** A tool that reads this repository's `catalog.json` and:
1. Detects cycles and prints the exact cycle if one exists (test by injecting one).
2. Produces a valid semester-by-semester plan with at most *k* courses per semester for a chosen major.
3. Finds the longest prerequisite chain (the minimum number of semesters if capacity were unlimited).
4. Counts the valid orderings of small sub-graphs, by brute force and by dynamic programming over subsets, and checks they agree.

**Acceptance criteria**
- Runs on the real catalog; a separate checker verifies that every produced plan respects all prerequisites and the capacity limit.
- An injected cycle is detected and printed in order.
- README contains two proofs written by you: (a) Kahn's algorithm outputs every vertex of a DAG in a valid order; (b) with unlimited capacity, the minimum number of semesters equals the number of vertices on the longest path.
- ≥ 40 tests, including hand-made DAGs whose answers you computed on paper.

**Stretch goals.** Minimise the number of semesters under capacity *k* for small graphs by search, and show an example where the greedy plan is not optimal; export the graph to Mermaid for the README.

**What it proves to an employer.** You can model a real system as a graph, prove your algorithm correct, and verify output with an independent checker.

### P3 · `toycrypt`: number theory and cryptography notebook (L3, portfolio-grade, ~30 hours)

**Real-world inspiration.** TLS 1.3 (RFC 8446), RSA (RFC 8017), Aadhaar's Verhoeff check digit and the NIST post-quantum transition (FIPS 203–205, 2024) all rest on the algebra in Chapter 11. Security teams value engineers who understand why textbook constructions are unsafe and who reach for vetted libraries.

**What to build.** A documented Python package plus Jupyter notebook, for education only:
- From scratch: extended Euclid, modular inverse, square-and-multiply exponentiation, Miller–Rabin primality testing, the Chinese remainder theorem, toy RSA (key generation, encryption, decryption, signing) and Diffie–Hellman over a small prime field.
- A "why textbook RSA is broken" section, using toy key sizes only: determinism (equal messages give equal ciphertexts), malleability (multiplying ciphertexts), and factoring small moduli; and why real systems use padding schemes from RFC 8017 and libraries such as [pyca/cryptography](https://cryptography.io/en/latest/).
- A birthday experiment: truncate SHA-256 (`hashlib`) to 16, 20 and 24 bits and measure how many random inputs it takes to find a collision.
- Written proofs: termination and correctness of Euclid's algorithm, and correctness of RSA decryption via Euler's theorem (in Lean as a stretch).

**Acceptance criteria**
- Miller–Rabin agrees with `sympy.isprime` on 10⁵ random integers below 2⁶⁴.
- RSA round trip succeeds for 1,000 random messages per key, for 5 keys; CRT decryption is measured against plain decryption, and the speed-up is reported and explained.
- Collision counts are within 10% of the birthday-bound prediction averaged over 50 trials per size.
- Both written proofs pass peer review with every step justified.
- The README begins with a clear warning that the code is for learning and must never protect real data.
- ≥ 60 tests; all functions have docstrings stating preconditions.

**Stretch goals.** Formalise Euclid's correctness in Lean; implement the Verhoeff check digit from its group table and prove it detects all adjacent transpositions by exhaustive check; read the FIPS 203 overview and write one page on how lattice problems differ from factoring.

**What it proves to an employer.** You can turn mathematics into tested code, explain why security needs more than correct maths, and write proofs others can check: a strong signal for security, fintech and research roles.

## Feeds into

- [FND112 Data Structures and Algorithms I](../../semester_2/FND112_data_structures_and_algorithms_i/README.md): induction, recurrences and graphs become algorithm analysis.
- [FND116 Probability and Statistics I](../../semester_2/FND116_probability_and_statistics_i/README.md) and [FND113 Linear Algebra and Calculus](../../semester_2/FND113_linear_algebra_and_calculus_for_computing/README.md).
- [CS201 Algorithms and Complexity](../../../02_year_2_core_computer_science/semester_3/CS201_algorithms_and_complexity/README.md) and [CS213 Security Foundations](../../../02_year_2_core_computer_science/semester_4/CS213_security_foundations/README.md) (P3 is the bridge).
- The [Computer Science (Theory, Systems and Research) major](../../../03_majors/computer_science_general/README.md) and the [FinTech Systems Engineering overlap](../../../04_overlaps/OV10_fintech_systems_engineering/README.md).
