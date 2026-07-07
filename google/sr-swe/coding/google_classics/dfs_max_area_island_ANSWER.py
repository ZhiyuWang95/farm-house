"""
Problem: Max Area of Island
Link: https://leetcode.com/problems/max-area-of-island/
Topic: DFS (flood fill, grid)
Difficulty: Medium

=========================
Explanation
=========================
Same flood-fill DFS as Number of Islands (dfs_number_of_islands.py), with
one addition: the DFS returns the size of the connected component instead of
just marking it visited. Track the global maximum across all islands.

For each unvisited land cell (grid[r][c] == 1), DFS explores all 4-directionally
connected land cells, marking each as 0 (visited) and accumulating a count.
The global maximum is updated after each DFS call.

Returning the count from DFS (rather than using a global counter) is slightly
cleaner and avoids class-level state. Either approach is correct.

Difference from Number of Islands: that problem counts distinct components;
this problem measures the LARGEST component's size. Both use identical DFS
flood-fill mechanics — the variation is only in what you accumulate.

=========================
Complexity
=========================
Time:  O(m * n) — each cell visited at most once
Space: O(m * n) recursion stack worst case (all land)
"""

from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c) -> int:
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != 1:
                return 0
            grid[r][c] = 0
            return 1 + dfs(r+1,c) + dfs(r-1,c) + dfs(r,c+1) + dfs(r,c-1)

        max_area = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    max_area = max(max_area, dfs(r, c))
        return max_area


if __name__ == "__main__":
    sol = Solution()
    grid = [
        [0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0],
    ]
    print(sol.maxAreaOfIsland(grid))              # 6
    print(sol.maxAreaOfIsland([[0,0,0,0,0,0,0,0]]))  # 0
