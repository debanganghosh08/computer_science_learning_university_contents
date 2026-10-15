# DSA for hiring · Pattern 17 · Weighted shortest paths

| Theory first | Time | Problems | Must-do |
|---|---|---|---|
| [CS201](../../../02_year_2_core_computer_science/semester_3/CS201_algorithms_and_complexity/README.md) chapter 7 (Dijkstra, Bellman-Ford, Floyd-Warshall) | ~9 hours | 10 | 2 |

When moves cost different amounts, BFS layers no longer equal distances. Pick the algorithm from the edge weights and the constraint:

| Weights and constraint | Algorithm | Time |
|---|---|---|
| all equal | BFS ([Pattern 14](14_graphs_bfs_dfs.md)) | O(V + E) |
| only 0 and 1 | 0-1 BFS with a deque | O(V + E) |
| non-negative | Dijkstra with a binary heap | O((V + E) log V) |
| negative allowed, or "at most k edges" | Bellman-Ford (k + 1 rounds for k stops) | O(k · E) |
| all pairs, V ≤ ~400 | Floyd-Warshall | O(V³) |
| cost of a path = its **maximum** edge (bottleneck) | Dijkstra with `max` instead of `+` | O((V + E) log V) |

## Recognise it

| When you see… | Think… |
|---|---|
| "minimum time/cost/effort from A to B", different costs per move | Dijkstra |
| "signal reaches all nodes; how long?" | Dijkstra from the source, answer = max distance |
| "with at most k stops/edges" | Bellman-Ford limited to k + 1 rounds, or Dijkstra over (node, stops) |
| "maximum probability path" | Dijkstra maximising a product (all factors ≤ 1) |
| "minimise the largest step along a path" | bottleneck Dijkstra, or binary search + BFS, or union-find |
| "number of shortest paths" | Dijkstra that also counts ties |
| grid where some moves are free and others cost 1 | 0-1 BFS |
| "every edge exactly once" | Eulerian path (Hierholzer), not a shortest path |

## Core templates

**Dijkstra with lazy deletion.** The heap may hold stale entries; skip any entry whose distance is larger than the best known.

```python
import heapq
from collections import deque, defaultdict


def dijkstra(n, edges, src):                  # edges: (u, v, w), w >= 0, directed
    adj = [[] for _ in range(n)]
    for u, v, w in edges:
        adj[u].append((v, w))
    dist = [float("inf")] * n
    dist[src] = 0
    heap = [(0, src)]
    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue                          # stale entry
        for v, w in adj[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(heap, (nd, v))
    return dist


def network_delay_time(times, n, k):          # nodes 1..n
    dist = dijkstra(n + 1, times, k)[1:]
    best = max(dist)
    return -1 if best == float("inf") else best
```

**Bottleneck Dijkstra (Path With Minimum Effort).** Path cost = largest single step; `max` is monotone along a path, so Dijkstra still works.

```python
def minimum_effort_path(heights):
    m, n = len(heights), len(heights[0])
    best = [[float("inf")] * n for _ in range(m)]
    best[0][0] = 0
    heap = [(0, 0, 0)]
    while heap:
        e, r, c = heapq.heappop(heap)
        if (r, c) == (m - 1, n - 1):
            return e
        if e > best[r][c]:
            continue
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < m and 0 <= nc < n:
                ne = max(e, abs(heights[nr][nc] - heights[r][c]))
                if ne < best[nr][nc]:
                    best[nr][nc] = ne
                    heapq.heappush(heap, (ne, nr, nc))
```

**Bellman-Ford limited to k + 1 edges.** Relax from a *copy* of the previous round, so one round adds at most one edge.

```python
def find_cheapest_price(n, flights, src, dst, k):
    dist = [float("inf")] * n
    dist[src] = 0
    for _ in range(k + 1):
        prev = dist[:]                        # distances using at most i edges
        for u, v, w in flights:
            if prev[u] + w < dist[v]:
                dist[v] = prev[u] + w
    return -1 if dist[dst] == float("inf") else dist[dst]
```

**0-1 BFS.** A 0-cost move goes to the front of the deque, a 1-cost move to the back.

```python
def minimum_obstacles(grid):                  # cost 1 to enter a cell with an obstacle
    m, n = len(grid), len(grid[0])
    dist = [[float("inf")] * n for _ in range(m)]
    dist[0][0] = 0
    dq = deque([(0, 0)])
    while dq:
        r, c = dq.popleft()
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < m and 0 <= nc < n:
                w = grid[nr][nc]
                if dist[r][c] + w < dist[nr][nc]:
                    dist[nr][nc] = dist[r][c] + w
                    if w == 0:
                        dq.appendleft((nr, nc))
                    else:
                        dq.append((nr, nc))
    return dist[m - 1][n - 1]
```

**Floyd-Warshall.** `k` must be the outer loop: after iteration k, paths may use intermediate nodes 0..k.

```python
def floyd_warshall(n, edges):                 # undirected, weighted
    d = [[float("inf")] * n for _ in range(n)]
    for i in range(n):
        d[i][i] = 0
    for u, v, w in edges:
        d[u][v] = min(d[u][v], w)
        d[v][u] = min(d[v][u], w)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if d[i][k] + d[k][j] < d[i][j]:
                    d[i][j] = d[i][k] + d[k][j]
    return d
```

**Counting shortest paths.** Equal distance adds ways; a shorter distance resets them.

```python
def count_paths(n, roads, mod=10**9 + 7):     # undirected, from 0 to n - 1
    adj = [[] for _ in range(n)]
    for u, v, w in roads:
        adj[u].append((v, w))
        adj[v].append((u, w))
    dist, ways = [float("inf")] * n, [0] * n
    dist[0], ways[0] = 0, 1
    heap = [(0, 0)]
    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue
        for v, w in adj[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v], ways[v] = nd, ways[u]
                heapq.heappush(heap, (nd, v))
            elif nd == dist[v]:
                ways[v] = (ways[v] + ways[u]) % mod
    return ways[n - 1]
```

**Eulerian path (Reconstruct Itinerary, Hierholzer).** Use each edge once; append a node when it has no unused edges, then reverse.

```python
def find_itinerary(tickets):
    adj = defaultdict(list)
    for a, b in sorted(tickets, reverse=True):
        adj[a].append(b)                      # pop() then yields the smallest
    route, stack = [], ["JFK"]
    while stack:
        while adj[stack[-1]]:
            stack.append(adj[stack[-1]].pop())
        route.append(stack.pop())
    return route[::-1]
```

**Java.** Store `{distance, node}` pairs as `long[]` and compare with `Long.compare`.

```java
static int networkDelayTime(int[][] times, int n, int k) {
    List<List<int[]>> adj = new ArrayList<>();
    for (int i = 0; i <= n; i++) adj.add(new ArrayList<>());
    for (int[] t : times) adj.get(t[0]).add(new int[]{t[1], t[2]});
    long[] dist = new long[n + 1];
    Arrays.fill(dist, Long.MAX_VALUE);
    dist[k] = 0;
    PriorityQueue<long[]> pq = new PriorityQueue<>((a, b) -> Long.compare(a[0], b[0]));
    pq.add(new long[]{0, k});
    while (!pq.isEmpty()) {
        long[] top = pq.poll();
        int u = (int) top[1];
        if (top[0] > dist[u]) continue;
        for (int[] e : adj.get(u)) {
            long nd = top[0] + e[1];
            if (nd < dist[e[0]]) {
                dist[e[0]] = nd;
                pq.add(new long[]{nd, e[0]});
            }
        }
    }
    long best = 0;
    for (int i = 1; i <= n; i++) best = Math.max(best, dist[i]);
    return best == Long.MAX_VALUE ? -1 : (int) best;
}
```

## Complexity

See the table at the top. Space is O(V + E) for adjacency lists; Floyd-Warshall needs O(V²). Lazy-deletion Dijkstra can hold up to E heap entries, so its heap is O(E), still O((V + E) log V) time.

## Common bugs

1. Dijkstra on negative edges (exercise 2).
2. In-place Bellman-Ford when the number of edges is limited (exercise 1).
3. Not skipping stale heap entries, so nodes are expanded many times.
4. Floyd-Warshall with `k` as an inner loop: wrong answers, not just slower.
5. `float("inf")` mixed with integers in Java-style overflow logic; in Java use `Long.MAX_VALUE` and check before adding.
6. Returning when a node is *pushed* rather than *popped*: in Dijkstra a node's distance is final only when it is popped.

## Problems (easy → hard)

Lists: **B75** Blind 75 · **N150** NeetCode 150 · **N250** NeetCode 250. ★ = in the [must-do 100](../problem_list.md).

| # | Problem | Level | What it teaches | Lists |
|---|---|---|---|---|
| 1 | ★ [Network Delay Time](https://leetcode.com/problems/network-delay-time/) | Medium | textbook Dijkstra | N150 · N250 |
| 2 | [Path With Minimum Effort](https://leetcode.com/problems/path-with-minimum-effort/) | Medium | bottleneck cost with Dijkstra | N250 |
| 3 | [Path with Maximum Probability](https://leetcode.com/problems/path-with-maximum-probability/) | Medium | maximising a product with a max-heap | |
| 4 | ★ [Cheapest Flights Within K Stops](https://leetcode.com/problems/cheapest-flights-within-k-stops/) | Medium | limited Bellman-Ford; why plain Dijkstra is wrong | N150 · N250 |
| 5 | [Find the City With the Smallest Number of Neighbors at a Threshold Distance](https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/) | Medium | Floyd-Warshall on a small graph | |
| 6 | [Number of Ways to Arrive at Destination](https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/) | Medium | counting ties during Dijkstra | |
| 7 | [Minimum Obstacle Removal to Reach Corner](https://leetcode.com/problems/minimum-obstacle-removal-to-reach-corner/) | Hard | 0-1 BFS | |
| 8 | [Minimum Cost to Make at Least One Valid Path in a Grid](https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/) | Hard | modelling arrows as 0-cost edges | |
| 9 | [Swim in Rising Water](https://leetcode.com/problems/swim-in-rising-water/) | Hard | bottleneck Dijkstra (compare with union-find in [Pattern 16](16_union_find.md)) | N150 · N250 |
| 10 | [Reconstruct Itinerary](https://leetcode.com/problems/reconstruct-itinerary/) | Hard | Eulerian path with lexical order | N150 · N250 |

## AI-era exercises

**Exercise 1 · Too many stops.**

```python
def find_cheapest_price_ai(n, flights, src, dst, k):
    dist = [float("inf")] * n
    dist[src] = 0
    for _ in range(k + 1):
        for u, v, w in flights:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
    return -1 if dist[dst] == float("inf") else dist[dst]
```

Find a three-city input where it returns a price that uses more than k stops.

<details><summary>Answer</summary>

`n = 3, flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]], src = 0, dst = 2, k = 0`. The answer is 500 (direct flight). In the single round, the code first sets `dist[1] = 100`, then immediately uses that fresh value to set `dist[2] = 200`, a route with one stop. Relaxing from a copy of the previous round (`prev`) limits each round to one more edge. The bug depends on edge order, so a test that only shuffles a few fixed inputs can miss it; generate random graphs and compare with a brute force over all paths of at most k + 1 edges.
</details>

**Exercise 2 · Negative edges.** An assistant's Dijkstra keeps a `done` set:

```python
import heapq


def dijkstra_ai(n, edges, src):
    adj = [[] for _ in range(n)]
    for u, v, w in edges:
        adj[u].append((v, w))
    dist = [float("inf")] * n
    dist[src] = 0
    done, heap = set(), [(0, src)]
    while heap:
        d, u = heapq.heappop(heap)
        if u in done:
            continue
        done.add(u)
        for v, w in adj[u]:
            if v not in done and d + w < dist[v]:
                dist[v] = d + w
                heapq.heappush(heap, (dist[v], v))
    return dist
```

Find a three-node graph with one negative edge (and no negative cycle) where it is wrong. Then decide: is the lazy-deletion template above, which has no `done` set, correct on that graph? What does it cost in general?

<details><summary>Answer</summary>

Edges `0 → 1 (1)`, `0 → 2 (3)`, `2 → 1 (−3)`. The code finalises node 1 at distance 1, then pops node 2 (distance 3) and refuses to update the finished node 1, so it reports 1 instead of 0. The lazy template has no `done` set: when node 2 improves node 1 to 0 it pushes node 1 again and re-expands it, so on graphs with negative edges but no negative cycle it still returns correct distances. It is no longer Dijkstra's algorithm in the analysed sense, though: nodes can be expanded many times, and in the worst case the number of re-expansions grows exponentially. With negative edges, use Bellman-Ford (O(VE)) and say why.
</details>

## You own this pattern when

- Given edge weights and constraints, you pick BFS, 0-1 BFS, Dijkstra, Bellman-Ford or Floyd-Warshall and justify it in one sentence.
- You write lazy-deletion Dijkstra from a blank file in under 7 minutes, including the stale-entry check.
- You can explain why Cheapest Flights needs a copy per round, with the three-city example.
