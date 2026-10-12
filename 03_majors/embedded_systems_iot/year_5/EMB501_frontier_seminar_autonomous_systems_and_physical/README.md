# EMB501 · Frontier Seminar: Autonomous Systems and Physical AI

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 5 · 9 | 4 (≈ 120 hours) | L4 → L5 | [EMB401](../../year_4/EMB401_edge_ai_and_tinyml/README.md), [EMB403](../../year_4/EMB403_robotics_software_with_ros_2/README.md) (with [EMB402](../../year_4/EMB402_embedded_and_iot_security/README.md) and [RES501](../../../../05_shared_years_3_to_5/RES501_research_methods_and_scientific_writing/README.md) alongside) | [THS501](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md), [THS502](../../../../05_shared_years_3_to_5/THS502_thesis_or_capstone_ii/README.md), [RES502](../../../../05_shared_years_3_to_5/RES502_reading_reproducing_and_extending_papers/README.md) |

## Why this course matters now

"Physical AI" means learned models that perceive and act in the real world: robot arms that fold laundry from a spoken instruction, humanoids trained partly in simulation, and vehicles that drive without a human. The field moved from closed demos to open, runnable models in two years: Physical Intelligence released π0 and π0.5 with code and weights under Apache 2.0; NVIDIA's GR00T N1.7 is a 3-billion-parameter open model whose inference needs a single 16 GB+ GPU (including Jetson Thor-class edge computers); Hugging Face's LeRobot packages these and smaller policies such as SmolVLA for low-cost arms; and Google DeepMind now lists a Gemini Robotics 2 family, including an on-device model. At the same time, the safety rules for autonomy are being written: ISO 21448 (safety of the intended functionality), ISO/PAS 8800 (2024, AI in road vehicles), and UL 4600 (safety cases for autonomous products), on top of ISO 26262 and IEC 61508. The gap between a policy that succeeds in a video and a system that is safe enough to deploy is where embedded engineers are needed: real-time control under the model, compute and energy budgets, runtime monitors, evaluation with honest statistics, and safety cases. This seminar takes you to the research frontier of that gap and prepares a thesis.

## Learning outcomes

By the end you can:

1. **Explain** the main approaches to autonomy (modular pipelines, imitation learning, reinforcement learning, vision-language-action models, world models) and **compare** their data, compute and safety implications.
2. **Read, present and critique** frontier papers, separating claims from evidence (success rates, sample sizes, evaluation protocols).
3. **Reproduce** a published robot-learning result (in simulation or on a low-cost arm) and **report** it with confidence intervals and ablations.
4. **Deploy** a learned policy on edge hardware within latency and control-rate budgets, with a deterministic safety layer underneath.
5. **Evaluate** policies under distribution shift with pre-registered protocols.
6. **Perform** hazard analysis (HARA, FMEA, FTA, STPA) and **write** a safety case (goal structuring notation) for a system with a learned component.
7. **Map** a system to ISO 26262, IEC 61508, ISO 21448, ISO/PAS 8800 and UL 4600 at the level needed to work with safety engineers.
8. **Analyse** security threats specific to learned autonomous systems (adversarial inputs, instruction injection into language-driven robots) and **design** defences.
9. **Write** a research proposal for a thesis that addresses an open problem in the field.

## Chapters and lessons

### Chapter 1 · The landscape of physical AI (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Modular vs end-to-end | Perception–planning–control pipelines vs learned policies; hybrid "dual-system" designs | Draw both architectures for a pick-and-place cell |
| 1.2 Where the field is (2026) | Open VLA models (π0/π0.5, GR00T N1.7, SmolVLA), closed families (Gemini Robotics 2), robot-learning libraries (LeRobot) | Build a table of 6 models: size, licence, inputs, compute, evaluation |
| 1.3 Autonomy in vehicles | Driving automation levels (SAE J3016), robotaxi operations, the role of safety drivers and remote assistance | Summarise one company's published safety methodology |
| 1.4 Reading claims critically | Demo videos vs evaluations; cherry-picking; what a success rate needs (trials, conditions, intervals) | Critique a published demo using a checklist |

**Check your understanding:** What does an end-to-end policy gain and lose compared with a modular stack? What would you need to know before believing "95% success"? Why do many deployed systems remain hybrid?

### Chapter 2 · Robot learning foundations (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Imitation learning | Behaviour cloning, compounding errors, action chunking (ACT), Diffusion Policy | Train ACT on a LeRobot simulation dataset; report success over 50 episodes |
| 2.2 Data collection | Teleoperation rigs (ALOHA, Mobile ALOHA), data quality, diversity vs quantity | Record 30 demonstrations on a low-cost arm or in simulation; write a dataset card |
| 2.3 Cross-embodiment datasets | Open X-Embodiment and RT-X; standard formats | Load and inspect two datasets; list their differences |
| 2.4 Reinforcement learning for robots | Sim-to-real, domain randomisation, reward design; links to [DLR403](../../../deep_learning/year_4/DLR403_reinforcement_learning_including_rl_for_language/README.md) | Train a simple policy in simulation with and without randomisation; test on shifted dynamics |

**Check your understanding:** Why do errors compound in behaviour cloning, and how does action chunking help? When is more diverse data better than more data? What does domain randomisation buy, and what does it cost?

### Chapter 3 · Vision-language-action models (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 From RT-2 to OpenVLA | Treating actions as tokens; co-training with web data | Present RT-2 or OpenVLA in 15 minutes with a critique |
| 3.2 Flow-matching policies | π0 and π0.5: action experts, open-world generalisation claims | Run an openpi checkpoint in simulation (LIBERO) and reproduce one reported number |
| 3.3 Action tokenisation | FAST tokenisation and its effect on training | Summarise FAST; compare autoregressive and flow-based action heads |
| 3.4 Generalist humanoid models | GR00T N1: dual-system architecture, synthetic and human-video data | Read the GR00T N1 paper; map its system 1/system 2 split onto embedded hardware |
| 3.5 Small models | SmolVLA and on-device variants; what shrinks and what breaks | Fine-tune SmolVLA on your Chapter 2 data; compare with ACT |

**Check your understanding:** Why might a VLA generalise to new instructions but fail on a new gripper? What is the role of the "action expert" in π0? When does a small task-specific policy beat a large generalist?

### Chapter 4 · World models and simulation (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Learned world models | DreamerV3 and model-based RL | Present DreamerV3's key idea and limits |
| 4.2 Video world models | NVIDIA Cosmos world foundation models; synthetic data generation | Generate or inspect synthetic scenes; list failure modes |
| 4.3 Physics simulators | Gazebo, Isaac Sim, MuJoCo-based suites; contact and friction limits | Measure the sim-to-real gap for one task you can run in both |
| 4.4 Evaluating with simulation | Simulation as a test oracle, scenario generation, coverage | Design 20 scenarios that stress your policy |

**Check your understanding:** Why can a policy exploit simulator bugs? What does a video world model know about physics, and how would you test it? When is simulated evaluation evidence for a safety case?

### Chapter 5 · Deploying learned policies on embedded hardware (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Compute budgets | VLA inference memory (for example openpi's >8 GB for inference; GR00T's 16 GB+), edge platforms (Jetson Orin/Thor class), power | Measure latency and power of a policy on your edge computer |
| 5.2 Control rates | Policy rate vs controller rate, action chunking, interpolation, jitter | Run a 5 Hz policy over a 200 Hz MCU controller; measure tracking error |
| 5.3 Compression for deployment | Quantisation and distillation (from EMB401 and [MLE404](../../../machine_learning_engineering/year_4/MLE404_efficient_inference_quantization_distillation/README.md)) applied to policies | Quantise a policy; measure success-rate change with confidence intervals |
| 5.4 Deterministic safety layers | Simplex architecture, velocity and force limits on the MCU, safety-rated stops, runtime monitors | Add a monitor that overrides unsafe commands; test with injected bad actions |

**Check your understanding:** Why should the learned policy never talk directly to motor drivers? What happens to a 5 Hz policy when the network stutters? How do you show that quantisation did not hurt safety, not only accuracy?

### Chapter 6 · Evaluating autonomous systems (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Statistics of success rates | Binomial confidence intervals, number of trials needed, comparing two policies | Compute the trials needed to distinguish 80% from 90% success |
| 6.2 Protocols | Pre-registered evaluation, fixed initial conditions, blind scoring, reporting failures | Write and pre-register an evaluation protocol for your reproduction |
| 6.3 Distribution shift | Lighting, clutter, new objects, new embodiments; out-of-distribution detection | Run your policy under 3 shifts; report each separately |
| 6.4 Field data | Disengagements, interventions, near misses; what operators should log | Design the logging schema for a deployed robot |

**Check your understanding:** Why is "20 successes out of 20" weaker evidence than it sounds? What makes an evaluation reproducible by another lab? Which field metrics are leading indicators of harm?

### Chapter 7 · Functional safety fundamentals (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Hazards and risk | Hazard analysis and risk assessment (HARA), severity, exposure, controllability | Run a HARA for an autonomous warehouse cart |
| 7.2 IEC 61508 and SILs | Safety lifecycle, safety integrity levels, systematic vs random failures | Assign SIL targets to 4 safety functions with reasons |
| 7.3 ISO 26262 | V-model, ASILs, safety goals, ASIL decomposition, hardware metrics (awareness) | Derive safety goals and decompose one ASIL for a braking function |
| 7.4 Analysis methods | FMEA, FTA, and STPA (system-theoretic process analysis) | Do an FTA and an STPA for the same hazard; compare what each finds |
| 7.5 Other domains | ISO 13849 for machinery control, IEC 62304 for medical software, DO-178C for avionics (awareness) | Map your EMB403 P3 robot onto ISO 13849 performance levels |

**Check your understanding:** Why does IEC 61508 treat software failures as systematic rather than random? What does ASIL decomposition require of independence? What can STPA find that FMEA misses?

### Chapter 8 · Safety for learned components (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 SOTIF | ISO 21448: hazards from functional insufficiencies and triggering conditions, known/unknown scenarios | List triggering conditions for a camera-based person detector |
| 8.2 AI-specific standards | ISO/PAS 8800 (2024) for AI in road vehicles; data and model lifecycle evidence | Write the data requirements a safety assessor would ask for |
| 8.3 Safety cases | UL 4600's safety-case approach; goal structuring notation (GSN); evidence and confidence | Write a GSN safety case for your Chapter 5 monitor |
| 8.4 Regulation | EU Machinery Regulation (EU) 2023/1230 (applies from January 2027); EU AI Act treatment of AI safety components (dates under revision; check the current text) | Build a regulatory map for a learned cobot sold in the EU and India |

**Check your understanding:** Why is "the model is 99% accurate" not a safety argument? What does a safety case claim, and what makes its evidence sufficient? How do you argue about scenarios you have not seen?

### Chapter 9 · Security of autonomous systems (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Vehicle cybersecurity | ISO/SAE 21434, UN Regulations No. 155 and 156; links to EMB402 | Map your EMB402 update system onto UN R156 concepts |
| 9.2 Attacks on perception (concepts) | Adversarial examples and physical patches as a threat class; defences (sensor fusion, plausibility checks, monitors) | Add a plausibility check that rejects physically impossible detections |
| 9.3 Language-driven robots | Instruction injection into language-conditioned policies and LLM planners; least-privilege action spaces; confirmation for risky actions | Design an action allow-list and confirmation policy for a language-driven arm |
| 9.4 Safety–security co-engineering | Where security failures become hazards; joint analysis | Extend your Chapter 7 STPA with security-caused control actions |

**Check your understanding:** Why must an LLM planner's output be treated as untrusted input to the controller? What does sensor fusion protect against, and what does it not? Why do safety and security teams need a shared hazard model?

### Chapter 10 · Lessons from failures (week 10)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Therac-25 | Software interlocks removed, race conditions, poor error messages | Present the failure chain and the design lessons |
| 10.2 Ariane 5 Flight 501 | Reused software, an unhandled conversion overflow, redundant units failing the same way | Explain why redundancy did not help |
| 10.3 Uber ATG, Tempe 2018 | Perception classification flips, disabled emergency braking, operator monitoring; NTSB findings | Write the safety-case gaps the NTSB report reveals |
| 10.4 Mars Pathfinder revisited | Priority inversion found and fixed in flight (from EMB302) | Compare how each case was detected and fixed |

**Check your understanding:** What do these failures have in common, despite different technologies? Why does identical redundancy fail against systematic faults? What would a runtime monitor have changed in each case?

### Chapter 11 · Research practice and open problems (weeks 11–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Reproduction as research | Reproducing a result, ablations, reporting negative results (with [RES502](../../../../05_shared_years_3_to_5/RES502_reading_reproducing_and_extending_papers/README.md)) | Complete your P3 reproduction with ablations |
| 11.2 Open problems | Generalisation across embodiments, data efficiency, verification of learned controllers, energy-efficient on-device policies, evaluation standards | Write a 2-page problem statement for one open problem |
| 11.3 Writing and presenting | Workshop-paper structure, figures for robot results, videos as evidence (and their limits) | Draft a 4-page workshop-style paper from your P3 |
| 11.4 Thesis proposals | Scope, risks, resources (compute, hardware), ethics review | Present a thesis proposal to the seminar for critique |

**Check your understanding:** What makes a reproduction publishable? How do you scope a thesis so that hardware delays do not sink it? Which open problem could your skills (embedded, real-time, safety) uniquely address?

## Weekly rhythm

| Week | Chapter | Seminar and lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Landscape discussion; model comparison table | Demo critique |
| 2 | 2 | Paper presentations (ACT, Diffusion Policy, Open X-Embodiment); Lab: train ACT | — |
| 3 | 3 | Paper presentations (RT-2, OpenVLA, π0, π0.5, GR00T N1); Lab: run openpi on LIBERO | **P1 due** |
| 4 | 4 | Paper presentations (DreamerV3, Cosmos); sim-to-real lab | — |
| 5 | 5 | Edge deployment lab with a safety layer | — |
| 6 | 6 | Evaluation protocols workshop | Pre-registered protocol |
| 7 | 7 | HARA, FTA and STPA workshop | Hazard analysis |
| 8 | 8 | Safety-case writing workshop; guest talk from a safety engineer (where available) | — |
| 9 | 9 | Security of autonomy workshop | **P2 due** |
| 10 | 10 | Failure case studies | Case presentation |
| 11 | 11 | Reproduction work (P3) | — |
| 12 | 11 | Reproduction work and ablations | — |
| 13 | 11 | Paper drafting | Draft paper |
| 14 | 11 | Thesis proposal presentations | **P3 due**, thesis proposal |
| 15 | Review | Mini-conference: paper presentations and oral examination | — |

## Working with AI in this course

- **Use AI for:** literature search and first-pass paper summaries (then read the paper); boilerplate for training and evaluation scripts; plotting with confidence intervals; first drafts of hazard lists and GSN structures that you then challenge; language editing of your paper.
- **Do without AI (drills):** hand-computing confidence intervals and required trial counts; HARA and FTA for a new system; reading a paper's evaluation section and listing what is missing; writing the safety argument's top-level claims. The oral examination is AI-off.
- **Verify AI output by:** checking every cited paper exists and says what is claimed (arXiv IDs, sections, tables); re-running numbers from released code; checking standards claims against the standard's actual clause (not a summary); testing generated safety monitors with injected faults.
- **Where AI still fails here (show it yourself):** in Week 1 you ask an assistant for a summary of the state of the art in robot foundation models with citations, then verify every citation and number. Log fabricated or mis-attributed citations, outdated model versions, success rates quoted without conditions, and confident statements about what a standard "requires". In robotics, language-model planners also propose actions that violate physical or safety constraints; Chapter 9's allow-list and confirmation design exists because of this.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Paper presentations and critiques (3) | 15% |
| Projects P1–P3 | 45% |
| Hazard analysis and safety case (Chapters 7–8) | 15% |
| Mini-conference paper, thesis proposal and oral examination (AI off) | 25% |

**Mastery gate.** You pass when you can: (1) reproduce a published robot-learning result within its reported confidence interval, or explain with evidence why you could not; (2) present a safety case for a system with a learned component that an independent reviewer judges complete at the top two levels of argument; (3) defend a thesis proposal that names an open problem, a method, a risk plan and an evaluation protocol.

## Industry reality

Where this is used: robotics companies building manipulation and humanoid platforms, autonomous-vehicle and driver-assistance teams, agricultural and warehouse automation, defence and space autonomy, and the safety-assessment firms and regulators that review them. Open releases have lowered the barrier to entry: openpi (Apache 2.0) states that inference needs more than 8 GB of GPU memory and LoRA fine-tuning more than 22.5 GB; GR00T N1.7 lists a 16 GB+ GPU for inference and 40 GB+ recommended for fine-tuning; and UL 4600 can be read free through UL's digital view. Engineers who combine robot learning with real-time embedded systems and safety engineering are rare (analysis), and that combination is the target of this seminar.

**Interview questions from this course**

1. *How would you deploy a vision-language-action policy on a real robot safely?* Strong answer: hybrid architecture with the policy proposing actions and a deterministic controller and safety layer on a microcontroller enforcing limits; latency and rate budgets; monitors and fallbacks; staged testing (simulation, blocks, supervised); logging; evaluation protocol.
2. *A paper reports 90% success. What do you ask before believing it?* Strong answer: number of trials and confidence interval, task and initial-condition distribution, scoring method, number of seeds and checkpoints, failures shown, comparison baselines, hardware and compute, released code.
3. *What is SOTIF and why does it matter for perception?* Strong answer: hazards from functional insufficiency rather than faults; triggering conditions; known-unsafe and unknown-unsafe scenarios; how scenario-based testing and field monitoring reduce the unknown area; link to ISO/PAS 8800 for AI.
4. *Walk me through a hazard analysis for an autonomous mobile robot.* Strong answer: system definition, hazards (collision, crush, falling loads), severity/exposure/controllability, safety goals, safety functions (speed and separation monitoring, safety-rated stop), required integrity levels, verification; mentions STPA for control-structure hazards.
5. *How would you stop an LLM-driven robot from doing something dangerous because of a malicious instruction?* Strong answer: treat model output as untrusted, constrained action space with allow-lists, physical limits enforced below the model, confirmation for risky actions, input provenance, monitoring and audit logs, red-team testing within scope.

## Reading list

Core papers (all free on arXiv):

- Brohan et al., "RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control" (2023) — https://arxiv.org/abs/2307.15818
- Open X-Embodiment Collaboration, "Open X-Embodiment: Robotic Learning Datasets and RT-X Models" (2023) — https://arxiv.org/abs/2310.08864
- Zhao et al., "Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware" (ACT, 2023) — https://arxiv.org/abs/2304.13705
- Chi et al., "Diffusion Policy: Visuomotor Policy Learning via Action Diffusion" (2023) — https://arxiv.org/abs/2303.04137
- Fu et al., "Mobile ALOHA" (2024) — https://arxiv.org/abs/2401.02117
- Kim et al., "OpenVLA: An Open-Source Vision-Language-Action Model" (2024) — https://arxiv.org/abs/2406.09246
- Black et al., "π0: A Vision-Language-Action Flow Model for General Robot Control" (2024) — https://arxiv.org/abs/2410.24164
- Physical Intelligence, "π0.5: a Vision-Language-Action Model with Open-World Generalization" (2025) — https://arxiv.org/abs/2504.16054
- Pertsch et al., "FAST: Efficient Action Tokenization for Vision-Language-Action Models" (2025) — https://arxiv.org/abs/2501.09747
- NVIDIA, "GR00T N1: An Open Foundation Model for Generalist Humanoid Robots" (2025) — https://arxiv.org/abs/2503.14734
- Gemini Robotics Team, "Gemini Robotics: Bringing AI into the Physical World" (2025) — https://arxiv.org/abs/2503.20020
- Shukor et al., "SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics" (2025) — https://arxiv.org/abs/2506.01844
- Hafner et al., "Mastering Diverse Domains through World Models" (DreamerV3, 2023) — https://arxiv.org/abs/2301.04104
- NVIDIA, "Cosmos World Foundation Model Platform for Physical AI" (2025) — https://arxiv.org/abs/2501.03575
- Liu et al., "LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning" (2023) — https://arxiv.org/abs/2306.03310

Safety and failure analysis:

- Nancy Leveson and John Thomas, *STPA Handbook* (2018, free) — https://psas.scripts.mit.edu/home/get_file.php?name=STPA_handbook.pdf
- Leveson and Turner, "An Investigation of the Therac-25 Accidents", *IEEE Computer* (1993) — http://sunnyday.mit.edu/papers/therac.pdf
- ESA, Ariane 5 Flight 501 Failure inquiry board report (1996) — https://esamultimedia.esa.int/docs/esa-x-1819eng.pdf
- NTSB, collision between a vehicle controlled by a developmental automated driving system and a pedestrian, Tempe, Arizona (HWY18MH010) — https://www.ntsb.gov/investigations/Pages/HWY18MH010.aspx
- Philip Koopman, UL 4600 resources (free digital view of the standard via UL) — https://users.ece.cmu.edu/~koopman/ul4600/
- Standards to know by number (texts are paid; your institution's library may have access): IEC 61508, ISO 26262:2018, ISO 21448:2022, ISO/PAS 8800:2024, ISO/SAE 21434:2021, ISO 13849, IEC 62304.

## Resources (free first)

- **Code and models:** LeRobot — https://github.com/huggingface/lerobot ; openpi — https://github.com/Physical-Intelligence/openpi ; Isaac-GR00T — https://github.com/NVIDIA/Isaac-GR00T ; Gemini Robotics models page — https://deepmind.google/models/gemini-robotics/
- **Simulation:** Gazebo — https://gazebosim.org/docs/ ; LIBERO benchmark (paper above)
- **Background courses:** Russ Tedrake, *Underactuated Robotics* and *Robotic Manipulation* (MIT, free) — https://underactuated.mit.edu/ and https://manipulation.csail.mit.edu/ ; Lynch and Park, *Modern Robotics* — http://hades.mech.northwestern.edu/index.php/Modern_Robotics
- **Optional books:** Nancy Leveson, *Engineering a Safer World* (MIT Press, 2011), the theory behind STPA (check your library or the publisher for an open-access copy); Philip Koopman, *How Safe Is Safe Enough?* (2022), on measuring autonomous-vehicle safety.

## Sources

- Physical Intelligence openpi repository (π0, π0-FAST, π0.5; Apache 2.0; GPU memory requirements) — https://github.com/Physical-Intelligence/openpi (checked 2026-10)
- NVIDIA Isaac-GR00T repository (N1.7, 3B parameters, hardware requirements; N1 cited as March 2025) — https://github.com/NVIDIA/Isaac-GR00T (checked 2026-10)
- LeRobot repository (supported policies and robots) — https://github.com/huggingface/lerobot (checked 2026-10)
- Google DeepMind, Gemini Robotics models page (Gemini Robotics 2, ER 2, On-Device 2) — https://deepmind.google/models/gemini-robotics/ (checked 2026-10)
- Koopman, UL 4600 page (editions 2020 and 2022; free digital view) — https://users.ece.cmu.edu/~koopman/ul4600/ (checked 2026-10)
- arXiv metadata for every paper in the reading list (checked 2026-10 via the arXiv API)

_Last reviewed: 2026-10_
