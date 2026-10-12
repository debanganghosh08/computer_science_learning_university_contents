# FE303 · Labs and projects

Every lab is checked three ways: automated (axe-core, Stylelint, contrast scripts), manually (keyboard and at least one screen reader), and visually (screenshots at 320 px, 1280 px, 400% zoom and forced colours). The APG lab is done without AI assistants. Audits of public websites use normal browsing only: no automated scanning of sites you do not own beyond loading pages, and no attempts to bypass anything.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Layers refactor | Re-architect a 1,500-line stylesheet with `@layer`, `:where()` and `@scope` | Zero `!important`; a layer diagram; screenshots proving no visual change | 4 h |
| 2 · Intrinsic layouts | Five layouts with no media queries; container-query card in three slots; RTL mirroring | Screenshots at 320/768/1920 px, Urdu RTL and 400% zoom; reflow test results | 5 h |
| 3 · Native overlays | `<dialog>`, popover, invoker commands; anchored tooltip with `@supports` fallback | Feature table (native vs JavaScript lines saved); keyboard tests | 4 h |
| 4 · Colour and type | OKLCH palette, light/dark/high-contrast themes; Hindi and English type scale; subset Devanagari font | Contrast report over every token pair (all pass 4.5:1 or 3:1 as required); CLS from fonts at most 0.01 | 5 h |
| 5 · Token pipeline | DTCG tokens to CSS variables, Android XML and Swift with Style Dictionary 5 | Pipeline repository; one rename propagated to three platforms in one commit | 4 h |
| 6 · Headless components | `Select`, `Dialog` and `Tabs` on a headless library with your tokens; one breaking change shipped with a codemod | Storybook; axe zero per story; codemod tests | 6 h |
| 7 · APG patterns (no AI) | Menu button, listbox and grid built from scratch per the WAI-ARIA Authoring Practices | Keyboard test matrix; NVDA recording | 6 h |
| 8 · Three screen readers | Run one purchase flow on NVDA, VoiceOver (macOS or iOS) and TalkBack | Logs comparing announcements; fixes for every blocker | 4 h |
| 9 · WCAG-EM audit | Audit 10 pages of a public Indian website by normal browsing | Report with severity, success criterion, reproduction steps and suggested fixes; one ACR section | 6 h |
| 10 · Indic and low-end | Localise a flow into Hindi and Tamil; test at 200% Android font scale on a low-cost phone outdoors | Before/after screenshots; list of truncations and contrast fixes | 4 h |

## Projects

### P1 · Accessible service-request form (L1, ~6 hours)

**Real-world inspiration:** Indian government services increasingly run through web forms, and GIGW 3.0 requires WCAG 2.1 AA on them. The *Pragya Prasun* judgement (April 2025) held that digital access is part of the right to life. Your form, a request for a duplicate certificate, is an **illustrative scenario**, not a real service.

**What to build:** a three-step form with:
- personal details, a document upload and review, with a progress indicator;
- inline and summary errors, and Hindi and English versions;
- light, dark and high-contrast themes;
- a layout that works from 320 px.

No CSS framework and no JavaScript framework: semantic HTML, modern CSS and less than 150 lines of JavaScript.

**Acceptance criteria:**
- **Automated:** axe-core reports zero violations on every step in both languages and all themes. The HTML validator reports zero errors.
- **Manual:** an NVDA script and a TalkBack script, each completing the form with one deliberate error, pass. Error messages are announced, and focus moves to the error summary.
- **WCAG 2.2 specifics:** targets at least 24×24 CSS px; no focus hidden under the sticky header (2.4.11); information already entered is not requested again (3.3.7); the upload works without drag-and-drop (2.5.7).
- **Resilience:** reflow at 400% zoom with no horizontal scrolling; text-spacing override with no clipping; correct rendering in forced-colours mode.
- **Language:** `lang` set correctly on mixed Hindi/English content; no clipped matras.

**Stretch goals:** progressive enhancement so the form submits with JavaScript disabled; a print stylesheet for the review step.

**What it proves to an employer:** you can deliver a form that passes a real accessibility audit, which is the most common accessibility work in Indian government, banking and insurance projects.

### P2 · Multi-brand token system and core components (L2, ~15 hours)

**Real-world inspiration:** groups that run several brands on shared code need one component library with many themes. GitHub Primer and IBM Carbon publish how they theme and document components. The two brands here (a bank and its payments sub-brand) are an **illustrative scenario**.

**What to build:**
- a DTCG token set (primitive → semantic → component) for two brands × light/dark × default/high-contrast;
- a Style Dictionary pipeline to CSS, Android and iOS;
- eight components on a headless library: `Button`, `TextField`, `Select`, `Checkbox`, `Dialog`, `Tabs`, `Toast` and `Tooltip`;
- Storybook documentation with usage rules and accessibility notes.

**Acceptance criteria:**
- **Contrast:** an automated script checks every foreground/background token pair used by every component state in all 8 theme combinations. All pass WCAG 2 thresholds (4.5:1 text, 3:1 non-text).
- **Accessibility:** axe in Storybook reports zero violations across all stories. A keyboard matrix for each component matches the APG pattern. `Toast` uses a polite live region and is never the only place an error appears.
- **No raw values:** Stylelint blocks raw colours, spacing and font sizes in component CSS. CI fails on a planted violation.
- **Visual regression:** screenshot tests cover every story in every theme. A planted 1 px padding change is caught.
- **Change management:** one breaking rename ships with a codemod and a deprecation warning, and a consumer app upgrades with zero manual edits.
- **Size:** each component's CSS plus JavaScript is at most 6 KB gzipped, excluding the headless library (`size-limit`).

**Stretch goals:** a third, high-legibility mode (larger type, stronger contrast) for older users; Figma variables synced from the same tokens.

**What it proves to an employer:** you can run the engineering side of a design system: tokens, theming, documentation and safe change.

### P3 · Accessible design system v1 with conformance evidence (L3, portfolio-grade, ~30 hours)

**Real-world inspiration:** the GOV.UK Design System and India's [UX4G](https://www.ux4g.gov.in/) show what public, accessible components with documented patterns look like. SEBI's 2025 circular asks regulated entities for audited accessibility, so a design system that ships conformance evidence saves every product team audit work.

**What to build:** extend P2 to 15+ components, adding:
- `Combobox`;
- a sortable, paginated `DataTable`;
- a `DatePicker` with Indian date formats and Hindi month names;
- `Accordion`, `Breadcrumbs`, `Pagination`, `FileUpload` and `Alert`.

Then publish it as a versioned package with a documentation site containing usage guidance, do/don't examples and accessibility notes per component. Also add:
- a per-component assistive-technology test matrix (NVDA, VoiceOver, TalkBack; JAWS optional);
- an Accessibility Conformance Report for the library;
- a contribution guide with an accessibility acceptance checklist;
- RTL (Urdu) and Indic script support.

**Acceptance criteria:**
- **Conformance:** a WCAG-EM-style evaluation of the documentation site and a sample app built from the library finds zero AA failures. The ACR documents every criterion as Supports, Partially Supports or Not Applicable, with justification.
- **Assistive technology:** a test matrix with recorded evidence for each component on three screen readers. Every known difference between screen readers is documented with its impact.
- **Internationalisation:** all components render correctly in Urdu (RTL, with no mirrored-icon errors) and in Hindi and Tamil, without clipping at 200% text size.
- **Quality gates in CI:** axe per story, visual regression in every theme, token lint, type check, unit and interaction tests. A pull request that breaks any one of them is blocked (demonstrated).
- **Adoption test:** two classmates build a provided 3-screen app using only your docs in under 2 hours each, with zero axe violations in their output.
- **AI audit:** you generate the same 3 screens with an AI tool told to use your library, then report how many raw values, missing labels and focus errors appeared, and which documentation changes reduced them.

**Stretch goals:** web-component builds of 5 components for non-React consumers; a public versioned changelog with migration guides; a third-party audit by a certified professional if available to you.

**What it proves to an employer:** you can build and govern the shared UI layer of an organisation, with the conformance evidence that regulators and procurement teams now ask for. That combination is rare and hard to replace.

## Feeds into

- [FE403 AI-Native Interfaces](../../year_4/FE403_ai_native_interfaces_streaming_generative_ui/README.md): accessible streaming, live regions and generative UI built from your components.
- [FE404 Frontend System Design at Scale](../../year_4/FE404_frontend_system_design_at_scale/README.md): design-system governance and internationalisation at organisation scale.
- [FE402 Advanced UI](../../year_4/FE402_advanced_ui_animation_graphics_webgl_and_webgpu/README.md): motion and data visualisation that respect reduced motion and screen readers.
- [QAE305 Mobile and Cross-Browser Testing](../../../software_quality_test_engineering/year_3/QAE305_mobile_and_cross_browser_testing/README.md), as an elective that extends the assistive-technology test matrix.
