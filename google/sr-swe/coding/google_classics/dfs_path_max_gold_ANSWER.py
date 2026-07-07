"""
Problem: Path with Maximum Gold
Link: https://leetcode.com/problems/path-with-maximum-gold/
Topic: DFS (backtracking on grid)
Difficulty: Medium

=========================
Explanation
=========================
Brute-force backtracking: start DFS from every non-zero cell, explore all
possible paths, and return the maximum gold collected. Classic mark/recurse/
unmark pattern — set the cell to 0 before recursing (marks visited), restore
after (unmarks for other paths from the same starting cell).

Why backtracking works (not just flood fill): we want the MAX-SUM path, not
a count of reachable cells. Different starting points and path shapes yield
different sums, so we must try all possibilities. The DFS returns the gold
collected along the BEST path from the current cell.

Key differences from Number of Islands / Max Area of Island:
- We restore cells after backtracking (marks are temporary, not permanent).
- We maximize a running SUM, not a count of visited cells.
- We start from every non-zero cell (not just unvisited ones) because a cell
  that was part of a previous starting-point's path must be available as a
  starting point itself.

The constraint "at most 25 non-zero cells" keeps this tractable despite
the exponential worst-case complexity.

=========================
Complexity
=========================
Time:  O(k * 4^k) where k = number of non-zero cells (at most 25)
Space: O(k) recursion depth
"""

from typing import List


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c) -> int:
            gold = grid[r][c]
            grid[r][c] = 0  # mark visited
            best = 0
            for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != 0:
                    best = max(best, dfs(nr, nc))
            grid[r][c] = gold  # unmark (backtrack)
            return gold + best

        max_gold = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != 0:
                    max_gold = max(max_gold, dfs(r, c))
        return max_gold


if __name__ == "__main__":
    sol = Solution()
    print(sol.getMaximumGold([[0,6,0],[5,8,7],[0,9,0]]))             # 24
    print(sol.getMaximumGold([[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]))  # 28
