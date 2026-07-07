"""
Problem: Find Median from Data Stream
Link: https://leetcode.com/problems/find-median-from-data-stream/
Topic: Design / OOD
Difficulty: Hard

=========================
Explanation
=========================
Sorting on every findMedian call is O(n log n) — too slow for a stream. The
insight: we don't need the full sorted order, just the middle element(s).

Split the stream into two halves: a max-heap for the lower half (so the top is
the largest small number) and a min-heap for the upper half (so the top is the
smallest large number). The median is either the top of one heap (odd total) or
the average of both tops (even total).

Invariant to maintain: the heaps are balanced (sizes differ by at most 1), and
every element in the lower half ≤ every element in the upper half.

On addNum: always push to the lower half (max-heap) first, then rebalance by
moving the max of lower to upper if needed. If the upper half becomes larger
than lower, move the min of upper back to lower.

Python's heapq is a min-heap. Simulate max-heap by negating values.
=========================
Complexity
=========================
Time:  addNum O(log n) — heap push/pop. findMedian O(1) — just peek at tops.
Space: O(n) — all elements stored across the two heaps.
"""

import heapq


class MedianFinder:
    def __init__(self):
        self.lower = []   # max-heap (negate values) for lower half
        self.upper = []   # min-heap for upper half

    def addNum(self, num: int) -> None:
        heapq.heappush(self.lower, -num)
        # ensure lower's max <= upper's min
        if self.upper and -self.lower[0] > self.upper[0]:
            heapq.heappush(self.upper, -heapq.heappop(self.lower))
        # rebalance sizes: lower can be equal or 1 larger
        if len(self.lower) > len(self.upper) + 1:
            heapq.heappush(self.upper, -heapq.heappop(self.lower))
        elif len(self.upper) > len(self.lower):
            heapq.heappush(self.lower, -heapq.heappop(self.upper))

    def findMedian(self) -> float:
        if len(self.lower) > len(self.upper):
            return float(-self.lower[0])
        return (-self.lower[0] + self.upper[0]) / 2.0


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
   "Find the median of each window of size k as it slides over the array."
   Same two-heap idea, but now you must also remove elements leaving the window
   — heaps don't support O(1) arbitrary removal. Solution: lazy deletion (mark
   removed elements, skip them when they reach the top). Tests whether you can
   adapt the static two-heap structure to a dynamic sliding window.

2. IPO (LeetCode 502, Hard)
   "Choose at most k projects to maximize capital; each project has a profit and
   minimum capital requirement." Not median, but uses two heaps: a min-heap of
   projects by capital (available projects), and a max-heap of profits (best
   project to pick right now). Tests whether you can apply the "two heaps for
   two sorted views" pattern to a greedy scheduling problem.

3. K-th Largest in a Stream (LeetCode 703, Easy)
   "Design a class that finds the k-th largest element in a stream." A simpler
   version of this problem: just maintain a min-heap of size k (the top is the
   k-th largest). Warm-up before the two-heap median problem — same concept of
   "use a heap to maintain a partial sorted view of the stream."
"""
