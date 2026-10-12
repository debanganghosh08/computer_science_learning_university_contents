# DLR302 · Labs and projects

Every lab and project ships with code, a fixed data split saved to disk, results over at least 3 seeds where training is involved, and a write-up that shows failure cases as images. All work fits a free Colab or Kaggle GPU; pre-compute frozen features once to save quota.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Convolution and classic CNNs | Loop and `im2col` versions of `conv2d` with backward and max pooling; then LeNet-5 on MNIST and a small AlexNet-style net on CIFAR-10 | Gradchecks and a match with `F.conv2d`; accuracy, parameter and FLOP counts per layer | 7 h |
| 2 · ResNet reproduction | ResNet-18 on CIFAR-10; plain 56-layer net vs residual 56-layer net | ≥ 92% test accuracy; training curves showing degradation in the plain net | 5 h |
| 3 · Recipe ablation | AdamW, cosine schedule, label smoothing, mixup/CutMix, RandAugment, EMA on Imagenette | Ablation table with mean ± std over 3 seeds | 5 h |
| 4 · Shift audit | Train on PlantVillage; test on PlantDoc field images; near-duplicate search across splits | Accuracy gap with confidence intervals, duplicate report, 30 annotated failure images | 4 h |
| 5 · Backbone bake-off | Linear probe and fine-tune ResNet-50, ConvNeXt-T, DINOv2-S and SigLIP on one small dataset | Accuracy vs inference latency plot; recommendation memo | 4 h |
| 6 · Detection metrics and fine-tuning | Implement IoU, NMS and COCO AP; fine-tune a torchvision detector | AP matching `pycocotools` to 3 decimals; per-class AP table | 5 h |
| 7 · Segmentation vs SAM 3 | U-Net on a segmentation dataset; zero-shot SAM 3 with concept prompts on the same images | mIoU and Dice for both; cases where each wins | 4 h |
| 8 · ViT vs ResNet at equal compute | ViT-Tiny and ResNet-18 trained for the same GPU-hours on CIFAR-10 | Accuracy, throughput and memory; attention maps vs Grad-CAM | 4 h |
| 9 · Self-supervised pretraining | SimCLR (or a small MAE) on STL-10 unlabeled split; k-NN and linear-probe evaluation | Label-efficiency curves vs supervised initialisation | 6 h |
| 10 · CLIP and SigLIP probes | Zero-shot Food-101 with prompt ensembles; SigLIP 2 with English vs Hindi prompts; a counting/spatial probe set | Accuracy tables and a failure taxonomy | 3 h |

## Projects

### P1 · Crop disease classifier with an honest field test (L1, ~6 hours)

**Real-world inspiration.** Smartphone-based crop diagnosis has been studied since Mohanty et al. (2016), whose PlantVillage model scored 99.35% on held-out lab images but 31.4% on images taken in other conditions. PlantDoc (Singh et al., 2019) collected field-style images to measure that gap.

**What to build.** Fine-tune a pretrained backbone on PlantVillage classes that also appear in PlantDoc. Evaluate on both a PlantVillage test split and PlantDoc. Then improve field accuracy without training on PlantDoc's test images: stronger augmentation (background replacement, lighting), a self-supervised backbone, or a small labelled field set from PlantDoc's training split.

**Acceptance criteria**
- Class mapping between the two datasets is documented; classes without a match are excluded and listed.
- Reported: in-distribution accuracy, field accuracy and macro-F1, each with a 95% bootstrap confidence interval.
- At least two interventions are compared over 3 seeds, and the field accuracy gain of the best one is larger than its confidence interval.
- A Grad-CAM panel of 12 images shows at least one shortcut (background, leaf position) and how the intervention changed it.
- An abstain option: images below a confidence threshold are flagged, with the coverage–accuracy curve shown.

**Compute budget.** ≤ 4 GPU-hours on Kaggle or Colab.

**Stretch goals.** Export to ONNX and measure CPU latency on a phone-class processor; add a "not a leaf" detector using CLIP zero-shot.

**What it proves to an employer.** You report deployment-relevant accuracy, not just benchmark accuracy, and you can close a measured gap with data rather than guesswork.

### P2 · Road-object detection on Indian streets (L2, ~15 hours)

**Real-world inspiration.** IDD, from IIIT Hyderabad, captures Indian roads with auto-rickshaws, animals, unmarked lanes and dense mixed traffic, conditions underrepresented in Western driving datasets (Varma et al., 2018).

**What to build.** A detector for a chosen subset of IDD classes (for example: person, rider, motorcycle, autorickshaw, car, bus, truck, animal). Compare (a) a COCO-pretrained detector with class mapping and no training, (b) a fine-tuned two-stage or one-stage detector, and (c) an open-vocabulary detector prompted with class names.

**Acceptance criteria**
- Your own COCO-style evaluation reproduces `pycocotools` numbers; per-class AP and mAP@[.5:.95] are reported for all three systems.
- The fine-tuned detector beats the no-training baseline by at least 5 mAP points on the validation split.
- Inference speed is measured on a T4 at a stated resolution (images per second, p50 and p95 latency); target ≥ 15 images per second for the fine-tuned model.
- A slice analysis covers small objects, night or low-light images, and occluded objects, with 10 failure images per slice.
- The training config, seed, split files and exact package versions are committed; a single command reproduces the evaluation.

**Compute budget.** ≤ 12 GPU-hours on Kaggle or Colab.

**Stretch goals.** Tracking across video frames; test-time augmentation; distillation of the open-vocabulary detector's pseudo-labels into a fast detector.

**What it proves to an employer.** You can adapt detection models to a hard local domain and measure them with standard metrics you understand line by line.

### P3 · Label-efficient satellite land-use mapping with self-supervised features (L3, portfolio-grade, ~30 hours)

**Real-world inspiration.** Land-use and crop mapping from satellite imagery supports agriculture and planning. Labels are expensive, but unlabeled imagery is abundant. EuroSAT (Helber et al., 2017) provides labelled Sentinel-2 patches, and DINOv3 includes backbones trained for aerial and satellite images (Siméoni et al., 2025).

**What to build.** A study of how much labelling self-supervised learning saves:
1. pretrain your own small SimCLR or MAE model on unlabeled patches (EuroSAT images without labels, or Sentinel-2 tiles over an Indian region of your choice);
2. compare it with ImageNet-supervised initialisation, DINOv2/DINOv3 frozen features, and training from scratch;
3. evaluate with 1%, 5%, 10% and 100% of labels, by linear probe and by fine-tuning;
4. if you use Indian tiles, label a small region yourself (at least 300 patches) as a shifted test set.

**Acceptance criteria**
- Label-efficiency curves for all 4 initialisations, with 3 seeds per point and shaded confidence bands.
- Your self-supervised model beats training from scratch at 1% and 10% labels by a margin larger than seed variance; if it does not, the write-up explains why with evidence.
- A spatially separated test split (no neighbouring tiles across splits) is used, and the result is compared with a random split to show the leakage effect.
- A confusion matrix and a map-style visualisation of predictions over one region.
- Every number in the README is regenerated by one script from saved checkpoints.

**Compute budget.** ≤ 25 GPU-hours (pretraining ≤ 15).

**Stretch goals.** Dense segmentation with DINOv3 patch features; multispectral (13-band) input instead of RGB; a short model card covering geographic coverage and failure modes.

**What it proves to an employer.** You can run a controlled study, avoid spatial leakage, and quantify the value of self-supervision, which is what applied-science and research-engineer roles in vision ask for.

## Feeds into

- [DLR402 Multimodal Models](../../year_4/DLR402_multimodal_models/README.md): vision encoders, CLIP/SigLIP and grounding become parts of vision–language models.
- [DLR305 Generative Models](../DLR305_generative_models_vaes_gans_and_diffusion/README.md): U-Nets, ViTs and image evaluation reappear in diffusion models.
- [DLR404 Efficient Deep Learning and GPU Programming](../../year_4/DLR404_efficient_deep_learning_and_gpu_programming/README.md): convolution and attention kernels, quantisation for edge deployment.
- [OV11 AI for Science and Research Engineering](../../../../04_overlaps/OV11_ai_for_science_research_engineering/README.md): satellite, microscopy and medical imaging applications.
- [THS501 Thesis or Capstone I](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md): P3 is a natural seed for a thesis on label-efficient vision.
