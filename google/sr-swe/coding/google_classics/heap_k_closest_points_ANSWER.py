"""
Problem: K Closest Points to Origin
Link: https://leetcode.com/problems/k-closest-points-to-origin/
Topic: Heap
Difficulty: Medium

=========================
Explanation
=========================
Same min-heap-of-size-k pattern as Kth Largest, but keyed by squared distance
instead of value. We don't need the actual Euclidean distance (sqrt) — squared
distance preserves ordering and avoids floating-point overhead.

Push (dist_sq, point) onto a max-heap of size k (simulate max-heap with
negation). When the heap exceeds k, the point with the largest distance gets
evicted. After processing all points, the heap contains the k closest.

Alternatively, use heapq.nsmallest(k, points, key=lambda p: p[0]**2 + p[1]**2)
— cleaner one-liner, same O(n log k) complexity.
=========================
Complexity
=========================
Time:  O(n log k) — n points, each heap operation O(log k).
Space: O(k) — heap holds at most k points.
"""

from typing import List
import heapq


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x, y in points:
            dist_sq = x * x + y * y
            heapq.heappush(heap, (-dist_sq, x, y))
            if len(heap) > k:
                heapq.heappop(heap)
        return [[x, y] for _, x, y in heap]


if __name__ == "__main__":
    sol = Solution()
    print(sol.kClosest([[1, 3], [-2, 2]], 1))              # [[-2, 2]]
    print(sol.kClosest([[3, 3], [5, -1], [-2, 4]], 2))     # [[3,3],[-2,4]]


"""
=========================
Google-asked variations (2-3)
=========================

1. Kth Largest Element in an Array (LeetCode 215, Medium)
   The same min-heap-of-size-k pattern with a different key. These two problems
   (K Closest and Kth Largest) together cement the pattern: "maintain a heap of
   size k, evict the worst candidate when it grows beyond k."

2. Find K Pairs with Smallest Sums (LeetCode 373, Medium)
   "Given two sorted arrays, find the k pairs (u,v) with the smallest u+v."
   Min-heap with lazy expansion — start with the k smallest first-array elements
   paired with nums2[0], then expand each pair by incrementing the second index.
   Same heap-based selection, but requires careful indexing to avoid duplicates.

3. Closest Binary Search Tree Value II (LeetCode 272, Hard)
   "Find the k values in a BST closest to a target float." Inorder traversal
   gives sorted values; use a max-heap of size k to maintain the k closest seen
   so far (keyed by |value - target|). Combines BST traversal with the
   heap-of-size-k pattern in a tree setting.
"""
