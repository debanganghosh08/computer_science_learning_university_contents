# FE304 · Labs and projects

Every performance claim in this course needs evidence: at least 5 runs, the median and the spread, the throttling profile, and the device. The standard lab profile is "baseline mobile": 4× CPU slowdown, 9 Mbps down, 3 Mbps up, 100 ms RTT. It matches the 2026 baseline network in Russell's analysis. From Lab 9 on, you also test on a real low-cost Android phone. Trace-reading drills are done without AI.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Trace reading (no AI) | Annotate a 3-second Performance trace of a provided page | Annotated trace: every task over 50 ms named with its cause | 4 h |
| 2 · Protocols and compression | Round trips at 100 ms and 300 ms RTT; HTTP/2 vs HTTP/3 on a lossy link; gzip vs Brotli vs zstd | Report with waterfalls and a table of bytes and decode times | 4 h |
| 3 · Pipeline thrash | Fix layout thrashing and convert a `top`-based animation to a compositor animation | Before/after traces; 60 fps at 4× CPU | 4 h |
| 4 · Main thread | Split a 600 ms handler; facade a chat widget; move analytics to a worker | INP before/after; third-party main-thread time cut by at least 300 ms | 5 h |
| 5 · Vitals clinic | LCP sub-part breakdown of 3 news homepages; fix a slow interaction and 4 shift sources in a sample app | Breakdown table; fixed app passing all three thresholds on baseline mobile | 6 h |
| 6 · Loading strategy | Priorities, code splitting, speculation rules, bfcache eligibility | Home route at most 200 KB JavaScript; bfcache "restored" evidence for 3 pages | 5 h |
| 7 · Images and Indic fonts | Responsive AVIF/WebP grid; subset Hindi and Tamil fonts; zero font-caused CLS | Byte savings at least 60%; CLS from fonts at most 0.01 | 4 h |
| 8 · Offline reader | Service worker with Workbox 7: offline last-20 articles, safe update and rollback | Offline demo; update test across two deployed versions | 5 h |
| 9 · Real low-end device | Remote-debug your P2 on a low-cost Android phone; compare with emulated throttling | Device report: where emulation lied and by how much | 3 h |
| 10 · Budgets and RUM | `size-limit` and Lighthouse CI gates; `web-vitals` attribution to a dashboard; regression alert | Failing PR on a planted 30 KB regression; alert screenshot on a planted INP regression | 5 h |

## Projects

### P1 · Rescue a slow news homepage (L1, ~6 hours)

**Real-world inspiration:** The Economic Times documented cutting INP from over 1,000 ms to 257 ms. It deferred non-critical work, lazy-loaded third parties, reduced DOM size and moved third-party work to workers, and bounce rate on topic pages fell 50%. You get a deliberately slow news homepage modelled on common patterns: hero image, ad slots, a carousel, a tag manager and web fonts. The page is an **illustrative scenario**.

**What to build:** a fixed version of the page, plus a written performance report: findings ranked by impact, each with a trace screenshot, the change and the measured result.

**Acceptance criteria (baseline mobile profile, median of 5 runs):**
- LCP at most 2.5 s (from about 6 s), INP at most 200 ms on the provided interaction script, CLS at most 0.1.
- No content, ad slot or analytics event removed; the business functionality is unchanged (a checklist test passes).
- JavaScript transferred on first load cut by at least 40%.
- The report attributes at least 80% of the LCP improvement to specific sub-parts.

**Stretch goals:** a lite mode triggered by `Save-Data`; a facade for the video embed.

**What it proves to an employer:** you can diagnose and fix real-world performance problems with evidence, without breaking what the business needs.

### P2 · Fast product-listing page with field monitoring (L2, ~15 hours)

**Real-world inspiration:** redBus reported a 7% increase in sales after improving INP on its search pages. It debounced scroll handlers, fetched smaller result batches earlier, and kept input state local instead of in a global store. The PLP you build is an **illustrative scenario**.

**What to build:** a product-listing page with filters, sorting, infinite scroll (plus a "load more" button for accessibility), responsive images and an "add to cart" interaction, using a framework of your choice. Add:
- RUM with `web-vitals` attribution sent to your own endpoint;
- a dashboard by route, device memory and effective connection type;
- a synthetic traffic generator that replays sessions from 3 device profiles.

**Acceptance criteria:**
- **Lab:** LCP at most 2.5 s, INP at most 200 ms, CLS at most 0.05 on baseline mobile, median of 5 runs.
- **Synthetic field:** after 2,000 replayed sessions across the 3 profiles, the dashboard shows P75 INP at most 200 ms and P75 LCP at most 2.5 s on the lowest profile, and reports P90 as well.
- **Attribution:** for the slowest 5% of interactions, the dashboard names the responsible script and handler.
- **Budgets in CI:** at most 170 KB of JavaScript (gzipped) for the route; image bytes above the fold at most 150 KB; a PR that breaks either budget fails.
- **Accessibility:** infinite scroll has a keyboard-reachable "load more" path, and focus is not lost when content loads (axe zero, manual check).

**Stretch goals:** prerender the most likely product detail page with speculation rules and measure navigation LCP; bfcache eligibility across the flow.

**What it proves to an employer:** you can build fast by default, measure what real users get, and tie fixes to evidence a product team will trust.

### P3 · A "lite" PWA for low-end phones and patchy networks (L3, portfolio-grade, ~30 hours)

**Real-world inspiration:** Indian users browse mostly on mobile and mostly on Android. Russell's 2026 analysis puts the Indian P75 connection at 6.2 Mbps with an 85 ms RTT and recommends designing for P90 or P95 in emerging markets. The app, a bus and train timetable and booking-status PWA using public or synthetic data, is an **illustrative scenario**.

**What to build:** an installable PWA with:
- search, results, a detail view and a saved-trips list;
- offline support for saved trips and the last searches;
- a lite mode (text-first, no images unless tapped);
- Hindi and English with subsetted fonts;
- background refresh when possible, with clear stale-data labels;
- a performance budget document derived from first principles, enforced in CI.

**Acceptance criteria:**
- **Real device:** on a low-cost Android phone with a MediaTek Helio G99-class or slower chip, using a 3 Mbps/300 ms throttled network (a P90-style profile you justify), the first visit reaches LCP at most 3 s and the repeat visit at most 1.5 s. You record the median of 5 runs on video with the trace.
- **Budget:** initial critical-path transfer at most 150 KB gzipped, including at most 75 KB of JavaScript, derived and justified in the budget document.
- **Interaction:** INP at most 200 ms at P75 in a 1,000-session synthetic replay on the lowest profile.
- **Offline:** with the network off, saved trips and the last 5 searches work. Every view shows data age, and no screen hangs on a spinner for more than 1 s without explanation.
- **Updates:** two deployments in sequence update the service worker safely. A planted bad deployment is rolled back with a kill-switch, and you document the recovery.
- **Accessibility:** axe zero; TalkBack walkthrough of search to saved trip; works at 200% Android font scale.
- **Report:** a 4-page write-up with the budget derivation, what you cut and why, and the field-vs-lab gap you observed.

**Stretch goals:** an SMS-style text-only fallback page under 14 KB; compare a framework build with a no-framework build of the same app and report the cost of each.

**What it proves to an employer:** you can build for the users most products underserve, with the evidence and discipline of a web performance engineer.

## Feeds into

- [FE404 Frontend System Design at Scale](../../year_4/FE404_frontend_system_design_at_scale/README.md): budgets, caching and offline-first architecture in design interviews and large systems.
- [FE401 Full-Stack Frameworks](../../year_4/FE401_full_stack_frameworks_rendering_data_fetching/README.md): rendering strategies chosen per route with measured trade-offs.
- [FE402 Advanced UI](../../year_4/FE402_advanced_ui_animation_graphics_webgl_and_webgpu/README.md): frame budgets for animation and graphics.
- [QAE303 Performance and Load Testing](../../../software_quality_test_engineering/year_3/QAE303_performance_and_load_testing/README.md), as an elective on the server side of the same problem.
