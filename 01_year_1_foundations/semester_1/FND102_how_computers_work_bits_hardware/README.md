# FND102 · How Computers Work: Bits, Hardware and the Operating System

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 1 · 1 | 4 (≈ 120 hours) | L0 → L2 | none | [CS202](../../../02_year_2_core_computer_science/semester_3/CS202_computer_architecture_and_systems_programming/README.md), [CS204](../../../02_year_2_core_computer_science/semester_3/CS204_computer_networks/README.md) (and through CS202, [CS203](../../../02_year_2_core_computer_science/semester_3/CS203_operating_systems/README.md)) |

## Why this course matters now

Every abstraction leaks: a float rounds a payment wrong, a 32-bit counter wraps, an array walked in the wrong order runs many times slower, and in 2018 the Meltdown and Spectre attacks showed that CPU speed tricks (speculative execution plus cache timing) could leak secrets across security boundaries. AI assistants such as Claude Code, GitHub Copilot and ChatGPT explain assembly from Compiler Explorer or a `strace` log well, but they cannot see your machine; claims about latency, cache behaviour or bit-level results must be measured or checked against a simulator. Hardware is also a live field in India: ISRO's Semiconductor Laboratory presented the 32-bit Vikram 3201 processor at Semicon India in September 2025, and IIT Madras's SHAKTI project builds open-source RISC-V processors. In this course you build a computer from NAND gates (the nand2tetris path), then climb to the operating system, so that nothing between a keypress and a pixel is magic.

## Learning outcomes

By the end you can:

1. Convert between decimal, binary and hexadecimal, and compute two's-complement results and overflow by hand.
2. Explain how integers, IEEE 754 floats, UTF-8 text, images and files are stored as bytes, and inspect them with `xxd` and Python's `struct`.
3. Build and test logic gates, an adder, an ALU, registers, RAM and a CPU in HDL from NAND alone (nand2tetris Projects 1–5).
4. Write assembly programs and an assembler that turns them into machine code (Projects 4 and 6).
5. Explain the fetch–decode–execute cycle and trace a short program through registers and memory.
6. Measure memory-hierarchy effects (cache locality, syscall cost) and explain the results with latency orders of magnitude.
7. Explain processes, system calls, virtual memory, files and file descriptors, and observe them with `ps`, `/proc` and `strace`.
8. Describe end to end what happens when you run `python hello.py` or `./a.out` on Linux, with evidence from tools.

## Chapters and lessons

### Chapter 1 · Bits and integers (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Place value | Binary and hex as base 2 and 16; bits, bytes, nibbles; why hex is a shorthand for 4-bit groups. | Convert 20 numbers among bases by hand; check with `bin`, `hex`, `int(s, 2)`. |
| 1.2 Unsigned and signed | Fixed-width integers, two's complement, range of n bits, sign extension. | Represent −1, −128 and 127 in 8 bits; explain why there is one more negative number. |
| 1.3 Overflow | Wraparound, carry vs overflow, why Python ints don't overflow but C, Java and hardware do. | Compute the exact moment a signed 32-bit Unix time overflows (the Year 2038 problem) with `datetime`. |
| 1.4 Bitwise operations | `&`, `\|`, `^`, `~`, shifts; masks, flags, testing and setting bits. | Pack and unpack Unix permission bits (`rwxr-x---`) to and from an integer. |

**Check your understanding:** (1) Why does adding two large positive 8-bit signed numbers give a negative result? (2) How does `x & (x - 1)` change `x`, and what is it useful for? (3) Why is hex, not decimal, the natural notation for memory addresses?

### Chapter 2 · Representing everything (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Floating point | IEEE 754 double: sign, exponent, fraction; rounding; why `0.1 + 0.2 != 0.3`; NaN, ±inf, −0.0. | Decode the bits of 0.1 and 1e308 with `struct.pack('>d', x)`. |
| 2.2 Money and precision | Why money is stored as integer paise or `Decimal`; accumulation error in loops. | Sum 0.1 ten million times as float and as integer paise; explain the difference. |
| 2.3 Text | ASCII, Unicode code points, UTF-8 (RFC 3629) as 1–4 byte sequences; mojibake. | Encode ₹ (U+20B9) to UTF-8 by hand (answer: E2 82 B9); verify with Python. |
| 2.4 Files are bytes | Magic numbers (the PNG signature `89 50 4E 47`), headers, endianness, images as pixel arrays, audio as samples. | Read a PNG's width and height from its header bytes with `struct.unpack`. |

**Check your understanding:** (1) Why can a 64-bit float represent 10³⁰⁸ but not 0.1 exactly? (2) Why is UTF-8 backward compatible with ASCII? (3) A file named `photo.png` starts with `25 50 44 46`; what is it really?

### Chapter 3 · Logic gates from NAND (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Boolean algebra | Truth tables, De Morgan's laws, canonical sum-of-products form. | Derive XOR as a sum of products; simplify it. |
| 3.2 NAND is universal | Building Not, And, Or from NAND; why one gate type suffices. | nand2tetris Project 1: Not, And, Or, Xor. |
| 3.3 Multiplexers | Mux, DMux, multi-bit and multi-way variants; selecting data with control bits. | Project 1: Mux, DMux, Mux16, Mux4Way16, DMux8Way. |
| 3.4 HDL and testing | Hardware description language, test scripts (`.tst`) and compare files (`.cmp`); the simulator as ground truth. | Write an extra test script that exposes a deliberately broken Xor. |

**Check your understanding:** (1) Why is "it passed the simulator's tests" stronger evidence than "it looks right"? (2) Express Or using only NAND and justify each step. (3) What does a Mux let a CPU do that gates alone do not?

### Chapter 4 · Arithmetic and the ALU (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Adders | Half adder, full adder, ripple-carry 16-bit adder, carry propagation delay. | Project 2: HalfAdder, FullAdder, Add16, Inc16. |
| 4.2 Subtraction for free | x − y = x + (¬y + 1); why two's complement makes one adder do both. | Compute 5 − 9 in 8 bits by hand through an adder. |
| 4.3 The ALU | Control bits (zx, nx, zy, ny, f, no), status flags (zr, ng); how 6 bits select 18 functions. | Project 2: the Hack ALU; derive which control bits give x − 1. |
| 4.4 Cost and speed | Gate count and depth as cost and delay; carry-lookahead idea. | Count gates in your Add16; estimate its critical path. |

**Check your understanding:** (1) Why does ripple-carry addition get slower as width grows? (2) How does the ALU compute `-x` with no subtractor? (3) What do the `zr` and `ng` flags let a program do next?

### Chapter 5 · Memory and sequential logic (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Time and state | The clock, combinational vs sequential logic, the data flip-flop (DFF) as a one-step memory. | Explain why a feedback loop of gates without a clock is unreliable. |
| 5.2 Registers | Bit, 16-bit Register, the load signal. | Project 3: Bit, Register. |
| 5.3 RAM | Addressing, RAM8 → RAM64 → … → RAM16K by composition. | Project 3: RAM8 through RAM16K. |
| 5.4 The program counter | Increment, load (jump), reset. | Project 3: PC; trace 8 clock cycles by hand. |

**Check your understanding:** (1) Why must memory be sequential but an adder need not be? (2) How many address bits does RAM16K need, and how are they split across levels? (3) What would break if the PC could not be loaded?

### Chapter 6 · Machine language and the CPU (weeks 6–7)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Instruction sets | Hack A- and C-instructions; compare with RISC-V RV32I (load/store, registers, immediate values); RISC vs CISC. | Translate 5 Hack instructions to binary by hand. |
| 6.2 Programming in assembly | Labels, variables, loops, pointers, memory-mapped screen and keyboard. | Project 4: Mult and Fill. |
| 6.3 Fetch–decode–execute | Instruction register, decode logic, jump conditions, the datapath. | Trace Mult for 3 × 2 cycle by cycle. |
| 6.4 Building the computer | CPU + instruction memory + data memory; why a CPU is "just" a state machine. | Project 5: CPU and Computer, passing all test scripts. |
| 6.5 A real ISA | Running RISC-V code in the Ripes simulator; pipelines as a preview of [CS202](../../../02_year_2_core_computer_science/semester_3/CS202_computer_architecture_and_systems_programming/README.md). | Write a RISC-V loop summing an array; watch the 5-stage pipeline in Ripes. |

**Check your understanding:** (1) Why does the Hack CPU need both an A-register and a D-register? (2) What does memory-mapped I/O mean for how a program draws on the screen? (3) Why can a pipelined CPU finish nearly one instruction per cycle even though each takes several?

### Chapter 7 · From source code to machine code (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Assemblers | Two passes, symbol table, predefined symbols, variables from address 16. | Project 6: the Hack assembler in Python, with tests (uses [FND101](../FND101_programming_i_computational_thinking_with_python/README.md) skills). |
| 7.2 Compilers | Source → assembly → object file → executable; optimisation levels. | Compare `-O0` and `-O2` output for a loop on Compiler Explorer (godbolt.org). |
| 7.3 Interpreters and bytecode | CPython compiles to bytecode and interprets it; the `dis` module; why Python is slower per operation. | `dis` a function with a loop; map each bytecode to a source line. |
| 7.4 Virtual machines | Stack-based VMs (nand2tetris Part II, the JVM, CPython) as portable layers. | Hand-translate `a = b + c * 2` into stack-VM instructions. |

**Check your understanding:** (1) Why does the assembler need two passes? (2) What does an optimising compiler know that lets it delete your loop? (3) Where in Python's pipeline does a `SyntaxError` come from, compared with a `TypeError`?

### Chapter 8 · The memory hierarchy and performance (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 The latency ladder | Registers, L1/L2/L3 cache, DRAM, SSD, network: orders of magnitude, not exact numbers (Norvig's table). | Build a log-scale chart of the ladder; restate each step "if L1 took 1 second…". |
| 8.2 Locality | Temporal and spatial locality, cache lines (find yours with `getconf LEVEL1_DCACHE_LINESIZE` on Linux), prefetching. | Run a provided C benchmark: row-major vs column-major traversal of a 4096×4096 array; explain the gap. |
| 8.3 Why Python hides it | Interpreter overhead per operation dwarfs cache effects in pure-Python loops; NumPy exposes them again. | Repeat 8.2 in pure Python and with NumPy; explain all three results. |
| 8.4 When speed leaks secrets | Meltdown and Spectre (2018): speculative execution plus cache timing as a side channel; mitigations cost performance. Concepts only. | Write a one-page explanation for a non-expert; cite the original disclosure site. |

**Check your understanding:** (1) Why does accessing one byte bring 64 neighbouring bytes into cache, and when does that help? (2) Why did the gap shrink in pure Python? (3) Why can an optimisation that never changes a program's output still be a security problem?

### Chapter 9 · The operating system and processes (week 10)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 What an OS does | Abstraction, protection, resource sharing; kernel mode vs user mode; system calls as the only door. | List 10 syscalls `strace python3 -c "print('hi')"` makes and what each does. |
| 9.2 Processes | Address space, PID, parent/child, `fork`, `exec`, `wait`, exit status, zombies. | Write a Python program using `os.fork` and `os.waitpid`; show a zombie with `ps`. |
| 9.3 Scheduling | Time slicing, context switches, run queues, CPU-bound vs I/O-bound. | Run 4 CPU-bound processes on a 2-core VM; observe with `top` and explain. |
| 9.4 Threads | Threads share an address space; races; Python's GIL and the free-threaded build officially supported since Python 3.14 (PEP 779). | Time a CPU-bound task with threads vs processes; explain the result. |

**Check your understanding:** (1) Why can't a user program simply write to the disk controller directly? (2) What exactly does `exec` replace, and what survives? (3) When do threads help a Python program even with the GIL?

### Chapter 10 · Virtual memory, files and I/O (week 11)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Virtual memory | Address translation, pages (commonly 4 KiB), page tables, TLB, page faults, segmentation faults. | Read `/proc/self/maps` for a Python process; label stack, heap, code and libraries. |
| 10.2 Stack and heap | Call frames, local variables, dynamic allocation, why stack overflow happens. | Trigger and explain a `RecursionError`; relate it to stack frames. |
| 10.3 Files | Inodes, directories, hard vs symbolic links, permissions, "everything is a file". | `ls -i`, `stat`, `ln`, `ln -s`; delete the original and explain what survives. |
| 10.4 File descriptors and buffering | `open`/`read`/`write`/`close`, stdin/stdout/stderr as fds 0/1/2, user-space buffering, `fsync` and durability. | Time writing 10⁶ lines buffered vs `flush` every line vs `fsync` every line. |

**Check your understanding:** (1) How can two processes both use address `0x400000` without conflict? (2) Why does a hard link keep data alive after `rm`? (3) Why might data you "wrote" be lost after a power cut?

### Chapter 11 · What happens when you run a program (week 12)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 From keypress to shell | Terminal, shell parsing, `PATH` lookup, `fork` + `exec`. | Use `type`, `which` and `strace -f bash -c ls` to follow the lookup. |
| 11.2 Loading | ELF format, `readelf -h`, entry point, dynamic linking with `ldd`, `libc`, `_start` → `main`. | Inspect a compiled `hello` with `readelf`, `ldd`, `objdump -d`. |
| 11.3 Running and exiting | System calls during execution (`write(1, …)`), exit codes, signals (`SIGINT`, `SIGSEGV`). | Write a one-page, evidence-backed trace of `./hello` from Enter to prompt. |
| 11.4 Booting | Firmware (UEFI), bootloader, kernel, `init`/`systemd`; what the machine does before you log in. | Read `journalctl -b` or `dmesg` and annotate the first 20 lines. |

**Check your understanding:** (1) Why does the shell fork before exec instead of exec-ing directly? (2) Where does `printf` end up becoming a system call? (3) What does exit code 139 tell you?

### Chapter 12 · Modern hardware (week 13)
| Lesson | What you learn | Practice |
|---|---|---|
| 12.1 Multicore | Cores, hyperthreads, shared caches, why clock speeds stopped rising and core counts grew. | Read `lscpu` on two machines; explain the differences. |
| 12.2 GPUs and accelerators | Many simple cores running the same instruction on different data; why matrix multiplication (and so AI) suits them. | Count the multiply-adds in a 4096×4096 matrix product; estimate time at a given FLOP rate. |
| 12.3 Instruction set landscape | x86-64, Arm, RISC-V (open ISA; SHAKTI, India's processor efforts); licensing vs open standards. | Compile one C function for x86-64 and RISC-V on Compiler Explorer; compare instruction counts. |
| 12.4 Interrupts and devices | Interrupts, DMA, device drivers, and the network card as a device (preview of [CS204](../../../02_year_2_core_computer_science/semester_3/CS204_computer_networks/README.md)). | Watch `/proc/interrupts` change while copying a large file. |

**Check your understanding:** (1) Why does doubling cores rarely double a program's speed? (2) What property of a workload makes it GPU-friendly? (3) Why does an open ISA matter for a country building its own chips?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Bits by hand and in Python | Conversion drill sheet; Y2038 calculation |
| 2 | 2 | Bytes in files | PNG/UTF-8 decoding notebook |
| 3 | 3 | nand2tetris Project 1 | All gates pass tests |
| 4 | 4 | Project 2 | ALU passes; **P1 due** |
| 5 | 5 | Project 3 | Memory chips pass |
| 6 | 6 | Project 4 | Mult and Fill |
| 7 | 6 | Project 5 | CPU and Computer pass |
| 8 | 7 | Project 6 assembler | Assembler output matches the official tool |
| 9 | 8 | Cache experiment | Report with charts; **P2 due** |
| 10 | 9 | Processes and syscalls | `strace` and `fork` notebook |
| 11 | 10 | Files and fsync timing | Measurement report |
| 12 | 11 | Program-run trace | One-page trace |
| 13 | 12 | `lscpu`, Compiler Explorer, interrupts | Short comparison write-up |
| 14 | Integration | P3 work and peer review | **P3 due** |
| 15 | Review and exam | Mock exam | Final exam (AI-off) |

## Working with AI in this course

- **Use AI for:** explaining a confusing simulator error or HDL message; explaining assembly from Compiler Explorer line by line (then check each instruction in the Intel/AMD or RISC-V reference); annotating `strace` or `readelf` output; generating extra test vectors for your assembler, whose expected outputs you confirm with the official tool.
- **Do without AI (drills):** all nand2tetris chips are your own HDL, written without AI code generation; weekly 15-minute drills of 20 conversions (binary, hex, two's complement, IEEE 754 fields); tracing fetch–decode–execute on paper; the final exam.
- **Verify AI output by:** running the nand2tetris test scripts (the simulator is the ground truth); recomputing bit-level answers in Python (`struct`, `bin`, masks); measuring latency and throughput yourself with repeated runs; checking OS claims against `man` pages and OSTEP.
- **Where AI still fails here:** confident arithmetic slips at bit boundaries (ask a chatbot for the two's complement of −128 in 8 bits, or the bits of 0.1, and check); invented HDL syntax or built-in chips that the nand2tetris simulator rejects; performance numbers that do not match your machine. It also cannot observe your system: every number in your reports must come from a tool you ran.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| nand2tetris Projects 1–6 (auto-tested) | 25% |
| Measurement labs (cache, syscalls, files) | 15% |
| Projects: P1 5%, P2 10%, P3 15% | 30% |
| Final exam (AI-off: conversions, circuit design on paper, tracing, OS reasoning) | 30% |

**Gate:** you pass when, with AI off, you can (1) design on paper a 4-bit adder–subtractor from gates and verify it on three cases; (2) hand-assemble and trace a 10-instruction Hack program; (3) explain, with `strace` and `readelf` evidence you collect live, every step from typing `./hello` to the prompt returning; and (4) predict the direction of a cache-locality experiment, run it, and explain the measured result.

## Industry reality

Performance engineering, embedded systems, security and SRE all depend on this layer. Meltdown and Spectre forced operating-system and browser changes across the industry in 2018. India's chip work spans ISRO SCL's Vikram 3201 for launch vehicles (presented September 2025; The Register noted its modest specifications) and IIT Madras's open-source SHAKTI RISC-V family. Debugging production incidents regularly comes down to file descriptors, memory, and system calls.

**Interview questions from this course**

1. *"What happens when you run `python script.py`?"* Shell parsing and `PATH` lookup, `fork`/`exec`, ELF loading and dynamic linking of the interpreter, compilation to bytecode, execution, syscalls for I/O, exit status back to the shell.
2. *"Why is row-by-row traversal of a 2D array faster than column-by-column in C?"* Row-major layout, cache lines and spatial locality, hardware prefetching; supported by a measurement and its magnitude.
3. *"Process vs thread?"* Separate vs shared address spaces, creation and switching cost, isolation on crash, communication methods, Python's GIL and the free-threaded build.
4. *"Why does 0.1 + 0.2 not equal 0.3, and how should money be stored?"* Binary fractions, IEEE 754 rounding, integers in the smallest unit or decimal types, rounding rules stated explicitly.
5. *"What is a page fault?"* Virtual-to-physical translation, page tables and TLB, minor vs major faults, demand paging, segfault as an invalid access.

## Resources (free first)

- **Core path:** [nand2tetris.org](https://www.nand2tetris.org/course) projects, [software](https://www.nand2tetris.org/software) and the [online IDE](https://nand2tetris.github.io/web-ide); book *The Elements of Computing Systems* (Nisan and Schocken, MIT Press, 2nd edition, 2021; paid; the projects are free). The [Coursera version](https://www.coursera.org/learn/build-a-computer) offers a paid certificate.
- **Operating systems:** [*Operating Systems: Three Easy Pieces*](https://pages.cs.wisc.edu/~remzi/OSTEP/) (free); NPTEL [Introduction to Operating Systems](https://nptel.ac.in/courses/106106144) (Prof. Chester Rebeiro, IIT Madras).
- **University courses:** [MIT 6.004 Computation Structures](https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/) and [computationstructures.org](https://computationstructures.org/); [Berkeley CS61C](https://cs61c.org/); [CMU 15-213](https://www.cs.cmu.edu/~213/) (its textbook, [CS:APP](https://csapp.cs.cmu.edu/), is paid); [Harvard CS61](https://cs61.seas.harvard.edu/); [Cornell CS3410](https://www.cs.cornell.edu/courses/cs3410/2024fa/).
- **Tools:** [Compiler Explorer](https://godbolt.org/); [Ripes RISC-V simulator](https://github.com/mortbopet/Ripes); [CPUlator](https://cpulator.01xz.net/); [Digital](https://github.com/hneemann/Digital) and [Logisim-evolution](https://github.com/logisim-evolution/logisim-evolution) circuit simulators; [x86 instruction reference](https://www.felixcloutier.com/x86/); [RISC-V ratified specifications](https://riscv.org/specifications/ratified/).
- **Readings:** [Peter Norvig's latency table](https://norvig.com/21-days.html); Ulrich Drepper, [*What Every Programmer Should Know About Memory*](https://people.freebsd.org/~lstewart/articles/cpumemory.pdf) (2007); David Goldberg, [*What Every Computer Scientist Should Know About Floating-Point Arithmetic*](https://docs.oracle.com/cd/E19957-01/806-3568/ncg_goldberg.html); [Python's floating-point tutorial](https://docs.python.org/3/tutorial/floatingpoint.html); [RFC 3629 (UTF-8)](https://www.rfc-editor.org/rfc/rfc3629); [Linux `/proc` documentation](https://www.kernel.org/doc/html/latest/filesystems/proc.html); [what-happens-when](https://github.com/alex/what-happens-when); Julia Evans's [strace zine](https://wizardzines.com/zines/strace/).
- **Video:** [Ben Eater's 8-bit breadboard computer](https://eater.net/8bit); [Crash Course Computer Science](https://www.youtube.com/playlist?list=PL8dPuuaLjXtNlUrzyH5r6jN9ulIgZBpdo).

## Sources

- Meltdown and Spectre disclosure (2018): [meltdownattack.com](https://meltdownattack.com/) (checked Oct 2026).
- Vikram 3201 presented at Semicon India 2025, specifications critique: [The Register, 3 Sep 2025](https://www.theregister.com/2025/09/03/india_hails_first_homegrown_chip/) (checked Oct 2026).
- SHAKTI open-source RISC-V processors, IIT Madras: [shakti.org.in](https://shakti.org.in/) (checked Oct 2026).
- Free-threaded Python officially supported in 3.14 (PEP 779): [What's New in Python 3.14](https://docs.python.org/3/whatsnew/3.14.html) (checked Oct 2026).
- nand2tetris projects, online IDE and Coursera certificate: [nand2tetris.org](https://www.nand2tetris.org/) (checked Oct 2026).
- Curriculum benchmark: [ACM/IEEE/AAAI CS2023](https://ieeecs-media.computer.org/media/education/reports/CS2023.pdf) knowledge areas for architecture and systems fundamentals (checked Oct 2026).

_Last reviewed: 2026-10_
