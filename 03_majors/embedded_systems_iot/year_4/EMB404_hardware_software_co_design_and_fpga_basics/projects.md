# EMB404 · Labs and projects

Hardware: a small FPGA board supported by the open toolchain (Lattice iCE40 boards such as iCEBreaker or UPduino, an ECP5 board, or a Gowin Tang Nano 9K/20K), your logic analyser, and optionally a VGA/DVI-capable board and monitor. Software: OSS CAD Suite (Yosys, nextpnr, Verilator, SymbiYosys, openFPGALoader), cocotb, LiteX, and an HLS tool (Bambu, or AMD Vitis HLS where licences allow). Every design must pass `verilator --lint-only -Wall`, synthesise with no unintended latches, and ship with a self-checking testbench.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Partition a workload | Profile an EMB301 firmware; compute Amdahl and roofline limits for offloading its hot loop | Profile data, calculations, a one-page recommendation | 3 h |
| 2 · Logic on paper and in simulation | ALU, counter and traffic-light FSM designed on paper, then simulated | Diagrams, timing diagrams, passing testbenches | 4 h |
| 3 · Synthesisable SystemVerilog | Find and remove latches and blocking-assignment races from a provided design | Before/after synthesis reports; explanation of each fix | 4 h |
| 4 · Testbenches, cocotb and an AI audit | cocotb testbench with a Python reference model for a UART transmitter; audit an AI-written RTL block and testbench | Coverage of FSM states; audit table (latches, CDC, unchecked testbench, unsupported syntax) | 5 h |
| 5 · Open toolchain on hardware | Build and program a design with Yosys, nextpnr and openFPGALoader; add a PLL clock | Build scripts, resource and timing reports, photo or capture of the running design | 3 h |
| 6 · Timing and an async FIFO | Pipeline a MAC to double Fmax; build and formally check an async FIFO with Gray-coded pointers | Timing reports before/after; SymbiYosys proof of no overflow/underflow | 6 h |
| 7 · UART, PWM and a bus wrapper | UART loopback to a laptop; hardware PWM; wrap PWM as a Wishbone or AXI4-Lite peripheral | 1 MB loopback with zero errors; PWM captures; bus-level testbench | 5 h |
| 8 · A LiteX SoC with your peripheral | Build a LiteX SoC with a RISC-V soft core; add your PWM peripheral and drive it from C | SoC build, register map, C driver, demo | 5 h |
| 9 · Peripheral vs custom instruction | Accelerate CRC32 as a memory-mapped peripheral and as a custom instruction (CFU style) | Kernel and application speed-ups for both; resource cost | 5 h |
| 10 · HLS vs hand-written RTL | FIR filter with HLS at II = 1 and by hand | Fmax, latency, II, LUT/DSP/BRAM use for both; verification results | 4 h |

## Projects

### P1 · A verified UART (L1, ~6 hours)

**Real-world inspiration.** UARTs are among the first peripherals brought up in chip and FPGA designs, and the way verification teams test them (reference models, random stimulus, coverage) is the same way they test much larger blocks.

**What to build.** A parameterised UART transmitter and receiver in SystemVerilog with oversampling and framing-error detection, a cocotb testbench with a Python reference model and random tests, and a hardware loopback to your laptop.

**Acceptance criteria**
- 10,000 random bytes pass in simulation at 3 baud rates, including back-to-back frames.
- The receiver tolerates ±2% baud-rate mismatch in simulation; behaviour at ±5% is documented.
- 100% FSM state and transition coverage reported.
- Lint clean; synthesis shows no latches; timing met at your board clock.
- 1 MB transferred through the FPGA loopback at 115,200 baud with zero errors (checksum compared).

**Stretch goals.** A formal property that the TX line idles high whenever the transmitter is idle; a FIFO-buffered version with flow control.

**What it proves to an employer.** You can design and verify a real hardware block with the methods used in chip teams, not just make it work once on a board.

### P2 · A LiteX SoC with a custom motor-control peripheral (L2, ~15 hours)

**Real-world inspiration.** Multi-axis motor controllers in drones, robots and CNC machines need many precise PWM outputs and encoder inputs; when a microcontroller runs out of timers or edge-capture speed, designers move these functions into programmable logic (illustrative scenario).

**What to build.** A memory-mapped peripheral with 4 PWM channels and 2 quadrature encoder inputs (with an index interrupt), integrated into a LiteX SoC with a RISC-V soft core, plus a documented register map and a C driver with host-side tests.

**Acceptance criteria**
- 4 PWM channels at 20 kHz with 16-bit resolution; measured duty-cycle error at most 0.1% on the logic analyser across 5 settings.
- Encoder counting is exact against a generated test signal at the highest edge rate you can produce, and that rate is reported and compared with your EMB301 MCU's timer-based encoder limit.
- The index interrupt reaches the C handler; latency in clock cycles is measured.
- Register map documented (address, fields, reset values, access types) and matched by the driver; driver unit tests run on the host against a register model.
- Timing closed with positive slack at the target clock; resource use reported.

**Stretch goals.** A hardware dead-time generator for H-bridges; a safety input that forces all PWM outputs off within one clock cycle, proven formally.

**What it proves to an employer.** You can build a complete hardware/software feature: RTL, bus integration, register map, driver and tests.

### P3 · A hardware accelerator with an honest end-to-end speed-up (L3, portfolio-grade, ~30 hours)

**Real-world inspiration.** Product teams move work into hardware only when the whole-system gain justifies the cost: secure-boot verification time, camera filtering at full frame rate, or vibration feature extraction on battery power (illustrative scenarios linked to EMB402 and EMB401).

**What to build.** Choose one kernel: (a) SHA-256 or CRC for firmware-image verification, (b) a streaming 3×3 image filter or small 2D convolution, or (c) an FIR/FFT feature extractor for vibration data. Implement it on your LiteX SoC in two ways (a DMA or streaming peripheral, and either a custom instruction or an HLS-generated block), with a verification plan, formal checks on the bus handshakes, and a written partitioning decision comparing your FPGA result with your EMB301 MCU and, where relevant, your EMB401 NPU measurements. Optionally, harden the core block with an open ASIC flow and submit it to a Tiny Tapeout shuttle.

**Acceptance criteria**
- **Correctness:** bit-exact agreement with the software reference on at least 100,000 random inputs plus documented edge cases.
- **Performance:** at least a 10× kernel speed-up over the soft core's software version for one of the two implementations; the whole-application speed-up reported and explained with Amdahl's law.
- **Implementation:** timing closed with positive slack at the stated clock; utilisation table (LUTs, flip-flops, block RAM, DSP) for both implementations.
- **Verification:** a written plan; coverage report showing at least 90% of planned items hit; a SymbiYosys proof (with stated depth) that the streaming or bus handshake never drops or duplicates data.
- **Review:** a peer design review using a checklist (CDC, resets, latches, testability) with every high-severity finding resolved.
- **Decision:** a 1–2 page partitioning note with measurements: when this kernel belongs on an MCU, an NPU, an FPGA or custom silicon.

**Stretch goals.** Measure energy per operation on the FPGA board and compare with the MCU; build a Linux driver for the accelerator on a LiteX Linux SoC; complete the Tiny Tapeout submission.

**What it proves to an employer.** You can make and defend hardware/software partitioning decisions with verified hardware and measured results, which is what FPGA, SoC and semiconductor teams look for.

## Feeds into

- [EMB501 Frontier Seminar: Autonomous Systems and Physical AI](../../year_5/EMB501_frontier_seminar_autonomous_systems_and_physical/README.md): accelerators for perception and safety-critical, deterministic processing.
- [THS501 Thesis or Capstone I](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md): accelerator design or open-silicon theses.
- [EMB402 Embedded and IoT Security](../EMB402_embedded_and_iot_security/README.md): option (a) speeds up secure-boot and update verification.
- The [EMB flagship industry project](../../../../06_career_and_market_readiness/05_industry_projects/EMB_embedded_systems_iot.md): an optional hardware-acceleration extension.
