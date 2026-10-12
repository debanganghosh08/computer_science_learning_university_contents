# CS203 · Labs and projects

Work on Linux (a VM or WSL2 is fine; cgroup and namespace labs need a kernel with cgroup v2, which current Ubuntu, Debian and Fedora releases use by default). xv6 labs run in QEMU and follow the public structure of MIT 6.1810. Every concurrent program must pass ThreadSanitizer and a stress loop.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · strace and system-call costs | Trace `ls`, `curl` and `python3 -c pass`; measure the cost of a null system call and a context switch with a pipe ping-pong | Categorised syscall tables; cost measurements with spread over 20 runs | 3 h |
| 2 · Scheduler simulator | Implement FIFO, SJF, STCF, RR, MLFQ and stride scheduling over job traces; compute turnaround and response time | Simulator, plots per policy, and a paragraph on which policy suits an interactive laptop vs a batch cluster | 5 h |
| 3 · xv6 page tables | Print a process's page table; map a read-only shared page to speed up a system call; detect accessed pages | Kernel patch passing the lab tests; one page-table diagram drawn by hand | 6 h |
| 4 · Memory cgroups and the OOM killer | Run a leaking program inside a cgroup with `memory.max`; read `memory.events` and the kernel log; compare with an unlimited run | Evidence chain from limit to kill, and the fix | 3 h |
| 5 · Locks and TSan | Implement spinlock, ticket lock and a futex-based mutex; benchmark at 1–16 threads; fix a racy hash map | Benchmarks, TSan reports before and after | 4 h |
| 6 · Bounded buffer and `epoll` | Multi-producer, multi-consumer bounded buffer; an `epoll` echo server load-tested at 10,000 connections | Code, latency percentiles, comparison with thread-per-connection | 5 h |
| 7 · Deadlock detection and flaky tests | Build a lock wrapper that reports lock-order cycles; reproduce and fix a provided flaky test using stress and `rr` | Detector, cycle report, root-cause write-up | 4 h |
| 8 · Durable writes | Write a key-value file update that survives crashes; kill the writer at random points 1,000 times and check that the file is always old-or-new | Harness, results, explanation of every `fsync` | 4 h |
| 9 · xv6 file system | Add doubly indirect blocks (large files) and symbolic links to xv6 | Patch passing the lab tests; diagram of the new inode layout | 6 h |
| 10 · Container by hand | Use `unshare`, cgroup v2 files, overlayfs and `pivot_root` to build a container; add a seccomp allowlist | Script, proof of each isolation property (separate PID 1, no network, limits enforced), list of syscalls allowed | 5 h |

## Projects

### P1 · A Unix shell with job control (L1, ~6 hours)

**Real-world inspiration.** bash, zsh and BusyBox `ash` (the shell in many container images and embedded systems) are built from the same handful of system calls you learn in Chapter 1.

**What to build.** A shell that supports commands with arguments, pipelines, `<`, `>`, `>>`, `2>&1`, background jobs with `&`, and the built-ins `cd`, `exit`, `jobs`, `fg` and `bg`, with correct process groups and terminal control so Ctrl-C and Ctrl-Z reach only the foreground job.

**Acceptance criteria**
- Output matches bash on the 50 provided test cases, including a pipeline of 5 commands.
- After 1,000 commands (mixed foreground and background), there are no zombie processes and no leaked file descriptors (checked through `/proc/<pid>/fd`).
- Ctrl-C during `sleep 100 | cat` stops the pipeline and leaves the shell running; `jobs` shows correct states.
- Every system call's return value is checked; error messages match the provided format.

**Stretch goals.** Command substitution `$(...)`; history; a `time` built-in that reports user and system time with `getrusage`.

**What it proves to an employer.** You understand processes, file descriptors and signals from the system-call level up, which is what debugging production Linux requires.

### P2 · Kernel extensions for xv6 (L2, ~15 hours)

**Real-world inspiration.** Linux uses copy-on-write `fork` and demand paging to make process creation cheap; schedulers trade fairness against latency.

**What to build.** Three xv6 changes: (1) a `trace` system call; (2) copy-on-write `fork` with per-page reference counts and a write-fault handler; (3) lazy heap allocation, where `sbrk` reserves address space and pages are allocated on first touch. Then add a lottery scheduler behind a compile-time flag.

**Acceptance criteria**
- All xv6 `usertests` and the provided `cowtest` and `lazytests` pass.
- Forking a process with a 64 MB heap consumes fewer than 100 new physical pages until the child writes (show free-page counts before and after).
- With tickets in a 3:2:1 ratio, the measured CPU shares over 10,000 ticks are within ±5% of 50%/33%/17%.
- The README walks through one COW fault with a gdb trace and explains how freeing a shared page is kept correct.

**Stretch goals.** Memory-mapped files (`mmap`/`munmap`) in xv6; a per-process CPU-time accounting system call.

**What it proves to an employer.** You can work inside a kernel: read unfamiliar low-level code, change page-table logic safely, and prove it with tests.

### P3 · A sandbox for running untrusted code (L3, portfolio-grade, ~30 hours)

**Real-world inspiration.** Online judges (Codeforces, CodeChef, LeetCode) run millions of untrusted submissions under strict time and memory limits; cloud platforms isolate tenants with gVisor and Firecracker microVMs; and AI coding agents such as Claude Code and OpenAI Codex run the commands and tests they write, which raises the same isolation question. This project builds the container-level layer and documents its limits honestly.

**What to build.** A sandbox runner in C, Go or Rust. Given a program, input and limits, it runs the program in new PID, mount, network, IPC, UTS and user namespaces; applies cgroup v2 limits (`cpu.max`, `memory.max`, `pids.max`); provides a read-only root through overlayfs with a small writable `tmpfs`; applies a seccomp allowlist; enforces a wall-clock timeout and an output cap; and returns a JSON verdict (`OK`, `TIME_LIMIT`, `MEMORY_LIMIT`, `RUNTIME_ERROR`, `OUTPUT_LIMIT`, `BLOCKED_SYSCALL`). A small queue service runs N jobs concurrently.

**Acceptance criteria**
- The provided misbehaviour suite (fork bomb, memory hog, infinite loop, network connection attempt, write outside the scratch area, attempt to read a planted host file, 1 GB of output) produces the correct verdict for every case, and the host stays healthy (load, free memory and process count return to baseline).
- Memory limits are enforced within 5% of the configured value; reported CPU time matches the cgroup's `cpu.stat` within 10 ms.
- Sandbox start-up overhead is under 50 ms at p95 on a stated machine, measured over 1,000 runs.
- After 100 concurrent jobs, no cgroups, mounts or processes are left behind (checked by a script).
- A threat-model document states what the sandbox does not defend against (for example, kernel vulnerabilities reachable through allowed system calls) and when to add gVisor or a microVM instead.

**Stretch goals.** Run the same suite under gVisor (`runsc`) and compare start-up overhead and syscall-heavy performance; per-language profiles (C, Python, Java) with minimal allowlists; Prometheus metrics for queue depth and verdicts.

**What it proves to an employer.** You can turn OS primitives into a working isolation layer, test it adversarially, measure its cost, and write down its limits. Platform, security and AI-infrastructure teams need exactly this.

## Feeds into

- [CS212 Distributed Systems I](../../semester_4/CS212_distributed_systems_i/README.md): processes, threads, failures and timeouts become nodes, RPCs and partial failure.
- [CS213 Security Foundations](../../semester_4/CS213_security_foundations/README.md): privilege separation, sandboxing and isolation boundaries.
- [CS215 Cloud and DevOps Foundations](../../semester_4/CS215_cloud_and_devops_foundations/README.md): containers, images and resource limits in practice.
- [OPS302 Linux Systems Administration in Depth](../../../03_majors/devops_sre_platform_engineering/year_3/OPS302_linux_systems_administration_in_depth/README.md) and [OPS303 Observability](../../../03_majors/devops_sre_platform_engineering/year_3/OPS303_observability_metrics_logs_traces/README.md): Chapter 10 grows into full production practice.
- [OV12A Running Agents in Production](../../../04_overlaps/OV12_agent_infrastructure_platform/OV12A_running_agents_in_production_sandboxes_durable/README.md): P3 is the foundation for sandboxing agent-executed code.
