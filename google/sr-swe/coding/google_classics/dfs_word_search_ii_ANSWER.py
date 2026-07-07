"""
Problem: Word Search II
Link: https://leetcode.com/problems/word-search-ii/
Topic: DFS (backtracking + Trie)
Difficulty: Hard

=========================
Explanation
=========================
Word Search I (dfs_word_search.py) checks one word per full board DFS: O(m*n*4^L)
per word. With up to 30,000 words, that's too slow. The key upgrade: build a
Trie from all target words, then run ONE backtracking DFS over the board with a
Trie node pointer. At each cell, advance the Trie pointer by the current letter;
if the pointer becomes None (no word has this prefix), prune immediately. If a
Trie node has a `word` marker, we've found a complete word — record it.

Implementation details:
1. Build Trie: each node is a dict of children and an optional `word` string.
2. DFS(r, c, trie_node): check if board[r][c] in trie_node's children.
   If not → prune. If yes → advance to child node, mark cell as '#' (visited),
   recurse on 4 neighbors, restore cell (backtrack).
3. If child node has `word` set → add to results, clear `word` to prevent
   duplicates (Trie pruning: if the node has no children after finding a word,
   you could also remove the node to speed up future DFS calls).

=========================
Complexity
=========================
Time:  O(m * n * 4^L) worst case, but Trie prefix pruning makes it far faster
       in practice. L = max word length.
Space: O(W * L) for the Trie where W = number of words
"""

from typing import List


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Build Trie
        trie = {}
        for word in words:
            node = trie
            for c in word:
                node = node.setdefault(c, {})
            node["$"] = word  # end-of-word marker stores the word itself

        rows, cols = len(board), len(board[0])
        result = []

        def dfs(r, c, node):
            ch = board[r][c]
            if ch not in node:
                return
            child = node[ch]
            if "$" in child:
                result.append(child["$"])
                del child["$"]  # avoid duplicates

            board[r][c] = "#"  # mark visited
            for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != "#":
                    dfs(nr, nc, child)
            board[r][c] = ch  # restore (backtrack)

            if not child:  # prune dead Trie branch
                del node[ch]

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, trie)

        return result


if __name__ == "__main__":
    sol = Solution()
    board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
    print(sorted(sol.findWords(board, ["oath","pea","eat","rain"])))  # ['eat', 'oath']
    print(sol.findWords([["a","b"],["c","d"]], ["abcb"]))             # []
