# CSG302 · Compiler Construction

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 3 · 5 | 4 (≈ 120 hours) | L2 → L4 | [CS201](../../../../02_year_2_core_computer_science/semester_3/CS201_algorithms_and_complexity/README.md), [CS212](../../../../02_year_2_core_computer_science/semester_4/CS212_distributed_systems_i/README.md), [CS216](../../../../02_year_2_core_computer_science/semester_4/CS216_programming_languages_compilers_and_interpreters/README.md); draws on [CS202](../../../../02_year_2_core_computer_science/semester_3/CS202_computer_architecture_and_systems_programming/README.md) | [CSG402](../../year_4/CSG402_complexity_theory_and_theoretical_cryptography/README.md); recommended for [CSG404](../../year_4/CSG404_programming_language_theory_and_type_systems/README.md) and [CSG401](../../year_4/CSG401_formal_methods_and_program_verification/README.md); electives [MLE404](../../../machine_learning_engineering/year_4/MLE404_efficient_inference_quantization_distillation/README.md), [DLR404](../../../deep_learning/year_4/DLR404_efficient_deep_learning_and_gpu_programming/README.md) |

Part of the [Computer Science (Theory, Systems and Research) major](../../README.md). CS216 built interpreters, a bytecode VM, a type checker and a first look at SSA and LLVM IR. This course builds a real optimizing compiler to native code and teaches what production compilers do between the parser and the machine: SSA construction, dataflow analysis, optimization, instruction selection, register allocation, runtime interfaces, JITs, and compilers for AI hardware.

## Why this course matters now

Compilers are being rebuilt for new hardware and new speed targets. MLIR, a framework of reusable compiler "dialects", underlies many machine-learning compilers ([Lattner et al., CGO 2021](https://arxiv.org/abs/2002.11054)); PyTorch 2's `torch.compile` captures Python bytecode and generates GPU kernels through Triton ([ASPLOS 2024](https://pytorch.org/blog/pytorch-2-paper-tutorial/)); CPython has an experimental copy-and-patch JIT ([PEP 744](https://peps.python.org/pep-0744/)); TypeScript 7 is a native port of its compiler to Go ([Microsoft, Jul 2026](https://devblogs.microsoft.com/typescript/announcing-typescript-7-0/)). LLVM ships a new major release about every six months ([LLVM release process](https://llvm.org/docs/HowToReleaseLLVM.html)), and machine learning already guides some of its decisions (MLGO, [arXiv 2101.04808](https://arxiv.org/abs/2101.04808)). AI assistants can write a parser or a simple pass quickly, and research models such as Meta's LLM Compiler can emulate optimization passes ([arXiv 2407.02524](https://arxiv.org/abs/2407.02524)). But a compiler is code that writes code, so one wrong rewrite miscompiles millions of programs. Random-program testing found hundreds of bugs in GCC and LLVM ([Csmith, PLDI 2011](https://users.cs.utah.edu/~regehr/papers/pldi11-preprint.pdf)), and the verified middle-end of CompCert was the exception. The skill employers pay for is building passes that are fast *and* provably or measurably correct, and debugging the miscompilations that nobody else can find.

## Learning outcomes

By the end you can:

1. **Build** a complete compiler for a statically typed language (ChocoPy, a typed Python subset) to RISC-V or x86-64 assembly that runs on real hardware or QEMU.
2. **Construct** LR(1) parsing tables and **design** error recovery that reports useful messages for broken programs.
3. **Implement** semantic analysis with nested scopes, classes, subtyping and good diagnostics.
4. **Design** IRs and **construct** SSA form with dominance frontiers, then **leave** SSA correctly.
5. **Implement** dataflow analyses as monotone frameworks and **prove** termination and soundness.
6. **Implement** optimizations (SCCP, GVN, DCE, LICM, inlining) and **measure** their effect on benchmarks.
7. **Implement** instruction selection and graph-colouring or linear-scan register allocation under a real calling convention.
8. **Explain** JIT tiers, inline caches, speculation and deoptimization, and **build** a small JIT.
9. **Write** an LLVM pass and a small MLIR lowering, and **verify** peephole rewrites with Alive2.
10. **Find** miscompilations with differential testing, test-case reduction and pass bisection.

## Chapters and lessons

### Chapter 1 · Compiler architecture and the project language (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Real pipelines | Clang → LLVM IR → SelectionDAG/GlobalISel → MC; rustc's HIR and MIR; GCC's GIMPLE and RTL; V8's tiers | Trace one C function through Clang's `-emit-llvm`, `-O2` and assembly in Compiler Explorer |
| 1.2 The ChocoPy language | Static types, classes, single inheritance, lists, `None`, nested functions with `nonlocal` | Write 15 ChocoPy programs that exercise every feature, with expected output |
| 1.3 Testing a compiler | Golden tests, differential testing against an interpreter, test-case reduction (C-Reduce) | Set up the test runner and CI for your compiler repository |
| 1.4 Target machines | RV64 and x86-64 basics: registers, addressing, the calling convention (RISC-V psABI, System V AMD64) | Hand-write assembly for factorial; run it in QEMU |

**Check your understanding:** (1) Why do production compilers use several IRs instead of one? (2) What does differential testing catch that golden tests miss? (3) Which parts of a calling convention must a compiler obey exactly, and which are free choices?

### Chapter 2 · Lexing and parsing for real languages (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Lexer generation | Regular expressions → NFA → minimised DFA; indentation tokens (INDENT/DEDENT) for Python-like syntax | Generate a DFA lexer for ChocoPy including indentation |
| 2.2 LR(1) and LALR(1) | Item sets, closure and goto; canonical LR(1) vs LALR(1) merging; reduce/reduce conflicts | Lab 2: build LR(1) tables by hand for a 10-rule grammar, then with Bison or Menhir |
| 2.3 Ambiguity at scale | Precedence declarations; GLR and Earley parsing; C++'s "most vexing parse" | Resolve three conflicts in a ChocoPy grammar without changing the language |
| 2.4 Error recovery | Panic mode, error productions, Menhir's error messages; incremental parsing in editors | Make your parser report every syntax error in a 200-line broken file |

**Check your understanding:** (1) Why can LALR(1) introduce conflicts that canonical LR(1) does not? (2) When is GLR worth its cost? (3) Why do most production compilers still hand-write recursive-descent parsers?

### Chapter 3 · Semantic analysis (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Symbol tables | Nested scopes, `global` and `nonlocal`, forward references, class members | Implement scoping for ChocoPy's nested functions |
| 3.2 Type checking with subtyping | Typing rules, `object` as top type, join (least upper bound) for list literals and conditionals | Lab 3: a checker that passes the provided semantic test suite |
| 3.3 Diagnostics | Spans, notes, fix-it hints (Clang, rustc style); error cascades and how to stop them | Make one type error produce exactly one message |
| 3.4 Desugaring | Lowering `for` over lists, method calls, string operations to simpler forms before IR | Write the desugaring rules and test each one |

**Check your understanding:** (1) Why must semantic analysis finish before code generation can lay out objects? (2) What is the join of `[int]` and `None` in ChocoPy, and why? (3) How do you stop one undeclared variable from producing twenty errors?

### Chapter 4 · Intermediate representations (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Three-address code and CFGs | Basic blocks, terminators, critical edges and why they are split | Lower ChocoPy functions to a CFG; print it with Graphviz |
| 4.2 Memory vs registers | `alloca`/load/store form vs SSA values; `mem2reg` | Compile the same function both ways in LLVM and diff the IR |
| 4.3 LLVM IR in depth | Types, GEP, `undef` and `poison`, nsw/nuw flags, intrinsics, metadata | Explain every instruction of an `-O1` loop in LLVM IR |
| 4.4 MLIR and progressive lowering | Dialects (`arith`, `scf`, `memref`, `linalg`), operations, regions, lowering pipelines | Work through MLIR Toy tutorial chapters 1–3 |
| 4.5 Other IR designs | Cornell's Bril, Cranelift's CLIF, rustc MIR, sea-of-nodes (HotSpot C2, and why V8 moved away from it) | Write a one-page comparison of two IRs |

**Check your understanding:** (1) What can an optimizer assume about `poison` that it cannot about a normal value? (2) Why does LLVM split critical edges before some passes? (3) What does MLIR's multi-level design buy an ML compiler?

### Chapter 5 · SSA form (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Dominance | Dominators, immediate dominators, dominator trees; the Cooper–Harvey–Kennedy algorithm | Compute dominators for a 12-block CFG by hand and in code |
| 5.2 Placing φ-functions | Dominance frontiers; Cytron et al.; minimal, pruned and semi-pruned SSA | Lab 5: build SSA for your IR |
| 5.3 Renaming | Stack-based renaming over the dominator tree | Verify the SSA property with an automatic checker |
| 5.4 Simple SSA construction | Braun et al. (2013): building SSA directly from the AST | Implement it as an alternative and compare φ counts |
| 5.5 Leaving SSA | Copy insertion, the lost-copy and swap problems, parallel copies | Write test programs that break a naive out-of-SSA pass |

**Check your understanding:** (1) Why are φ-functions placed at the dominance frontier and not everywhere? (2) Why does a naive out-of-SSA translation fail on the swap problem? (3) What does SSA make cheap that was expensive before?

### Chapter 6 · Dataflow analysis (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Lattices and monotone frameworks | Partial orders, joins, height, transfer functions; Kildall's worklist algorithm | Prove termination for a lattice of finite height |
| 6.2 Classic analyses | Liveness (backward), reaching definitions (forward), available expressions; may vs must | Lab 6: a generic solver with three analyses |
| 6.3 Sparse conditional constant propagation | Wegman–Zadeck SCCP on SSA; executable-edge tracking | Implement SCCP; show it beats separate passes on one example |
| 6.4 Abstract interpretation | Interval domain, widening and narrowing; soundness vs precision | Bound loop variables with intervals; show where widening loses precision |
| 6.5 Interprocedural basics | Call graphs, context sensitivity (idea), summaries | Compute a call graph for your test programs |

**Check your understanding:** (1) Why must transfer functions be monotone for the worklist algorithm to terminate? (2) What does "sound" mean for a liveness analysis, and what goes wrong if it is unsound? (3) Why is widening necessary for intervals but not for constant propagation?

### Chapter 7 · Optimization (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Redundancy | Global value numbering, partial redundancy elimination (idea), aggressive DCE | Implement GVN on your SSA IR |
| 7.2 Loops | Natural loops, loop-invariant code motion with legality conditions, induction variables and strength reduction | Implement LICM; construct the case where hoisting a division is illegal |
| 7.3 Inlining | Cost models, call-site heuristics, code-size trade-offs; MLGO's learned inliner in LLVM | Measure code size and time with three inlining thresholds |
| 7.4 Memory and aliasing | Alias analysis basics, type-based aliasing, `restrict`; why C's rules matter | Show an optimization blocked by possible aliasing, then enabled by `restrict` |
| 7.5 Pass pipelines | Pass ordering, LLVM's new pass manager, `-O2` vs `-O3`; Lab 7: write an LLVM pass | Write a function pass that counts and removes a pattern; run it with `opt` |

**Check your understanding:** (1) Why is LICM unsafe for an instruction that may trap, even if it is loop-invariant? (2) Why can inlining make code faster and slower at the same time? (3) Why does the order of passes matter?

### Chapter 8 · Instruction selection and scheduling (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Tree tiling | Maximal munch; optimal tiling by dynamic programming | Tile three expression trees for RISC-V by hand |
| 8.2 DAG selection in LLVM | SelectionDAG, legalization, GlobalISel; TableGen patterns | Read one RISC-V TableGen pattern and explain it |
| 8.3 Emitting real code | Stack frames, prologue/epilogue, spills, globals, string constants, runtime calls | Lab 8: generate RISC-V for ChocoPy expressions and calls; run on QEMU |
| 8.4 Scheduling | Dependence DAGs, list scheduling, latency hiding; interaction with register pressure | Reorder a basic block to hide a load latency; count cycles in a simple model |

**Check your understanding:** (1) Why is optimal tiling easy on trees but hard on DAGs? (2) What does legalization do for a 64-bit operation on a 32-bit target? (3) Why do schedulers and register allocators fight?

### Chapter 9 · Register allocation (weeks 9–10)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Interference | Live ranges, interference graphs, precolored registers | Build interference graphs from your liveness results |
| 9.2 Graph colouring | Chaitin–Briggs: simplify, spill, select; optimistic colouring; spill-cost heuristics | Lab 9: a colouring allocator for your back end |
| 9.3 Coalescing | Aggressive vs conservative (Briggs, George) coalescing; copies from out-of-SSA | Measure moves removed by each coalescing rule |
| 9.4 Linear scan | Poletto–Sarkar linear scan; why JITs use it; second-chance binpacking | Implement linear scan; compare compile time and spills with colouring |
| 9.5 SSA-based allocation | Chordal interference graphs in SSA; decoupled spilling | Show that your SSA interference graphs are chordal on 10 functions |

**Check your understanding:** (1) Why is register allocation NP-hard in general but polynomial on SSA form? (2) Why does a JIT prefer linear scan? (3) What happens to callee-saved registers in your prologue, and why?

### Chapter 10 · Runtime systems (week 10)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Objects and dispatch | Object layout, vtables, method dispatch, `isinstance` checks | Lay out ChocoPy objects and implement dynamic dispatch |
| 10.2 Garbage collection interface | Roots, stack maps, safepoints; conservative vs precise collection | Emit stack maps for your compiler and plug in a simple mark-sweep collector |
| 10.3 Exceptions and errors | Runtime checks (null, bounds, division), unwinding tables (idea) | Make every runtime error report source line and type |
| 10.4 Linking and loading | Object files, ELF sections, relocations, static vs dynamic linking | Link your output against a C runtime library; inspect with `readelf` |

**Check your understanding:** (1) Why does a precise GC need help from the compiler? (2) Where should bounds checks go so that later passes can remove most of them? (3) What does a relocation record?

### Chapter 11 · Just-in-time compilation (weeks 11–12)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Tiered execution | Interpreter → baseline → optimizing tiers (V8 Ignition, Sparkplug, Maglev, TurboFan; HotSpot C1/C2) | Use V8 or JVM flags to watch a function move between tiers |
| 11.2 Inline caches and speculation | Hidden classes/shapes, monomorphic vs megamorphic sites, type feedback | Write a JavaScript benchmark that turns a call site megamorphic; measure |
| 11.3 Deoptimization and OSR | Guards, deopt points, on-stack replacement | Trigger and observe deoptimization with V8 tracing flags |
| 11.4 Copy-and-patch and tracing JITs | Copy-and-patch (Xu and Kjolstad, 2021) behind CPython's JIT; tracing in LuaJIT and PyPy | Lab 10: a tiny copy-and-patch or template JIT for a stack bytecode |
| 11.5 WebAssembly engines | Validation, baseline vs optimizing compilers, sandboxing guarantees | Compile a C function to Wasm and inspect it in a browser |

**Check your understanding:** (1) What does a JIT know that an ahead-of-time compiler does not, and what does it cost? (2) Why must every speculative optimization have a way back? (3) Why is copy-and-patch attractive for CPython specifically?

### Chapter 12 · Compilers for AI hardware, and compiler correctness (weeks 13–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 12.1 Tensor compilers | Graph capture, operator fusion, tiling for memory hierarchies; XLA, TorchInductor, Triton | Lab 11: write a fused softmax in Triton (or in MLIR `linalg` on CPU) and measure against unfused |
| 12.2 Testing by random programs | Csmith, YARPGen, equivalence modulo inputs; LLM-driven fuzzing in recent research | Lab 12: fuzz your compiler against its interpreter for 1 hour; reduce every failure |
| 12.3 Translation validation | Alive2 for LLVM peepholes; undefined behaviour and refinement | Verify five peephole rules in Alive2; find the one that is wrong |
| 12.4 Verified compilation | CompCert's proof structure; CakeML; what "verified" covers and what it does not | Read CompCert's correctness statement and list its trusted components |
| 12.5 Machine learning inside compilers | MLGO, LLM Compiler, learned cost models; where a learned heuristic is safe (choices among correct options) and where it is not (rewrites) | Write a one-page design for using an LLM in a compiler without risking wrong code |

**Check your understanding:** (1) Why is a learned inlining heuristic safe while a learned rewrite rule is not, without validation? (2) What does Alive2 prove about a rewrite, and what does it assume? (3) Why does fusing operators matter more on GPUs than on CPUs?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Compiler Explorer anatomy | Test harness and CI |
| 2 | 2 | Lab 2 · LR(1) tables and ChocoPy parser | Parser passes syntax tests |
| 3 | 3 | Lab 3 · Type checker | Semantic tests pass; **P1 starts** |
| 4 | 4 | Lab 4 · IR lowering | IR printer and Graphviz output |
| 5 | 5 | Lab 5 · SSA construction | SSA checker green; **P1 due** |
| 6 | 6 | Lab 6 · Dataflow and SCCP | Analysis results on benchmarks |
| 7 | 7 | Lab 7 · An LLVM pass | Mid-term (AI off); **P2 starts** |
| 8 | 8 | Lab 8 · RISC-V back end | First programs run on QEMU |
| 9 | 9 | Lab 9 · Register allocation | Spill statistics |
| 10 | 9–10 | Runtime and GC hook | **P2 due** |
| 11 | 11 | Lab 10 · A tiny JIT | — |
| 12 | 11 | JIT measurement | P3 feature freeze plan |
| 13 | 12 | Labs 11–12 · Triton and fuzzing | Fuzzing report |
| 14 | 12 | Alive2 and CompCert reading | **P3 due** |
| 15 | Review | Live extension oral | Final exam (AI off) |

## Working with AI in this course

- **Use AI for:** reading unfamiliar LLVM, MLIR or TableGen code ("what does this pattern match?"); generating ChocoPy test programs (valid and invalid) and expected outputs, which you check against the reference interpreter; boilerplate (IR printers, Graphviz output, CLI flags); explaining assembly listings; drafting Triton kernels you then benchmark and test.
- **Do without AI (drills):** LR(1) item sets; dominators, dominance frontiers and φ placement by hand; dataflow fixed points on paper; register colouring with spilling for a given graph; the SSA construction, SCCP and register-allocator code in your compiler; the mid-term and final.
- **Verify AI output by:** running the full golden suite and differential tests on every change; checking every proposed peephole or rewrite in Alive2 before accepting it; bisecting optimization passes (`-opt-bisect-limit` in LLVM, or your own pass counter) when outputs differ; fuzzing for an hour after any back-end change; reading the generated assembly for one hot function.
- **Where AI still fails here (show it):** ask two assistants for 10 "safe" peephole optimizations on integer and floating-point code, then check them in Alive2. Rules that ignore signed overflow, `poison`, NaN or signed zero are the typical failures. Ask for an out-of-SSA pass and run your swap-problem tests against it. Record each failure with the counterexample Alive2 or your tests produced.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (12) | 25% |
| Projects P1 / P2 / P3 | 5% / 15% / 25% |
| Mid-term (AI off): parsing tables, SSA, dataflow | 10% |
| Final exam (AI off) + live extension oral | 20% |

**Mastery gate.** You pass when you can, with AI off: (1) convert an unseen 8-block CFG to SSA, run SCCP by hand, and leave SSA correctly; (2) colour a given interference graph with k registers, choosing and justifying spills; (3) in a 2-hour live session, add a new language feature or optimization to your compiler, with tests, and show the full suite still passes; and (4) find a planted miscompilation in a classmate's optimizer using differential testing and reduction within 45 minutes.

## Industry reality

Compiler skills are hired by CPU, GPU and AI-accelerator vendors, by language teams (Swift, Rust, Go, TypeScript, Kotlin, Java), by browser engines (V8, SpiderMonkey, JavaScriptCore), by database companies (query compilation) and by ML framework teams (XLA, TorchInductor, Triton, MLIR-based stacks). Public examples: LLVM's six-month release cadence and MLGO; CPython's copy-and-patch JIT (PEP 744); PyTorch 2's compiler stack; TypeScript's Go port; V8's Maglev tier; RISC-V as an open target, including Indian designs such as IIT Madras's [Shakti](https://shakti.org.in/) processors.

**Interview questions from this course**

1. *What is SSA, and why do compilers use it?* Strong answer: single assignment, φ at merges; makes use-def chains explicit and cheap; enables sparse analyses (SCCP, GVN); construction via dominance frontiers; cost of leaving SSA (copies, swap problem).
2. *How does register allocation work, and what happens when you run out of registers?* Strong answer: liveness → interference → colouring or linear scan; spill-cost heuristics; coalescing; calling-convention constraints; why JITs choose linear scan.
3. *Is it safe to hoist this expression out of the loop?* Strong answer: loop-invariance, dominance of exits, possible traps (division, loads), aliasing with stores in the loop, exceptions; speculation and guarding.
4. *A program gives different output at `-O2` than at `-O0`. How do you find out who is wrong?* Strong answer: check for undefined behaviour first (sanitizers); reduce with C-Reduce; bisect passes; inspect IR before and after the culprit pass; validate the rewrite with Alive2; file a minimal bug report.
5. *How does a JavaScript engine make `obj.x` fast?* Strong answer: hidden classes/shapes, inline caches, monomorphic vs megamorphic, speculation with guards, deoptimization, tiered compilation.

## Resources (free first)

- **Courses:** [Cornell CS 6120 Advanced Compilers (self-guided)](https://www.cs.cornell.edu/courses/cs6120/2023fa/self-guided/) with the Bril IR; [Stanford CS143](https://web.stanford.edu/class/cs143/); [CMU 15-411 Compiler Design](https://www.cs.cmu.edu/~janh/courses/411/); [ChocoPy (Berkeley CS164 language and reference materials)](https://chocopy.org/); NPTEL [Compiler Design](https://nptel.ac.in/courses/106105190) (IIT Kharagpur).
- **Free books:** Møller and Schwartzbach, [Static Program Analysis](https://cs.au.dk/~amoeller/spa/); Jeremy Siek, [Essentials of Compilation](https://github.com/IUCompilerCourse/Essentials-of-Compilation).
- **LLVM and MLIR:** [Writing an LLVM pass (new pass manager)](https://llvm.org/docs/WritingAnLLVMNewPMPass.html); [LLVM Language Reference](https://llvm.org/docs/LangRef.html); [Kaleidoscope tutorial](https://llvm.org/docs/tutorial/MyFirstLanguageFrontend/index.html); [MLIR Toy tutorial](https://mlir.llvm.org/docs/Tutorials/Toy/); [Triton documentation](https://triton-lang.org/main/index.html).
- **Papers:** [A Simple, Fast Dominance Algorithm](https://www.cs.tufts.edu/comp/150FP/archive/keith-cooper/dom14.pdf); [Simple and Efficient Construction of SSA Form (Braun et al., 2013)](https://c9x.me/compile/bib/braun13cc.pdf); [Copy-and-Patch Compilation (Xu and Kjolstad, 2021)](https://arxiv.org/abs/2011.13127); [MLIR](https://arxiv.org/abs/2002.11054); [MLGO](https://arxiv.org/abs/2101.04808); [Meta LLM Compiler](https://arxiv.org/abs/2407.02524); [Csmith](https://users.cs.utah.edu/~regehr/papers/pldi11-preprint.pdf).
- **Tools:** [Compiler Explorer](https://godbolt.org/), [Alive2 online](https://alive2.llvm.org/ce/), [Csmith](https://github.com/csmith-project/csmith), [C-Reduce](https://github.com/csmith-project/creduce), [YARPGen](https://github.com/intel/yarpgen), [QEMU](https://www.qemu.org/), [RISC-V specifications](https://riscv.org/specifications/ratified/), [CompCert](https://compcert.org/), [Bison](https://www.gnu.org/software/bison/), [Menhir](https://gallium.inria.fr/~fpottier/menhir/).
- **Paid, worth it:** Cooper and Torczon, *Engineering a Compiler* (3rd ed.); Appel, *Modern Compiler Implementation in ML/Java/C*.

## Sources

All checked 12 Oct 2026.

- Lattner et al., "MLIR: Scaling Compiler Infrastructure for Domain Specific Computation" (CGO 2021) — https://arxiv.org/abs/2002.11054
- PyTorch, "PyTorch 2 paper and tutorial at ASPLOS 2024" — https://pytorch.org/blog/pytorch-2-paper-tutorial/
- PEP 744, JIT compilation — https://peps.python.org/pep-0744/ ; Xu and Kjolstad, "Copy-and-Patch Compilation" (OOPSLA 2021) — https://arxiv.org/abs/2011.13127
- Microsoft, "Announcing TypeScript 7.0" (8 Jul 2026) — https://devblogs.microsoft.com/typescript/announcing-typescript-7-0/
- LLVM, "How To Release LLVM To The Public" (release schedule) — https://llvm.org/docs/HowToReleaseLLVM.html
- Trofin et al., "MLGO: a Machine Learning Guided Compiler Optimizations Framework" — https://arxiv.org/abs/2101.04808
- Cummins et al., "Meta Large Language Model Compiler" (Jun 2024) — https://arxiv.org/abs/2407.02524
- Yang, Chen, Eide, Regehr, "Finding and Understanding Bugs in C Compilers" (PLDI 2011) — https://users.cs.utah.edu/~regehr/papers/pldi11-preprint.pdf
- Shakti processor programme, IIT Madras — https://shakti.org.in/

_Last reviewed: 2026-10_
