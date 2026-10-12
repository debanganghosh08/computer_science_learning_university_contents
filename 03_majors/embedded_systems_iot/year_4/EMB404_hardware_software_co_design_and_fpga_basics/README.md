# EMB404 · Hardware-Software Co-Design and FPGA Basics

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 4 · 8 | 4 (≈ 120 hours) | L1 → L3 in digital design (L3 in software assumed) | [EMB304](../../year_3/EMB304_iot_protocols_and_cloud_connectivity/README.md) (with [CS202](../../../../02_year_2_core_computer_science/semester_3/CS202_computer_architecture_and_systems_programming/README.md), [EMB301](../../year_3/EMB301_microcontrollers_and_embedded_c/README.md) and [EMB303](../../year_3/EMB303_electronics_and_interfacing_for_programmers/README.md) assumed) | [EMB501](../../year_5/EMB501_frontier_seminar_autonomous_systems_and_physical/README.md), [THS501](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md) |

## Why this course matters now

When a processor cannot meet a deadline or an energy budget, the work moves into hardware: a field-programmable gate array (FPGA) can process every pixel, radio sample or network packet in a fixed number of clock cycles, and a custom instruction can make a small RISC-V core run a model several times faster. Knowing when to use a microcontroller, an FPGA, a GPU, an NPU or custom silicon, and how to split a design between hardware and software, is a senior skill. It is also a growing one in India: 12 semiconductor projects had been approved under the India Semiconductor Mission by May 2026, and a follow-on programme was approved in July 2026. Open tools have removed the cost barrier: Yosys and nextpnr synthesise and place designs for Lattice iCE40, ECP5 and Gowin FPGAs on a laptop, Verilator and cocotb verify them, and Tiny Tapeout lets students put small designs on real chips. AI assistants generate Verilog quickly but unreliably: on NVIDIA's CVDP benchmark (783 problems, 2025), state-of-the-art models reached no more than 34% pass@1 on code generation, and verification tasks such as testbench generation were particularly hard. This course teaches you to design, verify and integrate hardware with the rigour that silicon demands.

## Learning outcomes

By the end you can:

1. **Choose** between MCU, MPU, FPGA, GPU, NPU and ASIC for a workload using throughput, latency, determinism, power, cost and volume, with numbers.
2. **Design** combinational and sequential logic and finite-state machines, and **reason** about setup and hold timing.
3. **Write** synthesisable Verilog/SystemVerilog and **read** VHDL, avoiding latches, races and non-synthesisable constructs.
4. **Verify** designs with self-checking testbenches (Verilator, cocotb), assertions and basic formal checks (SymbiYosys).
5. **Build** designs with an open FPGA toolchain (Yosys, nextpnr, openFPGALoader) and **close timing** using reports, pipelining and correct clock-domain crossing.
6. **Implement** UART, SPI, PWM and video interfaces in hardware, and standard on-chip buses (Wishbone, AXI4-Lite, AXI-Stream).
7. **Integrate** a RISC-V soft core with LiteX, add a custom peripheral, and **write** its C driver.
8. **Accelerate** a software kernel in hardware (custom peripheral, DMA or custom instruction) and **measure** the end-to-end speed-up against Amdahl's law.
9. **Use** high-level synthesis appropriately and **explain** initiation interval, pipelining and resource trade-offs.
10. **Describe** the ASIC flow with open PDKs and **submit** a small design to an educational tapeout (optional).

## Chapters and lessons

### Chapter 1 · Why co-design (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 The compute spectrum | MCU, MPU, FPGA, GPU, NPU, ASIC: parallelism, determinism, energy per operation, non-recurring cost | Place 8 workloads (motor control, video scaling, packet filtering, keyword spotting, etc.) on the spectrum |
| 1.2 Partitioning | Profiling first, Amdahl's law, data movement cost, the roofline model revisited from CS202 | Profile an EMB301 firmware; compute the best possible speed-up of offloading its hot loop |
| 1.3 Case studies | FPGA uses in software-defined radio, camera pipelines, network cards, and particle-physics triggers (hls4ml) | Summarise one public case: what moved to hardware and why |
| 1.4 Economics | Unit cost vs development cost, volume break-even between FPGA and ASIC, supply risk | Build a break-even chart for 1,000 to 1,000,000 units (illustrative prices, stated) |

**Check your understanding:** Why can an FPGA at 100 MHz beat a CPU at 3 GHz on some tasks and lose badly on others? Why is moving data often more expensive than computing on it? When does an ASIC become cheaper than an FPGA?

### Chapter 2 · Digital design refresh (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Combinational logic | Boolean algebra, multiplexers, decoders, adders, comparators | Design a 4-bit ALU on paper; verify with a truth-table script |
| 2.2 Sequential logic | Flip-flops, registers, counters, shift registers, synchronous resets | Draw the timing diagram of a 4-bit counter with enable |
| 2.3 Finite-state machines | Moore vs Mealy, state encoding, illegal-state recovery | Design a traffic-light controller FSM with a pedestrian button |
| 2.4 Timing basics | Propagation delay, setup and hold times, maximum clock frequency | Compute the maximum frequency of a 3-stage path from given delays |

**Check your understanding:** Why are synchronous designs easier to reason about than asynchronous ones? What happens if setup time is violated? Why might a one-hot FSM run faster than a binary-encoded one?

### Chapter 3 · Hardware description languages (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Verilog and SystemVerilog | Modules, ports, `always_ff` and `always_comb`, parameters, `generate` | Write the Chapter 2 ALU and counter in SystemVerilog |
| 3.2 Hardware, not software | Blocking vs non-blocking assignments, concurrency, why loops unroll into hardware | Show a race from blocking assignments in sequential logic; fix it |
| 3.3 Synthesisable style | Latch inference, complete case statements, reset strategy, what synthesis ignores | Find 5 latches in a provided design using the synthesis report |
| 3.4 Reading VHDL and alternatives | VHDL entity/architecture literacy; Python-based Amaranth HDL | Translate a small VHDL module into SystemVerilog |

**Check your understanding:** Why does an `if` without an `else` in combinational logic create a latch? What does a `for` loop become in hardware? When would a team choose VHDL over Verilog?

### Chapter 4 · Simulation and verification (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Testbenches | Stimulus, expected results, self-checking tests, waveforms (GTKWave or Surfer) | Self-checking testbench for the ALU with all input combinations |
| 4.2 Verilator and cocotb | Fast cycle-based simulation; Python testbenches with coroutines | Test a UART transmitter with cocotb against a Python model |
| 4.3 Assertions and coverage | SystemVerilog assertions (immediate and concurrent concepts), functional coverage | Add assertions that catch a planted FSM bug |
| 4.4 Formal verification basics | Bounded model checking with SymbiYosys; proving properties instead of testing cases | Prove a FIFO never overflows or underflows |

**Check your understanding:** Why do verification engineers often outnumber designers in chip teams? What can a formal check prove that a million random tests cannot? Why must a testbench check results rather than print them?

### Chapter 5 · FPGA architecture and the open toolchain (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Inside an FPGA | Look-up tables, flip-flops, carry chains, block RAM, DSP blocks, PLLs, I/O banks | Map a design's resource report to these elements |
| 5.2 The open flow | Yosys synthesis, nextpnr place and route, bitstream packing, openFPGALoader; OSS CAD Suite | Blink an LED on an iCE40 or Gowin board using only open tools |
| 5.3 Constraints | Pin constraints, clock definitions, I/O standards | Add a second clock domain with a PLL and constrain it |
| 5.4 Vendor tools | AMD Vivado, Altera Quartus, Lattice Radiant, Gowin EDA: when you need them (larger devices, IP cores, hard processors) | Build the same design with a vendor tool; compare reports |

**Check your understanding:** Why does a 32-bit multiplier use DSP blocks rather than LUTs? What does place and route decide that synthesis cannot? What do vendor tools give you that open tools may not?

### Chapter 6 · Timing closure and clock domains (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Static timing analysis | Critical paths, slack, reading nextpnr and vendor timing reports | Find and report the critical path of a slow design |
| 6.2 Pipelining | Registers to cut paths, throughput vs latency, retiming | Pipeline a multiply-accumulate to double the maximum frequency |
| 6.3 Clock-domain crossing | Metastability, two-flip-flop synchronisers, handshakes, asynchronous FIFOs with Gray-coded pointers | Build an async FIFO; verify it with random clock ratios |
| 6.4 Resets and initialisation | Synchronous vs asynchronous reset, reset synchronisers, power-on state | Fix a design that fails only on some power-ups |

**Check your understanding:** Why can a CDC bug pass every simulation and fail in hardware? Why does pipelining improve throughput but not latency? Why are Gray codes used for FIFO pointers?

### Chapter 7 · Interfaces and buses in hardware (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Serial interfaces | UART transmitter and receiver with oversampling, SPI controller, I2C awareness | UART loopback to your laptop at 115,200 baud |
| 7.2 Timing-precise outputs | PWM generators, debouncers, quadrature decoders in hardware | Drive a servo with a hardware PWM; read an encoder at full speed |
| 7.3 Video | VGA or DVI timing, framebuffers vs racing the beam | Display a test pattern on a monitor |
| 7.4 On-chip buses | Wishbone, AXI4-Lite (registers) and AXI-Stream (data flows), handshakes (valid/ready) | Wrap your PWM as an AXI4-Lite or Wishbone peripheral |

**Check your understanding:** Why does a hardware UART receiver oversample? What does valid/ready back-pressure prevent? Why are registers and streams usually on different buses?

### Chapter 8 · Soft cores and SoC building (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 RISC-V soft cores | PicoRV32, VexRiscv, NEORV32, SERV: size, speed and features | Compare resource use and CoreMark-style speed of two cores (published or measured) |
| 8.2 LiteX | Building an SoC from Python: CPU, memory, UART, timers, your peripherals | Build a LiteX SoC and run C code on it |
| 8.3 Custom peripherals with drivers | Register maps, CSRs, interrupts; C drivers using EMB301 techniques | Add your PWM peripheral and drive it from C |
| 8.4 Bigger systems | Linux-capable soft SoCs and hard-processor FPGAs (Zynq-class) as awareness | Boot a pre-built LiteX Linux image in simulation or on a larger board (optional) |

**Check your understanding:** When is a soft core better than an external MCU? What must a peripheral's register map document for its driver writer? Why do hard-processor FPGAs exist?

### Chapter 9 · Accelerators and the hardware-software interface (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Choosing what to offload | Hot loops, data size, control complexity | Pick and justify a kernel to offload (CRC32, FIR filter, AES round, small matrix multiply) |
| 9.2 Interface options | Memory-mapped registers, DMA, streaming, custom RISC-V instructions | Implement the kernel as a peripheral; measure end-to-end speed-up |
| 9.3 Custom instructions | Custom function units (for example Google's CFU Playground), compiler intrinsics | Add a custom instruction for your kernel; compare with the peripheral |
| 9.4 Measuring honestly | Cycle counts including data movement, Amdahl, energy where measurable | Report kernel-only and whole-application speed-ups |

**Check your understanding:** Why can a 50× faster kernel give only a 1.5× faster application? When is a custom instruction better than a peripheral? What should a speed-up claim always include?

### Chapter 10 · High-level synthesis (week 10)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 C to hardware | Schedules, initiation interval (II), latency, resource binding | Synthesise a FIR filter from C with an open (Bambu) or vendor (Vitis HLS) tool |
| 10.2 Pragmas | Pipeline, unroll, array partitioning; their area cost | Reach II = 1 for the FIR and report resource growth |
| 10.3 When HLS works | Regular loops and dataflow vs control-heavy code; verification of HLS output | Compare your hand-written and HLS FIR on speed and area |
| 10.4 Domain tools | hls4ml for neural networks, Google XLS awareness | Convert a tiny quantised network with hls4ml; read its report |

**Check your understanding:** What does II = 1 mean for throughput? Why does unrolling a loop eat area? Why must HLS output still be verified at RTL level?

### Chapter 11 · Signal processing and ML on FPGAs (week 11)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Fixed-point arithmetic | Q formats, rounding, overflow, DSP block usage | Implement a fixed-point biquad; compare with a float model |
| 11.2 Streaming dataflow | Line buffers, sliding windows, back-pressure | Build a 3×3 image filter on a video stream |
| 11.3 Quantised NN accelerators | Binary and int8 networks, dataflow architectures (for example AMD's FINN) | Read a FINN or hls4ml design; estimate its throughput from resources |
| 11.4 FPGA vs MCU vs NPU for ML | Comparing with your EMB401 measurements | Write a recommendation for a 30 fps person detector at 1 W |

**Check your understanding:** Why are FPGAs strong at fixed-latency pipelines but weaker for large, changing models? What limits a streaming filter's frame rate? When would you choose an MCU NPU instead?

### Chapter 12 · From FPGA to silicon (weeks 12–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 12.1 The ASIC flow | RTL, synthesis, floorplanning, place and route, timing and power sign-off, DRC/LVS | Annotate a flow diagram with what each step checks |
| 12.2 Open silicon | Open PDKs (SkyWater SKY130), OpenROAD/OpenLane, Tiny Tapeout shuttles | Harden a small design with an open flow; optionally submit to Tiny Tapeout |
| 12.3 Verification careers | Design verification roles, UVM awareness, coverage closure, formal | Write a verification plan for your P3 accelerator |
| 12.4 Design reviews | Reviewing RTL for CDC, resets, latches and testability | Review another student's design with a checklist |

**Check your understanding:** Why is a silicon bug so much more expensive than an FPGA bug? What does LVS check that simulation cannot? Why is design verification a large share of chip jobs?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Partition a workload | — |
| 2 | 2 | Lab 2 · Logic on paper and in simulation | — |
| 3 | 3 | Lab 3 · Synthesisable SystemVerilog | — |
| 4 | 4 | Lab 4 · Testbenches, cocotb and an AI audit | **P1 due** |
| 5 | 5 | Lab 5 · Open toolchain on hardware | — |
| 6 | 6 | Lab 6 · Timing and an async FIFO | — |
| 7 | 7 | Lab 7 · UART, PWM and a bus wrapper | Mid-term (AI off) |
| 8 | 8 | Lab 8 · A LiteX SoC with your peripheral | — |
| 9 | 9 | Lab 9 · Peripheral vs custom instruction | — |
| 10 | 10 | Lab 10 · HLS vs hand-written RTL | **P2 due** |
| 11 | 11 | Streaming filter (in P3) | — |
| 12 | 12 | Open ASIC flow | — |
| 13 | 12 | Verification plan and review | — |
| 14 | — | — | **P3 due** |
| 15 | Review | Oral defence of P3 | Final exam (AI off) |

## Working with AI in this course

- **Use AI for:** explaining unfamiliar HDL constructs and tool messages; drafting cocotb testbench scaffolding and reference models in Python; generating test vectors; summarising timing reports; drafting register maps and driver boilerplate from your specification.
- **Do without AI (drills):** FSM design on paper; timing calculations (maximum frequency, slack); CDC design; reading a synthesis report for latches and resource use; writing a FIFO from scratch. The mid-term and final are AI-off.
- **Verify AI output by:** lint (`verilator --lint-only -Wall`); synthesis reports (no unintended latches, expected resources); self-checking simulation against an independent reference model; formal properties for FIFOs and handshakes; timing reports after place and route; testing on hardware last.
- **Where AI still fails here (show it yourself):** the CVDP benchmark found no more than 34% pass@1 for state-of-the-art models on Verilog code generation, with agentic and verification tasks harder still (arXiv 2506.14074). In Lab 4 you ask an assistant for an RTL block and its testbench, then audit both. Typical defects: inferred latches, blocking assignments in sequential logic, missing or wrong clock-domain crossing, off-by-one counters, simulation-only constructs (delays, `initial` blocks relied on in ASIC flows), SystemVerilog features your toolchain does not support, and testbenches that print values but never check them.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (10) | 25% |
| Projects P1–P3 | 35% |
| Mid-term (AI off) | 10% |
| Final exam (AI off) + P3 oral defence | 30% |

**Mastery gate.** You pass when you can, with AI off: (1) design, simulate and run on an FPGA a small peripheral (for example a PWM or SPI controller) with a self-checking testbench in 2 hours; (2) find and fix a planted CDC bug and a timing violation from reports in 45 minutes; (3) defend your P3's partitioning decision with measured kernel-level and application-level speed-ups.

## Industry reality

Where this is used: FPGA and ASIC design and verification at semiconductor companies and their Indian design centres, telecom and software-defined radio, test and measurement equipment, automotive camera and radar processing, defence and space electronics, and high-frequency trading. India's semiconductor programme had 12 approved projects by May 2026 and a second-phase programme from July 2026 (PIB), adding demand for engineers who understand both chips and the software that uses them (analysis). Open tools (Yosys, nextpnr, Verilator, cocotb, OpenROAD) and shuttles such as Tiny Tapeout make serious practice possible without expensive licences.

**Interview questions from this course**

1. *Blocking vs non-blocking assignments: when do you use each?* Strong answer: non-blocking (`<=`) in clocked logic so all registers update together; blocking (`=`) in combinational logic; what race appears if mixed; `always_ff` and `always_comb` as safer SystemVerilog styles.
2. *What is metastability, and how do you cross clock domains safely?* Strong answer: flip-flop sampling during a transition; mean time between failures; two-flip-flop synchronisers for single bits, handshakes for control, async FIFOs with Gray-coded pointers for data; never synchronise a multi-bit bus bit by bit.
3. *Would you use an MCU, FPGA or GPU for this workload?* Strong answer: characterises throughput, latency and determinism needs, data rates, power, cost and volume, team skills; gives numbers and a recommendation with a fallback.
4. *Your design fails timing at 100 MHz. What do you do?* Strong answer: read the critical path, pipeline or retime it, use DSP and block RAM resources properly, reduce fan-out, check constraints are correct, consider a multicycle path only when justified.
5. *How would you speed up a CRC-heavy firmware with hardware?* Strong answer: profile first; options (peripheral with DMA, custom instruction, existing hardware CRC unit); data movement cost; Amdahl estimate; measurement of end-to-end gain; driver and test plan.

## Resources (free first)

- **Practice and courses:** HDLBits (Verilog exercises) — https://hdlbits.01xz.net/ ; Nand2Tetris — https://www.nand2tetris.org/ ; ZipCPU tutorials (formal verification, FPGA design) — https://zipcpu.com/ ; Project F (FPGA graphics and design) — https://projectf.io/ ; fpga4fun — https://www.fpga4fun.com/
- **Open tools:** OSS CAD Suite — https://github.com/YosysHQ/oss-cad-suite-build ; Yosys documentation — https://yosyshq.readthedocs.io/ ; nextpnr — https://github.com/YosysHQ/nextpnr ; Apicula (Gowin) — https://github.com/YosysHQ/apicula ; openFPGALoader — https://github.com/trabucayre/openFPGALoader ; Verilator — https://verilator.org/ ; cocotb — https://www.cocotb.org/ ; SymbiYosys — https://symbiyosys.readthedocs.io/ ; Surfer waveform viewer — https://surfer-project.org/ ; Amaranth HDL — https://amaranth-lang.org/
- **Soft cores and SoCs:** LiteX — https://github.com/enjoy-digital/litex ; VexRiscv — https://github.com/SpinalHDL/VexRiscv ; PicoRV32 — https://github.com/YosysHQ/picorv32 ; NEORV32 — https://github.com/stnolting/neorv32 ; CFU Playground — https://github.com/google/CFU-Playground
- **HLS and ML:** hls4ml — https://fastmachinelearning.org/hls4ml/ ; Bambu (PandA) — https://panda.deib.polimi.it/ ; Google XLS — https://google.github.io/xls/ ; FINN — https://github.com/Xilinx/finn
- **Open silicon:** Tiny Tapeout — https://tinytapeout.com/ ; OpenROAD — https://theopenroadproject.org/ ; SkyWater SKY130 PDK — https://github.com/google/skywater-pdk
- **Benchmark paper:** Pinckney et al., "Comprehensive Verilog Design Problems" (arXiv 2506.14074) — https://arxiv.org/abs/2506.14074
- **Paid, optional:** Sarah Harris and David Harris, *Digital Design and Computer Architecture: RISC-V Edition* (Morgan Kaufmann, 2021).

## Sources

- Pinckney et al., "Comprehensive Verilog Design Problems: A Next-Generation Benchmark Dataset for Evaluating Large Language Models and Agents on RTL Design and Verification" (arXiv 2506.14074, Jun 2025; 783 problems, ≤34% pass@1 on code generation) — https://arxiv.org/abs/2506.14074 (checked 2026-10)
- PIB, Cabinet approval of two more semiconductor units (5 May 2026; 12 approved projects) and Semicon 2.0 (15 Jul 2026) — https://www.pib.gov.in/PressReleasePage.aspx?PRID=2258116&reg=48&lang=2 ; https://www.pib.gov.in/PressReleasePage.aspx?PRID=2284784&reg=48&lang=2 (as summarised in search results, 2026-10)
- Tiny Tapeout — https://tinytapeout.com/ (checked 2026-10)

_Last reviewed: 2026-10_
