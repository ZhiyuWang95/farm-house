"""
Problem: Kth Largest Element in an Array
Link: https://leetcode.com/problems/kth-largest-element-in-an-array/
Topic: Heap
Difficulty: Medium

=========================
Explanation
=========================
Sorting takes O(n log n) and uses O(n) space — but the follow-up constraint
says to do better. The key insight: we don't need all elements sorted, just the
top k.

Use a min-heap of size k. Iterate through nums: push each element onto the heap;
if the heap grows beyond k, pop the minimum. After processing all elements, the
heap contains the k largest values, and the heap's minimum (heap[0]) is the kth
largest.

Why a min-heap (not max-heap): we want to efficiently EVICT the smallest of the
top-k candidates. The heap root is always the current kth-largest threshold —
anything smaller than it gets popped and discarded.

Python's heapq is a min-heap natively, so no negation needed here.

Alternative: quickselect (average O(n), worst O(n^2)) — mention it if the
interviewer pushes for O(n) average. The heap approach is O(n log k) which is
better than O(n log n) when k << n.
=========================
Complexity
=========================
Time:  O(n log k) — n pushes, each heap operation costs O(log k).
Space: O(k) — heap holds at most k elements.
"""

from typing import List
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]


class Solution2:
    """Quickselect with 3-way partition — O(n) average, cleaner than in-place.

    Pick a random pivot and split the array into three groups:
      left  = elements GREATER than pivot  (these are "larger" candidates)
      mid   = elements EQUAL to pivot
      right = elements LESS than pivot

    Since we want the kth largest:
      - If k <= len(left): the answer is in the left (larger) group — recurse there.
      - If k <= len(left) + len(mid): the pivot itself IS the kth largest — return it.
      - Otherwise: the answer is in the right (smaller) group — recurse with
        adjusted k: k - len(left) - len(mid).

    3-way partition is cleaner than in-place because duplicates are handled
    naturally (all copies of the pivot land in mid at once), and the recursion
    logic maps directly to the kth largest definition without index arithmetic.

    Tradeoff vs in-place: uses O(n) extra space per call (new left/mid/right
    lists), but average recursion depth is O(log n) so total space is O(n log n)
    average. In-place quickselect is O(log n) space average. For interviews,
    this version is easier to write correctly under pressure.

    Average O(n): random pivot halves the search space on average.
    Worst O(n²): extremely unlikely with random pivot (would need adversarial input).
    """
    import random

    def findKthLargest(self, nums, k):
        def quick_select(nums, k):
            pivot = random.choice(nums)
            left, mid, right = [], [], []

            for num in nums:
                if num > pivot:
                    left.append(num)
                elif num < pivot:
                    right.append(num)
                else:
                    mid.append(num)
            
            if len(left) >= k:
                return quick_select(left, k)
            
            if len(left) + len(mid) < k:
                return quick_select(right, k - len(left) - len(mid))
            
            return pivot
        
        return quick_select(nums, k)


if __name__ == "__main__":
    sol = Solution()
    print(sol.findKthLargest([3, 2, 1, 5, 6, 4], 2))         # 5
    print(sol.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))  # 4
    print(sol.findKthLargest([1], 1))                          # 1

    sol2 = Solution2()
    print(sol2.findKthLargest([3, 2, 1, 5, 6, 4], 2))         # 5
    print(sol2.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))  # 4
    print(sol2.findKthLargest([1], 1))                         # 1


"""
=========================
Google-asked variations (2-3)
=========================

1. Top K Frequent Elements (LeetCode 347, Medium)
   "Return the k most frequent elements." Same min-heap-of-size-k pattern, but
   the heap key is frequency (from a Counter) rather than the value itself.
   Tests whether you can swap the comparison key while keeping the same
   heap-size-k structure.

2. K Closest Points to Origin (LeetCode 973, Medium)
   "Return the k closest points to origin." Again a min-heap-of-size-k, keyed
   by squared distance (no sqrt needed for comparison). Identical pattern, new
   domain. Google often gives a sequence: Kth Largest → Top K Frequent → K
   Closest to test pattern recognition.

3. Kth Largest in a Stream (LeetCode 703, Easy)
   "Design a class that finds the kth largest element in a growing stream."
   Maintain a persistent min-heap of size k; add() pushes and pops, return
   heap[0]. The static-array problem becomes a streaming design problem — tests
   whether you can make the one-pass heap approach persistent.
"""
