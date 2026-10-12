# FND102 · Labs and projects

Measurement rule for every lab: state a prediction before you measure, run each experiment at least 10 times, report the median and the spread (min–max or interquartile range), and record the machine (`lscpu`, OS, Python version). A number without these is not accepted.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Bits by hand | Fluency with bases, two's complement, overflow | 40 conversions done by hand, checked in Python; the exact Y2038 overflow timestamp with your code | 3 h |
| 2 · Bytes in files | See that every format is bytes | Notebook decoding a PNG header, a UTF-8 file containing "₹ नमस्ते", and a WAV header with `xxd` and `struct` | 3 h |
| 3 · Logic gates | nand2tetris Project 1 | 15 chips passing all supplied tests, plus one extra test script you wrote | 5 h |
| 4 · ALU | Project 2 | Adders and ALU passing tests; a table of control bits for 6 ALU functions you derived | 5 h |
| 5 · Memory | Project 3 | Bit through RAM16K and PC passing tests; a hand trace of 8 PC cycles | 5 h |
| 6 · Assembly | Project 4 | `Mult.asm` and `Fill.asm` passing tests; cycle count for 3 × 2 and 7 × 9 | 4 h |
| 7 · The computer | Project 5 | CPU and Computer passing all tests; a datapath diagram you drew | 6 h |
| 8 · Cache locality | Measure the memory hierarchy | Row- vs column-major results in C, pure Python and NumPy; a chart and a 300-word explanation | 3 h |
| 9 · Processes and syscalls | Observe the OS | `strace -c` summary for 3 programs, a `fork`/`wait` program, a zombie captured in `ps` output | 3 h |
| 10 · Files and durability | Inodes, links, buffering | Link experiments explained; timing of buffered vs flushed vs `fsync` writes for 10⁶ lines | 3 h |

## Projects

### P1 · `bitlens`: a byte-level inspector (L1, ~6 hours)

**Real-world inspiration.** Encoding bugs (mojibake in names, broken ₹ signs in invoices) and float bugs in billing are routine production issues. Engineers debug them with hex dumps and by decoding the exact bits.

**What to build.** A Python CLI:
- `bitlens int -5 --bits 8` shows binary, hex, unsigned reading and overflow behaviour.
- `bitlens float 0.1` shows sign, exponent and fraction fields, the exact stored value (`Decimal(0.1)`), and the gap to the next float (`math.ulp`).
- `bitlens text "₹ नमस्ते"` shows each character's code point, Unicode name (`unicodedata`) and UTF-8 bytes.

**Acceptance criteria**
- Float decoding agrees with `struct.pack('>d', x)` for 1,000 random values plus NaN, ±inf, −0.0, the smallest subnormal and the largest finite double.
- Integer output is correct for widths 8, 16, 32 and 64, including the most negative value of each.
- UTF-8 output matches `str.encode('utf-8')` for ASCII, Devanagari, Bengali, the ₹ sign and an emoji.
- ≥ 30 `pytest` tests; README with three worked examples and their explanation.

**Stretch goals.** Show the same float as IEEE 754 half precision (`struct` format `e`) and explain what is lost; detect and explain likely mojibake (UTF-8 bytes decoded as Latin-1).

**What it proves to an employer.** You can look beneath an abstraction and explain exactly what the machine stores.

### P2 · Hack toolchain: assembler, disassembler and emulator (L2, ~15 hours)

**Real-world inspiration.** Every platform needs a toolchain: assemblers such as GNU `as` and LLVM's integrated assembler, and emulators such as QEMU that run one machine's code on another.

**What to build.** In Python: (1) a two-pass Hack assembler (nand2tetris Project 6); (2) a disassembler from `.hack` back to readable assembly; (3) a Hack CPU emulator that runs a `.hack` file for N cycles and prints a register and memory trace.

**Acceptance criteria**
- Assembler output is byte-identical to the official assembler for `Add`, `Max`, `Rect` and `Pong`.
- Disassembling then reassembling any test program reproduces the same binary.
- The emulator's final RAM state matches the official CPU emulator for `Mult` (5 input pairs) and the first 10,000 cycles of `Fill`.
- ≥ 50 tests; a README that explains symbol resolution and shows one trace.

**Stretch goals.** A RISC-V RV32I subset assembler whose output runs in Ripes; a cycle counter that compares `Mult` with a shift-and-add version you write.

**What it proves to an employer.** You understand how text becomes executable bits, and you can build a tool that must agree exactly with a reference implementation.

### P3 · "From NAND to a running program" portfolio (L3, portfolio-grade, ~30 hours)

**Real-world inspiration.** Engineering deep-dive posts, such as Cloudflare's incident write-ups and Julia Evans's systems zines, explain a system by showing evidence from real tools. Performance work in industry follows the same discipline: hypothesis, controlled measurement, explanation.

**What to build.** A public repository with three parts:
1. **The computer:** nand2tetris Projects 1–6 complete, with a top-level README and a hand-drawn or Excalidraw diagram of your CPU datapath.
2. **The explainer:** "What happens when you run a program on Linux", up to 2,500 words, tracing `./hello` (C) and `python3 hello.py` from Enter to prompt, with captured evidence (`strace -f`, `ltrace` or `LD_DEBUG`, `readelf`, `/proc/PID/maps`).
3. **The performance report:** three experiments: cache locality (row vs column), syscall cost (writing 10⁶ lines unbuffered vs buffered), and creation cost (1,000 processes vs 1,000 threads). Each has a prediction, method, results chart, and an explanation that names the hardware or OS mechanism.

**Acceptance criteria**
- All nand2tetris test scripts pass, run by one command (`make test` or a Python script).
- Every experiment is reproducible with one command, repeated ≥ 10 times, reports median and spread, and lists the machine specification.
- Each claim in the explainer is backed by a captured tool output in the repo; zero unsupported claims after peer review using the [FND106](../FND106_technical_communication_and_professional_skills/README.md) review checklist.
- At least one prediction was wrong, and the report explains why.
- Oral defence with AI off: the examiner points at any line of your trace or any chip and you explain it.

**Stretch goals.** Run the experiments on two different machines (for example, an x86-64 laptop and an Arm board or cloud VM) and explain the differences; add a fourth experiment of your own design.

**What it proves to an employer.** You reason about systems with evidence, not folklore, and you can explain low-level behaviour clearly: the core of performance, SRE and embedded roles.

## Feeds into

- [CS202 Computer Architecture and Systems Programming in C](../../../02_year_2_core_computer_science/semester_3/CS202_computer_architecture_and_systems_programming/README.md): pipelines, caches and C build directly on Chapters 6–8 and P2.
- [CS203 Operating Systems](../../../02_year_2_core_computer_science/semester_3/CS203_operating_systems/README.md): processes, virtual memory and file systems in depth.
- [CS204 Computer Networks](../../../02_year_2_core_computer_science/semester_3/CS204_computer_networks/README.md): the network card as a device, sockets as file descriptors.
- [CS216 Programming Languages, Compilers and Interpreters](../../../02_year_2_core_computer_science/semester_4/CS216_programming_languages_compilers_and_interpreters/README.md): the assembler and VM ideas become a full compiler.
- The [Embedded Systems and IoT major](../../../03_majors/embedded_systems_iot/README.md) starts from this hardware view.
