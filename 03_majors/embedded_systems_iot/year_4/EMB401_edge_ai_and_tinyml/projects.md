# EMB401 · Labs and projects

Hardware: a Cortex-M4F or M7 board with an IMU and a microphone (or add-on breakouts), an ESP32-S3 board with a camera, your EMB301 current-measurement set-up (a power profiler if available), and a small DC fan or motor with an accelerometer for P3. NPU work can use an Arm Corstone/Ethos-U simulator (Fixed Virtual Platform) if no NPU board is available. Every dataset you record from people requires their written consent and a dataset card (who, what, where, licence, how to request deletion).

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Edge or cloud? Energy arithmetic | Compare the energy of streaming raw audio over BLE with local classification, using your measured EMB304 numbers | Calculation with every input sourced or measured; recommendation | 2 h |
| 2 · Collect your own dataset | Log and label 30+ minutes of IMU or audio data from at least 5 people; compare random vs by-person splits | Dataset and dataset card; the accuracy gap between splits | 5 h |
| 3 · Bit-exact features | Implement log-mel features on the device with CMSIS-DSP; match the training pipeline | Comparison of 500 frames (max absolute error); cycle counts per frame | 4 h |
| 4 · Architectures under a budget | Train 3 architectures for one task under 32 KB flash and 16 KB RAM | MACs, parameters, peak activation memory (by hand and by tool), accuracy | 4 h |
| 5 · Quantisation by slice | Convert to int8 with PTQ, then QAT; evaluate overall and per slice | Accuracy table by slice before and after; release decision | 4 h |
| 6 · Three runtimes, one model, and an AI audit | Deploy the same model with LiteRT Micro, ExecuTorch and a vendor or hosted tool; audit an AI-generated deployment | Flash, RAM, latency per runtime; audit table (wrong API version, wrong arena, feature mismatch) | 6 h |
| 7 · Arena diet | Reduce peak RAM by 30% without losing more than 1 point of accuracy | Before/after memory maps; the change that worked and why | 4 h |
| 8 · Wake word, false accepts per hour | Run continuous keyword spotting; measure false accepts on 1 hour of background audio and false rejects on new speakers | Error rates, ROC curve, chosen threshold with reasons | 5 h |
| 9 · Anomaly thresholds | Train an autoencoder on normal fan vibration; set a threshold for under 1 false alarm per day | Threshold method, validation with synthetic faults, AUC and operating point | 4 h |
| 10 · NPU vs CPU | Compile a vision model for an Ethos-U (board or simulator) or STM32N6-class NPU; compare with CPU-only | Latency, energy (or cycle estimates), operator fallback list | 4 h |

## Projects

### P1 · A gesture classifier on a microcontroller (L1, ~6 hours)

**Real-world inspiration.** Wearables and handheld controllers recognise flicks, taps and wrist rotations on-device to save energy and respond instantly (illustrative scenario).

**What to build.** Firmware that recognises 4 gestures plus an "unknown" class from a 6-axis IMU in real time, with your own collected data (at least 5 people) and a model you trained.

**Acceptance criteria**
- Accuracy reported on at least 3 people who are not in the training data; target at least 85% on the 4 gestures.
- False triggers counted over 10 minutes of everyday motion (walking, typing) and reported per minute.
- Model under 32 KB of flash with a tensor arena under 16 KB, both measured.
- Latency from window end to decision under 20 ms on a Cortex-M4F, measured with GPIO markers.
- Device and host predictions agree on 200 recorded test windows.

**Stretch goals.** Replace the CNN with a tree ensemble and compare; add streaming windows with 50% overlap.

**What it proves to an employer.** You can take a sensor ML task from data collection to a measured on-device model without leaking test data.

### P2 · A keyword spotter for an Indian language (L2, ~15 hours)

**Real-world inspiration.** Voice commands help users whose hands are busy or who prefer speaking to reading, for example on kiosks, appliances or farm equipment; widely used keyword datasets such as Speech Commands are English, so local-language keywords need local data (illustrative scenario).

**What to build.** A streaming keyword spotter for 3–5 keywords in an Indian language of your choice, trained on recordings from at least 10 consenting speakers plus Speech Commands-style background noise, deployed as int8 on a microcontroller with a PDM or I2S microphone.

**Acceptance criteria**
- False accepts of at most 1 per hour on 3 hours of mixed background audio (for example TV, street, kitchen) played at a realistic level.
- False rejects of at most 10% per keyword on at least 3 held-out speakers at 1 m, with per-speaker results shown.
- Detection latency (end of spoken keyword to output event) under 200 ms, measured.
- Tensor arena under 64 KB; flash use and energy per inference measured and reported.
- A dataset card with consent records (stored privately), speaker diversity and licence.

**Stretch goals.** Add a second language and measure cross-language false accepts; run on an NPU target and compare energy.

**What it proves to an employer.** You can build a production-shaped audio ML feature with honest error metrics, which is the core of wake-word and voice-interface work.

### P3 · A predictive-maintenance node with fleet monitoring (L3, portfolio-grade, ~30 hours)

**Real-world inspiration.** Pumps, fans and motors in factories and water systems usually fail with warning signs in vibration and current long before they stop; small manufacturers rarely have monitoring because wired systems are costly (illustrative scenario). Public datasets such as MIMII and ToyADMOS exist because this problem is common.

**What to build.** A battery-powered node mounted on a small fan or DC motor that samples vibration (and optionally motor current), computes features with CMSIS-DSP, runs an int8 anomaly model with hysteresis, and reports anomaly scores and feature summaries over MQTT (from EMB304). Add over-the-air model updates independent of firmware, a fleet dashboard with per-device score histograms, and a drift alarm. Guard all rotating parts.

**Acceptance criteria**
- **Detection:** 3 induced fault types (imbalance from an added mass, blocked airflow or load change, loose mounting) are each detected in at least 9 of 10 trials within 60 seconds.
- **False alarms:** at most 1 false alarm in 24 hours of normal operation, with the log attached.
- **Energy:** a measured trace supports at least 1 year of operation on your stated battery at one inference per minute plus hourly reports.
- **Correctness:** device and host outputs agree within a stated tolerance on 500 recorded test vectors, checked in CI.
- **Model updates:** a new model version is delivered over the air, checked for version and input-shape compatibility, and rolled back automatically if its self-test fails.
- **Drift:** a deliberate operating change (new speed or mounting) triggers a drift alarm; your documented re-baselining procedure restores normal false-alarm rates.
- **Report:** a reproducible benchmark report (clock, compiler, memory placement, latency, energy per inference, accuracy and operating point).

**Stretch goals.** Run the model on an NPU-equipped MCU and compare energy; add a small on-device continual baseline update with safeguards against learning a fault as normal; port the pipeline to ExecuTorch.

**What it proves to an employer.** You can deliver edge AI that survives contact with the field: measured detection and false-alarm rates, a real energy budget and a way to update and monitor models on a fleet.

## Feeds into

- [OV09A Deploying Models on Edge Devices](../../../../04_overlaps/OV09_edge_ai_secure_iot/OV09A_deploying_models_on_edge_devices/README.md): P3 is the starting point for multi-target deployment.
- [EMB402 Embedded and IoT Security](../../year_4/EMB402_embedded_and_iot_security/README.md): signing and protecting models and their updates.
- [EMB501 Frontier Seminar: Autonomous Systems and Physical AI](../../year_5/EMB501_frontier_seminar_autonomous_systems_and_physical/README.md): perception on constrained hardware and safety arguments for learned components.
- [MLE404 Efficient Inference](../../../machine_learning_engineering/year_4/MLE404_efficient_inference_quantization_distillation/README.md): the same compression ideas at data-centre scale.
- The [EMB flagship industry project](../../../../06_career_and_market_readiness/05_industry_projects/EMB_embedded_systems_iot.md): its on-device anomaly model.
