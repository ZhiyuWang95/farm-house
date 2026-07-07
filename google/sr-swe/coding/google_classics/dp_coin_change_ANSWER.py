"""
Problem: Coin Change
Link: https://leetcode.com/problems/coin-change/
Topic: DP (unbounded knapsack)
Difficulty: Medium

=========================
Explanation
=========================
Bottom-up DP over "amount." Define dp[a] = minimum number of coins needed
to make exactly amount a (dp[0] = 0 by definition -- zero coins needed for
zero amount).

Transition: for each amount a from 1 to target, try every coin
denomination c <= a, and consider "use one coin of value c, then
optimally solve the remaining a - c":
    dp[a] = min(dp[a], dp[a - c] + 1)  for every coin c <= a

Initialize dp[1..amount] to infinity (meaning "not yet known to be
reachable"), since not every amount is necessarily makeable. At the end,
dp[amount] is either the answer, or still infinity (meaning impossible,
return -1).

Why this is "unbounded knapsack": each coin can be reused an unlimited
number of times (you have infinite coins of each type), which is exactly
why the transition references dp[a - c] (the same DP array you're
currently building) rather than a previous "row" indexed by which coins
you've used so far, the way bounded/0-1 knapsack problems are structured.

This is THE template for an entire family of "minimum/count ways to
reach a target using a fixed set of building blocks, unlimited reuse"
problems.

=========================
Complexity
=========================
Time:  O(amount * len(coins)) -- for every amount from 1 to target, try
       every coin denomination.
Space: O(amount) -- one DP array indexed by amount.
"""

from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        INF = float("inf")
        dp = [0] + [INF] * amount

        for a in range(1, amount + 1):
            for c in coins:
                if c <= a and dp[a - c] + 1 < dp[a]:
                    dp[a] = dp[a - c] + 1

        return dp[amount] if dp[amount] != INF else -1


if __name__ == "__main__":
    sol = Solution()
    print(sol.coinChange([1, 2, 5], 11))  # 3
    print(sol.coinChange([2], 3))         # -1
    print(sol.coinChange([1], 0))         # 0


"""
=========================
Google-asked variations (2-3)
=========================

1. Coin Change II (LeetCode 518, Medium)
   "Return the NUMBER OF WAYS to make the amount, not the minimum coins."
   Same unbounded-knapsack DP shape, but the transition changes from `min`
   to `sum`: dp[a] += dp[a - c] for each coin. A subtle but important
   ordering detail: you must iterate coins in the OUTER loop and amounts
   in the INNER loop here (opposite nesting from this problem) to avoid
   counting permutations of the same coin combination as distinct ways --
   a classic "got the right DP shape but the loop order silently breaks
   it" trap Google likes to probe.

2. Perfect Squares (LeetCode 279, Medium)
   "Find the minimum number of perfect square numbers (1, 4, 9, 16, ...)
   that sum to n." Identical structure to Coin Change with the "coins"
   replaced by the implicit set of perfect squares <= n. Tests whether you
   recognize the unbounded-knapsack pattern when the "denominations"
   aren't handed to you as an explicit array.

3. Minimum Cost For Tickets (LeetCode 983, Medium)
   "Given specific travel days and ticket costs for 1-day/7-day/30-day
   passes, find the minimum cost to cover all travel days." A disguised
   unbounded-knapsack: the "amount" axis becomes "days," and each ticket
   type is a "coin" that covers a *range* of subsequent days rather than
   subtracting a fixed value -- tests whether you can adapt the
   dp[target] = min(dp[target], dp[target - x] + cost) recurrence when
   the "step back" isn't a simple subtraction but a lookback to "whatever
   day was N days before this ticket's coverage window."
"""
