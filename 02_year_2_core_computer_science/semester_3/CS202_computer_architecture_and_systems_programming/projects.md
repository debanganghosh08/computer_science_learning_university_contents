# CS202 · Labs and projects

All C work compiles with `-std=c23 -Wall -Wextra -Werror` (or `-std=c17` where your compiler lacks C23) and must be clean under AddressSanitizer, UndefinedBehaviorSanitizer and Valgrind unless a lab says otherwise. Use Linux on x86-64 or AArch64 (a VM, WSL2 or a cloud instance is fine).

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Data lab | Solve 15 bit-manipulation and float-encoding puzzles with a restricted operator set and an operation budget | Solutions passing the provided checker; 3 puzzles explained in prose | 4 h |
| 2 · Toolchain and strings | Build a multi-file project with Make; inspect `-E`, `-S`, `-c` outputs; replace an unsafe string module with a length-tracking one | Makefile, before/after code, ASan report showing the old bug and the clean new run | 4 h |
| 3 · Debugging and sanitizers | Find 8 planted bugs (overflow, use-after-free, double free, leak, uninitialised read, UB shift, signed overflow, data race) with gdb, Valgrind, ASan, UBSan, TSan; then ask an AI assistant for a string parser and audit it the same way | Bug log (symptom, tool, root cause, fix) and an "AI code audit" table | 5 h |
| 4 · C ↔ assembly | Hand-translate 6 functions to x86-64; reconstruct C from 4 listings; compare `-O0`, `-O2`, `-O3` | Annotated listings and a note on each optimisation you spotted | 4 h |
| 5 · Binary bomb | Defuse the phases of a provided binary using only gdb, `objdump` and reasoning | Inputs for each phase plus a short trace of how you found them | 5 h |
| 6 · RISC-V assembly | Write `strlen`, `memcpy`, a recursive Fibonacci and a bubble sort in RV64 assembly; run under QEMU user mode | Source, test script, and an instruction-count comparison with compiler output | 4 h |
| 7 · Pipelines in Ripes | Run 4 programs on Ripes' 5-stage processor with and without forwarding; reorder instructions to remove stalls | Cycle counts, pipeline diagrams, CPI before and after | 3 h |
| 8 · Cache simulator and transpose | Write a trace-driven cache simulator (sets, ways, LRU); then optimise a matrix transpose for minimum misses | Simulator passing reference traces; miss counts for each transpose version | 6 h |
| 9 · Linking and interposition | Build static and shared libraries; fix 3 link errors; write an `LD_PRELOAD` wrapper that logs allocation sizes | Explanations of each link error; a histogram of allocation sizes for `ls` and `git status` | 4 h |
| 10 · Profiling | Use `perf stat`, `perf record` and flame graphs to find and fix the hotspot in a provided image-processing program | Before/after flame graphs, counter table (IPC, cache misses, branch misses), speed-up with confidence interval | 4 h |

## Projects

### P1 · Varint codec with fuzzing (L1, ~6 hours)

**Real-world inspiration.** Protocol Buffers, the default message format of gRPC, encode integers as base-128 "varints" and use ZigZag encoding so small negative numbers stay short. The wire format is publicly documented: https://protobuf.dev/programming-guides/encoding/

**What to build.** A small C library and CLI: `varint_encode_u64`, `varint_decode_u64`, ZigZag `int64` variants, and length-prefixed records, with explicit error codes for truncated or over-long input.

**Acceptance criteria**
- Round-trip property holds for 10⁷ random values plus edge cases (0, 1, −1, `INT64_MIN`, `INT64_MAX`, `UINT64_MAX`).
- Byte-for-byte match with the provided reference test vectors from the Protocol Buffers encoding guide.
- Decoder rejects every malformed input in the provided corpus without reading out of bounds (ASan clean).
- 30 minutes of libFuzzer with ASan and UBSan finds no crash; the fuzz harness is in the repo.
- Throughput (MB/s) reported as the median of 10 runs with spread, on a stated CPU.

**Stretch goals.** A branch-reduced decoder and a measured comparison; a SIMD decoder for batches.

**What it proves to an employer.** You write C that handles hostile input safely, and you test it the way production parsers are tested.

### P2 · A general-purpose memory allocator (L2, ~15 hours)

**Real-world inspiration.** glibc malloc, jemalloc, tcmalloc and mimalloc are allocators whose design choices (size classes, free lists, per-thread caches) show up directly in the memory use and latency of large services.

**What to build.** `malloc`, `free`, `realloc` and `calloc` built on `mmap`/`sbrk`, with segregated free lists, boundary tags, immediate coalescing and 16-byte alignment, plus a `heap_check()` consistency checker. Package it as a shared library usable through `LD_PRELOAD`, protected by a global lock.

**Acceptance criteria**
- Passes every trace in the provided malloc-lab trace suite with `heap_check()` enabled after each operation.
- Reports space utilisation (peak payload ÷ peak heap) and throughput (operations per second) for each trace, next to glibc's numbers on the same machine.
- Runs `ls -lR /usr/include`, `git status` on a medium repository and `python3 -c "import json; json.dumps(list(range(10**6)))"` under `LD_PRELOAD` with correct output.
- Valgrind and ASan (on the test driver) show no invalid reads or writes in the allocator.
- The README explains the block layout with a diagram and justifies the size classes chosen.

**Stretch goals.** Per-thread caches and a multithreaded benchmark; large requests served directly by `mmap`; returning memory to the OS with `madvise`.

**What it proves to an employer.** You understand memory at the level that database, runtime and game-engine teams work at, and you can measure a design rather than guess.

### P3 · A RISC-V emulator that runs real C programs (L3, portfolio-grade, ~30 hours)

**Real-world inspiration.** QEMU, Spike (the RISC-V reference ISA simulator) and cycle-level simulators are how hardware teams test chips and how operating systems are brought up before silicon exists.

**What to build.** A user-mode RV64IM interpreter in C that loads a statically linked ELF built with a RISC-V cross-compiler, implements the `write`, `exit` and `brk` system calls, and executes the program. Add two analysis modes: an instruction trace, and an attached cache and branch-predictor model (reusing Lab 8) that reports hit and misprediction rates for the program it runs.

**Acceptance criteria**
- Passes every `rv64ui-p-*` and `rv64um-p-*` test from the official `riscv-tests` repository.
- Runs the provided C programs (quicksort, SHA-256, matrix multiply, a small interpreter) with output identical to QEMU user mode.
- Sustains at least 50 million emulated instructions per second on a stated machine, measured with a sound benchmark; the README shows one optimisation (for example, a decoded-instruction cache) with before/after `perf` counters.
- Clean under ASan and UBSan across the full test suite; malformed ELF files are rejected with an error, never a crash.
- The cache model's miss counts match the Lab 8 simulator on the same address trace.

**Stretch goals.** The A and C extensions; a GDB remote stub so `gdb` can debug programs inside your emulator; Sv39 page tables as a first step towards booting xv6 (used in [CS203](../CS203_operating_systems/README.md)).

**What it proves to an employer.** You understand an ISA end to end: encoding, execution, ABI, ELF loading and the memory system, and you can build and optimise a non-trivial C system. Compiler, embedded, hardware-verification and performance teams look for exactly this evidence.

## Feeds into

- [CS203 Operating Systems](../CS203_operating_systems/README.md): xv6 runs on RISC-V; page tables, traps and context switches build on Chapters 4, 5 and 9.
- [CS216 Programming Languages, Compilers and Interpreters](../../semester_4/CS216_programming_languages_compilers_and_interpreters/README.md): code generation targets the ISAs and calling conventions studied here.
- [CS213 Security Foundations](../../semester_4/CS213_security_foundations/README.md): memory-safety bug classes and their defences, from the defender's side.
- The Embedded Systems and IoT major: [EMB301](../../../03_majors/embedded_systems_iot/year_3/EMB301_microcontrollers_and_embedded_c/README.md), [EMB302](../../../03_majors/embedded_systems_iot/year_3/EMB302_real_time_operating_systems/README.md), [EMB305](../../../03_majors/embedded_systems_iot/year_3/EMB305_embedded_linux/README.md).
- [SWE305 Concurrency and Performance Engineering](../../../03_majors/software_engineering/year_3/SWE305_concurrency_and_performance_engineering/README.md): Chapter 10's measurement method is the starting point.
