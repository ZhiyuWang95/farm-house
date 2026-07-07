"""
Problem: Word Ladder
Link: https://leetcode.com/problems/word-ladder/
Topic: BFS (shortest path, implicit graph)
Difficulty: Hard

Problem statement:
A transformation sequence from word beginWord to word endWord using a
dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... ->
sk such that:
  - Every adjacent pair of words differs by a single letter.
  - Every si for 1 <= i <= k is in wordList. Note that beginWord does not
    need to be in wordList.
  - sk == endWord.

Given two words, beginWord and endWord, and a dictionary wordList, return
the number of words in the shortest transformation sequence from
beginWord to endWord, or 0 if no such sequence exists.

Example 1:
Input: beginWord = "hit", endWord = "cog",
       wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: "hit" -> "hot" -> "dot" -> "dog" -> "cog", 5 words.

Example 2:
Input: beginWord = "hit", endWord = "cog",
       wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: endWord "cog" is not in wordList, so there's no valid sequence.

Constraints:
1 <= beginWord.length <= 10
endWord.length == beginWord.length
1 <= wordList.length <= 5000
wordList[i].length == beginWord.length
beginWord, endWord, wordList[i] consist of lowercase English letters.
beginWord != endWord
All the words in wordList are unique.

Approach:
(write your approach/intuition here BEFORE coding)

Complexity:
Time: O(?)
Space: O(?)
"""

from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        pass
