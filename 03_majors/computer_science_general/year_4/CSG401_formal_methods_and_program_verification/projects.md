# CSG401 · Labs and projects

Every proof artifact builds in CI from a clean checkout with pinned tool versions (Lean toolchain file, Dafny and Verus versions, Rocq version). CI fails on `sorry`, `admit`, `assume` or `Admitted`, and prints the axioms each main theorem depends on. Statements of main theorems are written by you, without AI, and reviewed by a classmate before any proof work starts.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Property-based specifications | Specify a priority queue with Hypothesis or proptest properties and a model; find a planted bug | Properties, the shrunk counterexample, the fix | 3 h |
| 2 · Z3 | Prove bit-manipulation identities, solve a scheduling puzzle, find a counterexample to a wrong "optimization" | Z3 scripts and a paragraph per result | 4 h |
| 3 · CBMC and Kani | Find an out-of-bounds write in C with CBMC; prove panic-freedom of a Rust function with Kani | Counterexample traces; harnesses and results | 4 h |
| 4 · Model checking a mutex (formulas AI off) | Peterson's algorithm and a broken variant in Promela (SPIN) or TLA+ (TLC); safety and liveness | Models, LTL properties, the counterexample for the broken variant explained step by step | 5 h |
| 5 · Dafny | Binary search, insertion sort (sorted and permutation), and an integer square root | Verified code with no `assume`; a mutation test showing each spec rejects 5 buggy versions | 6 h |
| 6 · Verus | A fixed-capacity ring buffer with full functional specification | Verified Rust code; notes on every proof obligation that needed help | 6 h |
| 7 · Separation logic | List reversal and list append in VeriFast or Viper | Annotated, verified code; a paper proof of one step using the frame rule | 5 h |
| 8 · Lean basics | Natural Number Game worlds 1–4; list lemmas; a verified merge sort | Lean project with CI; `#print axioms` output for the sort theorem | 6 h |
| 9 · Rocq and Isabelle | Software Foundations *Basics*, *Induction*, *Lists*; one lemma in Isabelle with Sledgehammer | Completed exercise files; a comparison note | 5 h |
| 10 · Auditing AI proofs | Run an AI prover or assistant on 30 provided lemmas (some subtly mis-stated); audit every claimed success | Audit table: statement fidelity, axioms, banned tactics, changed definitions; success rate before and after audit | 5 h |

## Projects

### P1 · Verified algorithms with mutation-tested specifications (L1, ~6 hours)

**Real-world inspiration:** AWS and others use Dafny to verify components; a recurring lesson is that weak specifications let wrong code verify.

**What to build:** Dafny implementations of three algorithms from CSG301 or CS201 (for example, union-find with path compression's invariant, a heap's sift-down, and two-pointer deduplication of a sorted array), each with a full functional specification.

**Acceptance criteria:**
- All three verify with no `assume` or `{:axiom}`, under a stated Dafny version, in under 60 seconds total.
- A mutation suite of at least 10 buggy variants per algorithm, each rejected by the verifier (any that verify reveal a specification gap, which you then fix and report).
- Specifications reviewed by a classmate against an English description, with the review notes included.
- Compiled code passes a property-based test suite against a reference implementation.

**Stretch goals:** port one algorithm to Verus and compare proof effort; prove a complexity bound using a ghost counter.

**What it proves to an employer:** you can write specifications strong enough to matter, the most underrated skill in verification.

### P2 · Verifying a Rust component (L2, ~15 hours)

**Real-world inspiration:** the public effort to verify Rust's standard library with Kani and other tools, and Verus's use for systems code, show where industry wants Rust verification.

**What to build:** choose one: (a) the concurrent cache or ring buffer from your earlier work, or the CSG301 P2 flow checker, verified in Verus for functional correctness; or (b) a set of Kani proof harnesses and contracts for `unsafe` functions in an open-source crate (with the maintainers' licence respected), aiming at a contribution upstream.

**Acceptance criteria:**
- Track (a): every public function has `requires`/`ensures`; the main correctness theorem is stated in English and in Verus, and verifies under a stated version; no `assume` or `admit`.
- Track (b): at least 8 `unsafe` functions with contracts and harnesses; bounds stated for each; any bug found is reported responsibly to the maintainers.
- A comparison against fuzzing: run cargo-fuzz or proptest for 1 hour and report what each approach found.
- A report on proof effort (hours, lines of proof vs code) and what remains unverified.

**Stretch goals:** submit the harnesses to the Rust standard-library verification challenge or the crate; verify a concurrent component with Verus's ghost resources.

**What it proves to an employer:** you can bring verification to real systems code, which security, cloud and blockchain teams pay for.

### P3 · A mechanized correctness proof (L3, portfolio-grade, ~30 hours)

**Real-world inspiration:** CompCert proved a C compiler correct; AWS proved properties of Cedar in Lean; mathematicians now formalize research results in Lean, increasingly with AI help.

**What to build:** choose one track and agree the main theorem statement with the instructor in week 10.
- **Compiler track (Lean 4 or Rocq):** a compiler from an expression-and-statement language (with variables, `if` and `while`) to a stack machine, with a proof that compiled code produces the same final state as the source semantics (a simulation proof).
- **Protocol track (TLA+ plus Verus or Dafny):** refine your CSG303 commit or replication specification to an implementation-level specification, and verify the core state-machine code against it.
- **Mathematics track (Lean 4 + Mathlib):** formalize a non-trivial result from CSG301 or CSG402 (for example, a Chernoff bound used in a specific algorithm analysis, or a correctness theorem for an approximation algorithm), or contribute statements and proofs to Google DeepMind's Formal Conjectures or Mathlib through their review processes.

**Acceptance criteria:**
- The main theorem is stated in a single, readable file and matches the English statement approved in week 10 (a reviewer signs this off).
- CI builds the whole development from scratch; no `sorry`/`Admitted`/`assume`; the axiom report lists only the prover's standard axioms (or each extra axiom is justified).
- At least one *negative* check: a deliberately broken variant of the compiler, protocol or statement is shown to fail.
- An AI-assistance log: which lemmas AI tools proposed or proved, how each was audited, and the success rate. Every AI-proved lemma has its statement reviewed by you.
- A 6–8 page report: definitions, main theorem, proof architecture, trusted computing base, effort, what is not proved.

**Stretch goals:** add an optimization pass (constant folding) to the compiler and prove it preserves semantics; extract and run the verified compiler; get a contribution merged upstream.

**What it proves to an employer or lab:** you can produce a machine-checked guarantee for something real, and you can use AI to go faster without letting it lower the bar. This is a strong thesis and PhD-application artifact.

## Feeds into

- [CSG501 Frontier Seminar: AI for Mathematics, Science and Theory](../../year_5/CSG501_frontier_seminar_ai_for_mathematics_science/README.md): AI-assisted formalization at research scale.
- [CSG404 Programming Language Theory and Type Systems](../CSG404_programming_language_theory_and_type_systems/README.md): mechanized type soundness uses the same skills.
- [THS501 Thesis or Capstone I](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md) and the [CSG flagship industry project](../../../../06_career_and_market_readiness/05_industry_projects/CSG_computer_science_general.md): P3 is the verified component of the flagship.
