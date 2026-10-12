# EMB305 · Labs and projects

Hardware: a Raspberry Pi 4 or 5 (or a BeaglePlay/BeagleBone-class board), a 3.3 V USB–serial adapter for the console, a microSD card, an Ethernet cable, a BME280 or similar I2C sensor, and a Pico 2 for the co-processor work. Every lab runs first on QEMU (`qemu-system-aarch64 -M virt`) where possible. Builds need a Linux machine or VM with at least 100 GB free disk for Yocto; a shared lab build server with a shared-state cache is recommended.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Board survey and licences | Compare 3 boards on mainline kernel and U-Boot support; write a GPL compliance checklist | Comparison table with links to upstream support; checklist | 3 h |
| 2 · Cross toolchains and QEMU | Build "hello" and a small library-using app with glibc and musl toolchains; run under QEMU user and system mode; debug with gdbserver | Build scripts, size comparison, a remote-debug session log | 4 h |
| 3 · Break the boot | Starting from a working board, break the boot at the U-Boot, kernel and init stages (three faults each set by a partner) and fix them from the console | Console logs annotated with the diagnosis for each fault | 4 h |
| 4 · A smaller kernel | Reduce kernel size by at least 30% while keeping all peripherals your board uses | Before/after sizes, the config diff, a boot log proving peripherals still probe | 4 h |
| 5 · Device-tree overlay | Write an overlay that binds the kernel's existing BME280 driver; validate with `dtbs_check` | Overlay source, validation output, `iio` readings in user space | 3 h |
| 6 · Platform and char drivers | Write a platform driver from device tree that exposes a GPIO-backed device through a char device and sysfs, with a threaded IRQ | Driver source passing `checkpatch.pl`; a stress test of the IRQ path | 6 h |
| 7 · IIO driver, and an AI audit | Write an IIO driver for a simple I2C sensor; ask an assistant for the same driver for your kernel version and audit it | Your driver; the audit table (outdated API, invented properties, missing error paths) with evidence | 5 h |
| 8 · Buildroot image | A Buildroot external tree with your app, overlay and kernel config; image under 64 MB | `BR2_EXTERNAL` tree, image size, boot time | 4 h |
| 9 · Yocto layer and image | Your own layer, distro and image for QEMU and your board, with an SDK, SBOM and CVE report | Layer repository, build logs, SPDX SBOM, CVE summary | 8 h |
| 10 · RT latency | Compare standard and PREEMPT_RT kernels with `cyclictest` under stress; tune isolation and IRQ affinity | Latency histograms for each configuration; tuning notes | 4 h |

## Projects

### P1 · A network-booted development set-up (L1, ~6 hours)

**Real-world inspiration.** BSP teams rarely flash an SD card for every change; they boot kernels over TFTP with an NFS root so an edit-compile-test loop takes seconds, not minutes.

**What to build.** A development set-up in which your board's U-Boot loads the kernel and device tree over TFTP and mounts a hand-built BusyBox root filesystem over NFS from your laptop or a lab server. Reproduce it in QEMU so it can be tested without hardware.

**Acceptance criteria**
- Board boots to a shell over the network with the serial console showing each stage.
- Changing and reloading a kernel module takes under 2 minutes from edit to running code, timed.
- The root filesystem is built by your script (BusyBox, libraries, device nodes via devtmpfs) and is under 10 MB.
- The same kernel and root filesystem boot in QEMU from a single documented command.
- A README another student can follow from a blank SD card.

**Stretch goals.** Boot over USB gadget Ethernet; add a script that bisects kernel builds automatically.

**What it proves to an employer.** You can set up the bring-up workflow BSP engineers use daily, and you understand every stage of the boot.

### P2 · A sensor appliance image (L2, ~15 hours)

**Real-world inspiration.** Low-cost air-quality and environmental monitors built on small Linux boards are common in Indian cities, schools and offices (illustrative scenario); they need a small, fast-booting image and a reliable sensor path.

**What to build.** A Buildroot image for your board containing a trimmed kernel, a device-tree overlay for two sensors, your own IIO driver for one of them (from Lab 7), and a small application that reads both sensors, serves the readings on a local web page and logs to a data partition.

**Acceptance criteria**
- Image under 64 MB; boot from power-on to the application serving its first reading in under 10 seconds, measured from the serial log.
- Driver passes `checkpatch.pl` with zero errors; the overlay passes `dtbs_check`.
- Loading and unloading the module 100 times shows no leaks (`kmemleak` report) and no errors in `dmesg`.
- A 24-hour run shows no more than 5% growth in the application's memory use and no lost readings.
- Readings agree with a reference instrument within the sensor's datasheet accuracy.
- The root filesystem is read-only; logs and data go to a separate partition.

**Stretch goals.** Rebuild the same appliance with Yocto and compare image size, build time and maintainability; submit your driver for review on a public mailing list after a mentor's check.

**What it proves to an employer.** You can deliver a small, fast, maintainable Linux product image with your own kernel code in it.

### P3 · A production-grade Yocto gateway with A/B updates and a real-time co-processor (L3, portfolio-grade, ~30 hours)

**Real-world inspiration.** EV chargers, smart-meter data concentrators and industrial gateways pair a Linux processor (networking, UI, updates) with a microcontroller that handles real-time I/O, and they must update safely in the field for a decade (illustrative of a common architecture).

**What to build.** A Yocto layer, distro and image for your board with: a read-only root and a data partition; A/B updates with RAUC or SWUpdate using signed bundles and boot counting in U-Boot; a PREEMPT_RT kernel; a Pico 2 co-processor connected over UART or USB that samples sensors and drives an output on a fixed schedule, with a Linux service that talks to it; a systemd watchdog; remote logging; and a compliance pack (licence manifest, SPDX SBOM, CVE report).

**Acceptance criteria**
- **Reproducible build:** a clean build on a fresh machine from the README succeeds; two builds produce the same package versions (manifest diff attached).
- **Updates:** 50 power cuts at random points during updates all leave a bootable system; a deliberately broken image is rejected or rolled back automatically after at most 3 failed boots; unsigned bundles are refused.
- **Real time:** a 1-hour `cyclictest` under `stress-ng` load reports a worst-case latency at least 5× lower with your RT configuration than with the standard kernel on the same board; both histograms included.
- **Co-processor:** the Pico 2's sampling schedule shows no missed cycles over 1 hour regardless of Linux load (sequence numbers), and the Linux service recovers automatically if the link is unplugged and replugged.
- **Boot and health:** boot to the gateway service in under 15 seconds; the systemd watchdog restarts a hung service within 30 seconds.
- **Compliance:** the SBOM is in SPDX format; the CVE report's 5 highest-severity entries are triaged (affected or not, and why); a GPL source-offer text is included.

**Stretch goals.** dm-verity on the root filesystem and a signed FIT image (preview of EMB402); remoteproc/RPMsg on an SoC with an on-chip MCU core; an upgrade of the whole image across a Yocto release with a written log of every break.

**What it proves to an employer.** You can build and maintain the kind of Linux platform products ship on, with safe updates, measured real-time behaviour and compliance evidence. BSP, gateway, automotive and robotics teams hire for this.

## Feeds into

- [EMB402 Embedded and IoT Security](../../year_4/EMB402_embedded_and_iot_security/README.md): secure boot, dm-verity and signed updates harden the P3 gateway.
- [EMB403 Robotics Software with ROS 2](../../year_4/EMB403_robotics_software_with_ros_2/README.md): ROS 2 runs on the Linux image you can now build and tune.
- [EMB404 Hardware-Software Co-Design and FPGA Basics](../../year_4/EMB404_hardware_software_co_design_and_fpga_basics/README.md): Linux drivers for FPGA-based accelerators.
- [OV09B IoT Fleet Security and Over-the-Air Updates](../../../../04_overlaps/OV09_edge_ai_secure_iot/OV09B_iot_fleet_security_and_over_the_air_updates/README.md): A/B updates at fleet scale.
- The [EMB flagship industry project](../../../../06_career_and_market_readiness/05_industry_projects/EMB_embedded_systems_iot.md): the gateway tier of the fleet.
