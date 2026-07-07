"""
Problem: Serialize and Deserialize Binary Tree
Link: https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
Topic: Tree (DFS / pre-order encoding)
Difficulty: Hard

Problem statement:
Serialization is the process of converting a data structure into a
sequence of bits so that it can be stored or transmitted, and later
reconstructed. Design an algorithm to serialize and deserialize a binary
tree. There is no restriction on how your serialization/deserialization
algorithm should work -- you just need to ensure that a binary tree can be
serialized to a string, and this string can be deserialized to the
original tree structure.

Example 1:
Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]

Example 2:
Input: root = []
Output: []

Constraints:
The number of nodes in the tree is in the range [0, 10^4].
-1000 <= Node.val <= 1000

Approach:
(write your approach/intuition here BEFORE coding)

Complexity:
Time: O(?)
Space: O(?)
"""

from typing import Optional


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        pass

    def deserialize(self, data: str) -> Optional[TreeNode]:
        pass
