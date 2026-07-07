"""
Problem: Encode and Decode Strings
Link: https://leetcode.com/problems/encode-and-decode-strings/
Topic: String (length-prefix encoding)
Difficulty: Medium

Problem statement:
Design an algorithm to encode a list of strings to a single string, and decode
the single string back to the original list. The encoded string is then sent
over the network and decoded back.

The strings may contain any valid ASCII characters, including the delimiter
you choose — so you CANNOT simply join with a fixed delimiter like comma or
space.

Example:
Input:  ["lint","code","love","you"]
Encode: some string
Decode: ["lint","code","love","you"]

Input:  ["we","say",":","yes"]
Encode: some string
Decode: ["we","say",":","yes"]

Constraints:
0 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] contains any ASCII character.

Approach:
(write your approach/intuition here BEFORE coding)
Hint: Can you encode each string with its length so the decoder knows exactly
how many characters to read?

Complexity:
Time: O(?)
Space: O(?)
"""

from typing import List


class Codec:
    def encode(self, strs: List[str]) -> str:
        pass

    def decode(self, s: str) -> List[str]:
        pass
