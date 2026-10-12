# EMB · Embedded Systems and IoT: roles and market (2026)

| Learning path | Interview loop | AI impact | Market overview |
|---|---|---|---|
| [Embedded Systems and IoT major](../../../03_majors/embedded_systems_iot/README.md) | [AI-driven interviews](../../04_ai_driven_interviews/) | [Matrix row](../ai_impact_matrix.md) | [Market map](../README.md) |

All figures were checked in October 2026. Paragraphs marked **Analysis** are interpretation, not measurement.

## Role titles and seniority ladder

| Level | Common titles |
|---|---|
| Entry | Embedded Software Engineer (Trainee/I), Firmware Engineer, IoT Developer, Graduate Engineer (electronics) |
| Mid | Embedded Software Engineer, Embedded Linux Engineer, BSP/Driver Engineer, IoT Engineer, Robotics Software Engineer |
| Senior | Senior Firmware Engineer, Embedded Architect, Edge AI Engineer, Functional Safety Engineer |
| Staff and above | Principal Embedded Engineer, Systems Architect, Head of Firmware |

Neighbouring hardware roles include hardware design engineer, FPGA engineer and semiconductor verification engineer (EMB404). Industries: automotive and electric vehicles, consumer electronics, industrial automation, medical devices, telecom, defence, and semiconductors.

## What the work looks like day to day

- Write C (and increasingly C++ or Rust) for microcontrollers with kilobytes of memory (EMB301).
- Schedule tasks under a real-time operating system such as FreeRTOS or Zephyr, meeting deadlines (EMB302).
- Write and debug drivers for sensors and peripherals over I2C, SPI and UART, using an oscilloscope or logic analyser (EMB303).
- Connect devices with MQTT, BLE or cellular, and send telemetry to the cloud (EMB304).
- Build and maintain embedded Linux images (Yocto, device trees) (EMB305).
- Run small ML models on devices: keyword spotting, anomaly detection, vision (EMB401).
- Secure devices: secure boot, signed over-the-air updates, key storage (EMB402).
- Work on robots with ROS 2 (EMB403).

## Demand signals

- **Global employer survey.** "Internet of Things Specialists" and "Autonomous and Electric Vehicle Specialists" are among the 15 fastest-growing jobs to 2030. In India, 35% of employers expect semiconductors and computing technologies to transform their operations, above the global rate ([WEF 2025](https://reports.weforum.org/docs/WEF_Future_of_Jobs_Report_2025.pdf)).
- **Devices.** Connected IoT devices reached 18.5 billion in 2024 and are forecast to reach 39 billion in 2030 ([IoT Analytics, Oct 2025](https://iot-analytics.com/number-connected-iot-devices/)).
- **US projections.** Computer hardware engineers +9% and electrical and electronics engineers +8% from 2025 to 2035 ([BLS](https://www.bls.gov/ooh/architecture-and-engineering/computer-hardware-engineers.htm); [BLS](https://www.bls.gov/ooh/architecture-and-engineering/electrical-and-electronics-engineers.htm)).
- **US postings.** Indeed's "Electrical Engineering" postings index was 152.0 on 2 Oct 2026 (1 Feb 2020 = 100), far above software development at 78.3 ([Indeed Hiring Lab data](https://github.com/hiring-lab/job_postings_tracker)). The category is broader than embedded software, but the contrast is striking.
- **Recent graduates.** US electrical engineering graduates had 3.2% unemployment in 2024, against 7.0% for computer science and 7.8% for computer engineering ([New York Fed](https://www.newyorkfed.org/research/college-labor-market)).
- **India.** NASSCOM notes Indian providers are positioning engineering research and development (ER&D) as a "strategic pivot", with global ER&D spend projected at about $2.5 trillion by 2030 ([NASSCOM 2026](https://nasscom.in/knowledge-center/publications/technology-sector-india-strategic-review-2026)).

## How AI is changing the role

**Automated or mostly automated (analysis).** Register-definition and driver boilerplate, reading long datasheets for a specific setting, unit tests for pure logic, build scripts, and log parsing.

**Augmented.** Debugging timing and concurrency issues from traces, porting code between microcontroller families, code review for undefined behaviour and memory errors.

**Growing in value.**

- Hardware–software debugging with instruments. The bug may be in the board, the clock or the power supply, not the code.
- Real-time reasoning: worst-case execution time, interrupt latency, priority inversion.
- Safety and security standards (for example ISO 26262 in automotive, IEC 62304 in medical devices) where every change needs traceable evidence.
- Edge AI: fitting models into tight memory, latency and power budgets.
- Device security across a long product life.

**Analysis.** Embedded work has strong natural brakes on AI automation: code must run on specific hardware, timing must be proven, and failures can be physical or safety-critical. AI helps with the text-heavy parts, but the engineer still has to make the board work. Combined with the hardware posting data above, this is one of the more resilient software-adjacent families.

## Pay (indicative)

| Market | Role in source | Figure | Type | Source |
|---|---|---|---|---|
| US | Computer hardware engineers | Median $161,740; 10th $92,940; 90th $225,330 (May 2025) | Official survey | [BLS](https://www.bls.gov/ooh/architecture-and-engineering/computer-hardware-engineers.htm) |
| US | Electronics engineers, except computer | Median $130,220; 10th $81,840; 90th $206,960 (May 2025) | Official survey | [BLS](https://www.bls.gov/ooh/architecture-and-engineering/electrical-and-electronics-engineers.htm) |
| India | Embedded Software Engineer | Average base ₹5.8 lakh; base range ₹2.3–10 lakh; under 1 year ≈₹4.1 lakh total (186 profiles, Jun 2026) | Self-reported, whole market | [Payscale](https://www.payscale.com/research/IN/Job=Embedded_Software_Engineer/Salary) |
| India | Firmware Engineer | Average base ₹6.4 lakh (49 profiles, Apr 2026) | Self-reported, small sample | [Payscale](https://www.payscale.com/research/IN/Job=Firmware_Engineer/Salary) |
| India | Hardware Engineer | Median total pay ₹44.6 lakh; 25th ₹28.3 lakh; 90th ₹92.7 lakh (815 submissions) | Self-reported, mostly semiconductor and product companies | [Levels.fyi](https://www.levels.fyi/t/hardware-engineer/locations/india) |

The gap between the two India sources is large: embedded services work pays much less than design roles at semiconductor and device companies.

## The hiring loop

Typical loop (varies by company):

1. C fundamentals: pointers, memory layout, bit manipulation, `volatile`, undefined behaviour.
2. Embedded concepts: interrupts, DMA, RTOS scheduling, mutexes and priority inversion, memory-mapped I/O.
3. Debugging scenario: "the device resets randomly in the field; how do you find out why?"
4. Electronics basics: reading a schematic, pull-up resistors, communication buses.
5. Sometimes a take-home with a development board, or a coding round on constrained data structures.
6. Behavioural: a hard bug you found, working with hardware teams.

See [AI-driven interviews](../../04_ai_driven_interviews/).

## Durable skills that make you hard to replace

- C and computer architecture (caches, memory, interrupts).
- RTOS and concurrency on constrained systems.
- Electronics literacy and lab instruments.
- Communication protocols and wireless basics.
- Device security and update design.
- TinyML and model optimisation.
- Documentation discipline for safety-critical work.

## Adjacent roles and transitions

- **Edge AI and secure IoT**: overlap OV09 ([MLE](MLE_machine_learning_engineering.md)).
- **Robotics and autonomous systems** (EMB403, EMB501).
- **Mobile and wearables** ([MOB](MOB_mobile_engineering.md)).
- **IoT security** ([SEC](SEC_cybersecurity_defense.md)).
- **Networking and telecom** ([NET](NET_it_infrastructure_networking.md)).
- **Semiconductor design and verification** via EMB404.

## Sources

All checked October 2026.

- WEF, Future of Jobs Report 2025. https://reports.weforum.org/docs/WEF_Future_of_Jobs_Report_2025.pdf
- IoT Analytics, Number of connected IoT devices (28 Oct 2025). https://iot-analytics.com/number-connected-iot-devices/
- BLS, Occupational Outlook Handbook: Computer Hardware Engineers; Electrical and Electronics Engineers (2025–35; May 2025 pay; modified 27 Aug 2026). https://www.bls.gov/ooh/architecture-and-engineering/computer-hardware-engineers.htm ; https://www.bls.gov/ooh/architecture-and-engineering/electrical-and-electronics-engineers.htm
- Indeed Hiring Lab, job postings tracker (to 2 Oct 2026). https://github.com/hiring-lab/job_postings_tracker
- Federal Reserve Bank of New York, outcomes by major (released 4 Feb 2026; 2024 data). https://www.newyorkfed.org/research/college-labor-market
- NASSCOM, Strategic Review 2026. https://nasscom.in/knowledge-center/publications/technology-sector-india-strategic-review-2026
- Payscale India: Embedded Software Engineer; Firmware Engineer. Levels.fyi India: Hardware Engineer (self-reported; 12 Oct 2026). https://www.payscale.com/research/IN/Job=Embedded_Software_Engineer/Salary ; https://www.payscale.com/research/IN/Job=Firmware_Engineer/Salary ; https://www.levels.fyi/t/hardware-engineer/locations/india

_Last reviewed: 2026-10_
