# CSG402 · Labs and projects

Proofs are written in LaTeX and submitted without AI help. Code is in Python (with SageMath where useful) for exploration and Rust or C for anything performance- or timing-sensitive. All cryptographic code in this course is for learning: it runs only against your own keys and test vectors, never against systems you do not own, and is never deployed. Every cryptographic implementation is checked against official test vectors.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Reductions checked by SAT | Implement 3-SAT → independent set, 3-SAT → 3-colouring and subset sum gadgets; verify on 1,000 random instances that answers are preserved | Reduction code, solver-based checks, a written proof for one reduction (AI off) | 5 h |
| 2 · TQBF | A recursive TQBF solver and a generalized-geography game solver | Runtime vs quantifier depth plot; explanation tied to PSPACE-completeness | 4 h |
| 3 · Primality | Miller–Rabin and AKS; error-probability experiment for Miller–Rabin with 1–10 rounds on Carmichael numbers | Timing up to 64-bit inputs; error table; a note on why AKS is a theoretical landmark | 4 h |
| 4 · Sum-check | Prover and verifier over a prime field for counting satisfying assignments of a small formula | Completeness tests; a cheating-prover experiment with measured catch rate vs field size | 5 h |
| 5 · Orthogonal vectors | Brute force and bit-packed OV; reduce small CNF-SAT instances to OV | Running-time plots and an extrapolation; the reduction verified on random instances | 4 h |
| 6 · Distinguishers | Break three weak PRGs (LCG, truncated LCG, a linear-feedback shift register) with statistical or algebraic distinguishers | Distinguisher code and advantage estimates with confidence intervals | 4 h |
| 7 · Game-based proofs and the AI audit (proof AI off) | Encrypt-then-MAC IND-CCA proof as a game sequence; grade two AI-generated proofs | Your proof; graded AI proofs with every flawed hop identified | 5 h |
| 8 · Signatures | Schnorr signatures over a prime-order group in your own toy code; show nonce reuse reveals the key; implement deterministic nonces | Code, the key-recovery derivation, and the fix | 4 h |
| 9 · Fiat–Shamir | Correct non-interactive Schnorr proof; a weak variant (statement not hashed) in your own code that accepts a forged proof | Both implementations and the forgery explained | 4 h |
| 10 · SNARK circuit | Merkle-tree membership proof in circom or arkworks | Circuit, constraint count, prove/verify times and proof size; a test that a wrong witness fails | 5 h |
| 11 · Lattices and LWE | LLL with fpylll on increasing dimensions; Regev encryption with chosen parameters; ML-KEM test vectors against a library | Reduction-quality plot; LWE decryption-failure rate vs noise; test-vector results | 6 h |

## Projects

### P1 · An interactive proof system you can run (L1, ~6 hours)

**Real-world inspiration:** sum-check is the core of many modern proof systems used for verifiable computation and SNARKs.

**What to build:** a library that runs the sum-check protocol for a multilinear polynomial given as an arithmetic circuit, with an honest prover, a verifier and three cheating provers (wrong claim at round 1, wrong polynomial at a middle round, adaptive cheating).

**Acceptance criteria:**
- Completeness: the verifier accepts the honest prover on 1,000 random instances.
- Soundness: for each cheating strategy, the measured acceptance rate is within the theoretical bound (rounds × degree / field size) across at least 10⁴ trials, for two field sizes.
- Verifier time and communication are measured and shown to be polylogarithmic in the size of the summed domain relative to the prover's work.
- A two-page write-up of the protocol and its soundness proof (AI off).

**Stretch goals:** use sum-check to verify a matrix multiplication claim; compare with Freivalds' check from CS201.

**What it proves to an employer:** you understand the machinery under modern proof systems, which ZK and verifiable-computation teams test for.

### P2 · A provable-security dossier for an authenticated encryption scheme (L2, ~15 hours)

**Real-world inspiration:** standards bodies and auditors expect a security argument with every new construction; AEAD schemes such as AES-GCM and ChaCha20-Poly1305 come with proofs in standard models.

**What to build:** (1) a written IND-CCA (and INT-CTXT) proof for encrypt-then-MAC built from a PRF-based stream cipher and a PRF-based MAC, as a sequence of games with explicit advantage bounds; (2) an implementation in Rust or C using a standard block cipher and HMAC; (3) a concrete-security calculation for realistic message volumes.

**Acceptance criteria:**
- The proof has numbered games; each hop names the assumption or argument (PRF security, MAC unforgeability, identical-until-bad) and states the advantage loss; a classmate's review finds no unjustified hop (review included).
- The implementation passes official test vectors for its primitives and a property test (decrypt(encrypt(m)) = m; any single-bit change in the ciphertext is rejected).
- A constant-time check: a timing test (dudect-style, at least 10⁶ measurements) shows no detectable dependence of tag verification on the position of the first mismatching byte.
- A concrete-security table: how many messages of what size can be encrypted under one key before the bound becomes meaningful, and why.

**Stretch goals:** mechanize one game hop in EasyCrypt; add nonce-misuse resistance (SIV construction) and adapt the proof.

**What it proves to an employer:** you can both prove and implement cryptography carefully, which is rare and valued by security and cryptography teams.

### P3 · Post-quantum or zero-knowledge, done properly (L3, portfolio-grade, ~30 hours)

Choose one track.

**Track A · ML-KEM from the standard.** Real-world inspiration: organisations are migrating to ML-KEM under NIST's FIPS 203. Implement ML-KEM-768 in Rust or C directly from FIPS 203 (NTT, sampling, compression, encapsulation and decapsulation with the implicit-rejection step).

**Track B · An "over 18" credential with zero-knowledge.** Real-world inspiration: Google's open-sourced Longfellow ZK for age assurance (2025). The scenario here is **illustrative**: an issuer signs a date of birth; the holder proves to a website that they are over 18 without revealing the date or the signature. Build it with circom or arkworks, including signature verification inside the circuit (or a simplified signature scheme, stated clearly).

**Acceptance criteria (Track A):**
- Passes all NIST ACVP test vectors for ML-KEM-768 key generation, encapsulation and decapsulation.
- Decapsulation of tampered ciphertexts follows the specification's implicit-rejection behaviour, shown by tests.
- Constant-time evidence: no secret-dependent branches or memory indices (checked with a tool such as Valgrind-based taint checking or a dudect-style test, method stated).
- Benchmarks against liboqs on the same machine (cycles or nanoseconds for each operation).
- A 6-page report: the Module-LWE assumption, how parameters relate to security levels, decryption-failure probability, and what the implementation does not protect against (for example, power side channels).

**Acceptance criteria (Track B):**
- Proof generation and verification work end to end; a wrong date, a forged signature or a reused proof bound to another session are all rejected by tests.
- Measured proving time, verification time, proof size and constraint count.
- A threat model: what the issuer, holder and verifier learn; replay and linkability; what the trusted setup (if any) trusts.
- A written argument for soundness and zero-knowledge at the level of the underlying proof system's guarantees, with the circuit constraints checked for under-constraint bugs (each input range explicitly constrained).

**Stretch goals:** Track A: add ML-DSA verification; Track B: unlinkability across presentations. Either: a short preprint or blog post with code.

**What it proves to an employer or lab:** you can take a standard or a research idea to correct, tested, honest code with a security argument, which is exactly what PQC-migration, ZK and cryptography-research teams look for.

## Feeds into

- [CSG403 Quantum Computing for Computer Scientists](../CSG403_quantum_computing_for_computer_scientists/README.md): Shor's algorithm and why lattices are believed to resist it.
- [CSG501 Frontier Seminar](../../year_5/CSG501_frontier_seminar_ai_for_mathematics_science/README.md): AI for theory, including AI-assisted lower-bound constructions and formal proofs.
- [OV07 Privacy Engineering](../../../../04_overlaps/OV07_privacy_engineering/README.md) and [SAR304 Applied Cryptography and PKI](../../../security_architecture/year_3/SAR304_applied_cryptography_and_pki_for_architects/README.md): applying ZK, MPC and PQC in products.
- [THS501 Thesis or Capstone I](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md): P3 is a thesis seed.
