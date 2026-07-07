"""
Problem: Combination Sum II
Link: https://leetcode.com/problems/combination-sum-ii/
Topic: DFS (backtracking with deduplication)
Difficulty: Medium

Problem statement:
Given a collection of candidate numbers (candidates) and a target number
(target), find all unique combinations in candidates where the candidate
numbers sum to target. Each number in candidates may only be used ONCE.
The solution set must not contain duplicate combinations.

Example 1:
Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: [[1,1,6],[1,2,5],[1,7],[2,6]]

Example 2:
Input: candidates = [2,5,2,1,2], target = 5
Output: [[1,2,2],[5]]

Constraints:
1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30

Approach:
(write your approach/intuition here BEFORE coding)
Hint: Compare to Combination Sum I (dfs_combination_sum.py):
- No reuse: recurse with i+1 instead of i.
- Duplicates: add a skip guard when candidates[i] == candidates[i-1] AND i > start.

Complexity:
Time: O(?)
Space: O(?)
"""

from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        pass
