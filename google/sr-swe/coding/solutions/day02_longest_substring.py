"""
Problem: Longest Substring Without Repeating Characters
Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/
Pattern: Sliding Window
Difficulty: Medium

Approach:
(write your approach/intuition here BEFORE coding)

Complexity:
Time: O(N)
Space: O(N)
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        l = 0
        r = 0
        n = len(s)
        max_length = 0

        while(r < n):
            if s[r] not in char_set:
                char_set.add(s[r])
                r+=1
                max_length = r - l if r - l > max_length else max_length
            else:
                char_set.remove(s[l])
                l+=1
        return max_length

        


# --- Notes / follow-ups discussed ---
s ="pwwkew"
print(Solution().lengthOfLongestSubstring(s))