"""
Problem: Number of Enclaves
Link: https://leetcode.com/problems/number-of-enclaves/
Topic: Graph (DFS from boundary, count enclosed)
Difficulty: Medium

=========================
Explanation
=========================
Same boundary-DFS / reverse-source pattern as Surrounded Regions, but instead
of flipping enclosed cells, we just count them.

1. DFS from every border land cell (grid[r][c] == 1 on any edge): mark all
   connected land cells as visited by setting them to 0.
2. After the DFS pass, sum all remaining 1s — those are enclaves unreachable
   from any boundary.

Why not DFS from each interior cell to check if it can reach the boundary?
That would be O(m*n) per cell = O(m^2 * n^2) total. Starting from the border
and marking outward is O(m * n) total because every cell is visited at most once
across all DFS calls.

Relationship to Surrounded Regions: nearly identical logic, simpler output
(count instead of flip). Both use the "reverse source = flood from boundary"
technique to avoid expensive per-cell reachability checks.

=========================
Complexity
=========================
Time:  O(m * n)
Space: O(m * n) recursion stack worst case
"""

from typing import List


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != 1:
                return
            grid[r][c] = 0
            for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                dfs(r + dr, c + dc)

        for r in range(rows):
            dfs(r, 0)
            dfs(r, cols - 1)
        for c in range(cols):
            dfs(0, c)
            dfs(rows - 1, c)

        return sum(grid[r][c] for r in range(rows) for c in range(cols))


if __name__ == "__main__":
    sol = Solution()
    print(sol.numEnclaves([[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]))  # 3
    print(sol.numEnclaves([[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]))  # 0
