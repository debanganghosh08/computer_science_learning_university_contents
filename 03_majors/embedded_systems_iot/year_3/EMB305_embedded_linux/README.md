# EMB305 · Embedded Linux

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 3 · 6 | 4 (≈ 120 hours) | L2 → L3 | [CS202](../../../../02_year_2_core_computer_science/semester_3/CS202_computer_architecture_and_systems_programming/README.md) (with [CS203](../../../../02_year_2_core_computer_science/semester_3/CS203_operating_systems/README.md) and [FND104](../../../../01_year_1_foundations/semester_1/FND104_the_developers_toolkit_linux_shell_git/README.md) assumed) | [EMB402](../../year_4/EMB402_embedded_and_iot_security/README.md), [EMB403](../../year_4/EMB403_robotics_software_with_ros_2/README.md), [EMB404](../../year_4/EMB404_hardware_software_co_design_and_fpga_basics/README.md), [OV09B](../../../../04_overlaps/OV09_edge_ai_secure_iot/OV09B_iot_fleet_security_and_over_the_air_updates/README.md) |

## Why this course matters now

Routers, set-top boxes, EV chargers, industrial gateways, drones, robots and in-vehicle infotainment run Linux on application processors, and the people who make Linux boot on a new board (board support package, or BSP, engineers) are some of the hardest embedded hires to find. The platform has matured: the PREEMPT_RT real-time patches were merged into mainline Linux 6.12 in November 2024 after 20 years of work; the Yocto Project's 6.0 "Wrynose" release (April 2026) is a long-term-support line maintained until April 2030; and regulation such as the EU Cyber Resilience Act makes software bills of materials and years of security updates part of the job. AI assistants are useful here and also dangerous, because embedded Linux changes under them: kernel driver APIs change between releases, Yocto changed its override syntax from `_append` to `:append` in 2021, and device-tree bindings are specific to each SoC. This course teaches you to build, boot, debug and maintain Linux on real boards, with the kernel source and the bindings as your ground truth.

## Learning outcomes

By the end you can:

1. **Explain** the full boot chain of an ARM board (ROM code, SPL, U-Boot, kernel, device tree, initramfs, init) and **debug** a board that stops at any stage.
2. **Cross-compile** user-space programs and the kernel, and **debug** them remotely with gdbserver.
3. **Configure and build** a kernel, write **device-tree** nodes and overlays for new peripherals, and **trace** a peripheral from its node to its driver.
4. **Write** a kernel driver (platform, I2C or IIO) with interrupts, sysfs attributes and correct locking, and **decide** when a user-space driver is better.
5. **Build** minimal images with Buildroot and production images with Yocto (layers, recipes, machine and distro configs, SDKs, licence manifests and SBOMs).
6. **Design** storage and update strategies (read-only root, overlays, A/B updates with RAUC, SWUpdate or Mender) that survive power loss.
7. **Measure and tune** real-time latency with PREEMPT_RT and cyclictest, and boot time with `systemd-analyze` and kernel tracing.
8. **Integrate** Linux with microcontroller cores (remoteproc/RPMsg or a serial link) in a heterogeneous design.
9. **Maintain** a product image: CVE tracking, licence compliance, kernel and Yocto LTS upgrades.

## Chapters and lessons

### Chapter 1 · Why Linux on a device (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 MPU vs MCU | MMU, external DRAM, storage, boot time, power; when Linux, when an RTOS, when both | Choose Linux or RTOS for 6 products with reasons |
| 1.2 The SoC landscape | Broadcom (Raspberry Pi), TI AM335x/AM62 (BeagleBone family), NXP i.MX, Rockchip, STM32MP; mainline support as a buying criterion | Rate 3 boards by mainline kernel and U-Boot support |
| 1.3 What a BSP contains | Bootloader, kernel, device tree, firmware blobs, root filesystem, update system | List the BSP components of a Raspberry Pi image |
| 1.4 Licences | GPLv2 obligations for the kernel and BusyBox, written source offers, permissive user space | Write the compliance checklist for a product shipping Linux |

**Check your understanding:** Why does "mainline support" matter more than the SoC's benchmark speed for a 10-year product? What must you ship with a product that contains a modified GPL kernel? When is Linux the wrong choice even if the hardware can run it?

### Chapter 2 · Cross-development (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Toolchains | Target triplets, sysroots, C libraries (glibc, musl, uClibc-ng), Bootlin prebuilt toolchains, crosstool-NG | Build "hello" for aarch64 with two C libraries; compare sizes |
| 2.2 Build systems for cross builds | CMake toolchain files, pkg-config sysroot handling, Meson cross files | Cross-build a small library and app that uses it |
| 2.3 Emulation | QEMU user mode and `qemu-system-aarch64 -M virt`; binfmt | Run your cross-built binary under QEMU; boot a kernel under QEMU |
| 2.4 Remote debugging | gdbserver, `gdb-multiarch`, core dumps on the target, `strace` and `perf` on ARM | Debug a crash on the board from your laptop |

**Check your understanding:** Why might a binary built against glibc fail on a musl root filesystem? What is a sysroot for? Why debug remotely rather than install GDB on the device?

### Chapter 3 · The boot process (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 ROM code and SPL | What the SoC's boot ROM reads, boot pins and boot media, secondary program loaders | Trace the boot media order of your board from its documentation |
| 3.2 U-Boot | Commands, environment, boot scripts, `bootm`/`booti`, FIT images, network boot (TFTP and NFS root) | Boot a kernel over TFTP with an NFS root filesystem |
| 3.3 Kernel start-up | Decompression, early console, command line, device-tree handoff, initramfs | Break the boot at 3 points and read the console to diagnose each |
| 3.4 User-space start | init (BusyBox init, systemd), mounting, services, getting a login shell | Create a minimal init script that starts one service |
| 3.5 Raspberry Pi specifics | Firmware-driven boot, `config.txt`, EEPROM bootloader on Pi 4/5 | Boot the Pi with U-Boot instead of the default path |

**Check your understanding:** A board prints U-Boot's banner and then nothing: what are the likely causes? Why use NFS root during development? What does the kernel need from the bootloader to start?

### Chapter 4 · The kernel (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Configuring | Kconfig, defconfigs, `menuconfig`, built-in vs module, size trade-offs | Cut a kernel's size by 30% without losing your board's peripherals |
| 4.2 Building and installing | Cross-compiling `Image` and modules, `modules_install`, versioning | Build and boot your own kernel on the board |
| 4.3 Kernel lines | Mainline, stable, LTS and vendor kernels; why vendor forks become a trap | Diff a vendor kernel against mainline; count the patches |
| 4.4 Rust in the kernel | Where Rust is used (drivers, abstractions), what it changes for driver authors | Build a kernel with Rust support and load the sample Rust module |

**Check your understanding:** What do you lose when you stay on a vendor kernel? Why make a driver a module during development? What does an LTS kernel promise, and what does it not?

### Chapter 5 · Device trees (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Syntax and structure | DTS, DTSI includes, nodes, properties, phandles, `compatible` strings | Read your board's DTS and draw its I2C and SPI buses |
| 5.2 Bindings | YAML binding schemas in `Documentation/devicetree/bindings`, `dtbs_check` | Validate a node against its binding; fix 3 planted errors |
| 5.3 Pin multiplexing and GPIOs | Pinctrl, GPIO specifiers, interrupts in device tree | Add a button with an interrupt in device tree |
| 5.4 Overlays | Runtime and boot-time overlays, Raspberry Pi `dtoverlay` | Write an overlay for a BME280 so the kernel's driver binds automatically |

**Check your understanding:** How does the kernel decide which driver handles a device-tree node? Why are bindings validated by schema? What happens when two nodes claim the same pin?

### Chapter 6 · Writing kernel drivers (weeks 6–7)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Modules | Module init and exit, parameters, licences, `insmod`/`modprobe`, `dmesg` | Write and load a module that logs a parameter |
| 6.2 The driver model | Buses, devices, drivers, probe and remove, devres (`devm_*`) resource management | Write a platform driver bound from device tree |
| 6.3 Character devices and sysfs | `file_operations`, `copy_to_user`, sysfs attributes, `ioctl` design | Expose a sensor reading through a char device and a sysfs attribute |
| 6.4 Interrupts and concurrency | Threaded IRQs, spinlocks vs mutexes, wait queues, work queues | Handle a GPIO interrupt with a threaded handler; stress it |
| 6.5 Subsystems | I2C client drivers, the IIO subsystem for sensors, regmap | Write an IIO driver for a simple I2C sensor |
| 6.6 User-space drivers | libgpiod (the GPIO character device that replaced sysfs GPIO), spidev, i2c-dev, UIO | Implement the same sensor read from user space; compare effort and latency |

**Check your understanding:** Why can you not sleep while holding a spinlock? When is a user-space driver the better engineering choice? What does `devm_` resource management prevent?

### Chapter 7 · Root filesystems and Buildroot (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Root filesystem anatomy | FHS layout, BusyBox, shared libraries, `/dev` with devtmpfs, `/proc` and `/sys` | Build a root filesystem by hand that boots to a shell |
| 7.2 Buildroot | `make menuconfig`, defconfigs, packages, overlays, post-build scripts | Build a 20 MB image that runs your sensor application at boot |
| 7.3 Adding packages | `.mk` and `Config.in` files, external trees (`BR2_EXTERNAL`) | Package your own application in a Buildroot external tree |
| 7.4 Init systems | BusyBox init vs systemd: boot time, features, footprint | Measure boot time with each |

**Check your understanding:** Why might a product choose BusyBox init over systemd, and vice versa? What makes a Buildroot build reproducible? Why keep your packages in an external tree?

### Chapter 8 · The Yocto Project (weeks 9–10)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Concepts | BitBake, layers, recipes, classes, tasks; Poky; LTS releases (5.0 Scarthgap, 6.0 Wrynose) | Build `core-image-minimal` for QEMU, then for your board |
| 8.2 Writing recipes | `SRC_URI`, `do_compile`, `do_install`, dependencies, `bbappend`, override syntax (`:append`) | Write recipes for your app and your kernel module |
| 8.3 Machines, distros and images | Machine configs, BSP layers (for example `meta-raspberrypi`), distro features, image recipes | Create your own layer, distro and image |
| 8.4 SDKs and developer flow | `populate_sdk`, eSDK, `devtool` | Develop your app against the generated SDK |
| 8.5 Compliance outputs | Licence manifests, SPDX software bills of materials, `cve-check` | Produce an SBOM and a CVE report for your image |
| 8.6 Build performance | Shared-state cache, download mirrors, build hosts | Measure clean vs cached build times |

**Check your understanding:** Why do companies choose Yocto despite its learning curve? What breaks if you edit a recipe in a third-party layer instead of using a `bbappend`? Why does an SBOM matter for a product sold in the EU from 2027?

### Chapter 9 · Storage and updates (week 11)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Flash storage | SD and eMMC (managed) vs raw NAND/NOR (UBI/UBIFS), wear, write amplification | Measure write volume of your image in a day of logging |
| 9.2 Read-only roots | Read-only root plus overlay or separate data partition, tmpfs for logs | Make the root read-only; keep config and logs working |
| 9.3 A/B updates | RAUC, SWUpdate, Mender; boot counting and fallback in U-Boot | Implement an A/B update that falls back after 3 failed boots |
| 9.4 Power-fail safety | Atomic switches, filesystem choices, journaling, testing with power cuts | Cut power 50 times during updates and writes; report results |

**Check your understanding:** Why do SD cards die in data loggers, and how do you prevent it? What makes an A/B switch atomic? How does the bootloader know a new image is bad?

### Chapter 10 · Real-time and performance (week 12)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 PREEMPT_RT | What it changes (threaded interrupts, sleeping spinlocks), enabling it in mainline | Build an RT kernel for your board |
| 10.2 Measuring latency | `cyclictest`, stress loads, histograms, worst cases | Compare worst-case latency of standard and RT kernels under load |
| 10.3 Tuning | CPU isolation, IRQ affinity, `SCHED_FIFO` priorities, memory locking | Get worst-case latency below a target you set from Chapter 10.2 data |
| 10.4 Boot time and power | `systemd-analyze`, kernel `initcall_debug`, trimming services; cpufreq governors and suspend | Halve your boot time with documented changes |

**Check your understanding:** Why does PREEMPT_RT reduce worst-case latency but not raise throughput? Why measure under load? Which boot-time savings are worth their maintenance cost?

### Chapter 11 · Heterogeneous systems (week 13)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Linux plus microcontrollers | Why products pair them (real-time I/O, low-power standby); serial, SPI or USB links | Connect a Pico 2 to a Raspberry Pi and stream sensor data |
| 11.2 remoteproc and RPMsg | Loading and talking to an MCU core from Linux on SoCs such as STM32MP or i.MX | Run the RPMsg echo sample in QEMU or on hardware if available |
| 11.3 Containers on devices | When containers help on gateways, and their cost in flash and RAM | Package an app as a container on the Pi; measure overhead |
| 11.4 Device observability | journald, remote logging, metrics, crash collection | Ship logs and crash reports from the device to a server |

**Check your understanding:** Why not do 10 kHz motor control in Linux user space? What does RPMsg give you over a raw shared-memory buffer? When are containers on a device a bad idea?

### Chapter 12 · Production embedded Linux (week 14)
| Lesson | What you learn | Practice |
|---|---|---|
| 12.1 Hardening preview | Secure boot chain, dm-verity, removing debug consoles, least privilege (detailed in EMB402) | List what you would remove from your dev image before shipping |
| 12.2 Maintenance | Kernel and Yocto LTS upgrades, backports, CVE triage, end-of-life planning | Upgrade your image across a Yocto release; log every break |
| 12.3 Compliance | GPL source offers, licence manifests, SBOM delivery, EU Cyber Resilience Act obligations | Assemble a compliance pack for your P3 image |
| 12.4 Documentation | Bring-up guides, BSP release notes, reproducible builds | Write a bring-up guide another student can follow |

**Check your understanding:** What does it cost to keep a device on an unsupported kernel for 5 years? Why is a reproducible build a security feature? What evidence would an auditor ask for?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Board survey and licences | — |
| 2 | 2 | Lab 2 · Cross toolchains and QEMU | — |
| 3 | 3 | Lab 3 · Break the boot | — |
| 4 | 4 | Lab 4 · A smaller kernel | **P1 due** |
| 5 | 5 | Lab 5 · Device-tree overlay | — |
| 6 | 6 | Lab 6 · Platform and char drivers | — |
| 7 | 6 | Lab 7 · IIO driver, and an AI audit | Mid-term (AI off) |
| 8 | 7 | Lab 8 · Buildroot image | — |
| 9 | 8 | Lab 9 · Yocto layer and image | — |
| 10 | 8 | Lab 9 (cont.) | **P2 due** |
| 11 | 9 | A/B updates (in P3) | — |
| 12 | 10 | Lab 10 · RT latency | — |
| 13 | 11 | Linux plus MCU (in P3) | — |
| 14 | 12 | — | **P3 due** |
| 15 | Review | Oral defence of P3 | Final exam (AI off) |

## Working with AI in this course

- **Use AI for:** explaining kernel source and boot logs; drafting recipes, Buildroot packages and systemd units; summarising a long binding document; writing test scripts (power-cut harnesses, latency plots); comparing two `defconfig` files.
- **Do without AI (drills):** drawing the boot chain and naming what fails at each stage from a console log; writing a device-tree node from a schematic; a minimal platform driver; reading `dmesg` after a failed probe. The mid-term and final are AI-off.
- **Verify AI output by:** checking the kernel version you build (`git log` on the relevant subsystem, `Documentation/`), validating device-tree nodes with `make dtbs_check` against the YAML bindings, building with `W=1`, running `checkpatch.pl`, testing on QEMU and then hardware, and checking Yocto syntax against the manual for your release.
- **Where AI still fails here (show it yourself):** in Lab 7 you ask an assistant for an I2C sensor driver and a device-tree overlay for your kernel version, then build them. Record every defect. Expect outdated APIs (for example the I2C `probe` callback signature changed in recent kernels), `compatible` strings and properties that no binding defines, the deprecated sysfs GPIO interface, pre-2021 Yocto override syntax (`_append`), and missing error handling on probe paths. The compiler, `dtbs_check` and the binding documents decide, not the explanation.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (10) | 25% |
| Projects P1–P3 | 35% |
| Mid-term (AI off) | 10% |
| Final exam (AI off) + P3 oral defence | 30% |

**Mastery gate.** You pass when you can, with AI off: (1) diagnose a board that fails to boot (three planted faults across U-Boot environment, device tree and root filesystem) from its serial console in 45 minutes; (2) add a new I2C sensor to a board end to end (device-tree node, driver binding, readings in user space) in 90 minutes; (3) show your P3 image updating A/B over the network, surviving 50 power cuts, with an SBOM and CVE report.

## Industry reality

Where this is used: gateways, EV chargers, industrial HMIs, robots and drones, cameras, routers and vehicle infotainment. The ecosystem's long-term-support lines shape product plans: Yocto 5.0 Scarthgap is supported until April 2028 and 6.0 Wrynose until April 2030 (Yocto Project wiki). Real-time Linux no longer needs an out-of-tree patch set since 6.12 (Kernel Newbies). Bootlin, a French embedded-Linux firm, publishes its full training slides and labs free, which makes professional-grade self-study possible.

**Interview questions from this course**

1. *Walk me through what happens from power-on to a login prompt on an ARM board.* Strong answer: boot ROM and boot pins, SPL initialising DRAM, U-Boot loading kernel, device tree and initramfs, kernel init and driver probing, mounting root, init/systemd, services; where each fails and how you see it.
2. *What is a device tree, and why does Linux on ARM use it?* Strong answer: hardware description separate from the kernel image; compatible strings bind drivers; one kernel for many boards; bindings and validation; overlays for add-on boards.
3. *Kernel driver or user-space driver for a new SPI sensor?* Strong answer: user space (spidev) for speed of development and isolation when latency and sharing needs are modest; kernel (IIO) when multiple consumers, interrupts, standard interfaces or power management matter; mentions maintenance and upstreaming.
4. *How would you design firmware updates for a Linux gateway in the field?* Strong answer: A/B partitions with a tool such as RAUC, SWUpdate or Mender, signed images, boot counting and automatic fallback, data partition kept separate, staged rollout, power-cut testing.
5. *Yocto or Buildroot?* Strong answer: Buildroot for small, single-purpose images and quick builds; Yocto for product lines, many layers and vendors, SDKs, licence and SBOM outputs, LTS releases; the learning-curve and build-infrastructure costs.

## Resources (free first)

- **Primary course:** Bootlin training materials (slides and labs for embedded Linux, kernel drivers, Yocto and Buildroot; freely downloadable, per Bootlin's course pages) — https://bootlin.com/training/
- **Documentation:** Linux kernel documentation — https://docs.kernel.org/ ; Yocto Project documentation — https://docs.yoctoproject.org/ ; Yocto releases — https://wiki.yoctoproject.org/wiki/Releases ; Buildroot manual — https://buildroot.org/downloads/manual/manual.html ; U-Boot documentation — https://docs.u-boot.org/ ; Devicetree specification — https://www.devicetree.org/specifications/ ; Raspberry Pi documentation — https://www.raspberrypi.com/documentation/ ; BeagleBoard documentation — https://docs.beagleboard.org/
- **Kernel learning:** Linux Kernel Labs — https://linux-kernel-labs.github.io/ ; *Linux Device Drivers*, 3rd ed. (free, but written for kernel 2.6; use for concepts, not APIs) — https://lwn.net/Kernel/LDD3/ ; LWN.net — https://lwn.net/ ; Kernel Newbies — https://kernelnewbies.org/
- **Update systems:** RAUC — https://rauc.io/ ; SWUpdate — https://sbabic.github.io/swupdate/ ; Mender — https://docs.mender.io/
- **Tools:** QEMU — https://www.qemu.org/docs/master/ ; rt-tests (cyclictest) — https://git.kernel.org/pub/scm/utils/rt-tests/rt-tests.git/
- **Paid, optional:** Frank Vasquez and Chris Simmonds, *Mastering Embedded Linux Programming*, 3rd ed. (Packt, 2021); John Madieu, *Linux Device Driver Development*, 2nd ed. (Packt, 2022).

## Sources

- Kernel Newbies, Linux 6.12 ("the real-time patchset has been merged in mainline"; released 17 Nov 2024) — https://kernelnewbies.org/Linux_6.12 (checked 2026-10)
- Yocto Project wiki, Releases (6.0 Wrynose LTS to Apr 2030; 5.0 Scarthgap LTS to Apr 2028; 6.1 Blacksail Oct 2026) — https://wiki.yoctoproject.org/wiki/Releases (checked 2026-10)
- European Commission, Cyber Resilience Act — https://digital-strategy.ec.europa.eu/en/policies/cyber-resilience-act (checked 2026-10)
- Bootlin training materials — https://bootlin.com/training/ (checked 2026-10)

_Last reviewed: 2026-10_
