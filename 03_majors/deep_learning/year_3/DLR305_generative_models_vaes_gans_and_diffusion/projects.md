# DLR305 · Labs and projects

Every lab and project ships with code, fixed seeds, sample grids, and metrics computed with one documented implementation (`clean-fid` for FID, with the sample count stated). Every dataset must have a licence that allows your use; list it. Never train on images of real people without their consent.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · KL directions, autoregressive pixels and VAEs | Forward vs reverse KL fits of a bimodal target; a small autoregressive model on binarised MNIST; a convolutional VAE on Fashion-MNIST with β ∈ {0.5, 1, 4} and KL annealing | Both KL fits; bits per dimension; rate–distortion plot; a detected and fixed posterior collapse | 7 h |
| 2 · VQ-VAE and codebook health | VQ-VAE on CIFAR-10; dead-code reset or EMA codebook | Codebook utilisation before/after; reconstructions; a small transformer prior's samples | 5 h |
| 3 · DCGAN and WGAN-GP | DCGAN on Flowers-102 at 64×64; WGAN-GP on a 25-Gaussian grid | FID over training; mode-coverage counts for both losses | 5 h |
| 4 · RealNVP | Coupling-layer flow on 2-D moons and on MNIST | Exact log-likelihood; bpd comparison with Lab 1 | 3 h |
| 5 · DDPM from scratch | U-Net with time embeddings; linear vs cosine schedules on CIFAR-10 at 32×32 | Training curves, samples at checkpoints, FID (10k samples) | 6 h |
| 6 · Samplers and flow matching | DDPM ancestral vs DDIM vs a second-order ODE solver; conditional flow matching on 2-D data, then CIFAR-10 with the Lab 5 U-Net; one reflow step on 2-D | FID vs network evaluations (10–250) for every sampler and both objectives; path-curvature measurement | 8 h |
| 7 · Guidance sweep | Class-conditional model with condition dropout; classifier-free guidance scales 1–10 | FID and class-accuracy (by a separate classifier) vs scale | 3 h |
| 8 · DiT and LoRA fine-tuning | Small DiT on VAE latents; LoRA fine-tune of an open latent diffusion checkpoint on 200 licensed images | DiT samples; LoRA samples; base model licence and dataset licence table | 6 h |
| 9 · Metrics that disagree | FID, precision/recall, CMMD and CLIPScore for 3 models; FID vs sample size and JPEG quality; nearest-neighbour memorisation check | A case where metrics disagree, explained; memorisation rate on a deliberately tiny training set | 4 h |
| 10 · Watermarks and C2PA | Invisible watermark on your outputs; robustness to crop, resize, JPEG, screenshot; C2PA manifest with `c2patool` | Detection rate per transformation; verified manifest; one-page compliance note | 4 h |

## Projects

### P1 · A conditional handwriting generator for Indian scripts (L1, ~6 hours)

**Real-world inspiration.** Synthetic handwriting is used to augment training data for handwriting recognition in low-resource scripts. The Devanagari Handwritten Character Dataset (UCI, https://archive.ics.uci.edu/dataset/389/devanagari+handwritten+character+dataset) provides 46 classes of 32×32 characters.

**What to build.** A class-conditional VAE (or conditional DCGAN) that generates a requested Devanagari character, plus a separately trained classifier used only for evaluation.

**Acceptance criteria**
- Generated samples are classified as the requested class by the held-out classifier at least 80% of the time (averaged over all 46 classes, 100 samples each).
- Per-class results show the 5 hardest characters, with samples and a hypothesis for each.
- For the VAE: the ELBO split into reconstruction and KL is reported on the test set; for the GAN: FID against real test images.
- A data-augmentation test: adding generated samples to a small real training set (10% of the data) changes the classifier's test accuracy by a measured amount, with 3 seeds.

**Compute budget.** ≤ 3 GPU-hours on a free T4.

**Stretch goals.** Style control (stroke thickness) through a disentangled latent; extend to Bengali or Tamil characters.

**What it proves to an employer.** You can build, condition and honestly evaluate a generative model, including whether its samples are useful downstream.

### P2 · Diffusion and flow matching from scratch, compared fairly (L2, ~15 hours)

**Real-world inspiration.** Image generators moved from DDPM-style diffusion (Ho et al., 2020) to flow-matching transformers (Esser et al., 2024). Teams choose between objectives and samplers by measured quality per unit of compute.

**What to build.** One U-Net, two training objectives (ε-prediction diffusion and conditional flow matching), on CIFAR-10 or a 64×64 dataset with a clear licence. Compare quality vs sampling cost.

**Acceptance criteria**
- Both models use identical architecture, data, optimizer and training compute (±5%), and the same evaluation code.
- FID (`clean-fid`, 10,000 samples, stated reference set) vs network evaluations from 4 to 250 steps for at least 2 samplers per model.
- Each model's FID beats your Lab 3 GAN on the same dataset at equal or lower training compute, or the write-up shows convincingly why not.
- A memorisation check: for 1,000 samples, the nearest training image (in DINOv2 or CLIP feature space) is reported, with the 10 closest pairs shown.
- Compute ≤ 12 GPU-hours on Kaggle or Colab; every figure is regenerated by one script.

**Stretch goals.** Class-conditional versions with classifier-free guidance; one reflow step for the flow model and its effect at 4 steps.

**What it proves to an employer.** You understand the two dominant generative objectives well enough to implement them and compare them without fooling yourself.

### P3 · Provenance-ready fine-tuned image generator for Indian folk-art styles (L3, portfolio-grade, ~30 hours)

**Real-world inspiration.** Designers and small textile businesses use generative tools for pattern ideas, and the law now requires that synthetic content be marked: EU AI Act Article 50 (from 2 August 2026) and India's amended IT Rules (in force 20 February 2026). Artists' consent and licensing are live disputes, so the dataset must be clean. The product here is illustrative; it does not reproduce any company's system.

**What to build.** A LoRA fine-tune of an open latent diffusion checkpoint whose licence permits your use (for example, a Stable Diffusion 1.5- or SDXL-class model in fp16 on a 16 GB GPU), trained on 300–1,000 images of a folk-art style such as Madhubani, Warli or Kalamkari that are public domain or openly licensed (for example, from Wikimedia Commons). Ship:
1. a dataset card listing source, licence and attribution for every image;
2. the fine-tuned LoRA with a model card;
3. an evaluation report;
4. a generation wrapper that adds an invisible watermark and a signed C2PA manifest to every output;
5. a compliance note mapping your outputs to Article 50 and India's labelling and metadata duties.

**Acceptance criteria**
- 100% of training images have a recorded licence that allows the use; images without one are excluded and counted.
- Style fidelity: a blind pairwise study with at least 20 raters prefers your model's outputs over the base model's for "looks like the style" in ≥ 70% of comparisons, with a confidence interval.
- Prompt alignment does not collapse: CLIPScore on 50 held-out prompts is within 10% of the base model's.
- Memorisation audit: no generated image among 2,000 has a near-duplicate in the training set at a threshold you justify; the closest 10 pairs are shown.
- Watermark detection ≥ 95% on clean outputs and reported after JPEG 75, 50% crop and resize; C2PA manifests verify with `c2patool`.
- Compute ≤ 25 GPU-hours.

**Stretch goals.** A style-strength control; a small user study with artisans or designers on usefulness; testing the detectability of your outputs by an off-the-shelf AI-image detector.

**What it proves to an employer.** You can ship a generative model that is legally and ethically defensible, with evidence, which is now a requirement for any company releasing generative features.

## Feeds into

- [DLR402 Multimodal Models](../../year_4/DLR402_multimodal_models/README.md): VQ tokens, audio codecs, video diffusion and any-to-any models.
- [DLR404 Efficient Deep Learning and GPU Programming](../../year_4/DLR404_efficient_deep_learning_and_gpu_programming/README.md): faster samplers, fused attention and quantised diffusion inference.
- [DLR501 Frontier Seminar](../../year_5/DLR501_frontier_seminar_interpretability_reasoning/README.md): diffusion language models and generative world models.
- [OV05 AI Security and Safety Engineering](../../../../04_overlaps/OV05_ai_security_safety/README.md): provenance, watermark robustness and misuse.
- [PRO301 Professional Practice: Ethics, Law and Responsible AI](../../../../05_shared_years_3_to_5/PRO301_professional_practice_ethics_law_and_responsible/README.md): consent, copyright and synthetic-media law.
