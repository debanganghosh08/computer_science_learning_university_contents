# EMB303 · Labs and projects

Bench: a multimeter, a logic analyser, access to an oscilloscope (lab, club or a low-cost USB scope), a current-limited bench supply or USB power with a current meter, a breadboard and the [kit list](../../README.md#9-a-budget-hardware-kit) parts. Low voltage only (≤ 12 V DC); no mains; lithium cells only in protected commercial packs. Every lab submission includes photos of the set-up, the instrument settings, and captures with cursors or measurements visible.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Measure everything | Verify Ohm's law, a divider under load and an LED circuit; measure current three ways | Calculations next to measurements, with error explained | 3 h |
| 2 · Switching loads safely, and an AI audit | Switch a 12 V load and a relay from a 3.3 V GPIO with a MOSFET and flyback diode; ask an AI for the same design and audit it | Scope captures with and without the diode; audit table (defect, datasheet evidence) | 4 h |
| 3 · Logic levels and level shifting | Find your MCU's real switching thresholds; interface a 5 V part three ways | Threshold sweep plot; edge captures for each shifter | 4 h |
| 4 · Bounce, captured | Capture bounce on 5 switches; build hardware and software debouncing | Bounce statistics; zero-false-press test log | 3 h |
| 5 · Analogue front end | Read a thermistor through a buffer and anti-aliasing filter; demonstrate and fix aliasing | Linearised temperature vs reference thermometer; noise in LSB before and after | 4 h |
| 6 · Power budget and brown-out | Log a coin cell and a LiPo pack under pulsed load; reproduce and fix a radio-induced brown-out | Voltage-sag captures; budget spreadsheet; fix with evidence | 4 h |
| 7 · RS-485 and Modbus | Link two boards over 10 m of twisted pair; read registers with Modbus RTU | Captures of A/B lines with and without termination; error counts | 4 h |
| 8 · I2C rise times | Measure rise time with three pull-up values and two cable lengths; find the failure point at 400 kHz | Rise-time table vs the UM10204 limits; recommended values | 3 h |
| 9 · A CAN bus | Two-node CAN at 500 kbit/s with SN65HVD230 transceivers; arbitration and an error scenario | Scope capture of arbitration; error-counter log; SocketCAN capture decoded with a DBC file | 5 h |
| 10 · Instrument skills test | Timed tasks: compensate a probe, catch a rare glitch with a single-shot trigger, decode three buses in one capture | Captures and a short written answer per task | 3 h |

## Projects

### P1 · A correct I/O interface board (L1, ~6 hours)

**Real-world inspiration.** Appliance and industrial control panels combine buttons, indicator LEDs, a switched load and sensors at mixed voltages; interface mistakes, rather than code, are a common cause of field returns from such panels (illustrative scenario).

**What to build.** A breadboard or perfboard interface for a 3.3 V microcontroller with 4 debounced buttons, an 8-LED bar, a MOSFET-switched 12 V load (a small fan or relay), and a 5 V sensor level-shifted to 3.3 V. Draw the schematic in KiCad.

**Acceptance criteria**
- Every GPIO current and the total port current, measured, are within the MCU datasheet limits (table with datasheet references).
- Zero false presses in 200 presses per button, shown with a press counter and analyser captures of raw vs debounced signals.
- The MOSFET drain voltage spike at switch-off stays below 70% of the MOSFET's rated Vds (scope capture), and the MOSFET case temperature stays within 15 °C of ambient at full load after 10 minutes.
- The level-shifted signal meets the MCU's VIH and VIL with at least 0.3 V margin (scope capture with cursors).
- KiCad schematic passes ERC; every component value is justified in a short table.

**Stretch goals.** Replace software debouncing with an RC plus Schmitt-trigger circuit and compare interrupt counts; add reverse-polarity protection to the 12 V input.

**What it proves to an employer.** You can connect real hardware to a microcontroller without damaging it, and you justify every part with a datasheet number.

### P2 · An industrial sensor node on RS-485 and CAN (L2, ~15 hours)

**Real-world inspiration.** Factories, solar plants and building-management systems commonly connect energy meters, inverters and sensors with Modbus RTU over RS-485, and vehicles and machines use CAN (illustrative of typical deployments; check any specific site's documentation).

**What to build.** A Modbus RTU slave that exposes temperature, humidity and a digital-input count as holding registers over RS-485, plus a CAN node that broadcasts the same values in frames described by a DBC file. Use correct termination and biasing; document the wiring.

**Acceptance criteria**
- 10,000 Modbus transactions over at least 10 m of twisted pair at both 19,200 and 115,200 baud with at most 1 failed transaction in each run, polled by an independent tool (for example `mbpoll` or a desktop Modbus master).
- Driver-enable timing captured on the scope: the driver releases only after the last stop bit.
- Bus waveforms captured with and without termination; the README explains the difference.
- CAN at 500 kbit/s between two nodes for 1 hour with transmit and receive error counters at zero; measured bus load reported; a SocketCAN log decoded with your DBC file.
- A deliberately mis-timed CAN node is detected by error counters and the healthy node keeps operating.

**Stretch goals.** Add galvanic isolation on the RS-485 side and explain when it is required; move to CAN FD and measure the data-phase rate achieved.

**What it proves to an employer.** You can build and debug the field buses that industrial, energy and automotive systems actually use, with evidence from the wire.

### P3 · Design, build and bring up your own board (L3, portfolio-grade, ~30 hours)

**Real-world inspiration.** Small irrigation and pump controllers for farms combine a battery or solar input, sensors, a motor driver and a field bus or radio; they must survive electrical noise, long cables and careless wiring (illustrative scenario). A board designer and a firmware engineer usually share this work; here you do both.

**What to build.** A KiCad design for a controller board: protected power input (reverse polarity, transient suppression), regulator chosen from a written power budget, a socket or footprint for a Pico 2 or an STM32 module, I2C sensors with pull-ups sized from measured capacitance, a pump or motor driver with current sensing, an RS-485 or CAN transceiver, test points and a current-measurement jumper. Fabricate it (a two-layer board from any prototype service) or, if fabrication is not possible, build it on perfboard with the same schematic. Bring it up with a written log, then write firmware that runs the motor and reports over the bus.

**Acceptance criteria**
- KiCad ERC and DRC clean; bill of materials with part numbers, prices and alternates; a peer schematic review with every finding resolved or justified.
- A bring-up log covering first power-on under current limit, every rail measured, clock and debug-port checks, then each peripheral in turn.
- Measured average current within 15% of the written power budget in each operating mode.
- I2C rise time within the UM10204 limit for your chosen speed mode, measured on the scope.
- 100 consecutive motor starts (including 10 deliberate stalls) with zero microcontroller resets, proven by a reset counter and a supply-rail capture during the worst start.
- Bus communication error-free for 1 hour with the motor running.
- An EMC/ESD checklist applied to the layout, with photos of the finished board.

**Stretch goals.** Add a solar charging input and log a day of charge/discharge; design a panel-mount enclosure; run a simple conducted-noise comparison before and after adding filtering.

**What it proves to an employer.** You can take a product from schematic to a working, measured board and own the boundary where many embedded bugs hide. Hardware startups and small product teams hire for this combination.

## Feeds into

- [EMB403 Robotics Software with ROS 2](../../year_4/EMB403_robotics_software_with_ros_2/README.md): motors, encoders, IMUs and current sensing become a robot's hardware layer.
- [EMB304 IoT Protocols and Cloud Connectivity](../EMB304_iot_protocols_and_cloud_connectivity/README.md): the P3 board gains a radio and a cloud backend.
- [EMB404 Hardware-Software Co-Design and FPGA Basics](../../year_4/EMB404_hardware_software_co_design_and_fpga_basics/README.md): digital interfaces move into programmable logic.
- [EMB402 Embedded and IoT Security](../../year_4/EMB402_embedded_and_iot_security/README.md): debug ports and test points become part of the threat model.
- The [EMB flagship industry project](../../../../06_career_and_market_readiness/05_industry_projects/EMB_embedded_systems_iot.md): node hardware and its power budget.
