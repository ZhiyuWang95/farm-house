"""
Problem: Word Search
Link: https://leetcode.com/problems/word-search/
Topic: DFS (backtracking, grid)
Difficulty: Medium

=========================
Explanation
=========================
This extends the Number of Islands flood-fill template with the
defining feature of BACKTRACKING: you need to UNDO the "visited" mark
when a path doesn't pan out, because the same cell might be reusable on a
different attempted path.

Try every cell as a possible starting point for word[0]. From a matching
cell, DFS recursively: to match word[i] at (r, c), the current cell's
letter must equal word[i], then recurse into the 4 neighbors looking for
word[i+1]. Base case: if i == len(word), you've matched the whole word --
return True.

The backtracking step that's easy to forget: before recursing into
neighbors, mark the current cell as visited (e.g. swap it to a sentinel
character so it can't be reused in *this* path); after all 4 directions
have been tried and failed, restore the original character before
returning, so that a *different* starting path (which may legitimately
need to pass through this same cell) isn't incorrectly blocked.

This "mark, recurse, unmark" pattern is THE backtracking template --
internalize it once and it transfers directly to Permutations, Subsets,
Combination Sum, N-Queens, etc.

=========================
Complexity
=========================
Time:  O(m * n * 4 * 3^(L-1)) where L = len(word) -- m*n possible starting
       cells, and from each subsequent step there are at most 3 unexplored
       directions (can't backtrack into the cell you just came from in a
       simple path). This is exponential in word length but bounded tight
       by the small constraints (L <= 15).
Space: O(L) -- recursion depth equals the word length.
"""

from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def backtrack(r: int, c: int, i: int) -> bool:
            if i == len(word):
                return True
            if (
                r < 0 or r >= rows or c < 0 or c >= cols
                or board[r][c] != word[i]
            ):
                return False

            original = board[r][c]
            board[r][c] = "#"  # mark visited for this path only

            found = (
                backtrack(r + 1, c, i + 1)
                or backtrack(r - 1, c, i + 1)
                or backtrack(r, c + 1, i + 1)
                or backtrack(r, c - 1, i + 1)
            )

            board[r][c] = original  # un-mark: this cell may be reusable
            #                          on a different path
            return found

        for r in range(rows):
            for c in range(cols):
                if backtrack(r, c, 0):
                    return True
        return False


if __name__ == "__main__":
    board = [
        list("ABCE"),
        list("SFCS"),
        list("ADEE"),
    ]
    sol = Solution()
    print(sol.exist(board, "ABCCED"))  # True
    print(sol.exist(board, "SEE"))     # True
    print(sol.exist(board, "ABCB"))    # False


"""
=========================
Google-asked variations (2-3)
=========================

1. Word Search II (LeetCode 212, Hard)
   "Given a board and a LIST of words, find all words from the list that
   exist in the board." Running this problem's DFS once per word is too
   slow when the word list is large. The standard escalation: build a
   Trie out of all the words first, then do a single combined DFS over
   the board that walks the Trie alongside the board path -- as soon as a
   board path no longer matches any Trie prefix, prune immediately. This
   is one of Google's favorite "combine two data structures" questions
   (Trie + backtracking).

2. N-Queens (LeetCode 51, Hard)
   Different surface (place queens on a chessboard so none attack each
   other) but the exact same "mark, recurse, unmark" backtracking
   skeleton -- place a queen, recurse to the next row, and if no
   placement in that row works, backtrack and try a different column in
   the current row. Tests whether you understand backtracking as a
   general technique, not just a grid-word-matching trick.

3. Path with Maximum Gold (LeetCode 1219, Medium)
   "Collect the maximum gold along a path in a grid, where you can revisit
   cells 0 or more times across different paths but not within the same
   path, and 0-cells block movement." Same backtracking-on-a-grid shape as
   Word Search (mark/recurse/unmark on a single path), but optimizing for
   a maximum sum instead of a boolean match -- tests whether you can
   adapt the template's *return type and aggregation logic* while keeping
   the same traversal/backtrack skeleton.
"""
