# MOB501 · Labs and projects

This is a seminar, so labs are short, measurement-focused builds that support the week's reading. Hardware comes from the course pool; book it early. Any study involving people (comfort ratings, usability tests) follows RES501's ethics process: informed consent, no recording of bystanders, and data deleted at the end of the course. Agent experiments run only on emulators and test accounts, never on real accounts or real payments.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Watch platforms | The same glanceable feature as a Wear OS complication and widget and a watchOS widget; phone–watch sync | Sync-delay and battery measurements on both platforms | 5 h |
| 2 · Sensors and BLE | A step counter from raw accelerometer data compared against a reference; a BLE GATT client | Error vs reference over three walks; reconnection log | 5 h |
| 3 · Tracking and drift | Measure ARCore or ARKit anchor drift along a 50 m path with marked ground-truth points | Drift table with variance across five runs | 5 h |
| 4 · visionOS and Android XR | Port a 2D app to a window or panel; add one volume or spatial element | Video; frame-time capture | 6 h |
| 5 · Comfort and performance study | Five participants rate comfort and legibility under two frame-rate or text-size settings | Consent forms; anonymised ratings; analysis | 5 h |
| 6 · Glasses and multimodal prototype | A phone-camera prototype of "what am I looking at?" with an on-device model and a cloud fallback | Latency and battery budget; bystander-privacy policy | 5 h |
| 7 · App Intents and AppFunctions | Expose two actions, one with a side effect behind confirmation | Tests; threat model for the side-effect action | 4 h |
| 8 · Agent evaluation reproduction | Run a small AndroidWorld-style task set on an emulator with an open or API model | Success rates per task with variance over three runs | 6 h |
| 9 · Foldables | Make a flow continuous across fold, unfold and resize | Test results across postures; state-loss bugs found and fixed | 4 h |

## Projects

### P1 · Critical review of a frontier claim (L4, ~6 hours)

**Real-world inspiration:** program committees and engineering leads review claims before resources are committed. Platform keynotes and arXiv papers in XR, wearables and phone agents often report results under narrow conditions.

**What to build:** a written review of one paper (from the Chapter 4 or Chapter 7 reading lists, or approved by the instructor) or one platform claim (for example a developer-preview feature's stated performance).

**Acceptance criteria:**
- **Claims table:** every central claim listed with its evidence and your assessment (supported, partly supported, unsupported).
- **Substance:** at least one limitation that matters for practitioners, supported by evidence (a calculation, a small rerun, a missing baseline, or documentation that contradicts the claim).
- **Small rerun:** one figure, number or measurement reproduced at small scale, or a clear explanation of why it cannot be.
- **Length and clarity:** about 2,500 words, readable by a senior engineer outside the subfield.

**Stretch goals:** send a polite, specific question to the authors or file a documentation issue, and record the response.

**What it proves to an employer or lab:** you can judge new technology on evidence, the skill that separates staff engineers and researchers from early adopters.

### P2 · A product on a new surface (L4, ~15 hours)

**Real-world inspiration:** companies extend phone products to watches, headsets and glasses when one moment of use fits the device. Examples to choose from (all illustrative scenarios): medication reminders with adherence logging on a watch; a spatial version of your MOB403 design on visionOS or Android XR; a glanceable delivery status on display glasses (emulator).

**What to build:** one surface, integrated with a phone app you already have, with a written performance and privacy budget.

**Acceptance criteria:**
- **Performance budget met:** for watches, the feature costs at most 3% battery per day in a scripted day of use; for headsets, at least 95% of frames meet the display's frame deadline during a 5-minute scripted session; for glasses prototypes, a stated latency budget for every interaction is met at p90.
- **Usability:** five participants complete three tasks; you report task success, time and System Usability Scale scores, with consent records.
- **Privacy:** a data-flow diagram with retention periods; no camera or microphone data leaves the device without explicit consent.
- **Integration:** state stays consistent between phone and new surface when either goes offline for 10 minutes.

**Stretch goals:** expose the feature to a system assistant (App Intents or AppFunctions) with confirmation; add an accessibility mode tested with a screen reader or captions.

**What it proves to an employer:** you can extend a product to a new device with discipline about budgets, privacy and real users.

### P3 · Reproduction or extension study (L5, research-grade, ~30 hours)

**Real-world inspiration:** RES502's reproduce-then-extend method applied to mobile frontier topics. Choose one (or propose another):
- **AR in Indian public spaces:** measure ARCore and ARKit anchor drift and relocalisation success in crowded, reflective or featureless environments (markets, metro concourses), compared with published drift figures.
- **Agents and exposed actions:** reproduce a subset of AndroidWorld tasks, then extend by exposing the same actions through AppFunctions-style interfaces in test apps, and measure the change in success rate and unsafe actions.
- **Where should multimodal inference run?** Measure latency, energy and quality of on-watch or on-glasses-class inference against phone offload and cloud for one task.
- **Neural capture on phones:** Gaussian splat quality against capture time and device tier, using published metrics (PSNR, SSIM, LPIPS).

**What to build:** a pre-registered protocol, a measurement harness, the study itself and a paper-style report with an artefact package.

**Acceptance criteria:**
- **Protocol:** written and reviewed before data collection, including the number of trials, the statistics you will report and the threats to validity.
- **Rigour:** at least the pre-registered number of trials, with variance and confidence intervals; deviations from the protocol are reported.
- **Rerun:** a classmate reruns your artefact from your instructions and obtains results within your reported variance.
- **Report:** about 8 pages in a conference format (introduction, related work, method, results, limitations, ethics statement); negative results are acceptable if well measured.
- **Ethics:** no bystander recording, no real accounts or payments in agent studies, consent for any participant data.

**Stretch goals:** submit to a student workshop or post a preprint after instructor review; release the dataset under an open licence if consent allows.

**What it proves to an employer or lab:** you can produce new, rerunnable knowledge about mobile systems, the entry ticket to research roles, R&D teams and a strong thesis.

## Feeds into

- [THS501 Thesis or Capstone I](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md) and [THS502 Thesis or Capstone II](../../../../05_shared_years_3_to_5/THS502_thesis_or_capstone_ii/README.md): P3 is designed to become a thesis chapter or capstone.
- [RES502 Reading, Reproducing and Extending Papers](../../../../05_shared_years_3_to_5/RES502_reading_reproducing_and_extending_papers/README.md): the same reproduction standards.
- [LCH502 Career Launch and Founder Studio](../../../../05_shared_years_3_to_5/LCH502_career_launch_and_founder_studio/README.md): P2 can seed a product on a new surface.
