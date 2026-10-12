# EMB401 · Edge AI and TinyML

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 4 · 7 | 4 (≈ 120 hours) | L3 → L4 | [EMB301](../../year_3/EMB301_microcontrollers_and_embedded_c/README.md) (with [CS214](../../../../02_year_2_core_computer_science/semester_4/CS214_machine_learning_foundations/README.md) assumed) | [EMB501](../../year_5/EMB501_frontier_seminar_autonomous_systems_and_physical/README.md), [OV09A](../../../../04_overlaps/OV09_edge_ai_secure_iot/OV09A_deploying_models_on_edge_devices/README.md); pairs with [MLE404](../../../machine_learning_engineering/year_4/MLE404_efficient_inference_quantization_distillation/README.md) |

## Why this course matters now

Running models on the device removes the round trip to the cloud: a wake word must be detected in tens of milliseconds, a vibration anomaly must be flagged on a pump with no network, and raw audio or camera frames often must not leave the device at all. The tools have matured: LiteRT for Microcontrollers (formerly TensorFlow Lite Micro) fits its core runtime in 16 KB on a Cortex-M3; PyTorch's ExecuTorch made Cortex-M a first-class target with CMSIS-NN kernels in its 1.2 release and supports Arm Ethos-U NPUs; MLCommons' MLPerf Tiny benchmarks keyword spotting, visual wake words, image classification, anomaly detection and streaming wake words on microcontroller-class hardware; and microcontrollers with neural accelerators (Arm Ethos-U, ST's STM32N6) are now ordinary parts. Hosted tools such as Edge Impulse (now part of Qualcomm) can take you from data to a firmware library in an afternoon. What they cannot do is decide whether the model is still accurate on your sensor, in your factory, after int8 quantisation, at 3 mW. This course teaches you to collect the right data, fit models into kilobytes, and prove accuracy, latency and energy on the device.

## Learning outcomes

By the end you can:

1. **Decide** when on-device ML is justified over thresholds, classical DSP or the cloud, with latency, energy, privacy and cost arguments.
2. **Collect and curate** sensor datasets on devices, and **split** them by device, person or session so that evaluation reflects deployment.
3. **Design** feature pipelines (log-mel spectrograms, MFCCs, spectral and statistical features) that run within an MCU budget using CMSIS-DSP.
4. **Train** small architectures (DS-CNN, MobileNet-style, 1D CNNs, autoencoders, tree ensembles) under explicit flash, RAM and latency budgets.
5. **Quantise** models to int8 with post-training quantisation and quantisation-aware training, and **measure** accuracy loss overall and by slice.
6. **Deploy** models with LiteRT Micro, ExecuTorch, CMSIS-NN-backed kernels and vendor tools, and **size** the tensor arena from measurement.
7. **Measure** latency, peak memory and energy per inference on the device, and **compare** with MLPerf Tiny-style methodology.
8. **Build** end-to-end keyword spotting, anomaly detection and visual wake-word systems with streaming inference and threshold tuning.
9. **Operate** models on fleets: versioning, OTA model updates, on-device monitoring and drift detection.

## Chapters and lessons

### Chapter 1 · Why ML on the device (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 The case for the edge | Latency, bandwidth, energy per transmitted bit vs per inference, privacy, offline operation | Compute energy to send 1 s of audio over BLE vs classify it locally (use measured numbers from EMB304) |
| 1.2 The hardware spectrum | Cortex-M4F/M7, Cortex-M55 with Helium, Ethos-U NPUs, ESP32-S3 vector instructions, STM32N6, Linux-class edge (Raspberry Pi 5, NVIDIA Jetson) | Place 8 boards on a chart of RAM, compute and power |
| 1.3 When not to use ML | Thresholds, hysteresis, classical filters and rules that beat a model | Solve a "tap detection" task with a threshold; then argue whether ML adds value |
| 1.4 Benchmarks | MLPerf Tiny tasks, reference models and quality targets; what a benchmark does not tell you | Read one MLPerf Tiny result and list the conditions behind its numbers |

**Check your understanding:** When does sending raw data to the cloud cost less energy than local inference? Why is RAM, not compute, usually the binding constraint on an MCU? What is missing from a benchmark latency number for your product?

### Chapter 2 · Sensor data and datasets (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Collecting on the device | Logging firmware, sample rates, timestamps, metadata (device, placement, person, session) | Collect 30 minutes of labelled IMU or audio data from your own device |
| 2.2 Labelling and windows | Window length and stride, event vs window labels, class balance, "unknown" and "silence" classes | Choose window sizes for 3 tasks with justification |
| 2.3 Leak-free evaluation | Split by device, person or session; why random splits overstate accuracy | Show the accuracy gap between random and by-person splits |
| 2.4 Public datasets | Speech Commands, Visual Wake Words, ToyADMOS, MIMII; licences and limits | Combine a public dataset with your own recordings; measure domain shift |

**Check your understanding:** Why does a model trained on one microphone fail on another? What leaks when windows from the same recording appear in both train and test? Why must "none of the above" be a class?

### Chapter 3 · Signal processing for features (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Audio features | Framing, windowing, FFT, mel filter banks, log-mel and MFCC | Implement log-mel on the host; match it bit-for-bit with the device version |
| 3.2 Vibration and IMU features | RMS, peak, crest factor, spectral bands, orientation-independent features | Extract features from a motor's vibration at 3 speeds |
| 3.3 CMSIS-DSP | Fixed-point and float FFTs, filters, statistics on Cortex-M; cycle costs | Measure FFT cycles for 256 and 1,024 points in q15 and f32 |
| 3.4 Feature budgets | Feature cost vs model cost; when the feature extractor is the bottleneck | Profile a KWS pipeline: what fraction is features? |

**Check your understanding:** Why must the training pipeline and the firmware compute features identically? When is a q15 FFT accurate enough? Why can features dominate inference time?

### Chapter 4 · Small model architectures (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Convolutions for small devices | Depthwise-separable convolutions, DS-CNN for keyword spotting, MobileNet width multipliers | Count MACs and parameters of 3 architectures by hand |
| 4.2 1D models for sensor streams | 1D CNNs and small recurrent or attention layers; receptive field | Train a 1D CNN for activity recognition under 50 KB |
| 4.3 Classical models on MCUs | Decision trees and gradient-boosted trees compiled to C (for example emlearn) | Compare a tree ensemble and a CNN on the same features |
| 4.4 Architecture search awareness | MCUNet-style joint search of model and memory schedule | Read MCUNet; summarise what it optimises and why |

**Check your understanding:** Why do depthwise-separable convolutions save compute but sometimes not latency? When will a tree ensemble beat a neural network on a microcontroller? What does a MAC count fail to predict?

### Chapter 5 · Quantisation (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Integer arithmetic | Scale and zero point, per-tensor vs per-channel, int8 accumulation in int32 | Quantise one layer by hand; check against the converter |
| 5.2 Post-training quantisation | Representative datasets, calibration, full-integer conversion | Convert your model to int8; measure size and accuracy change |
| 5.3 Quantisation-aware training | Fake quantisation, fine-tuning, when PTQ is not enough | Recover accuracy lost in PTQ with QAT |
| 5.4 Evaluating by slice | Overall accuracy vs worst-slice accuracy (speakers, machines, noise levels) | Find the slice your quantised model breaks on |

**Check your understanding:** Why does a bad representative dataset ruin int8 accuracy? Why is per-channel quantisation preferred for convolution weights? What should block a release even if overall accuracy dropped only 0.5%?

### Chapter 6 · Runtimes and toolchains (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 LiteRT for Microcontrollers | Interpreter, op resolver, tensor arena, model as a C array, supported ops | Run your int8 model on a Cortex-M4F board |
| 6.2 Optimised kernels | CMSIS-NN and vendor kernels; checking that the optimised path is actually used | Measure latency with reference vs CMSIS-NN kernels |
| 6.3 ExecuTorch on microcontrollers | Export, Cortex-M and Ethos-U backends | Deploy the same model with ExecuTorch; compare footprint and latency |
| 6.4 Vendor and hosted tools | Edge Impulse (EON compiled models), ST Edge AI tools, ESP-DL; lock-in and reproducibility | Build the same model in a hosted tool; compare with your pipeline |

**Check your understanding:** How do you prove the optimised kernels ran and not the reference ones? What is the risk of a hosted tool for a 10-year product? Why can an unsupported operator force a whole redesign?

### Chapter 7 · Memory planning (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Where bytes go | Weights in flash, activations and scratch in RAM, arena overhead, input buffers | Draw the memory map of your firmware with the model loaded |
| 7.2 Arena sizing | Measuring arena use, peak activation memory, operator order | Shrink the arena to the measured minimum plus margin |
| 7.3 Reducing peak memory | Patch-based inference (MCUNetV2), smaller input resolutions, streaming layers | Cut peak RAM by 30% with an architectural change |
| 7.4 External memory | PSRAM and external flash: bandwidth and energy costs | Measure latency with weights in internal vs external memory |

**Check your understanding:** Why does peak activation memory, not parameter count, often decide if a model fits? What does streaming inference save? When is PSRAM worth its energy cost?

### Chapter 8 · Keyword spotting end to end (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 The pipeline | Microphone (PDM/I2S), ring buffer, sliding windows, features, model, posterior smoothing | Run continuous KWS on your board |
| 8.2 Streaming inference | Overlapping windows, stride vs latency, avoiding recomputation | Halve compute with a streaming-friendly model |
| 8.3 Thresholds and errors | False accepts per hour vs false rejects; ROC curves; per-speaker results | Tune thresholds on 1 hour of background noise |
| 8.4 Real-world robustness | Noise, distance, accents and languages (including Indian-language keywords), microphone variation | Record 10 speakers; report the worst speaker's error rate |

**Check your understanding:** Why is "false accepts per hour" a better metric than accuracy for a wake word? What does posterior smoothing trade? Why must evaluation include speakers not in training?

### Chapter 9 · Anomaly detection and predictive maintenance (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Learning "normal" | Autoencoders, Gaussian models, one-class methods; reconstruction error | Train an autoencoder on normal fan or pump vibration |
| 9.2 Thresholds without many failures | Percentile thresholds, validation with synthetic faults, alarm hysteresis | Set a threshold that yields fewer than 1 false alarm per day |
| 9.3 Drift and re-baselining | Seasonal and load changes, sensor ageing, on-device baseline updates | Simulate a load change and show the false-alarm spike and fix |
| 9.4 Datasets and evaluation | ToyADMOS, MIMII, AUC vs operating point | Report AUC and the operating point you would ship |

**Check your understanding:** Why is AUC not enough to choose an alarm threshold? How do you validate a detector when real failures are rare? When should a device re-learn "normal", and what can go wrong?

### Chapter 10 · Vision at the edge (week 10)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Visual wake words | Person or no-person at low resolution; camera interfaces | Run a person detector on an ESP32-S3 or Cortex-M7 board |
| 10.2 NPUs on microcontrollers | Ethos-U with the Vela compiler, STM32N6-class accelerators; supported operators; fallback to CPU | Compile a model for an NPU target (simulator or board); compare CPU and NPU paths |
| 10.3 Frame budgets | Frames per second vs energy; duty-cycled vision; motion-triggered capture | Build a 1-frame-per-second person counter and measure energy per frame |
| 10.4 Linux-class edge | Raspberry Pi 5 and Jetson-class boards; ExecuTorch or LiteRT on Linux; small language models on the edge (llama.cpp) and their memory cost | Run a small detector and a small language model on a Pi; record latency and power |

**Check your understanding:** Why might an NPU make some models slower? When is a microcontroller camera better than a Raspberry Pi camera system? What decides whether a small language model belongs on a device at all?

### Chapter 11 · Measuring latency, energy and accuracy on the device (week 11)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Latency | Cycle counters, GPIO markers, warm vs cold runs, interrupt interference | Report median and worst-case latency over 1,000 inferences |
| 11.2 Energy per inference | Current traces, integrating charge, separating features, model and idle | Measure µJ per inference with a power profiler or shunt |
| 11.3 Device vs desktop agreement | Bit-exactness tests, tolerance for float paths, test vectors in CI | Build a test that compares 500 device outputs with the host model |
| 11.4 Reporting honestly | Conditions (clock, compiler flags, memory placement), MLPerf Tiny-style reporting | Write a one-page benchmark report others could reproduce |

**Check your understanding:** Why might the same model run 2× slower from external flash? How do you separate the energy of the feature extractor from the model? What must a reproducible benchmark state?

### Chapter 12 · Edge AI in production (weeks 12–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 12.1 Model lifecycle | Model versioning with firmware, OTA model-only updates, compatibility checks | Ship a model update to your device without reflashing firmware |
| 12.2 Monitoring on fleets | On-device confidence histograms, sampled data upload with consent, drift alarms | Detect a deliberately shifted input distribution from fleet telemetry |
| 12.3 Privacy and security | Keeping raw data on-device, DPDP Act 2023 considerations, model extraction and tampering (detailed in EMB402) | Write the data-flow and privacy note for your P3 |
| 12.4 Hardware and model co-design | Choosing a chip for a model family and a model for a chip; costs at volume | Write a chip recommendation for a 100,000-unit product (illustrative) |

**Check your understanding:** Why version models and firmware together? What can a fleet's confidence histogram tell you that accuracy on a test set cannot? Which data may leave the device, and who decides?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Edge or cloud? Energy arithmetic | — |
| 2 | 2 | Lab 2 · Collect your own dataset | Dataset card |
| 3 | 3 | Lab 3 · Bit-exact features | — |
| 4 | 4 | Lab 4 · Architectures under a budget | **P1 due** |
| 5 | 5 | Lab 5 · Quantisation by slice | — |
| 6 | 6 | Lab 6 · Three runtimes, one model, and an AI audit | — |
| 7 | 7 | Lab 7 · Arena diet | Mid-term (AI off) |
| 8 | 8 | Lab 8 · Wake word, false accepts per hour | — |
| 9 | 9 | Lab 9 · Anomaly thresholds | — |
| 10 | 10 | Lab 10 · NPU vs CPU | **P2 due** |
| 11 | 11 | Energy per inference (in P3) | Benchmark report |
| 12 | 12 | OTA model update (in P3) | — |
| 13 | 12 | Drift monitoring (in P3) | — |
| 14 | — | — | **P3 due** |
| 15 | Review | Oral defence of P3 | Final exam (AI off) |

## Working with AI in this course

- **Use AI for:** data-pipeline and training scripts; plotting and evaluation code; explaining converter errors and unsupported-operator messages; generating test-vector harnesses; summarising papers (MCUNet, MLPerf Tiny) before you read them yourself.
- **Do without AI (drills):** MAC, parameter and activation-memory counts; int8 scale and zero-point arithmetic; window and stride choices; energy-per-inference calculations from a trace; reading an arena-usage report. The mid-term and final are AI-off.
- **Verify AI output by:** checking every claim about operator support against the runtime's actual operator list and your build; running device-vs-host comparison tests; measuring latency and energy on the board; re-evaluating with a by-device or by-person split; checking that optimised kernels are linked (symbol table, cycle counts).
- **Where AI still fails here (show it yourself):** in Lab 6 you ask an assistant for firmware that runs your model with each runtime. Record the defects: APIs from the old TensorFlow Lite Micro or a different ExecuTorch version, made-up arena sizes, feature extraction that does not match training, float models presented as "quantised", and latency or accuracy figures with no measurement behind them. More broadly, assistants tend to suggest random train/test splits, which overstate accuracy on sensor data; your Lab 2 shows by how much.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (10) | 25% |
| Projects P1–P3 | 35% |
| Mid-term (AI off) | 10% |
| Final exam (AI off) + P3 oral defence | 30% |

**Mastery gate.** You pass when you can, with AI off: (1) given a model description and an MCU, decide in 20 minutes whether it fits (flash, peak RAM, latency) and what to change if not; (2) take a float model to int8 on a device and report overall and worst-slice accuracy, latency and energy, matching the host within a stated tolerance; (3) defend your P3's evaluation split, threshold and energy budget in an oral exam.

## Industry reality

Where this is used: wake words in speakers and earbuds, gesture and activity recognition in wearables, predictive maintenance on motors and pumps, people counting and occupancy sensing, crop and livestock monitoring, and in-cabin sensing in vehicles. The ecosystem is consolidating around a few runtimes (LiteRT Micro, ExecuTorch, vendor compilers) and NPUs in microcontrollers, and a community benchmark (MLPerf Tiny) gives a shared reporting method. Edge AI roles ask for both embedded and ML depth, a combination that is rarer than either alone (analysis; see the [market map](../../../../06_career_and_market_readiness/01_market_map/roles/EMB_embedded_systems_iot.md)).

**Interview questions from this course**

1. *How would you fit a keyword-spotting model into 64 KB of RAM?* Strong answer: computes activation memory per layer, picks DS-CNN-style layers, int8 quantisation, streaming inference, arena measurement, features computed in-place, weights in flash; verifies with the runtime's arena report.
2. *What happens to accuracy when you quantise to int8, and how do you check it?* Strong answer: representative calibration data, per-channel weights, PTQ vs QAT, evaluation by slice and on device (bit-exact tests), and a release criterion on the worst slice.
3. *How do you measure energy per inference?* Strong answer: power profiler or shunt plus amplifier, GPIO markers to align phases, integrate charge over many inferences, separate idle, features and model, state clock and memory placement.
4. *Your anomaly detector raises 20 false alarms a day in a new factory. What do you do?* Strong answer: check domain shift (mounting, load, speed), re-baseline on site with a validation period, threshold by percentile with hysteresis, add context features, monitor alarm rate per device, and avoid retraining on unverified "normal" that contains faults.
5. *When would you not use ML on the device?* Strong answer: when a threshold, filter or rule meets the requirement, when data is too scarce to validate, when the model cannot be updated or monitored, or when energy for sensing dominates; gives an example of each.

## Resources (free first)

- **Primary texts:** Vijay Janapa Reddi et al., *Machine Learning Systems* (free online book with TinyML chapters) — https://mlsysbook.ai/ ; HarvardX Tiny Machine Learning courses on edX (free to audit) — https://www.edx.org/certificates/professional-certificate/harvardx-tiny-machine-learning
- **Runtimes and libraries:** LiteRT for Microcontrollers — https://developers.google.com/edge/litert/microcontrollers/overview ; tflite-micro repository — https://github.com/tensorflow/tflite-micro ; ExecuTorch — https://github.com/pytorch/executorch ; CMSIS-NN — https://github.com/ARM-software/CMSIS-NN ; CMSIS-DSP — https://github.com/ARM-software/CMSIS-DSP ; Arm Ethos-U Vela compiler — https://pypi.org/project/ethos-u-vela/ ; ESP-DL — https://github.com/espressif/esp-dl ; emlearn — https://github.com/emlearn/emlearn ; Edge Impulse documentation — https://docs.edgeimpulse.com/
- **Benchmarks:** MLPerf Tiny — https://mlcommons.org/benchmarks/inference-tiny/ ; Banbury et al., "MLPerf Tiny Benchmark" (arXiv 2106.07597) — https://arxiv.org/abs/2106.07597
- **Papers:** Zhang et al., "Hello Edge: Keyword Spotting on Microcontrollers" (arXiv 1711.07128) — https://arxiv.org/abs/1711.07128 ; Lai et al., "CMSIS-NN" (arXiv 1801.06601) — https://arxiv.org/abs/1801.06601 ; David et al., "TensorFlow Lite Micro" (arXiv 2010.08678) — https://arxiv.org/abs/2010.08678 ; Lin et al., "MCUNet" (arXiv 2007.10319) — https://arxiv.org/abs/2007.10319 ; Lin et al., "MCUNetV2" (arXiv 2110.15352) — https://arxiv.org/abs/2110.15352
- **Datasets:** Speech Commands (arXiv 1804.03209) — https://arxiv.org/abs/1804.03209 ; Visual Wake Words (arXiv 1906.05721) — https://arxiv.org/abs/1906.05721 ; ToyADMOS (arXiv 1908.03299) — https://arxiv.org/abs/1908.03299 ; MIMII (arXiv 1909.09347) — https://arxiv.org/abs/1909.09347
- **Paid, optional:** Pete Warden and Daniel Situnayake, *TinyML* (O'Reilly, 2019; APIs dated, concepts current); Daniel Situnayake and Jenny Plunkett, *AI at the Edge* (O'Reilly, 2023).

## Sources

- Google, LiteRT for Microcontrollers overview (16 KB core on Cortex-M3; C++17; tested on Cortex-M and ESP32) — https://developers.google.com/edge/litert/microcontrollers/overview (checked 2026-10)
- PyTorch ExecuTorch releases (v1.2: Cortex-M as first-class target with CMSIS-NN; v1.1: Zephyr with Ethos-U; latest v1.5.1) — https://github.com/pytorch/executorch/releases (checked 2026-10)
- MLCommons, MLPerf Tiny benchmark page (tasks and quality targets) — https://mlcommons.org/benchmarks/inference-tiny/ (checked 2026-10)
- Edge Impulse website (corporate address c/o Qualcomm Incorporated) — https://www.edgeimpulse.com/ (checked 2026-10)

_Last reviewed: 2026-10_
