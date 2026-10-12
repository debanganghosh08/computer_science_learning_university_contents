# CS202 · Computer Architecture and Systems Programming in C

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 2 · 3 | 4 (≈ 120 hours) | L1 → L3 | [FND102](../../../01_year_1_foundations/semester_1/FND102_how_computers_work_bits_hardware/README.md), [FND111](../../../01_year_1_foundations/semester_2/FND111_programming_ii_object_oriented_and_typed/README.md) | [CS203](../CS203_operating_systems/README.md), [EMB301](../../../03_majors/embedded_systems_iot/year_3/EMB301_microcontrollers_and_embedded_c/README.md), [EMB302](../../../03_majors/embedded_systems_iot/year_3/EMB302_real_time_operating_systems/README.md), [EMB305](../../../03_majors/embedded_systems_iot/year_3/EMB305_embedded_linux/README.md) |

## Why this course matters now

Every language runtime, database, browser engine and AI inference server ends in machine code that hits caches, pipelines and page tables. The machines are changing: AWS reports that for three years running more than half of the new CPU capacity it added was its Arm-based Graviton (Dec 2025), and RISC-V International ratified the RVA23 profile for 64-bit application processors (Oct 2024). Memory safety has become an industry priority: Google reports memory-safety bugs fell from 76% of Android vulnerabilities in 2019 to under 20% in 2025 as new code moved to Rust, and the Linux kernel declared its Rust experiment a success in December 2025, while most of the kernel remains C. AI assistants explain assembly and write C quickly, but a well-known study found about 40% of Copilot-generated programs in security-relevant scenarios were vulnerable (Pearce et al.). The engineer who can read the generated assembly, explain undefined behaviour, find a use-after-free in minutes and prove a speed-up with hardware counters remains hard to replace.

## Learning outcomes

By the end you can:

1. **Predict** the result of integer and floating-point expressions in C, including overflow, conversions and rounding, and **explain** which ones are undefined behaviour.
2. **Write** C that is clean under `-Wall -Wextra -Werror`, AddressSanitizer, UndefinedBehaviorSanitizer and Valgrind, with documented ownership of every allocation.
3. **Debug** crashes and memory corruption with gdb, sanitizers and fuzzing, from a core dump to a root cause.
4. **Translate** between C and x86-64, AArch64 and RISC-V assembly, and **explain** the calling convention and stack frame of any function.
5. **Analyse** pipeline hazards, branch prediction and cache behaviour, and **compute** their effect on run time.
6. **Optimise** a memory-bound kernel (transpose, matrix multiply) for locality and **prove** the gain with `perf` counters.
7. **Explain** linking, loading, virtual memory and dynamic memory allocation well enough to build a working allocator.
8. **Measure** performance with a sound method (warm-up, variance, confidence intervals) and **reject** speed claims that lack it.

## Chapters and lessons

### Chapter 1 · Bits, integers and floating point (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Integers in C | Two's complement; `<stdint.h>` types; unsigned wrap-around vs signed overflow (undefined); integer promotions (`-1 < 0u` is false) | Predict 20 expressions, then check them with the compiler |
| 1.2 Bit manipulation | Masks, shifts (shifting by ≥ width is UB), isolating the lowest set bit, popcount | CS:APP-style data lab: bit puzzles with a restricted operator set |
| 1.3 IEEE 754 | Sign/exponent/fraction, round-to-nearest-even, NaN, ±∞, subnormals, cancellation | Decode 5 floats by hand; compare naive and Kahan summation over 10⁷ values |
| 1.4 Byte order and layout | Endianness, `htonl`, alignment and padding, portable serialisation | Hex-dump a struct; write a little-endian encoder that works on any host |

**Check your understanding:** Why does the C standard make signed overflow undefined but unsigned overflow defined, and what does that let the optimiser do? Why can summing floats in a different order change the answer? A struct has fields `char, int, char`: what is its size, and how would you shrink it?

### Chapter 2 · C as a systems language (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 The toolchain | Preprocess → compile → assemble → link (`gcc -E/-S/-c`); warnings and sanitizer flags; Make and CMake | Build a 3-file project; inspect the output of every stage |
| 2.2 Pointers and arrays | Pointer arithmetic, array decay, `sizeof` traps, `const`, pointer-to-pointer, function pointers | A generic dynamic array of `void *` with a `qsort` comparator |
| 2.3 Strings and buffers | NUL-terminated strings; why `strcpy`/`strncpy` mislead; `snprintf`; length-carrying string types | Rewrite an unsafe string module; prove it clean under ASan |
| 2.4 Structs, unions and C23 | Tagged unions, flexible array members; C23 (ISO/IEC 9899:2024): `nullptr`, `bool` keyword, `[[nodiscard]]`, `constexpr` objects, `#embed` | A tagged-union value type for a tiny JSON parser |

**Check your understanding:** Why does `sizeof(arr)` differ inside and outside the function that received it? What can go wrong when a header is included twice, and what prevents it? When is a function pointer table better than a `switch`?

### Chapter 3 · Memory, lifetimes and undefined behaviour (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Storage and ownership | Automatic, static and allocated storage; `malloc/calloc/realloc/free`; ownership rules written into APIs | Annotate who frees what in a small library |
| 3.2 The memory-bug zoo | Out-of-bounds write (CWE-787), use-after-free (CWE-416), double free, leaks, uninitialised reads, dangling stack pointers | Find and fix 8 planted bugs |
| 3.3 UB and the optimiser | Signed overflow, null dereference, strict aliasing, unsequenced modification; checks the compiler is allowed to delete | Show a check that exists at `-O0` and disappears at `-O2` on Compiler Explorer |
| 3.4 Debugging tools | gdb (breakpoints, watchpoints, `bt`, `x`), core dumps, Valgrind memcheck, ASan, UBSan, MSan | Catch one bug with each tool; compare speed and report quality |
| 3.5 Fuzzing | Coverage-guided fuzzing with libFuzzer or AFL++ plus sanitizers | Fuzz your JSON parser for 30 minutes; fix every crash |

**Check your understanding:** Why can a use-after-free "work" in testing and fail in production? Why are sanitizers not a proof that code is memory-safe? Give one UB that a sanitizer catches and one it cannot.

### Chapter 4 · Machine-level programs on x86-64 (weeks 4–5)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 The ISA as a contract | Registers `rax`…`r15`, operand forms, `mov`, `lea`, arithmetic; AT&T vs Intel syntax | Hand-translate 5 C functions; compare with real compiler output |
| 4.2 Control flow | Condition codes, `cmp`/`test`, conditional jumps, `cmov`, loops, jump tables for `switch` | Reconstruct C source from 4 assembly listings |
| 4.3 Procedures | System V AMD64 ABI: argument registers, caller/callee-saved, stack frames, red zone | Step through recursion in gdb and draw every frame |
| 4.4 Data in assembly | Arrays, structs, alignment, scaled-index addressing | Binary-bomb style lab: reverse-engineer a provided binary's phases in gdb |
| 4.5 Stack smashing and its defences | Why an overflowing buffer can overwrite a return address; canaries, NX, ASLR, shadow stacks (concepts only) | Watch the stack canary abort your own buggy program; explain each defence |

**Check your understanding:** Why does the compiler use `lea` for arithmetic that has nothing to do with addresses? Which registers must a function restore before returning, and why does the ABI split them? Why do canaries stop some overflows but not an out-of-bounds write to a heap object?

### Chapter 5 · AArch64, RISC-V and ISA design (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 RISC vs CISC | Load/store design, fixed-length encodings; RISC-V RV64I and the M, A, F, D, C, V extensions; profiles such as RVA23 | Write `strlen` and `memcpy` in RISC-V assembly; run in QEMU |
| 5.2 AArch64 | 31 general registers, AAPCS64 calling convention, conditional select | Compile one C file for x86-64, AArch64 and RISC-V; compare instruction counts |
| 5.3 Instruction encoding | RISC-V R/I/S/B/U/J formats; decoding immediates | Write a decoder for 20 RV64I instructions (the seed of P3) |
| 5.4 Memory ordering | x86-TSO vs Arm's weaker model; C11 atomics, acquire/release | Run the message-passing litmus test in `herd7` for both models |

**Check your understanding:** Why does fixed-length encoding make decoding cheaper? Code that "always worked" on x86 breaks on Arm under load: what class of bug is likely? What does a profile like RVA23 buy software distributors?

### Chapter 6 · Processor design and pipelining (weeks 7–8)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Datapath and performance | Single-cycle RISC-V datapath; the "iron law": time = instructions × CPI × cycle time | Compute speed-ups for 5 design changes |
| 6.2 The five-stage pipeline | IF/ID/EX/MEM/WB; data hazards, forwarding, load-use stalls | Draw pipeline diagrams in the Ripes simulator; confirm stall counts |
| 6.3 Branches | Control hazards, 2-bit predictors, branch target buffers, misprediction cost, branchless code | Sum a sorted vs an unsorted array; measure `branch-misses` with `perf` |
| 6.4 Beyond one pipeline | Superscalar and out-of-order execution (renaming, reorder buffer), SIMD (AVX, NEON, RVV), Spectre as a lesson in speculation leaking through caches (concept and mitigations) | Auto-vectorise a loop; confirm with the compiler's vectorisation report |

**Check your understanding:** Why does a deeper pipeline raise the cost of a mispredicted branch? Forwarding removes most data stalls; which one can it not remove, and why? Why can an out-of-order core run a loop faster than its instruction count suggests?

### Chapter 7 · The memory hierarchy and caches (weeks 8–9)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Locality and latency | Registers, L1/L2/L3, DRAM, SSD; temporal and spatial locality | Pointer-chasing benchmark that reveals your cache sizes |
| 7.2 Cache organisation | Direct-mapped and set-associative caches; tag/index/offset; compulsory, capacity and conflict misses; write-back, LRU | Write a trace-driven cache simulator (CS:APP cache lab style) |
| 7.3 Cache-aware code | Loop interchange, blocking/tiling, struct-of-arrays vs array-of-structs | Optimise matrix transpose for minimum misses in the simulator |
| 7.4 Multicore memory | Coherence (MESI), false sharing, NUMA | Show false sharing with two threads; fix it with padding and `alignas` |

**Check your understanding:** Why can a 2× larger array make a loop 10× slower? Given a 32 KiB, 8-way cache with 64-byte lines, how many sets are there and which address bits pick the set? Why does false sharing not change the program's result, only its speed?

### Chapter 8 · Linking and loading (week 10)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Object files and ELF | Sections, symbol tables, strong and weak symbols; `readelf`, `objdump`, `nm` | Diagnose and fix a duplicate-symbol link error |
| 8.2 Static linking | Relocation, archives, why link order matters | Build a static library; reproduce and explain a link-order failure |
| 8.3 Dynamic linking | Shared objects, position-independent code, PLT/GOT, lazy binding, `ldd` | Build a `.so`; watch lazy binding resolve in gdb |
| 8.4 Interposition | `LD_PRELOAD` wrappers for profiling and testing | Count every allocation made by `ls` with a `malloc` wrapper |

**Check your understanding:** Why do shared libraries need position-independent code? Two libraries define the same symbol: which wins, and how could that bite you? What does lazy binding save, and what does it cost?

### Chapter 9 · Virtual memory and dynamic allocation (weeks 11–12)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Address translation | Pages, four-level x86-64 page tables, TLB, page faults, `mmap`, `/proc/self/maps` | Map a file with `mmap`; measure TLB misses with and without huge pages |
| 9.2 Protection and sharing | Page permissions, copy-on-write, shared library pages | Count page faults after `fork` with `perf stat` |
| 9.3 Allocator design | Implicit and explicit free lists, segregated fits, boundary tags, coalescing, fragmentation, alignment | Malloc lab: a correct allocator that passes the trace suite |
| 9.4 Production allocators | Size classes and per-thread caches in jemalloc, tcmalloc and mimalloc | Swap allocators with `LD_PRELOAD`; benchmark a multithreaded workload |

**Check your understanding:** Why does a TLB miss cost more with bigger page tables, and how do huge pages help? Why does `fork` not copy the parent's memory? What trade-off does every allocator make between speed and fragmentation?

### Chapter 10 · Performance engineering and safer systems code (weeks 13–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Benchmarking method | Warm-up, run-to-run variance, frequency scaling, CPU pinning, confidence intervals; `hyperfine` | Decide, with statistics, which of two implementations is faster |
| 10.2 Profiling | `perf stat/record/report`, IPC, cache and branch counters, flame graphs | Find and fix the hotspot in a provided program |
| 10.3 Performance models | Amdahl's law; the Roofline model (arithmetic intensity) | Place your matrix multiply on a roofline for your CPU |
| 10.4 Memory safety in practice | Rust ownership as compile-time checking; hardware tagging (Arm MTE), CHERI capabilities; when C is still the right tool | Port one buggy C module to Rust; compare bugs found at compile time |

**Check your understanding:** A change makes a benchmark 3% faster once. What must you do before believing it? Why can a memory-bound kernel not benefit from more SIMD width? What does Rust's borrow checker prevent that ASan only detects?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Data lab | — |
| 2 | 2 | Lab 2 · Toolchain and strings | — |
| 3 | 3 | Lab 3 · Debugging and sanitizers | Bug-hunt report |
| 4 | 4 | Lab 4 · C ↔ assembly | — |
| 5 | 4 | Lab 5 · Binary bomb | **P1 due** |
| 6 | 5 | Lab 6 · RISC-V assembly | P3 proposal |
| 7 | 6 | Lab 7 · Pipelines in Ripes | — |
| 8 | 6–7 | — | Mid-term (AI off) |
| 9 | 7 | Lab 8 · Cache simulator and transpose | — |
| 10 | 8 | Lab 9 · Linking and interposition | — |
| 11 | 9 | Malloc lab (P2) starts | — |
| 12 | 9 | — | **P2 due** |
| 13 | 10 | Lab 10 · Profiling | — |
| 14 | 10 | — | **P3 due** |
| 15 | Review | Oral defence of P3 | Final exam (AI off) |

## Working with AI in this course

- **Use AI for:** explaining an unfamiliar instruction or ABI rule; annotating a compiler listing line by line; decoding gdb, Valgrind and sanitizer reports; writing Makefiles and test drivers; summarising sections of the Intel, Arm or RISC-V manuals (then reading the cited section yourself).
- **Do without AI (drills):** bit puzzles; translating C ↔ assembly by hand; pipeline and stack-frame diagrams; splitting addresses into tag/index/offset; tracing an allocator's free list on paper. Exams test these.
- **Verify AI output by:** compiling with `-Wall -Wextra -Werror`; running ASan, UBSan and Valgrind; fuzzing parsers; checking the real assembly on Compiler Explorer for the exact compiler, version and flags; measuring every claimed speed-up with `perf stat` over repeated runs.
- **Where AI still fails here:** Pearce et al. generated 1,689 programs with GitHub Copilot across 89 security-relevant scenarios and judged about 40% vulnerable; the assistants have improved since, so in Lab 3 you test today's tool yourself: ask it for string-handling and parsing code, then run sanitizers and a fuzzer and log every defect. Expect claims like "this is faster" without measurement; your rule is no number, no claim.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (10) | 25% |
| Projects P1–P3 | 35% |
| Mid-term (AI off) | 10% |
| Final exam (AI off) + P3 oral defence | 30% |

**Mastery gate.** You pass when you can, without AI: (1) take a crashing C program you have never seen and find the root cause with gdb and sanitizers within 30 minutes; (2) explain, line by line, the x86-64 or RISC-V assembly of a 20-line C function including its stack frame; (3) improve a provided memory-bound kernel by at least 2× and prove it with hardware counters and a sound benchmark.

## Industry reality

Where this is used (public sources): Android's shift of new code to memory-safe languages and its measured fall in memory-safety vulnerabilities (Google, Nov 2025); the Linux kernel, mostly C, with Rust now a permanent part after the December 2025 Maintainers Summit (LWN); Arm servers at cloud scale (AWS Graviton5 announcement, Dec 2025); the RISC-V RVA23 profile, which fixes a common baseline (including vector and hypervisor extensions) for 64-bit application processors (RISC-V International, Oct 2024). Heartbleed (CVE-2014-0160) was a buffer over-read in OpenSSL's C code, a reminder of what one missing bounds check costs. Embedded, firmware, game engines, databases, browsers, trading systems and ML inference runtimes all hire people who can work at this level.

**Interview questions from this course**

1. *Walk me through what happens when you call `malloc(24)` and later `free` that pointer.* Strong answer: size-class rounding and alignment; header or size-class metadata; free lists or bins; per-thread caches; `brk` vs `mmap` for large requests; fragmentation and why `free` needs no size.
2. *Why is summing this array 5× faster after sorting it?* Strong answer: branch misprediction on a data-dependent `if`; pipeline flush cost; shows `perf stat` branch-miss counts; fixes with branchless code or `cmov`, and notes that compilers may already do it at `-O2`.
3. *What happens on a page fault?* Strong answer: TLB miss → page walk → not present → trap to kernel → find the mapping → allocate a zeroed page, read from file or copy-on-write → update the page table → restart the instruction; minor vs major faults; when it becomes a segmentation fault.
4. *Can `if (x + 1 > x)` ever be false in C?* Strong answer: for signed `int`, overflow is undefined, so the compiler may fold it to true; for unsigned it can be false at `UINT_MAX`; mentions `-fwrapv`, UBSan, and `__builtin_add_overflow` or C23 `ckd_add`.
5. *Two threads update separate counters and scaling is terrible. Why?* Strong answer: false sharing on one 64-byte cache line; coherence traffic; detects it with `perf c2c`; fixes with padding or per-thread counters merged later.

## Resources (free first)

- **Course spine:** CMU 15-213 Introduction to Computer Systems — https://www.cs.cmu.edu/~213/ ; 15-213 lab descriptions (based on the free CS:APP student labs) — https://www.cs.cmu.edu/~213/labs.html
- **Architecture:** MIT 6.004 Computation Structures (OCW) — https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/ ; NPTEL Computer Architecture (Madhu Mutyam, IIT Madras) — https://nptel.ac.in/courses/106106134
- **C:** Jens Gustedt, *Modern C* (free, covers C23) — https://gustedt.gitlabpages.inria.fr/modern-c/ ; Beej's Guide to C Programming — https://github.com/beejjorgensen/bgc ; C23 final working draft N3220 — https://www.open-std.org/jtc1/sc22/wg14/www/docs/n3220.pdf
- **Undefined behaviour:** John Regehr, "A Guide to Undefined Behavior in C and C++" — https://blog.regehr.org/archives/213 ; Chris Lattner, "What Every C Programmer Should Know About Undefined Behavior" — https://blog.llvm.org/2011/05/what-every-c-programmer-should-know.html
- **ISAs and ABIs:** RISC-V ratified specifications — https://riscv.org/specifications/ratified/ ; x86-64 System V psABI — https://gitlab.com/x86-psABIs/x86-64-ABI ; Intel SDM — https://www.intel.com/content/www/us/en/developer/articles/technical/intel-sdm.html
- **Memory and performance:** Ulrich Drepper, "What Every Programmer Should Know About Memory" (2007) — https://akkadia.org/drepper/cpumemory.pdf ; Agner Fog's optimisation manuals — https://www.agner.org/optimize/ ; Brendan Gregg, FlameGraph tools — https://github.com/brendangregg/FlameGraph
- **Tools:** Compiler Explorer — https://godbolt.org/ ; Ripes RISC-V simulator — https://github.com/mortbopet/Ripes ; QEMU — https://www.qemu.org/docs/master/ ; GDB — https://sourceware.org/gdb/documentation/ ; Valgrind — https://valgrind.org/docs/manual/manual.html ; AddressSanitizer — https://clang.llvm.org/docs/AddressSanitizer.html ; UBSan — https://clang.llvm.org/docs/UndefinedBehaviorSanitizer.html ; libFuzzer — https://llvm.org/docs/LibFuzzer.html ; herd7 memory-model simulator — https://diy.inria.fr/
- **Paid, optional:** Bryant and O'Hallaron, *Computer Systems: A Programmer's Perspective*, 3rd ed. (the textbook behind 15-213); Patterson and Hennessy, *Computer Organization and Design, RISC-V Edition*.

## Sources

- AWS, "AWS Introduces Graviton5" (Business Wire, 3 Dec 2025) — https://www.businesswire.com/news/home/20251203228412/en/AWS-Introduces-Graviton5the-Companys-Most-Powerful-and-Efficient-CPU (checked 2026-10)
- RISC-V International, "RISC-V Announces Ratification of the RVA23 Profile Standard" (Oct 2024) — https://riscv.org/blog/risc-v-announces-ratification-of-the-rva23-profile-standard/ (checked 2026-10)
- Google Security Blog, "Eliminating Memory Safety Vulnerabilities at the Source" (25 Sep 2024; 76% of Android vulnerabilities were memory-safety issues in 2019) — https://security.googleblog.com/2024/09/eliminating-memory-safety-vulnerabilities-Android.html (checked 2026-10)
- Google, "Rust in Android: move fast and fix things" (13 Nov 2025; below 20% in 2025) — https://blog.google/security/rust-in-android-move-fast-fix-things/ (checked 2026-10)
- LWN.net, "The (successful) end of the kernel Rust experiment" (Dec 2025) — https://lwn.net/Articles/1050174/ (checked 2026-10)
- Pearce et al., "Asleep at the Keyboard? Assessing the Security of GitHub Copilot's Code Contributions" (arXiv 2108.09293; IEEE S&P 2022) — https://arxiv.org/abs/2108.09293 (checked 2026-10)
- NVD, CVE-2014-0160 (Heartbleed) — https://nvd.nist.gov/vuln/detail/CVE-2014-0160 (checked 2026-10)
- ISO/IEC 9899:2024 (C23) — https://www.iso.org/standard/82075.html (checked 2026-10)

_Last reviewed: 2026-10_
