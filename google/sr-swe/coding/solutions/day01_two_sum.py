"""
Problem: Two Sum
Link: https://leetcode.com/problems/two-sum/
Pattern: Hashmap
Difficulty: Easy

Approach:
(write your approach/intuition here BEFORE coding)

Complexity:
Time: O(?)
Space: O(?)
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        gap_cache = {} # key: gap of nums[index] to target; value: index

        for i in range(len(nums)):
            num = nums[i]
            gap = target - num

            if num in gap_cache.keys():
                return [gap_cache[num], i]
            else:
                gap_cache[gap] = i
        
        return []

# --- Notes / follow-ups discussed ---
#
nums = [2, 7, 11, 15]
target = 9
print(Solution().twoSum(nums, target))