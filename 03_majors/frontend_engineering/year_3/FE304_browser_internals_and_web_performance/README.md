# FE304 · Browser Internals and Web Performance

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 3 · 6 | 4 (≈ 120 hours) | L2 → L3 | [FND114](../../../../01_year_1_foundations/semester_2/FND114_web_foundations_http_html_css_and_javascript/README.md), [CS205](../../../../02_year_2_core_computer_science/semester_3/CS205_software_engineering_i_design_testing/README.md) | [FE404](../../year_4/FE404_frontend_system_design_at_scale/README.md), [FE401](../../year_4/FE401_full_stack_frameworks_rendering_data_fetching/README.md), [FE402](../../year_4/FE402_advanced_ui_animation_graphics_webgl_and_webgpu/README.md) |

Part of the [Frontend Engineering major](../../README.md). Uses the transport knowledge of [CS204](../../../../02_year_2_core_computer_science/semester_3/CS204_computer_networks/README.md), the process and memory model of [CS203](../../../../02_year_2_core_computer_science/semester_3/CS203_operating_systems/README.md), and FE301's event loop. FND114 introduced LCP, INP and CLS. This course makes you the person a team calls when they fail.

## Why this course matters now

Google's Core Web Vitals pass when, at the 75th percentile of page loads, Largest Contentful Paint is at most 2.5 s, Interaction to Next Paint at most 200 ms, and Cumulative Layout Shift at most 0.1. In the HTTP Archive's July 2025 data only 48% of sites passed all three on mobile (56% on desktop). Mobile LCP was the weakest metric, good on just 62% of sites. India is mobile-first. In September 2026, 77.3% of Indian web traffic came from mobile, and Android ran on 93.89% of Indian phones (StatCounter). Cloudflare's 75th-percentile Indian connection is 6.2 Mbps down with an 85 ms round trip, and Alex Russell's 2026 analysis argues that teams building for emerging markets should design for the 90th or 95th percentile, not the 75th. Performance work pays: redBus reported a 7% sales increase after fixing INP, and The Economic Times cut INP from over 1,000 ms to 257 ms while bounce rate on topic pages fell 50%. AI now helps here: Chrome DevTools' AI assistance explains traces, and the Chrome DevTools MCP server (September 2025) lets coding agents record and read them. Deciding what the trace means, which percentile of users to serve and what to trade away is still a human job.

## Learning outcomes

By the end you can:

1. **Explain** how a modern browser turns bytes into pixels across its processes: networking, parsing, style, layout, paint, compositing and raster.
2. **Read** a DevTools Performance trace and a network waterfall, and **attribute** every millisecond of LCP and INP to a cause.
3. **Fix** LCP (TTFB, resource load delay, load duration, render delay), INP (input delay, processing, presentation) and CLS with measured before-and-after evidence.
4. **Design** a loading strategy: priorities, preloading, code splitting, lazy loading, speculative navigation and back/forward cache eligibility.
5. **Deliver** images, fonts (including Indic scripts) and video at the smallest size that looks right on each device.
6. **Implement** caching with HTTP headers and a service worker, including offline behaviour and safe updates.
7. **Set and enforce** performance budgets in CI, and **run** real-user monitoring (RUM) with attribution.
8. **Test** on real low-end Android devices and slow networks, and **justify** design decisions with percentile data rather than averages.

## Chapters and lessons

### Chapter 1 · How browsers are built (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Process model | Browser, renderer, GPU and network processes; site isolation; why one tab's crash does not kill others | Use the browser task manager and `chrome://process-internals` to map a page with three iframes |
| 1.2 Engines | Blink/RenderingNG, WebKit, Gecko; where Interop scores come from; why Safari matters for every Indian iPhone user | Compare the same trace in Chrome and Firefox profilers |
| 1.3 Navigation lifecycle | Request, response, commit, parse, load; `beforeunload`, `pagehide`, back/forward cache | Log the lifecycle events of a navigation; make a page bfcache-eligible |
| 1.4 Reading a trace | Main thread, compositor, raster, network tracks; tasks, frames, flame charts | Annotate a 3-second trace with every major task and its cause |

**Check your understanding:** Why can scrolling stay smooth while the main thread is busy? Why does an `unload` listener cost performance on later navigations? What would you look for first in a trace of a page that "feels slow"?

### Chapter 2 · Network and protocol performance (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Connection cost | DNS, TCP or QUIC, TLS 1.3 round trips; why 85 ms RTT dominates on Indian mobile; `preconnect` and `dns-prefetch` | Count round trips before the first byte at 100 ms and 300 ms RTT |
| 2.2 HTTP/2 and HTTP/3 | Multiplexing, stream priorities, head-of-line blocking; 103 Early Hints | Compare the same page over HTTP/2 and HTTP/3 on a lossy throttled link |
| 2.3 CDNs and edge | Edge caches, origin shield, regional points of presence; serving Indian users from Indian regions | Measure TTFB from three regions with and without a CDN |
| 2.4 Compression | gzip, Brotli, zstd; static vs dynamic compression; Compression Dictionary Transport (not Baseline) | Compress a 1 MB JavaScript bundle three ways; report size and decode time |

**Check your understanding:** Why does reducing request count matter less on HTTP/2 but connection count still matters? When does a CDN make TTFB worse? Why can a smaller compressed file still be slower on a low-end phone?

### Chapter 3 · The rendering pipeline (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Parsing | The HTML parser, the preload scanner, parser-blocking scripts, `async`/`defer`/`type=module`, render-blocking CSS | Make a page render 1 s sooner by changing only script and link attributes |
| 3.2 Style and layout | Selector matching cost, style invalidation, layout trees, forced synchronous layout and layout thrashing | Find and fix thrashing in a list animation; show the purple bars disappear |
| 3.3 Paint, layers, compositing | Paint records, layer promotion, `will-change`, compositor-only animations (`transform`, `opacity`) | Turn a janky `top`-based animation into a compositor animation at 60 fps |
| 3.4 Containment | `contain`, `content-visibility` (Baseline September 2025), `contain-intrinsic-size` | Render a 5,000-item page faster with `content-visibility`; check accessibility is preserved |

**Check your understanding:** Why does reading `offsetHeight` after writing a style trigger layout? Why is a compositor-only animation smooth during heavy JavaScript? What does `content-visibility: auto` risk for find-in-page and screen readers?

### Chapter 4 · JavaScript cost and the main thread (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 The cost of a byte of JavaScript | Download, parse, compile, execute; why 680 KiB (the median mobile page's JavaScript in Russell's 2026 analysis) hurts more on a Helio G99 than on a laptop | Profile the same bundle on a laptop and a low-end Android phone |
| 4.2 Long tasks and frames | Tasks over 50 ms; Long Animation Frames API (Chromium); attributing scripts | Find the script behind a 400 ms long animation frame |
| 4.3 Yielding | Breaking work up with `setTimeout`, `scheduler.yield` where supported (not Baseline), `isInputPending` history; prioritising input | Split a 600 ms handler so input stays responsive |
| 4.4 Hydration cost | SSR plus hydration, partial and progressive hydration, islands, resumability (preview of FE401) | Measure hydration time of the same page in three architectures |
| 4.5 Third parties | Tag managers, analytics and chat widgets; facades; moving work to workers (Partytown) | Remove 300 ms of third-party main-thread time without losing data |

**Check your understanding:** Why does a server-rendered page sometimes have worse INP than a client-rendered one? What makes third-party scripts hard to govern? When does yielding make total work slower but the page better?

### Chapter 5 · Core Web Vitals in depth (weeks 5–6)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 LCP | Candidate elements, sub-parts (TTFB, resource load delay, load duration, render delay), common causes | Break down the LCP of 3 Indian news homepages using DevTools |
| 5.2 INP | Interactions measured, input delay vs processing vs presentation delay; INP replaced FID in March 2024 | Reproduce and fix a slow "Add to cart" interaction |
| 5.3 CLS | Session windows, layout shift sources (images, ads, fonts, late banners), `aspect-ratio`, reserved space | Fix 4 shift sources on a sample news page |
| 5.4 Field vs lab | CrUX, PageSpeed Insights, Lighthouse 13; why lab scores and real users disagree; percentiles | Explain a site that scores 98 in Lighthouse but fails CrUX |
| 5.5 Real-user monitoring | `web-vitals` 6 with attribution; LCP and Event Timing APIs reached Baseline in December 2025, layout instability (CLS) is still Chromium-only | Ship RUM to a dashboard; segment by device memory and connection type |

**Check your understanding:** Why is the 75th percentile used instead of the mean? What does "resource load delay" tell you about how the LCP image was discovered? Why can you measure INP in Safari but still not CLS, and what does that do to your dashboards?

### Chapter 6 · Loading strategy (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Priorities | `fetchpriority` (Baseline October 2024), preload and `modulepreload`, priority inversion | Raise the LCP image priority; show the network order change |
| 6.2 Lazy loading done right | Native `loading="lazy"` (widely available June 2026); never lazy-load the LCP image (16–17% of pages still do, per Web Almanac 2025) | Find the LCP image lazy-loaded by a component library and fix it |
| 6.3 Code splitting | Route and interaction splitting, dynamic `import()`, chunking trade-offs, prefetch on intent | Split a 900 KB SPA so the home route loads under 200 KB |
| 6.4 Speculative navigation | Speculation Rules prerender and prefetch (Chromium; not Baseline), prerender safety (analytics, state) | Prerender likely next pages; measure navigation LCP |
| 6.5 Back/forward cache | Eligibility blockers (`unload`, `Cache-Control: no-store` on 23% of sites per Web Almanac 2025) | Make 3 pages bfcache-eligible; show instant back navigation |

**Check your understanding:** Why does preloading too much make LCP worse? When is prerendering harmful? Why does `no-store` on HTML hurt back navigation, and when is it still required?

### Chapter 7 · Images, fonts and media (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Image formats | AVIF (widely available July 2026) and WebP; quality settings; decoding cost on low-end CPUs | Encode 20 product photos; pick per-image quality by visual comparison |
| 7.2 Responsive images | `srcset` and `sizes`, art direction with `<picture>`, image CDNs, DPR caps for low-end devices | Cut image bytes 60% on a product grid with no visible loss |
| 7.3 Web fonts | `font-display`, preload, subsetting by script (Devanagari, Bengali, Tamil subsets are large), `size-adjust` fallbacks, system-font strategy | Ship Hindi and English text with zero font-caused layout shift |
| 7.4 Video | Posters, `preload="none"`, adaptive streaming, autoplay policies, data cost | Replace a hero autoplay video with a poster that loads on demand |

**Check your understanding:** Why might AVIF be slower than WebP on some devices? How does a wrong `sizes` attribute waste bytes? What is the cost of shipping a full Devanagari font for a page with ten Hindi words?

### Chapter 8 · Caching and service workers (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 HTTP caching strategy | Immutable hashed assets, short-lived HTML, `stale-while-revalidate`, `Vary`, CDN vs browser caches | Write a caching policy for an SPA and a server-rendered site |
| 8.2 Service worker lifecycle | Install, activate, `skipWaiting`, clients claim, update flow, navigation preload | Ship an update without breaking users on the old version |
| 8.3 Strategies | Cache-first, network-first, stale-while-revalidate with Workbox 7; offline fallback pages | Make a news reader work offline for the last 20 articles |
| 8.4 Storage | Cache Storage, IndexedDB, OPFS (widely available September 2025), quotas and eviction | Measure storage use and survive eviction gracefully |

**Check your understanding:** Why does a service worker sometimes make a site slower? What happens to users when you deploy a bug inside a cache-first service worker, and how do you recover? Why must HTML and hashed assets have different cache policies?

### Chapter 9 · Designing for India's devices and networks (weeks 10–11)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 The baseline device | Russell's 2026 baseline (Samsung Galaxy A24 4G class, MediaTek Helio G99); thermal throttling; RAM pressure; why your laptop lies | Profile your P2 on a real low-end Android phone with remote debugging |
| 9.2 The baseline network | P75 global (9 Mbps, 100 ms) vs India P75 (6.2 Mbps, 85 ms); variance, packet loss, handovers; designing for P90/P95 | Run tests across 4 throttling profiles; report the percentile your design serves |
| 9.3 Budgets from physics | Russell's critical-path budgets: for a 3 s target on the baseline, about 1.2 MiB total with about 0.62 MiB JavaScript for a JavaScript-heavy page | Derive a budget for your own app from target time, RTT and bandwidth |
| 9.4 Data cost and lite modes | `Save-Data`, user-selectable lite modes, avoiding autoplay, text-first fallbacks | Add a lite mode that halves page weight; measure usage in RUM |
| 9.5 Case studies | redBus (INP and sales) and The Economic Times (INP, bounce and page views); what transferred and what did not | Present a 10-minute case analysis with your own reproduction of one fix |

**Check your understanding:** Why does designing for P75 exclude many users in India? How would you defend a budget to a product manager who wants a carousel? What did redBus and The Economic Times change that you could apply tomorrow?

### Chapter 10 · Measurement, budgets and governance (week 12)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Budgets in CI | `size-limit`, Lighthouse CI assertions, bundle analysis, per-route budgets | Fail a pull request that adds 30 KB to the home route |
| 10.2 RUM operations | Dashboards by percentile, device and route; alerting on regressions; sampling | Set an alert that fires on a planted INP regression |
| 10.3 Experiments | A/B testing performance changes; tying vitals to conversions with care | Design an experiment for a lazy-loading change |
| 10.4 Using AI on traces | DevTools AI assistance and the Chrome DevTools MCP server: what they explain well and where they guess | Give an agent a trace; grade its diagnosis against your own |

**Check your understanding:** Why do budgets fail when nobody owns them? What can correlation between faster pages and higher conversion not prove? How do you check an AI's trace diagnosis quickly?

### Chapter 11 · Rendering architectures and performance (weeks 13–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 The spectrum | CSR, SSR, SSG, streaming, islands, resumability; TTFB vs LCP vs INP trade-offs | Build one page four ways; measure all three vitals on the baseline profile |
| 11.2 Choosing per route | Marketing, product listing, checkout and dashboard routes need different strategies | Write a rendering plan for an e-commerce site |
| 11.3 Performance reviews | Running a performance review of a real codebase; writing findings that get fixed | Review a classmate's P3 with prioritised findings |

**Check your understanding:** Why might streaming SSR improve LCP but hurt INP? Which route of an e-commerce site deserves the most JavaScript, and why? What evidence makes a performance finding convincing to a product team?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Trace reading | Annotated trace |
| 2 | 2 | Lab 2 · Protocols and compression | Round-trip and compression report |
| 3 | 3 | Lab 3 · Pipeline thrash | Fixed animation; **P1 starts** |
| 4 | 4 | Lab 4 · Main thread | Yielded handler, third-party report |
| 5 | 5 | Lab 5 · LCP breakdown | Sub-part analysis; **P1 due** |
| 6 | 5 | Lab 5 (cont.) · INP and CLS | Fixed interaction and shifts |
| 7 | 6 | Lab 6 · Loading strategy | Priority and split plan; mid-term (AI off) |
| 8 | 7 | Lab 7 · Images and Indic fonts | Byte and CLS report |
| 9 | 8 | Lab 8 · Offline reader | Service worker with safe update; **P2 due** |
| 10 | 9 | Lab 9 · Real low-end device | Device report |
| 11 | 9 | Case-study presentation | Reproduced fix |
| 12 | 10 | Lab 10 · Budgets and RUM | CI gate and alert; **P3 starts** |
| 13 | 11 | Four architectures | Measurement table |
| 14 | 11 | Peer performance review | **P3 due** |
| 15 | Review | P3 defence on a real device | Final exam (AI off) |

## Working with AI in this course

- **Use AI for:** first-pass trace explanations (DevTools AI assistance); generating test pages that reproduce a pattern; writing Lighthouse CI configuration; summarising a long waterfall; letting an agent with the Chrome DevTools MCP server run repeated traces.
- **Do without AI (drills):** trace annotation; LCP sub-part breakdowns; deriving a budget from RTT and bandwidth; the mid-term and final, which include reading printed traces.
- **Verify AI output by:** reproducing the claimed improvement with at least 5 runs and reporting the median and spread; checking field data, not just lab data; testing on a real low-end device; confirming every "this API is supported" claim with Baseline data.
- **Where AI still fails here (collect your own evidence):** look for advice that improves Lighthouse but not field INP, such as `preload` on everything, lazy-loading the LCP image, or adding `will-change` everywhere. Also look for generic advice that ignores the measured bottleneck, and claims about Safari support that are out of date. Record each one with the measurement that disproved it.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (10) | 25% |
| Projects P1 · P2 · P3 | 10% · 15% · 20% |
| Mid-term (AI off) | 10% |
| Final (AI off, 3 h, trace reading and live fixing) | 20% |

**Mastery gate.** You pass when you can, with AI off, take an unfamiliar slow page and within 3 hours:
- produce an annotated trace;
- attribute its LCP and INP to sub-parts;
- fix it to LCP ≤ 2.5 s, INP ≤ 200 ms and CLS ≤ 0.1 under a provided low-end throttling profile (4× CPU, 9 Mbps, 100 ms RTT), median of 5 runs;
- explain each change and its measured effect.

## Industry reality

Web performance engineer is a named senior specialism on the [FE market page](../../../../06_career_and_market_readiness/01_market_map/roles/FE_frontend_engineering.md), and performance on low-end devices and slow networks is listed as growing in value for India's mobile-first users. The public case studies are clear about the business link: redBus (INP and +7% sales) and The Economic Times (INP from over 1,000 ms to 257 ms, bounce −50%, page views +43%). Since Safari added the LCP and Event Timing APIs (Baseline December 2025), teams can measure two of the three vitals across all major engines. Frontend system design rounds (FE404) expect you to state performance budgets and how you would enforce them.

**Interview questions from this course**

1. *Walk me through what happens between receiving HTML and the first paint, and how you would make LCP faster.* A strong answer covers the parser, preload scanner, render-blocking CSS and parser-blocking scripts, the LCP sub-parts, and fixes for each: TTFB via CDN or caching, discovery via preload or `fetchpriority`, bytes via formats and sizes, render delay via blocking scripts.
2. *Our INP is 450 ms on mobile. How do you find and fix it?* A strong answer segments field data by interaction and device, uses attribution (`web-vitals`, LoAF) and reproduces with CPU throttling. It splits long handlers, yields, defers non-urgent work, reduces DOM size and re-renders, and verifies in the field.
3. *Why does our Lighthouse score say 98 while Search Console says the page fails?* A strong answer contrasts lab with field data: one simulated device vs real P75 users, interactions that Lighthouse does not perform, cache state, third parties, geography and device mix.
4. *Design caching for an SPA's assets, HTML and API.* A strong answer gives hashed assets `immutable` with long `max-age`, HTML short-lived or revalidated, and API data with `stale-while-revalidate` where safe and private where personalised. It covers CDN rules and how a service worker update is rolled out and rolled back.
5. *How would you set a performance budget for a product used mostly on low-end Android phones in India?* A strong answer derives the budget from a target time and the baseline device and network (citing data such as Russell's 2026 budgets), sets per-route JavaScript and image limits, enforces them in CI, and monitors P75 and P90 in RUM.

## Resources (free first)

- **Courses and guides:** [web.dev Learn Performance](https://web.dev/learn/performance); [Core Web Vitals](https://web.dev/articles/vitals) and the [LCP](https://web.dev/articles/lcp), [INP](https://web.dev/articles/inp), [CLS](https://web.dev/articles/cls) guides; [Optimize LCP](https://web.dev/articles/optimize-lcp), [INP](https://web.dev/articles/optimize-inp), [CLS](https://web.dev/articles/optimize-cls); [Optimise long tasks](https://web.dev/articles/optimize-long-tasks); [bfcache](https://web.dev/articles/bfcache); [Fetch Priority](https://web.dev/articles/fetch-priority); [Rendering on the web](https://web.dev/articles/rendering-on-the-web); [Offline cookbook](https://web.dev/articles/offline-cookbook).
- **Internals:** [Inside look at modern web browser](https://developer.chrome.com/blog/inside-browser-part1); [How browsers work](https://web.dev/articles/howbrowserswork); Ilya Grigorik, [High Performance Browser Networking](https://hpbn.co/); [Performance panel reference](https://developer.chrome.com/docs/devtools/performance/reference); [Long Animation Frames](https://developer.chrome.com/docs/web-platform/long-animation-frames); [Speculation rules](https://developer.chrome.com/docs/web-platform/implementing-speculation-rules).
- **Data:** [CrUX](https://developer.chrome.com/docs/crux); [HTTP Archive](https://httparchive.org/) and [Web Almanac 2025: Performance](https://almanac.httparchive.org/en/2025/performance); Alex Russell, [The Performance Inequality Gap, 2026](https://infrequently.org/2025/11/performance-inequality-gap-2026/).
- **Tools:** [Lighthouse](https://developer.chrome.com/docs/lighthouse/overview); [Lighthouse CI](https://github.com/GoogleChrome/lighthouse-ci); [web-vitals](https://github.com/GoogleChrome/web-vitals); [Workbox](https://developer.chrome.com/docs/workbox); [Partytown](https://partytown.qwik.dev/); [size-limit](https://github.com/ai/size-limit); [remote debugging Android](https://developer.chrome.com/docs/devtools/remote-debugging); [Chrome DevTools MCP](https://github.com/ChromeDevTools/chrome-devtools-mcp); WebPageTest (free tier).
- **Practitioner blogs:** [CSS Wizardry](https://csswizardry.com/) (for example, [Cache-Control for civilians](https://csswizardry.com/2019/03/cache-control-for-civilians/)); [DebugBear](https://www.debugbear.com/) articles.

## Sources

All checked 12 Oct 2026.

- web.dev, Web Vitals (thresholds and 75th percentile) — https://web.dev/articles/vitals
- HTTP Archive, Web Almanac 2025, Performance chapter (July 2025 data) — https://almanac.httparchive.org/en/2025/performance
- Alex Russell, "The Performance Inequality Gap, 2026" (24 Nov 2025; baseline device and network, India P75 from Cloudflare data, budgets, median JavaScript) — https://infrequently.org/2025/11/performance-inequality-gap-2026/
- StatCounter, India platform share and mobile OS share, Sep 2026 — https://gs.statcounter.com/platform-market-share/desktop-mobile-tablet/india · https://gs.statcounter.com/os-market-share/mobile/india
- web.dev case studies: redBus INP — https://web.dev/case-studies/redbus-inp · The Economic Times INP — https://web.dev/case-studies/economic-times-inp
- web-features 3.42.0 Baseline data (LCP and Event Timing Dec 2025; layout instability, speculation rules, LoAF, `scheduler`, Compression Dictionary Transport not Baseline; `fetchpriority` Oct 2024; `content-visibility` Sep 2025; AVIF widely available Jul 2026; `loading="lazy"` Jun 2026; OPFS Sep 2025) — https://web-platform-dx.github.io/web-features/
- Chrome for Developers, "Chrome DevTools (MCP) for your AI agent" (23 Sep 2025) — https://developer.chrome.com/blog/chrome-devtools-mcp

_Last reviewed: 2026-10_
