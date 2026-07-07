"""
Problem: Serialize and Deserialize Binary Tree
Link: https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
Topic: Tree (DFS / pre-order encoding)
Difficulty: Hard

=========================
Explanation
=========================
The key realization: a pre-order traversal (root, then left, then right)
that EXPLICITLY records null children (instead of skipping them) is
enough information to reconstruct the exact tree shape uniquely -- no
extra structural metadata needed.

Serialize: do a pre-order DFS, appending each node's value to a list; when
you hit a None child, append a sentinel marker (e.g. "N") instead of just
skipping it. Join everything with a delimiter (e.g. comma) into one
string.

Deserialize: split the string back into tokens, and use an iterator/index
pointer over them. Recursively rebuild: pop the next token; if it's the
"N" sentinel, return None; otherwise create a TreeNode with that value,
then recursively build its left subtree first, then its right subtree
(matching the exact order values were written in serialize) -- this
mirrors the pre-order structure exactly, since the next unconsumed token
is always "whatever subtree comes next" in the original traversal order.

Why explicit nulls matter: without them, [1,2,3] (1 with left=2, no right)
and [1,null,2,3]-shaped trees could become ambiguous from a pre-order
sequence alone. Recording every None as a placeholder removes that
ambiguity -- this is the single most important detail interviewers are
checking for in this problem.

=========================
Complexity
=========================
Time:  O(n) for both serialize and deserialize -- each node visited once.
Space: O(n) for the string/token list, plus O(h) recursion stack.
"""

from typing import Optional


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        tokens = []

        def dfs(node):
            if node is None:
                tokens.append("N")
                return
            tokens.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(tokens)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        tokens = iter(data.split(","))

        def build():
            val = next(tokens)
            if val == "N":
                return None
            node = TreeNode(int(val))
            node.left = build()
            node.right = build()
            return node

        return build()


if __name__ == "__main__":
    # Build [1,2,3,null,null,4,5]
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)

    codec = Codec()
    data = codec.serialize(root)
    print(data)  # "1,2,N,N,3,4,N,N,5,N,N"
    back = codec.deserialize(data)
    print(back.val, back.left.val, back.right.val,
          back.right.left.val, back.right.right.val)  # 1 2 3 4 5


"""
=========================
Google-asked variations (2-3)
=========================

1. Serialize/Deserialize a BST (LeetCode 449, Medium)
   Same problem, but the tree is guaranteed to be a BST. Because BST
   in-order traversal is always sorted, you can skip the null markers
   entirely: a pre-order traversal alone is enough to reconstruct a BST
   (use the BST property to decide where each subsequent value belongs --
   "everything less than the current node, before the next value greater
   than it, is the left subtree"). Tests whether you'll over-engineer the
   general solution instead of noticing the BST gives you a more compact
   encoding for free.

2. Serialize and Deserialize N-ary Tree (LeetCode 428, Hard, premium but
   commonly asked verbally)
   Generalizes from exactly 2 children to an arbitrary number of children
   per node. The fix: instead of an implicit "always read left then
   right," you must explicitly encode the *number* of children (or a
   sentinel marking "end of this node's children list") before
   recursing into each child. Tests whether you understand *why* binary
   tree serialization gets away with not encoding child count (it's
   always exactly 2 slots) and what breaks when that assumption is gone.

3. Encode and Decode Strings (LeetCode 271, Medium, premium but a classic
   verbal Google question)
   Different domain (a list of arbitrary strings, not a tree), but the
   same core problem: design a reversible string encoding scheme. The
   standard trick (length-prefix each string, e.g. "5#hello3#cat") is the
   spiritual cousin of this problem's delimiter-based encoding -- good to
   bring up if asked "what other serialization design problems have you
   seen," since it tests the same "design an unambiguous wire format"
   instinct in a simpler setting.
"""
