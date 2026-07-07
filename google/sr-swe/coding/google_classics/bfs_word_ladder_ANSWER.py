"""
Problem: Word Ladder
Link: https://leetcode.com/problems/word-ladder/
Topic: BFS (shortest path, implicit graph)
Difficulty: Hard

=========================
Explanation
=========================
The hard part isn't the BFS itself -- it's recognizing that this problem
IS a shortest-path-in-a-graph problem, where the graph is never built
explicitly:
  - Nodes = words.
  - An edge connects two words if they differ by exactly one letter.
  - "Shortest transformation sequence length" = shortest path (in number
    of nodes, not edges) from beginWord to endWord.

Since "shortest path in an unweighted graph" is BFS's signature use case,
the only real work is figuring out how to generate a word's neighbors
efficiently, since you don't have an adjacency list handed to you.

Naive neighbor generation: for a word of length L, try swapping each of
its L positions with each of the 26 letters (L * 26 candidates per word),
and check if the resulting word is in the dictionary (use a set for O(1)
lookup, not a list scan). This is the standard, expected approach --
don't overthink it into something fancier unless asked to optimize
further.

BFS mechanics: start the queue with (beginWord, level=1). Pop a word,
generate its L*26 neighbor candidates, and for each one that's in the
word set and not yet visited: if it equals endWord, return level+1;
otherwise mark it visited (remove from the set so it's never re-enqueued)
and push (neighbor, level+1).

Why remove from the set instead of using a separate "visited" set: this
problem only has one valid path length we care about (the shortest), and
once a word has been reached at the current BFS depth, any later edge to
it can't produce a *shorter* path -- so removing it from the candidate
pool is both a correctness optimization (no revisits) and a memory
shortcut (no second data structure needed).

=========================
Complexity
=========================
Time:  O(N * L^2 * 26) -- N words, each generating L*26 candidates, each
       candidate costing O(L) to construct/hash. (Some solutions further
       optimize neighbor lookup via pattern buckets, e.g. "h*t" -> ["hot",
       "hat", ...], but the direct approach is what's expected first.)
Space: O(N * L) -- the word set plus the BFS queue.
"""

from collections import deque
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        if endWord not in word_set:
            return 0

        queue = deque([(beginWord, 1)])
        word_set.discard(beginWord)

        while queue:
            word, level = queue.popleft()
            if word == endWord:
                return level

            for i in range(len(word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    if c == word[i]:
                        continue
                    candidate = word[:i] + c + word[i + 1:]
                    if candidate in word_set:
                        word_set.discard(candidate)
                        queue.append((candidate, level + 1))

        return 0


# =============================================================================
# Optimized: Bidirectional BFS
# =============================================================================
# Instead of one frontier expanding from beginWord, run two frontiers
# simultaneously -- one from beginWord, one from endWord -- and always
# expand the SMALLER one. Each side explores O(b^(d/2)) nodes before they
# meet, vs O(b^d) for single-direction. For Word Ladder with large
# dictionaries and long transformation chains, this is dramatically faster.
#
# Key difference in the loop: `front` and `back` are now SETS (not a queue
# with levels), since we only need to know "is this word in the other
# frontier" rather than the exact ordering of how we got there. Each
# iteration generates the next layer of `front`, and if any generated
# candidate appears in `back` the two frontiers have met.

class SolutionBidirectional:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        if endWord not in word_set:
            return 0

        front, back = {beginWord}, {endWord}
        length = 1

        while front and back:
            if len(front) > len(back):
                front, back = back, front  # always expand the smaller frontier

            next_front = set()
            for word in front:
                for i in range(len(word)):
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        candidate = word[:i] + c + word[i + 1:]
                        if candidate in back:
                            return length + 1
                        if candidate in word_set:
                            next_front.add(candidate)
                            word_set.discard(candidate)
            front = next_front
            length += 1

        return 0


if __name__ == "__main__":
    sol = Solution()
    print(sol.ladderLength(
        "hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]
    ))  # 5
    print(sol.ladderLength(
        "hit", "cog", ["hot", "dot", "dog", "lot", "log"]
    ))  # 0

    sol2 = SolutionBidirectional()
    print(sol2.ladderLength(
        "hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]
    ))  # 5
    print(sol2.ladderLength(
        "hit", "cog", ["hot", "dot", "dog", "lot", "log"]
    ))  # 0


"""
=========================
Google-asked variations (2-3)
=========================

1. Word Ladder II (LeetCode 126, Hard)
   "Return ALL shortest transformation sequences, not just the length."
   Same BFS to discover shortest distance, but you additionally need to
   track parent pointers (or build the level graph during BFS) and then
   DFS/backtrack from endWord back to beginWord to reconstruct every path
   of minimal length. Tests whether you can extend "shortest distance" BFS
   into "all shortest paths" -- a very common Google escalation pattern.

2. Open the Lock (LeetCode 752, Medium)
   "4-wheel combination lock, each wheel 0-9, find min turns to reach a
   target combination avoiding 'deadends'." Structurally identical to Word
   Ladder: nodes are lock states (strings), edges connect states one digit
   apart, BFS finds shortest path. A great "have you actually internalized
   the pattern, or did you just memorize Word Ladder" check.

3. Minimum Genetic Mutation (LeetCode 433, Medium)
   "Given a starting and target gene string (over alphabet ACGT) and a
   bank of valid intermediate genes, find the minimum number of single-
   character mutations to reach the target, using only genes in the
   bank." Nearly a verbatim restatement of Word Ladder with a 4-letter
   alphabet instead of 26 and a smaller bank instead of a word list --
   Google likes to dress up the same BFS-over-implicit-graph idea in a
   different domain to see if surface-level differences throw you off.
"""
