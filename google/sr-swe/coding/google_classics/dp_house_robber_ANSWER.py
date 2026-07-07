"""
Problem: House Robber
Link: https://leetcode.com/problems/house-robber/
Topic: DP
Difficulty: Medium

=========================
Explanation
=========================
At each house you make a binary choice: rob it (and skip the previous) or skip
it (and carry forward the best result so far). The naive recursion re-computes
the same subproblems — rob(i) depends on rob(i-2) and rob(i-1), exactly like
Fibonacci. That repeated work signals DP.

State: dp[i] = maximum money robbed from the first i+1 houses.
Recurrence: dp[i] = max(dp[i-1], dp[i-2] + nums[i])
  - dp[i-1]: skip house i, keep whatever was best through house i-1
  - dp[i-2] + nums[i]: rob house i, add to the best through house i-2
Base cases: dp[0] = nums[0], dp[1] = max(nums[0], nums[1]).

Space optimization: dp[i] only depends on the previous two values, so we can
use two variables instead of a full array.
=========================
Complexity
=========================
Time:  O(n) — one pass through the array.
Space: O(1) — only two variables needed.
"""

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        prev2, prev1 = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            prev2, prev1 = prev1, max(prev1, prev2 + nums[i])
        return prev1


if __name__ == "__main__":
    sol = Solution()
    print(sol.rob([1, 2, 3, 1]))      # 4
    print(sol.rob([2, 7, 9, 3, 1]))   # 12
    print(sol.rob([0]))               # 0
    print(sol.rob([1, 2]))            # 2


"""
=========================
Google-asked variations (2-3)
=========================

1. House Robber II (LeetCode 213, Medium)
   "Houses are arranged in a circle — first and last are adjacent." You can't
   rob both ends. Solution: run House Robber I twice — once on nums[0:-1] and
   once on nums[1:] — and take the max. Tests whether you can reduce a new
   constraint to two runs of the original problem.

2. House Robber III (LeetCode 337, Medium)
   "Houses are arranged in a binary tree; can't rob directly connected nodes."
   The same rob/skip recurrence, but now applied to a tree via DFS. Each node
   returns (rob_this_node, skip_this_node) up to its parent. Tests whether you
   can transfer a linear DP pattern onto a tree structure.

3. Delete and Earn (LeetCode 740, Medium)
   "Pick a number x, earn x points, but must delete all x-1 and x+1 values.
   Maximize total points." This reduces to House Robber: build an array where
   index i holds the total points from picking number i (i * count(i)), then
   apply House Robber on this array. Tests whether you can recognize a
   disguised instance of a known DP pattern.
"""
