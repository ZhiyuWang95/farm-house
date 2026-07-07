"""
Problem: Kth Largest Element in an Array
Link: https://leetcode.com/problems/kth-largest-element-in-an-array/
Topic: Heap
Difficulty: Medium

Problem statement:
Given an integer array nums and an integer k, return the kth largest element
in the array.

Note that it is the kth largest element in the sorted order, not the kth
distinct element.

Can you solve it without sorting?

Example 1:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Example 2:
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4

Constraints:
1 <= k <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4

Approach:
(write your approach/intuition here BEFORE coding)

Complexity:
Time: O(?)
Space: O(?)
"""

from typing import List
import heapq


class Solution:
    # Quickselect solution
    # Time: O(n) average, O(n^2) worst case
    # Space: O(1)
    def findKthLargestQuickselect(self, nums: List[int], k: int) -> int:
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
            
            left_size = len(left)
            left_mid_size = len(left) + len(mid)

            if k <= left_size:                        # kth largest is in the bigger half
                return quick_select(left, k)
            elif k > left_mid_size:                   # kth largest is in the smaller half
                return quick_select(right, k - left_mid_size)
            else:                                     # kth largest is the pivot itself
                return pivot
        
        return quick_select(nums, k)


    # Heap solution

    # Time: O(n log k)
    # Space: O(k)
    def findKthLargestHeap(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]
