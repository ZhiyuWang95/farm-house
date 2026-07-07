"""
Problem: Minimum Window Substring
Link: https://leetcode.com/problems/minimum-window-substring/
Topic: Sliding Window
Difficulty: Hard

=========================
Explanation
=========================
Unlike "longest window" problems where we shrink when a constraint breaks, here
we want the SMALLEST window that satisfies a coverage constraint. The pattern
flips: expand right until the window covers all of t, then shrink from the left
as long as coverage is maintained, recording the minimum at each shrink step.

Track coverage with two Counters: need (required frequencies from t) and window
(current frequencies in the window). Track `formed` = number of unique
characters in the window that have met their required frequency. When
formed == len(need), the window is valid — try to shrink.

Shrink by moving left: decrement window[s[left]], and if window[s[left]] drops
below need[s[left]], decrement formed. Then advance left.

This ensures every character is added and removed at most once — O(n) total.
=========================
Complexity
=========================
Time:  O(m + n) where m = len(s), n = len(t) — right and left each traverse s
       once; building need is O(n).
Space: O(m + n) for the two Counters, bounded by the character set size in
       practice (O(1) for fixed alphabet).
"""

from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        need = Counter(t)
        window = {}
        formed = 0
        required = len(need)
        left = 0
        min_len = float("inf")
        result = ""

        for right, char in enumerate(s):
            window[char] = window.get(char, 0) + 1
            if char in need and window[char] == need[char]:
                formed += 1
            while formed == required:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    result = s[left:right + 1]
                left_char = s[left]
                window[left_char] -= 1
                if left_char in need and window[left_char] < need[left_char]:
                    formed -= 1
                left += 1

        return result


if __name__ == "__main__":
    sol = Solution()
    print(sol.minWindow("ADOBECODEBANC", "ABC"))   # "BANC"
    print(sol.minWindow("a", "a"))                 # "a"
    print(sol.minWindow("a", "b"))                 # ""
    print(sol.minWindow("aa", "aa"))               # "aa"


"""
=========================
Google-asked variations (2-3)
=========================

1. Longest Substring Without Repeating Characters (LeetCode 3, Medium)
   The simpler sibling: maximize window length with "no duplicate" invariant.
   These two problems together illustrate the two directions of the sliding
   window template: maximize with a constraint vs minimize while satisfying
   coverage.

2. Permutation in String (LeetCode 567, Medium)
   "Check if any permutation of s1 is a substring of s2." Fixed-size window
   (size = len(s1)) — slide it across s2 and check if the character frequencies
   match. A simpler version of Minimum Window: fixed window size removes the
   need to track `formed` dynamically.

3. Substring with Concatenation of All Words (LeetCode 30, Hard)
   "Find all starting indices where a concatenation of all words (each used
   exactly once) appears in s." Each 'character' is now a word of fixed length
   — apply Minimum Window logic but step by word-length instead of one char.
   Tests whether you can generalize the character-frequency tracking to
   word-frequency tracking with a fixed-word-length stride.
"""
