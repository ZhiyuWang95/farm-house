"""
Problem: Serialize and Deserialize BST
Link: https://leetcode.com/problems/serialize-and-deserialize-bst/
Topic: Tree (BST pre-order, compact encoding)
Difficulty: Medium

Problem statement:
Design an algorithm to serialize and deserialize a BST. Unlike the general
binary tree version (tree_serialize_deserialize.py), you can exploit the BST
property to use a more compact encoding without null markers.

Example:
Input: root = [2,1,3]
Output: [2,1,3]  (serialize then deserialize produces the same BST)

Constraints:
0 <= Node.val <= 10^4
All node values are unique (BST property).

Approach:
(write your approach/intuition here BEFORE coding)
Hint: Pre-order serialization of a BST — without null markers — can be
reconstructed using value bounds (the BST property tells you when to stop
assigning nodes to the left vs right subtree).

Complexity:
Time: O(?)
Space: O(?)
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Codec:
    def serialize(self, root: TreeNode) -> str:
        pass

    def deserialize(self, data: str) -> TreeNode:
        pass
