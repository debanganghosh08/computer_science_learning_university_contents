# FE303 · CSS, Design Systems and Accessibility

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 3 · 5 | 4 (≈ 120 hours) | L2 → L3 | [FND114](../../../../01_year_1_foundations/semester_2/FND114_web_foundations_http_html_css_and_javascript/README.md), [CS205](../../../../02_year_2_core_computer_science/semester_3/CS205_software_engineering_i_design_testing/README.md) | [FE403](../../year_4/FE403_ai_native_interfaces_streaming_generative_ui/README.md), [FE404](../../year_4/FE404_frontend_system_design_at_scale/README.md), [FE402](../../year_4/FE402_advanced_ui_animation_graphics_webgl_and_webgpu/README.md) |

Part of the [Frontend Engineering major](../../README.md). FND114 covered the cascade, Flexbox, Grid, WCAG basics and a first NVDA pass. This course turns those into engineering disciplines: CSS architecture, design-system engineering, and accessibility that holds up in an audit and in court.

## Why this course matters now

The web is mostly inaccessible, and AI tools learned from that web. WebAIM's February 2026 scan of the top million home pages found detectable WCAG failures on 95.9% of them, with 56.1 errors per page on average. Low-contrast text appeared on 83.9% of pages, and pages using ARIA averaged more errors (59.1) than pages without it (42). In India the obligation is becoming concrete:
- the Rights of Persons with Disabilities (RPwD) Act 2016, and its 2023 amendment rules notifying Bureau of Indian Standards accessibility standards for ICT products and services;
- GIGW 3.0, which requires WCAG 2.1 AA on government sites;
- the Supreme Court's 2025 holding in *Pragya Prasun* that digital access is part of the right to life;
- SEBI's July 2025 circular requiring regulated financial entities to make websites and apps accessible and to be audited by IAAP-certified auditors.

The EU's European Accessibility Act has applied since 28 June 2025. Meanwhile CSS has changed. Container queries and `:has()` are now "widely available", and `@scope` and container style queries reached Baseline in 2026. UI generators (v0, Lovable, Bolt) and design-to-code tools such as the Figma MCP server produce plausible markup fast. A human still has to own the token architecture, the component contracts and the screen-reader experience.

## Learning outcomes

By the end you can:

1. **Architect** CSS for a large codebase with cascade layers, `@scope`, custom properties and a stated naming or utility strategy, and **predict** every conflict.
2. **Build** intrinsic, container-aware layouts that work from 320 px to ultra-wide, at 400% zoom, in RTL and in Indic scripts.
3. **Use** native interactive primitives (`<dialog>`, popover, invoker commands, view transitions) with progressive enhancement where support is not Baseline.
4. **Design** a colour, typography and token system (DTCG format) that themes multiple brands, dark mode and forced-colours mode from one source.
5. **Engineer** a component library: API design, headless behaviour, documentation, versioning, codemods and deprecation.
6. **Conform** components and pages to WCAG 2.2 AA, and **prove** it with automated checks plus scripted tests in NVDA, VoiceOver and TalkBack.
7. **Audit** a site with WCAG-EM and **write** an Accessibility Conformance Report (VPAT) that would satisfy a procurement or SEBI-style review.
8. **Explain** India's accessibility law (RPwD Act, the 2023 ICT standards rules, GIGW 3.0, SEBI's circular, Supreme Court judgements) and the EU and US equivalents, as they apply to a product team.

## Chapters and lessons

### Chapter 1 · The cascade as architecture (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Cascade layers | `@layer` order beats specificity; layering resets, tokens, components, utilities and overrides; importing third-party CSS into a layer | Refactor a stylesheet with 40 `!important`s to zero using layers |
| 1.2 Specificity tools | `:where()` for zero specificity, `:is()`, `@scope` with lower bounds (Baseline March 2026), native nesting | Scope a card's styles so they cannot leak into nested content |
| 1.3 Custom properties | Inheritance, fallbacks, `@property` for typed and animatable properties, the cost of very deep variable chains | Build a themable button whose 6 states come from 4 variables |
| 1.4 Strategies compared | Utility-first (Tailwind CSS 4), CSS Modules, BEM, runtime CSS-in-JS and its rendering cost; what generated code tends to use | Build one component in three strategies; compare CSS bytes, specificity graph and change cost |

**Check your understanding:** Why does a layered rule with low specificity beat an unlayered rule with high specificity? When does `@scope` solve a problem that BEM solved by convention? What does runtime CSS-in-JS cost on a low-end phone, and where is that cost paid?

### Chapter 2 · Intrinsic and container-aware layout (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Intrinsic sizing | `min-content`, `max-content`, `fit-content`, `minmax()`, `clamp()`; letting content decide | Build a layout with zero media queries that works from 320 px to 1920 px |
| 2.2 Grid in depth | Subgrid (widely available since March 2026), named lines, dense packing and its reading-order problem | Align card footers across a row with subgrid |
| 2.3 Container queries | Size queries and container units (widely available), style queries (Baseline May 2026) | A product card that changes layout by its container, used in three different slots |
| 2.4 Logical properties and writing modes | `inline`/`block` axes, `dir`, `dir="auto"`, Urdu (RTL) and Hindi on one page | Make a page mirror correctly for Urdu with no RTL-specific stylesheet |
| 2.5 Reflow and zoom | WCAG 1.4.10 Reflow (320 CSS px), 1.4.4 Resize Text, 1.4.12 Text Spacing; `field-sizing` (Baseline June 2026) | Pass reflow at 400% zoom and the text-spacing bookmarklet test |

**Check your understanding:** Why is a container query a better fit for a component library than a media query? What breaks for keyboard users when grid `dense` reorders items? What changes in your CSS when the same page must work in Urdu?

### Chapter 3 · Modern CSS and HTML for interaction (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 `:has()` and state selectors | Parent and sibling selection (widely available June 2026), `:focus-visible`, `:user-invalid`, styling by ARIA state | Style a form group's error state from its input's validity with no JavaScript |
| 3.2 Native overlays | `<dialog>` (`showModal`, `inert` background), popover (Baseline January 2025), invoker commands (Baseline December 2025); `closedby` and `popover="hint"` are still in Interop 2026 | Build modal, menu and toast with native elements; list what you no longer need from JavaScript |
| 3.3 Anchor positioning | Tethering tooltips and menus to anchors; not Baseline as of October 2026, so ship with a fallback | Anchored tooltip with a JavaScript fallback selected by `@supports` |
| 3.4 Transitions on entry and exit | `@starting-style`, `transition-behavior: allow-discrete`, same-document view transitions (Baseline October 2025); cross-document view transitions are in Interop 2026 | Animate dialog open and close, respecting `prefers-reduced-motion` |

**Check your understanding:** What does `showModal()` give you for accessibility that a styled `div` does not? How do you ship a non-Baseline feature without breaking users on older browsers? Why must an exit animation never delay focus return?

### Chapter 4 · Colour, typography and theming (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Colour spaces | OKLCH and why perceptual lightness helps palettes; `color-mix()`, relative colour syntax | Generate a 10-step palette in OKLCH; compare with an HSL palette for even lightness |
| 4.2 Contrast | WCAG 2 contrast ratios (4.5:1 text, 3:1 UI components and large text), `contrast-color()` (Baseline April 2026), APCA in the WCAG 3 drafts and why WCAG 2 still governs conformance | Automate contrast checks for every token pair; fix failures |
| 4.3 Themes | `prefers-color-scheme`, `light-dark()`, user-chosen themes, forced-colours mode (Windows High Contrast) | Ship light, dark and high-contrast themes; test in forced-colours emulation |
| 4.4 Typography | Fluid type with `clamp()`, variable fonts, line length, vertical rhythm; Devanagari and other Indic scripts need more line height for matras and conjuncts | Set a type scale that renders English and Hindi body text without clipping |
| 4.5 Web fonts | Noto families, subsetting by script, `font-display`, fallback metric overrides (`size-adjust`) to avoid layout shift | Cut Hindi font weight by subsetting; measure CLS before and after |

**Check your understanding:** Why can two colours with the same HSL lightness look different in brightness? Why is dark mode not just "invert the palette"? What does forced-colours mode remove, and how do you keep focus indicators visible in it?

### Chapter 5 · Design tokens (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Token taxonomy | Primitive, semantic and component tokens; aliasing; naming that survives a rebrand | Classify 80 values from a real stylesheet into three tiers |
| 5.2 The DTCG format | The Design Tokens Community Group format: `$value`, `$type`, aliases, groups, composite types | Write a token file that validates against the format |
| 5.3 Pipelines | Style Dictionary 5 and Tokens Studio transforms to CSS variables, Android XML and iOS Swift; Figma variables as a source | One `npm run tokens` builds web, Android and iOS outputs |
| 5.4 Theming with tokens | Multi-brand and mode switching through semantic aliases; density and font-scale modes | Two brands × light/dark × compact/comfortable from one source |

**Check your understanding:** Why should components consume semantic tokens rather than primitives? What breaks when design and code each keep their own copy of tokens? How do you version a token rename without breaking 30 apps?

### Chapter 6 · Component-library engineering (weeks 6–7)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Headless and styled layers | React Aria Components, Base UI and Radix provide behaviour; your layer adds tokens and styles; the shadcn/ui copy-in model | Build `Select` and `Dialog` on a headless library with your tokens |
| 6.2 Component API contracts | Props vs slots, variants, polymorphism (`asChild`), controlled state, forwarding refs and attributes | Write an API review for 5 components using a checklist |
| 6.3 Documentation as product | Storybook 10 stories, usage guidance, do/don't, accessibility notes per component | Document 8 components so a new engineer can use them without asking |
| 6.4 Versioning and change | Semantic versioning for visual changes, deprecation warnings, codemods, release notes | Ship a breaking prop rename with a codemod and a deprecation period |
| 6.5 Real systems | Public design systems: GOV.UK Design System, India's UX4G (NeGD), GitHub Primer, IBM Carbon, Atlassian | Compare how three of them document a text input and its errors |

**Check your understanding:** Why do mature design systems separate behaviour from appearance? What makes a visual change "breaking"? What does copy-in distribution (shadcn/ui) trade away compared with a versioned package?

### Chapter 7 · WCAG 2.2 AA in practice (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Conformance | Principles, success criteria, levels; what "AA conformance" claims; WCAG 2.2's additions (Focus Not Obscured, Dragging Movements, Target Size 24×24, Consistent Help, Redundant Entry, Accessible Authentication) and removal of 4.1.1 Parsing | Map each 2.2 AA criterion to the components it affects |
| 7.2 Names, roles, states | The accessible name computation (AccName 1.2), WAI-ARIA 1.2 roles and states, the first rule of ARIA | Compute accessible names for 15 tricky elements by hand; check in DevTools' accessibility tree |
| 7.3 Keyboard and focus | Focus order, roving `tabindex`, `aria-activedescendant`, focus trapping vs `inert`, focus return, skip links | Build an APG-conformant menu button and listbox |
| 7.4 Dynamic content | Live regions (polite vs assertive), status messages (4.1.3), loading states, route changes in SPAs | Announce search result counts without double announcements |
| 7.5 Forms and authentication | Labels, instructions, error identification and suggestion; OTP fields that allow paste and autofill (`autocomplete="one-time-code"`) | Make a login with OTP pass 3.3.8 Accessible Authentication |

**Check your understanding:** Why did WebAIM find more errors on pages using ARIA? When is `aria-activedescendant` better than moving DOM focus? Which 2.2 criterion does a sticky header most often fail, and how do you fix it?

### Chapter 8 · Assistive-technology testing and audits (weeks 9–10)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Screen readers | NVDA with Chrome or Firefox, VoiceOver on macOS and iOS, TalkBack on Android (93.9% of India's mobile OS share in September 2026); browse vs focus modes; rotor and headings navigation | Complete the same purchase on all three; log differences |
| 8.2 Beyond screen readers | Voice control, switch access, magnification, 200% Android font scale, reduced motion, cognitive load | Use your app at 200% system font size on an Android phone; fix every truncation |
| 8.3 Automated testing | axe-core (finds on average 57% of issues, per Deque), Lighthouse, ACT rules; running axe in Storybook and Playwright | Add axe gates to CI; triage false positives |
| 8.4 Manual audits | WCAG-EM sampling, test scripts, severity, reproducible issue reports | Audit 10 pages of a public website by normal browsing; write findings |
| 8.5 Reporting | Accessibility Conformance Reports (ITI's VPAT template), remediation plans, retesting | Write an ACR for your P2 component set |

**Check your understanding:** Why can a page pass every automated check and still be unusable with a screen reader? Why test with TalkBack specifically for Indian users? What makes an accessibility bug report actionable for a developer who has never used a screen reader?

### Chapter 9 · Law, policy and procurement (week 11)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 India's legal framework | RPwD Act 2016 (accessibility standards and access to ICT); RPwD (Amendment) Rules 2023 notifying BIS ICT accessibility standards (IS 17802); *Rajive Raturi* (Nov 2024) on mandatory rules; *Pragya Prasun* (Apr 2025) on accessible digital KYC | Summarise what a private fintech app must do, with citations |
| 9.2 Sector rules | GIGW 3.0 for government; SEBI's 31 July 2025 circular (IS 17802, WCAG 2.1, GIGW 3.0, IAAP-certified auditors, annual audits); UX4G inheriting GIGW 3.0 | Build a compliance checklist for a SEBI-regulated broker's web app |
| 9.3 Global obligations | European Accessibility Act (applies from 28 June 2025, EN 301 549); US Section 508 and ADA litigation as context | Compare obligations for an Indian SaaS selling into the EU |
| 9.4 Engineering for compliance | Accessibility in definition of done, design reviews, procurement of third-party widgets, evidence trails | Write an accessibility policy for a 50-person product team |

**Check your understanding:** What does the *Pragya Prasun* judgement change for a company running video KYC? Why does a SEBI-regulated broker need evidence, not just intent? Why is a third-party chat widget an accessibility liability?

### Chapter 10 · Inclusive design for India (week 12)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Multilingual interfaces | `lang` on mixed Hindi/English content, script-aware fonts, text expansion, numerals and `Intl` formats (`en-IN`, `hi-IN`) | Localise one flow into Hindi and Tamil; fix overflow and line-breaking |
| 10.2 Low literacy and first-time users | Icon plus text, plain language, voice input options, forgiving inputs | Rewrite an onboarding flow for a first-time smartphone user; test with 3 people |
| 10.3 Low-end devices | Large font scales, small screens (360 px wide), high-glare outdoor use, contrast beyond the minimum | Test on a low-cost Android phone outdoors; record and fix issues |
| 10.4 Government design patterns | UX4G components and patterns, GIGW requirements as engineering tasks | Rebuild a form using UX4G guidance; compare with your own system |

**Check your understanding:** Why is a translated string not a localised interface? What would you change for a user who reads Hindi slowly and uses a phone at 200% font scale? When is a contrast ratio above 4.5:1 worth the design trade-off?

### Chapter 11 · Governance, AI generation and quality gates (weeks 13–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Design-system governance | Central vs federated teams, contribution process, adoption metrics, accessibility sign-off per component | Write a contribution guide with an accessibility acceptance checklist |
| 11.2 Visual and accessibility regression | Screenshot tests per story, axe per story, Stylelint rules for tokens (no raw colours) | Block a raw hex colour and a contrast regression in CI |
| 11.3 Generating against your system | Design-to-code with the Figma MCP server, v0 with a custom component registry, agents told to use your tokens | Generate 5 screens with AI using only your library; measure how many raw values leak in |
| 11.4 Auditing generated UI | Checklist: semantics, names, focus, contrast, reflow, live regions, motion | Audit and fix 3 generated screens; record each failure class |

**Check your understanding:** What stops a design system from rotting after its first year? How do you make AI tools use your components instead of inventing new ones? Which accessibility checks can CI enforce, and which need a human every release?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Layers refactor | Zero `!important` |
| 2 | 2 | Lab 2 · Intrinsic layouts | 320–1920 px, RTL, 400% zoom |
| 3 | 3 | Lab 3 · Native overlays | Dialog, menu, tooltip with fallback; **P1 starts** |
| 4 | 4 | Lab 4 · Colour and type | OKLCH palette, contrast automation |
| 5 | 5 | Lab 5 · Token pipeline | Web, Android, iOS outputs; **P1 due** |
| 6 | 6 | Lab 6 · Headless components | `Select`, `Dialog` |
| 7 | 6 | Lab 6 (cont.) | Codemod and deprecation |
| 8 | 7 | Lab 7 · APG patterns (no AI) | Menu button, listbox; mid-term (AI off) |
| 9 | 8 | Lab 8 · Three screen readers | Test logs; **P2 due** |
| 10 | 8 | Lab 9 · WCAG-EM audit | Audit report and ACR |
| 11 | 9 | Policy brief | Compliance checklist |
| 12 | 10 | Lab 10 · Indic and low-end | Localised flow; **P3 starts** |
| 13 | 11 | Quality gates | CI with visual and axe gates |
| 14 | 11 | Generated-UI audit | **P3 due** |
| 15 | Review | P3 demo with live screen-reader walkthrough | Final exam (AI off) |

## Working with AI in this course

- **Use AI for:** generating layout variants; converting designs to first-draft CSS; writing token transforms; drafting alt text and ACR prose, which you then correct; explaining an unfamiliar WCAG criterion after you have read the Understanding document.
- **Do without AI (drills):** the APG pattern lab; computing accessible names by hand; every screen-reader test; the mid-term (predict the cascade, fix an inaccessible component on paper) and the final.
- **Verify AI output by:** axe-core and Lighthouse; a keyboard-only pass; NVDA plus TalkBack scripts; the DevTools accessibility tree; contrast automation over token pairs; checking every CSS feature's Baseline status rather than trusting the model.
- **Where AI still fails here:** WebAIM's numbers describe the training data. Generated UI commonly ships missing labels, ARIA that contradicts native semantics, focus traps without escape, colour-only states and fixed heights that clip Hindi text. Log every instance you find in Lab 11.4 and P3. That log is graded.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (10) | 25% |
| Projects P1 · P2 · P3 | 10% · 15% · 20% |
| Mid-term (AI off) | 10% |
| Final (AI off, 3 h) with live screen-reader demonstration | 20% |

**Mastery gate.** You pass when you can, with AI off, in 3 hours, take a provided inaccessible page with a modal, a menu, a form and a data table and make it conform to WCAG 2.2 AA. Evidence: zero axe violations; NVDA and TalkBack test scripts passed live in front of an examiner; reflow at 400% zoom; correct forced-colours rendering; no `!important` in your CSS. You must also explain each fix by citing the success criterion.

## Industry reality

Design-systems engineer and accessibility engineer are named specialisms on the [FE market page](../../../../06_career_and_market_readiness/01_market_map/roles/FE_frontend_engineering.md), and accessibility is listed there as growing in value because generated markup often fails keyboard and screen-reader use. Public design systems (GOV.UK, UX4G, Primer, Carbon) show the standard of documentation employers expect. In India, SEBI's 2025 circular created demand for audits by IAAP-certified professionals across brokers, exchanges and mutual funds, according to Deque's summary of the circular. Accessibility knowledge is therefore a hiring signal in fintech, not only in government work.

**Interview questions from this course**

1. *How would you structure CSS for a 200-screen app shared by 8 teams?* A strong answer uses cascade layers for order, tokens through custom properties, scoped or module-based component styles, and a policy on utilities. It covers lint rules against raw values and how third-party CSS is contained.
2. *Make this modal accessible.* A strong answer uses `<dialog>` with `showModal()` or an APG-conformant equivalent: labelled by its heading, `inert` background, Escape to close, focus moved in and returned on close, no scroll bleed, and reduced-motion handling. It tests with a screen reader.
3. *Media queries or container queries for a product card?* A strong answer chooses container queries because the card's slot, not the viewport, determines its space. It explains containment and container units and keeps media queries for page-level layout and user preferences.
4. *Design a token system for two brands with dark mode.* A strong answer describes primitive, semantic and component tiers, aliasing per brand and mode, the DTCG format and pipelines to each platform. It covers contrast checks per combination and versioning of renames.
5. *What can automated accessibility testing not catch?* A strong answer cites axe's own estimate of about 57% coverage. It lists meaningful alt text, logical focus order, understandable error messages, screen-reader announcement quality and cognitive load, and describes a manual test plan with NVDA and TalkBack.

## Resources (free first)

- **CSS:** [web.dev Learn CSS](https://web.dev/learn/css); [MDN container queries](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_containment/Container_queries); [MDN View Transition API](https://developer.mozilla.org/en-US/docs/Web/API/View_Transition_API); [Chrome CSS and UI docs](https://developer.chrome.com/docs/css-ui), including [anchor positioning](https://developer.chrome.com/docs/css-ui/anchor-positioning-api); [Every Layout](https://every-layout.dev/) (partly free); [Modern CSS Solutions](https://moderncss.dev/); [CSS Color 5](https://www.w3.org/TR/css-color-5/).
- **Design systems:** [Design Tokens format](https://tr.designtokens.org/format/); [Style Dictionary](https://styledictionary.com/); [GOV.UK Design System](https://design-system.service.gov.uk/); [UX4G](https://www.ux4g.gov.in/); [Primer](https://primer.style/); [Carbon](https://carbondesignsystem.com/); [Atlassian Design](https://atlassian.design/); [Storybook accessibility testing](https://storybook.js.org/docs/writing-tests/accessibility-testing).
- **Accessibility:** [WCAG 2.2](https://www.w3.org/TR/WCAG22/) and [Understanding WCAG 2.2](https://www.w3.org/WAI/WCAG22/Understanding/); [WAI-ARIA 1.2](https://www.w3.org/TR/wai-aria-1.2/); [AccName 1.2](https://www.w3.org/TR/accname-1.2/); [ARIA Authoring Practices](https://www.w3.org/WAI/ARIA/apg/); [WCAG-EM](https://www.w3.org/WAI/test-evaluate/conformance/wcag-em/); [ACT rules](https://act-rules.github.io/); [Inclusive Components](https://inclusive-components.design/); [The A11Y Project](https://www.a11yproject.com/); [WebAIM screen reader guide](https://webaim.org/techniques/screenreader/); [NVDA](https://www.nvaccess.org/download/); [axe-core](https://github.com/dequelabs/axe-core); [VPAT template (ITI)](https://www.itic.org/policy/accessibility/vpat).
- **India and global law:** [GIGW 3.0](https://guidelines.india.gov.in/); [DEPwD acts and rules](https://depwd.gov.in/acts/) (RPwD Act 2016, Rules 2017, 2023 ICT standards amendment); [European Accessibility Act](https://commission.europa.eu/strategy-and-policy/policies/justice-and-fundamental-rights/disability/union-equality-strategy-rights-persons-disabilities-2021-2030/european-accessibility-act_en).
- **Certification (optional):** [IAAP certifications](https://www.accessibilityassociation.org/s/certification) (CPACC, WAS). Paid; useful mainly for audit roles.

## Sources

All checked 12 Oct 2026.

- WebAIM Million 2026 (Feb 2026 data) — https://webaim.org/projects/million/
- DEPwD, Acts and Rules page (RPwD Act 2016; RPwD Rules 2017; RPwD (Amendment) Rules 2023, accessibility standards on ICT products and services) — https://depwd.gov.in/acts/
- Deque, "SEBI sets a new standard for digital accessibility in finance in India" (summary of SEBI circular of 31 Jul 2025 and revision of 29 Aug 2025; vendor summary, check the circular text) — https://www.deque.com/blog/sebi-sets-a-new-standard-for-digital-accessibility-in-finance-in-india/
- *Rajive Raturi v. Union of India* (8 Nov 2024) and *Pragya Prasun v. Union of India*, 2025 INSC 599 (30 Apr 2025): judgement links in [FND114 sources](../../../../01_year_1_foundations/semester_2/FND114_web_foundations_http_html_css_and_javascript/README.md#sources)
- GIGW 3.0 — https://guidelines.india.gov.in/ · UX4G (NeGD, MeitY; Design System 3.0; inherits GIGW 3.0) — https://www.ux4g.gov.in/
- European Commission, European Accessibility Act — https://commission.europa.eu/strategy-and-policy/policies/justice-and-fundamental-rights/disability/union-equality-strategy-rights-persons-disabilities-2021-2030/european-accessibility-act_en
- web-features 3.42.0 Baseline data (container queries widely available Aug 2025; `:has()` Jun 2026; subgrid Mar 2026; `@scope` Mar 2026; container style queries May 2026; popover Jan 2025; invoker commands Dec 2025; `contrast-color()` Apr 2026; `field-sizing` Jun 2026; anchor positioning, scroll-driven animations, `closedby` not Baseline) — https://web-platform-dx.github.io/web-features/
- web.dev, "Same-document view transitions are now Baseline Newly available" (16 Oct 2025) — https://web.dev/blog/same-document-view-transitions-are-now-baseline-newly-available
- Mozilla Hacks, "Launching Interop 2026" (Feb 2026) — https://hacks.mozilla.org/2026/02/launching-interop-2026/
- StatCounter, mobile OS market share India, Sep 2026 (Android 93.89%) — https://gs.statcounter.com/os-market-share/mobile/india
- axe-core (average 57% of WCAG issues found automatically) — https://github.com/dequelabs/axe-core
- Figma, Guide to the Figma MCP server — https://help.figma.com/hc/en-us/articles/32132100833559

_Last reviewed: 2026-10_
