# CSG402 · Complexity Theory and Theoretical Cryptography

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 4 · 7 | 4 (≈ 120 hours) | L2 → L4 (L5 for P3) | [CSG302](../../year_3/CSG302_compiler_construction/README.md) (catalog); draws on [CSG301](../../year_3/CSG301_advanced_algorithms/README.md), [CS201](../../../../02_year_2_core_computer_science/semester_3/CS201_algorithms_and_complexity/README.md), [FND103](../../../../01_year_1_foundations/semester_1/FND103_discrete_mathematics_for_computing/README.md), [FND116](../../../../01_year_1_foundations/semester_2/FND116_probability_and_statistics_i/README.md) and [CS213](../../../../02_year_2_core_computer_science/semester_4/CS213_security_foundations/README.md) | [CSG403](../CSG403_quantum_computing_for_computer_scientists/README.md) (recommended), [CSG501](../../year_5/CSG501_frontier_seminar_ai_for_mathematics_science/README.md); elective [SAR304](../../../security_architecture/year_3/SAR304_applied_cryptography_and_pki_for_architects/README.md); overlap [OV07](../../../../04_overlaps/OV07_privacy_engineering/README.md) |

Part of the [Computer Science (Theory, Systems and Research) major](../../README.md). CS201 introduced P, NP and reductions. This course asks the deeper questions: what can be computed with limited time, space, randomness or interaction; why some lower bounds are so hard to prove; and how hardness becomes useful, as the foundation of cryptography. The second half builds modern cryptography from first principles: one-way functions, pseudorandomness, provable security, zero-knowledge proofs and lattice-based (post-quantum) schemes. The course is proof-heavy. The CSG302 prerequisite comes from the catalog; the background you actually use is CSG301's probability and CS201's reductions.

## Why this course matters now

Complexity theory is still producing surprises. In 2025 Ryan Williams showed that any multitape Turing machine running in time t can be simulated in roughly √(t log t) space, the first major improvement on the time–space relationship in about fifty years ([arXiv 2502.17779](https://arxiv.org/abs/2502.17779), STOC 2025). India has its own landmark: in 2002 Agrawal, Kayal and Saxena at IIT Kanpur proved that primality can be tested deterministically in polynomial time ([AKS, "PRIMES is in P"](https://www.cse.iitk.ac.in/users/manindra/algebra/primality_v6.pdf)). Theory also reaches production. NIST published its first post-quantum standards in August 2024 ([FIPS 203](https://csrc.nist.gov/pubs/fips/203/final), [FIPS 204](https://csrc.nist.gov/pubs/fips/204/final), [FIPS 205](https://csrc.nist.gov/pubs/fips/205/final)); two of them rest on the hardness of lattice problems (Module-LWE). NIST's draft transition plan would remove quantum-vulnerable public-key algorithms from its standards by 2035 ([NIST PQC](https://csrc.nist.gov/projects/post-quantum-cryptography), [NIST IR 8547 draft](https://csrc.nist.gov/pubs/ir/8547/ipd)). Zero-knowledge proofs now ship in consumer products: Google open-sourced its Longfellow ZK libraries in July 2025 so that a person can prove they are over 18 without revealing anything else ([Google](https://blog.google/technology/safety-security/opening-up-zero-knowledge-proof-technology-to-promote-privacy-in-age-assurance/)). Proof systems are also fragile: in 2022 Trail of Bits disclosed "Frozen Heart" bugs, weak Fiat–Shamir implementations in several zero-knowledge libraries that let provers forge proofs ([Trail of Bits](https://blog.trailofbits.com/2022/04/13/part-1-coordinated-disclosure-of-vulnerabilities-affecting-girault-bulletproofs-and-plonk/)). AI assistants can recite definitions and sketch reductions, but a security proof with a hybrid that does not quite match is the classic failure, and only someone trained to check every step will catch it.

## Learning outcomes

By the end you can:

1. **Define** the main complexity classes (L, NL, P, NP, coNP, PH, PSPACE, EXP, BPP, RP, ZPP, P/poly, IP) and **prove** inclusions and completeness results.
2. **Use** diagonalization, padding and reductions, and **explain** why relativization and natural proofs block common approaches to P vs NP.
3. **Analyse** randomized classes and derandomization, and **explain** AKS as a derandomization success.
4. **Implement and prove** interactive protocols (sum-check, graph non-isomorphism), and **connect** the PCP theorem to hardness of approximation.
5. **Apply** fine-grained hypotheses (SETH, 3SUM, APSP) to explain why some polynomial algorithms are unlikely to improve.
6. **Construct** PRGs, PRFs and encryption from one-way functions and **prove** security with game-based reductions and hybrid arguments.
7. **Design and prove** Σ-protocols and zero-knowledge proofs, and **explain** how SNARKs and Fiat–Shamir work and fail.
8. **Explain and implement** LWE-based encryption and **relate** it to ML-KEM and ML-DSA.
9. **Audit** AI-written proofs and cryptographic code for broken reductions, misuse of assumptions and non-constant-time behaviour.

## Chapters and lessons

### Chapter 1 · Models, diagonalization and hierarchies (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Robust models | Multitape Turing machines, RAM simulation overheads, why P is model-independent | Simulate a 2-tape machine on 1 tape; derive the overhead |
| 1.2 Diagonalization | Undecidability recap; time and space hierarchy theorems | Prove the time hierarchy theorem in your own words |
| 1.3 Padding and translation | Padding arguments; why EXP ≠ P is known but P ≠ NP is not | Show that P = NP implies EXP = NEXP |
| 1.4 Nondeterminism and certificates | NP via verifiers vs nondeterministic machines; coNP | Write verifiers and co-verifiers for 5 problems |

**Check your understanding:** (1) Why does diagonalization separate P from EXP but not P from NP? (2) What does padding transfer, and in which direction? (3) Why is "NP = problems with short checkable certificates" the more useful definition?

### Chapter 2 · NP-completeness in depth and the polynomial hierarchy (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Cook–Levin, properly | The tableau construction; local checkability | Encode a small machine's computation as CNF |
| 2.2 Reductions catalogue | Gadget reductions (3-colouring, Hamiltonian cycle), parsimonious reductions | Lab 1: implement three reductions and check them with a SAT solver on random instances |
| 2.3 Ladner and the structure of NP | NP-intermediate problems if P ≠ NP; candidates (factoring, graph isomorphism) | Explain why graph isomorphism is unlikely to be NP-complete |
| 2.4 The polynomial hierarchy | Σₖ and Πₖ, alternating quantifiers, oracles, collapse results | Place "minimum circuit equivalent" style problems in PH |
| 2.5 Barriers | Relativization (Baker–Gill–Solovay); natural proofs (Razborov–Rudich); algebrization (mention) | Explain in one page why a proof technique that relativizes cannot settle P vs NP |

**Check your understanding:** (1) Why must a reduction for NP-hardness run in polynomial time, and what goes wrong if it does not? (2) What would it mean for the hierarchy to collapse to its second level? (3) Why does an oracle world with P = NP rule out certain proofs?

### Chapter 3 · Space (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Space classes | L, NL, PSPACE; configuration graphs | Show s-t connectivity is in NL |
| 3.2 Savitch and Immerman–Szelepcsényi | NSPACE(s) ⊆ SPACE(s²); NL = coNL by inductive counting | Present the inductive-counting argument to a partner |
| 3.3 PSPACE-completeness | TQBF; two-player games (generalized geography) | Lab 2: a TQBF solver; measure blow-up with quantifier depth |
| 3.4 Time vs space today | Williams (2025): time t in about √(t log t) space; what it does and does not imply | Read the paper's introduction; summarise the main idea in half a page |

**Check your understanding:** (1) Why does Savitch's theorem not show NL = L? (2) Why are many two-player games PSPACE-complete? (3) What does a better time–space simulation suggest about P vs PSPACE?

### Chapter 4 · Randomness and derandomization (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Randomized classes | RP, coRP, ZPP, BPP; amplification (link to CSG301 Chernoff bounds) | Prove ZPP = RP ∩ coRP |
| 4.2 Where BPP sits | BPP ⊆ P/poly (Adleman); BPP ⊆ Σ₂ ∩ Π₂ (Sipser–Gács–Lautemann) | Prove Adleman's theorem |
| 4.3 Primality | Miller–Rabin vs AKS; why AKS matters even though Miller–Rabin is used in practice | Lab 3: implement both; compare running times up to 64-bit inputs |
| 4.4 Derandomization | Hardness vs randomness (Nisan–Wigderson, Impagliazzo–Wigderson: statements); polynomial identity testing as the open frontier | Explain what circuit lower bound would imply BPP = P |

**Check your understanding:** (1) Why is BPP not known to be in NP? (2) Why does nobody use AKS in production, and why is it still important? (3) What is the link between proving lower bounds and removing randomness?

### Chapter 5 · Circuits and lower bounds (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Circuits and advice | Circuit families, P/poly, Karp–Lipton | Show P/poly contains undecidable languages |
| 5.2 Counting arguments | Shannon: most functions need exponential circuits; yet no explicit example is known | Reproduce Shannon's counting argument |
| 5.3 Restricted models | AC⁰ and parity (Håstad's switching lemma, statement); monotone circuits | Show parity needs depth-2 circuits of exponential size |
| 5.4 Why lower bounds are hard | Natural proofs barrier revisited; recent connections (algorithms ⇒ lower bounds) | Write a half-page explanation for a non-specialist |

**Check your understanding:** (1) Why does P/poly containing undecidable languages not contradict anything? (2) Why are lower bounds for restricted circuits possible when general ones are not? (3) What makes a proof "natural"?

### Chapter 6 · Interactive proofs and PCPs (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Interaction plus randomness | IP; graph non-isomorphism protocol; public vs private coins | Simulate GNI with an honest and a cheating prover |
| 6.2 Sum-check | Arithmetization; the sum-check protocol; #SAT ∈ IP | Lab 4: implement sum-check over a prime field |
| 6.3 IP = PSPACE | Proof outline via TQBF arithmetization and degree reduction | Present the outline in 10 minutes |
| 6.4 PCPs | The PCP theorem; equivalence with hardness of approximation (link to CSG301 Chapter 6); MIP* = RE (mention) | Derive inapproximability of MAX-3SAT from the PCP theorem (sketch) |
| 6.5 From IPs to succinct arguments | Delegated computation; why sum-check underlies modern SNARKs | Measure verifier time vs prover time in your Lab 4 code |

**Check your understanding:** (1) Why does the verifier in sum-check need only one random field element per round? (2) What does the PCP theorem say in plain words? (3) Why is soundness error |degree|/|field| per round, and how do you shrink it?

### Chapter 7 · Fine-grained complexity (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Conjectures | SETH, Orthogonal Vectors, 3SUM, APSP | Reduce CNF-SAT to Orthogonal Vectors |
| 7.2 Conditional lower bounds | Edit distance has no strongly subquadratic algorithm under SETH (Backurs–Indyk) | Explain why CS201's O(nm) edit distance is probably optimal |
| 7.3 Using it in practice | Choosing approximations or parameterisations when exact speed-ups are ruled out | Lab 5: OV brute force vs bit-packed; extrapolate to 10⁶ vectors |

**Check your understanding:** (1) Why is a conditional lower bound useful to an engineer? (2) What would refuting SETH imply? (3) Why do fine-grained reductions need to be very efficient themselves?

### Chapter 8 · One-way functions and pseudorandomness (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Why P ≠ NP is not enough | Average-case hardness; one-way functions; Impagliazzo's five worlds | Explain why cryptography needs more than P ≠ NP |
| 8.2 Negligible functions and indistinguishability | Computational indistinguishability, the hybrid argument | Prove that indistinguishability is transitive over polynomially many hybrids |
| 8.3 Hard-core predicates | Goldreich–Levin | Present the Goldreich–Levin theorem statement and intuition |
| 8.4 PRGs and PRFs | PRG length extension; GGM construction of PRFs; PRPs and Luby–Rackoff | Lab 6: break three weak "PRGs" with statistical distinguishers |

**Check your understanding:** (1) What is the difference between a function that is hard in the worst case and one-way? (2) Why does a hybrid argument lose a factor equal to the number of hybrids? (3) Why does GGM need a length-doubling PRG?

### Chapter 9 · Provable security (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Defining security | Games: IND-CPA, IND-CCA, EUF-CMA; adversaries and advantage | Write the IND-CCA game precisely |
| 9.2 Proofs by reduction | Building an adversary for the assumption from an adversary for the scheme | Prove CPA security of PRF-based encryption |
| 9.3 Authenticated encryption | MACs from PRFs; encrypt-then-MAC and CCA security; why encrypt-and-MAC fails | Lab 7: write the encrypt-then-MAC CCA proof as a sequence of games |
| 9.4 Idealized models | Random oracle model, its uses (Fiat–Shamir, OAEP) and the CGH separation argument | Discuss when ROM proofs are acceptable |
| 9.5 Machine-checked crypto proofs | EasyCrypt and CryptoVerif (overview) | Mechanize one game hop in EasyCrypt (guided) |

**Check your understanding:** (1) Why must a reduction run in polynomial time with polynomial loss? (2) What does a "tight" reduction buy in parameter choice? (3) Why does a scheme proven in the random oracle model not automatically stay secure with SHA-256?

### Chapter 10 · Public-key cryptography (week 10)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Number-theoretic assumptions | Discrete log, CDH, DDH, RSA, factoring; generic group model (idea) | Show DDH is easy in a group with a pairing |
| 10.2 Key exchange and encryption | Diffie–Hellman, ElGamal (IND-CPA under DDH), trapdoor permutations | Prove ElGamal IND-CPA from DDH |
| 10.3 Signatures | Hash-and-sign, Schnorr signatures, nonce requirements | Lab 8: show on your own toy implementation why a reused Schnorr nonce reveals the key |
| 10.4 The quantum threat | Shor's algorithm breaks factoring and discrete log (details in CSG403); resource estimates (Gidney, 2025) | Summarise the 2025 estimate and its assumptions |

**Check your understanding:** (1) Why is DDH stronger than CDH? (2) Why does nonce reuse in Schnorr or ECDSA leak the key? (3) Why are symmetric schemes much less affected by quantum computers than public-key schemes?

### Chapter 11 · Zero-knowledge proofs (weeks 11–12)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 The simulation paradigm | Completeness, soundness, zero-knowledge; graph isomorphism protocol | Write the simulator for graph isomorphism ZK |
| 11.2 Σ-protocols | Schnorr identification, special soundness, honest-verifier ZK, OR-proofs | Prove special soundness for Schnorr |
| 11.3 Fiat–Shamir | Making proofs non-interactive; what must be hashed; the Frozen Heart bugs | Lab 9: implement Fiat–Shamir correctly; show a "weak" variant accepting a forged proof in your own toy code |
| 11.4 ZK for NP and commitments | Commitment schemes; ZK for 3-colouring | Implement a commitment-based 3-colouring ZK protocol |
| 11.5 SNARKs and STARKs | Arithmetic circuits, polynomial commitments, Groth16 vs PLONK vs STARKs (setup, proof size, assumptions) | Lab 10: a Merkle-membership circuit in circom or arkworks; measure prove/verify time |
| 11.6 Deployments | Age assurance (Google Longfellow ZK), private payments, rollups; MPC and FHE in one lesson | Write the threat model for an "over 18" credential |

**Check your understanding:** (1) Why does zero-knowledge need a simulator rather than "the verifier learns nothing obvious"? (2) What exactly goes wrong if the Fiat–Shamir hash omits the statement? (3) What does a trusted setup trust?

### Chapter 12 · Lattices and post-quantum cryptography (weeks 13–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 12.1 Lattices | Bases, SVP and CVP, LLL reduction and what it achieves | Lab 11: run LLL with fpylll on small dimensions; watch it fail as dimension grows |
| 12.2 SIS and LWE | Ajtai's SIS; Regev's LWE; worst-case to average-case reductions (statements) | Implement Regev encryption; verify correctness with the noise bound |
| 12.3 Structured lattices | Ring- and Module-LWE; efficiency via NTT | Implement a number-theoretic transform and use it for polynomial multiplication |
| 12.4 The NIST standards | ML-KEM (FIPS 203), ML-DSA (FIPS 204), SLH-DSA (FIPS 205, hash-based); Falcon and HQC in ongoing standardization | Run ML-KEM test vectors from NIST's ACVP against a library |
| 12.5 Migration | Hybrid key exchange, crypto agility, "harvest now, decrypt later", NIST IR 8547 draft timeline | Write a one-page migration plan for an illustrative bank |

**Check your understanding:** (1) Why does LWE need noise, and what limits how much? (2) Why is a hash-based signature (SLH-DSA) considered conservative? (3) Why deploy hybrid classical+PQ key exchange rather than PQ alone?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Hierarchy proofs (AI off) | Problem set 1 |
| 2 | 2 | Lab 1 · Reductions checked by SAT | — |
| 3 | 3 | Lab 2 · TQBF | Problem set 2; **P1 starts** |
| 4 | 4 | Lab 3 · Primality | — |
| 5 | 5 | Lower-bound proofs | **P1 due** |
| 6 | 6 | Lab 4 · Sum-check | — |
| 7 | 7 | Lab 5 · Orthogonal vectors | Mid-term (AI off); **P2 starts** |
| 8 | 8 | Lab 6 · Distinguishers | — |
| 9 | 9 | Lab 7 · Game-based proofs | Proof write-up |
| 10 | 10 | Lab 8 · Signatures | **P2 due**; P3 proposal |
| 11 | 11 | Lab 9 · Fiat–Shamir | — |
| 12 | 11 | Lab 10 · SNARK circuit | P3 midpoint |
| 13 | 12 | Lab 11 · Lattices and LWE | — |
| 14 | 12 | ML-KEM test vectors | **P3 due** |
| 15 | Review | Proof oral | Final exam (AI off) |

## Working with AI in this course

- **Use AI for:** explaining a step in a textbook proof (then re-deriving it yourself); generating random instances and checking reductions with solvers; boilerplate for finite-field arithmetic, NTTs and test harnesses; translating pseudocode from FIPS documents into tests; summarising papers before you read them.
- **Do without AI (drills):** every proof you submit (hierarchy theorems, completeness results, hybrid arguments, security reductions, simulators, special soundness); constructing reductions; the mid-term, final and proof oral. In this course, the proof *is* the deliverable.
- **Verify AI output by:** checking that each hybrid differs from the next in exactly one place that a stated assumption covers; checking the direction and running time of every reduction; testing reductions on random instances with a SAT solver; running cryptographic code against official test vectors (NIST ACVP) and a timing test for constant-time behaviour; never using AI-written cryptographic code outside the lab.
- **Where AI still fails here (show it):** in Lab 7 and Lab 9 you will ask two assistants for (a) a CCA-security proof of encrypt-then-MAC and (b) a Fiat–Shamir transform for Schnorr, then grade them. Common failures: hybrids that change two things at once, reductions that need the secret key they do not have, omitting the statement or commitment from the Fiat–Shamir hash (the Frozen Heart pattern), and code that branches on secret data. Keep the graded examples.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (11) | 20% |
| Projects P1 / P2 / P3 | 5% / 15% / 20% |
| Weekly proof sets (AI off) | 15% |
| Mid-term (AI off) | 10% |
| Final exam (AI off) + proof oral | 15% |

**Mastery gate.** You pass when you can, with AI off: (1) prove an unseen problem NP-complete or PSPACE-complete in 60 minutes; (2) write a complete game-based security proof for a symmetric construction you have not seen, with every hybrid justified; (3) design a Σ-protocol for a given algebraic relation and prove completeness, special soundness and honest-verifier zero-knowledge; and (4) explain LWE encryption, derive its correctness condition, and say how parameter choices trade security against failure probability.

## Industry reality

This material is used by cryptography engineers (PQC migration, protocol design and review), zero-knowledge teams (identity, payments, blockchain scaling), security researchers and auditors, and by theory researchers in labs and universities. PQC migration is now a compliance topic for banks and governments worldwide; NIST's standards and draft timeline drive it. Cryptography is also where AI-written code is most dangerous: the code compiles and passes simple tests while leaking secrets through timing or failing a subtle proof condition.

**Interview questions from this course**

1. *What does IND-CCA security mean, and why do we need authenticated encryption?* Strong answer: the game with a decryption oracle; malleability attacks on CPA-only schemes; encrypt-then-MAC or AEAD (AES-GCM, ChaCha20-Poly1305); nonce misuse and what breaks.
2. *Explain zero-knowledge to an engineer and give a real use.* Strong answer: completeness, soundness, zero-knowledge via simulation; Σ-protocols and Fiat–Shamir; SNARK trade-offs (setup, proof size); age assurance or private payments; what the circuit must constrain.
3. *Why is ML-KEM believed to resist quantum attacks?* Strong answer: Module-LWE; no known quantum algorithm beyond generic speed-ups; lattice reduction as the best attack; parameter sets; hybrid deployment; why RSA and ECC fall to Shor.
4. *Does P ≠ NP imply secure cryptography?* Strong answer: no; cryptography needs average-case hardness and one-way functions; NP-hardness is worst-case; Impagliazzo's worlds.
5. *Review this Fiat–Shamir implementation.* Strong answer: the hash must include the statement, all public parameters and the prover's commitment; domain separation; the Frozen Heart disclosures; test with forged proofs.

## Resources (free first)

- **Complexity:** Arora and Barak, [Computational Complexity: A Modern Approach (draft)](https://theory.cs.princeton.edu/complexity/book.pdf); Boaz Barak, [Introduction to Theoretical Computer Science](https://introtcs.org/); MIT [18.404J Theory of Computation (Sipser, OCW)](https://ocw.mit.edu/courses/18-404j-theory-of-computation-fall-2020/); Salil Vadhan, [Pseudorandomness](https://people.seas.harvard.edu/~salil/pseudorandomness/); NPTEL [Computational Complexity](https://nptel.ac.in/courses/106106229) (IIT Hyderabad); [Complexity Zoo](https://complexityzoo.net/Complexity_Zoo); [ECCC](https://eccc.weizmann.ac.il/).
- **Cryptography:** Boneh and Shoup, [A Graduate Course in Applied Cryptography](https://toc.cryptobook.us/); Pass and shelat, [A Course in Cryptography](https://www.cs.cornell.edu/courses/cs4830/2010fa/lecnotes.pdf); Justin Thaler, [Proofs, Arguments, and Zero-Knowledge](https://people.cs.georgetown.edu/jthaler/ProofsArgsAndZK.pdf); Lindell, [How to Simulate It](https://eprint.iacr.org/2016/046); Peikert, [A Decade of Lattice Cryptography](https://eprint.iacr.org/2015/939); Regev, [LWE survey](https://cims.nyu.edu/~regev/papers/lwesurvey.pdf); NPTEL [Foundations of Cryptography](https://nptel.ac.in/courses/106106221) (IIIT Bangalore); [ZKDocs](https://www.zkdocs.com/); [Cryptopals](https://cryptopals.com/) (exercises on your own code).
- **Papers:** [Williams 2025](https://arxiv.org/abs/2502.17779); [PRIMES is in P](https://www.cse.iitk.ac.in/users/manindra/algebra/primality_v6.pdf); [Backurs–Indyk](https://arxiv.org/abs/1412.0348); [MIP* = RE](https://arxiv.org/abs/2001.04383); [Groth16](https://eprint.iacr.org/2016/260); [PLONK](https://eprint.iacr.org/2019/953); [Gidney 2025](https://arxiv.org/abs/2505.15917).
- **Standards and tools:** [FIPS 203](https://csrc.nist.gov/pubs/fips/203/final), [FIPS 204](https://csrc.nist.gov/pubs/fips/204/final), [FIPS 205](https://csrc.nist.gov/pubs/fips/205/final), [NIST PQC project](https://csrc.nist.gov/projects/post-quantum-cryptography), [ACVP test vectors](https://github.com/usnistgov/ACVP-Server), [liboqs](https://openquantumsafe.org/liboqs/), [fpylll](https://github.com/fplll/fpylll), [SageMath](https://www.sagemath.org/), [EasyCrypt](https://www.easycrypt.info/), [arkworks](https://arkworks.rs/), [circom](https://docs.circom.io/), [Microsoft SEAL](https://github.com/microsoft/SEAL), [Longfellow ZK](https://github.com/google/longfellow-zk).
- **Paid, worth it:** Sipser, *Introduction to the Theory of Computation*; Katz and Lindell, *Introduction to Modern Cryptography* (3rd ed.).

## Sources

All checked 12 Oct 2026.

- Williams, "Simulating Time With Square-Root Space" (arXiv 2502.17779; STOC 2025) — https://arxiv.org/abs/2502.17779
- Agrawal, Kayal, Saxena, "PRIMES is in P" (IIT Kanpur; *Annals of Mathematics* 2004) — https://www.cse.iitk.ac.in/users/manindra/algebra/primality_v6.pdf
- NIST FIPS 203, 204, 205 (13 Aug 2024) — https://csrc.nist.gov/pubs/fips/203/final ; https://csrc.nist.gov/pubs/fips/204/final ; https://csrc.nist.gov/pubs/fips/205/final
- NIST Post-Quantum Cryptography project page (updated 5 Aug 2026; Falcon and HQC in ongoing standardization; IR 8547 timeline to 2035) — https://csrc.nist.gov/projects/post-quantum-cryptography ; NIST IR 8547 initial public draft (Nov 2024) — https://csrc.nist.gov/pubs/ir/8547/ipd ; NIST selects HQC (Mar 2025) — https://www.nist.gov/news-events/news/2025/03/nist-selects-hqc-fifth-algorithm-post-quantum-encryption
- Google, "Opening up 'Zero-Knowledge Proof' technology to promote privacy in age assurance" (3 Jul 2025) — https://blog.google/technology/safety-security/opening-up-zero-knowledge-proof-technology-to-promote-privacy-in-age-assurance/
- Trail of Bits, "Coordinated disclosure of vulnerabilities affecting Girault, Bulletproofs, and PlonK" (13 Apr 2022) — https://blog.trailofbits.com/2022/04/13/part-1-coordinated-disclosure-of-vulnerabilities-affecting-girault-bulletproofs-and-plonk/
- Gidney, "How to factor 2048 bit RSA integers with less than a million noisy qubits" (May 2025) — https://arxiv.org/abs/2505.15917

_Last reviewed: 2026-10_
