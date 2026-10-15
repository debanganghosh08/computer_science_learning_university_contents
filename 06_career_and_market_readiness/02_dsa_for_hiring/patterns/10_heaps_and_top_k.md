# DSA for hiring · Pattern 10 · Heaps, top-k and two heaps

| Theory first | Time | Problems | Must-do |
|---|---|---|---|
| [FND112](../../../01_year_1_foundations/semester_2/FND112_data_structures_and_algorithms_i/README.md) chapter 9 | ~8 hours | 12 | 4 |

A binary heap gives the minimum (or maximum) in O(1) and inserts or removes in O(log n). Use it when you repeatedly need "the best item right now" while items keep arriving: the k largest of a stream, the next event in a simulation, the smallest head among k sorted lists, the running median.

## Recognise it

| When you see… | Think… |
|---|---|
| "k largest / k smallest / k closest / k most frequent" | a heap of size k holding the current best k; the *opposite* kind of heap |
| "k-th largest" in a fixed array | size-k min-heap O(n log k), or quickselect O(n) expected |
| "merge k sorted lists/arrays/streams" | heap of the current heads |
| "running median", "balance two halves" | max-heap for the lower half, min-heap for the upper half |
| "schedule tasks / greedy pick the most urgent or most profitable available" | heap keyed by the greedy criterion |
| "smallest range covering one element from each list" | heap of heads + track the current maximum |

**Not this pattern when** k is close to n (sort instead), or you need to search or delete arbitrary elements (use an ordered map, [Pattern 09](09_binary_search_trees.md)).

## Core templates

Python's `heapq` is a min-heap on a plain list. For a max-heap, push negated keys. Python 3.14 added max-heap functions to `heapq` (`heapify_max`, `heappush_max`, `heappop_max`); negation works in every version.

**Top-k with a size-k min-heap.** The root is the weakest of the current best k, so it is the one to evict.

```python
import heapq
from collections import Counter


def kth_largest(nums, k):
    heap = []
    for x in nums:
        heapq.heappush(heap, x)
        if len(heap) > k:
            heapq.heappop(heap)          # drop the smallest of k + 1
    return heap[0]


def k_closest(points, k):
    heap = []                             # max-heap by distance via negation
    for x, y in points:
        heapq.heappush(heap, (-(x * x + y * y), x, y))
        if len(heap) > k:
            heapq.heappop(heap)
    return [[x, y] for _, x, y in heap]
```

**Merge k sorted lists.** Put a unique tie-breaker before the payload so the heap never compares payloads.

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_k_lists(lists):
    heap = [(node.val, i, node) for i, node in enumerate(lists) if node]
    heapq.heapify(heap)
    dummy = tail = ListNode()
    while heap:
        _, i, node = heapq.heappop(heap)
        tail.next = tail = node
        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))
    return dummy.next
```

**Two heaps for a running median.** Invariant: every value in `low` ≤ every value in `high`, and `len(low)` is `len(high)` or one more.

```python
class MedianFinder:
    def __init__(self):
        self.low = []                     # max-heap via negation
        self.high = []                    # min-heap

    def addNum(self, x):
        heapq.heappush(self.low, -x)
        heapq.heappush(self.high, -heapq.heappop(self.low))   # move the largest low up
        if len(self.high) > len(self.low):
            heapq.heappush(self.low, -heapq.heappop(self.high))

    def findMedian(self):
        if len(self.low) > len(self.high):
            return float(-self.low[0])
        return (-self.low[0] + self.high[0]) / 2
```

**Greedy with a heap: Task Scheduler by simulation.** Run the most frequent available task; tasks cool down in a queue.

```python
from collections import deque


def least_interval(tasks, n):
    heap = [-c for c in Counter(tasks).values()]
    heapq.heapify(heap)
    cooling = deque()                     # (time when available again, -remaining)
    time = 0
    while heap or cooling:
        time += 1
        if heap:
            c = heapq.heappop(heap) + 1   # run one unit of the most frequent task
            if c:
                cooling.append((time + n, c))
        if cooling and cooling[0][0] == time:
            heapq.heappush(heap, cooling.popleft()[1])
    return time
```

**Two heaps for "best affordable" (IPO).** Projects unlock as capital grows; always take the most profitable unlocked one.

```python
def find_maximized_capital(k, w, profits, capital):
    projects = sorted(zip(capital, profits))
    available, i = [], 0
    for _ in range(k):
        while i < len(projects) and projects[i][0] <= w:
            heapq.heappush(available, -projects[i][1])
            i += 1
        if not available:
            break
        w -= heapq.heappop(available)
    return w
```

**Java.** Prefer `Integer.compare` or `Comparator.comparingInt` to subtraction in comparators.

```java
static int findKthLargest(int[] nums, int k) {
    PriorityQueue<Integer> heap = new PriorityQueue<>();          // min-heap
    for (int x : nums) {
        heap.offer(x);
        if (heap.size() > k) heap.poll();
    }
    return heap.peek();
}

static int[][] kClosest(int[][] points, int k) {
    PriorityQueue<int[]> heap = new PriorityQueue<>(
        (a, b) -> Long.compare((long) b[0] * b[0] + (long) b[1] * b[1],
                               (long) a[0] * a[0] + (long) a[1] * a[1]));  // max-heap by distance
    for (int[] p : points) {
        heap.offer(p);
        if (heap.size() > k) heap.poll();
    }
    return heap.toArray(new int[0][]);
}
```

## Complexity

| Operation | Cost |
|---|---|
| push / pop | O(log n) |
| peek | O(1) |
| `heapify` of n items | O(n) |
| top-k of n items with a size-k heap | O(n log k) time, O(k) space |
| merge k lists with N total nodes | O(N log k) |
| running median per insert | O(log n); query O(1) |

## Common bugs

1. Pushing `(val, node)` when values can tie: Python compares the nodes and raises `TypeError` (exercise 1).
2. Java comparators written as `a - b`, which overflow for large magnitudes (exercise 2).
3. Using a max-heap of all n items for top-k: O(n log n) and O(n) memory when O(n log k) and O(k) were possible.
4. Forgetting that `heapq.heapify` returns `None` (it works in place).
5. In two-heap medians, rebalancing before moving the element across, which breaks the ordering invariant.
6. Lazy deletion without a "valid" check when popping, so stale entries are returned.

## Problems (easy → hard)

Lists: **B75** Blind 75 · **N150** NeetCode 150 · **N250** NeetCode 250. ★ = in the [must-do 100](../problem_list.md).

| # | Problem | Level | What it teaches | Lists |
|---|---|---|---|---|
| 1 | [Last Stone Weight](https://leetcode.com/problems/last-stone-weight/) | Easy | max-heap via negation, simulation | N150 · N250 |
| 2 | [Kth Largest Element in a Stream](https://leetcode.com/problems/kth-largest-element-in-a-stream/) | Easy | a size-k min-heap as state | N150 · N250 |
| 3 | ★ [Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/) | Medium | heap O(n log k) vs quickselect O(n) expected | N150 · N250 |
| 4 | ★ [K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/) | Medium | max-heap of size k; compare squared distances | N150 · N250 |
| 5 | [Top K Frequent Words](https://leetcode.com/problems/top-k-frequent-words/) | Medium | ordering ties lexicographically inside the heap key | |
| 6 | ★ [Task Scheduler](https://leetcode.com/problems/task-scheduler/) | Medium | heap + cooldown queue; the closed-form count | N150 · N250 |
| 7 | [Reorganize String](https://leetcode.com/problems/reorganize-string/) | Medium | greedy most-frequent-first with a held-back item | N250 |
| 8 | [Find K Pairs with Smallest Sums](https://leetcode.com/problems/find-k-pairs-with-smallest-sums/) | Medium | lazily expanding a sorted frontier | |
| 9 | [Design Twitter](https://leetcode.com/problems/design-twitter/) | Medium | merging k feeds with a heap | N150 · N250 |
| 10 | ★ [Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/) | Hard | two heaps and their invariant | B75 · N150 · N250 |
| 11 | [IPO](https://leetcode.com/problems/ipo/) | Hard | sorted unlock order + max-heap of options | N250 |
| 12 | [Smallest Range Covering Elements from K Lists](https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/) | Hard | heap of heads + running maximum | |

Also practise [Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/) here (listed under [Pattern 07](07_linked_lists.md)).

## AI-era exercises

**Exercise 1 · Find the crash.**

```python
import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_k_lists_ai(lists):
    heap = [(node.val, node) for node in lists if node]
    heapq.heapify(heap)
    dummy = tail = ListNode()
    while heap:
        _, node = heapq.heappop(heap)
        tail.next = tail = node
        if node.next:
            heapq.heappush(heap, (node.next.val, node.next))
    return dummy.next
```

It passes `[[1, 4, 5], [2, 3, 6]]`. What input makes it crash, and why does the same code work in some other languages?

<details><summary>Answer</summary>

Any input where two heap entries have equal values, such as `[[1], [1]]`: tuples compare element by element, so with equal first elements Python compares the `ListNode` objects and raises `TypeError: '<' not supported between instances of 'ListNode' and 'ListNode'`. Add a unique tie-breaker, `(val, i, node)`, as in the template. Java's `PriorityQueue` with a comparator on `val` alone does not compare the nodes, which is why translated code hides this bug.
</details>

**Exercise 2 · A comparator that lies.** An assistant's Java min-heap:

```java
static int smallestAi(int[] nums) {
    PriorityQueue<Integer> heap = new PriorityQueue<>((a, b) -> a - b);
    for (int x : nums) heap.offer(x);
    return heap.peek();
}
```

Find an input where it returns a value that is not the minimum, and explain.

<details><summary>Answer</summary>

`{Integer.MAX_VALUE, -2}` returns `Integer.MAX_VALUE`: comparing −2 with `MAX_VALUE` computes `-2 - 2147483647`, which overflows to `2147483647`, a positive number, so −2 is ordered *after* `MAX_VALUE`. (With −1 the difference is exactly `Integer.MIN_VALUE` and the bug hides, which is why boundary tests need more than one value.) `a - b` is only safe when the difference cannot overflow. Use `Integer.compare(a, b)` or `Comparator.naturalOrder()`. Ask for the value range whenever you review a comparator.
</details>

## You own this pattern when

- You can say which heap (min or max) a top-k problem needs and why, in one sentence.
- You write Find Median from Data Stream from a blank file with the invariant stated first.
- You never push incomparable payloads without a tie-breaker, and never write `a - b` comparators.
