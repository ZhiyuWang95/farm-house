"""
Problem: Top K Frequent Elements
Link: https://leetcode.com/problems/top-k-frequent-elements/
Topic: Heap
Difficulty: Medium

=========================
Explanation
=========================
The naive approach sorts by frequency — O(n log n). But the follow-up asks for
better than O(n log n). Two approaches:

Heap approach (O(n log k)): count frequencies with a Counter, then maintain a
min-heap of size k keyed by frequency. After processing all unique elements,
the heap contains the k most frequent. Heap root is the kth most frequent.

Bucket sort approach (O(n)): since frequency is at most n, create n+1 buckets
indexed by frequency. Place each element in its frequency bucket. Then read
from the highest-frequency bucket down until you've collected k elements.

The heap approach is cleaner and generalizes to streams; bucket sort is O(n) but
only works when you have all elements upfront and frequency is bounded by n.

Python's heapq is min-heap. We store (freq, element) tuples so the smallest
frequency gets evicted when the heap exceeds size k.
=========================
Complexity
=========================
Time:  O(n log k) with heap — n elements, each heap operation O(log k).
       O(n) with bucket sort — count pass + bucket fill + single reverse scan.
Space: O(n) for the frequency map and heap/buckets.
"""

from typing import List
import heapq
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        heap = []
        for num, freq in count.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)
        return [num for freq, num in heap]


class SolutionBucketSort:
    """O(n) bucket sort approach."""
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in count.items():
            buckets[freq].append(num)
        result = []
        for freq in range(len(buckets) - 1, 0, -1):
            for num in buckets[freq]:
                result.append(num)
                if len(result) == k:
                    return result
        return result


if __name__ == "__main__":
    sol = Solution()
    print(sol.topKFrequent([1, 1, 1, 2, 2, 3], 2))   # [1, 2]
    print(sol.topKFrequent([1], 1))                    # [1]


"""
=========================
Google-asked variations (2-3)
=========================

1. Kth Largest Element in an Array (LeetCode 215, Medium)
   The simpler version — no frequency counting, just the kth largest value.
   Same min-heap-of-size-k pattern. Good warm-up before this problem.

2. Sort Characters By Frequency (LeetCode 451, Medium)
   "Sort string so more frequent characters come first." Count frequencies,
   sort by frequency descending (or use a max-heap). Tests the same
   frequency-counting + heap combination but asks for a full sort rather than
   top-k cutoff.

3. Top K Frequent Words (LeetCode 692, Medium)
   "Same problem but for strings; break ties alphabetically." The heap key
   becomes (freq, word) but with alphabetical tie-breaking — in Python, push
   (-freq, word) so the min-heap naturally sorts by descending freq then
   ascending alphabetical order. Tests whether you can handle composite sort
   keys in a heap.
"""
