"""
Problem: Encode and Decode Strings
Link: https://leetcode.com/problems/encode-and-decode-strings/
Topic: String (length-prefix encoding)
Difficulty: Medium

=========================
Explanation
=========================
The constraint "strings may contain any character" rules out all fixed-
delimiter approaches. The standard solution is length-prefix encoding:
encode each string as "<length>#<string>" — the length tells the decoder
exactly how many characters follow, so no separator is needed and the string
content can be arbitrary.

Encode: for each string s, produce f"{len(s)}#{s}". Concatenate all.

Decode: scan the encoded string:
1. Find the next '#' starting from the current position.
2. The number before '#' is the length L.
3. Read exactly L characters after '#' — that's the original string.
4. Advance position past those L characters.
5. Repeat.

This handles empty strings ("0#"), strings containing '#' ("2###" encodes "#"),
and strings with digits correctly because we always look for the '#' separator
and then read a fixed-length slice — we never interpret the string content.

=========================
Complexity
=========================
Time:  O(n) encode and decode where n = total characters across all strings
Space: O(n) for the encoded string
"""

from typing import List


class Codec:
    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            j = s.index("#", i)
            length = int(s[i:j])
            result.append(s[j + 1: j + 1 + length])
            i = j + 1 + length
        return result


if __name__ == "__main__":
    codec = Codec()

    strs = ["lint", "code", "love", "you"]
    encoded = codec.encode(strs)
    print(encoded)             # "4#lint4#code4#love3#you"
    print(codec.decode(encoded))  # ["lint", "code", "love", "you"]

    tricky = ["we", "say", ":", "yes"]
    print(codec.decode(codec.encode(tricky)))  # ["we", "say", ":", "yes"]

    edge = ["", "#", "5#abc"]
    print(codec.decode(codec.encode(edge)))    # ["", "#", "5#abc"]
