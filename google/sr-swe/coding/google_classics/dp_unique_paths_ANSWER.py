"""
Problem: Unique Paths
Link: https://leetcode.com/problems/unique-paths/
Topic: DP
Difficulty: Medium

=========================
Explanation
=========================
The robot can only move right or down, so every path has exactly (m-1) down
moves and (n-1) right moves — total 2D grid of choices. The number of unique
paths is a combinatorics result: C(m+n-2, m-1). But the DP solution is more
generalizable (handles obstacles in Unique Paths II) and is what interviewers
want to see.

State: dp[r][c] = number of unique paths to reach cell (r, c).
Recurrence: dp[r][c] = dp[r-1][c] + dp[r][c-1] (can only arrive from above or
from the left).
Base case: dp[0][c] = 1 for all c (only one way to travel along the top row —
keep going right), dp[r][0] = 1 for all r (only one way along the left column).

Space optimization: since dp[r][c] only depends on the row above and the cell
to the left, we can reduce to a single 1D array, updating left-to-right.
=========================
Complexity
=========================
Time:  O(m * n) — fill every cell once.
Space: O(n) with the 1D optimization (one row at a time), O(m * n) for the
       full 2D table.
"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n
        for _ in range(1, m):
            for c in range(1, n):
                dp[c] += dp[c - 1]
        return dp[n - 1]


if __name__ == "__main__":
    sol = Solution()
    print(sol.uniquePaths(3, 7))   # 28
    print(sol.uniquePaths(3, 2))   # 3
    print(sol.uniquePaths(1, 1))   # 1


"""
=========================
Google-asked variations (2-3)
=========================

1. Unique Paths II (LeetCode 63, Medium)
   "Same grid, but some cells are obstacles (value 1 in obstacleGrid) — paths
   cannot pass through them." Same DP but set dp[r][c] = 0 if the cell is an
   obstacle. A direct "add one constraint to the same recurrence" follow-up.

2. Minimum Path Sum (LeetCode 64, Medium)
   "Each cell has a cost; find the path from top-left to bottom-right with
   minimum total cost." Same move constraints (right/down only), same recurrence
   structure, but dp[r][c] = min(dp[r-1][c], dp[r][c-1]) + grid[r][c] instead
   of a count. Tests whether you can swap "count paths" for "optimize a path"
   in the same DP skeleton.

3. Dungeon Game (LeetCode 174, Hard)
   "Knight starts top-left, must reach bottom-right; each cell adds or removes
   HP; find minimum initial HP so knight survives." Same grid, same moves, but
   now you must work BACKWARDS (bottom-right to top-left) because the constraint
   is on minimum health at each cell, not a sum. Tests whether you can identify
   when reversing the DP direction is necessary.
"""
