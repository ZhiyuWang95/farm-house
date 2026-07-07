"""
Problem: Max Area of Island
Link: https://leetcode.com/problems/max-area-of-island/
Topic: DFS (flood fill, grid)
Difficulty: Medium

Problem statement:
Given an m x n binary matrix grid (0=water, 1=land), return the maximum area
of an island in the grid. An island is a group of 1s connected 4-directionally.
Return 0 if there is no island.

Example 1:
Input:
[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6

Example 2:
Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0

Constraints:
m == grid.length, n == grid[i].length
1 <= m, n <= 50
grid[i][j] is 0 or 1.

Approach:
(write your approach/intuition here BEFORE coding)

Complexity:
Time: O(?)
Space: O(?)
"""

from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        pass
