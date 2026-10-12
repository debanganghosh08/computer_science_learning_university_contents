# CS203 · Operating Systems

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 2 · 3 | 4 (≈ 120 hours) | L1 → L3 | [CS202](../CS202_computer_architecture_and_systems_programming/README.md) (taken in the same semester; this course's C-heavy labs are timed to follow CS202's chapters) | [CS212](../../semester_4/CS212_distributed_systems_i/README.md), [CS213](../../semester_4/CS213_security_foundations/README.md), [CS215](../../semester_4/CS215_cloud_and_devops_foundations/README.md), [OPS302](../../../03_majors/devops_sre_platform_engineering/year_3/OPS302_linux_systems_administration_in_depth/README.md), [NET301](../../../03_majors/it_infrastructure_networking/year_3/NET301_routing_and_switching/README.md) |

## Why this course matters now

Every container, cloud function, database and phone app is a set of processes the kernel schedules, isolates and feeds with memory and I/O. The kernel itself keeps moving: Linux replaced its CFS scheduler policy with EEVDF starting in 6.6 and, in 6.12 (Nov 2024), merged sched_ext, which lets operators load scheduling policies written as BPF programs at run time. AWS built the Firecracker microVM to run Lambda and Fargate workloads with VM-level isolation and container-like start-up (NSDI 2020), and Kubernetes resource limits are enforced through Linux cgroups. Even experts get OS semantics wrong: in 2018 PostgreSQL developers found that their assumptions about `fsync()` error reporting on Linux could silently lose data. AI assistants explain kernel code and write thread code fluently, but concurrency bugs pass a single test run and fail under load; the person who can reason about interleavings, page faults and durability, and then prove it with tools, is the one trusted with production.

## Learning outcomes

By the end you can:

1. **Implement** a Unix shell with pipelines, redirection and job control using `fork`, `exec`, `wait`, `pipe` and `dup2`.
2. **Compare** scheduling policies (RR, MLFQ, stride, CFS/EEVDF) by simulation and by measurement on Linux.
3. **Translate** virtual to physical addresses through multi-level page tables, and **implement** copy-on-write fork in xv6.
4. **Write** correct multithreaded C with locks, condition variables and semaphores, and **prove** the absence of data races with ThreadSanitizer and stress tests.
5. **Diagnose** deadlocks, atomicity violations and order violations, and **design** lock orderings that prevent them.
6. **Explain** how a file system lays out data and survives crashes (journaling, copy-on-write), and **write** durable, atomic file updates.
7. **Build** a container from namespaces, cgroups v2, overlayfs and seccomp, and **compare** its isolation with gVisor and microVMs.
8. **Diagnose** a slow or failing Linux machine with `/proc`, `perf` and eBPF tools using the USE method.

## Chapters and lessons

### Chapter 1 · The kernel and the process (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 What a kernel does | User and kernel mode, system calls, traps and interrupts; protection, abstraction, resource management | `strace ls`; group every system call by purpose |
| 1.2 The process API | `fork`, `exec`, `wait`, `exit`; zombies and orphans; why `fork` + `exec` is two calls | Mini-shell that runs commands and reaps children |
| 1.3 File descriptors | Per-process descriptor table, open-file table, `dup2`, pipes, "everything is a file" | Add `<`, `>`, `|` and `2>&1` to the shell |
| 1.4 Limited direct execution | Timer interrupts, kernel stacks, saving and restoring registers, context-switch cost | Measure system-call and context-switch time with a pipe ping-pong |

**Check your understanding:** Why does the shell, not the child, have to close the unused ends of a pipe, and what hangs if it does not? Why is `exec` not allowed to return on success? What stops a user program from simply disabling the timer interrupt?

### Chapter 2 · CPU scheduling (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Metrics and classic policies | Turnaround and response time; FIFO, SJF, STCF, round robin; the convoy effect | Scheduler simulator that reports both metrics per policy |
| 2.2 MLFQ and proportional share | MLFQ rules, gaming and priority boost; lottery and stride scheduling | Add MLFQ; demonstrate a gaming process, then fix the rule |
| 2.3 Linux scheduling | CFS virtual runtime, EEVDF (6.6+), `nice`, `SCHED_FIFO`/`RR`/`DEADLINE`, sched_ext BPF schedulers (6.12+) | Run CPU-bound jobs at different `nice` values; measure their shares |
| 2.4 Multicore and limits | Per-CPU run queues, load balancing, affinity (`taskset`), cgroup `cpu.max` throttling | Throttle a process with `cpu.max`; read `cpu.stat` to prove it |

**Check your understanding:** Why does round robin give good response time but poor turnaround for equal-length jobs? What problem does a priority boost solve in MLFQ? A container is "using 50% CPU" yet requests are slow: what cgroup counter would you check first?

### Chapter 3 · Virtual memory in the kernel (weeks 3–4)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Address spaces | Base and bounds, segmentation, paging, free-space management | Translate 10 addresses through a two-level page table by hand |
| 3.2 Page tables for real | RISC-V Sv39 in xv6, TLBs, address-space identifiers | xv6 lab: print a process's page table at `exec` |
| 3.3 Paging policy | Demand paging; FIFO, LRU, clock; Belady's anomaly; working sets and thrashing | Simulate replacement policies on recorded memory traces |
| 3.4 Linux memory in practice | Copy-on-write `fork`, `mmap`ed files, page cache, overcommit, the OOM killer, cgroup `memory.max` | Trigger and read an OOM kill inside a memory-limited cgroup |

**Check your understanding:** Why does a bigger page reduce TLB misses but waste memory? Why can adding RAM make thrashing vanish while a faster CPU does not help? Why can `malloc` succeed and the process still be killed later?

### Chapter 4 · Threads and locks (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Threads | `pthreads`; shared heap, private stacks; kernel vs user-level threads | Parallel array sum; measure speed-up from 1 to 16 threads |
| 4.2 Races | Data races, critical sections, atomicity; ThreadSanitizer | Break a shared counter, fix it, prove both with TSan |
| 4.3 Building locks | Test-and-set, compare-and-swap, ticket locks, spinning vs blocking, futexes | Spinlock and ticket lock with C11 atomics; benchmark under contention |
| 4.4 Concurrent data structures | Coarse vs fine-grained locking, hand-over-hand lists, approximate counters | Scalable counter vs one global lock at 1–16 threads |

**Check your understanding:** Why can adding threads make a program slower? When is spinning better than sleeping? Why is a ticket lock fair where a test-and-set lock is not?

### Chapter 5 · Synchronisation patterns (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Condition variables | Wait/signal, Mesa semantics, why the check is always a `while` loop | Bounded buffer with multiple producers and consumers |
| 5.2 Semaphores | Semaphores as locks and as ordering; readers–writers; dining philosophers | Three problems from *The Little Book of Semaphores* |
| 5.3 Event-driven concurrency | Event loops, `epoll`, non-blocking I/O, `io_uring` submission and completion rings | Echo server: thread-per-connection vs `epoll`, at 10,000 connections |
| 5.4 Memory ordering | Acquire/release, the ABA problem, read-copy-update (RCU) as an idea | Single-producer, single-consumer ring buffer with atomics; TSan clean |

**Check your understanding:** Why does replacing `while` with `if` around `pthread_cond_wait` create a bug that rarely shows? What does an event loop lose compared with threads? Why does lock-free not mean wait-free?

### Chapter 6 · Deadlock and concurrency bugs (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Deadlock | The four Coffman conditions; resource-allocation graphs; lock ordering; why the banker's algorithm is rare in practice | Lock wrapper that records lock order and reports cycles (a tiny "lockdep") |
| 6.2 Non-deadlock bugs | Atomicity and order violations, from a study of real bugs in MySQL, Apache, Mozilla and OpenOffice (Lu et al., 2008) | Classify 6 real bug reports and write the fix for each |
| 6.3 Finding them | TSan, Helgrind, stress loops with random delays, record-and-replay with `rr` | Reproduce a flaky test reliably, then fix it |
| 6.4 Priority inversion and livelock | Priority inheritance; back-off; starvation | Demonstrate priority inversion with real-time threads; fix with a priority-inheritance mutex |

**Check your understanding:** Which Coffman condition does a global lock order break? Why do concurrency bugs often vanish when you add a `printf`? A system never deadlocks but throughput drops to zero under load: what might be happening?

### Chapter 7 · Devices and file systems (weeks 8–9)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Devices | Polling vs interrupts, DMA, drivers; HDD seeks; SSD flash pages, erase blocks, FTL, wear levelling, TRIM; NVMe queues | `fio` random vs sequential reads; explain the gap |
| 7.2 The file API | Inodes, directories, hard and symbolic links, permissions; `open`, `read`, `write`, `fsync`, `rename` | Crash-safe config update: write temp, `fsync`, `rename`, `fsync` the directory |
| 7.3 File system layout | Bitmaps, inode tables, indirect blocks, extents, FFS cylinder groups | xv6 lab: large files (doubly indirect blocks) and symbolic links |
| 7.4 Crash consistency | `fsck`, journaling (ext4 `data=ordered`), copy-on-write (Btrfs, ZFS), log-structured file systems; the PostgreSQL `fsync` episode | Fault-injection harness that kills the writer at random points and checks invariants |
| 7.5 The page cache | Buffered vs direct I/O, read-ahead, `mmap` vs `read`, `io_uring` | Compare throughput of `read`, `mmap` and `io_uring` on a 4 GB file |

**Check your understanding:** Why is `rename` the standard way to replace a file atomically, and why is it not durable without an `fsync` on the directory? What does a journal write first, and why? Why does an SSD need garbage collection?

### Chapter 8 · Inside a kernel: xv6 (weeks 10–11)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Boot and structure | xv6-riscv boot, supervisor mode, kernel page table, the `proc` structure | Trace boot in gdb under QEMU |
| 8.2 Traps and system calls | Trap vector, `usertrap`, argument fetching, system-call dispatch | Add a `trace` system call |
| 8.3 Sleep, wake-up and kernel locks | Spinlocks with interrupts off, sleep locks, the lost wake-up problem | Find and fix a provided lost wake-up bug |
| 8.4 Copy-on-write fork | Reference-counted pages, page-fault handler, write faults | Implement COW `fork`; pass `usertests` |

**Check your understanding:** Why must a kernel spinlock disable interrupts on that CPU? What exactly goes wrong in a lost wake-up? Why does COW `fork` need a reference count per physical page?

### Chapter 9 · Virtualisation and containers (weeks 12–13)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Virtual machines | Trap-and-emulate, VT-x/AMD-V, nested paging (EPT/NPT), KVM with QEMU, virtio | Run the same syscall-heavy benchmark in a KVM guest and on the host |
| 9.2 Containers from primitives | Namespaces (pid, mount, net, user, uts, ipc, cgroup), cgroups v2 (`cpu.max`, `memory.max`, `pids.max`), overlayfs, `pivot_root` | Build a container by hand with `unshare` and cgroup files |
| 9.3 Isolation strength | Capabilities, user namespaces, seccomp-bpf; gVisor's user-space kernel; Firecracker microVMs; threat models | Write a seccomp allowlist; show a blocked system call |
| 9.4 Images and orchestration | OCI image and runtime specs, `runc`; how Kubernetes requests and limits become cgroup settings | Inspect the cgroup files of a running Docker or Podman container |

**Check your understanding:** Why is the shared kernel the main isolation weakness of containers compared with VMs? What does a user namespace let an unprivileged user do, and why is that both useful and risky? You must run untrusted code from strangers (an online judge, or code an AI agent wrote): which isolation layer would you choose, and what would you measure?

### Chapter 10 · The OS in production (week 14)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Observability | `/proc`, `/sys`, `vmstat`, `iostat`, `pidstat`; the USE method (utilisation, saturation, errors) | Diagnose 3 provided "slow machine" scenarios |
| 10.2 eBPF tracing | `bpftrace`, kprobes and tracepoints, the verifier | Latency histogram of `read()` per process |
| 10.3 How kernels evolve | Rust in Linux after the 2025 Maintainers Summit; sched_ext; reading LWN and the kernel mailing lists | Present one recent kernel change and its trade-offs in 5 minutes |
| 10.4 Postmortem practice | Turning an OS-level incident into a timeline, root cause and fix | Write a blameless postmortem for one of the 10.1 scenarios |

**Check your understanding:** High load average but idle CPUs: what are the candidates? Why is eBPF considered safe enough to run in production kernels? What would make you choose a BPF scheduler over tuning the default one?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · strace and syscall costs | — |
| 2 | 2 | Lab 2 · Scheduler simulator | — |
| 3 | 3 | Lab 3 · xv6 page tables | **P1 due** (shell) |
| 4 | 3 | Lab 4 · OOM and memory cgroups | — |
| 5 | 4 | Lab 5 · Locks and TSan | — |
| 6 | 5 | Lab 6 · Bounded buffer and epoll | — |
| 7 | 6 | Lab 7 · Deadlock and flaky tests | Mid-term (AI off) |
| 8 | 7 | Lab 8 · Durable writes | — |
| 9 | 7 | Lab 9 · xv6 file system | — |
| 10 | 8 | P2 (xv6 kernel work) | — |
| 11 | 8 | P2 (cont.) | **P2 due** |
| 12 | 9 | Lab 10 · Container by hand | — |
| 13 | 9 | P3 | — |
| 14 | 10 | Diagnosis drills | **P3 due** |
| 15 | Review | Oral defence of P3 | Final exam (AI off) |

## Working with AI in this course

- **Use AI for:** walking through unfamiliar xv6 or Linux code paths; summarising man pages and kernel documentation (then reading the cited section); interpreting `strace`, `perf` and `bpftrace` output; generating stress tests and fault-injection harnesses; drafting a seccomp allowlist that you then test.
- **Do without AI (drills):** scheduling traces and page-table translations by hand; writing a bounded buffer and a readers–writers lock from memory; spotting the deadlock in a code listing; explaining the `fork`/`pipe`/`dup2`/`exec` sequence for a pipeline on a whiteboard.
- **Verify AI output by:** running every threaded program under ThreadSanitizer and a stress loop of 1,000+ iterations with random delays; passing xv6 `usertests`; checking commands against the kernel documentation for *your* kernel version; testing durability claims with a crash-injection harness, not by reading the code.
- **Where AI still fails here:** you will see it yourself. Generated thread code that passes one run can fail under TSan or a stress loop, so every lab requires both. Interfaces drift between versions: cgroup v1 and v2 use different files (`memory.limit_in_bytes` vs `memory.max`), so an answer that mixes them fails on a modern distribution. Log each failure you find in a "verified or refuted" table that you submit with the labs.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (10) | 25% |
| Projects P1–P3 | 35% |
| Mid-term (AI off) | 10% |
| Final exam (AI off) + P3 oral defence | 30% |

**Mastery gate.** You pass when you can, without AI: (1) write a correct bounded buffer and explain why every line is needed; (2) add a working system call to xv6 in under two hours; (3) given a Linux machine with a planted problem (CPU throttling, memory pressure, I/O saturation or a lock convoy), find it with standard tools and explain the evidence within 45 minutes.

## Industry reality

Where this is used (public sources): Linux's scheduler moved to EEVDF from 6.6 and gained sched_ext in 6.12 (Linux kernel documentation and KernelNewbies); Firecracker microVMs were built to run AWS Lambda and Fargate (Agache et al., NSDI 2020); gVisor provides a user-space kernel for sandboxing containers (gVisor documentation); Kubernetes enforces CPU and memory limits through cgroups; the Linux kernel made Rust a permanent part of its development in December 2025 (LWN); PostgreSQL's 2018 `fsync` discovery changed how databases handle write-back errors (LWN). Platform, SRE, database, embedded and security teams all test this material in interviews.

**Interview questions from this course**

1. *What happens when you run `ls | wc -l` in a shell?* Strong answer: parse; `pipe()`; two `fork`s; `dup2` the pipe ends onto stdout/stdin; close unused ends (or `wc` never sees EOF); `exec`; parent `wait`s for both; mentions file-descriptor inheritance.
2. *Process or thread: which would you use for a worker pool, and why?* Strong answer: isolation and fault containment vs cheap sharing; creation and context-switch costs; memory overhead; language runtime constraints (e.g., Python's global interpreter lock); real examples of both designs.
3. *How is a mutex implemented?* Strong answer: atomic compare-and-swap fast path in user space; `futex` system call to sleep when contended; spinning briefly before sleeping; fairness and priority inversion.
4. *A container was OOM-killed although the host had free memory. Why?* Strong answer: the cgroup's `memory.max` (Kubernetes limit) was hit; page cache and kernel memory can count against it; check `memory.events` and the kernel log; fix the limit, the leak or the cache behaviour.
5. *How do you update a file so that a crash leaves either the old or the new version, never a mix?* Strong answer: write a temporary file, `fsync` it, `rename` over the original, `fsync` the directory; explains why each step exists and what happens if `fsync` reports an error.

## Resources (free first)

- **Primary text:** Remzi and Andrea Arpaci-Dusseau, *Operating Systems: Three Easy Pieces* (free) — https://pages.cs.wisc.edu/~remzi/OSTEP/
- **Labs and kernel:** MIT 6.1810 Operating System Engineering — https://pdos.csail.mit.edu/6.1810/ ; xv6-riscv source — https://github.com/mit-pdos/xv6-riscv
- **Courses:** UC Berkeley CS162 — https://cs162.org/ ; NPTEL Introduction to Operating Systems (Chester Rebeiro, IIT Madras; xv6-based) — https://nptel.ac.in/courses/106106144
- **Concurrency:** Allen B. Downey, *The Little Book of Semaphores* (free) — https://github.com/AllenDowney/LittleBookOfSemaphores
- **Linux documentation:** man pages — https://man.archlinux.org/ ; EEVDF scheduler — https://docs.kernel.org/scheduler/sched-eevdf.html ; sched_ext — https://docs.kernel.org/scheduler/sched-ext.html ; cgroup v2 — https://docs.kernel.org/admin-guide/cgroup-v2.html ; namespaces(7) — https://man.archlinux.org/man/namespaces.7.en ; seccomp(2) — https://man.archlinux.org/man/seccomp.2.en
- **Isolation:** Firecracker — https://firecracker-microvm.github.io/ ; gVisor — https://gvisor.dev/docs/ ; OCI runtime specification — https://github.com/opencontainers/runtime-spec
- **Production tooling:** Brendan Gregg, "Linux Performance Analysis in 60,000 Milliseconds" (Netflix TechBlog, 2015), a USE-method checklist — https://netflixtechblog.com/linux-performance-analysis-in-60-000-milliseconds-accc10403c55 ; bpftrace — https://github.com/bpftrace/bpftrace ; rr record-and-replay debugger — https://rr-project.org/ ; LWN.net — https://lwn.net/
- **Paid, optional:** Michael Kerrisk, *The Linux Programming Interface*; Silberschatz, Galvin and Gagne, *Operating System Concepts*.

## Sources

- KernelNewbies, Linux 6.6 (EEVDF) — https://kernelnewbies.org/Linux_6.6 and Linux 6.12 (sched_ext) — https://kernelnewbies.org/Linux_6.12 (checked 2026-10)
- Linux kernel documentation, "Extensible Scheduler Class" — https://docs.kernel.org/scheduler/sched-ext.html (checked 2026-10)
- Agache et al., "Firecracker: Lightweight Virtualization for Serverless Applications", NSDI 2020 — https://www.usenix.org/conference/nsdi20/presentation/agache (checked 2026-10)
- LWN.net, "PostgreSQL's fsync() surprise" (Apr 2018) — https://lwn.net/Articles/752063/ (checked 2026-10)
- LWN.net, "The (successful) end of the kernel Rust experiment" (Dec 2025) — https://lwn.net/Articles/1050174/ (checked 2026-10)
- Lu, Park, Seo and Zhou, "Learning from Mistakes: A Comprehensive Study on Real World Concurrency Bug Characteristics", ASPLOS 2008 — https://dl.acm.org/doi/10.1145/1346281.1346323 (checked 2026-10)
- Kubernetes documentation, "Resource Management for Pods and Containers" — https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/ (checked 2026-10)

_Last reviewed: 2026-10_
