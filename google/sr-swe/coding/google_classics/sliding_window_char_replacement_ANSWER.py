"""
Problem: Longest Repeating Character Replacement
Link: https://leetcode.com/problems/longest-repeating-character-replacement/
Topic: Sliding Window
Difficulty: Medium

=========================
Explanation
=========================
Key insight: a window of length L is valid if (L - max_freq_in_window) <= k,
where max_freq_in_window is the count of the most frequent character. The
"replacements needed" = characters that aren't the dominant one = L - max_freq.

Expand right always. Only shrink when the window becomes invalid:
(window_size - max_freq) > k → shrink left by 1.

The clever optimization: we never shrink max_freq when we move left. This seems
wrong but is intentional — we only care if max_freq INCREASES (meaning we found
a longer valid window). If it doesn't increase, the window size stays the same
(we shrink by 1 when we advance right), so we never record a smaller answer.
We're looking for the maximum window, not every valid window.

This means max_freq can be a stale overestimate, but that's fine — it only
causes us to NOT shrink when we could have, never to shrink incorrectly.
=========================
Complexity
=========================
Time:  O(n) — right moves n steps; left moves at most n steps total. The 26
       character count array lookup is O(1).
Space: O(1) — count array of size 26.
"""


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0] * 26
        max_freq = 0
        left = 0
        result = 0

        for right in range(len(s)):
            count[ord(s[right]) - ord('A')] += 1
            max_freq = max(max_freq, count[ord(s[right]) - ord('A')])
            while (right - left + 1) - max_freq > k:
                count[ord(s[left]) - ord('A')] -= 1
                left += 1
            result = max(result, right - left + 1)

        return result


if __name__ == "__main__":
    sol = Solution()
    print(sol.characterReplacement("ABAB", 2))      # 4
    print(sol.characterReplacement("AABABBA", 1))   # 4
    print(sol.characterReplacement("AAAA", 2))      # 4
    print(sol.characterReplacement("ABCD", 0))      # 1


"""
=========================
Google-asked variations (2-3)
=========================

1. Max Consecutive Ones III (LeetCode 1004, Medium)
   "Given a binary array, flip at most k zeros; find the longest subarray of
   1s." Identical structure: window is valid when (zeros in window) <= k.
   A direct simplification of this problem where 'max frequency' is always the
   count of 1s, and 'replacements needed' is the count of 0s.

2. Longest Subarray of 1s After Deleting One Element (LeetCode 1493, Medium)
   "Delete exactly one element; find the longest subarray of 1s." k=1 special
   case of Max Consecutive Ones III. Good as a warm-up before the general
   version.

3. Minimum Number of Operations to Make Array Continuous (LeetCode 2009, Hard)
   "Replace elements to make the array contain n consecutive distinct integers;
   minimize replacements." Sliding window over the sorted unique values — window
   size is how many elements we keep unchanged; we want to maximize the window
   where max - min < n. Tests whether you can apply the "replacements = size -
   max_valid_count" reasoning to an array (not string) context.
"""
