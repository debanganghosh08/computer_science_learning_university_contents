# EMB302 · Real-Time Operating Systems

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 3 · 5 | 4 (≈ 120 hours) | L2 → L3 | [CS202](../../../../02_year_2_core_computer_science/semester_3/CS202_computer_architecture_and_systems_programming/README.md) (with [CS203](../../../../02_year_2_core_computer_science/semester_3/CS203_operating_systems/README.md) and [EMB301](../EMB301_microcontrollers_and_embedded_c/README.md) chapters 1–4 alongside) | [EMB402](../../year_4/EMB402_embedded_and_iot_security/README.md), [EMB305](../EMB305_embedded_linux/README.md), [EMB403](../../year_4/EMB403_robotics_software_with_ros_2/README.md) |

## Why this course matters now

A real-time system is correct only if it is right **and on time**: an airbag controller that computes the perfect answer 5 ms late has failed. Many connected devices run a real-time operating system (RTOS); two widely used open-source kernels are FreeRTOS (kernel V11.3.1, August 2026, with symmetric multiprocessing in the main kernel since V11) and Zephyr (4.4 released April 2026; the 3.7 long-term-support line is maintained until July 2029). The classic failure is still the one NASA's Mars Pathfinder hit in 1997: a low-priority task held a lock that a high-priority task needed while a medium-priority task ran, and the watchdog kept resetting the spacecraft until engineers enabled priority inheritance remotely. AI assistants generate task, queue and semaphore code fluently, but they cannot see a timeline: they do not know your worst-case execution times, your interrupt load or which lock a medium-priority task never touches. This course teaches you to reason about time on paper, prove schedulability, and confirm it with traces.

## Learning outcomes

By the end you can:

1. **Classify** timing requirements (hard, firm, soft; period, deadline, jitter) and **write** them as testable numbers.
2. **Explain and implement** a context switch on a Cortex-M (PendSV, SysTick, exception stacking).
3. **Prove** schedulability with the Liu–Layland bound and exact response-time analysis, including blocking terms, and **compare** rate-monotonic with EDF.
4. **Build** applications with tasks, queues, semaphores, mutexes, event groups and task notifications in FreeRTOS and Zephyr.
5. **Diagnose and prevent** priority inversion, deadlock and starvation, and **choose** between priority inheritance and priority ceiling.
6. **Size** stacks and heaps from measurements and analysis, and **detect** overflows with the MPU.
7. **Measure** execution times, latencies and CPU load with cycle counters and trace tools (Tracealyzer, SystemView, Zephyr tracing).
8. **Design** watchdog supervision and recovery so that a stuck task is detected and handled.
9. **Decide** between bare metal, an RTOS, and Linux with PREEMPT_RT for a given requirement.

## Chapters and lessons

### Chapter 1 · What "real-time" means (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Time as a correctness condition | Hard, firm and soft deadlines; release time, period, deadline, response time, jitter; examples (ABS brakes, audio, telemetry) | Write timing requirements for an e-bike controller as numbers |
| 1.2 Why a super-loop breaks | Worst-case loop time grows with every feature; latency of the slowest path | Add one slow feature to a loop and measure how a 1 ms control task's jitter explodes |
| 1.3 The RTOS landscape | FreeRTOS (MIT), Zephyr (Apache 2.0), Eclipse ThreadX, NuttX, RTEMS; commercial and safety-certified kernels (QNX, VxWorks, SAFERTOS) | Compare 4 kernels on licence, footprint, certification, tooling |
| 1.4 RTOS vs Linux | Determinism vs features; PREEMPT_RT in mainline Linux since 6.12 (2024); when you need both (AMP) | Decide RTOS, Linux or both for 6 product briefs |

**Check your understanding:** Why is average latency the wrong metric for a hard real-time task? What makes a soft deadline "soft" in money terms? Why can a faster CPU still miss deadlines?

### Chapter 2 · Tasks and the context switch (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Task anatomy | Task control block, private stack, states (ready, running, blocked, suspended), idle task | Draw the state machine and trace it from FreeRTOS source |
| 2.2 Context switching on Cortex-M | Exception stacking, PendSV at lowest priority, SysTick tick, MSP vs PSP, lazy FPU stacking | Write a two-task round-robin switcher in about 100 lines of C and assembly |
| 2.3 Ticks and tickless idle | Tick rate trade-offs, timer resolution, tickless idle for low power | Measure power with 1 kHz ticks vs tickless idle |
| 2.4 Creating tasks safely | Static vs dynamic creation, priorities, stack size parameters, task deletion pitfalls | Port your EMB301 P3 loop into 3 FreeRTOS tasks |

**Check your understanding:** Why is PendSV given the lowest priority? What state does a task need saved that the hardware does not stack automatically? Why can a 10 kHz tick be a bad idea?

### Chapter 3 · Scheduling theory (weeks 3–4)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Fixed-priority preemptive scheduling | The task model (C, T, D), critical instant, utilisation | Simulate 3 tasks by hand on a timeline |
| 3.2 Rate-monotonic and the Liu–Layland bound | U ≤ n(2^(1/n) − 1), about 69.3% as n grows; sufficient, not necessary | Find a task set above the bound that is still schedulable |
| 3.3 Response-time analysis | Exact iterative test R = C + Σ⌈R/Tj⌉Cj; adding blocking B and release jitter | Analyse a 5-task set; confirm with a real trace |
| 3.4 Deadline-monotonic and EDF | D < T cases; EDF's 100% bound and its overload behaviour | Overload both schedulers; compare which tasks miss |
| 3.5 Interrupts in the analysis | ISRs as highest-priority "tasks", deferred handling, interrupt storms | Add a 10 kHz ISR to your analysis; find the new worst case |

**Check your understanding:** Why is the critical instant the worst case for fixed-priority scheduling? EDF schedules everything up to 100% utilisation, so why do common kernels such as FreeRTOS schedule by fixed priority? What happens to your analysis if one task's WCET was measured, not bounded?

### Chapter 4 · Synchronisation primitives (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Critical sections | Disabling interrupts vs scheduler locking vs mutexes; cost of each | Measure the jitter each one adds to a 1 kHz task |
| 4.2 Semaphores and mutexes | Binary and counting semaphores for signalling; mutexes for ownership; recursive mutexes | Build a producer–consumer with each and explain which is right |
| 4.3 Event groups and task notifications | Waiting on combinations of events; notifications as lightweight semaphores | Replace 3 semaphores with task notifications; measure RAM and speed |
| 4.4 Deadlock | Coffman conditions, lock ordering, timeouts, detecting deadlock from a trace | Create and break a two-lock deadlock |

**Check your understanding:** Why should a mutex never be given from an ISR? When is a counting semaphore better than a queue? Why does a timeout on every lock not solve deadlock?

### Chapter 5 · Priority inversion (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Bounded and unbounded inversion | The three-task pattern; why the medium task causes unbounded blocking | Reproduce unbounded inversion on hardware with a trace |
| 5.2 Mars Pathfinder | The 1997 resets, the information-bus mutex, the fix by enabling priority inheritance on the spacecraft | Write a one-page post-mortem from the published accounts |
| 5.3 Priority inheritance | How it bounds blocking, chained blocking, FreeRTOS and Zephyr implementations | Fix your reproduction with inheritance; measure the new worst case |
| 5.4 Priority ceiling protocols | Immediate ceiling, original ceiling protocol, deadlock freedom; blocking term B in response-time analysis | Recompute the response-time analysis with B from each protocol |

**Check your understanding:** Why did the Pathfinder bug not appear in most ground tests? What does the ceiling protocol prevent that inheritance does not? How would you detect inversion in a field device with no debugger?

### Chapter 6 · Inter-task communication (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Queues | Copy semantics, depth sizing from rates, blocking send/receive, backpressure | Size a queue from producer bursts and consumer service time; verify no overflow |
| 6.2 Stream and message buffers, mailboxes, pipes | Zero-copy patterns, pointer passing with ownership rules | Stream ADC samples to a processing task at 8 kHz without copies |
| 6.3 Deferred interrupt handling | `FromISR` APIs, `portYIELD_FROM_ISR`, Zephyr work queues | Move UART parsing from the ISR to a task; measure ISR time |
| 6.4 Software timers and daemons | Timer service task priority, callback rules | Find the bug when a timer callback blocks |

**Check your understanding:** How deep must a queue be if a producer bursts 20 items every 100 ms and the consumer handles 1 item per 4 ms? Why is passing pointers through a queue dangerous, and how do you make it safe? Why must the timer service task have a carefully chosen priority?

### Chapter 7 · Memory in an RTOS (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Allocation strategies | Static allocation, FreeRTOS `heap_1` to `heap_5`, fragmentation, memory pools and slabs | Run a 24-hour allocation stress; report fragmentation per heap scheme |
| 7.2 Stack sizing | High-water marks, stack painting, call-graph analysis (`-fstack-usage`), interrupt stack | Size every task's stack with two methods; compare |
| 7.3 Overflow protection | MPU guard regions, FreeRTOS overflow hooks, Zephyr stack sentinels and hardware stack protection | Trigger an overflow and catch it with the MPU |
| 7.4 Isolation | FreeRTOS-MPU and Zephyr userspace: unprivileged threads, memory domains | Isolate a parser task so its bugs cannot corrupt the control task |

**Check your understanding:** Why do many safety standards discourage dynamic allocation after start-up? Why does stack painting under-estimate the true worst case? What does an MPU buy you that a software check cannot?

### Chapter 8 · Zephyr in depth (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 The build system | `west`, CMake, Kconfig, devicetree overlays, board definitions | Add a custom board overlay for your sensor wiring |
| 8.2 Kernel services | Threads, work queues, `k_msgq`, `k_poll`, timers, logging, shell | Rebuild your Chapter 6 pipeline in Zephyr |
| 8.3 Power management | System and device power management, tickless kernel | Measure idle current of the same app on FreeRTOS and Zephyr |
| 8.4 Testing in Zephyr | Ztest, Twister, `native_sim`, Renode and QEMU targets in CI | Run your tests on `native_sim` and an emulated board in CI |

**Check your understanding:** What problem does devicetree solve that `#define`s did not? Why run firmware tests on `native_sim` and also on an emulated MCU? What is the cost of Zephyr's portability?

### Chapter 9 · Timing analysis and tracing (week 10)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Measuring execution time | DWT cycle counter, GPIO markers, measuring under cache and flash-accelerator effects, input-dependent paths | Build a WCET measurement harness with worst-case inputs |
| 9.2 Static WCET awareness | Why measurement can miss the worst path; static analysers (for example AbsInt aiT, OTAWA) and when industry uses them | Find an input that beats your "measured worst case" |
| 9.3 Trace tools | Percepio Tracealyzer, SEGGER SystemView, Zephyr tracing (CTF); task, ISR and lock timelines | Trace a 10-second run; identify every deadline miss |
| 9.4 CPU load and slack | Idle-task accounting, run-time statistics, headroom targets | Report CPU load per task and remaining slack |

**Check your understanding:** Why is the maximum of 10,000 measurements not a WCET? What does a trace show that a profiler does not? How much headroom would you keep, and why?

### Chapter 10 · Multicore (week 11)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 SMP scheduling | FreeRTOS SMP, core affinity, global vs partitioned scheduling, spinlocks | Run your app on both cores of an RP2350 or ESP32; measure speed-up |
| 10.2 AMP | Separate kernels per core, OpenAMP and RPMsg, shared-memory mailboxes | Pass messages between cores with a lock-free mailbox |
| 10.3 Multicore pitfalls | Memory ordering, cache coherence (where present), priority inversion across cores | Find a race that appears only with two cores enabled |
| 10.4 Partitioning for determinism | Keeping hard real-time work on a dedicated core | Move the control loop to its own core; compare jitter |

**Check your understanding:** Why can SMP make worst-case timing harder to prove even when average throughput improves? When would you choose AMP over SMP? Why is "it worked on one core" not evidence of correctness?

### Chapter 11 · Watchdogs and fault tolerance (week 12)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Watchdog design | Independent vs window watchdog; why kicking from a timer ISR is useless | Show a hung task going unnoticed with a naive kick |
| 11.2 Task supervision | Each task checks in; a supervisor kicks only when all are alive and on time | Implement supervision; detect a stuck task within 500 ms |
| 11.3 Failure handling | Safe states, brown-out detection, error counters, graceful degradation | Define safe states for an e-bike controller and test each |
| 11.4 Post-mortem data | Core dumps (Zephyr, ESP-IDF), reset reasons, persistent crash logs | Capture and decode a core dump after a forced fault |

**Check your understanding:** Why does a watchdog kicked by the idle task catch some failures but not others? What is a safe state for a motor, a heater and a door lock? What information must survive a reset for field debugging?

### Chapter 12 · Designing and verifying RTOS applications (weeks 13–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 12.1 Architecture patterns | Active objects and event-driven design, priority assignment by rate and criticality, avoiding shared state | Redesign a 9-task app into 4 active objects |
| 12.2 Testing concurrency | Stress, randomised delays, fault injection, long soak tests | Run a 12-hour soak with injected delays; report misses |
| 12.3 Model checking awareness | Modelling a protocol in TLA+ or SPIN to find interleavings tests miss | Model a two-task handshake; find the bug the model reveals |
| 12.4 Certification context | What IEC 61508 and ISO 26262 ask of an RTOS; pre-certified kernels; the Zephyr safety effort | Write the evidence list you would need for a SIL 2 product |

**Check your understanding:** Why do active objects reduce the need for mutexes? What can a model checker find that a 12-hour soak test cannot? Why do certified products often pay for a pre-certified kernel?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Super-loop jitter | Timing requirements sheet |
| 2 | 2 | Lab 2 · A context switch from scratch | — |
| 3 | 3 | Lab 3 · Schedulability by hand and by trace | — |
| 4 | 3 | Lab 3 (cont.) | **P1 due** |
| 5 | 4 | Lab 4 · Sync primitives and their jitter | — |
| 6 | 5 | Lab 5 · Priority inversion | Pathfinder post-mortem |
| 7 | 6 | Lab 6 · Zero-copy pipeline | Mid-term (AI off) |
| 8 | 7 | Lab 7 · Stacks and the MPU | — |
| 9 | 8 | Lab 8 · Same app in Zephyr | — |
| 10 | 9 | Lab 9 · Trace a deadline miss | **P2 due** |
| 11 | 10 | Lab 10 · Two cores | — |
| 12 | 11 | Watchdog supervision (in P3) | — |
| 13 | 12 | Soak and fault-injection tests (in P3) | — |
| 14 | 12 | — | **P3 due** |
| 15 | Review | Oral defence of P3 | Final exam (AI off) |

## Working with AI in this course

- **Use AI for:** explaining kernel source you are reading (FreeRTOS `tasks.c`, Zephyr `sched.c`); generating Kconfig and devicetree boilerplate; writing trace post-processing scripts (parse a SystemView or CTF export into per-task statistics); drafting test harnesses for stress and fault injection; turning a trace into a written incident summary.
- **Do without AI (drills):** timeline simulations by hand; Liu–Layland and response-time calculations; queue sizing; identifying inversion and deadlock from a printed trace; drawing the context-switch stack frame. The mid-term and final are AI-off.
- **Verify AI output by:** asking which API is ISR-safe and checking the kernel documentation; running response-time analysis on the task set it proposes; tracing the result on hardware; running a soak test with injected delays; checking stack high-water marks after the soak.
- **Where AI still fails here (show it yourself):** in Lab 5 you give an assistant a three-task design with a shared resource and ask for working FreeRTOS code. Log what it does: typical defects include using a binary semaphore where a mutex (with inheritance) is needed, calling blocking APIs from ISRs instead of `FromISR` variants, kicking the watchdog from a timer, and claiming a design is schedulable without any WCET numbers. A trace either confirms or refutes each claim.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (10) | 25% |
| Projects P1–P3 | 35% |
| Mid-term (AI off) | 10% |
| Final exam (AI off) + P3 oral defence | 30% |

**Mastery gate.** You pass when you can, with AI tools off: (1) given a 5-task set with WCETs, periods and one shared resource, compute every response time including blocking and say whether it is schedulable, in 30 minutes; (2) find a planted priority inversion or deadlock from a recorded trace in 30 minutes and fix it; (3) show, with a trace and a soak-test report, that your P3 meets every deadline under worst-case load.

## Industry reality

Where this is used: engine and battery controllers, drones, medical pumps, industrial PLC modules, smart meters and many battery-powered IoT products run an RTOS or an RTOS-like scheduler. FreeRTOS remains MIT-licensed and gained SMP support in its main kernel with V11 (FreeRTOS release notes); Zephyr publishes two releases a year with long-term-support lines (Zephyr release page). PREEMPT_RT, the real-time patch set for Linux, was merged into mainline Linux 6.12 in 2024, so "Linux or RTOS" is now often "which parts on Linux, which on a microcontroller" (Kernel Newbies). Mars Pathfinder's priority inversion remains the standard case study and is still asked about in interviews.

**Interview questions from this course**

1. *Mutex or semaphore: what is the difference, and when do you use each?* Strong answer: mutex = ownership, only the owner releases, supports priority inheritance; semaphore = signalling or counting resources, can be given from an ISR; gives a concrete example of each and the bug from using a semaphore as a lock.
2. *Explain priority inversion and how to prevent it.* Strong answer: the three-task scenario, why the medium task makes blocking unbounded; inheritance vs ceiling; Pathfinder; how to detect it with a trace; designing to avoid shared locks in the first place.
3. *Are these three periodic tasks schedulable?* Strong answer: computes utilisation, applies the Liu–Layland bound, then exact response-time analysis when the bound is inconclusive; states assumptions (independent tasks, WCETs known, context-switch cost).
4. *What can and cannot be done inside an ISR in an RTOS?* Strong answer: no blocking calls, only `FromISR` APIs, keep it short, defer work to a task, request a context switch on exit, interrupt priorities relative to the kernel's maximum syscall priority.
5. *How do you choose a task's stack size, and how do you know it is enough?* Strong answer: static analysis of the call graph plus measurement under worst-case load (painting, high-water marks), interrupt stack separately, margin policy, MPU guard regions to catch overflow in testing and the field.

## Resources (free first)

- **Primary texts:** Richard Barry, *Mastering the FreeRTOS Real Time Kernel* (free) — https://github.com/FreeRTOS/FreeRTOS-Kernel-Book ; Zephyr Project documentation — https://docs.zephyrproject.org/ ; Nordic DevAcademy, nRF Connect SDK Fundamentals (free course built on Zephyr) — https://academy.nordicsemi.com/
- **Papers:** Liu and Layland, "Scheduling Algorithms for Multiprogramming in a Hard-Real-Time Environment", *JACM* (1973) — https://dl.acm.org/doi/10.1145/321738.321743 ; Sha, Rajkumar and Lehoczky, "Priority Inheritance Protocols", *IEEE Transactions on Computers* (1990) — https://doi.org/10.1109/12.57058
- **Case study:** Mike Jones's 1997 account of the Mars Pathfinder priority inversion, based on the flight software team's explanation — https://www.cs.cornell.edu/courses/cs614/1999sp/papers/pathfinder.html
- **Kernel sources:** FreeRTOS-Kernel — https://github.com/FreeRTOS/FreeRTOS-Kernel ; Zephyr — https://github.com/zephyrproject-rtos/zephyr
- **Tools:** SEGGER SystemView — https://www.segger.com/products/development-tools/systemview/ ; Percepio Tracealyzer (paid; academic licences exist) — https://percepio.com/tracealyzer/ ; TLA+ — https://lamport.azurewebsites.net/tla/tla.html ; Renode — https://antmicro.com/platforms/renode/
- **Paid, optional:** Giorgio Buttazzo, *Hard Real-Time Computing Systems*, 4th ed. (Springer), the standard scheduling-theory text.

## Sources

- FreeRTOS-Kernel releases (V11.3.1, 21 Aug 2026; V11.3.0, 30 Mar 2026) — https://github.com/FreeRTOS/FreeRTOS-Kernel/releases (checked 2026-10)
- Zephyr releases (4.4.0 on 14 Apr 2026; 3.7 LTS until 27 Jul 2029; 4.5 targeted for Oct 2026) — https://docs.zephyrproject.org/latest/releases/index.html (checked 2026-10)
- Mars Pathfinder account — https://www.cs.cornell.edu/courses/cs614/1999sp/papers/pathfinder.html (checked 2026-10)
- Kernel Newbies, Linux 6.12 (PREEMPT_RT merged) — https://kernelnewbies.org/Linux_6.12 (checked 2026-10)
- Liu and Layland (1973); Sha, Rajkumar and Lehoczky (1990) — links above

_Last reviewed: 2026-10_
