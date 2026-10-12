# DLR · Deep Learning: roles and market (2026)

| Learning path | Interview loop | AI impact | Market overview |
|---|---|---|---|
| [Deep Learning major](../../../03_majors/deep_learning/README.md) | [AI-driven interviews](../../04_ai_driven_interviews/) | [Matrix row](../ai_impact_matrix.md) | [Market map](../README.md) |

All figures were checked in October 2026. Paragraphs marked **Analysis** are interpretation, not measurement.

## Role titles and seniority ladder

| Level | Common titles |
|---|---|
| Entry | Research Intern, AI Resident, Research Engineer I, Applied Deep Learning Engineer |
| Mid | Research Engineer, ML Engineer (training), Applied Scientist |
| Senior | Senior Research Engineer, Research Scientist, Member of Technical Staff (pretraining, post-training, evaluation, inference) |
| Staff and above | Staff/Principal Research Scientist, Research Lead |

Many research-scientist roles in industry expect a PhD or a publication record. Research-engineer roles more often hire strong engineers without a PhD who can implement, scale and debug experiments. A separate specialism is the **GPU performance engineer**, who writes kernels in CUDA or Triton and optimises training and inference (DLR404).

## What the work looks like day to day

- Read papers, reproduce results and run ablations.
- Train and fine-tune models: data mixtures, optimisers, learning-rate schedules, normalisation (DLR304).
- Debug training instability: loss spikes, divergence, numerical precision problems.
- Scale training across many GPUs: data, tensor and pipeline parallelism.
- Post-train language models: supervised fine-tuning, preference optimisation, reinforcement learning (DLR401, DLR403).
- Build evaluations that measure what matters, and guard against benchmark contamination.
- Write kernels and profile memory bandwidth and compute use (DLR404).
- Study how models work internally: interpretability (DLR501).

## Demand signals

- **Where models are built.** Industry produced over 90% of notable frontier models in 2025 ([AI Index 2026](https://hai.stanford.edu/assets/files/ai_index_report_2026.pdf)).
- **PhD pipeline.** New AI PhDs in the US and Canada rose 22% from 2022 to 2024, but "the PhDs that make up that increase took jobs in academia, not in industry" ([AI Index 2026](https://hai.stanford.edu/assets/files/ai_index_report_2026.pdf)). AI-software-related master's graduates in the US grew 82% from 2022 to 2024 (same source). Competition for industry research roles is intense.
- **Capital.** US private AI investment reached $285.9 billion in 2025 ([AI Index 2026](https://hai.stanford.edu/ai-index/2026-ai-index-report)).
- **US projections.** Computer and information research scientists +22% from 2025 to 2035, a small occupation of 38,600 people; the typical entry education is a master's degree ([BLS](https://www.bls.gov/ooh/computer-and-information-technology/computer-and-information-research-scientists.htm)).
- **Snapshot of frontier labs.** On 12 Oct 2026, Anthropic's job board listed 33 roles with "Research Engineer" in the title and OpenAI's listed 14 ([Anthropic careers](https://www.anthropic.com/jobs), [OpenAI careers](https://openai.com/careers)). This is a one-day count from two employers, not a market measure.
- **India.** India showed one of the fastest increases in AI talent concentration among LinkedIn members (+120% from 2019 to 2025), and the largest net outflow of AI research authors and inventors of any country in 2025 ([AI Index 2026](https://hai.stanford.edu/assets/files/ai_index_report_2026.pdf)). Many Indian AI researchers build their careers abroad, which leaves room for those who build research careers in India (**analysis**).

## How AI is changing the role

**Automated or mostly automated.** Boilerplate model code, data loaders, plotting, experiment configuration, and first drafts of paper sections and related-work summaries.

**Augmented.** Implementing a method from a paper, writing evaluation harnesses, debugging tensor-shape and numerical issues, and writing kernels (with careful testing). METR's measurements show frontier agents completing machine-learning engineering tasks that take humans hours, at 50% reliability ([METR](https://metr.org/time-horizons/)).

**Growing in value.**

- Research taste: choosing which experiment is worth the compute.
- Experimental rigour: controls, seeds, confidence intervals, honest reporting.
- Scaling and systems knowledge: memory, communication, parallelism.
- Evaluation science, including for safety and reliability.
- Interpretability and alignment research.

A caution from the evidence: engineers who relied heavily on AI while learning showed "learning penalties" in one study cited by the AI Index ([AI Index 2026](https://hai.stanford.edu/assets/files/ai_index_report_2026.pdf)). Build the fundamentals by hand first (DLR301: autograd and backpropagation from scratch).

**Analysis.** AI is accelerating AI research itself, which raises the bar: a research engineer is expected to run more experiments, faster, with AI help. The scarce skills are judgement about what to try and the ability to tell a real result from noise.

## Pay (indicative)

| Market | Role in source | Figure | Type | Source |
|---|---|---|---|---|
| US | Computer and information research scientists | Median $140,300; 10th $82,200; 90th $230,630 (May 2025) | Official survey | [BLS](https://www.bls.gov/ooh/computer-and-information-technology/computer-and-information-research-scientists.htm) |
| India | Research Scientist | Average base ₹8.2 lakh; base range ₹3.0–30 lakh (212 profiles, May 2026) | Self-reported, whole market | [Payscale](https://www.payscale.com/research/IN/Job=Research_Scientist/Salary) |
| India | Research Scientist (title within software engineering) | Median total pay ₹54.5 lakh, the top-paying software title (Oct 2026) | Self-reported, mostly product companies | [Levels.fyi](https://www.levels.fyi/t/software-engineer/locations/india) |

The huge gap between the two India figures reflects who reports: Payscale covers all employers using the title (including academic and government labs); Levels.fyi mostly covers large technology companies. Frontier-lab pay is far above official medians and is not reliably published.

## The hiring loop

Typical loop for industry research roles (varies widely):

1. Screen on publications, open-source work or reproduced papers.
2. Coding interview: practical Python and sometimes DSA.
3. Deep learning fundamentals: backpropagation, attention, normalisation, optimisation, scaling behaviour.
4. Implementation exercise: implement or debug a model component (for example an attention layer or a training loop) under time pressure.
5. Research discussion or job talk: present your work and defend choices.
6. Behavioural and team matching.

See [AI-driven interviews](../../04_ai_driven_interviews/).

## Durable skills that make you hard to replace

- Linear algebra, probability, calculus and optimisation.
- PyTorch internals and automatic differentiation.
- GPU architecture and performance profiling.
- Experimental design and statistics.
- Reading, reproducing and extending papers (RES502).
- Clear scientific writing.

## Adjacent roles and transitions

- **Machine learning engineering** ([MLE](MLE_machine_learning_engineering.md)).
- **AI engineering**: applying models in products ([AIE](AIE_ai_engineering.md)).
- **Computer science research** ([CSG](CSG_computer_science_general.md)).
- **AI for science**: overlap OV11.
- **AI safety and security**: overlap OV05.
- **Edge AI and efficient models** ([EMB](EMB_embedded_systems_iot.md)).

## Sources

All checked October 2026.

- Stanford HAI, AI Index 2026 (report and summary page). https://hai.stanford.edu/assets/files/ai_index_report_2026.pdf ; https://hai.stanford.edu/ai-index/2026-ai-index-report
- BLS, Occupational Outlook Handbook: Computer and Information Research Scientists (2025–35; May 2025 pay; modified 27 Aug 2026). https://www.bls.gov/ooh/computer-and-information-technology/computer-and-information-research-scientists.htm
- METR, Time horizons (updated 8 Sep 2026). https://metr.org/time-horizons/
- Job boards on 12 Oct 2026: https://www.anthropic.com/jobs ; https://openai.com/careers
- Payscale India: Research Scientist; Levels.fyi India: Software Engineer (self-reported; 12 Oct 2026). https://www.payscale.com/research/IN/Job=Research_Scientist/Salary ; https://www.levels.fyi/t/software-engineer/locations/india

_Last reviewed: 2026-10_
