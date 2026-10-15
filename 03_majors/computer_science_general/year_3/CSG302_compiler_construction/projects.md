# CSG302 · Labs and projects

The course project is one compiler that grows every week, kept in a single repository with CI. Write it in Rust, OCaml, Java, Kotlin or C++ (your choice, fixed in week 1). Every lab adds tests to the shared suite; nothing is accepted if the whole suite does not pass. Performance claims use dynamic instruction counts (QEMU plugins or the Spike simulator) as well as wall-clock time, because instruction counts are reproducible across machines.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Compiler Explorer anatomy | Follow 3 C functions through Clang at `-O0`, `-O1`, `-O2`; name every transformation you can see | Annotated IR and assembly diffs; test harness and CI skeleton for your compiler | 4 h |
| 2 · LR(1) tables and the ChocoPy parser (tables AI off) | Build LR(1) and LALR(1) tables for a small grammar by hand; then a full ChocoPy parser with indentation handling and error recovery | Hand tables with one conflict explained; parser passing syntax tests; error output for 20 broken files | 6 h |
| 3 · Type checker | Scopes, `global`/`nonlocal`, classes, subtyping and joins; one-error-per-mistake diagnostics | Semantic test results; 10 diagnostics before/after improvement | 6 h |
| 4 · IR lowering | Desugar and lower to your CFG IR; Graphviz output | IR for every test program; round-trip interpreter for your IR that matches the reference outputs | 5 h |
| 5 · SSA construction (dominators AI off) | Dominators, frontiers, φ placement, renaming, out-of-SSA with parallel copies | SSA checker green on all programs; swap and lost-copy tests passing | 6 h |
| 6 · Dataflow and SCCP | Generic worklist solver; liveness, reaching definitions; SCCP on SSA | Analysis dumps; dynamic instruction counts before and after SCCP + DCE | 5 h |
| 7 · An LLVM pass | Out-of-tree new-pass-manager plugin that finds and rewrites one pattern; FileCheck tests | Plugin, lit tests, before/after IR on 5 programs | 5 h |
| 8 · RISC-V back end | Instruction selection by tiling, frames, calls, runtime calls; run under QEMU | All expression and call tests running natively | 6 h |
| 9 · Register allocation (colouring by hand AI off) | Chaitin–Briggs with conservative coalescing; then linear scan | Spill and move counts per program for both allocators; compile-time comparison | 7 h |
| 10 · A tiny JIT | Template or copy-and-patch JIT for a stack bytecode (from CS216's VM or a provided one) | Speed-up over the interpreter on 5 benchmarks; a write-up of what you would speculate on next | 5 h |
| 11 · Fused kernels | A fused softmax or layer-norm in Triton (GPU) or MLIR `linalg` lowered to loops (CPU) | Correctness tests against a reference; speed-up over the unfused version; profile | 4 h |
| 12 · Fuzzing and Alive2 | Fuzz your compiler against your IR interpreter for 1 hour; reduce failures; verify 5 peepholes in Alive2 | Bug list with reduced test cases and fixes; Alive2 results including one rejected rule and its counterexample | 5 h |

## Projects

### P1 · A dataflow framework on Bril (L1, ~6 hours)

**Real-world inspiration:** every optimizing compiler has a generic dataflow engine (LLVM, GCC, Cranelift); static analyzers such as Infer and the Clang Static Analyzer are built on the same lattice ideas.

**What to build:** a generic worklist dataflow solver for Cornell's Bril IR, parameterised by lattice, direction and transfer function, with three instances (liveness, reaching definitions, constant propagation) and a dead-code-elimination pass that uses liveness.

**Acceptance criteria:**
- Analyses agree with hand-computed results on 10 small programs you write, including loops and unreachable code.
- After your DCE + constant propagation, every Bril benchmark program produces identical output under `brili`.
- Total dynamic instruction count (`brili -p`) across the benchmark suite falls, and you report the per-program change.
- A one-page argument that each transfer function is monotone and the lattice has finite height.

**Stretch goals:** an interval analysis with widening; a sound "unused variable" linter built on liveness.

**What it proves to an employer:** you can implement analyses that compilers and static-analysis tools rely on, and argue they terminate and are sound.

### P2 · A verified peephole pass for LLVM (L2, ~15 hours)

**Real-world inspiration:** LLVM's InstCombine pass contains many local rewrites; Alive and Alive2 were created because hand-written rewrites were a recurring source of miscompilations.

**What to build:** an out-of-tree LLVM pass plugin with at least 15 peephole rewrites on integer and floating-point code (for example, algebraic identities, comparisons, bit tricks), each one verified with Alive2 before it is accepted, plus a small loop-invariant code motion for side-effect-free instructions.

**Acceptance criteria:**
- Every rewrite has an Alive2 proof (or a documented reason for its preconditions such as `nsw` or `nnan` flags); at least one candidate rule that Alive2 rejected is kept in the report with its counterexample.
- lit/FileCheck tests for every rewrite, including negative tests where the rewrite must not fire.
- Loaded with `opt -load-pass-plugin`, the pass leaves the output of 30 PolyBench/C kernels unchanged.
- Measured change in static and dynamic instruction count on those kernels, honestly reported even if small.
- A short note comparing your rules with what `-O2` already does (which rules are redundant and why).

**Stretch goals:** generate candidate rules with an AI assistant, filter them through Alive2 automatically, and report the acceptance rate; upstream a test case or fix to LLVM.

**What it proves to an employer:** you can contribute to a production compiler without breaking it, and you use formal tools rather than hope.

### P3 · An optimizing ChocoPy compiler to RISC-V (L3, portfolio-grade, ~30 hours beyond the labs)

**Real-world inspiration:** university compiler courses at Berkeley (ChocoPy), CMU (C0) and Stanford build full compilers because the integration is where the real lessons are. Industrial back ends for RISC-V (LLVM, GCC) are maintained by teams in many countries, and open RISC-V cores, including India's Shakti, need toolchains.

**What to build:** finish your compiler: full ChocoPy (classes, inheritance, lists, strings, nested functions) to RV64 assembly; SSA-based middle end with at least SCCP, GVN, aggressive DCE and LICM; graph-colouring register allocation with coalescing; a runtime with dynamic dispatch, bounds and null checks, and a mark-sweep GC using your stack maps.

**Acceptance criteria:**
- Passes at least 95% of a test suite of 300 or more programs (the public ChocoPy examples plus your own), with every failure listed and explained.
- Differential fuzzing: 10,000 generated well-typed programs produce identical output from your native code and your IR interpreter (generator written by you or adapted, seeds recorded).
- On a benchmark set of 10 programs, optimized builds execute at least 1.5× fewer dynamic instructions than your `-O0` builds, with a per-optimization breakdown.
- GC stress mode (collect at every allocation) passes the whole suite.
- Error messages for 20 invalid programs are judged clear by two classmates (rubric provided).
- A 6–8 page design document: IRs, pass pipeline and order, allocator design, runtime layout, testing strategy, known limitations.

**Stretch goals:** an alternative back end that emits LLVM IR, compared with yours on speed and compile time; a linear-scan mode for fast compiles; a tiered mode that interprets first and compiles hot functions.

**What it proves to an employer:** you can build and test a complete optimizing compiler, which compiler, language-runtime, database query-engine and ML-compiler teams treat as direct evidence.

## Feeds into

- [CSG404 Programming Language Theory and Type Systems](../../year_4/CSG404_programming_language_theory_and_type_systems/README.md): ChocoPy's typing rules become formal judgments, and soundness gets proved.
- [CSG401 Formal Methods and Program Verification](../../year_4/CSG401_formal_methods_and_program_verification/README.md): verify a pass or a translation step from P2 or P3.
- [CSG402 Complexity Theory and Theoretical Cryptography](../../year_4/CSG402_complexity_theory_and_theoretical_cryptography/README.md): constant-time code generation and side channels connect compilers to cryptographic implementations.
- [MLE404 Efficient Inference](../../../machine_learning_engineering/year_4/MLE404_efficient_inference_quantization_distillation/README.md) and [DLR404 Efficient Deep Learning and GPU Programming](../../../deep_learning/year_4/DLR404_efficient_deep_learning_and_gpu_programming/README.md): Lab 11 is the bridge to ML compilers.
- [THS501 Thesis or Capstone I](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md) and the [CSG flagship industry project](../../../../06_career_and_market_readiness/05_industry_projects/CSG_computer_science_general.md).
