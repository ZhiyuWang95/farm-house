"""
Problem: House Robber II
Link: https://leetcode.com/problems/house-robber-ii/
Topic: DP
Difficulty: Medium

=========================
Explanation
=========================
The only difference from House Robber I is that the houses form a circle, making
house 0 and house n-1 adjacent. If you rob house 0 you can't rob house n-1, and
vice versa.

The key insight: break the circle constraint by running House Robber I twice on
two overlapping subarrays that exclude one endpoint each:
  - nums[0 : n-1]  (include first house, exclude last)
  - nums[1 : n]    (exclude first house, include last)

The answer is max of the two runs. This works because the optimal solution must
either include house 0 or not — these two cases cover all possibilities, and
within each case the circle constraint is gone (it's a linear subarray).

Edge case: n == 1 — only one house, just return nums[0].
=========================
Complexity
=========================
Time:  O(n) — two linear passes.
Space: O(1) — two-variable rolling update in each pass.
"""

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def rob_linear(houses: List[int]) -> int:
            if not houses:
                return 0
            if len(houses) == 1:
                return houses[0]
            prev2, prev1 = houses[0], max(houses[0], houses[1])
            for i in range(2, len(houses)):
                prev2, prev1 = prev1, max(prev1, prev2 + houses[i])
            return prev1

        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))


if __name__ == "__main__":
    sol = Solution()
    print(sol.rob([2, 3, 2]))      # 3
    print(sol.rob([1, 2, 3, 1]))   # 4
    print(sol.rob([1, 2, 3]))      # 3
    print(sol.rob([1]))            # 1


"""
=========================
Google-asked variations (2-3)
=========================

1. House Robber I (LeetCode 198, Medium)
   The linear version — always do this first, then extend to the circular case.
   The "run the linear version twice on subarrays" trick is a reusable pattern:
   whenever a circular constraint appears, break it by fixing one element in/out
   and running the linear version on both cases.

2. House Robber III (LeetCode 337, Medium)
   "Houses on a binary tree — can't rob parent and child simultaneously." The
   circle-breaking trick doesn't directly apply here; instead use tree DFS
   where each call returns (max_if_rob_this, max_if_skip_this). Shows the
   same rob/skip DP on a different topology.

3. Maximum Sum of Non-Adjacent Elements in a Circle (general variant)
   The same "split into two linear subproblems" technique appears whenever you
   have a circular array with a non-adjacency constraint — e.g., scheduling
   tasks in a circular queue, or picking non-adjacent nodes in a ring graph.
   Recognizing this pattern generalizes well beyond the house-robbing framing.
"""
