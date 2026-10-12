# EMB303 · Electronics and Interfacing for Programmers

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 3 · 5 | 4 (≈ 120 hours) | L0 → L3 in electronics (L2 in software assumed) | [CS202](../../../../02_year_2_core_computer_science/semester_3/CS202_computer_architecture_and_systems_programming/README.md); take alongside [EMB301](../EMB301_microcontrollers_and_embedded_c/README.md) | [EMB403](../../year_4/EMB403_robotics_software_with_ros_2/README.md), [EMB304](../EMB304_iot_protocols_and_cloud_connectivity/README.md), [EMB404](../../year_4/EMB404_hardware_software_co_design_and_fpga_basics/README.md) |

## Why this course matters now

Many "firmware bugs" turn out to live in the circuit: a missing pull-up, a 5 V signal on a 3.3 V pin, a regulator that browns out when the radio transmits, a motor whose noise resets the microcontroller. Software engineers who can read a schematic, choose a resistor, and use an oscilloscope and a logic analyser are rare and hard to replace, and the instruments are now cheap: an 8-channel 24 MHz logic analyser costs around ₹500–900 in India and works with the free sigrok/PulseView software. Circuits are also where AI assistants are weakest: on EmbedBench (ICSE 2026), the best model reached only 55.6% pass@1 when given the schematic and 50.0% when it had to produce the schematic itself. An assistant will confidently wire a relay coil straight to a GPIO or suggest a pull-up value without knowing your bus capacitance. This course takes you from Ohm's law to bringing up a board, so you can tell when the code is innocent.

**Safety first.** This course works only with low voltages (≤ 12 V DC) from current-limited supplies, USB or small batteries. Mains (230 V AC) work is out of scope. Lithium cells are handled only in protected, commercial packs.

## Learning outcomes

By the end you can:

1. **Calculate** voltages, currents and power in DC circuits (Ohm's law, Kirchhoff's laws, dividers, RC time constants) and **confirm** them with a multimeter.
2. **Choose** components for a microcontroller interface: current-limiting resistors, pull-ups, transistor or MOSFET switches, flyback diodes, level shifters, decoupling capacitors.
3. **Explain** logic levels (VIH, VIL, VOH, VOL), push-pull vs open-drain outputs, and pin current limits, and **interface** 3.3 V and 5 V parts safely.
4. **Debounce** mechanical inputs in hardware and software and **prove** it with captures.
5. **Size** I2C pull-ups from bus capacitance and rise time, **configure** SPI modes, and **build** RS-485 and CAN links with correct termination.
6. **Use** an oscilloscope and a logic analyser correctly: probing, grounding, triggering, sample rates, protocol decoding.
7. **Drive** DC motors, servos and steppers through proper drivers and **measure** the noise they inject.
8. **Write** a power budget for a battery device and **verify** it with measurements.
9. **Read** a development board's schematic and **run** a structured bring-up of a new board.

## Chapters and lessons

### Chapter 1 · Voltage, current and resistance (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 The water analogy and its limits | Charge, voltage, current, resistance; DC vs AC; ground as a reference, not "zero" | Measure 5 battery and USB voltages; explain each reading |
| 1.2 Ohm's and Kirchhoff's laws | V = IR, KVL around loops, KCL at nodes, series and parallel | Solve 10 circuits on paper; build 3 and measure |
| 1.3 Power and heat | P = VI = I²R, resistor power ratings, why parts get hot | Find the minimum resistor wattage for 5 cases; feel the difference safely |
| 1.4 Voltage dividers | Dividers as sensors and level translators; loading effect | Build a divider to read 12 V on a 3.3 V ADC; show the loading error |
| 1.5 Using a multimeter | Voltage, resistance, continuity; measuring current in series and the blown-fuse trap | Measure an LED's current three ways |

**Check your understanding:** Why does a voltage divider's output drop when you connect a load? Why must an ammeter be in series, and what happens if you put it across a supply? Two resistors in parallel: why is the result smaller than either?

### Chapter 2 · Components a programmer must know (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Resistors and capacitors | Tolerance, E-series values, capacitor types; RC time constant; decoupling capacitors and why every IC has one | Measure an RC charge curve; compare with τ = RC |
| 2.2 Diodes and LEDs | Forward voltage, reverse protection, Schottky vs silicon, LED current limiting | Compute and verify the resistor for 3 LED colours at 3.3 V |
| 2.3 Transistors as switches | NPN BJT base resistor, logic-level N-MOSFET (Vgs threshold vs Rds(on) at 3.3 V), low-side switching | Switch a 12 V load from a 3.3 V GPIO with a MOSFET; measure its temperature |
| 2.4 Inductive loads | Relay coils and motors, flyback diodes, why a GPIO cannot drive a relay | Capture the voltage spike with and without a flyback diode on the oscilloscope |
| 2.5 Reading component datasheets | Absolute maximum vs recommended operating conditions, typical vs min/max, derating | Extract the 8 numbers that matter from a MOSFET datasheet |

**Check your understanding:** Why does a MOSFET rated "Vgs(th) = 2 V" still get hot when driven from 3.3 V? What does a flyback diode protect, and why does it slow the relay's release? Why are datasheet "typical" values dangerous to design with?

### Chapter 3 · Logic levels and GPIO electrical limits (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Logic thresholds | VIH, VIL, VOH, VOL, noise margin; CMOS vs TTL levels | Sweep an input voltage and find where your MCU switches |
| 3.2 Output types | Push-pull vs open-drain; wired-AND; drive strength settings and edge rates | Show two push-pull outputs fighting (current-limited); fix with open-drain |
| 3.3 Pull-ups and pull-downs | Floating inputs, internal vs external pull-ups, choosing values (speed vs current) | Measure the current wasted by a 1 kΩ vs 47 kΩ pull-up at 3.3 V |
| 3.4 Mixing 3.3 V and 5 V | 5 V-tolerant pins, divider level shifting, BSS138 bidirectional shifters, dedicated translators | Interface a 5 V sensor to a 3.3 V MCU three ways; scope the edges |
| 3.5 Current limits and protection | Per-pin and per-port current limits, ESD, series resistors, clamp diodes | Read the limits for your MCU; design an LED bar within them |

**Check your understanding:** Why can a floating input make a device draw extra current? When does a resistor divider fail as a level shifter? What exactly breaks when you exceed an MCU pin's absolute maximum voltage?

### Chapter 4 · Buttons, switches and encoders (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Contact bounce | What bounce looks like (duration and pattern vary by switch), why interrupts fire many times | Capture bounce on 5 different switches; record durations |
| 4.2 Hardware debouncing | RC filter plus Schmitt trigger input; component choice | Build one and capture the clean edge |
| 4.3 Software debouncing | Counter and integrator algorithms, sampling vs interrupt-driven, long press and double press | Implement and test against your captured bounce data |
| 4.4 Keypads and rotary encoders | Matrix scanning, ghosting and diodes, quadrature decoding with a state table | Read a 4×4 keypad and an encoder without missed steps |

**Check your understanding:** Why is "wait 50 ms after the first edge" a weak debounce? When is hardware debouncing worth the parts cost? Why does fast spinning of a cheap encoder lose counts, and how do you detect it?

### Chapter 5 · Analogue front ends (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Sensors as circuits | Resistive sensors (thermistor, LDR, strain gauge) in dividers and bridges; current-output sensors (4–20 mA) | Read a thermistor; linearise with the Steinhart–Hart equation |
| 5.2 Op-amp building blocks | Buffer, non-inverting gain, comparator with hysteresis, rail-to-rail limits | Buffer a high-impedance sensor; show the ADC error disappear |
| 5.3 Sampling and aliasing | Nyquist, anti-aliasing RC filters, choosing sample rate | Demonstrate aliasing of a 1.1 kHz signal sampled at 1 kHz; add a filter |
| 5.4 Grounds and references | Analogue vs digital ground, ground loops, reference stability, measuring noise | Reduce ADC noise by layout and reference changes; quantify in LSB |

**Check your understanding:** Why does a 4–20 mA loop start at 4 mA rather than 0? Why must an anti-aliasing filter sit before the ADC rather than in software? How can moving one ground wire change your readings?

### Chapter 6 · Power and power budgets (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Regulators | LDO vs buck vs boost; dropout, efficiency, quiescent current, noise | Measure efficiency of an LDO and a buck at 3 loads |
| 6.2 Batteries | Alkaline, NiMH, Li-ion/LiPo discharge curves, coin cells and pulse-current limits, protection circuits, safe handling | Log a coin cell's voltage sag under a radio-like pulse load |
| 6.3 Power budgets | Per-state current × time, duty cycle, regulator overhead, self-discharge, end-of-life voltage | Build a spreadsheet budget for a LoRa sensor; predict life |
| 6.4 Brown-out and sequencing | Brown-out reset levels, inrush, bulk capacitance, rails that must start in order | Make a board reset during radio bursts; fix it with capacitance and BOR settings |

**Check your understanding:** Why can an LDO with 2 µA quiescent current waste more energy than a buck converter in some designs? Why does a coin cell that reads 3.0 V at rest fail during transmission? What should firmware do when it detects a falling supply?

### Chapter 7 · UART, RS-232 and RS-485 (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 UART on the wire | Start/stop bits, idle-high, TTL vs RS-232 voltage levels, USB–UART bridges | Decode a UART frame from an oscilloscope trace by hand |
| 7.2 Baud-rate error | Clock tolerance budget between two devices; oversampling | Find the largest baud mismatch that still works; compare with theory |
| 7.3 RS-485 | Differential signalling, half duplex, driver enable timing, termination and biasing, long cables | Link two boards over 10 m of twisted pair at 115,200 baud |
| 7.4 Modbus RTU | Frames, CRC-16, silent intervals, typical uses in Indian factories and solar inverters | Read registers from a Modbus device or simulator |

**Check your understanding:** Why can RS-485 run hundreds of metres when TTL UART cannot run a few? What goes wrong if the driver-enable pin is released too early? Why does Modbus use silent time to mark frames?

### Chapter 8 · I2C and SPI at the electrical level (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 I2C physics | Open-drain bus, pull-up sizing from bus capacitance and rise-time limits in the NXP UM10204 specification | Measure rise time with 3 pull-up values and 2 cable lengths |
| 8.2 I2C failure modes | Address clashes, multiplexers, clock stretching, stuck SDA, hot-plugging | Diagnose 4 broken I2C set-ups from captures |
| 8.3 SPI signal integrity | Modes, chip-select timing, ringing at high clock rates, series termination | Push SPI to its failure frequency over a long jumper; fix it |
| 8.4 Choosing a bus | I2C vs SPI vs UART for sensors, displays, flash and radios | Justify the bus for 6 parts of a weather station |

**Check your understanding:** What limits how fast an I2C bus can run with a given pull-up? Why is a long ribbon cable worse for SPI than for I2C? When does a 1 kΩ pull-up become a problem?

### Chapter 9 · CAN and field buses (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 CAN basics | Differential pair, dominant and recessive bits, 120 Ω termination at both ends | Build a 2-node CAN bus with SN65HVD230 transceivers |
| 9.2 Arbitration and frames | Identifier-based priority, bit stuffing, CRC, ACK slot | Show two nodes contending; the lower ID wins on the scope |
| 9.3 Bit timing and errors | Sample point, synchronisation, error counters, error-passive and bus-off states | Mis-set one node's bit timing; watch the error counters |
| 9.4 CAN FD, LIN and tools | Higher data-phase rates; LIN for body electronics; SocketCAN, `candump`, DBC files | Log a CAN bus with SocketCAN and decode signals from a DBC file |

**Check your understanding:** Why does CAN need no collision recovery? What happens to a node that keeps transmitting errors? Why do cars still use LIN alongside CAN?

### Chapter 10 · Instruments (week 10)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Oscilloscope fundamentals | Bandwidth, sample rate, rise-time rule of thumb, ×1 vs ×10 probes, probe compensation | Compensate a probe; measure the same edge with both settings |
| 10.2 Probing technique | Long ground leads and ringing, ground-spring probing, never grounding to a different potential | Show ringing caused by a long ground lead, then remove it |
| 10.3 Triggering | Edge, pulse width, runt and serial triggers; single-shot capture of rare events | Capture a once-per-minute glitch |
| 10.4 Logic analysers | Sample rate vs signal rate, thresholds, protocol decoders in PulseView, correlating with debug pins | Decode UART, I2C and SPI in one capture with timing markers |
| 10.5 USB instruments | Capabilities and limits of low-cost USB scopes and mixed-signal tools | Write a one-page "which instrument for which question" guide |

**Check your understanding:** Why can a 24 MHz logic analyser mislead you about a 10 MHz SPI bus? What does a ×10 probe trade away? When must you use a scope instead of a logic analyser?

### Chapter 11 · Motors and actuators (week 11)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 DC motors and H-bridges | Stall current, PWM speed control, braking vs coasting, driver ICs | Drive a DC motor both ways; measure stall current safely |
| 11.2 Servos and steppers | Servo pulse control; stepper drivers (current limit, microstepping) | Run a stepper with acceleration ramps without missed steps |
| 11.3 Noise and isolation | Motor noise on supply rails, separate supplies, decoupling, optocouplers | Make motor noise reset the MCU; fix it and prove with a scope |
| 11.4 Current sensing | Shunt plus amplifier (INA219/INA226-style), Hall sensors | Plot motor current during start-up and stall |

**Check your understanding:** Why does a motor that runs fine on the bench reset the controller when it stalls? What does microstepping improve and what does it not? Why measure current on the low side or the high side?

### Chapter 12 · Schematics, boards and bring-up (weeks 12–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 12.1 Reading schematics | Symbols, net labels, hierarchical sheets, reference designators, power symbols | Trace every signal from the USB connector to the MCU on the Pico 2 or Nucleo schematic |
| 12.2 PCB basics in KiCad | Schematic capture, footprints, a two-layer layout, ground planes, design rule checks | Draw a sensor breakout board in KiCad |
| 12.3 EMC and ESD basics | Loop area, return paths, decoupling placement, ESD protection on connectors | Review 3 small boards against an EMC checklist |
| 12.4 Design for test | Test points, debug headers, current-measurement jumpers, LEDs for status | Add a test plan to your KiCad board |
| 12.5 Structured bring-up | Current-limited first power-on, rails, clocks, debug port, then one peripheral at a time; a bring-up log | Bring up a provided "mystery" board with 3 planted faults and log every step |

**Check your understanding:** Why should first power-on of a new board use a current-limited supply? What would you check if the debugger cannot connect to a new board? Why do test points save more time than they cost?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Measure everything | — |
| 2 | 2 | Lab 2 · Switching loads safely | — |
| 3 | 3 | Lab 3 · Logic levels and level shifting | — |
| 4 | 4 | Lab 4 · Bounce, captured | **P1 due** |
| 5 | 5 | Lab 5 · Analogue front end | — |
| 6 | 6 | Lab 6 · Power budget and brown-out | — |
| 7 | 7 | Lab 7 · RS-485 and Modbus | Mid-term practical (AI off) |
| 8 | 8 | Lab 8 · I2C rise times | — |
| 9 | 9 | Lab 9 · A CAN bus | — |
| 10 | 10 | Lab 10 · Instrument skills test | **P2 due** |
| 11 | 11 | Motors and noise (in P3) | — |
| 12 | 12 | KiCad board (in P3) | Schematic review |
| 13 | 12 | Mystery-board bring-up | Bring-up log |
| 14 | 12 | — | **P3 due** |
| 15 | Review | Practical exam on the bench | Final exam (AI off) |

## Working with AI in this course

- **Use AI for:** explaining a datasheet section you have located; checking your arithmetic for dividers, RC filters and power budgets; drafting a bill of materials; generating PulseView decoder scripts or Python to analyse captures; proposing a schematic-review checklist you then refine.
- **Do without AI (drills):** Ohm's law and divider calculations; pull-up sizing; reading a schematic aloud; choosing a MOSFET from a datasheet; oscilloscope set-up for a given signal. The practical exams are AI-off and on the bench.
- **Verify AI output by:** reading the datasheet's absolute-maximum and recommended-conditions tables yourself; simulating the circuit in Falstad or ngspice; measuring every rail with a multimeter **before** connecting the microcontroller; powering new circuits from a current-limited supply; capturing signals to compare with expected timing.
- **Where AI still fails here (show it yourself):** EmbedBench reports best-model pass@1 of 55.6% with a schematic and 50.0% without (arXiv 2506.11003). In Lab 2 you ask an assistant to design a relay or motor driver from a GPIO and record what it gets wrong. Common defects include driving inductive loads directly from a pin, omitting the flyback diode, picking MOSFETs that are not fully on at 3.3 V gate drive, ignoring per-pin current limits, assuming 5 V tolerance, wrong pinouts for a different board revision, and part numbers that do not exist. Check each against a datasheet and a measurement.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (10) | 25% |
| Projects P1–P3 | 35% |
| Mid-term bench practical (AI off) | 15% |
| Final bench exam (AI off) | 25% |

**Mastery gate.** You pass when you can, with AI off and on the bench: (1) given a sensor and a datasheet, design and build the interface (level shifting, pull-ups, decoupling, protection) and prove it with a capture in 60 minutes; (2) find 3 planted faults on a mystery board (for example a missing pull-up, a wrong termination, a brown-out under load) in 45 minutes with a written bring-up log; (3) produce a power budget for a battery device that matches your measured average current within 15%.

## Industry reality

Where this is used: every board bring-up, every field failure analysis and every interview at a hardware company. RS-485 and Modbus are common in industrial equipment such as solar inverters, energy meters and PLCs, CAN is standard in vehicles, and I2C and SPI connect typical low-cost sensors (analysis). The I2C specification (NXP UM10204) is free and defines the rise-time limits you design pull-ups to. Low-cost instruments have changed who can do this work: open-source sigrok/PulseView decodes dozens of protocols on analysers that cost less than a textbook.

**Interview questions from this course**

1. *How do you choose the pull-up resistor value on an I2C bus?* Strong answer: open-drain bus; lower bound from the maximum sink current (VOL at 3 mA for standard/fast mode), upper bound from bus capacitance and the rise-time limit for the chosen speed mode; typical values; measuring rise time on a scope to confirm.
2. *Why can't you drive a relay or motor directly from a GPIO, and how do you do it properly?* Strong answer: pin current limits; inductive kickback; low-side MOSFET or transistor with a gate/base resistor, flyback diode, separate supply, decoupling; logic-level MOSFET choice from Rds(on) at the actual gate voltage.
3. *A 5 V sensor must talk to a 3.3 V microcontroller. What are your options?* Strong answer: check 5 V tolerance in the datasheet; divider for slow unidirectional signals; BSS138-style bidirectional shifter for I2C; dedicated translator for fast signals; check VIH of the 5 V side when driven at 3.3 V.
4. *How does CAN arbitration work, and what happens if two nodes send at once?* Strong answer: dominant zero overrides recessive one; each transmitter reads back; the node that sees a dominant bit it did not send stops; lowest identifier wins without data loss; bit stuffing and error handling.
5. *A device resets whenever its radio transmits. How do you investigate?* Strong answer: scope the supply rail during transmission with single-shot triggering, check the brown-out threshold and reset reason, measure battery internal resistance and regulator dropout, add bulk capacitance, consider lowering transmit power or staggering loads.

## Resources (free first)

- **Primary texts:** *Lessons in Electric Circuits* (free, All About Circuits) — https://www.allaboutcircuits.com/textbook/ ; MIT 6.002 Circuits and Electronics (OCW) — https://ocw.mit.edu/courses/6-002-circuits-and-electronics-spring-2007/ ; SparkFun tutorials (pull-ups, logic levels, I2C, SPI, serial) — https://learn.sparkfun.com/tutorials
- **Specifications and application notes:** NXP UM10204, *I2C-bus specification and user manual* — https://www.nxp.com/docs/en/user-guide/UM10204.pdf ; TI SLVA704, *Understanding the I2C Bus* — https://www.ti.com/lit/an/slva704/slva704.pdf ; TI SLOA101, *Introduction to the Controller Area Network* — https://www.ti.com/lit/an/sloa101b/sloa101b.pdf ; Jack Ganssle, *A Guide to Debouncing* — http://www.ganssle.com/debouncing.htm
- **Tools:** sigrok and PulseView — https://sigrok.org/ ; Falstad circuit simulator — https://www.falstad.com/circuit/ ; ngspice — https://ngspice.sourceforge.io/ ; KiCad — https://www.kicad.org/ ; Linux SocketCAN documentation — https://docs.kernel.org/networking/can.html ; Wokwi (virtual logic analyser for firmware-side practice) — https://docs.wokwi.com/
- **Board schematics to study:** Raspberry Pi Pico 2 datasheet (includes schematic) — https://datasheets.raspberrypi.com/pico/pico-2-datasheet.pdf
- **Paid, optional:** Horowitz and Hill, *The Art of Electronics*, 3rd ed. (the reference); Scherz and Monk, *Practical Electronics for Inventors*, 4th ed. (gentler).

## Sources

- Xu et al., EmbedAgent/EmbedBench (arXiv 2506.11003, v3 Jan 2026; ICSE 2026) — https://arxiv.org/abs/2506.11003 (checked 2026-10)
- Logic analyser prices: Robu.in listings seen via search, 12 Oct 2026 — https://robu.in/product/usb-logic-analyze-24m-8ch-mcu-arm-fpga-dsp-debug-tool/ (checked 2026-10)
- NXP UM10204 I2C-bus specification — https://www.nxp.com/docs/en/user-guide/UM10204.pdf (checked 2026-10)

_Last reviewed: 2026-10_
