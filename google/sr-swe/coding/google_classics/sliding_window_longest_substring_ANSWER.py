"""
Problem: Longest Substring Without Repeating Characters
Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/
Topic: Sliding Window
Difficulty: Medium

=========================
Explanation
=========================
The window invariant: the substring s[left:right+1] contains no duplicate
characters. We expand right one character at a time. When we encounter a
duplicate (s[right] already in our window), we shrink from the left until the
duplicate is removed.

Use a hashmap {char → last_seen_index} instead of a set for O(1) shrinking:
when a duplicate at index right is found, jump left directly to
last_seen[s[right]] + 1 instead of advancing left one step at a time.

Important: when jumping left, never move it backwards — take max(left,
last_seen[char] + 1). This handles characters that were seen before the current
window's left boundary.
=========================
Complexity
=========================
Time:  O(n) — right pointer moves n steps; left moves at most n steps total
       (not per iteration). Each character is visited at most twice.
Space: O(min(n, m)) where m is the size of the character set — the hashmap
       holds at most one entry per unique character in the window.
"""

from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}
        left = 0
        best = 0
        for right, char in enumerate(s):
            if char in last_seen:
                left = max(left, last_seen[char] + 1)
            last_seen[char] = right
            best = max(best, right - left + 1)
        return best


if __name__ == "__main__":
    sol = Solution()
    print(sol.lengthOfLongestSubstring("abcabcbb"))  # 3
    print(sol.lengthOfLongestSubstring("bbbbb"))     # 1
    print(sol.lengthOfLongestSubstring("pwwkew"))    # 3
    print(sol.lengthOfLongestSubstring(""))          # 0


"""
=========================
Google-asked variations (2-3)
=========================

1. Longest Substring with At Most K Distinct Characters (LeetCode 340, Medium)
   "Find the longest substring with at most k distinct characters." Same
   sliding window but the shrink condition changes from "any duplicate" to
   "more than k distinct characters in window." Use a Counter; shrink when
   len(counter) > k. Tests whether you can generalize the "no duplicate"
   invariant to "at most k distinct."

2. Minimum Window Substring (LeetCode 76, Hard)
   The harder sibling: instead of maximizing the window with a constraint, you
   minimize it while satisfying a coverage requirement. Same two-pointer
   structure, but the expand/shrink roles are swapped (expand until satisfied,
   shrink while still satisfied).

3. Longest Substring with At Least K Repeating Characters (LeetCode 395, Medium)
   "Find the longest substring where every character appears at least k times."
   NOT a standard sliding window — the window shrink condition is non-monotone.
   Solved with divide-and-conquer (split at characters appearing < k times) or
   a sliding window over the number of unique characters. A good test of
   recognizing when the standard template doesn't apply.
"""
