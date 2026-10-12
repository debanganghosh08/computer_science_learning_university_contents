# EMB302 · Labs and projects

Hardware: a Cortex-M board with a debug probe (STM32 Nucleo or Raspberry Pi Pico 2 with a Debug Probe), a logic analyser, and a second microcontroller board to act as a stimulus generator in P2 and P3. FreeRTOS and Zephyr are both used; every lab states which. Labs can be developed in Renode or QEMU, but timing results must come from real hardware (⚡). Every timing claim in a submission needs a trace or capture behind it.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Super-loop jitter ⚡ | Measure the jitter of a 1 ms control action in a super-loop as features are added | Jitter histogram per version; timing requirements sheet for an e-bike controller | 3 h |
| 2 · A context switch from scratch | Two tasks switching via PendSV and SysTick on Cortex-M, written by you | Code with the stacked-frame diagram; measured switch time in cycles | 5 h |
| 3 · Schedulability by hand and by trace ⚡ | Analyse a 5-task set with response-time analysis, implement it in FreeRTOS, trace it | Hand analysis, trace screenshots, a table comparing predicted and measured worst-case response times | 6 h |
| 4 · Sync primitives and their jitter ⚡ | Protect shared data with interrupt disabling, scheduler locking and a mutex | Jitter each method adds to a 1 kHz task; recommendation | 3 h |
| 5 · Priority inversion, and an AI audit ⚡ | Reproduce unbounded inversion, then fix it with inheritance and with a ceiling; audit an AI-generated version of the same design | Traces before and after; the AI audit table (defect, evidence, fix) | 5 h |
| 6 · Zero-copy pipeline | Stream 8 kHz ADC samples through a stream buffer to a processing task with deferred interrupt handling | Drop counter at zero over 30 min; ISR time and CPU load | 4 h |
| 7 · Stacks and the MPU | Size every stack two ways; catch a deliberate overflow with an MPU guard | Stack table (analysis vs high-water mark), fault log | 4 h |
| 8 · Same app in Zephyr | Port Lab 6 to Zephyr with devicetree and work queues; run tests on `native_sim` and an emulated board in CI | Port diff, CI run, idle-current comparison with FreeRTOS | 5 h |
| 9 · Trace a deadline miss ⚡ | Given a firmware image with an intermittent deadline miss, find the cause using Tracealyzer, SystemView or Zephyr tracing | Annotated trace, root cause, fix, before/after miss count | 4 h |
| 10 · Two cores ⚡ | Run a control loop on one core of an RP2350 or ESP32 and communications on the other; compare SMP and AMP set-ups | Jitter and throughput for each set-up; a lock-free mailbox with tests | 5 h |

## Projects

### P1 · A tiny preemptive kernel (L1, ~6 hours)

**Real-world inspiration.** FreeRTOS, Zephyr and every commercial RTOS are built on the same small core: a ready list, a tick, and a context switch. Writing one is the fastest way to understand what you later configure.

**What to build.** A fixed-priority preemptive kernel for Cortex-M (or RISC-V on the RP2350) supporting at least 4 tasks, `delay_ticks()`, a binary semaphore and an idle task with sleep. No dynamic allocation.

**Acceptance criteria**
- Three periodic tasks at 1 ms, 5 ms and 20 ms toggle pins; their periods on a logic analyser are within one tick of target over 10,000 periods.
- A higher-priority task becoming ready preempts a lower one within one tick (or immediately when woken by an ISR), shown on a trace.
- Context-switch time measured in cycles and reported.
- Runs under QEMU or Renode as well as on hardware, with a test script.
- Under 2 KB of code, excluding the application.

**Stretch goals.** Priority inheritance on a mutex; tickless idle with measured current savings.

**What it proves to an employer.** You understand RTOS internals, so you can debug a scheduler problem instead of guessing at configuration settings.

### P2 · A schedulability-proven data-acquisition pipeline (L2, ~15 hours)

**Real-world inspiration.** Condition-monitoring sensors on pumps and motors sample vibration at kilohertz rates, compute features and report anomalies; a dropped sample window or a late report can hide a failing bearing (illustrative scenario).

**What to build.** A FreeRTOS or Zephyr application that samples an accelerometer or ADC at 4–8 kHz with DMA, computes RMS and an FFT-based feature every 125 ms, logs features to flash, and sends a telemetry frame over UART every second, with a command task and a low-priority housekeeping task. A second board generates the input signal.

**Acceptance criteria**
- A written response-time analysis using your measured WCETs (method documented); every task's analysed worst-case response time is below its deadline.
- A 10-minute trace shows zero deadline misses and every measured worst case below the analysed bound.
- Zero dropped samples over 1 hour, proven by sequence counters.
- CPU load at most 70% in the worst-case mode, measured.
- Every task's stack has at least 25% margin after a 1-hour run with worst-case inputs.
- A frequency injected by the stimulus board is reported correctly (within one FFT bin) in 100 of 100 telemetry frames.

**Stretch goals.** Port to the other RTOS and compare footprint, idle current and worst-case latency; add an EDF variant in your P1 kernel and compare behaviour under overload.

**What it proves to an employer.** You can prove a firmware design meets its deadlines, with analysis and traces that agree, which is what senior reviewers ask for.

### P3 · A supervised battery-monitoring controller with fault injection (L3, portfolio-grade, ~30 hours)

**Real-world inspiration.** Electric vehicles, e-scooters and home inverters use a battery management system (BMS) that measures cell voltages, temperatures and current, estimates state of charge, and must open the pack's contactor quickly when a fault appears; in cars, ISO 26262 governs this kind of function. India's EV and energy-storage growth makes BMS firmware a common job description (analysis). This project is a **simulation**: inputs come from potentiometers or a second board's DAC/PWM, never from real lithium cells.

**What to build.** RTOS firmware for a simulated 4-cell monitor: periodic sampling of 4 "cell voltages", 2 temperatures and pack current; coulomb-counting state of charge; fault detection (over-voltage, under-voltage, over-temperature, over-current, sensor-stuck); a fault reaction that drives a "contactor" GPIO to its safe state; CAN or UART status frames; a command interface; task supervision with an independent watchdog; MPU isolation of the communications parser; core-dump capture. A second board runs a hardware-in-the-loop test script that injects faults and timestamps the reaction.

**Acceptance criteria**
- **Fault reaction:** over 1,000 injected faults, the time from fault stimulus to contactor GPIO change (measured by the logic analyser or the test board) is at most 10 ms, with the full distribution reported.
- **Control timing:** the 10 ms monitoring task's release jitter is at most 100 µs under worst-case communications load.
- **Supervision:** a deliberately stalled task (any of them) is detected within 500 ms and the system enters its safe state, in 20 of 20 trials; the reset reason and a core dump are retrievable afterwards.
- **Soak:** a 12-hour run with randomised communications bursts and injected delays shows zero deadline misses (trace summary attached).
- **Isolation:** malformed command frames (fuzzed, at least 10,000) never corrupt the monitoring task's data; the parser runs unprivileged.
- **Evidence pack:** requirements with numbers, a response-time analysis, a fault-tree sketch for "contactor fails to open", the test report, and a short README explaining the safe-state choices.

**Stretch goals.** Run the same firmware on Zephyr with userspace isolation; add a CAN FD link and measure bus load; write the hazard analysis in the style of ISO 26262 Part 3 (preview of EMB501).

**What it proves to an employer.** You can build supervised, fault-tolerant real-time firmware and back every timing and safety claim with evidence. Automotive, EV, industrial and medical-device teams look for exactly this.

## Feeds into

- [EMB402 Embedded and IoT Security](../../year_4/EMB402_embedded_and_iot_security/README.md): task isolation and the boot/update path become a security design.
- [EMB305 Embedded Linux](../EMB305_embedded_linux/README.md): Linux plus an RTOS core (AMP) and PREEMPT_RT comparisons.
- [EMB403 Robotics Software with ROS 2](../../year_4/EMB403_robotics_software_with_ros_2/README.md): micro-ROS runs on top of FreeRTOS or Zephyr.
- [EMB501 Frontier Seminar](../../year_5/EMB501_frontier_seminar_autonomous_systems_and_physical/README.md): P3's evidence pack is a first safety case.
- The [EMB flagship industry project](../../../../06_career_and_market_readiness/05_industry_projects/EMB_embedded_systems_iot.md): its firmware architecture comes from P2 and P3.
