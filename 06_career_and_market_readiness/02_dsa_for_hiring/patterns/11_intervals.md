# DSA for hiring · Pattern 11 · Intervals and sweep line

| Theory first | Time | Problems | Must-do |
|---|---|---|---|
| [CS201](../../../02_year_2_core_computer_science/semester_3/CS201_algorithms_and_complexity/README.md) lessons 4.1, 4.2 (interval scheduling, exchange arguments) | ~7 hours | 12 | 4 |

Interval problems are scheduling problems: bookings, meetings, shifts, time ranges in logs. Almost all of them start with **sort by start** (to merge) or **sort by end** (to choose as many non-overlapping intervals as possible), or turn intervals into **+1/−1 events** and sweep. Before coding, ask one clarifying question: do intervals that only touch (`[1, 2]` and `[2, 3]`) overlap? Different problems answer differently.

## Recognise it

| When you see… | Think… |
|---|---|
| "merge overlapping", "union of ranges", "insert into a sorted list of ranges" | sort by start, extend the last merged end |
| "minimum removals so none overlap", "max number of non-overlapping", "min arrows" | sort by end, greedily keep the earliest-ending (exchange argument) |
| "minimum rooms / platforms / servers", "max concurrent sessions" | sweep line over events, or a min-heap of end times |
| "intersection of two sorted interval lists" | two pointers, advance the one that ends first |
| "for each query point, the smallest interval containing it" | sort queries and intervals, heap of candidates |
| "can a person attend all meetings" | sort by start, check adjacent pairs |

## Core templates

**Merge.** After sorting by start, an interval overlaps the merged block exactly when it starts at or before the block's end.

```python
import heapq


def merge(intervals):
    out = []
    for s, e in sorted(intervals):
        if out and s <= out[-1][1]:           # touching counts as overlapping here
            out[-1][1] = max(out[-1][1], e)   # max: a contained interval must not shrink it
        else:
            out.append([s, e])
    return out
```

**Insert into sorted, disjoint intervals.** Three phases: before, overlapping, after.

```python
def insert(intervals, new):
    s, e = new
    out, i, n = [], 0, len(intervals)
    while i < n and intervals[i][1] < s:
        out.append(intervals[i])
        i += 1
    while i < n and intervals[i][0] <= e:
        s, e = min(s, intervals[i][0]), max(e, intervals[i][1])
        i += 1
    out.append([s, e])
    out.extend(intervals[i:])
    return out
```

**Keep the earliest-ending.** Choosing the interval that ends first leaves the most room for the rest; any optimal schedule can be exchanged into this one.

```python
def erase_overlap_intervals(intervals):      # touching does NOT overlap here
    kept, end = 0, float("-inf")
    for s, e in sorted(intervals, key=lambda iv: iv[1]):
        if s >= end:
            kept += 1
            end = e
    return len(intervals) - kept
```

**Sweep line for maximum overlap.** At equal times, process ends before starts so `[1, 5]` and `[5, 10]` share a room.

```python
def min_meeting_rooms(intervals):
    events = []
    for s, e in intervals:
        events.append((s, 1))
        events.append((e, -1))
    events.sort()                             # (t, -1) sorts before (t, 1)
    cur = best = 0
    for _, delta in events:
        cur += delta
        best = max(best, cur)
    return best


def min_meeting_rooms_heap(intervals):
    ends = []                                 # end times of rooms in use
    for s, e in sorted(intervals):
        if ends and ends[0] <= s:
            heapq.heapreplace(ends, e)        # reuse the room that frees first
        else:
            heapq.heappush(ends, e)
    return len(ends)
```

**Intersections of two sorted lists.**

```python
def interval_intersection(A, B):
    i = j = 0
    out = []
    while i < len(A) and j < len(B):
        lo = max(A[i][0], B[j][0])
        hi = min(A[i][1], B[j][1])
        if lo <= hi:
            out.append([lo, hi])
        if A[i][1] < B[j][1]:
            i += 1
        else:
            j += 1
    return out
```

**Queries against intervals (Minimum Interval to Include Each Query).** Add intervals that have started; discard those that ended; the heap top is the smallest valid one.

```python
def min_interval(intervals, queries):
    intervals = sorted(intervals)
    heap, i, ans = [], 0, {}
    for q in sorted(set(queries)):
        while i < len(intervals) and intervals[i][0] <= q:
            l, r = intervals[i]
            heapq.heappush(heap, (r - l + 1, r))
            i += 1
        while heap and heap[0][1] < q:
            heapq.heappop(heap)
        ans[q] = heap[0][0] if heap else -1
    return [ans[q] for q in queries]
```

**Java.** Sort with `Integer.compare`, never `a[0] - b[0]`.

```java
static int[][] merge(int[][] intervals) {
    int[][] a = intervals.clone();
    Arrays.sort(a, (x, y) -> Integer.compare(x[0], y[0]));
    List<int[]> out = new ArrayList<>();
    for (int[] iv : a) {
        if (!out.isEmpty() && iv[0] <= out.get(out.size() - 1)[1]) {
            int[] last = out.get(out.size() - 1);
            last[1] = Math.max(last[1], iv[1]);
        } else {
            out.add(new int[]{iv[0], iv[1]});
        }
    }
    return out.toArray(new int[0][]);
}
```

## Complexity

Sorting dominates: O(n log n) time. Merging, the greedy and the sweep are O(n) after sorting. The heap version of Meeting Rooms II is O(n log n). Intersections of two sorted lists are O(m + n). The query template is O((n + q) log n).

## Common bugs

1. Forgetting `max` when extending the merged end, so `[1, 10]` followed by `[2, 3]` shrinks to `[1, 3]` (exercise 2).
2. Wrong tie-breaking at equal times in a sweep (exercise 1).
3. Sorting by start for the "maximum non-overlapping" greedy; it must be by end.
4. Mutating the input intervals while merging and returning aliases into it.
5. Assuming touching intervals overlap (or not) without checking the statement: Merge Intervals merges `[1, 4]` and `[4, 5]`; Non-overlapping Intervals treats `[1, 2]` and `[2, 3]` as non-overlapping; Minimum Number of Arrows bursts touching balloons together.

## Problems (easy → hard)

Lists: **B75** Blind 75 · **N150** NeetCode 150 · **N250** NeetCode 250. ★ = in the [must-do 100](../problem_list.md).

| # | Problem | Level | What it teaches | Lists |
|---|---|---|---|---|
| 1 | [Meeting Rooms](https://leetcode.com/problems/meeting-rooms/) (Premium; free mirror [LintCode 920](https://www.lintcode.com/problem/920/)) | Easy | sort by start, check neighbours | B75 · N150 · N250 |
| 2 | [Summary Ranges](https://leetcode.com/problems/summary-ranges/) | Easy | building intervals from a sorted array | |
| 3 | ★ [Merge Intervals](https://leetcode.com/problems/merge-intervals/) | Medium | sort by start; extend with `max` | B75 · N150 · N250 |
| 4 | ★ [Insert Interval](https://leetcode.com/problems/insert-interval/) | Medium | three phases, O(n) without re-sorting | B75 · N150 · N250 |
| 5 | ★ [Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/) | Medium | earliest-end greedy and its exchange argument | B75 · N150 · N250 |
| 6 | ★ [Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/) (Premium; free mirror [LintCode 919](https://www.lintcode.com/problem/919/)) | Medium | sweep line vs heap of end times | B75 · N150 · N250 |
| 7 | [Minimum Number of Arrows to Burst Balloons](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/) | Medium | the same greedy with touching = overlapping | |
| 8 | [Interval List Intersections](https://leetcode.com/problems/interval-list-intersections/) | Medium | two pointers on intervals | |
| 9 | [Remove Covered Intervals](https://leetcode.com/problems/remove-covered-intervals/) | Medium | sort by start ascending, end descending | |
| 10 | [My Calendar II](https://leetcode.com/problems/my-calendar-ii/) | Medium | tracking double-booked overlaps | |
| 11 | [Minimum Interval to Include Each Query](https://leetcode.com/problems/minimum-interval-to-include-each-query/) | Hard | offline queries + heap | N150 · N250 |
| 12 | [Data Stream as Disjoint Intervals](https://leetcode.com/problems/data-stream-as-disjoint-intervals/) | Hard | merging on insert with an ordered structure | |

[Car Pooling](https://leetcode.com/problems/car-pooling/) (a capacity sweep) is listed under [Pattern 04](04_prefix_sums.md).

## AI-era exercises

**Exercise 1 · Find the tie-breaking bug.**

```python
def min_meeting_rooms_ai(intervals):
    events = []
    for s, e in intervals:
        events.append((s, 1))
        events.append((e, -1))
    events.sort(key=lambda ev: (ev[0], -ev[1]))
    cur = best = 0
    for _, delta in events:
        cur += delta
        best = max(best, cur)
    return best
```

Find the smallest failing input and explain what the sort key says about a meeting that ends at 5 and one that starts at 5.

<details><summary>Answer</summary>

`[[1, 5], [5, 10]]` returns 2 instead of 1. The key `(time, -delta)` puts starts (`-1`) before ends (`+1`) at the same time, so the second meeting is counted before the first one leaves. The plain tuple sort in the template orders `(5, -1)` before `(5, 1)`, ending first. Whether a meeting ending at 5 frees the room for one starting at 5 is a specification question; ask it, then encode the answer in the tie-break and test the boundary.
</details>

**Exercise 2 · Two wrong merges.** An assistant offered two versions of Merge Intervals:

```python
def merge_ai_v1(intervals):
    out = []
    for s, e in sorted(intervals):
        if out and s <= out[-1][1]:
            out[-1][1] = e
        else:
            out.append([s, e])
    return out


def merge_ai_v2(intervals):
    out = []
    for s, e in sorted(intervals):
        if out and s < out[-1][1]:
            out[-1][1] = max(out[-1][1], e)
        else:
            out.append([s, e])
    return out
```

Give a two-interval failing input for each, and say which bug a random test with values 0..5 finds faster.

<details><summary>Answer</summary>

`merge_ai_v1([[1, 10], [2, 3]])` returns `[[1, 3]]`: a contained interval shrinks the block because `max` is missing. `merge_ai_v2([[1, 4], [4, 5]])` returns `[[1, 4], [4, 5]]` instead of `[[1, 5]]`: touching intervals are not merged. Both appear quickly in random tests over small values compared with a brute force that marks covered points (use half-steps or a closed-interval union so that touching is handled as the problem defines it). The second bug only shows up when an end equals a start, so make sure the generator draws from a small range where equal endpoints are common.
</details>

## You own this pattern when

- You ask about touching intervals before writing any comparison.
- You can prove the earliest-end greedy with an exchange argument in four sentences.
- You solve Meeting Rooms II both ways (sweep and heap) and explain when each is easier to extend.
