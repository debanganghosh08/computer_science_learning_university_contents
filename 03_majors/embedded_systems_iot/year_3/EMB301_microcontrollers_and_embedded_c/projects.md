# EMB301 · Labs and projects

Hardware: an STM32 Nucleo-64 board (for example NUCLEO-F446RE) **or** a Raspberry Pi Pico 2, plus an 8-channel logic analyser and a multimeter (see the [kit list](../../README.md#9-a-budget-hardware-kit)). Every lab can be started in Wokwi or Renode; labs marked ⚡ need real hardware for the final measurement. All C compiles with `-Wall -Wextra -Werror` and every repository has a README stating the exact part number, SDK version and how to reproduce each measurement.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Toolchains and simulators | Build and flash blink with the vendor SDK, with CMake and `arm-none-eabi-gcc`, and in Wokwi or Renode | Build logs, binary sizes, a screenshot of the simulated pin waveform | 3 h |
| 2 · GPIO from raw registers | Drive an LED and read a button using only addresses from the reference manual; then use the SVD-generated header | Code, the manual page references for every register, an `-O0` vs `-O2` disassembly showing why `volatile` matters | 3 h |
| 3 · Startup code and linker script | Replace the vendor startup file and linker script with your own; place one function in RAM | Startup file, linker script, annotated map file, measured speed-up of the RAM function | 4 h |
| 4 · Interrupt latency ⚡ | Measure GPIO-edge-to-ISR-response latency and jitter over 10,000 events at two priorities and with a competing interrupt | Histogram, worst case, explanation of each component of the latency | 4 h |
| 5 · Timers and PWM | Generate 1 kHz, 50 Hz servo and 38 kHz carrier signals; measure an unknown frequency by input capture | Hand calculations, analyser captures within 0.5% of target | 4 h |
| 6 · ADC with DMA | Timer-triggered 8 kHz sampling into a double buffer; characterise noise before and after 16× oversampling | Noise statistics in LSB, CPU load measured with a GPIO marker | 4 h |
| 7 · I2C driver from the datasheet, and an AI audit | Write a BME280 driver at register level; ask an AI assistant for the same driver for your exact MCU and audit it | Your driver with annotated bus captures; an audit table (defect, how found, reference-manual page) | 5 h |
| 8 · Same driver, four ways | Implement UART echo with bare metal, vendor HAL/LL, Zephyr and Rust `embedded-hal` | Table of code size, RAM, latency and lines of code; one paragraph per option on when you would choose it | 5 h |
| 9 · Bug hunt with a debugger | Find 5 planted bugs (stack overflow, missing `.bss` init, missing `volatile`, wrong clock config, ISR flag cleared late) using GDB, watchpoints, fault registers and RTT | A bug log: symptom, hypothesis, tool, evidence, root cause, fix | 6 h |
| 10 · Sleep current ⚡ | Measure run, sleep and deepest-sleep current; find three hidden drains on a provided circuit | Current table, a charge-per-cycle plot, the fixes and their effect | 4 h |

## Projects

### P1 · Bare-metal heartbeat and latency meter (L1, ~6 hours)

**Real-world inspiration.** Power converters and motor drives rely on fast interrupt response to shut down on over-current; a firmware engineer must know, not guess, how long that response takes (illustrative scenario).

**What to build.** A firmware image with your own startup code and linker script (no vendor startup file) that blinks a heartbeat LED from a hardware timer interrupt, debounces a button in software, and measures its own interrupt latency: an external signal (from a second board or a timer output looped back) triggers an interrupt that toggles a pin, and a capture timer records the delay.

**Acceptance criteria**
- Boots and runs from your startup code; the map file is annotated to show `.text`, `.data`, `.bss`, stack and vector table.
- Binary under 4 KB at `-Os`.
- Latency histogram from at least 10,000 events, with minimum, median and maximum in CPU cycles and nanoseconds; the maximum is explained (flash wait states, priority, competing interrupt).
- Debounce: zero false presses in 100 presses of a deliberately bouncy switch, verified with the analyser.
- Same image runs in Renode or Wokwi with the heartbeat visible in the simulated trace.

**Stretch goals.** Port to the RISC-V cores of the RP2350 and compare latency; move the ISR to RAM and measure the difference.

**What it proves to an employer.** You understand what happens below `main()` and you measure timing instead of assuming it.

### P2 · Portable sensor driver library with host tests (L2, ~15 hours)

**Real-world inspiration.** Cold-chain loggers for vaccines and food log temperature and humidity on cheap MCUs, and their makers often change MCU vendor when chip supply or prices change (illustrative scenario); drivers that separate device logic from the bus survive such ports.

**What to build.** A C driver library for a BME280 (I2C) and a MAX31855 thermocouple interface (SPI) with a bus abstraction layer, running on two different MCU families (for example STM32 and RP2350) and on the host against a fake bus that replays recorded transactions.

**Acceptance criteria**
- Identical device-driver source compiles for both MCUs and the host; only the bus layer differs.
- Readings agree with a reference thermometer within the sensor's datasheet tolerance across at least 3 temperature points.
- Host unit tests (Unity or equivalent) cover at least 80% of driver lines, including error paths (NACK, CRC or fault bits, bus timeout), and run in CI on every push.
- I2C bus recovery works: a deliberately hung bus (MCU reset mid-read) recovers without power cycling in 10 of 10 trials.
- Annotated logic-analyser captures for initialisation and one measurement on each bus.
- An AI-audit section: at least one AI-generated draft, every defect found in it, and how each was detected.

**Stretch goals.** A Rust version using `embedded-hal` 1.0 traits; DMA-based non-blocking reads with a callback API.

**What it proves to an employer.** You write drivers that are testable, portable and verified on the wire, which is a large part of the daily work of a firmware team.

### P3 · Low-power field sensor node with a fail-safe bootloader (L3, portfolio-grade, ~30 hours)

**Real-world inspiration.** India had installed 7.24 crore smart meters by 30 June 2026 against 20.33 crore sanctioned under RDSS ([T&D India](https://www.tndindia.com/indias-smart-meter-population-at-7-24-crore-parliament/amp/)); each is a low-power embedded device that must log data, survive power loss and accept firmware updates for years. Farm soil-moisture nodes and pharmacy cold-chain loggers have the same constraints at smaller scale (illustrative).

**What to build.** A battery-powered node that wakes on an RTC alarm, samples sensors (DMA-driven ADC plus your P2 drivers), stores timestamped records in a wear-levelled flash log, exposes a UART/USB command shell for configuration and log download, and goes back to its deepest usable sleep mode. Add a two-slot bootloader that validates an image header and CRC32, keeps the old image until the new one is verified, and records reset reasons. Use an independent watchdog.

**Acceptance criteria**
- **Power:** a measured current trace for one full wake cycle; average current within 10% of your written budget; sleep current at the MCU supply (for example the IDD jumper on a Nucleo) of 50 µA or less, or a documented breakdown showing which board component prevents it. Projected life of at least 2 years on 2×AA at a 15-minute reporting interval, with the calculation shown.
- **Data integrity:** 10,000 records written and read back with zero corruption; the log survives 20 random power cuts during writes with at most the in-flight record lost.
- **Update safety:** 50 deliberately corrupted images (bit flips, truncation, wrong length) are all rejected; 20 power cuts at random points during an update always leave a bootable valid image (old or new).
- **Robustness:** a forced firmware hang is recovered by the watchdog within 2 seconds, and the reset reason is logged and readable from the shell.
- **Quality:** static analysis (GCC warnings, cppcheck with the MISRA add-on, clang-tidy) with every remaining finding justified in a deviation table; host tests in CI; version and git hash printed at boot.
- A one-page design note: sleep-mode choice, budget, flash layout, failure modes considered.

**Stretch goals.** Add a BLE or LoRa radio and include its energy in the budget (preview of EMB304); sign images instead of only checksumming them (preview of EMB402); run the whole test suite in Renode in CI.

**What it proves to an employer.** You can build a device that lasts in the field: measured power, data that survives power loss and an update path that cannot brick the product. This is core work in IoT hardware startups and in meter, wearable and industrial-sensor teams.

## Feeds into

- [EMB302 Real-Time Operating Systems](../EMB302_real_time_operating_systems/README.md): the P3 node's loop becomes RTOS tasks with deadlines.
- [EMB304 IoT Protocols and Cloud Connectivity](../EMB304_iot_protocols_and_cloud_connectivity/README.md): the node gains a radio and a cloud backend.
- [EMB401 Edge AI and TinyML](../../year_4/EMB401_edge_ai_and_tinyml/README.md): the node runs an anomaly-detection model on its own samples.
- [EMB402 Embedded and IoT Security](../../year_4/EMB402_embedded_and_iot_security/README.md): the CRC-checked bootloader becomes a signed, rollback-protected secure boot chain.
- The [EMB flagship industry project](../../../../06_career_and_market_readiness/05_industry_projects/EMB_embedded_systems_iot.md): P3 is its node hardware and firmware base.
