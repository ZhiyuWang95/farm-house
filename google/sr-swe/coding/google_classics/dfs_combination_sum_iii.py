"""
Problem: Combination Sum III
Link: https://leetcode.com/problems/combination-sum-iii/
Topic: DFS (backtracking, bounded candidates)
Difficulty: Medium

Problem statement:
Find all valid combinations of k numbers that sum up to n such that the
following conditions are true:
- Only numbers 1 through 9 are used.
- Each number is used at most once.

Return a list of all possible valid combinations. The list must not contain
the same combination twice, and the combinations may be returned in any order.

Example 1:
Input: k = 3, n = 7
Output: [[1,2,4]]

Example 2:
Input: k = 3, n = 9
Output: [[1,2,6],[1,3,5],[2,3,4]]

Example 3:
Input: k = 4, n = 1
Output: []

Constraints:
2 <= k <= 9
1 <= n <= 60

Approach:
(write your approach/intuition here BEFORE coding)
Hint: Same backtracking template as Combination Sum I, but add a count
constraint (exactly k numbers) and use candidates 1-9 without reuse.

Complexity:
Time: O(?)
Space: O(?)
"""

from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        pass
