"""
Problem: Next Permutation
Link: https://leetcode.com/problems/next-permutation/
Topic: Array (permutation, in-place)
Difficulty: Medium

Problem statement:
Given an array of integers nums, find the next permutation of nums — the
next lexicographically greater arrangement. If no such arrangement exists
(already the largest), rearrange to the lowest possible order (ascending).
Must be done in-place with O(1) extra memory.

Example 1:
Input: nums = [1,2,3]
Output: [1,3,2]

Example 2:
Input: nums = [3,2,1]
Output: [1,2,3]

Example 3:
Input: nums = [1,1,5]
Output: [1,5,1]

Constraints:
1 <= nums.length <= 100
0 <= nums[i] <= 100

Approach:
(write your approach/intuition here BEFORE coding)
Hint: Find the rightmost "descent" (position where the sequence stops being
sorted descending). That's where the change needs to happen.

Complexity:
Time: O(?)
Space: O(?)
"""

from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """Do not return anything, modify nums in-place instead."""
        pass
