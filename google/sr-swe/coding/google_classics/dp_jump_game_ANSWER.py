"""
Problem: Jump Game
Link: https://leetcode.com/problems/jump-game/
Topic: DP
Difficulty: Medium

=========================
Explanation
=========================
DP works here (dp[i] = can we reach index i?) but the greedy solution is
simpler and O(1) space — worth knowing both and stating the greedy approach.

Greedy insight: track the farthest index reachable so far. At each index i,
if i > farthest, we can never reach i — return False. Otherwise update
farthest = max(farthest, i + nums[i]) and continue. If we finish the loop,
we can reach the end.

Why greedy works: if we can reach index i, we can reach every index up to
farthest from i. There's no benefit to holding back — using the full jump
length from every reachable index only expands our reach.

DP version for reference: dp[i] = any(dp[j] for j < i if j + nums[j] >= i).
O(n^2) time, O(n) space. The greedy is strictly better here — good to mention
the DP first then optimize to greedy.
=========================
Complexity
=========================
Time:  O(n) — single pass.
Space: O(1) — just the farthest variable.
"""

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0
        for i in range(len(nums)):
            if i > farthest:
                return False
            farthest = max(farthest, i + nums[i])
        return True


if __name__ == "__main__":
    sol = Solution()
    print(sol.canJump([2, 3, 1, 1, 4]))   # True
    print(sol.canJump([3, 2, 1, 0, 4]))   # False
    print(sol.canJump([0]))               # True
    print(sol.canJump([1, 0, 1, 0]))      # False


"""
=========================
Google-asked variations (2-3)
=========================

1. Jump Game II (LeetCode 45, Medium)
   "Find the minimum number of jumps to reach the last index (guaranteed
   reachable)." Greedy BFS-style: track the current jump's range and the
   farthest reachable from that range; when you exhaust the range, increment
   jumps and extend. The same greedy farthest-reach insight, now counting
   levels. A very common direct follow-up.

2. Jump Game III (LeetCode 1306, Medium)
   "From index i you can jump to i+arr[i] or i-arr[i]; can you reach any
   index with value 0?" No longer a greedy problem — the bidirectional jumps
   mean you need BFS/DFS to explore reachability. Tests whether you recognize
   when the greedy assumption breaks (non-monotone jumps).

3. Jump Game VII (LeetCode 1871, Medium)
   "Binary string; from index i jump to any j in [i+minJump, i+maxJump] if
   s[j]=='0'; can you reach the last index?" Window-based BFS or prefix-sum
   optimization — tests range-jump reachability with a variable window, a
   harder generalization of the single fixed-max-jump version.
"""
