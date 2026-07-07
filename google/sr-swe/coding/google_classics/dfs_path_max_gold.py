"""
Problem: Path with Maximum Gold
Link: https://leetcode.com/problems/path-with-maximum-gold/
Topic: DFS (backtracking on grid)
Difficulty: Medium

Problem statement:
In a gold mine grid of size m x n, each cell contains an integer representing
gold. Return the maximum amount of gold you can collect under the conditions:
- Every time you are located in a cell you will collect all the gold in that cell.
- From your position, you can walk one step to the left, right, up, or down.
- You can't visit the same cell more than once.
- Never visit a cell with 0 gold.
- You can start and stop collecting gold at any position in the grid.

Example 1:
Input: grid = [[0,6,0],[5,8,7],[0,9,0]]
Output: 24  (path: 9 -> 8 -> 7)

Example 2:
Input: grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
Output: 28  (path: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7)

Constraints:
m == grid.length, n == grid[i].length
1 <= m, n <= 15
0 <= grid[i][j] <= 100
At most 25 cells contain non-zero gold values.

Approach:
(write your approach/intuition here BEFORE coding)

Complexity:
Time: O(?)
Space: O(?)
"""

from typing import List


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        pass
