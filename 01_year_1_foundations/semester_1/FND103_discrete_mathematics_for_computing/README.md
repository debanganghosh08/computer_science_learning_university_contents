# FND103 · Discrete Mathematics for Computing

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 1 · 1 | 4 (≈ 120 hours) | L0 → L2 | none (school algebra) | [FND112](../../semester_2/FND112_data_structures_and_algorithms_i/README.md), [FND113](../../semester_2/FND113_linear_algebra_and_calculus_for_computing/README.md), [FND116](../../semester_2/FND116_probability_and_statistics_i/README.md) |

## Why this course matters now

Discrete maths is the language of correctness: loop invariants prove code right, graphs model road networks and dependency trees, counting sizes up brute-force search, and modular arithmetic underlies the key exchange in every TLS 1.3 connection (RFC 8446) and the post-quantum standards NIST finalised in August 2024 (FIPS 203, 204, 205). AI has changed what is rare. In July 2025 an advanced Gemini Deep Think model scored 35 of 42 at the International Mathematical Olympiad, graded by IMO coordinators, so producing a plausible proof is no longer scarce. What stays valuable is stating the right claim from a fuzzy requirement, spotting the gap in a convincing argument, and checking with code or a proof assistant such as Lean. Every chapter pairs proofs with Python so you can test a claim on small cases before you trust it.

## Learning outcomes

By the end you can:

1. Translate English requirements into propositional and predicate logic, and back.
2. Decide equivalence and satisfiability of formulas with truth tables in Python and with the Z3 solver.
3. Write direct, contrapositive, contradiction, case and induction proofs that a peer can check line by line, and find the flaw in a faulty proof.
4. Reason about sets, functions and relations, including equivalence relations, partial orders and topological order.
5. Prove simple programs correct with loop invariants and structural induction.
6. Solve and estimate recurrences, and connect them to the running time of recursive code.
7. Count with the product rule, permutations, combinations, inclusion–exclusion and pigeonhole, and confirm counts by brute force.
8. Model problems as graphs and prove basic graph facts (handshake lemma, trees have n − 1 edges, bipartite iff no odd cycle).
9. Use gcd, extended Euclid, modular inverses and fast exponentiation to build and break toy RSA.
10. Check a small proof mechanically in Lean 4, and audit an AI-generated proof.

## Chapters and lessons

### Chapter 1 · Propositional logic (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Propositions | Statements, connectives ¬ ∧ ∨ → ↔, precedence, truth tables. | Write `truth_table(f, n)` with `itertools.product`; print tables for 5 formulas. |
| 1.2 Implication | Vacuous truth, converse, inverse, contrapositive; "only if" vs "if". | Rewrite 8 English rules as implications; mark which are equivalent. |
| 1.3 Equivalence laws | De Morgan, distribution, absorption, implication elimination; simplifying conditions in code. | Simplify three nested `if` conditions and prove equivalence by table. |
| 1.4 Satisfiability | SAT, tautology, contradiction; SAT solvers; the Z3 Python API. | Encode a 4×4 Sudoku or a seating puzzle as constraints in Z3; extract the solution. |

**Check your understanding:** (1) Why is "if the moon is cheese then 2 + 2 = 5" true? (2) A code review turns `if not (a and b)` into `if not a and not b`; is it equivalent? (3) Why does a truth table become impractical at 40 variables, and what does a SAT solver do instead?

### Chapter 2 · Predicates and quantifiers (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Predicates | Predicates as boolean functions, domains, free and bound variables. | Write Python predicates for "is prime", "is sorted", "is a palindrome". |
| 2.2 Quantifiers | ∀ and ∃; `all()` and `any()` as quantifiers over finite domains. | Encode 10 specifications ("every user has at most one active session") as `all`/`any` checks. |
| 2.3 Negation and order | Negating quantified statements; ∀x∃y vs ∃y∀x. | Negate 6 statements into plain English; give a world where swapping quantifiers changes truth. |
| 2.4 Specs from requirements | Ambiguity in natural language; writing a precise spec before code. | Find and resolve the ambiguity in three requirement sentences from a real API doc. |

**Check your understanding:** (1) What does `all([])` return and why is that the logically correct answer? (2) How do "every student has a mentor" and "some mentor teaches every student" differ? (3) What is the negation of "every request gets a response within 2 seconds"?

### Chapter 3 · Proof techniques (weeks 3–4)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Direct proof | Definitions as the starting point; even, odd and divisibility proofs. | Prove: the sum of two odd numbers is even; the square of an odd number is odd. |
| 3.2 Contrapositive and contradiction | When to use each; √2 is irrational; infinitely many primes (Euclid). | Prove: if n² is even then n is even, both ways. |
| 3.3 Cases and counterexamples | Proof by cases; one counterexample disproves a universal claim; searching for counterexamples in code. | Disprove "n² + n + 41 is always prime" by computer search. |
| 3.4 Writing proofs others can check | Structure, stating what is assumed and what is shown, avoiding "clearly". | Rewrite a classmate's proof so each line cites a definition or prior line. |
| 3.5 Machine-checked proof | Lean 4 basics through the Natural Number Game: goals, tactics (`rw`, `induction`). | Complete the first three worlds of the Natural Number Game. |

**Check your understanding:** (1) Why does checking a claim for n = 1…1,000,000 not prove it? (2) In a proof by contradiction, what exactly are you assuming? (3) What does Lean guarantee about a proof it accepts, and what can it not guarantee about your statement?

### Chapter 4 · Sets (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Sets and notation | Membership, subsets, set-builder notation, empty set, power set. | Implement `power_set(s)`; prove \|P(S)\| = 2ⁿ. |
| 4.2 Operations | Union, intersection, difference, complement, Cartesian product; Venn diagrams; set identities. | Prove a De Morgan law for sets by element-chasing; test it with Python sets. |
| 4.3 Sets in computing | Python `set`, relational algebra preview (a SQL join as a filtered Cartesian product, see [FND115](../../semester_2/FND115_databases_i_data_modeling_and_sql/README.md)). | Compute a join of two small tables using only set comprehensions. |
| 4.4 Infinity | Countable sets, Cantor's diagonal argument, why some problems have no program (halting problem preview). | Show the integers and the even numbers have the same size with an explicit bijection. |

**Check your understanding:** (1) Why is ∅ a subset of every set but not an element of every set? (2) How large is A × B, and why does that matter for a careless SQL join? (3) Why does the diagonal argument imply some functions cannot be computed?

### Chapter 5 · Functions and relations (weeks 6–7)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Functions | Domain, codomain, image; injective, surjective, bijective; composition and inverse. | Classify 8 Python functions (e.g., `abs`, `str.lower`, `sorted`) by these properties on stated domains. |
| 5.2 Hashing and pigeonhole | A hash function maps a big set into a small one, so collisions must exist. | Find two strings with the same value under a toy 8-bit hash by brute force. |
| 5.3 Relations | Reflexive, symmetric, antisymmetric, transitive; relation as a set of pairs and as a matrix. | Test properties of 6 relations in code. |
| 5.4 Equivalence relations | Equivalence classes and partitions; congruence mod n; union–find preview. | Group 1,000 usernames into classes under "same after lowercasing and removing dots". |
| 5.5 Partial orders | Posets, Hasse diagrams, topological order of a DAG. | Topologically sort this university's own `catalog.json` prerequisites. |

**Check your understanding:** (1) Why can no compression scheme shorten every possible file? (2) Is "follows on social media" an equivalence relation? Why not? (3) Why does a prerequisite graph with a cycle have no valid study order?

### Chapter 6 · Induction and recursion (weeks 7–8)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Weak induction | Base case, inductive step, common mistakes (wrong base, assuming the conclusion). | Prove 1 + 2 + … + n = n(n + 1)/2 and check it in Python for n ≤ 1,000. |
| 6.2 Strong induction | Using all smaller cases; every integer ≥ 2 has a prime factorisation. | Prove any postage of ₹8 or more can be made with ₹3 and ₹5 stamps. |
| 6.3 Recursive definitions | Recursively defined sets and functions; structural induction on lists and trees. | Prove `len(xs + ys) == len(xs) + len(ys)` by structural induction. |
| 6.4 Proving code correct | Preconditions, postconditions, loop invariants; correctness of binary search. | Write the invariant for your binary search from [FND101](../FND101_programming_i_computational_thinking_with_python/README.md); test it with assertions on 10,000 runs. |
| 6.5 The faulty proof | "All horses are the same colour" and other broken inductions. | Find the exact broken step in three faulty proofs. |

**Check your understanding:** (1) Why can't the inductive step alone prove anything? (2) What does a loop invariant have to be true at, and why those points? (3) Where precisely does the "all horses" proof fail?

### Chapter 7 · Recurrences and growth (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Recurrence relations | Fibonacci, Tower of Hanoi (2ⁿ − 1 moves), linear recurrences. | Prove the Hanoi count by induction; count moves in code for n ≤ 20. |
| 7.2 Solving by unrolling | Unrolling, guess-and-verify by induction; T(n) = 2T(n/2) + n. | Unroll the merge-sort recurrence; confirm with an instrumented merge sort. |
| 7.3 Sums | Arithmetic, geometric and harmonic sums; bounding sums with integrals informally. | Compute and bound Σ 1/k for n = 10⁶; compare with ln n. |
| 7.4 Asymptotic notation | O, Ω, Θ; dominant terms; why constants are dropped and when they still matter. | Rank 10 functions by growth; check with a plot. |

**Check your understanding:** (1) Why does naive recursive Fibonacci make exponentially many calls, and what does memoisation change? (2) What is wrong with "O(n²) is always slower than O(n)"? (3) How many moves does Hanoi with 64 discs need, and how long at one move per second?

### Chapter 8 · Counting (weeks 9–10)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Sum and product rules | Counting choices; strings over alphabets; a 6-digit OTP has 10⁶ values. | Count passwords under a policy; compute brute-force time at 10⁹ guesses per second. |
| 8.2 Permutations and combinations | P(n, k), C(n, k), Pascal's triangle, binomial theorem. | Implement `nCr` exactly with integers; verify Pascal's rule for n ≤ 50. |
| 8.3 Stars and bars | Distributing identical items; multisets. | Count ways to split ₹100 in ₹10 notes among 4 people; brute-force check. |
| 8.4 Inclusion–exclusion | Overcounting and correcting; derangements. | Count integers ≤ 1,000 divisible by 3, 5 or 7, by formula and by code. |
| 8.5 Pigeonhole | Simple and generalised; birthday-style arguments. | Prove two people in a group of 367 share a birthday; simulate collisions for 23 people. |

**Check your understanding:** (1) When do you use permutations vs combinations, in one sentence? (2) Why must a brute-force check agree with your formula on small cases before you trust the formula? (3) How many random 32-bit IDs give about a 50% chance of a collision?

### Chapter 9 · Discrete probability (week 10)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Sample spaces | Outcomes, events, uniform probability as counting. | Exact probability of each sum of two dice, then simulate 10⁶ rolls. |
| 9.2 Conditional probability | P(A\|B), independence, Bayes' rule; base-rate fallacy. | A test with 99% accuracy for a 1-in-1,000 condition: compute P(condition \| positive). |
| 9.3 Expectation | Random variables, expected value, linearity of expectation. | Expected number of colliding pairs among n random IDs; compare with simulation. |
| 9.4 Randomised algorithms | Why randomness helps (random pivots, hashing); preview of [FND116](../../semester_2/FND116_probability_and_statistics_i/README.md). | Estimate the expected comparisons of quicksort with random pivots by simulation. |

**Check your understanding:** (1) Why does a highly accurate test still give mostly false positives for rare conditions? (2) Why does linearity of expectation not need independence? (3) Why do birthday collisions appear so much earlier than intuition suggests?

### Chapter 10 · Graphs (weeks 11–12)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Basics | Vertices, edges, directed and undirected, degree, handshake lemma; adjacency list vs matrix. | Prove the handshake lemma; check it on a random graph in NetworkX. |
| 10.2 Paths and connectivity | Walks, paths, cycles, connected components; BFS and DFS as systematic search. | Model a metro map; find connected components and shortest hop counts with BFS. |
| 10.3 Trees | Equivalent definitions; a tree on n vertices has n − 1 edges; spanning trees. | Prove the n − 1 property by induction (remove a leaf). |
| 10.4 Euler and Hamilton | Königsberg, Euler path conditions (easy) vs Hamiltonian paths (no known efficient algorithm). | Decide whether a drawing can be traced without lifting the pen, by the degree rule. |
| 10.5 Colouring and bipartite graphs | Graph colouring for exam timetables and register allocation; bipartite iff no odd cycle. | Colour a 30-course exam-clash graph greedily; report the number of slots and argue a lower bound. |

**Check your understanding:** (1) Why must every graph have an even number of odd-degree vertices? (2) Why is greedy colouring not always optimal? (3) What does an odd cycle prevent, and why?

### Chapter 11 · Number theory and cryptography (weeks 12–13)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Divisibility and primes | Division algorithm, primes, the fundamental theorem of arithmetic, sieve of Eratosthenes. | Sieve primes to 10⁷; time it. |
| 11.2 gcd and Euclid | Euclid's algorithm and why it terminates; extended Euclid and Bézout's identity. | Implement extended Euclid; prove it returns correct coefficients. |
| 11.3 Modular arithmetic | Congruences, modular inverse, fast modular exponentiation (square-and-multiply), Fermat's little theorem, Chinese remainder theorem. | Implement `modpow` and `modinv`; check against Python's built-in `pow(a, b, m)` and `pow(a, -1, m)`. |
| 11.4 RSA and Diffie–Hellman | Why RSA decryption works (Euler's theorem); why real systems need padding (RFC 8017) and vetted libraries. | Build toy RSA with 16-bit primes, then break it by factoring; explain why 2048-bit keys resist this. |
| 11.5 Check digits as algebra | Luhn as mod-10 arithmetic; Verhoeff (used for Aadhaar numbers) built on the dihedral group D5. | Prove Luhn detects every single-digit error; show a transposition it misses. |

**Check your understanding:** (1) Why does fast exponentiation need only about log₂(e) squarings? (2) What breaks in RSA if p = q? (3) Why should you never use your toy RSA for anything real?

### Chapter 12 · Proofs, machines and AI (week 14)
| Lesson | What you learn | Practice |
|---|---|---|
| 12.1 Auditing AI proofs | Hidden assumptions, circular steps, unjustified "clearly", wrong base cases. | Grade 5 AI-generated proofs with a rubric; find and fix each flaw. |
| 12.2 Proof assistants | What Lean checks; formal statement vs intended meaning; libraries such as Mathlib. | Formalise one statement from Chapter 6 in Lean with AI help, and confirm Lean accepts it. |
| 12.3 Solvers as verifiers | Using Z3 to check program properties and find counterexamples. | Ask Z3 for an input where two versions of a function disagree. |
| 12.4 Synthesis and exam practice | Mixed problems across chapters, AI-off. | Two timed mock exams. |

**Check your understanding:** (1) An AI proof uses the result it is proving in step 3; how would you show this to someone? (2) Lean accepted a proof but the theorem statement had the wrong inequality; what was proved? (3) Why is "the solver found no counterexample" meaningful only within the model you encoded?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Truth tables and Z3 | Problem set 1 |
| 2 | 2 | `all`/`any` specifications | Problem set 2 |
| 3 | 3 | Proof writing workshop | Problem set 3 |
| 4 | 3 | Natural Number Game | NNG worlds 1–3; **P1 due** |
| 5 | 4 | Sets and joins | Problem set 4 |
| 6 | 5 | Relations in code | Problem set 5 |
| 7 | 5–6 | Topological sort of the catalog | Problem set 6 |
| 8 | 6–7 | Loop invariants and recurrences | Problem set 7 |
| 9 | 8 | Counting by formula and brute force | Problem set 8 |
| 10 | 8–9 | Probability simulations | Problem set 9; **P2 due** |
| 11 | 10 | Graphs in NetworkX | Problem set 10 |
| 12 | 10–11 | Colouring and number theory | Problem set 11 |
| 13 | 11 | Toy RSA | Problem set 12 |
| 14 | 12 | AI-proof audit | **P3 due** |
| 15 | Review and exam | Mock exams | Final exam (AI-off) |

## Working with AI in this course

- **Use AI for:** hints when stuck (ask for the next step only, not the proof); explaining notation; generating candidate counterexamples that you then test in code; translating your finished proof into Lean, where Lean, not the AI, decides whether it is correct; generating practice problems.
- **Do without AI (drills):** all problem-set proofs are written by you; a weekly 30-minute closed-book drill (one induction proof, one counting problem, one modular computation); the final exam.
- **Verify AI output by:** brute-forcing small cases in Python (n ≤ 10 for counting, n ≤ 10⁴ for identities); running formal claims through Lean or Z3; checking that every proof step cites a definition or an earlier line; recomputing modular arithmetic with `pow`.
- **Where AI still fails here:** frontier models now solve olympiad problems, so the realistic failures are quieter: an inductive step that silently assumes the claim, ordered vs unordered counting mixed up, a base case skipped, or a correct proof of a slightly different statement than the one asked. Lab 10 has you collect and document such failures with the counterexample or the exact faulty line.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Weekly problem sets (proofs plus code checks) | 25% |
| Labs (Z3, Lean, NetworkX, number theory) | 15% |
| Projects: P1 5%, P2 10%, P3 15% | 30% |
| Final exam (3 hours, AI-off) | 30% |

**Gate:** you pass when, with AI off, you can (1) write a correct induction proof of a statement you have not seen, and locate the error in a given faulty proof; (2) derive a counting formula and confirm it with a brute-force program in under 20 lines; (3) implement extended Euclid and modular inverse and use them to encrypt and decrypt with toy RSA; and (4) model a scheduling or dependency problem as a graph and justify your algorithm's correctness in writing.

## Industry reality

TLS 1.3 (RFC 8446) and RSA (RFC 8017) are applied number theory; the 2024 NIST post-quantum standards replace some of it with lattice-based schemes, which is why the field keeps needing people who understand the maths. Build systems and package managers rely on DAGs and topological order. SAT and SMT solvers such as Microsoft's open-source Z3 power program verification, and AWS describes using automated reasoning to check security properties of its services. Pigeonhole guarantees every hash function has collisions; the 2017 SHAttered attack found a practical SHA-1 collision far faster than the generic birthday bound, which is why SHA-1 is being phased out of security uses (Git itself plans SHA-256 as the default for new repositories in Git 3.0).

**Interview questions from this course**

1. *"Prove that a tree with n nodes has n − 1 edges."* Induction on n; every finite tree with ≥ 2 nodes has a leaf; removing it keeps a tree; correct base case.
2. *"How would you compute C(n, k) mod a prime p for large n?"* Factorials with modular inverses via Fermat's little theorem or extended Euclid, precomputation, overflow awareness, and a brute-force check for small n.
3. *"Detect a cycle in a dependency graph and output a build order."* Kahn's algorithm or DFS colouring, why a DAG always has a topological order, what to report when a cycle exists.
4. *"Why does RSA decryption recover the message?"* Choice of e and d with ed ≡ 1 (mod φ(n)), Euler's theorem, the case where m shares a factor with n, and why textbook RSA needs padding.
5. *"How many random 32-bit IDs before a 50% collision chance?"* The birthday bound √(2N ln 2) ≈ 1.18√N, about 77,000 for N = 2³²; implications for ID and hash design.

## Resources (free first)

- **Textbooks:** Lehman, Leighton and Meyer, [*Mathematics for Computer Science*](https://courses.csail.mit.edu/6.042/spring18/mcs.pdf) (MIT, 2018 PDF); Richard Hammack, [*Book of Proof*](https://richardhammack.github.io/BookOfProof/); Oscar Levin, [*Discrete Mathematics: An Open Introduction*](https://discrete.openmathbooks.org/dmoi3.html).
- **Courses:** [MIT 6.1200J Mathematics for Computer Science (Spring 2024)](https://ocw.mit.edu/courses/6-1200j-mathematics-for-computer-science-spring-2024/) and the [2015 lecture videos](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/); [Stanford CS103](https://web.stanford.edu/class/cs103/); [Berkeley CS70](https://www.eecs70.org/); [CMU 15-251](https://www.cs.cmu.edu/~15251/); NPTEL [Discrete Mathematics](https://nptel.ac.in/courses/106106183) (Prof. Sudarshan Iyengar).
- **Tools:** [Lean Natural Number Game](https://adam.math.hhu.de/#/g/leanprover-community/nng4); [Lean](https://lean-lang.org/) and the [Lean community](https://leanprover-community.github.io/); [Z3 guide](https://microsoft.github.io/z3guide/) and [Z3 on GitHub](https://github.com/Z3Prover/z3); [itertools](https://docs.python.org/3/library/itertools.html); [SymPy](https://docs.sympy.org/latest/index.html); [NetworkX](https://networkx.org/documentation/stable/); [OEIS](https://oeis.org/) for checking integer sequences.
- **Practice:** [CSES problem set](https://cses.fi/problemset/) (mathematics and graph sections); [Advent of Code](https://adventofcode.com/).
- **Standards and cases:** [RFC 8017 (PKCS #1 RSA)](https://www.rfc-editor.org/rfc/rfc8017); [RFC 8446 (TLS 1.3)](https://www.rfc-editor.org/rfc/rfc8446); [NIST FIPS 203](https://csrc.nist.gov/pubs/fips/203/final); [SHAttered](https://shattered.io/).

## Sources

- NIST finalises FIPS 203, 204 and 205, August 2024: [NIST news release](https://www.nist.gov/news-events/news/2024/08/nist-releases-first-3-finalized-post-quantum-encryption-standards) (checked Oct 2026).
- Gemini Deep Think IMO 2025 result (35/42, graded by IMO coordinators, 21 Jul 2025): [Google DeepMind](https://deepmind.google/discover/blog/advanced-version-of-gemini-with-deep-think-officially-achieves-gold-medal-standard-at-the-international-mathematical-olympiad/); AlphaProof silver-medal level at IMO 2024: [Google DeepMind](https://deepmind.google/discover/blog/ai-solves-imo-problems-at-silver-medal-level/) (checked Oct 2026).
- AWS automated reasoning for security: [AWS Provable Security](https://aws.amazon.com/security/provable-security/) (checked Oct 2026).
- First practical SHA-1 collision (2017): [shattered.io](https://shattered.io/); Git 3.0 plan to default to SHA-256 (no release date set): [Git BreakingChanges](https://git-scm.com/docs/BreakingChanges) (checked Oct 2026).
- Verhoeff used for Aadhaar numbers (citing an NPCI document): [Wikipedia, Verhoeff algorithm](https://en.wikipedia.org/wiki/Verhoeff_algorithm) (checked Oct 2026).
- Curriculum benchmark: [ACM/IEEE/AAAI CS2023](https://ieeecs-media.computer.org/media/education/reports/CS2023.pdf), Mathematical and Statistical Foundations (checked Oct 2026).

_Last reviewed: 2026-10_
