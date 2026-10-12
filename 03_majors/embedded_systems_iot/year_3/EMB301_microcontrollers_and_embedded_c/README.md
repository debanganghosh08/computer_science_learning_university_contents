# EMB301 · Microcontrollers and Embedded C

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 3 · 5 | 4 (≈ 120 hours) | L1 → L3 | [CS202](../../../../02_year_2_core_computer_science/semester_3/CS202_computer_architecture_and_systems_programming/README.md) | [EMB302](../EMB302_real_time_operating_systems/README.md) (taken alongside), [EMB401](../../year_4/EMB401_edge_ai_and_tinyml/README.md), [OV09A](../../../../04_overlaps/OV09_edge_ai_secure_iot/OV09A_deploying_models_on_edge_devices/README.md), [OV09B](../../../../04_overlaps/OV09_edge_ai_secure_iot/OV09B_iot_fleet_security_and_over_the_air_updates/README.md) |

## Why this course matters now

A microcontroller (MCU) is a whole computer on one chip: CPU, flash, RAM, timers and communication peripherals, often for under ₹200. Firmware for them is written in C against memory-mapped registers, and the work has changed in three ways. The cores now include RISC-V alongside Arm Cortex-M (Raspberry Pi's RP2350 lets you boot either dual Cortex-M33 or dual Hazard3 RISC-V cores on the same chip; Espressif's ESP32-C series is RISC-V). Coding rules have tightened: MISRA C:2025 (March 2025) supersedes every earlier edition, and Rust's `embedded-hal` 1.0 (January 2024) gave memory-safe firmware a stable driver interface. And AI assistants write peripheral code in seconds, but on EmbedBench the best model managed only 29.4% pass@1 when porting Arduino code to Espressif's ESP-IDF (2025–26). This course makes you the engineer who reads the reference manual, writes the driver at register level, proves it on a logic analyser and a current meter, and catches the invented register address before it ships.

## Learning outcomes

By the end you can:

1. **Explain** the memory map, bus matrix, reset sequence and clock tree of a Cortex-M or RISC-V MCU, and **locate** any peripheral register from the reference manual and the SVD file.
2. **Write** register-level drivers in C for GPIO, timers, ADC, UART, SPI and I2C, with correct use of `volatile`, atomic set/clear registers and read-modify-write protection.
3. **Write** startup code and a linker script, and **read** a map file to account for every byte of flash and RAM.
4. **Configure** the interrupt controller (NVIC, RISC-V PLIC/CLIC) with priorities, and **measure** interrupt latency and jitter with a logic analyser.
5. **Debug** firmware over SWD or JTAG with GDB, watchpoints, SWO/RTT logging and fault-register decoding, from a HardFault to a root cause.
6. **Compare** bare-metal, vendor HAL, Zephyr and Rust `embedded-hal` implementations of the same driver by code size, latency and portability.
7. **Design** a low-power node, **measure** its sleep and active current, and **predict** its battery life within 10%.
8. **Apply** MISRA C:2025 and CERT C awareness with static analysis, and **unit-test** firmware logic on the host.
9. **Audit** AI-generated firmware against the datasheet, the errata sheet and real measurements.

## Chapters and lessons

### Chapter 1 · The microcontroller as a system (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 MCU vs MPU vs SoC | On-chip flash and SRAM vs external DRAM and an MMU; why MCUs boot in microseconds; where each is used (meters vs routers) | Classify 10 real products' main chips from their teardown photos and datasheets |
| 1.2 The cores you will meet | Cortex-M0+/M4F/M33/M55 (Armv6-M to Armv8.1-M), RV32IMAC (ESP32-C6, RP2350 Hazard3), Xtensa LX7 (ESP32-S3); FPU, DSP and vector extensions | Build one C function for M0+, M4F and RV32; compare instruction counts on Compiler Explorer |
| 1.3 The document stack | Datasheet (electrical, pinout) vs reference manual (registers) vs errata sheet vs application notes vs SVD file | Find the register, bit field and reset value for "enable GPIOA clock" on an STM32F446 in all three documents |
| 1.4 Toolchains | `arm-none-eabi-gcc` and RISC-V GCC, CMake, Pico SDK, ESP-IDF, STM32CubeIDE/CubeMX, PlatformIO; flashing via UF2, ST-LINK, `esptool` | Build and flash "blink" three ways; record build time and binary size |
| 1.5 Simulators | Wokwi (ESP32, STM32, Pico, logic analyser), Renode (multi-node, CI), QEMU (Cortex-M machines) | Run the same blink in Wokwi and Renode; capture the pin waveform in the simulator |

**Check your understanding:** Why does a microcontroller usually have no MMU, and what does that change about how bugs show up? When would you choose a Cortex-M0+ over an M33 for the same product? Which document wins when the datasheet and the errata sheet disagree?

### Chapter 2 · Memory-mapped I/O and bit manipulation (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Registers as memory | Peripheral address space, register offsets, reset values, reserved bits; `volatile` and what it does not do (no atomicity, no ordering across cores) | Toggle a GPIO by writing raw addresses; then remove `volatile` at `-O2` and explain the result |
| 2.2 Bit-field idioms | Set, clear, toggle, test, insert a multi-bit field with masks and shifts; why C bit-fields are non-portable for registers | Write `REG_FIELD_SET(reg, mask, pos, val)` with tests on the host |
| 2.3 Atomic register access | Read-modify-write hazards with interrupts; STM32 `BSRR`, RP2350 SET/CLR/XOR register aliases, Cortex-M3/M4 bit-banding | Create an RMW race between main and an ISR; fix it two ways |
| 2.4 CMSIS and SVD | CMSIS device headers, `struct` register overlays, SVD files as the machine-readable truth; `svd2rust` | Generate a header from the SVD and diff it against an AI-written one |

**Check your understanding:** Why can two correct-looking writes to the same port register lose an update? What does `volatile` guarantee to the compiler, and what does it not guarantee to the hardware? Why is the SVD file a better check for an AI-written header than the AI's own explanation?

### Chapter 3 · From reset to `main` (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 The vector table and reset | Initial stack pointer, reset handler, exception vectors; RP2350 and ESP32 boot ROMs | Read the vector table from a `.elf` with `objdump` |
| 3.2 Startup code | Copying `.data` from flash to RAM, zeroing `.bss`, calling constructors, `SystemInit` | Write your own startup file in C; boot without the vendor's |
| 3.3 Linker scripts | `MEMORY`, `SECTIONS`, `KEEP`, load vs run address, placing code in RAM, stack and heap regions | Move a hot function to RAM; measure the speed-up with a GPIO toggle |
| 3.4 Clock trees | Internal and external oscillators, PLL configuration, flash wait states, peripheral clock gating | Configure 180 MHz on the F446 by hand; prove it with a timer-driven pin and the logic analyser |
| 3.5 Size budgets | Map files, `size`, `-Os` vs `-O2`, `-ffunction-sections` with `--gc-sections`, `printf` cost | Cut a 40 KB binary below 16 KB and document every saving |

**Check your understanding:** What happens if `.bss` is not zeroed, and why might tests still pass? Why must flash wait states change before the clock goes up? Where does your stack live, and how would you know it overflowed?

### Chapter 4 · Interrupts and exceptions (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 The NVIC | Enable, pending, priority, preemption and sub-priority; tail-chaining and late arrival; RISC-V PLIC/CLIC by comparison | Two interrupts at different priorities; show preemption on a logic analyser |
| 4.2 Latency and jitter | Hardware entry latency (12 cycles on Cortex-M3/M4 with zero-wait-state memory), flash wait states, critical sections that add jitter | Measure GPIO-in to GPIO-out latency over 10,000 events; plot the histogram |
| 4.3 ISR design rules | Keep ISRs short; defer work; clear the flag correctly (write-1-to-clear); no blocking calls; reentrancy | Refactor a slow ISR into a flag plus main-loop handler |
| 4.4 Sharing data with ISRs | Torn reads of 64-bit values, `volatile` vs atomics, disabling interrupts with PRIMASK vs BASEPRI, lock-free single-producer/single-consumer ring buffers | Implement an SPSC ring buffer; stress it with a 100 kHz interrupt |
| 4.5 Faults | HardFault, MemManage, BusFault, UsageFault; CFSR/HFSR/MMFAR/BFAR; recovering the stacked PC | Write a fault handler that prints the faulting PC and decode 3 planted faults |

**Check your understanding:** Why can disabling all interrupts to protect a counter break a motor-control loop? A flag is cleared at the end of the ISR and the ISR fires twice: why? How do you find the line that caused an imprecise BusFault?

### Chapter 5 · Timers, PWM and time (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Timer anatomy | Prescaler, auto-reload, counter modes, update events; SysTick | Compute prescaler and reload for 1 kHz, 50 Hz and 38 kHz by hand; verify on the analyser |
| 5.2 PWM | Duty cycle, resolution vs frequency trade-off, centre-aligned PWM, dead time for H-bridges | Dim an LED and drive a hobby servo (1–2 ms pulse at 50 Hz) |
| 5.3 Input capture and encoders | Measuring frequency and pulse width; quadrature encoder mode | Measure an unknown signal's frequency within 0.1% |
| 5.4 Keeping time | Wrap-around-safe comparisons (`(int32_t)(now - then) >= 0`), 32-bit microsecond counters overflowing after ~71.6 minutes, RTC and low-power timers | Find the wrap-around bug in a provided timeout function |

**Check your understanding:** Why does doubling PWM frequency halve the available resolution at a fixed timer clock? Why is `if (now > deadline)` wrong with a free-running counter? When would you use an RTC instead of SysTick?

### Chapter 6 · Analogue input and output (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 SAR ADCs | Resolution, reference voltage, sampling time vs source impedance, conversion time, LSB size | Measure a potentiometer; compute expected code vs measured code |
| 6.2 Noise and accuracy | Offset, gain error, INL/DNL (datasheet reading), averaging and oversampling, calibration registers | Characterise ADC noise (standard deviation in LSB) with and without averaging |
| 6.3 DMA-driven sampling | Timer-triggered conversions, circular DMA, half/full-transfer interrupts | Sample at 8 kHz into a double buffer with zero CPU copies |
| 6.4 DAC, comparators, internal sensors | DAC output, analogue comparators, internal temperature sensor and its calibration values | Generate a sine table with the DAC; read the on-chip temperature with factory calibration |

**Check your understanding:** Why does a high-impedance sensor give wrong readings with a short sampling time? How many samples must you average to gain one bit of resolution, and what condition must the noise meet? Why use DMA rather than an interrupt per sample at 8 kHz?

### Chapter 7 · Serial peripherals from registers (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 UART | Baud-rate generation and error, framing, overrun, idle-line detection, DMA receive | Build a command shell over UART with an interrupt-driven ring buffer |
| 7.2 SPI | Modes (CPOL/CPHA), chip-select timing, full duplex, DMA bursts | Read a SPI sensor's ID register; decode the transaction on the analyser |
| 7.3 I2C | Addressing, ACK/NACK, repeated start, clock stretching, bus-hang recovery (9 clocks) | Write a BME280 driver at register level; recover a deliberately hung bus |
| 7.4 Driver API design | Blocking vs non-blocking, callbacks vs events, error codes, testability, separating bus from device | Refactor your sensor driver so it runs against a fake bus on the host |

**Check your understanding:** A UART at 115,200 baud from an 8 MHz clock has 2.1% error: will it work, and with what? Why does an I2C bus hang after a reset in the middle of a read? What makes a driver testable without hardware?

### Chapter 8 · Bare metal, HAL, RTOS or Rust? (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Vendor HALs | STM32 HAL vs LL drivers, Pico SDK, ESP-IDF driver layers; hidden costs (blocking, timeouts, code size) | Implement the same UART echo with HAL and LL; compare size and latency |
| 8.2 Zephyr preview | Devicetree, Kconfig, driver model, one application source for boards from different vendors | Port your sensor app to Zephyr on two different boards |
| 8.3 Embedded Rust | `embedded-hal` 1.0 traits, PACs and HALs, ownership of peripherals, `probe-rs` | Blink and read the BME280 in Rust on the Pico 2 |
| 8.4 Program structure | Super-loop, cooperative scheduler, event-driven state machines (hierarchical, QP-style), when to move to an RTOS (EMB302) | Rewrite a tangled loop as an explicit state machine with a transition table |

**Check your understanding:** When is a vendor HAL the right call, and when does it become a liability? What does Rust's ownership model prevent in peripheral access that C cannot? Which symptoms tell you a super-loop has outgrown itself?

### Chapter 9 · Debugging like a firmware engineer (weeks 9–10)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Debug ports | SWD vs JTAG, debug probes (ST-LINK, CMSIS-DAP/Raspberry Pi Debug Probe, J-Link), OpenOCD, pyOCD, probe-rs | Attach GDB to a running target without resetting it |
| 9.2 GDB on targets | Hardware breakpoints and their limit, data watchpoints (DWT), inspecting peripherals, `monitor` commands | Catch a stray write to a global with a watchpoint |
| 9.3 Logging without breaking timing | `printf` cost, semihosting (slow), SWO/ITM, SEGGER RTT, binary logging, cycle counter (DWT_CYCCNT) timestamps | Measure the time cost of each logging method |
| 9.4 Instruments and code together | Correlating GPIO markers with bus traces; triggers; "debug pins" | Find a timing bug that only appears without the debugger attached |
| 9.5 Systematic debugging | Reproduce, bisect (git bisect on firmware), one change at a time, hypothesis log | Debug 5 planted bugs (stack overflow, uninitialised `.bss`, missing `volatile`, wrong clock, ISR flag) and log each |

**Check your understanding:** Why can adding a `printf` make a bug disappear? What does a data watchpoint cost at run time compared with a software check? Your board works when powered from USB but not from a battery: list your first three measurements.

### Chapter 10 · Low-power design (week 11)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Where current goes | Active vs sleep current, clock frequency and voltage, peripheral clocks, floating GPIO leakage, pull-ups | Find three hidden current drains on a provided board |
| 10.2 Sleep modes | Sleep/Stop/Standby (STM32), dormant (RP2350), light and deep sleep (ESP32); wake sources and wake latency | Wake on RTC every 10 s and on a button; measure each mode |
| 10.3 Measuring µA | Shunt resistors and INA219, Nordic Power Profiler Kit II or Joulescope (if available), USB meters' limits | Plot a full wake-measure-sleep cycle and integrate charge |
| 10.4 Battery budgets | mAh, duty-cycle averaging, self-discharge, temperature, end-of-life voltage | Predict life on 2×AA for a sensor reporting every 15 minutes; compare with measurement |

**Check your understanding:** Why can a node that sleeps at 5 µA still drain its battery in a month? Why is wake-up energy, not just sleep current, often what matters? What does a USB power meter miss?

### Chapter 11 · Robust, standard-compliant firmware (week 12)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Coding standards | MISRA C:2025 (purpose, mandatory/required/advisory, deviations), BARR-C:2018, SEI CERT C | Classify 15 snippets against a rule subset |
| 11.2 Static analysis | GCC `-Wall -Wextra -Wconversion`, `-fanalyzer`, clang-tidy, cppcheck with its MISRA add-on | Run all four on your project; fix or justify every finding |
| 11.3 Fixed-point and integer safety | Q15/Q31 formats, saturation, overflow, division cost on M0+ | Implement a fixed-point low-pass filter; compare with float on M0+ and M4F |
| 11.4 Testing firmware | Host unit tests (Unity/Ceedling, CMock), fakes for registers, hardware-in-the-loop in CI with Renode or a real board | Get 80% line coverage on driver logic, running in CI |
| 11.5 Watchdogs and asserts | Independent vs window watchdog, what to do on assert in the field, reset-reason registers | Log reset causes across 20 forced resets |

**Check your understanding:** What problem was MISRA created to solve, and why is a deviation record not a failure? Why is fixed-point still common on MCUs that have an FPU? What should a field device do when an assert fails?

### Chapter 12 · Bootloaders and production firmware (weeks 13–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 12.1 Flash programming | Erase/program granularity, wear, write protection, option bytes | Store and wear-level 1,000 config writes in two flash pages |
| 12.2 A minimal bootloader | Image header (magic, version, length, CRC32), jump to application, vector-table relocation | Write a UART bootloader that refuses a corrupted image |
| 12.3 Versioning and build identity | Semantic versions, git hash in firmware, reproducible builds | Print version and build ID at boot; reproduce a bit-identical build |
| 12.4 Factory and field | Production test firmware, serial numbers, calibration data, crash logs stored across resets | Write a 30-second self-test for your P3 node |

**Check your understanding:** Why does a CRC detect corruption but not tampering (and what fixes that in EMB402)? What happens if power fails halfway through writing a new image? Why must a field device record why it last reset?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Toolchains and simulators | — |
| 2 | 2 | Lab 2 · GPIO from raw registers | — |
| 3 | 3 | Lab 3 · Startup code and linker script | — |
| 4 | 4 | Lab 4 · Interrupt latency | **P1 due** |
| 5 | 5 | Lab 5 · Timers and PWM | — |
| 6 | 6 | Lab 6 · ADC with DMA | — |
| 7 | 7 | Lab 7 · I2C driver from the datasheet | Mid-term practical (AI off) |
| 8 | 8 | Lab 8 · Same driver, four ways | — |
| 9 | 9 | Lab 9 · Bug hunt with a debugger | — |
| 10 | 9 | Lab 9 (cont.) | **P2 due** |
| 11 | 10 | Lab 10 · Sleep current | — |
| 12 | 11 | Static analysis and host tests (in P3) | MISRA deviation report |
| 13 | 12 | Bootloader (in P3) | — |
| 14 | 12 | — | **P3 due** |
| 15 | Review | Oral defence of P3 | Final exam (AI off) |

## Working with AI in this course

- **Use AI for:** explaining a reference-manual section you have already located; drafting host-side test harnesses and fakes; generating lookup tables (sine, CRC) that you then check; writing CMake and CI files; turning your logic-analyser notes into a bug report. GitHub Copilot, Claude Code and Cursor work inside VS Code with the Pico SDK, ESP-IDF and STM32 extensions; STM32CubeMX generates clock and pin configuration you must still review.
- **Do without AI (drills):** GPIO, timer and UART drivers from raw registers; prescaler and baud-rate arithmetic; decoding a HardFault stack frame; reading a map file; battery-life estimates. The mid-term and final are AI-off.
- **Verify AI output by:** checking every register address, bit position and reset value against the SVD file and the reference manual for your exact part number; checking the errata sheet; compiling with warnings as errors and static analysis; capturing the bus or pin on a logic analyser; measuring current rather than trusting a claimed saving.
- **Where AI still fails here (show it yourself):** EmbedBench found the best model at 29.4% pass@1 on Arduino-to-ESP-IDF migration, against 73.8% for MicroPython on a Pico (arXiv 2506.11003), so vendor-SDK code is where to be most suspicious. In Lab 7 you ask an assistant for a register-level I2C driver for your exact MCU and log every defect: invented or wrong-family register names and addresses (for example STM32F1 GPIO registers used on an F4), missing clock enables, missing `volatile`, flags cleared the wrong way, deprecated SDK APIs (ESP-IDF's legacy ADC driver vs `adc_oneshot`), and non-ISR-safe calls inside interrupt handlers.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (10) | 25% |
| Projects P1–P3 | 35% |
| Mid-term practical (AI off) | 15% |
| Final exam (AI off) + P3 oral defence | 25% |

**Mastery gate.** You pass when you can, with AI tools off: (1) bring up a peripheral you have not used before (for example a timer in input-capture mode or an SPI ADC) from the reference manual alone in 90 minutes, proven on a logic analyser; (2) take a firmware image that HardFaults and name the faulting line from the stacked frame and fault registers within 20 minutes; (3) predict a node's average current from its duty cycle and measure it within 10%.

## Industry reality

Where this is used: every product in the major's [India context](../../README.md#india-context-checked-october-2026), from smart meters to EV battery management systems, runs MCU firmware. Chips used in this course are mainstream: the RP2350 adds Arm TrustZone, signed boot enforced by mask ROM with a key fingerprint in OTP, a SHA-256 accelerator and fault-injection mitigations, starting at $5 for the Pico 2 board (Raspberry Pi). MISRA C remains the de facto coding standard in automotive and other safety work, and its 2025 edition supersedes all earlier ones (MISRA). Rust firmware is no longer experimental: `embedded-hal` 1.0 stabilised GPIO, SPI, I2C and UART traits, including async versions (Rust Embedded WG, January 2024).

**Interview questions from this course**

1. *What does `volatile` do, and when is it not enough?* Strong answer: forces each access to happen as written (no caching in registers, no elision); needed for memory-mapped registers and variables shared with ISRs; does not make read-modify-write atomic or order accesses across cores; mentions critical sections, atomics or hardware set/clear registers.
2. *Write a macro or function to set bits 4–6 of a 32-bit register to a value without touching other bits.* Strong answer: mask `0x7u << 4`, clear then OR, unsigned constants, value masked before shifting, mention of RMW atomicity with interrupts.
3. *Walk through what happens from power-on to `main()` on a Cortex-M.* Strong answer: SP and reset vector loaded from the vector table, reset handler, clock setup, `.data` copy, `.bss` zeroing, C runtime init, `main`; where the linker script defines each symbol; what goes wrong if any step is skipped.
4. *An I2C sensor works for hours, then reads 0xFF forever until power-cycled. How do you debug it?* Strong answer: capture the bus with a logic analyser; suspect a stuck SDA after a reset or noise mid-transaction; check pull-up values and rise times; implement bus recovery (clock out 9 pulses, then STOP); add timeouts and error counters.
5. *How would you get a battery sensor node to last two years on 2×AA cells?* Strong answer: computes an average-current budget, chooses the deepest sleep mode compatible with wake sources, gates sensor power, batches radio transmissions, accounts for wake-up energy and self-discharge, and validates with a current trace rather than datasheet numbers.

## Resources (free first)

- **Primary texts:** Jonathan Valvano's free *Embedded Systems* materials (University of Texas) — https://users.ece.utexas.edu/~valvano/ ; Miro Samek, *Modern Embedded Systems Programming* video course (free) — https://www.state-machine.com/video-course ; The Embedded Rust Book — https://docs.rust-embedded.org/book/
- **Reference manuals:** RP2350 datasheet — https://datasheets.raspberrypi.com/rp2350/rp2350-datasheet.pdf ; STM32F446 reference manual RM0390 — https://www.st.com/resource/en/reference_manual/rm0390-stm32f446xx-advanced-armbased-32bit-mcus-stmicroelectronics.pdf ; Arm Cortex-M4 Devices Generic User Guide — https://developer.arm.com/documentation/dui0553/latest/ ; ESP-IDF Programming Guide — https://docs.espressif.com/projects/esp-idf/en/latest/ ; Raspberry Pi Pico SDK documentation — https://www.raspberrypi.com/documentation/pico-sdk/ ; CMSIS 6 — https://arm-software.github.io/CMSIS_6/
- **Practice and articles:** Interrupt (Memfault's embedded blog: fault debugging, linker scripts, low power) — https://interrupt.memfault.com/ ; Embedded Artistry — https://embeddedartistry.com/
- **Standards:** BARR-C:2018 Embedded C Coding Standard (free PDF) — https://barrgroup.com/embedded-systems/books/embedded-c-coding-standard ; SEI CERT C — https://wiki.sei.cmu.edu/confluence/display/c ; MISRA C:2025 (paid, short PDF) — https://misra.org.uk/product/misra-c2025/
- **Tools:** Wokwi — https://docs.wokwi.com/ ; Renode — https://antmicro.com/platforms/renode/ ; QEMU — https://www.qemu.org/docs/master/ ; OpenOCD — https://openocd.org/ ; probe-rs — https://probe.rs/ ; sigrok/PulseView — https://sigrok.org/ ; Unity and CMock — https://www.throwtheswitch.org/unity ; cppcheck — https://cppcheck.sourceforge.io/ ; Compiler Explorer — https://godbolt.org/
- **Paid, optional:** Elecia White, *Making Embedded Systems*, 2nd ed. (O'Reilly, 2024); Joseph Yiu, *The Definitive Guide to Arm Cortex-M3 and Cortex-M4 Processors*, 3rd ed.

## Sources

- Raspberry Pi, Pico 2 product page (RP2350 features and price) — https://www.raspberrypi.com/products/raspberry-pi-pico-2/ (checked 2026-10)
- MISRA, MISRA C:2025 product page ("supersedes all previous versions"; updated March 2025) — https://misra.org.uk/product/misra-c2025/ (checked 2026-10)
- Rust Embedded Working Group, "embedded-hal v1.0 now released!" (9 Jan 2024) — https://blog.rust-embedded.org/embedded-hal-v1/ (checked 2026-10)
- Xu et al., EmbedAgent/EmbedBench (arXiv 2506.11003, v3 Jan 2026; ICSE 2026) — https://arxiv.org/abs/2506.11003 (checked 2026-10)
- Wokwi supported hardware — https://docs.wokwi.com/getting-started/supported-hardware ; Antmicro Renode — https://antmicro.com/platforms/renode/ (checked 2026-10)

_Last reviewed: 2026-10_
