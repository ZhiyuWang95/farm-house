"""
Problem: Group Anagrams
Link: https://leetcode.com/problems/group-anagrams/
Pattern: Hashmap
Difficulty: Medium

Approach:
(write your approach/intuition here BEFORE coding)

Complexity:
Time: O(?)
Space: O(?)
"""

from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_map = {}

        for i in range(len(strs)):
            the_str = strs[i]
            letters = ''.join(sorted(the_str))
            if letters in strs_map.keys():
                strs_map[letters].append(the_str)
            else:
                strs_map[letters] = [the_str]
        
        result = []
        for key, value in strs_map.items():
            result.append(value)
        return result


# --- Notes / follow-ups discussed ---
#
