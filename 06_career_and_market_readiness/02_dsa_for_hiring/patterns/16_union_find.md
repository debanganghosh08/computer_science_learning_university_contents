# DSA for hiring · Pattern 16 · Union-find (disjoint set union)

| Theory first | Time | Problems | Must-do |
|---|---|---|---|
| [CS201](../../../02_year_2_core_computer_science/semester_3/CS201_algorithms_and_complexity/README.md) lessons 3.4 (union-find), 7.4 (Kruskal) | ~7 hours | 13 | 3 |

Union-find maintains a partition of items into groups under two operations: `union(a, b)` merges their groups and `find(a)` returns a group's representative. With union by size (or rank) and path compression, a sequence of m operations on n items costs O(m α(n)), where α is the inverse Ackermann function: at most 4 for any input that fits in this universe. Reach for it when connections only get **added** and you keep asking "are these connected?" or "how many groups?".

## Recognise it

| When you see… | Think… |
|---|---|
| "number of connected components / provinces / groups" with edges given up front | union-find or BFS/DFS; union-find is shorter when edges stream in |
| "the edge that creates a cycle" in an undirected graph | the first `union` that finds both ends already joined |
| "merge accounts/records sharing any key" | union on shared keys (emails, phone numbers) |
| equalities and inequalities between variables | union all `==`, then check every `!=` |
| "minimum cost to connect everything" | Kruskal: sort edges, union if not already connected |
| "earliest time when A and B are connected" as things are added | process additions in order, check after each union |
| deletions or "disconnect" operations | not plain union-find; process offline in reverse, or use another structure |

## Core templates

```python
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.count = n                         # number of groups

    def find(self, x):
        root = x
        while self.parent[root] != root:
            root = self.parent[root]
        while self.parent[x] != root:          # path compression (iterative)
            self.parent[x], x = root, self.parent[x]
        return root

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False                       # already connected
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra                   # attach the smaller tree under the larger
        self.size[ra] += self.size[rb]
        self.count -= 1
        return True
```

**The edge that closes a cycle.**

```python
def find_redundant_connection(edges):          # nodes are 1..n
    dsu = DSU(len(edges) + 1)
    for u, v in edges:
        if not dsu.union(u, v):
            return [u, v]
    return []
```

**Union on shared keys (Accounts Merge).** Give each email an id, union all emails of one account, then group by root.

```python
from collections import defaultdict


def accounts_merge(accounts):
    ids, owner = {}, {}
    for acc in accounts:
        for email in acc[1:]:
            if email not in ids:
                ids[email] = len(ids)
                owner[email] = acc[0]
    dsu = DSU(len(ids))
    for acc in accounts:
        first = ids[acc[1]]
        for email in acc[2:]:
            dsu.union(first, ids[email])
    groups = defaultdict(list)
    for email, i in ids.items():
        groups[dsu.find(i)].append(email)
    return [[owner[g[0]]] + sorted(g) for g in groups.values()]
```

**Kruskal's minimum spanning tree.**

```python
def min_cost_connect_points(points):
    n = len(points)
    edges = sorted(
        (abs(x1 - x2) + abs(y1 - y2), i, j)
        for i, (x1, y1) in enumerate(points)
        for j, (x2, y2) in enumerate(points) if i < j
    )
    dsu, total = DSU(n), 0
    for w, i, j in edges:
        if dsu.union(i, j):
            total += w
            if dsu.count == 1:
                break
    return total
```

**Equalities first, then inequalities.**

```python
def equations_possible(equations):
    dsu = DSU(26)
    for e in equations:
        if e[1] == "=":
            dsu.union(ord(e[0]) - 97, ord(e[3]) - 97)
    return all(dsu.find(ord(e[0]) - 97) != dsu.find(ord(e[3]) - 97)
               for e in equations if e[1] == "!")
```

**Connect in order of a threshold (Swim in Rising Water).** Add cells from lowest to highest; the answer is the level at which the corners join.

```python
def swim_in_water(grid):
    n = len(grid)
    order = sorted((grid[r][c], r, c) for r in range(n) for c in range(n))
    dsu = DSU(n * n)
    for t, r, c in order:
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] <= t:
                dsu.union(r * n + c, nr * n + nc)
        if dsu.find(0) == dsu.find(n * n - 1):
            return t
    return grid[0][0]
```

**Java.**

```java
static int[] parent, sz;

static int find(int x) {
    while (parent[x] != x) {
        parent[x] = parent[parent[x]];          // path halving
        x = parent[x];
    }
    return x;
}

static boolean union(int a, int b) {
    int ra = find(a), rb = find(b);
    if (ra == rb) return false;
    if (sz[ra] < sz[rb]) { int t = ra; ra = rb; rb = t; }
    parent[rb] = ra;
    sz[ra] += sz[rb];
    return true;
}

static int countComponents(int n, int[][] edges) {
    parent = new int[n];
    sz = new int[n];
    for (int i = 0; i < n; i++) { parent[i] = i; sz[i] = 1; }
    int count = n;
    for (int[] e : edges) if (union(e[0], e[1])) count--;
    return count;
}
```

## Complexity

With union by size and path compression: O(α(n)) amortised per operation, effectively constant. With path compression alone: O(log n) amortised. With neither: O(n) per `find` on a chain (exercise 2). Kruskal on E edges: O(E log E) for sorting. Min Cost to Connect All Points has E = n(n − 1)/2 edges, so O(n² log n); Prim's algorithm on the dense graph is O(n²).

## Common bugs

1. Linking the elements instead of their roots: `parent[a] = b` (exercise 1).
2. Counting components by counting distinct `parent` values without calling `find` (parents may be stale).
3. Forgetting to map non-integer keys (emails, coordinates) to ids.
4. Processing inequalities before all equalities are merged.
5. Using union-find when edges are removed over time.
6. Recursive `find` in Python on a long chain before compression has flattened it; the iterative version avoids the recursion limit.

## Problems (easy → hard)

Lists: **B75** Blind 75 · **N150** NeetCode 150 · **N250** NeetCode 250. ★ = in the [must-do 100](../problem_list.md).

| # | Problem | Level | What it teaches | Lists |
|---|---|---|---|---|
| 1 | ★ [Redundant Connection](https://leetcode.com/problems/redundant-connection/) | Medium | the union that fails closes a cycle | N150 · N250 |
| 2 | ★ [Number of Connected Components in an Undirected Graph](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/) (Premium; free mirror [LintCode 3651](https://www.lintcode.com/problem/3651/)) | Medium | count = n − successful unions | B75 · N150 · N250 |
| 3 | [Graph Valid Tree](https://leetcode.com/problems/graph-valid-tree/) (Premium; free mirror [LintCode 178](https://www.lintcode.com/problem/178/)) | Medium | a tree has n − 1 edges and no cycle | B75 · N150 · N250 |
| 4 | [Number of Operations to Make Network Connected](https://leetcode.com/problems/number-of-operations-to-make-network-connected/) | Medium | spare edges vs components − 1 | |
| 5 | ★ [Accounts Merge](https://leetcode.com/problems/accounts-merge/) | Medium | union on shared keys | N250 |
| 6 | [Satisfiability of Equality Equations](https://leetcode.com/problems/satisfiability-of-equality-equations/) | Medium | equalities, then inequalities | |
| 7 | [Most Stones Removed with Same Row or Column](https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/) | Medium | union rows with columns; answer = stones − groups | |
| 8 | [Smallest String With Swaps](https://leetcode.com/problems/smallest-string-with-swaps/) | Medium | sort characters within each component | |
| 9 | [Regions Cut By Slashes](https://leetcode.com/problems/regions-cut-by-slashes/) | Medium | modelling: split each cell into four triangles | |
| 10 | [Min Cost to Connect All Points](https://leetcode.com/problems/min-cost-to-connect-all-points/) | Medium | Kruskal vs Prim on a dense graph | N150 · N250 |
| 11 | [Redundant Connection II](https://leetcode.com/problems/redundant-connection-ii/) | Hard | directed version: a node with two parents | |
| 12 | [Making A Large Island](https://leetcode.com/problems/making-a-large-island/) | Hard | component sizes + distinct neighbouring roots | |
| 13 | [Swim in Rising Water](https://leetcode.com/problems/swim-in-rising-water/) | Hard | union in threshold order (or Dijkstra on the max) | N150 · N250 |

[Find if Path Exists in Graph](https://leetcode.com/problems/find-if-path-exists-in-graph/) and [Number of Provinces](https://leetcode.com/problems/number-of-provinces/) ([Pattern 14](14_graphs_bfs_dfs.md)) are good first union-find exercises too.

## AI-era exercises

**Exercise 1 · Find the bug.**

```python
class DSU_AI:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        while self.parent[x] != x:
            x = self.parent[x]
        return x

    def union(self, a, b):
        if self.find(a) == self.find(b):
            return False
        self.parent[a] = b
        return True


def count_components_ai(n, edges):
    d = DSU_AI(n)
    return n - sum(d.union(u, v) for u, v in edges)
```

Find a three-node input where `count_components_ai` is wrong.

<details><summary>Answer</summary>

`n = 3, edges = [(0, 1), (0, 2)]`: the first union sets `parent[0] = 1`; the second sets `parent[0] = 2`, which detaches 0 from 1. Both unions reported success, so the count is 3 − 2 = 1 and happens to be right, but the structure is wrong: `find(1) == 1` and `find(2) == 2`. Add a third edge `(1, 2)`: the code thinks 1 and 2 are not connected and "successfully" unions them, returning 0 components. Fix: link roots, `self.parent[self.find(a)] = self.find(b)` (and add union by size). Lesson: a correct count can hide a broken invariant; test `find` results, not only the final number.
</details>

**Exercise 2 · Measure the missing optimisations.** Without union by size and path compression, `find` can be O(n). Build the worst case for the naive root-linking DSU below and count the total steps for n = 1,000 and 2,000.

```python
class NaiveDSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.steps = 0

    def find(self, x):
        while self.parent[x] != x:
            x = self.parent[x]
            self.steps += 1
        return x

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra != rb:
            self.parent[ra] = rb
```

<details><summary>Answer</summary>

Call `union(0, i)` for i = 1, 2, …, n − 1. Each call links the current root under the new node, so the tree becomes a chain 0 → 1 → 2 → … and the i-th call's `find(0)` walks i − 1 links: (n − 1)(n − 2)/2 steps in total, which is 498,501 for n = 1,000 and 1,997,001 for n = 2,000 (doubling n quadruples the work). Union by size keeps every tree's height at most log₂ n; path compression flattens the chain on the first walk.
</details>

## You own this pattern when

- You write the DSU class from memory with union by size and iterative path compression.
- You can say when union-find beats BFS (incremental edges, many connectivity queries) and when it cannot be used (deletions).
- You solve Accounts Merge and Redundant Connection AI off in under 20 minutes each.
