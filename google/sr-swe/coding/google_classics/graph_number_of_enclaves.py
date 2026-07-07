"""
Problem: Number of Enclaves
Link: https://leetcode.com/problems/number-of-enclaves/
Topic: Graph (DFS/BFS from boundary)
Difficulty: Medium

Problem statement:
Given an m x n binary matrix grid (0=sea, 1=land), return the number of land
cells from which you CANNOT walk off the boundary in any number of moves.
(4-directional movement between adjacent land cells.)

Example 1:
Input: grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
Output: 3

Example 2:
Input: grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
Output: 0  (the island touches the border)

Constraints:
m == grid.length, n == grid[i].length
1 <= m, n <= 500
grid[i][j] is 0 or 1.

Approach:
(write your approach/intuition here BEFORE coding)

Complexity:
Time: O(?)
Space: O(?)
"""

from typing import List


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        pass
