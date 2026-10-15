# SWE · Software Engineering: interview question bank

| Role and market | Levels | Practise with | Score with |
|---|---|---|---|
| [SWE role page](../../01_market_map/roles/SWE_software_engineering.md) | Intern/new grad (NG) → mid-level (Mid) → senior (Sr) | [Mock kit](../how_to_run_a_mock_with_any_llm.md) | [Rubrics](../rubrics.md) |

General software engineering loops are the template most other engineering loops vary from: data structures and algorithms, design at two zoom levels, testing and debugging, and increasingly a round where an AI assistant is allowed and your judgement is what is graded.

## 1. The typical loop

| Round | Duration | What it tests | AI policy you may meet | Mock brief |
|---|---|---|---|---|
| Online assessment | 60–120 min | 2–4 DSA problems on HackerRank, CodeSignal, HackerEarth or similar; auto-graded | Usually AI-off and proctored | [Day 1 OA prompt](../simulation_days.md#1-day-1-new-grad-software-engineer-at-a-product-company-india) |
| Coding (1–2 rounds) | 45–60 min | Problem solving, clean code, testing, communication | Usually AI-off | Kit 4.1 |
| AI-assisted coding | 60 min | Working in a multi-file codebase with an assistant; catching its errors | AI-on with a named tool (Canva, Meta, Google pilot; see [README](../README.md#6-company-policies-allowed-required-or-banned)) | Kit 4.2 |
| Low-level design / machine coding | 60–120 min | Classes, interfaces, extensibility; in India often a runnable "machine coding" build | Usually AI-off | Kit 4.10 (backend variant) |
| System design | 45–60 min | Mid-level and above: architecture, data, trade-offs | AI-off | Kit 4.3 |
| Behavioural / hiring manager | 45 min | Ownership, conflict, learning, AI judgement | AI-off | Kit 4.11, 4.12 |

**India notes.** Product companies and global capability centres commonly add a machine-coding round (candidate reports describe 90–120 minutes to build working, modular code, then a review; formats vary and are not confirmed by the companies). Services firms often start with an aptitude and coding test, sometimes at a supervised centre, such as TCS iON's NQT ([TCS iON](https://www.tcsion.com/hub/national-qualifier-test/)).

**Level differences.** New grads: mostly DSA plus one design-flavoured round. Mid-level: LLD plus system design carry more weight. Senior: system design, a project deep dive and leadership stories decide the level.

## 2. How to use this bank

Say your answer aloud with a timer before opening the guide. To run a question as a mock, add `QUESTION: <text>` to the matching brief in the [mock kit](../how_to_run_a_mock_with_any_llm.md). Tags: **NG**, **Mid**, **Sr** show the lowest level at which the question is common.

## 3. Questions

### Coding (AI-off)

**Q1 · NG · Common free time.** Given two people's busy intervals for a day (each list unsorted, intervals may overlap), return all free slots of at least D minutes between 09:00 and 18:00.

<details><summary>Answer guide</summary>

- **Testing:** interval reasoning, sorting, boundary handling.
- **Strong answer:** merge both lists into one, sort by start (O(n log n)), merge overlaps, then walk gaps between the day start, merged intervals and day end, keeping gaps ≥ D. Clarify whether intervals are half-open and whether touching intervals (10:00–11:00, 11:00–12:00) leave a zero gap. Test: empty calendars, one interval covering the whole day, intervals outside working hours.
- **Common mistakes:** forgetting the gap before the first and after the last interval; not clipping to working hours; mutating input.
- **Follow-ups:** k people instead of two (heap merge of k sorted lists, O(n log k)); calendars in different time zones.
</details>

**Q2 · NG · Build order.** Services declare dependencies (`A needs B`). Return a valid start order or report a cycle and the services in it.

<details><summary>Answer guide</summary>

- **Testing:** graph modelling, topological sort, cycle detection.
- **Strong answer:** Kahn's algorithm with in-degree counts and a queue, O(V + E); if output size < V, a cycle exists. To report the cycle, run DFS with three colours and reconstruct from the back edge. Discuss deterministic output (sorted queue) if the order must be stable.
- **Common mistakes:** edges in the wrong direction; ignoring services with no dependencies; recursion depth on long chains in Python.
- **Follow-ups:** start independent services in parallel waves (levels of Kahn's algorithm); dependencies change at runtime.
</details>

**Q3 · NG · Top-k terms.** Given a list of search terms, return the k most frequent; ties broken alphabetically.

<details><summary>Answer guide</summary>

- **Testing:** hashing, heaps, custom ordering.
- **Strong answer:** count with a hash map; keep a min-heap of size k keyed by (count, reverse alphabetical) so the weakest candidate is on top, O(n log k); or sort all distinct terms when k is close to the number of distinct terms. Explain the tie comparator carefully and test it.
- **Common mistakes:** comparator inverted for ties; O(n log n) sort described as O(n); not handling k larger than distinct terms.
- **Follow-ups:** a stream too large for memory (Count-Min Sketch plus a heap; approximate); top-k over a sliding hour.
</details>

**Q4 · Mid · Versioned config store.** Implement `set(key, value, ts)` and `get(key, ts)` returning the value with the largest timestamp ≤ ts. Timestamps for a key arrive increasing.

<details><summary>Answer guide</summary>

- **Testing:** choosing a data structure for the access pattern.
- **Strong answer:** map from key to a list of (ts, value) appended in order; `get` uses binary search for the rightmost ts ≤ query, O(log n). If timestamps can arrive out of order, use a balanced tree or sorted container. Discuss memory (compaction of old versions) and what `get` returns before the first version.
- **Common mistakes:** off-by-one in the binary search; linear scan; ignoring equal timestamps.
- **Follow-ups:** support deletes as tombstones; make it safe for concurrent readers and one writer.
</details>

**Q5 · Mid · Busiest stretch.** In a stream of log lines with user IDs, find the longest contiguous stretch containing at most k distinct users.

<details><summary>Answer guide</summary>

- **Testing:** sliding window with counts.
- **Strong answer:** two pointers with a hash map of counts; extend right, shrink left while distinct > k; track the best length. O(n) time, O(k) space. Test k = 0, all same user, k larger than distinct users.
- **Common mistakes:** removing a key only when count hits zero is forgotten, so distinct is overcounted; O(n·k) rescans.
- **Follow-ups:** return the stretch itself; the stream is unbounded and you need the answer over the last hour only.
</details>

**Q6 · Mid · Grid with breakable walls.** Shortest path from top-left to bottom-right in a grid where you may remove at most k walls.

<details><summary>Answer guide</summary>

- **Testing:** BFS with augmented state.
- **Strong answer:** BFS over states (row, col, walls_used), visited per state, O(R·C·k). Optimisation: keep for each cell the minimum walls used to reach it and skip worse states. If k ≥ R + C − 2, the Manhattan distance is the answer immediately.
- **Common mistakes:** visited only by cell, which wrongly prunes paths with fewer removals; DFS instead of BFS.
- **Follow-ups:** walls have different removal costs (Dijkstra on the state graph); return the path.
</details>

**Q7 · NG · Expression evaluator.** Evaluate a string with integers, `+ - * /` (integer division toward zero) and parentheses.

<details><summary>Answer guide</summary>

- **Testing:** parsing, stacks or recursion, precedence.
- **Strong answer:** either recursive descent (expression → term → factor) or two stacks (shunting-yard). Handle unary minus, spaces and multi-digit numbers. State division semantics explicitly; Python's `//` floors, so use `int(a / b)` or adjust.
- **Common mistakes:** precedence wrong for `2-3-4` (left associativity); unary minus after `(`; division rounding.
- **Follow-ups:** add variables and a symbol table; report a helpful error position for malformed input.
</details>

### Code review and AI-generated code

**Q8 · NG · Review this AI-generated function.** An assistant produced this for "index of the first element ≥ target in a sorted list, or `len(nums)` if none". Would you accept it?

```python
def first_at_least(nums, target):
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid
    return lo
```

<details><summary>Answer guide</summary>

- **Testing:** verification of plausible code with boundary tests.
- **Strong answer:** test the boundaries: `[1,2,3]` with target 5 returns 2, not 3, because `hi` starts at `len − 1` so the "none" case can never be returned. Fix: `hi = len(nums)` and keep `while lo < hi`. Then re-test: empty list → 0, target below all → 0, duplicates → first occurrence, target above all → len. Mention `bisect.bisect_left` as the library equivalent.
- **Common mistakes:** reading it, finding it "looks right", approving without running boundary cases.
- **Follow-ups:** write a property-based test comparing it with a linear scan; what changes for "last element ≤ target"?
</details>

**Q9 · Mid · The copilot suggested a retry decorator. Would you ship it?**

```python
@retry(times=3, backoff_seconds=0)
def create_payment(order_id, amount_paise):
    return http.post("/payments", json={"order_id": order_id, "amount": amount_paise})
```

<details><summary>Answer guide</summary>

- **Testing:** distributed-systems judgement about AI suggestions.
- **Strong answer:** not as is. A POST that timed out may have succeeded, so a retry can charge twice; add an idempotency key (generated once per logical payment and sent as a header the server deduplicates on). Retry only on retryable failures (timeouts, connection errors, 502/503/504, 429 respecting `Retry-After`), never on 4xx validation errors; exponential backoff with jitter and a cap; total deadline; log attempts. Confirm the server honours idempotency keys.
- **Common mistakes:** only adding backoff; assuming a timeout means failure.
- **Follow-ups:** how do you test this (fault injection, a fake server that commits then times out)? What metrics show retry storms?
</details>

**Q10 · Mid · Thread safety in a generated class.** This counter is called from many request threads. Review it.

```java
class RequestCounter {
    private final Map<String, Integer> counts = new HashMap<>();
    public void hit(String user) { counts.put(user, counts.getOrDefault(user, 0) + 1); }
    public int get(String user) { return counts.getOrDefault(user, 0); }
}
```

<details><summary>Answer guide</summary>

- **Testing:** concurrency fundamentals, code review depth.
- **Strong answer:** `HashMap` is not thread-safe; concurrent puts can lose updates and corrupt internal state. The read-modify-write is a check-then-act race even with a synchronised map. Fix: `ConcurrentHashMap` with `merge(user, 1, Integer::sum)`, or `LongAdder` values for heavy contention. Also flag unbounded growth (one entry per user forever): add eviction or time windows. Suggest a concurrent test that hammers `hit` and asserts the total.
- **Common mistakes:** "add `synchronized`" without discussing contention; missing the memory issue.
- **Follow-ups:** counts must be per minute; counts must be shared across 10 servers.
</details>

**Q11 · Sr · Agents open 40 pull requests a week in your repo. Design the review policy.**

<details><summary>Answer guide</summary>

- **Testing:** engineering leadership for AI-generated change.
- **Strong answer:** classify changes by risk (documentation, tests, dependency bumps, business logic, security-sensitive paths, migrations); require human owner approval proportional to risk, using code-owner files; small PRs with a description of intent and test evidence; mandatory CI (tests, static analysis, secret scanning, licence checks); no auto-merge on risky paths; track metrics (revert rate, incidents linked to AI PRs, review time). Make the human who triggers the agent accountable for the change.
- **Common mistakes:** either "ban it" or "trust CI"; no metrics to adjust the policy.
- **Follow-ups:** a reviewer rubber-stamps AI PRs; how do you detect and fix it? How do you keep juniors learning?
</details>

### AI-assisted coding

**Q12 · Mid · You get a 3,000-line unfamiliar repository and a feature request, with an AI assistant allowed. Walk me through your first ten minutes.**

<details><summary>Answer guide</summary>

- **Testing:** orientation, planning, sensible delegation.
- **Strong answer:** read the README and run the tests first (baseline green or not); find the entry point and trace one request; ask the assistant to summarise module responsibilities, then verify by reading the key files; restate the feature as acceptance criteria; identify the files to change and the risky part; plan to write a failing test first; delegate boilerplate, keep business rules and edge cases for yourself.
- **Common mistakes:** pasting the whole task into the assistant immediately; not running existing tests.
- **Follow-ups:** the assistant's summary is wrong about one module; how do you notice? Tests are already failing on main: what do you do?
</details>

### Low-level design and machine coding

**Q13 · NG · Parking lot.** Design classes for a multi-floor parking lot with different vehicle and spot sizes and hourly pricing.

<details><summary>Answer guide</summary>

- **Testing:** object modelling, separation of concerns, extensibility.
- **Strong answer:** entities `ParkingLot`, `Floor`, `Spot` (size, occupied), `Vehicle` (type), `Ticket` (entry time, spot), `PricingStrategy` interface, `SpotAllocationStrategy` interface; a service that issues and closes tickets. Pricing and allocation as strategies so new rules do not change existing classes. Handle concurrency on spot assignment (lock per floor or atomic compare-and-set).
- **Common mistakes:** a god class; pricing logic in `Vehicle`; deep inheritance trees for each vehicle type.
- **Follow-ups:** add electric-vehicle charging spots; add monthly passes.
</details>

**Q14 · Mid · In-memory pub/sub.** Topics, publishers, subscribers with their own consumption speed, at-least-once delivery, and an offset per subscriber.

<details><summary>Answer guide</summary>

- **Testing:** concurrency design, delivery semantics.
- **Strong answer:** each topic is an append-only list; each subscriber has an offset and a worker thread; deliver, then advance offset only on acknowledgement (at-least-once, so handlers must be idempotent); retry with backoff and a dead-letter list after N failures; reset offset to replay. Use per-topic locks or lock-free append; bounded memory with retention.
- **Common mistakes:** advancing offset before the handler succeeds (that is at-most-once); one global lock.
- **Follow-ups:** ordering per key; slow subscriber causing memory growth.
</details>

**Q15 · Mid · Elevator controller.** Design the control logic for a bank of 4 elevators in a 20-floor building.

<details><summary>Answer guide</summary>

- **Testing:** state machines, scheduling trade-offs.
- **Strong answer:** each car is a state machine (idle, moving up, moving down, doors open, maintenance); requests are hall calls (floor, direction) and car calls; a dispatcher assigns hall calls by estimated time of arrival; the SCAN (elevator) algorithm within a car. Separate the dispatcher strategy so it can change (energy saving, peak mode). Tests: simulation with timestamps.
- **Common mistakes:** nearest-car only, which starves far floors; no direction handling.
- **Follow-ups:** morning peak mode; one car fails mid-trip.
</details>

### Testing

**Q16 · NG · How would you test a function that parses dates typed by users?**

<details><summary>Answer guide</summary>

- **Testing:** test design technique.
- **Strong answer:** equivalence classes (valid formats, invalid formats), boundaries (29 Feb in leap and non-leap years, 31st in 30-day months, year limits), locale ambiguity (`03/04/2026`), whitespace and Unicode digits, time zones if times are included, very long input. Table-driven tests; a property test that format(parse(x)) round-trips. Decide and document behaviour for ambiguous input.
- **Common mistakes:** only happy-path tests; no decision on ambiguous formats.
- **Follow-ups:** how would you find inputs you did not think of (fuzzing)? How do you test daylight-saving transitions?
</details>

**Q17 · Mid · A test fails about 1 run in 50 in CI. How do you investigate?**

<details><summary>Answer guide</summary>

- **Testing:** debugging non-determinism.
- **Strong answer:** reproduce by running it in a loop locally and in CI with the same seed and parallelism; classify the cause: ordering dependence between tests, shared state, time (`now()`, time zones), concurrency races, network or external services, random data, resource limits. Add logging around the failure; fix the cause (inject a clock, isolate state, await conditions instead of sleeps). Quarantine with a ticket and owner only as a temporary step.
- **Common mistakes:** adding retries to the test; increasing timeouts blindly.
- **Follow-ups:** how do you measure flakiness across the whole suite? The flaky test is in code an AI assistant wrote; does that change anything?
</details>

### System design

**Q18 · Mid · URL shortener with click analytics.**

<details><summary>Answer guide</summary>

- **Testing:** classic design fundamentals.
- **Strong answer:** requirements (custom aliases, expiry, analytics freshness); estimates (for example 100M new URLs a month, 100:1 read:write); key generation (base62 of a counter allocated in ranges per server, or random with collision check); key-value store for code → URL; cache hot codes; redirects return 301 vs 302 (302 keeps analytics accurate); clicks written asynchronously to a queue and aggregated in a columnar store; abuse prevention (malware URL scanning, rate limits).
- **Common mistakes:** hashing long URLs and truncating without handling collisions; synchronous analytics writes on the redirect path.
- **Follow-ups:** a celebrity link gets 50,000 clicks a second; GDPR deletion requests.
</details>

**Q19 · Mid · Feature-flag service.** Teams roll out features to percentages of users, by country, or to a list of user IDs, with instant kill switches.

<details><summary>Answer guide</summary>

- **Testing:** read-heavy design, consistency trade-offs, safety.
- **Strong answer:** flags stored in a strongly consistent store with audit history; clients (SDKs) cache rules locally and evaluate in-process for latency; updates pushed via streaming or polled every few seconds; deterministic bucketing by hashing (flag key + user ID) so users stay in the same bucket; kill switch has the shortest propagation path; safe defaults when the service is unreachable.
- **Common mistakes:** a network call per flag evaluation; random bucketing per request.
- **Follow-ups:** how do you clean up stale flags? How would you link flags to experiment analysis?
</details>

**Q20 · Sr · Collaborative document editing.**

<details><summary>Answer guide</summary>

- **Testing:** deep trade-offs, consistency models.
- **Strong answer:** compare operational transformation (central server orders operations; simpler with a server, used by many editors) with CRDTs (merge without coordination; good for offline; metadata overhead); presence and cursors over WebSockets; a document session pinned to one server (or partition) for ordering; snapshots plus operation logs; permissions per document; offline edits and reconciliation; undo per user.
- **Common mistakes:** last-write-wins for the whole document; ignoring offline.
- **Follow-ups:** 500 simultaneous editors on one document; version history and restore.
</details>

**Q21 · Sr · Extract a module from a monolith into a service without downtime.**

<details><summary>Answer guide</summary>

- **Testing:** migration strategy, risk management.
- **Strong answer:** strangler-fig pattern: define the interface inside the monolith first; route calls through it; build the service behind it; dual-run (shadow reads, compare results); migrate data with change data capture or dual writes plus reconciliation; switch traffic gradually with a flag; keep rollback possible until confidence; remove old code. Discuss ownership of the data, transactions that used to be local (now sagas or outbox), and latency budgets.
- **Common mistakes:** big-bang cut-over; shared database between the monolith and the new service indefinitely.
- **Follow-ups:** how do you know the migration is done? A cross-module transaction exists today; what replaces it?
</details>

### Debugging and production

**Q22 · Mid · A service's memory grows steadily until it is killed every 6 hours. Diagnose.**

<details><summary>Answer guide</summary>

- **Testing:** systematic production debugging.
- **Strong answer:** confirm with metrics (heap vs off-heap vs native); correlate with traffic and deploys; take heap snapshots at two points and diff retained objects; common causes: unbounded caches or maps, listeners never removed, thread-locals, connection leaks, large buffers, native memory in libraries. Mitigate meanwhile (rolling restarts, memory limit alerts). Fix and add a test or metric that detects regrowth.
- **Common mistakes:** raising the memory limit as the fix; guessing without snapshots.
- **Follow-ups:** the leak only happens in production; how do you profile safely there?
</details>

**Q23 · NG · Code works on your laptop but fails in CI. List likely causes and how you check each.**

<details><summary>Answer guide</summary>

- **Testing:** environment awareness.
- **Strong answer:** dependency versions (lock files), environment variables and secrets, file paths and case sensitivity (macOS vs Linux), time zone and locale, test order and parallelism, missing services (database), network access, resource limits, tests relying on local state. Check by reproducing the CI container locally and diffing environments.
- **Common mistakes:** re-running until green.
- **Follow-ups:** how do you make builds reproducible?
</details>

### Fundamentals

**Q24 · Mid · Two threads transfer money between accounts and the system sometimes freezes. Explain and fix.**

<details><summary>Answer guide</summary>

- **Testing:** deadlock understanding.
- **Strong answer:** a deadlock: thread 1 locks A then waits for B, thread 2 locks B then waits for A. The four Coffman conditions (mutual exclusion, hold and wait, no preemption, circular wait). Fix by global lock ordering (always lock the lower account ID first), or try-lock with timeout and retry, or a single-writer design. In a database, use one transaction and let the database detect deadlocks, with retry.
- **Common mistakes:** one global lock without discussing throughput.
- **Follow-ups:** how would you detect deadlocks in production (thread dumps)?
</details>

**Q25 · Mid · Inventory: optimistic or pessimistic locking?** Flash sale, 1,000 units, 50,000 buyers in a minute.

<details><summary>Answer guide</summary>

- **Testing:** concurrency control under contention.
- **Strong answer:** optimistic locking (version column, retry on conflict) works when conflicts are rare; under heavy contention on one row it causes retry storms. Alternatives: atomic conditional update (`UPDATE ... SET stock = stock - 1 WHERE id = ? AND stock > 0`), pre-sharded stock counters, a reservation queue, or a token bucket of units in an in-memory store with durable confirmation. Add holds with expiry for checkout.
- **Common mistakes:** read-then-write without a condition (oversell).
- **Follow-ups:** payment fails after reservation; how do units return?
</details>

**Q26 · NG · You force-pushed and overwrote a teammate's commits on a shared branch. Recover.**

<details><summary>Answer guide</summary>

- **Testing:** Git internals, calm recovery.
- **Strong answer:** tell the team immediately; the teammate's local clone or `git reflog` (theirs or the server's, if available) has the old commit; find the lost commit hash, create a branch at it, and merge or cherry-pick the lost commits; push normally. Prevent with branch protection and `--force-with-lease`.
- **Common mistakes:** more force-pushing; not communicating.
- **Follow-ups:** explain rebase vs merge and when each is appropriate.
</details>

### Behavioural (software-engineering specific)

**Q27 · Mid · Tell me about a design decision you would revisit.**

<details><summary>Answer guide</summary>

- **Testing:** reflective technical judgement.
- **Strong answer:** the decision and context; why it was reasonable then; the signals that it was wrong (incidents, slowed delivery, cost); what you would do now and how you would migrate; what principle you took away.
- **Common mistakes:** a decision someone else made; no consequence described.
- **Follow-ups:** did you push for the change? What stopped it?
</details>

**Q28 · Sr · Refactor or rewrite? Walk me through a real decision.**

<details><summary>Answer guide</summary>

- **Testing:** pragmatism, risk management.
- **Strong answer:** default to incremental refactoring behind tests; consider a rewrite only when the platform is obsolete, the domain changed fundamentally, or the cost of change is measurably extreme; even then, migrate incrementally (strangler fig). Discuss characterisation tests, business continuity and team capacity. Mention that AI tools make large mechanical refactors cheaper but do not reduce the verification burden.
- **Common mistakes:** rewrite enthusiasm with no migration plan.
- **Follow-ups:** how did you get buy-in? What did it cost?
</details>

## Sources

- Company AI-interview policies and dates: [section README](../README.md#6-company-policies-allowed-required-or-banned) and its sources (checked October 2026).
- TCS iON National Qualifier Test page (checked October 2026): https://www.tcsion.com/hub/national-qualifier-test/
- Loop structure: [SWE role page](../../01_market_map/roles/SWE_software_engineering.md).

_Last reviewed: 2026-10_
