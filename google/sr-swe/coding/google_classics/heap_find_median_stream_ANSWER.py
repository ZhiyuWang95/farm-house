"""
Problem: Find Median from Data Stream
Link: https://leetcode.com/problems/find-median-from-data-stream/
Topic: Heap
Difficulty: Hard

=========================
Explanation
=========================
Naive: keep a sorted list, insert with bisect (O(n) per addNum due to shift),
read middle in O(1). Too slow at 5*10^4 calls.

Key insight: we don't need the full sorted order — just the middle value(s).
Split the stream into two halves using two heaps:

  lower: max-heap — stores the smaller half  (negate values for Python)
  upper: min-heap — stores the larger half

Invariant after every addNum:
  1. Every value in lower <= every value in upper  (ordering)
  2. len(lower) == len(upper)  OR  len(lower) == len(upper) + 1  (size balance)

With this invariant, findMedian is O(1):
  - Odd total: lower has one extra → median is lower's max
  - Even total: median is average of lower's max and upper's min

addNum three-step process:
  1. Always push to lower first (single entry point).
  2. Fix ordering: if lower's max > upper's min, move lower's max to upper.
  3. Rebalance: step 1 always grows lower, step 2 can equalize them — so only
     lower can ever be too large. If lower has 2+ more than upper, move one over.

=========================
Complexity
=========================
Time:  O(log n) per addNum — each step does at most 2 heap operations.
       O(1) per findMedian — just peek at both heap tops.
Space: O(n) — both heaps together hold all n elements.
"""

import heapq


class MedianFinder:
    def __init__(self):
        self.lower = []   # max-heap (negated) — smaller half
        self.upper = []   # min-heap — larger half

    def addNum(self, num: int) -> None:
        # step 1: always push to lower first
        heapq.heappush(self.lower, -num)

        # step 2: fix ordering — lower's max must be <= upper's min
        if self.upper and -self.lower[0] > self.upper[0]:
            heapq.heappush(self.upper, -heapq.heappop(self.lower))

        # step 3: rebalance sizes — lower can be equal or 1 larger
        if len(self.lower) > len(self.upper) + 1:
            heapq.heappush(self.upper, -heapq.heappop(self.lower))
        elif len(self.upper) > len(self.lower):
            heapq.heappush(self.lower, -heapq.heappop(self.upper))

    def findMedian(self) -> float:
        if len(self.lower) > len(self.upper):   # odd total — lower has the middle
            return float(-self.lower[0])
        return (-self.lower[0] + self.upper[0]) / 2.0   # even total — average both tops


if __name__ == "__main__":
    mf = MedianFinder()
    mf.addNum(1)
    mf.addNum(2)
    print(mf.findMedian())   # 1.5
    mf.addNum(3)
    print(mf.findMedian())   # 2.0
    mf.addNum(4)
    print(mf.findMedian())   # 2.5


"""
=========================
Google-asked variations (2-3)
=========================

1. Sliding Window Median (LeetCode 480, Hard)
   "Find the median of every window of size k as it slides across the array."
   Same two-heap structure, but now you also need to REMOVE elements as they
   fall out of the window — heaps don't support arbitrary removal efficiently,
   so the trick is lazy deletion (mark removed elements, skip them when they
   reach the top). Much harder than this problem; rarely asked cold.

2. K-th Largest Element in a Stream (LeetCode 703, Easy)
   "Design a class that always returns the kth largest element after each add."
   Simpler sibling: just maintain a min-heap of size k — the root is always
   the kth largest. No two-heap balancing needed.

3. IPO (LeetCode 502, Hard)
   "Given projects with profit/capital requirements, pick at most k projects
   to maximize profit starting with capital w." Uses TWO heaps differently:
   a min-heap of (capital, profit) sorted by capital to find affordable
   projects, and a max-heap of profit to always pick the most profitable
   available one. Tests whether you can combine two heaps for a greedy
   strategy rather than for median-finding.
"""
