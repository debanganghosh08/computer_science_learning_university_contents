# DSA for hiring · Pattern 15 · Topological sort and DAGs

| Theory first | Time | Problems | Must-do |
|---|---|---|---|
| [FND112](../../../01_year_1_foundations/semester_2/FND112_data_structures_and_algorithms_i/README.md) lessons 10.3, 10.4; [CS201](../../../02_year_2_core_computer_science/semester_3/CS201_algorithms_and_complexity/README.md) lesson 6.3 | ~7 hours | 11 | 3 |

A topological order lists the nodes of a directed graph so that every edge points forward. It exists exactly when the graph has no directed cycle. Build systems, package managers, course planners and spreadsheet recalculation all depend on it, which is why interviewers like it: the modelling ("which way does the edge point?") matters as much as the algorithm.

## Recognise it

| When you see… | Think… |
|---|---|
| prerequisites, dependencies, "must happen before" | directed edge `before → after`; Kahn's algorithm |
| "can all tasks be finished?" | cycle detection: Kahn's leftover nodes, or DFS with three colours |
| "an order of letters / tasks consistent with these comparisons" | derive edges from adjacent pairs, then topological sort |
| "minimum time if independent tasks run in parallel" | longest path in a DAG: DP in topological order |
| "nodes that never reach a cycle" | reverse the edges and run Kahn's from the sinks |
| "the centre of a tree" (minimum height) | peel leaves layer by layer (Kahn's on an undirected tree) |

## Core templates

**Kahn's algorithm.** Repeatedly take a node with no remaining prerequisites. If some nodes are never taken, they lie on or behind a cycle.

```python
from collections import deque, defaultdict


def topo_order(n, edges):                    # edges: (u, v) means u before v
    adj = [[] for _ in range(n)]
    indeg = [0] * n
    for u, v in edges:
        adj[u].append(v)
        indeg[v] += 1
    q = deque(i for i in range(n) if indeg[i] == 0)
    order = []
    while q:
        u = q.popleft()
        order.append(u)
        for v in adj[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    return order if len(order) == n else []  # [] signals a cycle


def can_finish(num_courses, prerequisites):  # LeetCode gives [course, prereq]
    return len(topo_order(num_courses, [(b, a) for a, b in prerequisites])) == num_courses
```

**DFS with three colours.** White = unvisited, grey = on the current path, black = finished. An edge into a grey node is a back edge: a cycle. Reverse post-order is a topological order.

```python
def topo_dfs(n, edges):
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
    WHITE, GREY, BLACK = 0, 1, 2
    color = [WHITE] * n
    post = []
    for s in range(n):
        if color[s] != WHITE:
            continue
        color[s] = GREY
        stack = [(s, iter(adj[s]))]          # iterative DFS: (node, remaining neighbours)
        while stack:
            u, it = stack[-1]
            v = next(it, None)
            if v is None:
                color[u] = BLACK
                post.append(u)
                stack.pop()
            elif color[v] == GREY:
                return []                    # back edge: cycle
            elif color[v] == WHITE:
                color[v] = GREY
                stack.append((v, iter(adj[v])))
    return post[::-1]
```

**Derive edges, then sort (Alien Dictionary).** Only the first differing letter of adjacent words gives an edge. A longer word before its own prefix is invalid.

```python
def alien_order(words):
    letters = {c for w in words for c in w}
    adj = defaultdict(set)
    indeg = {c: 0 for c in letters}
    for a, b in zip(words, words[1:]):
        for x, y in zip(a, b):
            if x != y:
                if y not in adj[x]:
                    adj[x].add(y)
                    indeg[y] += 1
                break
        else:
            if len(a) > len(b):
                return ""                    # "abc" before "ab" is impossible
    q = deque(sorted(c for c in letters if indeg[c] == 0))
    out = []
    while q:
        c = q.popleft()
        out.append(c)
        for d in sorted(adj[c]):
            indeg[d] -= 1
            if indeg[d] == 0:
                q.append(d)
    return "".join(out) if len(out) == len(letters) else ""
```

**Longest path in a DAG (Parallel Courses III).** Process in topological order; a task finishes at its own time plus the latest finish among its prerequisites.

```python
def minimum_time(n, relations, time):        # courses are 1-indexed
    adj = [[] for _ in range(n)]
    indeg = [0] * n
    for a, b in relations:
        adj[a - 1].append(b - 1)
        indeg[b - 1] += 1
    finish = time[:]                          # finish[i] = earliest completion time
    q = deque(i for i in range(n) if indeg[i] == 0)
    while q:
        u = q.popleft()
        for v in adj[u]:
            finish[v] = max(finish[v], finish[u] + time[v])
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    return max(finish)
```

**Java.**

```java
static int[] findOrder(int n, int[][] prerequisites) {
    List<List<Integer>> adj = new ArrayList<>();
    for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
    int[] indeg = new int[n];
    for (int[] p : prerequisites) {           // p = [course, prereq]: prereq -> course
        adj.get(p[1]).add(p[0]);
        indeg[p[0]]++;
    }
    Deque<Integer> q = new ArrayDeque<>();
    for (int i = 0; i < n; i++) if (indeg[i] == 0) q.add(i);
    int[] order = new int[n];
    int k = 0;
    while (!q.isEmpty()) {
        int u = q.poll();
        order[k++] = u;
        for (int v : adj.get(u)) if (--indeg[v] == 0) q.add(v);
    }
    return k == n ? order : new int[0];
}
```

## Complexity

Kahn's algorithm and the DFS version are O(V + E) time and O(V + E) space. Alien Dictionary is O(C) for C total characters in the input, plus O(U + E) for U distinct letters. DAG longest path is O(V + E).

## Common bugs

1. Edge direction reversed: LeetCode's `[a, b]` in Course Schedule means "b before a".
2. Two-colour DFS (one visited set) reports a false cycle on a diamond-shaped DAG (exercise 2).
3. Alien Dictionary: comparing more than the first differing letter, adding duplicate edges (double-counting in-degrees), or missing the invalid-prefix case (exercise 1).
4. Forgetting nodes with no edges at all: they must still appear in the order.
5. Returning a partial order when a cycle exists instead of signalling failure.
6. Recursive DFS on 10⁵ nodes in Python; use the iterative version above.

## Problems (easy → hard)

Lists: **B75** Blind 75 · **N150** NeetCode 150 · **N250** NeetCode 250. ★ = in the [must-do 100](../problem_list.md).

| # | Problem | Level | What it teaches | Lists |
|---|---|---|---|---|
| 1 | [Find the Town Judge](https://leetcode.com/problems/find-the-town-judge/) | Easy | in-degree and out-degree counting | N250 |
| 2 | ★ [Course Schedule](https://leetcode.com/problems/course-schedule/) | Medium | cycle detection by Kahn's or colours | B75 · N150 · N250 |
| 3 | ★ [Course Schedule II](https://leetcode.com/problems/course-schedule-ii/) | Medium | returning the order itself | N150 · N250 |
| 4 | [Find Eventual Safe States](https://leetcode.com/problems/find-eventual-safe-states/) | Medium | reverse graph + Kahn's from sinks | |
| 5 | [Minimum Height Trees](https://leetcode.com/problems/minimum-height-trees/) | Medium | peeling leaves; at most two centres | N250 |
| 6 | [Course Schedule IV](https://leetcode.com/problems/course-schedule-iv/) | Medium | reachability sets propagated in topological order | N250 |
| 7 | [Find All Possible Recipes from Given Supplies](https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/) | Medium | modelling strings as nodes; supplies as sources | |
| 8 | ★ [Alien Dictionary](https://leetcode.com/problems/alien-dictionary/) (Premium; free mirror [LintCode 892](https://www.lintcode.com/problem/892/)) | Hard | deriving edges; invalid input detection | B75 · N150 · N250 |
| 9 | [Longest Increasing Path in a Matrix](https://leetcode.com/problems/longest-increasing-path-in-a-matrix/) | Hard | the grid is a DAG; memoised DFS or Kahn's by layers | N150 · N250 |
| 10 | [Parallel Courses III](https://leetcode.com/problems/parallel-courses-iii/) | Hard | longest path in a DAG | |
| 11 | [Sort Items by Groups Respecting Dependencies](https://leetcode.com/problems/sort-items-by-groups-respecting-dependencies/) | Hard | two-level topological sort | |

## AI-era exercises

**Exercise 1 · Missing validation.**

```python
from collections import defaultdict, deque


def alien_order_ai(words):
    letters = {c for w in words for c in w}
    adj = defaultdict(set)
    indeg = {c: 0 for c in letters}
    for a, b in zip(words, words[1:]):
        for x, y in zip(a, b):
            if x != y:
                if y not in adj[x]:
                    adj[x].add(y)
                    indeg[y] += 1
                break
    q = deque(c for c in letters if indeg[c] == 0)
    out = []
    while q:
        c = q.popleft()
        out.append(c)
        for d in adj[c]:
            indeg[d] -= 1
            if indeg[d] == 0:
                q.append(d)
    return "".join(out) if len(out) == len(letters) else ""
```

Find a two-word input where it returns an order although none exists.

<details><summary>Answer</summary>

`["abc", "ab"]`: in any alphabet a word sorts after its own proper prefix, so this list cannot be sorted and the answer is `""`. The comparison loop finds no differing letter and adds no edge, so the code returns some order of `a`, `b`, `c`. The fix is the `for ... else` branch in the template that rejects `len(a) > len(b)` when no difference was found. When reviewing parsing-heavy graph code, list the ways the *input* can be inconsistent, not only the ways the graph can have a cycle.
</details>

**Exercise 2 · A false cycle.**

```python
def can_finish_ai(n, prerequisites):
    adj = [[] for _ in range(n)]
    for a, b in prerequisites:
        adj[b].append(a)
    visited = set()

    def has_cycle(u):
        if u in visited:
            return True
        visited.add(u)
        return any(has_cycle(v) for v in adj[u])

    return not any(has_cycle(u) for u in range(n) if u not in visited)
```

Find the smallest input with no cycle where it answers `False`, and explain why two states are not enough.

<details><summary>Answer</summary>

Course 2 depends on 0 and 1, and course 1 depends on 0: `n = 3, prerequisites = [[1, 0], [2, 0], [2, 1]]`. From 0 the DFS reaches 2 through 1, then reaches 2 again directly from 0; the second visit is treated as a cycle. "Visited" mixes two different situations: "on the current path" (a real back edge) and "fully explored earlier" (harmless). Three colours separate them. Small random DAGs (edges only from lower to higher index) expose the bug quickly, because the correct answer is always `True`.
</details>

## You own this pattern when

- You state the edge direction in words before coding ("an edge from prerequisite to course").
- You write Kahn's algorithm from a blank file in under 5 minutes and use it to detect cycles.
- You can explain grey vs black in DFS cycle detection, with the diamond example.
