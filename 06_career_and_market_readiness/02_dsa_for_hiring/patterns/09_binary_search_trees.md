# DSA for hiring · Pattern 09 · Binary search trees and ordered maps

| Theory first | Time | Problems | Must-do |
|---|---|---|---|
| [FND112](../../../01_year_1_foundations/semester_2/FND112_data_structures_and_algorithms_i/README.md) lesson 8.3 | ~7 hours | 12 | 3 |

A BST keeps every key in the left subtree smaller and every key in the right subtree larger, so an in-order walk is sorted and search follows one root-to-leaf path. Interview BST problems test two things: that you use the **global** ordering invariant (not just parent-child comparisons), and that you know when to reach for a library ordered map (`TreeMap`/`TreeSet` in Java; `bisect` on a sorted list in Python) instead of writing a tree.

## Recognise it

| When you see… | Think… |
|---|---|
| "validate", "recover", "k-th smallest", "successor" in a BST | in-order traversal is sorted |
| search/insert/delete in a BST | walk one path: O(h) |
| LCA in a BST | the first node whose value lies between p and q |
| "is there a booked interval overlapping [s, e)?", "nearest value ≤ x" with inserts | ordered map: floor/ceiling queries |
| "a value within t of the current one, among the last k" | ordered set over a sliding window, or buckets of width t + 1 |
| sorted array → balanced tree | pick the middle as root, recurse |

## Core templates

```python
import bisect


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

**Validate with bounds.** Every node must lie in an open interval inherited from all its ancestors.

```python
def is_valid_bst(root):
    stack = [(root, float("-inf"), float("inf"))]
    while stack:
        node, lo, hi = stack.pop()
        if not node:
            continue
        if not (lo < node.val < hi):
            return False
        stack.append((node.left, lo, node.val))
        stack.append((node.right, node.val, hi))
    return True
```

**k-th smallest with an iterative in-order walk.** Stops after k nodes: O(h + k).

```python
def kth_smallest(root, k):
    stack, node = [], root
    while True:
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        k -= 1
        if k == 0:
            return node.val
        node = node.right
```

**LCA in a BST.** Walk down until p and q are on different sides.

```python
def lca_bst(root, p, q):
    node = root
    while node:
        if p.val < node.val and q.val < node.val:
            node = node.left
        elif p.val > node.val and q.val > node.val:
            node = node.right
        else:
            return node
```

**Insert and delete.** Deleting a node with two children copies its in-order successor's value, then deletes the successor from the right subtree.

```python
def insert_bst(root, val):
    if not root:
        return TreeNode(val)
    if val < root.val:
        root.left = insert_bst(root.left, val)
    else:
        root.right = insert_bst(root.right, val)
    return root


def delete_bst(root, key):
    if not root:
        return None
    if key < root.val:
        root.left = delete_bst(root.left, key)
    elif key > root.val:
        root.right = delete_bst(root.right, key)
    else:
        if not root.left:
            return root.right
        if not root.right:
            return root.left
        succ = root.right
        while succ.left:
            succ = succ.left
        root.val = succ.val
        root.right = delete_bst(root.right, succ.val)
    return root
```

**Ordered-map queries in Python with `bisect`.** Python has no built-in balanced BST; a sorted list gives O(log n) search but O(n) insertion, which is fine for n in the low thousands.

```python
class MyCalendar:
    def __init__(self):
        self.starts, self.ends = [], []          # sorted, non-overlapping bookings

    def book(self, start, end):
        i = bisect.bisect_right(self.starts, start)
        if i > 0 and self.ends[i - 1] > start:   # previous booking runs into us
            return False
        if i < len(self.starts) and self.starts[i] < end:
            return False                         # next booking starts before we end
        self.starts.insert(i, start)
        self.ends.insert(i, end)
        return True
```

**Java ordered maps.** `floorKey`, `ceilingKey`, `floor` and `ceiling` are O(log n) on a red-black tree.

```java
static class MyCalendarJ {
    private final TreeMap<Integer, Integer> booked = new TreeMap<>();   // start -> end

    boolean book(int start, int end) {
        Integer prev = booked.floorKey(start);
        if (prev != null && booked.get(prev) > start) return false;
        Integer next = booked.ceilingKey(start);
        if (next != null && next < end) return false;
        booked.put(start, end);
        return true;
    }
}

static boolean containsNearbyAlmostDuplicate(int[] nums, int indexDiff, int valueDiff) {
    TreeSet<Long> window = new TreeSet<>();
    for (int i = 0; i < nums.length; i++) {
        Long c = window.ceiling((long) nums[i] - valueDiff);
        if (c != null && c <= (long) nums[i] + valueDiff) return true;
        window.add((long) nums[i]);
        if (i >= indexDiff) window.remove((long) nums[i - indexDiff]);
    }
    return false;
}
```

## Complexity

Search, insert and delete are O(h): O(log n) for a balanced tree, O(n) for a degenerate one (keys inserted in sorted order). Library ordered maps are balanced (Java's `TreeMap` is a red-black tree), so O(log n) is guaranteed. Validation and full in-order traversal are O(n). The `bisect` calendar is O(log n) to search and O(n) to insert.

## Common bugs

1. Checking only `left.val < node.val < right.val` at each node (exercise 1).
2. Using `<=` vs `<` inconsistently when duplicates are allowed; ask how duplicates are stored.
3. Bounds of `int` type in Java validation (`Integer.MIN_VALUE` is a valid node value); use `long` or nullable bounds.
4. Deleting the successor from the wrong subtree, or forgetting to reattach the returned subtree (`root.left = delete(...)`).
5. Claiming O(log n) for a plain BST without saying "if balanced".
6. Integer overflow in `nums[i] ± valueDiff` in Java; cast to `long` first.

## Problems (easy → hard)

Lists: **B75** Blind 75 · **N150** NeetCode 150 · **N250** NeetCode 250. ★ = in the [must-do 100](../problem_list.md).

| # | Problem | Level | What it teaches | Lists |
|---|---|---|---|---|
| 1 | [Search in a Binary Search Tree](https://leetcode.com/problems/search-in-a-binary-search-tree/) | Easy | one path, O(h) | |
| 2 | [Convert Sorted Array to Binary Search Tree](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/) | Easy | middle as root gives height ⌈log₂(n + 1)⌉ | |
| 3 | [Two Sum IV - Input is a BST](https://leetcode.com/problems/two-sum-iv-input-is-a-bst/) | Easy | in-order + two pointers vs a hash set | |
| 4 | ★ [Lowest Common Ancestor of a Binary Search Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/) | Medium | the split point; O(h), no recursion needed | B75 · N150 · N250 |
| 5 | ★ [Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/) | Medium | inherited bounds; in-order strictly increasing | B75 · N150 · N250 |
| 6 | ★ [Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/) | Medium | early-exit in-order; follow-up: subtree sizes for frequent queries | B75 · N150 · N250 |
| 7 | [Insert into a Binary Search Tree](https://leetcode.com/problems/insert-into-a-binary-search-tree/) | Medium | returning the (possibly new) subtree root | N250 |
| 8 | [Delete Node in a BST](https://leetcode.com/problems/delete-node-in-a-bst/) | Medium | the three deletion cases | N250 |
| 9 | [Binary Search Tree Iterator](https://leetcode.com/problems/binary-search-tree-iterator/) | Medium | a controlled in-order stack; amortised O(1) `next` | |
| 10 | [Recover Binary Search Tree](https://leetcode.com/problems/recover-binary-search-tree/) | Medium | finding the two inversions in an in-order sequence | |
| 11 | [My Calendar I](https://leetcode.com/problems/my-calendar-i/) | Medium | floor/ceiling on an ordered map | |
| 12 | [Contains Duplicate III](https://leetcode.com/problems/contains-duplicate-iii/) | Hard | ordered set over a window, or bucketing by value | |

## AI-era exercises

**Exercise 1 · Find the bug.**

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_valid_bst_ai(root):
    if not root:
        return True
    if root.left and root.left.val >= root.val:
        return False
    if root.right and root.right.val <= root.val:
        return False
    return is_valid_bst_ai(root.left) and is_valid_bst_ai(root.right)
```

Give the smallest tree it accepts that is not a BST.

<details><summary>Answer</summary>

Three nodes: root 5, right child 6, and 6's left child 4 (level order `[5, null, 6, 4]`). Every parent-child pair is ordered correctly, but 4 sits in the right subtree of 5. The code checks only local pairs; the property is global. Fix: pass `(lo, hi)` bounds down (the template) or check that the in-order sequence is strictly increasing. Two nodes are never enough to fool it: with a single parent-child pair, the local check is the whole check. An exhaustive test over all tree shapes with up to three nodes and values 0..2 finds this counterexample in milliseconds.
</details>

**Exercise 2 · Bound the data structure.** For My Calendar I with up to 1,000 calls, an assistant's Python solution keeps a sorted list and uses `bisect.insort`. It says "each booking is O(log n)". Give the true cost per booking and in total, compute it for 1,000 and for 10⁵ calls, and name the data structure you would use in Java and what you would say in a Python interview.

<details><summary>Answer</summary>

`insort` finds the position in O(log n) but inserting into a Python list shifts elements: O(n) per booking, O(n²) in total. For 1,000 calls that is about 5 × 10⁵ element moves (fast: a `memmove` of pointers). For 10⁵ calls it is about 5 × 10⁹ moves in the worst case (inserts near the front), too slow. In Java, `TreeMap` gives O(log n) per booking. In Python, say that the standard library has no balanced BST, that a sorted list is acceptable at this input size, and that at larger scale you would use a balanced tree, a skip list or a third-party sorted container, after confirming with the interviewer that one is allowed.
</details>

## You own this pattern when

- You can explain why local checks are not enough for BST validity and construct the counterexample in under a minute.
- You delete a node with two children correctly on the first attempt.
- You know the floor/ceiling API of your language's ordered map, or how to replace it with `bisect`.
