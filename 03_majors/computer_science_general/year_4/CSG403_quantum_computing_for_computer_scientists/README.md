# CSG403 · Quantum Computing for Computer Scientists

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 4 · 8 | 4 (≈ 120 hours) | L1 → L4 | [CSG303](../../year_3/CSG303_distributed_systems_ii_consensus_replication/README.md) (catalog); draws on [FND113](../../../../01_year_1_foundations/semester_2/FND113_linear_algebra_and_calculus_for_computing/README.md), [FND116](../../../../01_year_1_foundations/semester_2/FND116_probability_and_statistics_i/README.md), [CSG301](../../year_3/CSG301_advanced_algorithms/README.md); recommended [CSG402](../CSG402_complexity_theory_and_theoretical_cryptography/README.md) | [CSG501](../../year_5/CSG501_frontier_seminar_ai_for_mathematics_science/README.md); supports [THS501](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md) |

Part of the [Computer Science (Theory, Systems and Research) major](../../README.md). No physics is assumed beyond school level. Quantum computing is presented as linear algebra over complex numbers plus a rule for measurement, which is all a computer scientist needs to write circuits, analyse algorithms, reason about complexity and read error-correction papers. The catalog lists CSG303 as the prerequisite; the course connects to it through error correction, which is replication against faults in another form. What you really need is FND113's linear algebra and CSG301's probability.

## Why this course matters now

The field moved from "does error correction work?" to "how fast can it be engineered?". In December 2024 Google reported surface-code memories whose logical error rate fell as the code grew from distance 3 to 5 to 7, showing operation below the surface-code threshold ([Nature, 2024](https://www.nature.com/articles/s41586-024-08449-y)). In November 2025 Quantinuum launched Helios, with 98 barium-ion qubits, a reported two-qubit gate fidelity of 99.921% and 48 error-corrected logical qubits at a 2:1 encoding rate (company-reported) ([Quantum Computing Report](https://quantumcomputingreport.com/quantinuum-launches-helios-quantum-computer-with-industry-leading-fidelity-and-singapore-partnership/)). IBM unveiled Nighthawk (120 qubits, 218 tunable couplers) and Loon, a proof-of-concept processor for quantum LDPC codes ([IBM, Nov 2025](https://www.ibm.com/quantum/blog/qdc-2025)), with a roadmap targeting a 200-logical-qubit system by 2029 ([IBM roadmap](https://www.ibm.com/roadmaps/quantum.pdf)). The cryptographic stakes rose too: Gidney estimated in May 2025 that RSA-2048 could be factored with fewer than a million noisy qubits in under a week, down from 20 million qubits in 2019 ([arXiv 2505.15917](https://arxiv.org/abs/2505.15917), [arXiv 1905.09749](https://arxiv.org/abs/1905.09749)). India's National Quantum Mission (approved April 2023, ₹6,003.65 crore to 2030–31) targets intermediate-scale machines of 50–1,000 physical qubits ([DST](https://dst.gov.in/cabinet-approves-national-quantum-mission-scale-scientific-industrial-rd-quantum-technologies)). AI is already part of the stack: Google DeepMind's AlphaQubit decodes surface-code errors with a neural network ([Nature, 2024](https://www.nature.com/articles/s41586-024-08148-8)), and there is a benchmark for AI-generated Qiskit code ([Qiskit HumanEval](https://arxiv.org/abs/2406.14712)). The field still needs people who can tell a real advantage from a hyped one, read a resource estimate, and write correct circuits.

## Learning outcomes

By the end you can:

1. **Compute** with state vectors, unitaries, tensor products and measurement, by hand for 1–3 qubits and in code for 20+.
2. **Explain and demonstrate** superposition, interference and entanglement with Bell states, teleportation and the CHSH game.
3. **Program** circuits in Qiskit and Cirq, run them on simulators and on real cloud hardware, and **interpret** noisy results.
4. **Analyse** Deutsch–Jozsa, Bernstein–Vazirani, Simon, Grover, the QFT, phase estimation and Shor, including their query or gate complexity and why they work.
5. **Place** BQP among classical complexity classes and **evaluate** claims of quantum advantage, including dequantization results.
6. **Model** noise with density matrices and channels, and **apply** error mitigation, while explaining its limits.
7. **Explain** stabilizer codes, the surface code, thresholds and decoding, and **simulate** error-correction experiments with Stim and PyMatching.
8. **Compare** hardware platforms using published metrics, and **read** vendor claims critically (physical vs logical vs error-detected qubits).
9. **Advise** on post-quantum migration timelines using resource estimates and the CSG402 standards.

## Chapters and lessons

### Chapter 1 · The linear algebra of quantum computing (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Complex vectors and Dirac notation | Kets, bras, inner products, norms, orthonormal bases | Convert 10 states between vector and ket notation |
| 1.2 Operators | Unitary and Hermitian matrices, eigenvalues, projectors, the spectral theorem | Diagonalize Pauli X, Y, Z and Hadamard by hand |
| 1.3 Tensor products | Composite systems, Kronecker products, why the state space doubles per qubit | Compute H⊗I and CNOT matrices; count memory for 30 qubits |
| 1.4 A simulator of your own | Statevector simulation with NumPy; applying a gate without building the full matrix | Lab 1: a 10-qubit statevector simulator with tests |

**Check your understanding:** (1) Why must quantum gates be unitary? (2) Why does simulating n qubits naively need 2ⁿ complex numbers? (3) What is the difference between a sum of states and a mixture?

### Chapter 2 · Qubits, gates and measurement (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 One qubit | Amplitudes, the Born rule, the Bloch sphere | Plot states on the Bloch sphere after sequences of gates |
| 2.2 Single-qubit gates | X, Y, Z, H, S, T, rotations; global vs relative phase | Show HZH = X numerically and geometrically |
| 2.3 Measurement | Projective measurement, basis changes, statistics from repeated shots | Estimate an amplitude from 1,000 shots with a confidence interval |
| 2.4 No-cloning | Proof from linearity; why it matters for copying, error correction and cryptography | Write the 3-line proof without notes |
| 2.5 First hardware run | Cloud access (IBM Quantum free plan or another provider), transpilation, shots | Lab 2: run the same circuit on a simulator and on hardware; compare |

**Check your understanding:** (1) Why can't you observe a global phase but can observe a relative phase? (2) Why does measuring in a different basis need a gate first? (3) What does no-cloning forbid that classical error correction relies on?

### Chapter 3 · Entanglement and protocols (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Bell states | CNOT, entanglement, product vs entangled states, Schmidt decomposition (idea) | Prove that a Bell state is not a product state |
| 3.2 The CHSH game | Classical value 3/4 vs quantum cos²(π/8) ≈ 0.85; what Bell tests show | Lab 3: play CHSH on real hardware; compare the measured win rate with 0.75 and 0.85 |
| 3.3 Teleportation and superdense coding | Using entanglement plus classical bits; no faster-than-light signalling | Implement teleportation with mid-circuit measurement and feed-forward |
| 3.4 Quantum key distribution vs post-quantum cryptography | BB84 idea; why most organisations choose PQC (link to CSG402) | Write a one-paragraph comparison for a non-specialist |

**Check your understanding:** (1) Why does teleportation not transmit information faster than light? (2) What does a CHSH win rate above 0.75 rule out? (3) Why is QKD hard to deploy at internet scale?

### Chapter 4 · Circuits, universality and simulation (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 The circuit model | Gate sets, depth, width, uncomputation, reversible classical logic (Toffoli) | Build a reversible adder and uncompute its garbage |
| 4.2 Universality | Clifford + T is universal; Solovay–Kitaev (statement); T-count as a cost measure | Approximate a rotation with Clifford+T using a synthesis tool; report T-count |
| 4.3 Classical simulation | Gottesman–Knill (Clifford circuits are easy); stabilizer simulation; tensor networks | Lab 4: simulate 1,000-qubit Clifford circuits with Stim; hit the limit of statevector simulation |
| 4.4 Programming frameworks | Qiskit (circuits, transpiler, primitives), Cirq, PennyLane; API changes between major versions | Port one circuit between Qiskit and Cirq |

**Check your understanding:** (1) Why does entanglement alone not make a computation hard to simulate classically? (2) Why is T-count the main cost in fault-tolerant estimates? (3) Why do you uncompute ancilla qubits?

### Chapter 5 · Query algorithms (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Oracles and phase kickback | Bit oracles vs phase oracles; the kickback trick | Build phase oracles for three Boolean functions |
| 5.2 Deutsch–Jozsa and Bernstein–Vazirani | One query vs many; interference as the resource | Lab 5: implement both; count classical queries needed for the same task |
| 5.3 Simon's algorithm | Exponential separation in the query model; the ancestor of Shor | Implement Simon's for n = 4 and solve the linear system classically |
| 5.4 Query complexity | Lower bounds by the polynomial and adversary methods (ideas) | Explain why query separations do not directly give real-world speed-ups |

**Check your understanding:** (1) Where exactly does interference cancel the wrong answers in Deutsch–Jozsa? (2) Why is Simon's speed-up exponential but Deutsch–Jozsa's only against deterministic classical algorithms? (3) What is lost when an oracle must be built from real gates?

### Chapter 6 · Grover and amplitude amplification (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Grover's algorithm | Oracle + diffusion as a rotation; O(√N) iterations | Lab 6: Grover on 3–5 qubits; plot success vs iterations, including over-rotation |
| 6.2 Optimality | The Ω(√N) lower bound (BBBV), so no exponential search speed-up | Present the hybrid-argument idea of the lower bound |
| 6.3 Amplitude amplification and estimation | Generalising Grover; quadratic speed-up for Monte Carlo estimation | Compare sample counts for estimating a probability classically and with amplitude estimation |
| 6.4 Consequences | Symmetric key sizes (AES-256 margin); why Grover rarely wins in practice once error correction overhead is counted | Estimate the wall-clock time of a Grover search on 2⁶⁴ items under stated gate times |

**Check your understanding:** (1) Why does running Grover for too many iterations make the answer worse? (2) Why does a quadratic speed-up often disappear once error-correction overhead is included? (3) Why is AES-256 considered safe against Grover?

### Chapter 7 · Fourier transform, phase estimation and Shor (weeks 7–8)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 The quantum Fourier transform | Circuit with O(n²) gates; approximate QFT | Build and verify the QFT against a DFT for 4 qubits |
| 7.2 Phase estimation | Estimating eigenphases; precision vs qubits; success probability | Lab 7: phase estimation for a T gate and a random unitary |
| 7.3 Order finding and factoring | Reduction from factoring to order finding; modular exponentiation; continued fractions | Run Shor for N = 15 and N = 21 on a simulator; post-process by hand once |
| 7.4 Discrete logarithms and elliptic curves | Why Shor also breaks Diffie–Hellman and ECC | Explain which deployed algorithms fall and which do not |
| 7.5 Resource estimation | Logical qubits, T-count/Toffoli-count, code distance, physical qubits and time; Gidney–Ekerå 2019 vs Gidney 2025 | Reproduce the structure of one published estimate with Qualtran or a spreadsheet model |

**Check your understanding:** (1) Where does the exponential speed-up in Shor's algorithm come from? (2) Why is modular exponentiation the expensive part of the circuit? (3) Which assumptions dominate a resource estimate, and how did they change between 2019 and 2025?

### Chapter 8 · Quantum complexity and the advantage question (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 BQP | Definition; P ⊆ BPP ⊆ BQP ⊆ PSPACE; oracle separations | Prove BQP ⊆ PSPACE by a path-sum argument (sketch) |
| 8.2 What quantum computers probably cannot do | No known efficient algorithm for NP-complete problems; Grover's bound | Rebut three popular claims about quantum computers "trying all answers" |
| 8.3 Advantage experiments | Random circuit sampling, verification by cross-entropy, classical spoofing and simulation responses; quantum volume and other benchmarks | Read one advantage claim and one classical rebuttal; summarise both fairly |
| 8.4 Dequantization | Tang's quantum-inspired classical algorithm for recommendation systems (2018) | Explain what assumption about data access made the quantum speed-up disappear |

**Check your understanding:** (1) Why is BQP believed not to contain NP? (2) Why are sampling advantages hard to verify? (3) What does a dequantization result tell you about a proposed quantum machine-learning speed-up?

### Chapter 9 · Noise, mitigation and near-term algorithms (week 10)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Density matrices and channels | Mixed states, Kraus operators, depolarizing and amplitude-damping noise; T1, T2 | Simulate a noisy Bell state and compute its fidelity |
| 9.2 Hardware error budgets | Gate and readout fidelities, crosstalk, leakage; calibration data from providers | Lab 8: predict a circuit's success probability from published calibration data; compare with a hardware run |
| 9.3 Error mitigation | Readout correction, zero-noise extrapolation, probabilistic error cancellation and its sampling cost | Apply ZNE to an expectation value and report the variance cost |
| 9.4 Variational algorithms | VQE and QAOA; barren plateaus; why heuristics need classical baselines | Lab 9: QAOA for MaxCut vs Goemans–Williamson from CSG301 on the same graphs |

**Check your understanding:** (1) Why does error mitigation not scale the way error correction does? (2) What does a barren plateau do to training? (3) Why must every near-term algorithm be compared against the best classical method, not a naive one?

### Chapter 10 · Quantum error correction (weeks 11–12)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Repetition codes | Bit-flip and phase-flip codes; syndromes without measuring data | Implement the 3-qubit code; show it corrects one bit flip |
| 10.2 The stabilizer formalism | Pauli groups, stabilizers, logical operators; Shor and Steane codes | Write the stabilizers of the Steane code and check commutation |
| 10.3 The surface code | Lattice, X and Z checks, code distance, circuit-level noise | Lab 10: Stim memory experiments for distances 3–9 |
| 10.4 Thresholds and decoding | Threshold theorem; minimum-weight perfect matching (PyMatching); neural decoders (AlphaQubit); the Λ suppression factor in Google's Willow results | Estimate a threshold from your simulations; compare with a published value |
| 10.5 Toward fault tolerance | Lattice surgery, magic-state distillation, logical gates; qLDPC codes and IBM's bivariate bicycle codes | Compare physical-qubit overheads for a surface code vs a qLDPC memory at the same logical error rate (from published figures) |

**Check your understanding:** (1) How can you detect an error without destroying the encoded information? (2) What does it mean physically to be "below threshold"? (3) Why do qLDPC codes promise lower overhead, and what do they demand from hardware?

### Chapter 11 · Hardware and compilation (week 13)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Platforms | Superconducting circuits (Google, IBM), trapped ions (Quantinuum, IonQ), neutral atoms (QuEra, Pasqal, Atom Computing), photonics (PsiQuantum, Xanadu), spin qubits; trade-offs in speed, connectivity and fidelity | Build a comparison table from primary sources with dates |
| 11.2 Compiling circuits | Native gate sets, transpilation, qubit mapping and routing (SABRE), optimization passes (link to CSG302) | Lab 11: transpile a circuit for two coupling maps; compare depth and two-qubit gate counts |
| 11.3 Reading claims | Physical vs logical vs error-detected qubits; fidelity definitions; who measured what | Grade three press releases against their technical papers |
| 11.4 Roadmaps and India | Vendor roadmaps (IBM to 2029 and beyond); India's National Quantum Mission and its hubs | Write a dated one-page landscape brief |

**Check your understanding:** (1) Why do all-to-all connected trapped ions need fewer SWAP gates? (2) Why are logical-qubit counts from different vendors often not comparable? (3) What would make you believe a roadmap date?

### Chapter 12 · Implications and careers (week 14)
| Lesson | What you learn | Practice |
|---|---|---|
| 12.1 Cryptography timelines | "Harvest now, decrypt later"; Mosca's inequality (migration time + data lifetime vs time to a cryptographically relevant machine) | Apply Mosca's inequality to three illustrative organisations |
| 12.2 Applications with evidence | Chemistry and materials simulation as the most-studied candidates; optimization claims and their classical competition | Summarise one application paper with a resource estimate |
| 12.3 Quantum software work | Compilers, error-correction software, benchmarking, resource estimation, PQC migration | Present your P3 |

**Check your understanding:** (1) Why can PQC migration be urgent even if large quantum computers are years away? (2) Which applications have the strongest evidence of eventual advantage, and why? (3) Which quantum-software skills transfer to classical jobs?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Statevector simulator | Hand-calculation set (AI off) |
| 2 | 2 | Lab 2 · First hardware run | **P1 starts** |
| 3 | 3 | Lab 3 · CHSH on hardware | — |
| 4 | 4 | Lab 4 · Stabilizer simulation | **P1 due** |
| 5 | 5 | Lab 5 · Query algorithms | — |
| 6 | 6 | Lab 6 · Grover | **P2 starts** |
| 7 | 7 | Lab 7 · Phase estimation | Mid-term (AI off) |
| 8 | 7 | Shor for 15 and 21 | — |
| 9 | 8 | Advantage-claim review | **P2 due** |
| 10 | 9 | Labs 8–9 · Noise and QAOA | P3 proposal |
| 11 | 10 | Lab 10 · Surface code in Stim | — |
| 12 | 10 | Decoding and thresholds | P3 midpoint |
| 13 | 11 | Lab 11 · Transpilation | Landscape brief |
| 14 | 12 | Presentations | **P3 due** |
| 15 | Review | Circuit oral | Final exam (AI off) |

## Working with AI in this course

- **Use AI for:** explaining a derivation step; translating circuits between Qiskit, Cirq and PennyLane; boilerplate for running jobs, collecting counts and plotting; summarising hardware papers (then checking numbers against the paper); drafting Stim circuits for standard experiments.
- **Do without AI (drills):** all hand calculations for 1–3 qubits; deriving Deutsch–Jozsa, Grover's rotation and phase estimation; the no-cloning proof; stabilizer calculations; the mid-term, final and circuit oral.
- **Verify AI output by:** comparing every circuit's output with your own statevector simulator on small sizes; checking unitarity and expected measurement distributions; pinning library versions and running code before trusting it; checking every hardware number against the vendor's paper or calibration data, with dates.
- **Where AI still fails here (show it):** quantum SDKs change quickly between major versions, and assistants often produce code for removed APIs; Qiskit HumanEval exists precisely to measure this kind of generation. In the week-13 audit exercise, ask two assistants for Grover, QPE and a surface-code memory experiment, run them under pinned current versions, and log every failure: removed functions, wrong qubit ordering (Qiskit's little-endian convention), missing uncomputation, and wrong oracle phases. Also ask for "the current largest quantum computer" and check the answer's date and definition of qubit.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (11) | 20% |
| Projects P1 / P2 / P3 | 5% / 15% / 25% |
| Hand-calculation sets (AI off) | 10% |
| Mid-term (AI off) | 10% |
| Final exam (AI off) + circuit oral | 15% |

**Mastery gate.** You pass when you can, with AI off: (1) compute the output state and measurement probabilities of an unseen 3-qubit circuit by hand; (2) derive Grover's iteration count and explain over-rotation; (3) explain phase estimation and how Shor reduces factoring to it, including the classical post-processing; (4) given a stabilizer code's generators, find its logical operators and say which single-qubit errors it corrects; and (5) critique a vendor press release against its technical paper, separating physical, logical and error-detected qubits.

## Industry reality

Quantum software roles exist at hardware companies (compilers, control software, error-correction software, benchmarking), at cloud providers, in research labs and at banks and governments preparing for post-quantum migration. India's National Quantum Mission funds hubs at IISc Bengaluru and IITs Madras, Bombay and Delhi (per DST and PIB). Much of the practical demand in the next few years is for PQC migration and resource estimation rather than for running production quantum algorithms (analysis).

**Interview questions from this course**

1. *Explain to a software engineer what a qubit is and why quantum computers are not just faster computers.* Strong answer: amplitudes and measurement; interference as the resource; exponential state space without exponential readout; limited known speed-ups (Shor exponential, Grover quadratic); noise.
2. *Will quantum computers break our encryption, and when?* Strong answer: Shor breaks RSA and ECC; symmetric and hash-based crypto survive with larger parameters; resource estimates (fewer than 1 million noisy qubits for RSA-2048 under 2025 assumptions); uncertainty about timelines; Mosca's inequality; migrate to ML-KEM/ML-DSA with hybrid deployment.
3. *What is quantum error correction and why is "below threshold" important?* Strong answer: redundancy without cloning; syndromes; surface code; threshold theorem; logical error falling with distance; overhead; decoding speed.
4. *A startup claims a quantum advantage for portfolio optimization. How do you evaluate it?* Strong answer: compare against the best classical solvers, not naive baselines; problem sizes; error mitigation costs; whether the instance is hard; dequantization; independent replication.
5. *Write a circuit that prepares a GHZ state on 5 qubits and verify it.* Strong answer: H plus CNOT chain or tree (log depth); measurement statistics; parity checks or fidelity witness; mapping to hardware connectivity.

## Resources (free first)

- **Courses and notes:** John Watrous, [Basics of Quantum Information (IBM Quantum Learning)](https://quantum.cloud.ibm.com/learning/en/courses/basics-of-quantum-information); Ronald de Wolf, [Quantum Computing: Lecture Notes](https://arxiv.org/abs/1907.09415); Scott Aaronson, [Introduction to Quantum Information Science notes](https://www.scottaaronson.com/qclec.pdf); MIT [8.370x Quantum Information Science I (OCW)](https://ocw.mit.edu/courses/8-370x-quantum-information-science-i-spring-2018/); NPTEL [Quantum Computing: Algorithms and Limitations through the Query Model](https://nptel.ac.in/courses/106104845) (IIT Kanpur) and [Quantum Algorithms and Cryptography](https://nptel.ac.in/courses/106106241) (IIT Madras); [Error Correction Zoo](https://errorcorrectionzoo.org/).
- **Software:** [Qiskit](https://github.com/Qiskit/qiskit) and [IBM Quantum documentation](https://quantum.cloud.ibm.com/docs/en/guides); [Cirq](https://quantumai.google/cirq); [PennyLane](https://pennylane.ai/); [Quirk](https://algassert.com/quirk); [Stim](https://github.com/quantumlib/Stim); [PyMatching](https://github.com/oscarhiggott/PyMatching); [Qualtran](https://github.com/quantumlib/Qualtran).
- **Papers:** [Shor (1995)](https://arxiv.org/abs/quant-ph/9508027); [Grover (1996)](https://arxiv.org/abs/quant-ph/9605043); [Quantum volume](https://arxiv.org/abs/1811.12926); [Tang (2018)](https://arxiv.org/abs/1807.04271); [Gidney–Ekerå (2019)](https://arxiv.org/abs/1905.09749); [Gidney (2025)](https://arxiv.org/abs/2505.15917); [Below-threshold surface code (2024)](https://www.nature.com/articles/s41586-024-08449-y); [AlphaQubit (2024)](https://www.nature.com/articles/s41586-024-08148-8); [Bivariate bicycle codes (2023)](https://arxiv.org/abs/2308.07915); [Qiskit HumanEval](https://arxiv.org/abs/2406.14712).
- **Paid, worth it:** Nielsen and Chuang, *Quantum Computation and Quantum Information* (10th anniversary ed.).

## Sources

All checked 12 Oct 2026.

- Google Quantum AI, "Quantum error correction below the surface code threshold", *Nature* (Dec 2024) — https://www.nature.com/articles/s41586-024-08449-y
- Quantum Computing Report, "Quantinuum launches Helios" (Nov 2025; figures company-reported) — https://quantumcomputingreport.com/quantinuum-launches-helios-quantum-computer-with-industry-leading-fidelity-and-singapore-partnership/
- IBM, Quantum Developer Conference 2025 blog (Nighthawk: 120 qubits, 218 couplers; Loon: qLDPC proof of concept) — https://www.ibm.com/quantum/blog/qdc-2025 ; IBM quantum roadmap (Starling, 200 logical qubits by 2029) — https://www.ibm.com/roadmaps/quantum.pdf
- Gidney, "How to factor 2048 bit RSA integers with less than a million noisy qubits" (May 2025) — https://arxiv.org/abs/2505.15917 ; Gidney and Ekerå (2019) — https://arxiv.org/abs/1905.09749
- DST, "Cabinet approves National Quantum Mission" (19 Apr 2023) — https://dst.gov.in/cabinet-approves-national-quantum-mission-scale-scientific-industrial-rd-quantum-technologies
- Google DeepMind and Google Quantum AI, "Learning high-accuracy error decoding for quantum processors" (AlphaQubit), *Nature* (Nov 2024) — https://www.nature.com/articles/s41586-024-08148-8
- "Qiskit HumanEval: An Evaluation Benchmark For Quantum Code Generative Models" (arXiv 2406.14712, Jun 2024) — https://arxiv.org/abs/2406.14712

_Last reviewed: 2026-10_
