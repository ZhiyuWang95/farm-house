"""
Problem: Word Search II
Link: https://leetcode.com/problems/word-search-ii/
Topic: DFS (backtracking + Trie)
Difficulty: Hard

Problem statement:
Given an m x n board of characters and a list of strings words, return all
words in words that can be found in the board (4-directionally adjacent letters,
no reuse of the same cell position).

Example 1:
Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],
       words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]

Example 2:
Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []

Constraints:
m == board.length, n == board[i].length
1 <= m, n <= 12
board[i][j] is a lowercase English letter.
1 <= words.length <= 3 * 10^4
1 <= words[i].length <= 10

Approach:
(write your approach/intuition here BEFORE coding)
Hint: Word Search I checks one word at a time (O(m*n*4^L) per word). With many
words, a Trie lets you check all words simultaneously in one board DFS pass.

Complexity:
Time: O(?)
Space: O(?)
"""

from typing import List


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        pass
