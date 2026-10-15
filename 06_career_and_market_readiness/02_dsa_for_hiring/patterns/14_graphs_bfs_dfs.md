# DSA for hiring · Pattern 14 · Graphs: BFS, DFS and grids

| Theory first | Time | Problems | Must-do |
|---|---|---|---|
| [FND112](../../../01_year_1_foundations/semester_2/FND112_data_structures_and_algorithms_i/README.md) chapter 10; [CS201](../../../02_year_2_core_computer_science/semester_3/CS201_algorithms_and_complexity/README.md) chapter 6 | ~12 hours | 15 | 5 |

Most graph interview problems never say "graph". A grid of land and water, a word list where words differ by one letter, accounts that share emails, a lock with four wheels: each is a set of states (nodes) with moves between them (edges). The work is in **modelling**: what is a node, what is an edge, and is the graph weighted? Then BFS (fewest steps, unweighted) or DFS (reachability, components, cycles) is a short template.

## Recognise it

| When you see… | Think… |
|---|---|
| a grid with regions, islands, "connected" cells | DFS/BFS flood fill; count components |
| "minimum number of steps/moves/minutes", all moves cost the same | BFS; distance = BFS layer |
| several starting points spreading at once (rotting, fire, nearest exit) | multi-source BFS: put every source in the queue at distance 0 |
| "cells that can reach both X and Y" | search *backwards* from X and from Y, intersect |
| "copy a graph" | map old node → new node while traversing |
| "can it be split into two groups with no edge inside a group" | BFS/DFS 2-colouring (bipartite check) |
| state includes more than position (keys held, obstacles removed, stops used) | BFS over `(position, extra state)` |
| different edge weights | not BFS: Dijkstra or 0-1 BFS ([Pattern 17](17_shortest_paths.md)) |

## Core templates

**Grid components (iterative DFS, no recursion limit).**

```python
from collections import deque, defaultdict

DIRS = ((1, 0), (-1, 0), (0, 1), (0, -1))


def num_islands(grid):
    m, n = len(grid), len(grid[0])
    seen = set()
    count = 0
    for r in range(m):
        for c in range(n):
            if grid[r][c] == "1" and (r, c) not in seen:
                count += 1
                seen.add((r, c))
                stack = [(r, c)]
                while stack:
                    x, y = stack.pop()
                    for dx, dy in DIRS:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == "1" and (nx, ny) not in seen:
                            seen.add((nx, ny))
                            stack.append((nx, ny))
    return count
```

**BFS shortest path (unweighted).** Mark a node as seen when it is **enqueued**, not when it is dequeued.

```python
def bfs_dist(adj, src):
    dist = {src: 0}
    q = deque([src])
    while q:
        u = q.popleft()
        for v in adj[u]:
            if v not in dist:
                dist[v] = dist[u] + 1
                q.append(v)
    return dist                              # unreachable nodes are absent
```

**Multi-source BFS (Rotting Oranges).** All sources start in the queue; count layers; check for leftovers.

```python
def oranges_rotting(grid):
    m, n = len(grid), len(grid[0])
    q = deque((r, c) for r in range(m) for c in range(n) if grid[r][c] == 2)
    fresh = sum(row.count(1) for row in grid)
    minutes = 0
    while q and fresh:
        for _ in range(len(q)):              # one layer = one minute
            r, c = q.popleft()
            for dr, dc in DIRS:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh -= 1
                    q.append((nr, nc))
        minutes += 1
    return -1 if fresh else minutes
```

**Search backwards from the targets (Pacific Atlantic).**

```python
def pacific_atlantic(h):
    m, n = len(h), len(h[0])

    def reach(starts):
        seen = set(starts)
        q = deque(starts)
        while q:
            r, c = q.popleft()
            for dr, dc in DIRS:
                nr, nc = r + dr, c + dc
                if (0 <= nr < m and 0 <= nc < n and (nr, nc) not in seen
                        and h[nr][nc] >= h[r][c]):   # water flows downhill, we walk uphill
                    seen.add((nr, nc))
                    q.append((nr, nc))
        return seen

    pac = reach([(0, c) for c in range(n)] + [(r, 0) for r in range(m)])
    atl = reach([(m - 1, c) for c in range(n)] + [(r, n - 1) for r in range(m)])
    return sorted(map(list, pac & atl))
```

**Clone a graph.**

```python
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def clone_graph(node):
    if not node:
        return None
    copies = {node: Node(node.val)}
    q = deque([node])
    while q:
        u = q.popleft()
        for v in u.neighbors:
            if v not in copies:
                copies[v] = Node(v.val)
                q.append(v)
            copies[u].neighbors.append(copies[v])
    return copies[node]
```

**Bipartite check (graph may be disconnected).**

```python
def is_bipartite(graph):                     # adjacency list: graph[u] = [v, ...]
    color = {}
    for s in range(len(graph)):
        if s in color:
            continue
        color[s] = 0
        q = deque([s])
        while q:
            u = q.popleft()
            for v in graph[u]:
                if v not in color:
                    color[v] = 1 - color[u]
                    q.append(v)
                elif color[v] == color[u]:
                    return False
    return True
```

**Implicit graph with bucketed neighbours (Word Ladder).** Words sharing a pattern like `h*t` are neighbours.

```python
def ladder_length(begin, end, words):
    words = set(words)
    if end not in words:
        return 0
    buckets = defaultdict(list)
    for w in words | {begin}:
        for i in range(len(w)):
            buckets[w[:i] + "*" + w[i + 1:]].append(w)
    dist = {begin: 1}
    q = deque([begin])
    while q:
        w = q.popleft()
        if w == end:
            return dist[w]
        for i in range(len(w)):
            key = w[:i] + "*" + w[i + 1:]
            for v in buckets[key]:
                if v not in dist:
                    dist[v] = dist[w] + 1
                    q.append(v)
            buckets[key] = []                # each bucket is expanded once
    return 0
```

**BFS over (position, extra state)** (Shortest Path in a Grid with Obstacles Elimination).

```python
def shortest_path_with_k(grid, k):
    m, n = len(grid), len(grid[0])
    if k >= m + n - 2:
        return m + n - 2                     # enough removals to walk straight
    start = (0, 0, k)
    dist = {start: 0}
    q = deque([start])
    while q:
        r, c, left = q.popleft()
        if (r, c) == (m - 1, n - 1):
            return dist[(r, c, left)]
        for dr, dc in DIRS:
            nr, nc = r + dr, c + dc
            if 0 <= nr < m and 0 <= nc < n:
                nl = left - grid[nr][nc]
                if nl >= 0 and (nr, nc, nl) not in dist:
                    dist[(nr, nc, nl)] = dist[(r, c, left)] + 1
                    q.append((nr, nc, nl))
    return -1
```

**Java.** Encode a cell as `r * n + c` to avoid allocating `int[]` pairs.

```java
static int numIslands(char[][] grid) {
    int m = grid.length, n = grid[0].length, count = 0;
    int[] dr = {1, -1, 0, 0}, dc = {0, 0, 1, -1};
    boolean[] seen = new boolean[m * n];
    Deque<Integer> q = new ArrayDeque<>();
    for (int r = 0; r < m; r++)
        for (int c = 0; c < n; c++) {
            if (grid[r][c] != '1' || seen[r * n + c]) continue;
            count++;
            seen[r * n + c] = true;
            q.add(r * n + c);
            while (!q.isEmpty()) {
                int cell = q.poll(), x = cell / n, y = cell % n;
                for (int d = 0; d < 4; d++) {
                    int nx = x + dr[d], ny = y + dc[d];
                    if (nx >= 0 && nx < m && ny >= 0 && ny < n && grid[nx][ny] == '1' && !seen[nx * n + ny]) {
                        seen[nx * n + ny] = true;
                        q.add(nx * n + ny);
                    }
                }
            }
        }
    return count;
}
```

## Complexity

BFS and DFS are O(V + E) time and O(V) space. On an m × n grid, V = mn and E ≤ 4mn, so O(mn). Word Ladder with buckets is O(N · L²) for N words of length L (building keys costs O(L) each). BFS over extra state multiplies V by the number of states: O(m · n · k) for obstacle elimination.

## Common bugs

1. Marking visited at dequeue time: correct answers, but the queue can blow up (exercise 2).
2. DFS for "fewest steps": DFS finds *a* path, not the shortest (exercise 1).
3. Recursive DFS on a 1,000 × 1,000 grid: Python's recursion limit or the Java thread stack is exceeded. Use an explicit stack.
4. Multi-source BFS that starts from one source at a time: O(sources × grid) instead of O(grid).
5. Counting one extra minute/layer after the last real change (check `fresh` in the loop condition).
6. Bipartite check that only starts from node 0 and misses other components.

## Problems (easy → hard)

Lists: **B75** Blind 75 · **N150** NeetCode 150 · **N250** NeetCode 250. ★ = in the [must-do 100](../problem_list.md).

| # | Problem | Level | What it teaches | Lists |
|---|---|---|---|---|
| 1 | [Flood Fill](https://leetcode.com/problems/flood-fill/) | Easy | grid traversal; the same-colour edge case | |
| 2 | [Find if Path Exists in Graph](https://leetcode.com/problems/find-if-path-exists-in-graph/) | Easy | build an adjacency list, then BFS/DFS | |
| 3 | ★ [Number of Islands](https://leetcode.com/problems/number-of-islands/) | Medium | counting components | B75 · N150 · N250 |
| 4 | [Max Area of Island](https://leetcode.com/problems/max-area-of-island/) | Medium | component sizes | N150 · N250 |
| 5 | ★ [Clone Graph](https://leetcode.com/problems/clone-graph/) | Medium | old → new map during traversal | B75 · N150 · N250 |
| 6 | [Number of Provinces](https://leetcode.com/problems/number-of-provinces/) | Medium | components from an adjacency matrix (also union-find) | |
| 7 | ★ [Rotting Oranges](https://leetcode.com/problems/rotting-oranges/) | Medium | multi-source BFS by layers | N150 · N250 |
| 8 | [01 Matrix](https://leetcode.com/problems/01-matrix/) | Medium | distance to the nearest source, all at once | |
| 9 | [Walls and Gates](https://leetcode.com/problems/walls-and-gates/) (Premium; free mirror [LintCode 663](https://www.lintcode.com/problem/663/)) | Medium | multi-source BFS in place | N150 · N250 |
| 10 | ★ [Pacific Atlantic Water Flow](https://leetcode.com/problems/pacific-atlantic-water-flow/) | Medium | reverse search from the targets | B75 · N150 · N250 |
| 11 | [Surrounded Regions](https://leetcode.com/problems/surrounded-regions/) | Medium | mark what touches the border first | N150 · N250 |
| 12 | [Is Graph Bipartite?](https://leetcode.com/problems/is-graph-bipartite/) | Medium | 2-colouring across components | |
| 13 | [Shortest Path in Binary Matrix](https://leetcode.com/problems/shortest-path-in-binary-matrix/) | Medium | BFS with 8 directions; why DFS is wrong | |
| 14 | ★ [Word Ladder](https://leetcode.com/problems/word-ladder/) | Hard | implicit graph; wildcard buckets | N150 · N250 |
| 15 | [Shortest Path in a Grid with Obstacles Elimination](https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/) | Hard | BFS over (cell, removals left) | |

## AI-era exercises

**Exercise 1 · Wrong traversal for the question.** An assistant's Shortest Path in Binary Matrix (8-directional moves):

```python
def shortest_path_binary_matrix_ai(grid):
    n = len(grid)
    if grid[0][0] or grid[n - 1][n - 1]:
        return -1
    seen = {(0, 0)}

    def dfs(r, c):
        if (r, c) == (n - 1, n - 1):
            return 1
        for dr, dc in [(0, 1), (1, 0), (1, 1), (-1, 0), (0, -1), (-1, -1), (-1, 1), (1, -1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0 and (nr, nc) not in seen:
                seen.add((nr, nc))
                d = dfs(nr, nc)
                if d != -1:
                    return d + 1
        return -1

    return dfs(0, 0)
```

Find the smallest grid where the answer is wrong. Would changing the direction order fix it?

<details><summary>Answer</summary>

The 2 × 2 grid of zeros: the answer is 2 (one diagonal step), but DFS tries `(0, 1)` first, reaches the corner from there and returns 3. Reordering the directions to try the diagonal first fixes this grid but not the method: DFS returns the first path it finds, and with a shared `seen` set it can also block cells that a shorter path needs. BFS explores by distance, so the first time it reaches the target is the shortest. Test against BFS on random 4 × 4 grids.
</details>

**Exercise 2 · Prove the blow-up.** An assistant's BFS marks cells when they are dequeued:

```python
from collections import deque


def bfs_pushes_ai(n):
    """BFS from (0, 0) on an open n x n grid; returns how many times a cell was enqueued."""
    seen, q, pushes = set(), deque([(0, 0)]), 1
    while q:
        r, c = q.popleft()
        seen.add((r, c))
        for dr, dc in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in seen:
                q.append((nr, nc))
                pushes += 1
    return pushes
```

The distances it would compute are still correct. Why is this still a bug? Measure `pushes` for n = 4, 6, 8 and explain the growth.

<details><summary>Answer</summary>

A cell can be enqueued once per path that reaches it before it is first dequeued, and every copy expands its neighbours again. On an open grid the number of copies of cell (i, j) grows like the number of shortest paths to it, C(i + j, i), so the queue grows exponentially with n instead of staying at n². For n = 4, 6 and 8 the function reports 69, 923 and 12,869 pushes, against 16, 36 and 64 cells. The fix is one line: mark `seen` when enqueuing. This is a correctness-adjacent bug that sample tests never catch; only a timing or counting test does.
</details>

## You own this pattern when

- For any graph problem you state the node, the edge and whether weights differ, before coding.
- You write grid BFS and DFS iteratively from a blank file in under 5 minutes.
- You solve Word Ladder and Rotting Oranges AI off and explain why BFS gives the minimum.
