# Frontend Engineering (FE) · Learning path

| Code | Entry requirements | Major courses | Levels | Market page |
|---|---|---|---|---|
| FE | [FND114](../../01_year_1_foundations/semester_2/FND114_web_foundations_http_html_css_and_javascript/README.md), [CS205](../../02_year_2_core_computer_science/semester_3/CS205_software_engineering_i_design_testing/README.md) | FE301–FE305, FE401–FE404, FE501 | L0 → L5 over five years | [FE roles and market](../../06_career_and_market_readiness/01_market_map/roles/FE_frontend_engineering.md) |

Frontend engineers build the part of software that people see, touch, hear and trust: the interface in the browser, and increasingly the server code that renders it and the AI features inside it. This major takes you from your first web page to designing interfaces used by millions on low-cost phones, in many languages, with AI agents inside and outside the page.

## 1. Who this major is for and where it leads

It suits you if you care how things feel to use, like seeing your work immediately, and are willing to be precise about details others ignore: a 100 ms delay, a missing label, a layout that breaks in Tamil.

| Role | What people in it actually do |
|---|---|
| Frontend engineer / UI engineer (SDE-1 frontend in many Indian companies) | Turn designs into accessible, responsive components; manage state and data fetching; handle loading, error and empty states; write tests |
| Full-stack / product engineer | Own a feature end to end in a framework such as Next.js: rendering, data access, authentication, deployment |
| Design engineer | Work between design and code: prototypes, motion, interaction quality, design-system components |
| Design-systems engineer | Build and govern the shared components, tokens and documentation many teams depend on |
| Accessibility engineer | Make products usable with screen readers, keyboards and other assistive technology; audit and write conformance reports |
| Web performance engineer | Measure and fix loading and responsiveness on real devices and networks; set and enforce budgets |
| Creative developer | Animation, WebGL and WebGPU graphics, 3D and data visualisation |
| AI interface engineer | Streaming answers, generative UI, agent consoles with approvals and undo, on-device AI features |
| Staff / principal frontend engineer, frontend architect | Set technical direction across teams: architecture, platform, standards, hiring bar |

Seniority titles and the day-to-day work are described, with sources, on the [FE market page](../../06_career_and_market_readiness/01_market_map/roles/FE_frontend_engineering.md). In the US, the BLS projects web developers and digital designers to grow 5% from 2025 to 2035, while noting that AI "may soften" growth; many frontend engineers are counted as software developers instead (+10%). In India, Payscale's self-reported data puts front-end developer average base pay at ₹6.6 lakh against ₹4.2 lakh for "web developer". That gap is a skills signal, not a guarantee (figures from the market page, checked October 2026).

## 2. How AI is changing frontend work

**What the evidence says (checked October 2026):**

- **Frontend is among the most AI-exposed engineering work.** In Anthropic's analysis of Claude Code use, JavaScript/TypeScript made up 31% of queries and HTML/CSS 28%. "UI/UX Component Development" was 12% of conversations. Anthropic wrote that "jobs that center on making simple applications and user interfaces may face disruption from AI systems sooner" ([Anthropic, Apr 2025](https://www.anthropic.com/research/impact-software-development)).
- **AI tools are standard equipment, and trust is conditional.** 65.9% of developers use AI coding assistants or agents at work, but 48.0% trust AI output only when they can easily verify it ([Stack Overflow 2026](https://survey.stackoverflow.co/2026/ai/data)).
- **Whole-app and design-to-code generation is routine.** UI generators such as v0, Lovable and Bolt produce working apps from prompts. Figma's MCP server lets coding agents read design context and generate code from frames ([Figma](https://help.figma.com/hc/en-us/articles/32132100833559)). Generated interfaces were preferred over plain text answers and matched expert-built interfaces in about half of cases in one 2026 study ([Leviathan et al.](https://arxiv.org/abs/2604.09577)).
- **Agents now test and debug UI.** The Chrome DevTools MCP server lets agents record performance traces and inspect pages ([Chrome, Sep 2025](https://developer.chrome.com/blog/chrome-devtools-mcp)), and Playwright ships planner, generator and healer test agents ([Playwright](https://playwright.dev/docs/test-agents)).
- **Generated code inherits the web's flaws.** 95.9% of the top million home pages have detectable WCAG failures ([WebAIM Million 2026](https://webaim.org/projects/million/)). In Veracode's 2025 study, 45% of AI-generated code samples introduced OWASP Top 10 flaws ([Veracode](https://www.veracode.com/blog/genai-code-security-report/)). Multi-turn edits of generated UI are fragile: the best of eight models completed only 37.3% of five-turn tasks ([EvoGenUI-Bench, 2026](https://arxiv.org/abs/2608.29387)).

**Being automated or mostly automated:** scaffolding components from descriptions or screenshots, CSS layout, form boilerplate, simple landing pages and admin dashboards, converting between frameworks.

**Augmented (AI helps, you decide):** refactoring state management, writing tests, framework migrations, debugging rendering and performance issues.

**Growing in value** (from the [market page](../../06_career_and_market_readiness/01_market_map/roles/FE_frontend_engineering.md)):
- accessibility to WCAG 2.2, now backed by Indian law and regulation;
- performance on low-end Android phones and slow networks;
- design-system and component architecture;
- AI-native interfaces (streaming, sources, recovery, approval of agent actions);
- product and UX judgement.

**Analysis.** Building a screen is becoming cheap; building the right screen, which works for everyone and stays fast and maintainable, is not. This major therefore spends its time on what generators get wrong and on judgement that cannot be generated. Every course has AI-off drills and a log of verified AI failures.

## 3. The five-year path

Courses in **bold** matter most for this major. Paths and prerequisites come from [`catalog.json`](../../catalog.json).

| Year · Semester | Courses | Why they matter for frontend |
|---|---|---|
| 1 · 1 | FND101, FND102, FND103, **[FND104](../../01_year_1_foundations/semester_1/FND104_the_developers_toolkit_linux_shell_git/README.md)**, **[FND105](../../01_year_1_foundations/semester_1/FND105_ai_native_learning_and_building/README.md)**, FND106 | Git, shell and AI-native working habits from day one |
| 1 · 2 | **[FND111](../../01_year_1_foundations/semester_2/FND111_programming_ii_object_oriented_and_typed/README.md)**, FND112, FND113, **[FND114](../../01_year_1_foundations/semester_2/FND114_web_foundations_http_html_css_and_javascript/README.md)**, FND115, FND116 | TypeScript and the web platform (FND114 is the entry course); linear algebra for graphics (FND113) |
| 2 · 3 | [CS201](../../02_year_2_core_computer_science/semester_3/CS201_algorithms_and_complexity/README.md), CS202, CS203, **[CS204](../../02_year_2_core_computer_science/semester_3/CS204_computer_networks/README.md)**, **[CS205](../../02_year_2_core_computer_science/semester_3/CS205_software_engineering_i_design_testing/README.md)**, CS206 | Networks underpin web performance; software engineering is the second entry course; DSA rounds still appear in Indian product-company loops |
| 2 · 4 | CS211, [CS212](../../02_year_2_core_computer_science/semester_4/CS212_distributed_systems_i/README.md), **[CS213](../../02_year_2_core_computer_science/semester_4/CS213_security_foundations/README.md)**, CS214, CS215, **[CS216](../../02_year_2_core_computer_science/semester_4/CS216_programming_languages_compilers_and_interpreters/README.md)** | Security for XSS, CSP and auth; compilers for bundlers and TypeScript; distributed systems for sync and collaboration |
| 3 · 5 | **[FE301](year_3/FE301_modern_javascript_and_typescript_in_depth/README.md)** JavaScript and TypeScript in depth · **[FE302](year_3/FE302_react_and_component_architecture/README.md)** React and component architecture · **[FE303](year_3/FE303_css_design_systems_and_accessibility/README.md)** CSS, design systems and accessibility · [PRO301](../../05_shared_years_3_to_5/PRO301_professional_practice_ethics_law_and_responsible/README.md) professional practice | The language, the component model and the visual and accessible layer, taken together |
| 3 · 6 | **[FE304](year_3/FE304_browser_internals_and_web_performance/README.md)** browser internals and performance · **[FE305](year_3/FE305_frontend_testing_and_tooling/README.md)** testing and tooling · [CAR301](../../05_shared_years_3_to_5/CAR301_career_lab_i_dsa_mastery_portfolio_and_open/README.md) Career Lab I · one elective | Speed on real devices; quality pipelines; DSA, portfolio and open source |
| 4 · 7 | **[FE401](year_4/FE401_full_stack_frameworks_rendering_data_fetching/README.md)** full-stack frameworks · **[FE402](year_4/FE402_advanced_ui_animation_graphics_webgl_and_webgpu/README.md)** animation, graphics, WebGL and WebGPU · [IND401](../../05_shared_years_3_to_5/IND401_industry_co_op_studio/README.md) industry co-op studio · overlap course A | Own the server side of the UI; craft and graphics; real team work |
| 4 · 8 | **[FE403](year_4/FE403_ai_native_interfaces_streaming_generative_ui/README.md)** AI-native interfaces · **[FE404](year_4/FE404_frontend_system_design_at_scale/README.md)** frontend system design at scale · [CAR401](../../05_shared_years_3_to_5/CAR401_career_lab_ii_interviews_system_design_and_ai/README.md) Career Lab II · overlap course B | The newest interface layer and the senior design skill; interview preparation |
| 5 · 9 | **[FE501](year_5/FE501_frontier_seminar_multimodal_spatial_and_on/README.md)** frontier seminar · [RES501](../../05_shared_years_3_to_5/RES501_research_methods_and_scientific_writing/README.md) research methods · [RES502](../../05_shared_years_3_to_5/RES502_reading_reproducing_and_extending_papers/README.md) reproducing papers · [THS501](../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md) thesis or capstone I | On-device AI, agentic web, spatial and local-first interfaces; research skills |
| 5 · 10 | [THS502](../../05_shared_years_3_to_5/THS502_thesis_or_capstone_ii/README.md) thesis or capstone II · [LCH502](../../05_shared_years_3_to_5/LCH502_career_launch_and_founder_studio/README.md) career launch and founder studio · electives | Ship the capstone; launch a career or a product |

Each course has its own labs and three projects in its `projects.md`. FE301 to FE303 run in parallel and reference each other, as do FE304 and FE305.

## 4. Skill map by level

| Level | You can… | Where you get it |
|---|---|---|
| L0 · Absolute beginner | Follow a tutorial to build and publish a static page | FND114 (early weeks) |
| L1 · Foundations | Write semantic, responsive, accessible pages and plain JavaScript that calls APIs; explain what happens when a URL loads | FND114, FND111 |
| L2 · Practitioner (intern-ready) | Build a small app with a framework, handle async data and errors, pass an accessibility audit, and debug with DevTools | FND114 mastery gate, CS205, start of FE301–FE303 |
| L3 · Professional (job-ready) | Ship production features in a team with TypeScript, tests, CI, performance budgets and WCAG 2.2 AA; pass a machine-coding round; make server–client and caching decisions | FE301–FE305 mastery gates, FE401 |
| L4 · Expert (hard to replace) | Design frontend systems for millions of users and dozens of teams: collaboration, offline-first, design-system governance, i18n for Indic scripts and RTL, AI agent interfaces with safety controls; lead reviews | FE401–FE404, IND401, CAR401 |
| L5 · Research and frontier | Reproduce and extend published work on interfaces (on-device AI, generative UI, local-first, XR), contribute to web standards and open source, publish | FE501, RES501/502, THS501/502 |

## 5. Recommended overlaps and electives

**Overlaps** (Years 4–5):

- **[OV08 Full-Stack AI Product Engineering](../../04_overlaps/OV08_full_stack_ai_product_engineering/README.md)** is the natural overlap for this major. It combines FE403 with [BE403](../backend_engineering/year_4/BE403_backends_for_ai_serving_llm_features_vector/README.md) (backends for AI) and [AIE404](../ai_engineering/year_4/AIE404_ai_product_engineering_and_ux/README.md) (AI product engineering and UX). Its two courses, OV08A and OV08B, cover shipping AI features end to end and product analytics. Plan to take BE403 and AIE404 as electives so you meet its prerequisites.
- **[OV02 Cloud-Native Backend](../../04_overlaps/OV02_cloud_native_backend/README.md)** suits students heading towards full-stack or platform roles. It builds on [BE301](../backend_engineering/year_3/BE301_api_design_rest_grpc_and_graphql/README.md), BE304 and CLD303, so take BE301 as a Year 3 elective.

**Electives that pair well:**

| Elective | Why |
|---|---|
| [BE301 API Design](../backend_engineering/year_3/BE301_api_design_rest_grpc_and_graphql/README.md) | Design the APIs your UI consumes; needed for OV02 |
| [SWE304 AI-Assisted Software Engineering](../software_engineering/year_3/SWE304_ai_assisted_software_engineering_agents/README.md) | Agents in the development lifecycle, at depth |
| [SWE301 Software Architecture](../software_engineering/year_3/SWE301_software_architecture_and_design_patterns/README.md) | Architecture patterns behind FE404 |
| [MOB303 Flutter and React Native](../mobile_engineering/year_3/MOB303_cross_platform_apps_flutter_and_react_native/README.md) | The shortest step from React to mobile |
| [QAE302 Test Automation](../software_quality_test_engineering/year_3/QAE302_test_automation_engineering_ui_and_api/README.md) and [QAE305 Mobile and Cross-Browser Testing](../software_quality_test_engineering/year_3/QAE305_mobile_and_cross_browser_testing/README.md) | Deeper UI automation and device coverage |
| [OFF302 Web Application Security Testing](../ethical_hacking_offensive_security/year_3/OFF302_web_application_security_testing/README.md) | See your own code from the authorised tester's side |
| [AIE404 AI Product Engineering and UX](../ai_engineering/year_4/AIE404_ai_product_engineering_and_ux/README.md) and [BE403 Backends for AI](../backend_engineering/year_4/BE403_backends_for_ai_serving_llm_features_vector/README.md) | Prerequisites for OV08 |

## 6. Flagship industry project

The major's flagship project, specified in [`06_career_and_market_readiness/05_industry_projects/FE_frontend_engineering.md`](../../06_career_and_market_readiness/05_industry_projects/FE_frontend_engineering.md), is built during IND401 and Year 5. It combines the course capstones into one product that real users can use: a fast, accessible, multilingual web app with an AI feature that has proper streaming, approvals and evaluation. Strong course projects to build towards it are FE302 P3 (real-time watchlist), FE303 P3 (design system), FE304 P3 (lite PWA), FE403 P3 (multilingual assistant) and FE404 P3 (collaborative editor).

## 7. Certifications (optional, honest value)

No certification is required for frontend jobs, and none replaces a portfolio of shipped, measured work.

- **IAAP CPACC and WAS** ([IAAP](https://www.accessibilityassociation.org/s/certification)) are the most useful. Accessibility audits are a growing service line, and SEBI's 2025 circular asks regulated entities to use IAAP-certified auditors, according to [Deque's summary](https://www.deque.com/blog/sebi-sets-a-new-standard-for-digital-accessibility-in-finance-in-india/). They are paid and worth it mainly if you want audit or accessibility-specialist roles.
- **Vendor or course certificates** (for example the [Meta Front-End Developer certificate](https://www.coursera.org/professional-certificates/meta-front-end-developer) on Coursera, or framework certificates such as [certificates.dev](https://certificates.dev/)) can structure beginner study. They carry little weight with employers once you have real projects; treat them as optional.
- **Cloud certificates** help only if you move towards full-stack or platform work (see the CLD and OPS majors).

## 8. The interview loop

The typical loop, described with sources on the [FE market page](../../06_career_and_market_readiness/01_market_map/roles/FE_frontend_engineering.md), varies by company:

1. **JavaScript and TypeScript fundamentals:** closures, the event loop, promises, types; often implementing `debounce`, `Promise.all` or a custom `Promise` (FE301).
2. **Machine coding:** building a component or small app live, such as an autocomplete, modal, infinite list or task board, often in a browser editor. Interviewers watch accessibility, state handling and edge cases (FE302, FE303). Indian product companies commonly run this round; one self-reported senior frontend loop (September 2025) had machine coding, DSA, JavaScript, product design and hiring-manager rounds ([candidate report](https://www.jointaro.com/interviews/companies/flipkart/experiences/senior-frontend-engineer-india-september-16-2025-declined-offer-positive-f89c4ee4/)).
3. **Frontend system design:** a news feed, collaborative editor, design system or offline app, covering rendering, caching, performance budgets, accessibility and i18n (FE404).
4. **DSA:** sometimes, especially at product companies in India ([CS201](../../02_year_2_core_computer_science/semester_3/CS201_algorithms_and_complexity/README.md), [CAR301](../../05_shared_years_3_to_5/CAR301_career_lab_i_dsa_mastery_portfolio_and_open/README.md)).
5. **Behavioural and product:** often with a designer or product manager.

AI rules differ. Canva expects frontend candidates to use AI in its coding interview and evaluates whether they can find and fix issues in AI-generated code; other firms forbid AI in live rounds. Prepare for both through [AI-driven interviews](../../06_career_and_market_readiness/04_ai_driven_interviews/) and [CAR401](../../05_shared_years_3_to_5/CAR401_career_lab_ii_interviews_system_design_and_ai/README.md).

## 9. Fast track for working professionals

Assume 10–15 hours a week. Use each course's mastery gate as a placement test: if you pass it, skip the course.

| You are… | Take, in order | Roughly |
|---|---|---|
| A backend or full-stack developer new to modern frontend | FND114 mastery gate (or the course) → FE301 → FE302 → FE303 → FE304 → FE401 | 9–12 months |
| A frontend developer aiming for senior | FE301 (gate check) → FE304 → FE305 → FE404 → FE403 | 6–9 months |
| A designer moving to design engineering | FND114 → FE303 → FE302 → FE402 | 8–10 months |
| A QA engineer moving to frontend | FE305 (gate check) → FE301 → FE302 → FE303 | 6–8 months |
| Any of the above targeting AI interface roles | FE302 → FE303 → FE403, plus AIE404 | 5–7 months |

In parallel, rebuild one existing product screen at work (with permission) to WCAG 2.2 AA and the FE304 performance budget, with before/after evidence. Concrete improvements like that convince hiring managers more than course completions.

## Sources

All checked 12 Oct 2026. Market figures are reused from the [FE market page](../../06_career_and_market_readiness/01_market_map/roles/FE_frontend_engineering.md), which lists its own sources (BLS, Payscale, WEF, Octoverse, HackerRank, NASSCOM, Canva).

- Anthropic, "AI's impact on software development" (28 Apr 2025) — https://www.anthropic.com/research/impact-software-development
- Stack Overflow, 2026 Developer Survey, AI section — https://survey.stackoverflow.co/2026/ai/data
- Figma, Guide to the Figma MCP server — https://help.figma.com/hc/en-us/articles/32132100833559
- Chrome for Developers, "Chrome DevTools (MCP) for your AI agent" (23 Sep 2025) — https://developer.chrome.com/blog/chrome-devtools-mcp
- Playwright, test agents — https://playwright.dev/docs/test-agents
- Leviathan et al., "Generative UI: LLMs are Effective UI Generators" (arXiv 2604.09577, Feb 2026) — https://arxiv.org/abs/2604.09577
- Peng et al., "EvoGenUI-Bench" (arXiv 2608.29387, Aug 2026) — https://arxiv.org/abs/2608.29387
- WebAIM Million 2026 — https://webaim.org/projects/million/
- Veracode, 2025 GenAI Code Security Report — https://www.veracode.com/blog/genai-code-security-report/
- Deque, summary of SEBI's 31 Jul 2025 accessibility circular — https://www.deque.com/blog/sebi-sets-a-new-standard-for-digital-accessibility-in-finance-in-india/
- Candidate interview report (self-reported, Sep 2025) — https://www.jointaro.com/interviews/companies/flipkart/experiences/senior-frontend-engineer-india-september-16-2025-declined-offer-positive-f89c4ee4/
- Canva Engineering, "Yes, you can use AI in our interviews" (11 Jun 2025) — https://www.canva.dev/blog/engineering/yes-you-can-use-ai-in-our-interviews/

_Last reviewed: 2026-10_
