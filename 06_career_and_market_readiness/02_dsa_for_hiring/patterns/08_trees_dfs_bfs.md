# DSA for hiring · Pattern 08 · Binary trees: DFS and BFS

| Theory first | Time | Problems | Must-do |
|---|---|---|---|
| [FND112](../../../01_year_1_foundations/semester_2/FND112_data_structures_and_algorithms_i/README.md) lessons 8.1, 8.2, 8.5 | ~12 hours | 15 | 8 |

Almost every tree problem is one of two shapes. **DFS that returns something** from each subtree (height, sum, "is valid", best path) and combines children's answers at the parent. **BFS by levels** when the question mentions depth, levels, "closest" or "right side". Decide which shape before writing code, and decide what the recursive function *returns*: that sentence is the solution.

## Recognise it

| When you see… | Think… |
|---|---|
| height, balance, diameter, "max/min over all root-to-leaf paths" | post-order DFS returning a value; update a global best at each node |
| "path between any two nodes" (max path sum, diameter) | return the best *downward* path; combine left + node + right for the answer |
| "level by level", "right side view", "zigzag", "minimum depth" | BFS processing one level per outer loop |
| two trees compared (same, subtree, symmetric) | DFS on pairs of nodes |
| reconstruct from traversals | preorder gives the root; inorder splits left from right |
| "lowest common ancestor" | DFS returning "found p or q here" |
| "distance k from a node" | add parent pointers, then BFS as in a graph |
| path sums that may start anywhere | prefix sums along the root-to-node path ([Pattern 04](04_prefix_sums.md)) |

## Core templates

```python
from collections import deque, defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(level):                   # LeetCode level-order list with None, for tests
    if not level or level[0] is None:
        return None
    root = TreeNode(level[0])
    queue, i = [root], 1
    for node in queue:                   # a list may grow while it is iterated
        for side in ("left", "right"):
            if i < len(level) and level[i] is not None:
                child = TreeNode(level[i])
                setattr(node, side, child)
                queue.append(child)
            i += 1
    return root
```

**DFS returning a value + global best (diameter).** Return height; the diameter through a node is `left height + right height`.

```python
def diameter_of_binary_tree(root):
    best = 0

    def height(node):
        nonlocal best
        if not node:
            return 0
        l, r = height(node.left), height(node.right)
        best = max(best, l + r)          # edges on the longest path through node
        return 1 + max(l, r)

    height(root)
    return best
```

**Max path sum.** A child contributes only if its best downward path is positive.

```python
def max_path_sum(root):
    best = float("-inf")

    def gain(node):
        nonlocal best
        if not node:
            return 0
        l = max(gain(node.left), 0)
        r = max(gain(node.right), 0)
        best = max(best, node.val + l + r)
        return node.val + max(l, r)      # a downward path uses one side only

    gain(root)
    return best
```

**BFS by levels.** Freeze the level size before the inner loop.

```python
def level_order(root):
    if not root:
        return []
    out, q = [], deque([root])
    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        out.append(level)
    return out
```

**Lowest common ancestor.** Return the node if it is p or q; a node whose both sides return non-null is the answer.

```python
def lowest_common_ancestor(root, p, q):
    if root is None or root is p or root is q:
        return root
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)
    if left and right:
        return root
    return left or right
```

**Build from preorder + inorder.** A value → index map makes each split O(1); values must be distinct.

```python
def build_from_pre_in(preorder, inorder):
    pos = {v: i for i, v in enumerate(inorder)}
    it = iter(preorder)

    def build(lo, hi):                   # inorder[lo:hi]
        if lo >= hi:
            return None
        v = next(it)
        node = TreeNode(v)
        node.left = build(lo, pos[v])
        node.right = build(pos[v] + 1, hi)
        return node

    return build(0, len(inorder))
```

**Serialize with explicit nulls.** Preorder with a null marker is enough to rebuild the exact shape.

```python
def serialize(root):
    out = []

    def dfs(node):
        if not node:
            out.append("#")
            return
        out.append(str(node.val))
        dfs(node.left)
        dfs(node.right)

    dfs(root)
    return ",".join(out)


def deserialize(data):
    it = iter(data.split(","))

    def build():
        v = next(it)
        if v == "#":
            return None
        node = TreeNode(int(v))
        node.left = build()
        node.right = build()
        return node

    return build()
```

**Path sums starting anywhere (Path Sum III).** Prefix sums along the current root-to-node path; undo on the way back up.

```python
def path_sum_iii(root, target):
    seen = defaultdict(int)
    seen[0] = 1

    def dfs(node, cur):
        if not node:
            return 0
        cur += node.val
        count = seen[cur - target]
        seen[cur] += 1
        count += dfs(node.left, cur) + dfs(node.right, cur)
        seen[cur] -= 1                   # backtrack: this prefix leaves the path
        return count

    return dfs(root, 0)
```

**Iterative inorder** (no recursion limit).

```python
def inorder_iterative(root):
    out, stack, node = [], [], root
    while stack or node:
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        out.append(node.val)
        node = node.right
    return out
```

**Java.**

```java
static class TreeNode {
    int val; TreeNode left, right;
    TreeNode(int v) { val = v; }
}

static List<List<Integer>> levelOrder(TreeNode root) {
    List<List<Integer>> out = new ArrayList<>();
    if (root == null) return out;
    Deque<TreeNode> q = new ArrayDeque<>();
    q.offer(root);
    while (!q.isEmpty()) {
        List<Integer> level = new ArrayList<>();
        for (int size = q.size(); size > 0; size--) {
            TreeNode node = q.poll();
            level.add(node.val);
            if (node.left != null) q.offer(node.left);
            if (node.right != null) q.offer(node.right);
        }
        out.add(level);
    }
    return out;
}
```

## Complexity

Every template visits each node once: O(n) time. Space is O(h) for DFS, where h is the height (O(log n) balanced, O(n) for a skewed tree), and O(w) for BFS, where w is the maximum width (up to about n/2 for a complete tree).

## Common bugs

1. Recomputing height inside a recursive check (diameter, balance), which makes the solution O(n²) on skewed trees (exercise 2).
2. Not clamping negative gains at 0 in max path sum (exercise 1), or returning `l + r + val` upward (a path cannot fork).
3. BFS that reads `len(q)` inside the loop after appending, mixing levels.
4. Confusing "edges" with "nodes" in diameter and depth questions; ask which one is wanted.
5. Forgetting to undo `seen[cur]` in Path Sum III, so sums from other branches leak in.
6. Deep recursion on a 10⁵-node skewed tree in Python; use the iterative form or say so.

## Problems (easy → hard)

Lists: **B75** Blind 75 · **N150** NeetCode 150 · **N250** NeetCode 250. ★ = in the [must-do 100](../problem_list.md).

| # | Problem | Level | What it teaches | Lists |
|---|---|---|---|---|
| 1 | ★ [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/) | Easy | DFS returning a value; BFS counting levels | B75 · N150 · N250 |
| 2 | ★ [Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/) | Easy | pre-order transformation | B75 · N150 · N250 |
| 3 | [Same Tree](https://leetcode.com/problems/same-tree/) | Easy | DFS on pairs | B75 · N150 · N250 |
| 4 | [Subtree of Another Tree](https://leetcode.com/problems/subtree-of-another-tree/) | Easy | O(mn) pair DFS vs serialisation + string matching | B75 · N150 · N250 |
| 5 | ★ [Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/) | Easy | return height, update a global best | N150 · N250 |
| 6 | [Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/) | Easy | return height or a sentinel for "unbalanced" in one pass | N150 · N250 |
| 7 | ★ [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/) | Medium | BFS by levels | B75 · N150 · N250 |
| 8 | [Binary Tree Right Side View](https://leetcode.com/problems/binary-tree-right-side-view/) | Medium | last node of each level | N150 · N250 |
| 9 | [Count Good Nodes in Binary Tree](https://leetcode.com/problems/count-good-nodes-in-binary-tree/) | Medium | passing state *down* (max so far) | N150 · N250 |
| 10 | ★ [Lowest Common Ancestor of a Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/) | Medium | returning "found" signals upward | |
| 11 | ★ [Construct Binary Tree from Preorder and Inorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/) | Medium | index map; why distinct values matter | B75 · N150 · N250 |
| 12 | [Path Sum III](https://leetcode.com/problems/path-sum-iii/) | Medium | prefix sums with backtracking | |
| 13 | [All Nodes Distance K in Binary Tree](https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/) | Medium | tree → graph with parent links, then BFS | |
| 14 | ★ [Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/) | Hard | downward gain vs path through the node | B75 · N150 · N250 |
| 15 | ★ [Serialize and Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/) | Hard | preorder with null markers; designing a format | B75 · N150 · N250 |

## AI-era exercises

**Exercise 1 · Find the bug.**

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_path_sum_ai(root):
    best = float("-inf")

    def gain(node):
        nonlocal best
        if not node:
            return 0
        l, r = gain(node.left), gain(node.right)
        best = max(best, node.val + l + r)
        return node.val + max(l, r)

    gain(root)
    return best
```

Find a two-node tree where it is wrong and explain the fix in one sentence.

<details><summary>Answer</summary>

Root 2 with left child −1: the best path is `[2]` with sum 2, but the code computes `2 + (−1) + 0 = 1` at the root and returns 1. A negative subtree should be dropped, not added: clamp each child's gain with `max(gain, 0)`. Random small trees with values in −3..3, checked against a brute force over all node pairs, catch this immediately.
</details>

**Exercise 2 · Prove the complexity.** An assistant writes Diameter of Binary Tree as:

```python
def depth_ai(node):
    return 0 if not node else 1 + max(depth_ai(node.left), depth_ai(node.right))


def diameter_ai(root):
    if not root:
        return 0
    through = depth_ai(root.left) + depth_ai(root.right)
    return max(through, diameter_ai(root.left), diameter_ai(root.right))
```

It says "O(n), each node is visited once". Is that right? Give the worst-case tree, count the work, and point to the template that fixes it.

<details><summary>Answer</summary>

No. `diameter_ai` calls `depth_ai` at every node, and `depth_ai` visits the whole subtree. On a skewed tree (a path of n nodes), the subtree sizes are n − 1, n − 2, …, so the work is about n²/2: O(n²). On a balanced tree it is O(n log n). The template `diameter_of_binary_tree` computes height and diameter in the same post-order pass, so every node is visited once: O(n). Timing n = 1,000, 2,000 and 4,000 on a skewed tree (iteratively built, recursion limit raised for the test) shows the quadratic growth.
</details>

## You own this pattern when

- For any tree problem you can say in one sentence what your recursive function returns, before coding.
- You solve problems 11, 14 and 15 AI off in under 25 minutes each.
- You can state the space complexity of DFS and BFS in terms of height and width, with a worst-case shape for each.
