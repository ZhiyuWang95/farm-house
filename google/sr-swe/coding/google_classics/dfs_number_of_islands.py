"""
Problem: Number of Islands
Link: https://leetcode.com/problems/number-of-islands/
Topic: DFS (grid / flood fill)
Difficulty: Medium

Problem statement:
Given an m x n 2D binary grid which represents a map of '1's (land) and
'0's (water), return the number of islands. An island is surrounded by
water and is formed by connecting adjacent lands horizontally or
vertically.

Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.

Approach:
(write your approach/intuition here BEFORE coding)

Complexity:
Time: O(?)
Space: O(?)
"""

from typing import List


# Time: O(M * N)
# Space: O(M * N)
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        counter = 0
        rows = len(grid)
        cols = len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    counter += 1
                    stack = [(i, j)]
                    grid[i][j] = '0'
                    
                    while stack:
                        r, c = stack.pop()
                        for dr, dc in directions:
                            nr = r + dr
                            nc = c + dc
                            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1':
                                grid[nr][nc] = '0'
                                stack.append((nr, nc))
        return counter
