"""
Problem: Serialize and Deserialize BST
Link: https://leetcode.com/problems/serialize-and-deserialize-bst/
Topic: Tree (BST pre-order, compact encoding)
Difficulty: Medium

=========================
Explanation
=========================
The general binary tree version (tree_serialize_deserialize.py) needs explicit
null markers because there's no way to infer where a subtree ends. The BST
version doesn't — the BST property (left < root < right) tells us when values
"belong" to the current subtree.

Serialize: pre-order traversal, values separated by spaces. No null markers.

Deserialize: convert string to a queue of integers, then reconstruct using
bounds. The helper `build(lo, hi)` peeks at the front of the queue; if the
next value falls in [lo, hi], it belongs to the current subtree — consume it
as a node and recurse for left (lo to node.val) and right (node.val to hi).
If out of bounds, stop (the current subtree is done).

Why this is more compact: the general tree encodes null nodes, wasting space
proportional to tree size. The BST encoding is exactly n numbers, no extras.

=========================
Complexity
=========================
Time:  O(n) serialize and deserialize
Space: O(n) for the serialized string; O(h) recursion for deserialize
"""

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Codec:
    def serialize(self, root: TreeNode) -> str:
        result = []

        def preorder(node):
            if not node:
                return
            result.append(str(node.val))
            preorder(node.left)
            preorder(node.right)

        preorder(root)
        return " ".join(result)

    def deserialize(self, data: str) -> TreeNode:
        if not data:
            return None
        nums = deque(int(x) for x in data.split())

        def build(lo, hi):
            if not nums or nums[0] < lo or nums[0] > hi:
                return None
            val = nums.popleft()
            node = TreeNode(val)
            node.left = build(lo, val)
            node.right = build(val, hi)
            return node

        return build(float("-inf"), float("inf"))


if __name__ == "__main__":
    def inorder(root):
        if not root:
            return []
        return inorder(root.left) + [root.val] + inorder(root.right)

    root = TreeNode(2, TreeNode(1), TreeNode(3))
    codec = Codec()
    serialized = codec.serialize(root)
    print(serialized)            # "2 1 3"
    reconstructed = codec.deserialize(serialized)
    print(inorder(reconstructed))  # [1, 2, 3]
