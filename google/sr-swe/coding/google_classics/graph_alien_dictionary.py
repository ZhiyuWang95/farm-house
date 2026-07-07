"""
Problem: Alien Dictionary
Link: https://leetcode.com/problems/alien-dictionary/
Topic: Graph (topological sort, string)
Difficulty: Hard

Problem statement:
A new alien language uses English letters but with a different order.
You are given a list of strings words sorted lexicographically by the alien
language's rules. Return a string of unique letters in the alien alphabet order.
If no solution, return "". If multiple valid solutions, return any.

Example 1:
Input: words = ["wrt","wrf","er","ett","rftt"]
Output: "wertf"

Example 2:
Input: words = ["z","x"]
Output: "zx"

Example 3:
Input: words = ["z","x","z"]
Output: ""  (cycle: z before x before z)

Example 4:
Input: words = ["abc","ab"]
Output: ""  (invalid: longer word is prefix of shorter)

Constraints:
1 <= words.length <= 100
1 <= words[i].length <= 100
words[i] consists of only lowercase English letters.

Approach:
(write your approach/intuition here BEFORE coding)

Complexity:
Time: O(?)
Space: O(?)
"""

from typing import List


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        pass
