# EMB501 · Labs and projects

Compute and hardware: a GPU with at least 8 GB of memory for running open VLA checkpoints (openpi states >8 GB for inference; larger models need more), shared lab GPUs or cloud credits for fine-tuning (openpi states >22.5 GB for LoRA fine-tuning), an edge computer (Jetson-class or a laptop GPU), your EMB403 robot or a low-cost arm supported by LeRobot (for example SO-100/SO-101), and a microcontroller for the safety layer. Simulation-only paths are accepted for every lab and for P1 and P3; P2 needs either real hardware or hardware-in-the-loop with a real MCU. Real-robot work follows the EMB403 safety rules (speed and force limits, hardware stop, supervision).

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Demo critique and model table | Critique a published robot demo with a checklist; compare 6 models (size, licence, inputs, compute, evaluation) | Critique (1 page); comparison table with a source for every cell | 3 h |
| 2 · Train ACT | Train ACT on a LeRobot simulation dataset; evaluate over 50 episodes | Success rate with a 95% confidence interval; training curves; failure examples | 5 h |
| 3 · Run an open VLA | Run an openpi or SmolVLA checkpoint on a LIBERO task suite; compare with a reported number | Your number vs the paper's, with conditions; discrepancy notes | 6 h |
| 4 · Sim-to-real gap | Run one task in simulation and on hardware (or a recorded real dataset); measure the gap | Paired results; the 5 largest causes with evidence | 4 h |
| 5 · Policy over a safety layer | A slow policy commands a fast MCU controller with velocity, workspace and force limits; inject bad actions | Tracking error vs policy rate; monitor intervention log | 5 h |
| 6 · Pre-registered evaluation | Compute trials needed to detect a 10-point difference; write and register an evaluation protocol | Power calculation; protocol document with timestamp | 3 h |
| 7 · Hazard analysis three ways | HARA, FTA and STPA for an autonomous warehouse cart or your EMB403 robot | All three analyses; a comparison of what each found | 5 h |
| 8 · A safety case in GSN | Goal structuring notation safety case for the Lab 5 monitor, with evidence links | GSN diagram; evidence table; reviewer comments addressed | 4 h |
| 9 · Language-driven arm guardrails | Allow-list action space and confirmation policy for a language-conditioned arm; test with adversarial instructions in simulation | Design note; test results (blocked, confirmed, executed) | 4 h |

## Projects

### P1 · A critical survey with a runnable baseline (L1, ~6 hours)

**Real-world inspiration.** Robotics teams choosing between open models must compare claims that use different tasks, robots and metrics; an engineer who can turn those claims into a fair, runnable comparison saves months (illustrative scenario).

**What to build.** A 4-page critical survey of 4–6 robot-learning approaches from the reading list, plus a runnable baseline: ACT and one VLA (SmolVLA or an openpi checkpoint) evaluated on the same simulated task suite with the same protocol.

**Acceptance criteria**
- Every claim in the survey cites the paper's table or section; every model's licence and compute needs are stated with sources.
- Both policies evaluated on at least 50 episodes per task with 95% confidence intervals and the same initial-condition seeds.
- At least 3 failure modes per policy described with examples (videos or frame sequences).
- A one-command script reproduces your evaluation.
- GPU hours and approximate energy for training and evaluation reported.

**Stretch goals.** Add Diffusion Policy as a third baseline; evaluate under one distribution shift (lighting or object change).

**What it proves to an employer.** You can cut through claims in a fast-moving field and produce comparable, reproducible numbers.

### P2 · A learned policy on edge hardware with a safety case (L2, ~15 hours)

**Real-world inspiration.** Collaborative robots and mobile manipulators that use learned policies still need deterministic limits underneath and a written safety argument before anyone deploys them near people (illustrative of the approach in ISO 21448 and UL 4600).

**What to build.** Deploy a trained policy (from P1 or fine-tuned on your own demonstrations) on an edge computer controlling a low-cost arm or your EMB403 robot, with a microcontroller safety layer that enforces velocity, workspace and (where measurable) force limits and a watchdog on the command stream. Write a hazard analysis (HARA plus STPA) and a GSN safety case for the combined system.

**Acceptance criteria**
- **Budget:** policy latency (median and 99th percentile) and control-loop jitter measured on the edge computer and MCU; the action-chunk or interpolation design keeps the controller at its rate when the policy stalls.
- **Monitor:** in at least 200 injected unsafe commands (out-of-workspace, over-speed, sudden jumps), the safety layer blocks or clamps 100% and logs each event.
- **Watchdog:** if the policy process is killed, motion stops within 300 ms in 10 of 10 trials.
- **Evaluation:** task success under a pre-registered protocol with at least the number of trials your Lab 6 calculation requires, reported with a 95% interval.
- **Safety case:** top-level claim, argument and evidence links for each hazard; at least one hazard you could not fully mitigate is stated as residual risk with operating restrictions.

**Stretch goals.** Quantise the policy (from EMB401 and MLE404 methods) and show the success rate and latency change with intervals; add a learned out-of-distribution detector that triggers a safe stop.

**What it proves to an employer.** You can put a learned model on real hardware without trusting it blindly, with the measurements and the safety argument a robotics or automotive safety team expects.

### P3 · Reproduce and extend a frontier result: a workshop paper (L3, portfolio-grade, ~30 hours)

**Real-world inspiration.** Research labs and advanced engineering teams decide what to build on by reproducing published results; reproductions that add a careful extension (edge deployment, energy, safety monitoring, robustness) are publishable and highly visible to employers.

**What to build.** Reproduce one reported result from the reading list (in simulation or on hardware) and extend it in a direction this major prepares you for: running it within an embedded compute or energy budget, measuring the effect of a safety monitor on task success, robustness under distribution shift, or performance on low-cost hardware. Write it up as a 4–6 page workshop-style paper.

**Acceptance criteria**
- **Reproduction:** your number falls within the reported confidence interval, or a documented analysis explains the discrepancy (environment, seeds, checkpoints, hardware) with evidence.
- **Extension:** at least two ablations; every result reported with 95% confidence intervals and the trial counts justified by a power calculation.
- **Release:** code, configurations and evaluation seeds published; one command reruns the main table; compute and energy used are reported.
- **Paper:** workshop format with related work, method, results, limitations, and a safety and ethics statement; reviewed by two classmates with responses to every comment.
- **Presentation:** a 12-minute talk at the course mini-conference with live or recorded evidence.

**Stretch goals.** Submit to a robotics or embedded-ML workshop; turn the extension into your THS501 thesis proposal.

**What it proves to an employer.** You can operate at the research frontier with engineering rigour: reproduce, extend, measure honestly and communicate. Research labs, robotics startups and advanced autonomy teams hire for this, and it is the natural start of a thesis or a deep-tech company.

## Feeds into

- [THS501 Thesis or Capstone I](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md) and [THS502 Thesis or Capstone II](../../../../05_shared_years_3_to_5/THS502_thesis_or_capstone_ii/README.md): P3 is designed to become a thesis proposal.
- [RES502 Reading, Reproducing and Extending Papers](../../../../05_shared_years_3_to_5/RES502_reading_reproducing_and_extending_papers/README.md): shared reproduction methods.
- [LCH502 Career Launch and Founder Studio](../../../../05_shared_years_3_to_5/LCH502_career_launch_and_founder_studio/README.md): P2's safety-layered deployment is a credible base for a robotics product.
