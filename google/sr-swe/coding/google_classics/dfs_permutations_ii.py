"""
Problem: Permutations II
Link: https://leetcode.com/problems/permutations-ii/
Topic: DFS (backtracking with deduplication)
Difficulty: Medium

Problem statement:
Given a collection of numbers, nums, that might contain duplicates, return all
possible unique permutations in any order.

Example 1:
Input: nums = [1,1,2]
Output: [[1,1,2],[1,2,1],[2,1,1]]

Example 2:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Constraints:
1 <= nums.length <= 8
-10 <= nums[i] <= 10

Approach:
(write your approach/intuition here BEFORE coding)
Hint: This is Permutations I (dfs_permutations.py) with duplicates. The key
addition: sort nums first, then skip nums[i] if it equals nums[i-1] AND
nums[i-1] hasn't been used yet in the current path.

Complexity:
Time: O(?)
Space: O(?)
"""

from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        pass
