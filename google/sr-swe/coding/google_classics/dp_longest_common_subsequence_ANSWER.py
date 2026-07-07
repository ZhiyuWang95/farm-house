"""
Problem: Longest Common Subsequence
Link: https://leetcode.com/problems/longest-common-subsequence/
Topic: DP
Difficulty: Medium

=========================
Explanation
=========================
A subsequence doesn't require contiguous characters, so you can't use a sliding
window. The brute force — enumerate all subsequences of both strings — is
exponential. The key insight: when we compare text1[i] and text2[j], we either
match them (if equal) or skip one of them. Both choices lead to strictly smaller
subproblems, and those subproblems repeat — classic DP signal.

State: dp[i][j] = length of LCS of text1[0:i] and text2[0:j].
Recurrence:
  - If text1[i-1] == text2[j-1]: dp[i][j] = dp[i-1][j-1] + 1
  - Else: dp[i][j] = max(dp[i-1][j], dp[i][j-1])
Base case: dp[0][j] = dp[i][0] = 0 (empty string has LCS of 0 with anything).

Space optimization: dp[i][j] only depends on dp[i-1][j-1], dp[i-1][j], and
dp[i][j-1] — we can reduce to two rows (or one with careful indexing).
=========================
Complexity
=========================
Time:  O(m * n) — fill every cell of the (m+1) x (n+1) table once.
Space: O(m * n) for the full table, O(min(m, n)) with the two-row optimization.
"""


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[m][n]


if __name__ == "__main__":
    sol = Solution()
    print(sol.longestCommonSubsequence("abcde", "ace"))   # 3
    print(sol.longestCommonSubsequence("abc", "abc"))     # 3
    print(sol.longestCommonSubsequence("abc", "def"))     # 0
    print(sol.longestCommonSubsequence("", "abc"))        # 0


"""
=========================
Google-asked variations (2-3)
=========================

1. Edit Distance (LeetCode 72, Hard)
   "Find the minimum number of insert/delete/replace operations to convert
   word1 to word2." Uses the same 2D DP table with the same recurrence shape,
   but the "match" branch is free (dp[i-1][j-1]) and the "mismatch" branch
   takes 1 + min of three neighbors. LCS and Edit Distance are the two most
   fundamental 2D string DPs — knowing both and how they differ is a key signal.

2. Shortest Common Supersequence (LeetCode 1092, Medium)
   "Find the shortest string that has both strings as subsequences." The length
   is m + n - LCS(m, n). Reconstructing the actual string requires backtracking
   through the dp table. Tests whether you can go from "compute the length" to
   "reconstruct the solution."

3. Distinct Subsequences (LeetCode 115, Hard)
   "Count the number of ways s's subsequences match t." Same 2D DP table, but
   the recurrence changes: when characters match you ADD dp[i-1][j-1] to
   dp[i-1][j] instead of taking a max. A sharp test of whether you can adapt
   the same table shape for a counting problem vs an optimization problem.
"""
