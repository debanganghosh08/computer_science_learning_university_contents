# FE302 · Labs and projects

All work uses React 19.3 with TypeScript under `strict`, and the React Compiler's lint rules (`eslint-plugin-react-hooks`, `recommended`) must pass. Every component must have zero axe violations and a keyboard walkthrough recorded in its README. Lab 1 and the P1 core are done without AI assistants, because they rehearse the machine-coding rounds of frontend interviews.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Mini renderer (no AI) | `createElement`, host rendering, `useState`, keyed reconciliation of children | 40 tests including keyed reorder; a diagram of your reconciliation algorithm | 6 h |
| 2 · State design | Inventory every piece of state in a provided app (owner, lifetime, source of truth), then refactor | Inventory table; refactor with 25%+ fewer state variables and all tests green | 4 h |
| 3 · Effects clinic | Remove or fix 10 effects (derivations, chains, races, subscriptions) | 8+ effects removed; race test that fails before and passes after; `useSyncExternalStore` subscription with no tearing | 5 h |
| 4 · Compound components | Accessible `Tabs`, `Disclosure` and `Menu` with controlled and uncontrolled modes | Storybook stories; axe zero; keyboard tests per WAI-ARIA APG | 5 h |
| 5 · Concurrent features | Filter 20,000 rows with transitions vs debounce; optimistic cart with rollback | INP numbers at 4× CPU throttle for three variants; rollback test under failure | 6 h |
| 6 · Server cache | Move fetch-in-effect code to TanStack Query; remove a waterfall | Diff with deleted lines counted; Network-panel timings before/after | 4 h |
| 7 · Server Components | Build a product page with Server Components, one streamed slow panel and validated Server Functions | Boundary diagram; client JS before/after; authorisation and validation tests; CVE-2025-55182 incident review | 7 h |
| 8 · Performance | Profile a slow dashboard; apply React Compiler, context splitting and virtualisation | Render counts and INP before/after; compiler bail-out list with reasons | 5 h |
| 9 · Accessible forms | One-schema validation shared with the server; error summary; Hindi localisation | NVDA and TalkBack test scripts passed; plural/number format tests | 5 h |
| 10 · Same feature, four frameworks | Live-filtered list with a detail panel in React, Solid, Svelte and Vue (or Angular) | Table: shipped JS, update time for 10,000 rows, lines of code; 2-page decision record | 8 h |

## Projects

### P1 · Accessible station search (L1, ~6 hours)

**Real-world inspiration:** railway and travel sites in India ask users to pick one of thousands of stations or cities by typing. The task is a classic frontend machine-coding question. The dataset is any public list of Indian railway station names and codes. The interface is an **illustrative scenario**, not a copy of any site.

**What to build:** a `StationCombobox` with:
- async suggestions from a mock API with random 50–800 ms latency;
- matching on station name, code and common spellings;
- recent selections and keyboard support per the APG combobox pattern;
- loading, empty and error states;
- a virtualised list when more than 100 matches return.

**Acceptance criteria:**
- **Accessibility:** axe reports zero violations, and a recorded NVDA walkthrough selects "Howrah Jn (HWH)" using only the keyboard. `aria-expanded`, `aria-activedescendant` and the result count announcements behave as the APG pattern specifies.
- **Race safety:** a test with randomised latencies over 200 runs never shows results for an outdated query.
- **Responsiveness:** INP is at most 200 ms with 8,000 stations loaded at 4× CPU throttling (DevTools trace attached).
- **Correctness:** 25 Testing Library tests written against roles and names, not class names.
- **Constraint:** core behaviour written without AI; the README states which parts, if any, used AI afterwards.

**Stretch goals:** Hindi and English matching with transliteration ("dilli" finds "Delhi"); highlight matched characters without breaking Devanagari conjuncts (`Intl.Segmenter`).

**What it proves to an employer:** you can pass a machine-coding round to a production standard, including accessibility and race conditions, not just a working demo.

### P2 · Collaborative-ready task board (L2, ~15 hours)

**Real-world inspiration:** issue trackers such as Jira, Linear and Trello are dense, interactive React-style apps where drag-and-drop, optimistic updates and keyboard use all matter.

**What to build:** a board with columns and cards. It supports drag-and-drop reordering with a keyboard alternative (pick up, move, drop with announcements), inline editing, filters stored in the URL, undo for the last 20 actions, and optimistic mutations through TanStack Query against a mock API. The mock API fails 20% of requests and returns responses out of order.

**Acceptance criteria:**
- **No lost updates:** a scripted test performs 500 random moves and edits under the failing API. The final client state equals the server state, and every failed mutation is rolled back and reported.
- **Keyboard and screen reader:** every drag operation has a keyboard path; NVDA announces pick-up, position and drop; axe reports zero violations.
- **Performance:** with 1,000 cards, moving a card keeps INP at most 200 ms at 4× CPU throttle, and at most 3 components re-render per move (Profiler evidence).
- **State discipline:** no server data in a global client store; filters survive reload and back/forward.
- **Undo:** undo restores order and content exactly, including after a rolled-back failure.

**Stretch goals:** live updates from a WebSocket feed with conflict handling (preview of FE404's collaboration chapter); `<ViewTransition>` animations that respect `prefers-reduced-motion`.

**What it proves to an employer:** you can build the interaction-heavy, failure-tolerant UI that product companies ship, and you can prove it does not lose data.

### P3 · Real-time market watchlist on Server Components (L3, portfolio-grade, ~30 hours)

**Real-world inspiration:** Indian brokerage apps stream live prices to thousands of rows. Zerodha's Kite Connect API documents a [WebSocket streaming interface](https://kite.trade/docs/connect/v3/websocket/) for market quotes. Use a simulated feed with the same shape. Do not connect to a real brokerage account. Any trading data you display is synthetic, and the product is an **illustrative scenario**.

**What to build:** a Next.js 16 or React Router v8 app with:
- a server-rendered shell and instrument search, using Server Components and validated Server Functions;
- client islands for a live watchlist of up to 500 instruments ticking up to 5 times per second, using `useSyncExternalStore` over a WebSocket store;
- a detail panel that streams in with Suspense, and an order-entry form (mock, never executed) using Actions and `useOptimistic`;
- keyboard shortcuts and colour-plus-icon price change indicators (never colour alone);
- Hindi and English UI.

**Acceptance criteria:**
- **Rendering efficiency:** at 500 instruments × 5 ticks/s, only rows whose values changed re-render (Profiler evidence). Main-thread long tasks stay under 50 ms on a 4× CPU-throttled trace over 60 seconds.
- **Responsiveness:** INP at most 200 ms while ticking, measured with the `web-vitals` library with attribution.
- **Memory:** heap growth under 5 MB over a 30-minute soak test with subscribe and unsubscribe churn.
- **Security:** every Server Function checks authorisation and validates input with a shared schema; a test suite of 15 malicious inputs is rejected; dependency versions are at or above the patched RSC releases, checked in CI.
- **Accessibility:** axe zero; a screen-reader user can read a row's price and change without being flooded (live-region throttling documented and tested).
- **Bundle:** client JavaScript for the first load at most 170 KB gzipped (a stated budget, checked by `size-limit`).
- **Write-up:** a decision record on state placement, the server–client boundary and the rejected alternatives, plus your AI-error log from the course.

**Stretch goals:** port the watchlist island to Solid or Svelte inside the same page and compare update cost; add sparkline charts on canvas (preview of FE402).

**What it proves to an employer:** you can architect a real-time, server-rendered React app with measured performance, memory safety and security, which is the bar for fintech and trading frontends.

## Feeds into

- [FE401 Full-Stack Frameworks](../../year_4/FE401_full_stack_frameworks_rendering_data_fetching/README.md): caching, routing and deployment of the RSC app.
- [FE402 Advanced UI](../../year_4/FE402_advanced_ui_animation_graphics_webgl_and_webgpu/README.md): view transitions, canvas charts and animation on top of these components.
- [FE403 AI-Native Interfaces](../../year_4/FE403_ai_native_interfaces_streaming_generative_ui/README.md): streaming, optimistic and interruptible UI patterns.
- [FE404 Frontend System Design at Scale](../../year_4/FE404_frontend_system_design_at_scale/README.md): the task board becomes a collaborative app.
