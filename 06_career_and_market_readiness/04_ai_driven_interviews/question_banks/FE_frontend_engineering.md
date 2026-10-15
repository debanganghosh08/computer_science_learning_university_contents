# FE · Frontend Engineering: interview question bank

| Role and market | Levels | Practise with | Score with |
|---|---|---|---|
| [FE role page](../../01_market_map/roles/FE_frontend_engineering.md) | NG → Mid → Sr | [Mock kit](../how_to_run_a_mock_with_any_llm.md), especially brief 4.10 | [Rubrics](../rubrics.md) |

AI tools generate plausible UI code fast, which is why frontend interviews now probe what generated code most often gets wrong: asynchronous behaviour, state, accessibility, performance and security in the browser.

## 1. The typical loop

| Round | Duration | What it tests | AI policy you may meet | Mock brief |
|---|---|---|---|---|
| JavaScript/TypeScript fundamentals | 45 min | Event loop, closures, promises, types | AI-off | Kit 4.1 |
| Machine coding (build a component or small app) | 60–120 min | Working UI, state, edge cases, accessibility, structure | AI-off; some companies run it AI-on (Canva includes frontend roles, [Jun 2025](https://www.canva.dev/blog/engineering/yes-you-can-use-ai-in-our-interviews/)) | Kit 4.10 |
| Frontend system design | 60 min | Rendering strategy, data fetching, caching, performance budgets, accessibility | AI-off | Kit 4.3 (frontend focus) |
| DSA | 45 min | Common at product companies in India | AI-off | Kit 4.1 |
| Behavioural, often with a designer or PM | 45 min | Collaboration, user focus | AI-off | Kit 4.11 |

**India notes.** Machine coding is a signature round at many product companies; candidate reports describe 90–120 minutes with a working result expected (unconfirmed by the companies). Vanilla JavaScript versions of components (no framework) are sometimes required to test fundamentals.

## 2. How to use this bank

Answer aloud with a timer, then open the guide. For machine-coding questions, actually build them. Add `QUESTION: <text>` to brief 4.10 to run one as a mock.

## 3. Questions

### JavaScript and TypeScript fundamentals

**Q1 · NG · Predict the output and explain.**

```js
console.log('A');
setTimeout(() => console.log('B'), 0);
Promise.resolve().then(() => console.log('C'));
queueMicrotask(() => console.log('D'));
(async () => { console.log('E'); await null; console.log('F'); })();
console.log('G');
```

<details><summary>Answer guide</summary>

- **Testing:** event loop, microtasks vs macrotasks.
- **Strong answer:** `A E G C D F B`. Synchronous code runs first (A, E inside the async function until `await`, G). Microtasks run in order of queueing: C, D, then the continuation after `await` (F). The timer callback is a macrotask, so B runs after the microtask queue empties.
- **Common mistakes:** putting B before the promise callbacks; thinking `await null` continues synchronously.
- **Follow-ups:** what happens if a microtask keeps queueing microtasks (starves rendering)? Where does `requestAnimationFrame` fit?
</details>

**Q2 · NG · Closures in loops.** Why does `for (var i = 0; i < 3; i++) setTimeout(() => console.log(i))` print 3 three times, and how do you fix it?

<details><summary>Answer guide</summary>

- **Testing:** scope and closures.
- **Strong answer:** `var` is function-scoped, so all callbacks close over the same `i`, which is 3 when they run. `let` creates a new binding per iteration; alternatively pass `i` as an argument or use an IIFE. Explain closures as functions retaining access to their lexical environment.
- **Common mistakes:** "setTimeout is asynchronous" without explaining the shared binding.
- **Follow-ups:** a memory leak caused by a closure holding a large object; how to spot it in DevTools.
</details>

**Q3 · Mid · Implement `debounce(fn, wait, { leading })` with `cancel()`.**

<details><summary>Answer guide</summary>

- **Testing:** timers, `this` and argument forwarding, API design.
- **Strong answer:** keep a timer ID; on each call clear and reset it; call `fn.apply(lastThis, lastArgs)` on trailing edge; with `leading`, call immediately if no timer is pending; `cancel` clears state. Contrast with throttle (at most once per interval). Test with fake timers.
- **Common mistakes:** losing `this` or arguments; leading and trailing both firing for a single call.
- **Follow-ups:** add `flush()`; debounce in a React component without recreating it each render (`useMemo` or `useRef`).
</details>

**Q4 · Mid · Implement `Promise.all` and `Promise.allSettled`.**

<details><summary>Answer guide</summary>

- **Testing:** promise semantics.
- **Strong answer:** return a new promise; iterate inputs (accept non-promises via `Promise.resolve`); store results by index; count completions; `all` rejects on first rejection, `allSettled` records `{status, value|reason}`; empty input resolves immediately with `[]`. Note that `all` does not cancel the other operations; use `AbortController` for that.
- **Common mistakes:** pushing results in completion order; never resolving for empty input.
- **Follow-ups:** implement a concurrency-limited `mapLimit(items, 5, fn)`.
</details>

**Q5 · Mid · Type an API state.** Model loading, success with data and error with message so the UI cannot read `data` while loading.

<details><summary>Answer guide</summary>

- **Testing:** TypeScript discriminated unions, generics.
- **Strong answer:** `type State<T> = { status: 'idle' } | { status: 'loading' } | { status: 'success'; data: T } | { status: 'error'; error: string }`; narrowing with `switch (state.status)`; exhaustiveness via a `never` check. Contrast with optional fields that allow impossible combinations. Bonus: `function pick<T, K extends keyof T>(obj: T, keys: K[]): Pick<T, K>`.
- **Common mistakes:** `data?: T; error?: string; loading: boolean`.
- **Follow-ups:** runtime validation of API responses (types do not exist at runtime; use a schema validator).
</details>

**Q6 · NG · Shallow and deep copies in state updates.** Why does updating `user.address.city` in a copied object sometimes mutate the original state?

<details><summary>Answer guide</summary>

- **Testing:** references, immutability.
- **Strong answer:** spread (`{...user}`) copies one level; nested objects are shared. Copy the path you change (`{...user, address: {...user.address, city}}`) or use an immutable helper; `structuredClone` copies deeply but is costly and drops functions. Explain why frameworks rely on reference changes to detect updates.
- **Common mistakes:** `JSON.parse(JSON.stringify())` as a universal fix (loses dates, undefined, Maps).
- **Follow-ups:** how does structural sharing keep updates cheap?
</details>

### Browser and rendering

**Q7 · Mid · Layout thrashing.** A loop reads `offsetHeight` and writes `style.height` for 500 elements and the page freezes. Explain and fix.

<details><summary>Answer guide</summary>

- **Testing:** rendering pipeline (style, layout, paint, composite).
- **Strong answer:** reading a layout property after a write forces synchronous layout; alternating reads and writes forces it 500 times. Batch all reads, then all writes; or use `requestAnimationFrame`; prefer transforms and opacity (compositor-only) for animation. Use the Performance panel to confirm long tasks and forced reflows.
- **Common mistakes:** blaming JavaScript speed in general.
- **Follow-ups:** what is `content-visibility` and when does it help?
</details>

**Q8 · Mid · Core Web Vitals.** What do LCP, INP and CLS measure, and how do you improve each?

<details><summary>Answer guide</summary>

- **Testing:** performance literacy tied to users.
- **Strong answer:** LCP: time until the largest content element renders (optimise server response, preload the hero image, avoid render-blocking resources, correct image sizes). INP: responsiveness to interactions across the visit; it replaced FID as a Core Web Vital in March 2024 (break up long tasks, yield to the main thread, reduce JavaScript, avoid heavy work in handlers). CLS: unexpected layout shifts (reserve space for images and ads, avoid inserting content above existing content, font loading strategy). Measure with field data, not only lab tools.
- **Common mistakes:** only quoting Lighthouse scores.
- **Follow-ups:** INP is poor only on low-end Android phones; how do you find the cause?
</details>

**Q9 · Mid · CSR, SSR, SSG, streaming: choose for three pages.** A marketing page, a logged-in dashboard, a product page with prices that change hourly.

<details><summary>Answer guide</summary>

- **Testing:** rendering trade-offs.
- **Strong answer:** marketing: static generation with a CDN. Dashboard: client rendering or server components with client interactivity, since it is behind login and personalised (SEO irrelevant). Product page: SSR or static with incremental revalidation (cache for minutes, revalidate), prices possibly fetched client-side or streamed. Discuss time to first byte vs time to interactive, hydration cost, caching per user, and SEO.
- **Common mistakes:** one strategy for the whole site.
- **Follow-ups:** hydration mismatch errors: causes and fixes.
</details>

**Q10 · NG · CORS.** Your frontend at `app.example.com` calls `api.example.com` and the browser blocks it. Explain.

<details><summary>Answer guide</summary>

- **Testing:** same-origin policy.
- **Strong answer:** different origins (scheme, host, port); the browser enforces CORS by checking `Access-Control-Allow-Origin` and, for non-simple requests, a preflight `OPTIONS` with allowed methods and headers; credentials require explicit allowance and a specific origin (not `*`). CORS protects users' browsers, not the server; it is not authentication.
- **Common mistakes:** "disable CORS"; `Allow-Origin: *` with credentials.
- **Follow-ups:** why does the request work in curl but not in the browser?
</details>

### React and state

**Q11 · Mid · Infinite re-render.** A component calls `setFilters({...defaults})` inside `useEffect(() => {...}, [filters])`. What happens and how do you fix it?

<details><summary>Answer guide</summary>

- **Testing:** effect dependencies and identity.
- **Strong answer:** each run creates a new object, `filters` changes identity, the effect runs again: an infinite loop. Fix: derive state instead of syncing it; set state only when values differ; move defaults outside or memoise; question whether an effect is needed at all (most derived data belongs in render).
- **Common mistakes:** removing the dependency to silence the linter.
- **Follow-ups:** when do you need `useEffect` at all?
</details>

**Q12 · Mid · Using array index as `key`.** Show a bug it causes.

<details><summary>Answer guide</summary>

- **Testing:** reconciliation.
- **Strong answer:** keys identify items across renders; with index keys, deleting the first item shifts identities, so component state (an input's text, a checkbox) stays with the wrong row. Use stable IDs from data. Index keys are acceptable only for static lists that never reorder.
- **Common mistakes:** "keys are for performance only".
- **Follow-ups:** generating IDs on the client for new unsaved items.
</details>

**Q13 · Mid · Where should this state live?** Theme, the logged-in user, a list of orders from the server, and a form's draft values.

<details><summary>Answer guide</summary>

- **Testing:** state architecture.
- **Strong answer:** form draft: local component state (or a form library). Theme and user: context or a small global store (changes rarely). Orders: a server-state cache (for example TanStack Query or SWR) with caching, deduplication, revalidation and invalidation on mutation, not a hand-rolled global store. URL state for filters and pagination so links are shareable.
- **Common mistakes:** everything in one global store; server data copied into local state and going stale.
- **Follow-ups:** optimistic update for "cancel order" with rollback on failure.
</details>

### Machine coding

**Q14 · NG · Autocomplete.** Build a search box that queries an API as the user types, shows suggestions, supports arrow keys and Enter, and handles slow or failed responses.

<details><summary>Answer guide</summary>

- **Testing:** async UI correctness, accessibility.
- **Strong answer:** debounce input; cancel stale requests with `AbortController` or ignore responses whose query is not the latest (race condition); cache results per query; loading, empty and error states; keyboard navigation with `aria-activedescendant` and the combobox pattern (`role="combobox"`, `role="listbox"`, `aria-expanded`); highlight the matched text safely (no raw HTML injection); click outside to close.
- **Common mistakes:** out-of-order responses overwrite newer ones; mouse-only interaction.
- **Follow-ups:** recent searches offline; 10,000 suggestions (virtualise).
</details>

**Q15 · Mid · Virtualised list.** Render 100,000 rows of variable height smoothly.

<details><summary>Answer guide</summary>

- **Testing:** performance engineering.
- **Strong answer:** render only visible rows plus an overscan buffer inside a container whose height equals the total; compute visible range from scroll position; variable heights need measurement and a cache of positions (estimated until measured, prefix sums for lookup); keep keys stable; handle scroll anchoring when heights change. Mention accessibility trade-offs (screen readers and find-in-page see only rendered rows).
- **Common mistakes:** rendering all rows with `display: none`; recomputing all positions on every scroll event.
- **Follow-ups:** infinite loading at the bottom; jump to row 50,000.
</details>

**Q16 · Mid · Accessible modal dialog.**

<details><summary>Answer guide</summary>

- **Testing:** accessibility depth.
- **Strong answer:** use the native `<dialog>` element with `showModal()` where supported, or `role="dialog"` with `aria-modal="true"` and `aria-labelledby`; move focus into the dialog on open, trap focus while open, close on Escape, return focus to the trigger on close; make the background inert; prevent background scroll. Test with keyboard only and a screen reader.
- **Common mistakes:** a `div` overlay with no focus management.
- **Follow-ups:** nested dialogs; a dialog that opens from a route change.
</details>

**Q17 · Mid · File explorer tree.** Folders and files with expand/collapse, add, rename and delete, persisted locally.

<details><summary>Answer guide</summary>

- **Testing:** recursive UI, data modelling.
- **Strong answer:** normalised state (`byId` map plus `childrenIds`) rather than deeply nested objects, making updates O(1) and immutable updates simple; recursive rendering component; validation (duplicate names in a folder); keyboard support following the tree-view pattern (`role="tree"`, `treeitem`, arrow keys); persistence to `localStorage` with versioning.
- **Common mistakes:** deep nested state with mutation; deleting a folder leaves orphans.
- **Follow-ups:** drag-and-drop move with cycle prevention (cannot move a folder into its own descendant).
</details>

### Frontend system design

**Q18 · Mid · News feed frontend.**

<details><summary>Answer guide</summary>

- **Testing:** end-to-end frontend architecture.
- **Strong answer:** cursor-based pagination with infinite scroll and virtualisation; server-state cache with normalised posts; optimistic likes with rollback; image strategy (responsive sizes, lazy loading, placeholders to avoid layout shift); new-posts indicator instead of shifting content; prefetching; offline and error states; performance budget (JavaScript size, LCP target); analytics without blocking the main thread.
- **Common mistakes:** refetching the whole feed after every action.
- **Follow-ups:** real-time updates (WebSocket vs polling); accessibility of an infinite feed.
</details>

**Q19 · Sr · A design system for 30 product teams.**

<details><summary>Answer guide</summary>

- **Testing:** platform thinking.
- **Strong answer:** design tokens (colour, spacing, type) as the source of truth, exported to CSS variables and platforms; accessible primitives with documented keyboard behaviour; theming including dark mode; semantic versioning and codemods for breaking changes; visual regression and accessibility tests in CI; contribution model and governance; adoption metrics; bundle size per component (tree-shaking).
- **Common mistakes:** a component dump with no versioning or ownership.
- **Follow-ups:** one team forks a component; how do you bring them back?
</details>

**Q20 · Sr · Collaborative whiteboard frontend.**

<details><summary>Answer guide</summary>

- **Testing:** rendering technology and sync choices.
- **Strong answer:** canvas (or WebGL) for thousands of shapes vs DOM/SVG for fewer, more accessible elements; a scene graph with spatial indexing for hit-testing; CRDT-based document sync (offline friendly) over WebSocket; presence and cursors throttled; undo per user; viewport culling; export; accessibility alternatives (an outline view).
- **Common mistakes:** sending full document state on every change.
- **Follow-ups:** 200 concurrent users on one board; memory on low-end tablets.
</details>

**Q21 · Mid · Checkout page frontend.**

<details><summary>Answer guide</summary>

- **Testing:** reliability on a money path.
- **Strong answer:** minimal JavaScript and third-party scripts on the page; payment fields in the provider's iframe or hosted fields (keeps card data off your origin); idempotent submit (disable button, idempotency key); clear error and retry states; handling the redirect or 3-D Secure challenge return; address validation; performance budget; analytics that do not block; accessible form errors.
- **Common mistakes:** trusting client-side success; double submits.
- **Follow-ups:** the payment provider's script fails to load; what does the user see?
</details>

### Security

**Q22 · Mid · Where does cross-site scripting (XSS) still come from in a React app, and how do you defend against it?**

<details><summary>Answer guide</summary>

- **Testing:** defensive browser security.
- **Strong answer:** React escapes text by default, so risks concentrate in `dangerouslySetInnerHTML`, user-controlled `href` values with dangerous URL schemes, rendering server-provided HTML, third-party scripts, and template injection outside React. Defences: avoid raw HTML or sanitise with a maintained sanitiser; validate URL schemes against an allow-list; Content Security Policy (script sources, no inline scripts); Trusted Types where supported; Subresource Integrity for third-party scripts.
- **Common mistakes:** "React prevents XSS completely".
- **Follow-ups:** how do you roll out a strict CSP without breaking the site (report-only mode first)?
</details>

**Q23 · Mid · Where do you store the session token?**

<details><summary>Answer guide</summary>

- **Testing:** authentication trade-offs.
- **Strong answer:** `HttpOnly`, `Secure`, `SameSite` cookies keep tokens away from JavaScript (limits XSS token theft) but need CSRF consideration (`SameSite=Lax` or `Strict`, CSRF tokens for state-changing requests). `localStorage` is readable by any script on the origin. Short-lived access tokens with refresh rotation; logout invalidation server-side.
- **Common mistakes:** "JWT in localStorage is standard, so it is fine".
- **Follow-ups:** cross-subdomain authentication; mobile web views.
</details>

### Testing

**Q24 · Mid · Testing strategy for a React application.**

<details><summary>Answer guide</summary>

- **Testing:** test pyramid judgement.
- **Strong answer:** unit tests for pure logic; component tests that use the UI as a user would (Testing Library: query by role and label); a few end-to-end tests for critical journeys (Playwright or Cypress) against a stable test environment; visual regression for the design system; automated accessibility checks (axe) plus manual keyboard checks; mock the network at the boundary (for example Mock Service Worker). Avoid testing implementation details.
- **Common mistakes:** snapshot tests of everything; E2E for every edge case.
- **Follow-ups:** E2E tests are flaky; top three causes.
</details>

### AI-era review

**Q25 · Mid · Review this AI-generated component.**

```jsx
function Clock({ items }) {
  const [seconds, setSeconds] = useState(0);
  useEffect(() => {
    setInterval(() => setSeconds(seconds + 1), 1000);
  }, []);
  return (
    <div>
      <div onClick={() => refresh()}>Refresh</div>
      <p>{seconds}s</p>
      <ul>{items.map(i => <li>{i.name}</li>)}</ul>
    </div>
  );
}
```

<details><summary>Answer guide</summary>

- **Testing:** verifying generated UI code.
- **Strong answer:** (1) stale closure: the interval captures `seconds = 0`, so it shows 1 forever; use `setSeconds(s => s + 1)`. (2) No cleanup: the interval keeps running after unmount (and duplicates in development Strict Mode); return `() => clearInterval(id)`. (3) A clickable `div` is not keyboard-accessible or announced as a button; use `<button type="button">`. (4) Missing `key` on list items; use a stable ID. Then write a test with fake timers.
- **Common mistakes:** spotting only the missing key (the linter's warning).
- **Follow-ups:** the interval drifts over an hour; how do you show accurate elapsed time (compute from a start timestamp)?
</details>

**Q26 · Sr · A tool generated a whole page from a design screenshot. What do you check before it ships?**

<details><summary>Answer guide</summary>

- **Testing:** quality gates for generated UI.
- **Strong answer:** semantic HTML and heading structure; keyboard and screen-reader behaviour; colour contrast; responsive behaviour across breakpoints; use of the design system's tokens and components instead of hard-coded values; performance (bundle size, images, layout shift); states the screenshot did not show (loading, empty, error, long text, right-to-left or Hindi text rendering); security of any raw HTML; tests. Generated code is a draft; the owner signs off on these properties.
- **Common mistakes:** pixel comparison as the only check.
- **Follow-ups:** how would you automate these checks in CI?
</details>

### Behavioural

**Q27 · Mid · Tell me about pushing back on a design for accessibility or performance reasons.**

<details><summary>Answer guide</summary>

- **Testing:** collaboration with design and product.
- **Strong answer:** the design and the concrete problem (for example a carousel with autoplay and no pause, or a 4 MB hero video); evidence you brought (an accessibility audit, a field performance measurement, user impact); the alternative you proposed with the designer; the outcome and what changed in the team's process (for example an accessibility checklist in design reviews).
- **Common mistakes:** "I just implemented it as designed"; or overriding the designer without discussion.
- **Follow-ups:** what if the PM insisted on shipping as is?
</details>

## Sources

- Canva Engineering (11 Jun 2025): https://www.canva.dev/blog/engineering/yes-you-can-use-ai-in-our-interviews/
- web.dev, *Interaction to Next Paint becomes a Core Web Vital on March 12* (checked October 2026): https://web.dev/blog/inp-cwv-march-12
- WAI-ARIA Authoring Practices Guide (combobox, dialog, tree view patterns): https://www.w3.org/WAI/ARIA/apg/
- MDN Web Docs on CORS and Content Security Policy: https://developer.mozilla.org/
- Loop structure: [FE role page](../../01_market_map/roles/FE_frontend_engineering.md).

_Last reviewed: 2026-10_
