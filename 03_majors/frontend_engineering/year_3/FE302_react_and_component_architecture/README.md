# FE302 · React and Component Architecture

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 3 · 5 | 4 (≈ 120 hours) | L2 → L3 | [FND114](../../../../01_year_1_foundations/semester_2/FND114_web_foundations_http_html_css_and_javascript/README.md), [CS205](../../../../02_year_2_core_computer_science/semester_3/CS205_software_engineering_i_design_testing/README.md) | [FE402](../../year_4/FE402_advanced_ui_animation_graphics_webgl_and_webgpu/README.md), [FE401](../../year_4/FE401_full_stack_frameworks_rendering_data_fetching/README.md), [FE403](../../year_4/FE403_ai_native_interfaces_streaming_generative_ui/README.md), [MOB303](../../../mobile_engineering/year_3/MOB303_cross_platform_apps_flutter_and_react_native/README.md) |

Part of the [Frontend Engineering major](../../README.md). Taken alongside [FE301](../FE301_modern_javascript_and_typescript_in_depth/README.md), whose closures, event loop and signals material this course relies on, and [FE303](../FE303_css_design_systems_and_accessibility/README.md), whose accessible patterns every component here must meet.

## Why this course matters now

React is the framework developers name most often (HackerRank 2025), and it is now governed by the React Foundation under the Linux Foundation (launched February 2026). The model has changed a lot in two years:
- **React 19.2** (October 2025) added `<Activity>` and `useEffectEvent`.
- **React Compiler 1.0** (October 2025) memoises automatically. In Meta's Quest Store it improved initial loads and navigations by up to 12% and made some interactions more than 2.5× faster.
- **React 19.3** (September 2026) made `<ViewTransition>` and Fragment refs stable and added `browser()` and Trusted Types support.
- **React Server Components** moved rendering onto the server. In December 2025 they also carried a CVSS 10.0 remote-code-execution flaw (CVE-2025-55182) that affected Next.js, React Router and other frameworks.

UI generators such as v0 and Lovable, and coding agents, produce React components in seconds. They do not decide where state should live, which effects are unnecessary, where the server–client boundary goes, or how 40 teams share components without breaking each other. That architecture judgement is what this course teaches.

## Learning outcomes

By the end you can:

1. **Explain** React's render and commit phases, reconciliation and identity (keys, component type, position), and **predict** when state is kept or reset.
2. **Design** state: choose local, lifted, derived, URL, server-cache or global, and justify each with the data's owner and lifetime.
3. **Remove** unnecessary effects, and **write** correct ones (cleanup, race-safe fetching, `useEffectEvent`, `useSyncExternalStore`).
4. **Build** composable, accessible component APIs (compound components, controlled/uncontrolled, headless primitives) that other teams can extend without forking.
5. **Use** concurrent features (transitions, `useDeferredValue`, Suspense, Actions, `useOptimistic`, `<Activity>`, `<ViewTransition>`) and **measure** their effect on INP.
6. **Split** an app correctly across Server and Client Components, treating every Server Function as a public, validated endpoint.
7. **Profile** and fix rendering performance with the React Profiler, the React Compiler, virtualisation and context design.
8. **Compare** React with Vue, Svelte, Solid and Angular on reactivity model, bundle cost, SSR story and hiring market, using a build of the same feature in each.

## Chapters and lessons

### Chapter 1 · The rendering model (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Elements, components, instances | JSX compiles to element objects; components are functions of props and state; the tree React keeps | Write `createElement` and a 100-line renderer for host elements (no AI) |
| 1.2 Render and commit | Render is pure and may run more than once; commit touches the DOM; `StrictMode` double-invokes to expose impurity | Find three impure components using `StrictMode` warnings |
| 1.3 Reconciliation and identity | Same type at the same position keeps state; keys as identity; index keys and reordering bugs | Reproduce lost input text in a reorderable list; fix it with stable keys |
| 1.4 The Rules of React | Components and hooks must be pure and idempotent; hooks are called unconditionally; the compiler's lint rules (`set-state-in-render`, `set-state-in-effect`, `refs`) | Fix 10 lint violations and explain what each would break |

**Check your understanding:** Why does moving a component inside a conditional reset its state? Why is "render runs twice in development" a feature? What breaks if a component reads `Date.now()` during render, and how would the compiler treat it?

### Chapter 2 · State design (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 State as a snapshot | `useState` semantics, batching, updater functions, why logging after `setState` shows the old value | Fix a counter that increments by 1 when clicked 3 times quickly |
| 2.2 Minimal state | Derive, do not duplicate; lifting state up; colocating state down; "single source of truth" | Remove 4 redundant state variables from a checkout form |
| 2.3 Reducers and state machines | `useReducer`, events vs setters, finite states with XState 5 for flows like OTP login | Model OTP login (idle, sending, sent, verifying, locked) so impossible states cannot exist |
| 2.4 URL and form state | Search params as state, shareable filters, back-button behaviour | Make a product-listing filter shareable by URL and correct under back/forward |
| 2.5 Choosing global state | Context, Zustand 5, Jotai, Redux Toolkit: what each is for; most apps need less global state than they have | Delete a global store from a sample app by moving data to server cache and URL |

**Check your understanding:** What is the owner and lifetime of "selected tab", "cart", "logged-in user" and "search results", and where should each live? When does a state machine pay for its complexity? Why does putting server data in a global client store create bugs?

### Chapter 3 · Effects and their pitfalls (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Effects synchronise | Effects connect to external systems; dependency arrays describe what you read, not when to run | Rewrite 5 "on mount" effects as synchronisation |
| 3.2 You might not need an effect | Derived data, event-driven logic, resetting state with keys; the cost of effect chains | Remove 8 of 10 effects from a provided component with no behaviour change (tests prove it) |
| 3.3 Data fetching races | Ignore stale responses, `AbortController` cleanup, why libraries or frameworks should own fetching | Fix a profile page that shows the wrong user after fast navigation |
| 3.4 Escape hatches | `useEffectEvent` (19.2) for non-reactive logic, `useLayoutEffect` for measurement, `useSyncExternalStore` for external stores, refs | Subscribe to `matchMedia` and a WebSocket correctly; prove no tearing |

**Check your understanding:** Why does adding a function to a dependency array cause an infinite loop, and what are the three correct fixes? When is `useLayoutEffect` required? Why does fetching in effects produce waterfalls?

### Chapter 4 · Composition and component API design (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Composition over configuration | `children` and slots, compound components (`<Tabs.List>`), avoiding prop explosion | Refactor a 30-prop `Card` into composable parts |
| 4.2 Controlled and uncontrolled | Value/onChange contracts, default values, the "controllable state" hook | Build a `Disclosure` that works both ways and is tested both ways |
| 4.3 Refs and the DOM | `ref` as a prop (React 19), `useImperativeHandle`, Fragment refs (19.3) for groups of nodes without wrappers | Focus the first invalid field of a form group through a Fragment ref |
| 4.4 Headless primitives | React Aria Components, Base UI, Radix; behaviour and accessibility separated from styling; the copy-in model of shadcn/ui | Build the same `Select` on two headless libraries; compare keyboard behaviour and bundle bytes |
| 4.5 Error and loading boundaries | Error boundaries, Suspense boundaries, where to place each for good UX | Design boundaries for a dashboard so one failing widget does not blank the page |

**Check your understanding:** What makes a component API easy to extend without forking? Why should behaviour (keyboard, focus, ARIA) live in a headless layer? Where would you put error boundaries in a 12-widget dashboard, and why not around each widget?

### Chapter 5 · Concurrent React (weeks 5–6)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Transitions | Urgent vs non-urgent updates; `useTransition`, `startTransition`; interruptible rendering | Keep typing responsive while filtering 20,000 rows; measure INP before and after |
| 5.2 Deferred values | `useDeferredValue` vs debouncing; stale UI indication | Compare debounce and deferred value on a 4× CPU-throttled profile |
| 5.3 Suspense and `use` | Suspending on promises and context, cache requirements, avoiding fallback flashes | Build a profile page with nested Suspense that never shows a spinner for under 300 ms |
| 5.4 Actions | Form actions, `useActionState`, `useFormStatus`, `useOptimistic`, rollback on error | An optimistic "add to cart" that rolls back cleanly on a 500 |
| 5.5 `<Activity>` and `<ViewTransition>` | Keeping hidden UI's state and pre-rendering it; animated transitions with `addTransitionType` (19.3) | Tabs that keep scroll and form state when hidden, with directional view transitions |

**Check your understanding:** Why can a transition make INP better even though the total work is the same? When is debouncing still the right tool? What happens to an optimistic update when two requests fail out of order?

### Chapter 6 · Server state and data fetching (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Server state is a cache | Staleness, deduplication, background refetch, garbage collection; TanStack Query 5 | Replace hand-written fetch effects with queries; count the deleted lines |
| 6.2 Query keys and invalidation | Key design, targeted invalidation, dependent and parallel queries | Invalidate exactly the affected lists after a mutation |
| 6.3 Optimistic updates | Snapshot, update, rollback; conflicting concurrent mutations | Optimistic drag-and-drop reorder that survives a simulated 30% failure rate |
| 6.4 Waterfalls | Detecting them in the Network panel; prefetching; hoisting data needs to routes | Remove a three-level waterfall; show the before and after timings |

**Check your understanding:** Why are "server state" and "client state" different problems? What is the trade-off between normalised caches and per-query caches? How do you detect a waterfall in production, not just locally?

### Chapter 7 · React Server Components (weeks 8–9)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 The model | Server Components render on the server and send a serialised tree; Client Components hydrate; `'use client'` marks a boundary, not a file type | Draw the boundary for a product page; count client JavaScript before and after |
| 7.2 Serialisation rules | What can cross the boundary (props must be serialisable), passing Server Components as `children` to Client Components, `<Context>` rendered directly in Server Components (19.3) | Fix 6 boundary errors in a provided app |
| 7.3 Server Functions | `'use server'`, progressive enhancement of forms, revalidation; every Server Function is a public HTTP endpoint | Add authorisation and Zod validation to every Server Function in a sample app |
| 7.4 Security lessons | CVE-2025-55182: unsafe deserialisation in RSC packages (19.0–19.2.0) allowed unauthenticated remote code execution, even in apps with no Server Functions; patch cadence and dependency monitoring | Write a one-page incident review: exposure, detection, patch path for Next.js and React Router |
| 7.5 Streaming and client-only parts | Streaming HTML with Suspense; `use(browser())` (19.3) to keep a component out of server rendering | Stream a slow recommendations panel without blocking the main content |

**Check your understanding:** Why does RSC reduce JavaScript but not necessarily server cost? What does the attacker control in a Server Function call, and what must you check every time? Why did an RSC flaw affect apps that never wrote a Server Function?

### Chapter 8 · Performance (week 10)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Measuring renders | React DevTools Profiler, "why did this render", interaction tracing in the Performance panel | Profile a slow dashboard; list the top 3 causes with evidence |
| 8.2 Memoisation | `memo`/`useMemo`/`useCallback` by hand vs React Compiler 1.0; when the compiler bails out | Enable the compiler on a sample app; report render counts and INP before and after |
| 8.3 Context and subscriptions | Context re-render fan-out, splitting contexts, selector-based stores | Cut re-renders in a theme-plus-user context by 90% |
| 8.4 Large lists and code splitting | Virtualisation with TanStack Virtual, `lazy`, route-level splitting, preloading on intent | Render 50,000 rows at 60 fps; lazy-load the editor only when opened |

**Check your understanding:** Why can adding `useMemo` everywhere make an app slower? What does the compiler need from your code to optimise it? When is virtualisation harmful to accessibility, and how do you mitigate it?

### Chapter 9 · Forms, accessibility and internationalisation in React (week 11)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Form architecture | Native forms and Actions vs React Hook Form; schema validation shared with the server | A KYC-style form (illustrative) validated on both sides with one schema |
| 9.2 Accessible errors and focus | Error summaries, `aria-describedby`, focus on submit failure, `aria-live` for async results; focus on route change in SPAs | Pass a screen-reader test script with NVDA and TalkBack |
| 9.3 Internationalisation | ICU messages, plurals, `Intl` formatting, Hindi and English on one screen, lazy-loaded locale bundles | Localise the form into Hindi; test plural and number formats |
| 9.4 Testing components | Testing Library queries by role and name; testing behaviour, not implementation | 20 tests that would survive a full re-styling |

**Check your understanding:** Why should validation rules live in one schema? What does a screen-reader user experience when an SPA changes route without focus management? Why are role-based queries also an accessibility check?

### Chapter 10 · Alternatives compared honestly (weeks 12–13)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Fine-grained reactivity | Solid (1.9 stable, 2.0 in release candidate) and signals: components run once, only bindings update | Build the same live-filtered list in Solid; compare update cost with React |
| 10.2 Compilers | Svelte 5 runes and SvelteKit 3 (October 2026); Vue 3.5 with SFCs (3.6, in release candidate, is planned to add Vapor Mode) | Build the list in Svelte and Vue; compare shipped JavaScript |
| 10.3 Angular | Signals, zoneless change detection (default since v21), dependency injection, the enterprise market (v22, June 2026) | Port one feature to Angular; note what the framework decides for you |
| 10.4 Web components and Preact | Lit and custom elements for design systems shared across frameworks; Preact 11 as a small React-compatible runtime | Wrap one React component as a custom element; list the trade-offs |
| 10.5 Choosing | Criteria: team skills, hiring pool, SSR needs, bundle budget, long-term support; how to run a time-boxed spike | Write a 2-page decision record for a hypothetical Indian fintech choosing a stack |

**Check your understanding:** Why does React re-run components while Solid does not, and what does each design make easy or hard? When is a web component the right sharing format for a design system? What evidence would make you choose a framework other than React for a new product?

### Chapter 11 · Architecture at scale (week 14)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Feature-based structure | Feature folders, public module APIs, import boundaries enforced by lint | Restructure a 15,000-line app; add boundary lint rules |
| 11.2 Observability | Error boundaries with reporting (Sentry), source maps, user-impact metrics | Trace a production-style error back to a component and commit |
| 11.3 Migrations | Class to hooks, Create React App (sunset in February 2025) to Vite or a framework, codemods | Migrate a CRA app to Vite 8 with a codemod-first plan |
| 11.4 Reviewing generated components | Checklist: semantics, state placement, effects, keys, accessibility, bundle cost | Review 5 v0- or agent-generated components; file each fix with a test |

**Check your understanding:** How do you stop 10 teams from importing each other's internals? What is the cheapest way to migrate 300 class components safely? What is the first thing you check in a generated component?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Mini renderer (no AI) | Renderer with tests |
| 2 | 2 | Lab 2 · State design | State inventory and refactor |
| 3 | 3 | Lab 3 · Effects clinic | 8 effects removed; **P1 starts** |
| 4 | 4 | Lab 4 · Compound components | Accessible `Tabs` and `Disclosure` |
| 5 | 5 | Lab 5 · Concurrent features | INP comparison; **P1 due** |
| 6 | 5 | Lab 5 (cont.) | Optimistic cart |
| 7 | 6 | Lab 6 · Server cache | Waterfall removal report |
| 8 | 7 | Lab 7 · Server Components | Boundary diagram; mid-term (AI off) |
| 9 | 7 | Lab 7 (cont.) | Incident review; **P2 due** |
| 10 | 8 | Lab 8 · Performance | Compiler before/after |
| 11 | 9 | Lab 9 · Accessible forms | NVDA/TalkBack script |
| 12 | 10 | Lab 10 · Same feature, four frameworks | Comparison table; **P3 starts** |
| 13 | 10 | Lab 10 (cont.) | Decision record |
| 14 | 11 | Generated-code review | **P3 due** |
| 15 | Review | P3 demo and oral defence | Final exam (AI off) |

## Working with AI in this course

- **Use AI for:** generating component variants to compare; first drafts of tests from a behaviour list; explaining a React DevTools Profiler flame chart; migration codemods (which you test). v0, Lovable, Claude Code, GitHub Copilot and Cursor all generate React. Use them, then review with the chapter 11 checklist.
- **Do without AI (drills):** the mini renderer; the effects clinic; the state inventory; an accessible combobox built from scratch in 90 minutes (a common machine-coding task); the mid-term and final.
- **Verify AI output by:** `eslint-plugin-react-hooks` with the compiler-powered `recommended` rules; Testing Library tests written from the specification, not from the code; axe plus a keyboard and screen-reader pass; React Profiler render counts; checking every API against react.dev, because models trained before 2026 do not know 19.2–19.3 APIs and may suggest removed patterns such as `forwardRef` everywhere or Create React App.
- **Where AI still fails here (collect your own evidence):** log each generated component that uses `useEffect` to derive state, uses index keys in reorderable lists, fetches in effects without cancellation, uses `div` buttons, places `'use client'` at the top of every file, or passes non-serialisable props across the server boundary. The log is graded in P3.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (10) | 25% |
| Projects P1 · P2 · P3 | 10% · 15% · 20% |
| Mid-term (AI off) | 10% |
| Final exam (AI off, 3 h, includes a 90-minute machine-coding task) and P3 defence | 20% |

**Mastery gate.** You pass when you can, with AI off, in 90 minutes, build an autocomplete with async suggestions that:
- follows the WAI-ARIA combobox pattern and has zero axe violations;
- is race-safe under random network delays;
- keeps INP under 200 ms on a 4× CPU-throttled profile with 10,000 options.

Then, in a 20-minute oral, you must place the state, effects and server–client boundary of a provided feature and defend each choice.

## Industry reality

React underpins web products at Meta and many Indian and global product companies, and React Native extends the same model to mobile ([MOB303](../../../mobile_engineering/year_3/MOB303_cross_platform_apps_flutter_and_react_native/README.md)). Next.js 16.4 (October 2026) ships React 19.3 and turns on Cache Components by default in `create-next-app`. React Router v8 (June 2026) requires React 19.2.7+ and still marks its RSC support as unstable. The December 2025 RSC vulnerability showed that frontend architecture is now also server security. Framework teams patched within days, and teams without a dependency-update routine stayed exposed. Machine-coding rounds (building a component live) are common in frontend loops; see the [market page](../../../../06_career_and_market_readiness/01_market_map/roles/FE_frontend_engineering.md).

**Interview questions from this course**

1. *Why do keys matter? What happens if you use the array index as a key in a sortable list?* A strong answer explains identity in reconciliation and shows lost input state and wrong animations after a reorder. It says when index keys are acceptable (static lists) and how to generate stable keys.
2. *Build an autocomplete (live coding).* A strong answer debounces or defers, cancels stale requests, caches results, and follows the ARIA combobox pattern (keyboard, `aria-activedescendant`, announcements). It handles empty, loading and error states, then discusses virtualisation for large lists.
3. *This component shows stale data after a prop change. Fix it.* A strong answer finds the stale closure or missing dependency. It prefers deriving state or keying the component over adding effects, and uses `useEffectEvent` for non-reactive logic.
4. *When would you use a Server Component, and what must you never do in a Server Function?* A strong answer covers bundle reduction, data locality and serialisation limits. It says to treat Server Functions as public endpoints that need authentication, authorisation and validation, and cites the 2025 RSC vulnerability as the reason to patch quickly.
5. *Our React app feels slow when typing in a filter. How do you investigate?* A strong answer measures first (Profiler, INP attribution). It then applies transitions or deferred values, virtualises, splits context, and enables the compiler, and it shows before and after numbers.

## Resources (free first)

- **Official:** [react.dev Learn](https://react.dev/learn); [You Might Not Need an Effect](https://react.dev/learn/you-might-not-need-an-effect); [Server Components reference](https://react.dev/reference/rsc/server-components); [`useEffectEvent`](https://react.dev/reference/react/useEffectEvent), [`<Activity>`](https://react.dev/reference/react/Activity), [`<ViewTransition>`](https://react.dev/reference/react/ViewTransition); [React Compiler](https://react.dev/learn/react-compiler).
- **Deep dives:** Rodrigo Pombo, [Build your own React](https://pomb.us/build-your-own-react/); Dan Abramov's [overreacted.io](https://overreacted.io/); Dominik Dorfmeister, [Practical React Query](https://tkdodo.eu/blog/practical-react-query); [patterns.dev](https://www.patterns.dev/).
- **Libraries:** [TanStack Query](https://tanstack.com/query/latest); [TanStack Virtual](https://tanstack.com/virtual/latest); [React Aria](https://react-spectrum.adobe.com/react-aria/); [Base UI](https://base-ui.com/); [Radix Primitives](https://www.radix-ui.com/primitives); [React Hook Form](https://react-hook-form.com/); [Testing Library guiding principles](https://testing-library.com/docs/guiding-principles/).
- **Alternatives:** [Vue reactivity in depth](https://vuejs.org/guide/extras/reactivity-in-depth); [Svelte docs](https://svelte.dev/docs/kit); [Solid docs](https://docs.solidjs.com/); [Angular signals](https://angular.dev/guide/signals); [TC39 Signals proposal](https://github.com/tc39/proposal-signals).
- **Accessibility patterns:** [WAI-ARIA Authoring Practices: combobox](https://www.w3.org/WAI/ARIA/apg/patterns/combobox/).

## Sources

All checked 12 Oct 2026.

- React blog: React 19.3 (9 Sep 2026) — https://react.dev/blog/2026/09/09/react-19-3 · React Compiler v1.0 (7 Oct 2025; Quest Store results) — https://react.dev/blog/2025/10/07/react-compiler-1 · The React Foundation (24 Feb 2026) — https://react.dev/blog/2026/02/24/the-react-foundation · Critical Security Vulnerability in React Server Components, CVE-2025-55182 (3 Dec 2025) — https://react.dev/blog/2025/12/03/critical-security-vulnerability-in-react-server-components · React versions — https://react.dev/versions
- Next.js 16 (21 Oct 2025) and 16.4 (6 Oct 2026) — https://nextjs.org/blog/next-16 · https://nextjs.org/blog/next-16-4
- Remix team, React Router v8 (17 Jun 2026) — https://remix.run/blog/react-router-v8
- Angular release schedule (v22, 3 Jun 2026) — https://angular.dev/reference/releases · zoneless default from v21 — https://angular.dev/guide/zoneless
- Svelte blog (SvelteKit 3, 1 Oct 2026) — https://svelte.dev/blog
- npm registry dist-tags on 12 Oct 2026 (vue latest 3.5.43, rc 3.6.0-rc.11; solid-js latest 1.9.17, next 2.0.0-rc.14; preact 11.0.1) — https://registry.npmjs.org/
- HackerRank, 2025 Developer Skills Report — https://www.hackerrank.com/reports/developer-skills-report-2025

_Last reviewed: 2026-10_
