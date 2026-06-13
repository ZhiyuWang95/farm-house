"""
Problem: Container With Most Water
Link: https://leetcode.com/problems/container-with-most-water/
Pattern: Two Pointers
Difficulty: Medium

Approach:
(write your approach/intuition here BEFORE coding)

Complexity:
Time: O(N)
Space: O(1)
"""

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        l_height = height[l]
        r_height = height[r]
        max_area = (r - l) * min(l_height, r_height)

        while (l < r):
            if l_height < r_height:
                l += 1
                l_height = height[l]
            else:
                r -= 1
                r_height = height[r]
            max_area = (r - l) * min(l_height, r_height) if (r - l) * min(l_height, r_height) > max_area else max_area
        return max_area

# --- Notes / follow-ups discussed ---
#
height = [1,8,6,2,5,4,8,3,7]
print(Solution().maxArea(height))