"""
Problem: Partition Equal Subset Sum
Link: https://leetcode.com/problems/partition-equal-subset-sum/
Topic: DP
Difficulty: Medium

=========================
Explanation
=========================
If we can split the array into two equal-sum subsets, each must sum to
total / 2. So the question reduces to: "can any subset of nums sum to target =
total / 2?" If total is odd, immediately return False.

This is the classic 0/1 knapsack problem: each number can be used at most once,
and we want to know if we can hit an exact target.

State: dp[s] = True if some subset of nums seen so far sums to s.
Recurrence: for each num, update dp[s] = dp[s] OR dp[s - num] for s from
target down to num (iterate in reverse so each num is only "used" once).
Base case: dp[0] = True (empty subset sums to 0).

We iterate s in reverse to avoid using the same number twice in one pass —
the same trick as the space-optimized 0/1 knapsack.
=========================
Complexity
=========================
Time:  O(n * target) where target = sum(nums) / 2 — n numbers, target states each.
Space: O(target) — 1D dp array of size target + 1.
"""

from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2
        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            for s in range(target, num - 1, -1):
                dp[s] = dp[s] or dp[s - num]

        return dp[target]


if __name__ == "__main__":
    sol = Solution()
    print(sol.canPartition([1, 5, 11, 5]))   # True
    print(sol.canPartition([1, 2, 3, 5]))    # False
    print(sol.canPartition([1, 1]))          # True
    print(sol.canPartition([1]))             # False


"""
=========================
Google-asked variations (2-3)
=========================

1. Target Sum (LeetCode 494, Medium)
   "Assign + or - to each number; count assignments that sum to target."
   Reducible to subset-sum: count subsets summing to (total + target) / 2.
   Tests whether you can reframe a sign-assignment problem as a subset-sum
   count (changing dp[s] from boolean to integer count).

2. Coin Change (LeetCode 322, Medium)
   "Unbounded knapsack: coins can be reused; find minimum coins to reach
   target." The same dp array, but iterate s forward (not reverse) to allow
   reuse, and track minimum count instead of boolean reachability. The
   forward vs reverse iteration is the single key difference between 0/1
   knapsack and unbounded knapsack — a crucial distinction to articulate.

3. Last Stone Weight II (LeetCode 1049, Medium)
   "Smash stones together; minimise the last remaining stone weight." Reduces
   to: split stones into two groups minimising |sum_A - sum_B|, which is
   equivalent to finding the largest subset sum <= total/2 — a variant of
   partition equal subset sum where you don't need exact equality.
"""
