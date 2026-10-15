# DSA for hiring · Pattern 07 · Linked lists

| Theory first | Time | Problems | Must-do |
|---|---|---|---|
| [FND112](../../../01_year_1_foundations/semester_2/FND112_data_structures_and_algorithms_i/README.md) lessons 5.1, 5.2 | ~8 hours | 15 | 6 |

Linked-list problems test pointer discipline, not algorithms: the right order of assignments, a dummy node to remove the head special case, and fast/slow pointers for positions you cannot index. Draw the boxes and arrows before you type; interviewers notice candidates who do.

## Recognise it

| When you see… | Think… |
|---|---|
| "reverse", "reorder", "rotate" a list | iterative reversal with `prev`, `cur`, `nxt` |
| the head might be deleted or replaced | dummy (sentinel) node before the head |
| "middle", "k-th from the end" | fast/slow pointers, or a gap of k |
| "does it have a cycle / where does it start", "find the duplicate in 1..n" | Floyd's tortoise and hare |
| "merge sorted lists" | dummy node + tail pointer; heap for k lists |
| a list with extra pointers to copy | map old → new, or interleave copies |
| "add numbers stored as lists" | digit-by-digit with a carry |

## Core templates

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def from_list(values):                  # helpers for testing
    dummy = tail = ListNode()
    for v in values:
        tail.next = ListNode(v)
        tail = tail.next
    return dummy.next


def to_list(head):
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out
```

**Reverse.** Save `next` before you overwrite it.

```python
def reverse_list(head):
    prev, cur = None, head
    while cur:
        nxt = cur.next
        cur.next = prev
        prev, cur = cur, nxt
    return prev
```

**Dummy node + tail.** The dummy removes the "is the result empty yet?" branch.

```python
def merge_two_lists(a, b):
    dummy = tail = ListNode()
    while a and b:
        if a.val <= b.val:              # <= keeps the merge stable
            tail.next, a = a, a.next
        else:
            tail.next, b = b, b.next
        tail = tail.next
    tail.next = a or b
    return dummy.next
```

**Gap of n with a dummy.** Start both pointers at the dummy so deleting the head is not special.

```python
def remove_nth_from_end(head, n):
    dummy = ListNode(0, head)
    fast = slow = dummy
    for _ in range(n + 1):
        fast = fast.next
    while fast:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next          # slow is just before the target
    return dummy.next
```

**Floyd's cycle detection.** After the meeting, a pointer from the head and one from the meeting point reach the cycle start together (distance argument: if the tail has length μ and the cycle length λ, the meeting point is μ steps short of a multiple of λ).

```python
def detect_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
        if slow is fast:
            p = head
            while p is not slow:
                p, slow = p.next, slow.next
            return p                    # start of the cycle
    return None
```

**Middle + reverse + weave (Reorder List).** Three templates composed.

```python
def reorder_list(head):
    if not head or not head.next:
        return
    slow, fast = head, head.next
    while fast and fast.next:           # slow ends at the end of the first half
        slow, fast = slow.next, fast.next.next
    second = reverse_list(slow.next)
    slow.next = None
    first = head
    while second:
        n1, n2 = first.next, second.next
        first.next, second.next = second, n1
        first, second = n1, n2
```

**Reverse in groups of k.** Check that k nodes exist before reversing a group.

```python
def reverse_k_group(head, k):
    dummy = ListNode(0, head)
    group_prev = dummy
    while True:
        kth = group_prev
        for _ in range(k):
            kth = kth.next
            if not kth:
                return dummy.next
        group_next = kth.next
        prev, cur = group_next, group_prev.next
        while cur is not group_next:    # reverse the k nodes, attaching to group_next
            nxt = cur.next
            cur.next = prev
            prev, cur = cur, nxt
        first = group_prev.next         # becomes the last node of the group
        group_prev.next = kth
        group_prev = first
```

**Java.**

```java
static class ListNode {
    int val; ListNode next;
    ListNode(int v) { val = v; }
    ListNode(int v, ListNode n) { val = v; next = n; }
}

static ListNode reverseList(ListNode head) {
    ListNode prev = null, cur = head;
    while (cur != null) {
        ListNode nxt = cur.next;
        cur.next = prev;
        prev = cur;
        cur = nxt;
    }
    return prev;
}

static ListNode mergeTwoLists(ListNode a, ListNode b) {
    ListNode dummy = new ListNode(0), tail = dummy;
    while (a != null && b != null) {
        if (a.val <= b.val) { tail.next = a; a = a.next; }
        else { tail.next = b; b = b.next; }
        tail = tail.next;
    }
    tail.next = (a != null) ? a : b;
    return dummy.next;
}
```

## Complexity

All templates are O(n) time and O(1) extra space, except recursion-based versions (O(n) stack) and Copy List with Random Pointer with a hash map (O(n) space; O(1) with interleaving). Merging k lists is O(N log k) with a heap ([Pattern 10](10_heaps_and_top_k.md)) or by pairwise merging.

## Common bugs

1. Losing the rest of the list by overwriting `cur.next` before saving it.
2. No dummy node, so deleting or replacing the head crashes or returns the wrong head (exercise 1).
3. `while fast.next` when `fast` can already be `None`; check `fast and fast.next`.
4. Forgetting to cut the first half (`slow.next = None`) in Reorder List, creating a cycle.
5. Comparing nodes with `==` on values when identity (`is`) is meant, as in cycle and intersection problems.
6. Recursive solutions on long lists: Python's default recursion limit is 1,000 frames (exercise 2).

## Problems (easy → hard)

Lists: **B75** Blind 75 · **N150** NeetCode 150 · **N250** NeetCode 250. ★ = in the [must-do 100](../problem_list.md).

| # | Problem | Level | What it teaches | Lists |
|---|---|---|---|---|
| 1 | ★ [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) | Easy | the three-pointer reversal, iterative and recursive | B75 · N150 · N250 |
| 2 | ★ [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/) | Easy | dummy + tail | B75 · N150 · N250 |
| 3 | ★ [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) | Easy | Floyd, O(1) space vs a visited set | B75 · N150 · N250 |
| 4 | [Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list/) | Easy | which middle for even lengths depends on the start of `fast` | |
| 5 | [Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/) | Easy | middle + reverse second half + compare | |
| 6 | [Intersection of Two Linked Lists](https://leetcode.com/problems/intersection-of-two-linked-lists/) | Easy | switch heads to equalise path lengths | |
| 7 | ★ [Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) | Medium | gap pointers starting at a dummy | B75 · N150 · N250 |
| 8 | ★ [Reorder List](https://leetcode.com/problems/reorder-list/) | Medium | composing middle, reverse and weave | B75 · N150 · N250 |
| 9 | [Add Two Numbers](https://leetcode.com/problems/add-two-numbers/) | Medium | carry handling; the final carry node | N150 · N250 |
| 10 | [Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/) | Medium | the second phase of Floyd and its proof | |
| 11 | [Copy List with Random Pointer](https://leetcode.com/problems/copy-list-with-random-pointer/) | Medium | old → new map; interleaving for O(1) space | N150 · N250 |
| 12 | [Reverse Linked List II](https://leetcode.com/problems/reverse-linked-list-ii/) | Medium | reversing a sub-range in one pass | N250 |
| 13 | [Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/) | Medium | an array as a functional graph; Floyd without nodes | N150 · N250 |
| 14 | ★ [Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/) | Hard | heap of heads or divide and conquer, O(N log k) | B75 · N150 · N250 |
| 15 | [Reverse Nodes in k-Group](https://leetcode.com/problems/reverse-nodes-in-k-group/) | Hard | group boundaries; reconnecting both ends | N150 · N250 |

## AI-era exercises

**Exercise 1 · Find the crash.**

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def remove_nth_from_end_ai(head, n):
    fast = slow = head
    for _ in range(n):
        fast = fast.next
    while fast.next:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return head
```

It passes `[1, 2, 3, 4, 5], n = 2`. Find the whole family of inputs that crash it, and fix it with one extra node.

<details><summary>Answer</summary>

It crashes whenever `n` equals the list length, that is, whenever the head itself must be removed: `[1], n = 1` and `[1, 2], n = 2` raise `AttributeError` on `fast.next` because `fast` is already `None`. The fix is the template version: start both pointers at a dummy node in front of the head, advance `fast` n + 1 times, and return `dummy.next`. Ask any assistant's linked-list code: "what happens when the head changes?"
</details>

**Exercise 2 · A hidden constraint.** An assistant offers the elegant recursive reversal:

```python
def reverse_list_recursive_ai(head):
    if head is None or head.next is None:
        return head
    new_head = reverse_list_recursive_ai(head.next)
    head.next.next = head
    head.next = None
    return new_head
```

What is its space complexity? Run it on a 5,000-node list with CPython's default settings and explain the result. What would you say in an interview where the list can have 10⁶ nodes?

<details><summary>Answer</summary>

It uses O(n) stack space: one frame per node. CPython's default recursion limit is 1,000 (`sys.getrecursionlimit()`), so a 5,000-node list raises `RecursionError` when run locally with defaults. Raising the limit with `sys.setrecursionlimit` only moves the problem, since a deep enough recursion can crash the interpreter. For 10⁶ nodes, say that you would use the iterative version (O(1) space), and mention that Java has the same issue (`StackOverflowError`) with its default thread stack size.
</details>

## You own this pattern when

- You write Reverse Linked List, Merge Two Sorted Lists and Remove Nth Node in under 5 minutes each with no crash on empty and one-node lists.
- You can prove why the second phase of Floyd's algorithm finds the cycle start.
- You draw pointer diagrams for Reverse Nodes in k-Group before coding and get it right in one attempt.
