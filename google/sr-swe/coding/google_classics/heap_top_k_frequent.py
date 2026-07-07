"""
Problem: Top K Frequent Elements
Link: https://leetcode.com/problems/top-k-frequent-elements/
Topic: Heap
Difficulty: Medium

Problem statement:
Given an integer array nums and an integer k, return the k most frequent
elements. You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]

Constraints:
1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.

Follow up: Your algorithm's time complexity must be better than O(n log n),
where n is the array's size.

Approach:
(write your approach/intuition here BEFORE coding)

Complexity:
Time: O(?)
Space: O(?)
"""

from typing import List
import heapq
from collections import Counter

# Time: O(n + n * log k + k) = O(n log k)
# Space: O(n)
# where n is the length of the nums array and k is the number of most frequent elements to return.

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_num = Counter(nums)
        heap = []
        for num, freq in freq_num.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)
        return [num for _, num in heap]

