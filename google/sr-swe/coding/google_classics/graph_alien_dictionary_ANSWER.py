"""
Problem: Alien Dictionary
Link: https://leetcode.com/problems/alien-dictionary/
Topic: Graph (topological sort, string)
Difficulty: Hard

=========================
Explanation
=========================
Two-phase problem: (1) extract ordering constraints from adjacent word pairs,
then (2) topological sort those constraints.

Phase 1 — build the directed graph:
Compare each adjacent pair (words[i], words[i+1]) character by character.
The FIRST position where they differ tells you words[i][j] comes before
words[i+1][j] in the alien alphabet — add directed edge words[i][j] -> words[i+1][j].
Stop comparing after the first difference (later chars give no information).
Edge case: if words[i] is longer than words[i+1] and words[i+1] is a prefix
of words[i] (e.g., ["abc","ab"]), the sorted order is invalid — return "".

Phase 2 — Kahn's topological sort:
Initialize in-degree for ALL unique characters (not just those in edges).
BFS from zero-in-degree nodes. If output length < total unique characters,
a cycle exists — return "".

Common mistake: forgetting to initialize in-degree entries for all characters
(only initializing those that appear in edges), which means leaf nodes in the
character ordering never get enqueued.

=========================
Complexity
=========================
Time:  O(C) where C = total characters across all words (dominates graph build)
Space: O(1) — at most 26 nodes and 26^2 edges regardless of input size
"""

from typing import List
from collections import defaultdict, deque


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adj = defaultdict(set)
        in_degree = {c: 0 for word in words for c in word}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            min_len = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""  # longer word as prefix is invalid ordering
            for j in range(min_len):
                if w1[j] != w2[j]:
                    if w2[j] not in adj[w1[j]]:
                        adj[w1[j]].add(w2[j])
                        in_degree[w2[j]] += 1
                    break

        queue = deque(c for c, deg in in_degree.items() if deg == 0)
        result = []

        while queue:
            c = queue.popleft()
            result.append(c)
            for neighbor in adj[c]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        return "".join(result) if len(result) == len(in_degree) else ""


if __name__ == "__main__":
    sol = Solution()
    print(sol.alienOrder(["wrt", "wrf", "er", "ett", "rftt"]))  # "wertf"
    print(sol.alienOrder(["z", "x"]))                           # "zx"
    print(sol.alienOrder(["z", "x", "z"]))                      # "" (cycle)
    print(sol.alienOrder(["abc", "ab"]))                        # "" (invalid prefix)
