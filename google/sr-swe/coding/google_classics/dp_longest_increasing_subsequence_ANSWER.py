"""
Problem: Longest Increasing Subsequence
Link: https://leetcode.com/problems/longest-increasing-subsequence/
Topic: DP (also solvable via binary search)
Difficulty: Medium

=========================
Explanation
=========================
Approach 1: O(n^2) DP (start here, then optimize when asked the follow-up)

dp[i] = length of the longest increasing subsequence that ENDS at index i
(not "in the first i elements" -- specifically ending AT i). Base case:
dp[i] = 1 for all i (every element is trivially an increasing subsequence
of length 1 by itself).

Transition: for each i, look at every earlier index j < i. If nums[j] <
nums[i], then we could extend the subsequence ending at j by appending
nums[i]: dp[i] = max(dp[i], dp[j] + 1). Take the max over all valid j.

Answer: max(dp) over all i (the LIS could end anywhere, not necessarily
at the last index).

Approach 2: O(n log n) via binary search ("patience sorting" / greedy
tails array) -- this is the follow-up Google is fishing for.

Maintain an array `tails`, where tails[k] = the smallest possible tail
value of any increasing subsequence of length k+1 found so far. Key
invariant: `tails` is always sorted, which is what makes binary search
valid on it.

For each num in nums: binary search `tails` for the leftmost position
where tails[pos] >= num (i.e. the first existing subsequence-tail that
num could replace to make it smaller, hence more extensible later).
  - If pos == len(tails): num extends the longest subsequence found so
    far -- append num to tails (grows the answer by 1).
  - Otherwise: tails[pos] = num (replace -- this doesn't change the
    LENGTH of the LIS found so far, but means future numbers have an
    easier/smaller tail to beat, keeping all options open).

len(tails) at the end is the answer. The subtlety to articulate out loud:
`tails` does NOT necessarily represent an actual valid subsequence from
the array at the end -- it's a bookkeeping structure of "best possible
tail value for each achievable length," not the LIS itself. Don't get
tripped up trying to read an actual subsequence out of it.

=========================
Complexity
=========================
Approach 1 (DP):              Time O(n^2),     Space O(n).
Approach 2 (binary search):   Time O(n log n), Space O(n) for `tails`.
"""

import bisect
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp) if dp else 0

    def lengthOfLISOptimized(self, nums: List[int]) -> int:
        tails: List[int] = []
        for num in nums:
            pos = bisect.bisect_left(tails, num)
            if pos == len(tails):
                tails.append(num)
            else:
                tails[pos] = num
        return len(tails)


if __name__ == "__main__":
    sol = Solution()
    print(sol.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))         # 4
    print(sol.lengthOfLISOptimized([10, 9, 2, 5, 3, 7, 101, 18]))  # 4
    print(sol.lengthOfLIS([0, 1, 0, 3, 2, 3]))                    # 4
    print(sol.lengthOfLIS([7, 7, 7, 7, 7, 7, 7]))                 # 1


"""
=========================
Google-asked variations (2-3)
=========================

1. Russian Doll Envelopes (LeetCode 354, Hard)
   "Envelopes have (width, height); one fits inside another if both
   dimensions are strictly smaller. Find the max number of envelopes you
   can nest." Reduces to LIS: sort envelopes by width ascending (and
   height DESCENDING as a tiebreak for equal widths, to avoid incorrectly
   chaining same-width envelopes), then find the LIS of the height
   sequence. A classic "2D problem reduces to 1D LIS after the right
   sort" trick Google loves testing.

2. Longest Increasing Subsequence count / reconstruction (no single
   canonical # -- common verbal follow-up: "now print the actual
   subsequence, or count how many distinct LIS's exist")
   The O(n log n) `tails` trick stops giving you this directly -- you'd
   fall back to the O(n^2) DP version and track parent pointers (for
   reconstruction) or a parallel `count[i]` array (for counting distinct
   LIS's of max length). Tests whether you understand the *tradeoff*
   between the two approaches, not just that the faster one exists.

3. Maximum Length of Pair Chain (LeetCode 646, Medium)
   "Given pairs (a, b), chain them so pair2 can follow pair1 if
   pair1[1] < pair2[0]; find the longest chain." Same greedy-interval
   flavor as LIS once you sort by the first element, and is frequently
   compared against LIS to test whether you can tell when a greedy
   interval-scheduling approach suffices (it does here, O(n log n) via
   sorting + greedy) versus when you genuinely need the LIS-style DP/
   binary-search machinery.
"""
