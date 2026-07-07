"""
Problem: Word Break
Link: https://leetcode.com/problems/word-break/
Topic: DP
Difficulty: Medium

=========================
Explanation
=========================
The brute-force approach tries every possible split of s recursively — O(2^n)
splits. Many subproblems repeat: "can s[i:] be segmented?" gets recomputed for
the same i many times. That's the overlapping-subproblem signal for DP.

State: dp[i] = True if s[0:i] can be segmented using wordDict.
Recurrence: dp[i] = True if there exists some j < i such that dp[j] is True
AND s[j:i] is in wordDict.
Base case: dp[0] = True (empty string is always valid — zero words needed).

We scan i from 1 to n, and for each i we check all possible last-word endpoints
j. If we find a valid split, dp[i] = True.

Converting wordDict to a set makes the s[j:i] membership check O(1) instead of
O(len(wordDict)).
=========================
Complexity
=========================
Time:  O(n^2 * m) where n = len(s), m = average word length — n^2 pairs (i,j)
       each requiring an O(m) string slice comparison. In practice much faster
       because most slices fail the set lookup immediately.
Space: O(n + W) where W = total characters in wordDict (for the set).
"""

from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break

        return dp[n]


if __name__ == "__main__":
    sol = Solution()
    print(sol.wordBreak("leetcode", ["leet", "code"]))            # True
    print(sol.wordBreak("applepenapple", ["apple", "pen"]))       # True
    print(sol.wordBreak("catsandog", ["cats","dog","sand","and","cat"]))  # False
    print(sol.wordBreak("a", ["b"]))                              # False


"""
=========================
Google-asked variations (2-3)
=========================

1. Word Break II (LeetCode 140, Hard)
   "Return all possible sentences (not just true/false)." The same DP tells you
   WHICH splits are valid, but you must reconstruct all actual sentences —
   backtracking guided by the dp array. Tests whether you can convert a
   boolean-reachability DP into a path-enumeration problem without re-exploring
   dead ends.

2. Concatenated Words (LeetCode 472, Hard)
   "Given a list of words, find all words that are formed by concatenating at
   least two shorter words from the same list." Word Break applied to each word
   where the dictionary is the rest of the list. Tests whether you recognize the
   same sub-problem structure in a new framing.

3. Word Break with minimum cuts / fewest words
   "Return the minimum number of words needed to segment s, or -1 if impossible."
   Change dp[i] from boolean to an integer (min words to reach position i),
   recurrence becomes dp[i] = min(dp[j] + 1) for valid splits. A natural
   "now optimize instead of just checking feasibility" follow-up.
"""
