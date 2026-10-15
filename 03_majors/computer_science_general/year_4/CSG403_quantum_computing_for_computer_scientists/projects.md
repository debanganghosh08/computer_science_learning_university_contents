# CSG403 · Labs and projects

Use Python with pinned versions of Qiskit, Cirq, Stim and PyMatching (record them in a lock file). Hardware runs use free cloud access (for example IBM Quantum's free plan; check its current monthly limits) and must be planned to fit within it: test on simulators first, then submit the smallest circuit that answers the question. Every hardware result states the device, date, calibration snapshot, shots and the error bars you computed.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Statevector simulator | A NumPy simulator for up to 10 qubits applying gates without building full matrices; measurement sampling | Code with unit tests against hand-computed states (AI off for the core apply-gate function) | 5 h |
| 2 · First hardware run | One- and two-qubit circuits on a simulator and on hardware | Counts, confidence intervals, and an explanation of each difference | 3 h |
| 3 · CHSH on hardware | Play the CHSH game with optimal angles | Win rate with a 95% interval vs 0.75 and 0.854; what noise did to it | 4 h |
| 4 · Stabilizer simulation | Simulate 1,000-qubit Clifford circuits in Stim; find where statevector simulation runs out of memory | Runtime and memory plots; one-paragraph explanation via Gottesman–Knill | 3 h |
| 5 · Query algorithms | Deutsch–Jozsa, Bernstein–Vazirani, Simon (n = 4) | Circuits, results, and classical query counts for comparison | 4 h |
| 6 · Grover | 3–5 qubit Grover with a marked-item oracle; success vs iterations on simulator and hardware | Plots showing the √N optimum and over-rotation; hardware degradation analysis | 4 h |
| 7 · Phase estimation | QPE for a T gate and a random single-qubit unitary at 3–6 precision qubits | Error vs precision qubits; success probability vs theory | 4 h |
| 8 · Noise budgets | Predict success probability from calibration data; compare with hardware; apply readout mitigation and ZNE | Prediction vs measurement table; variance cost of mitigation | 5 h |
| 9 · QAOA vs classical | QAOA depth 1–3 for MaxCut on 10 graphs vs Goemans–Williamson and exact solutions | Approximation ratios with error bars; a fair-comparison statement | 5 h |
| 10 · Surface code in Stim | Memory experiments at distances 3, 5, 7, 9 with circuit-level noise; decode with PyMatching | Logical error per round vs physical error rate; a threshold-crossing plot | 6 h |
| 11 · Transpilation and the AI audit | Transpile circuits for two coupling maps at several optimization levels; audit AI-written circuits under pinned versions | Depth and two-qubit counts; audit table of AI failures (API, qubit ordering, oracle phase) | 5 h |

## Projects

### P1 · A tested quantum simulator (L1, ~6 hours)

**Real-world inspiration:** every quantum SDK ships simulators, and their correctness underpins every algorithm study run on them.

**What to build:** extend Lab 1 into a small library: arbitrary single-qubit and controlled gates, measurement with collapse, mid-circuit measurement with classical feed-forward, and an import path from a Qiskit circuit.

**Acceptance criteria:**
- Agrees with Qiskit's statevector simulator to 10⁻¹⁰ (up to global phase) on 1,000 random circuits of 2–12 qubits.
- Teleportation with feed-forward produces the input state for 100 random inputs.
- A 20-qubit, 200-gate random circuit runs in under 60 seconds on a laptop (measured), with a note on memory use.
- Qubit-ordering convention documented and tested (Qiskit's little-endian ordering is a classic source of bugs).

**Stretch goals:** a density-matrix mode with depolarizing noise; GPU acceleration with CuPy.

**What it proves to an employer:** you understand exactly what quantum software computes, and you test it like production code.

### P2 · Shor's algorithm and an honest resource estimate (L2, ~15 hours)

**Real-world inspiration:** governments and banks use published resource estimates to decide how urgently to migrate to post-quantum cryptography.

**What to build:** (1) Shor's order-finding circuit with explicit modular multiplication for N = 15 and N = 21, run on a simulator, with classical post-processing by continued fractions; (2) a resource-estimate model (spreadsheet, Python or Qualtran) that reproduces the structure of a published RSA-2048 estimate and shows how the result moves when you change physical error rate, cycle time and code distance.

**Acceptance criteria:**
- Both N = 15 and N = 21 are factored; the measured success probability per run is compared with the theoretical probability, over at least 1,000 runs each.
- Gate counts, depth and qubit counts reported for each circuit, before and after transpilation.
- The resource model reproduces the published estimate's headline numbers within a factor of 2 when using the paper's stated assumptions (or explains precisely why not).
- A sensitivity table: physical qubits and run time when the physical error rate is 10× better or worse, and when cycle time doubles.
- A two-page brief for a non-specialist on what the estimate does and does not mean for RSA and ECC timelines, linked to the PQC standards from CSG402.

**Stretch goals:** run the N = 15 circuit (or a compiled variant) on hardware and analyse why it does or does not work; implement semiclassical QFT with mid-circuit measurement.

**What it proves to an employer:** you can connect the algorithm to the engineering and the policy question, which security and quantum-strategy teams need.

### P3 · An error-correction study (L3, portfolio-grade, ~30 hours)

**Real-world inspiration:** Google's 2024 below-threshold surface-code experiment, AlphaQubit's neural decoding and IBM's qLDPC work all rest on simulation and decoding studies of this kind.

**What to build:** a reproducible study of quantum memory with Stim and PyMatching. Choose one research question, for example: *How do code distance, measurement error and decoder choice change the logical error suppression factor Λ under circuit-level noise calibrated to published hardware numbers?* Optional extensions: a small neural decoder trained on Stim samples, or a comparison of a surface code with a published bivariate-bicycle memory at matched logical error rates.

**Acceptance criteria:**
- Memory experiments for distances 3–11 at no fewer than 6 physical error rates, with enough shots that each logical error rate has a stated confidence interval.
- A threshold estimate with uncertainty, and Λ (suppression per distance step of 2) at a noise level matching a published device, compared with the published value and the difference explained.
- At least two decoders compared (for example PyMatching with and without correlated matching, or MWPM vs your neural decoder) on accuracy and decoding time per round.
- Everything reproducible from one command with fixed seeds; raw data and plotting scripts published.
- An 8-page report in paper format: background, method, results, limitations (noise-model assumptions), and what the result implies for hardware requirements.

**Stretch goals:** run a small repetition-code experiment on real hardware and compare with your simulation; add leakage or correlated errors to the noise model.

**What it proves to an employer or lab:** you can do real quantum-error-correction research engineering, one of the most in-demand skills in quantum hardware companies.

## Feeds into

- [CSG501 Frontier Seminar: AI for Mathematics, Science and Theory](../../year_5/CSG501_frontier_seminar_ai_for_mathematics_science/README.md): AI decoders, AI for circuit design and quantum resource estimation as research topics.
- [CSG402 Complexity Theory and Theoretical Cryptography](../CSG402_complexity_theory_and_theoretical_cryptography/README.md): P2's brief links resource estimates to PQC migration.
- [THS501 Thesis or Capstone I](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md): P3 is a ready thesis seed.
