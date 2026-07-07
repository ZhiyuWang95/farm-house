"""
Problem: Combination Sum II
Link: https://leetcode.com/problems/combination-sum-ii/
Topic: DFS (backtracking with deduplication)
Difficulty: Medium

=========================
Explanation
=========================
Two changes from Combination Sum I (dfs_combination_sum.py):
1. No reuse: recurse with `i + 1` instead of `i`.
2. Dedup: skip candidates[i] if it equals candidates[i-1] AND i > start.

Why the dedup guard works: after sorting, duplicate values are adjacent.
At a given recursion level (fixed `start`), if we've already explored the
subtree rooted at candidates[i-1] = V and backtracked, trying candidates[i] = V
again would generate identical combinations (same value, same remaining elements
ahead). The `i > start` check (not `i > 0`) is important: it only skips
SAME-LEVEL duplicates. If i == start, this is the FIRST time we're picking
this value at this level, so we must allow it even if candidates[i-1] exists.

Contrast with Permutations II dedup: that uses `not used[i-1]` because order
matters for permutations. For combinations (order doesn't matter), the
simpler `i > start` guard suffices.

=========================
Complexity
=========================
Time:  Exponential, roughly O(2^n) — bounded by subset count
Space: O(target) recursion depth
"""

from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        current = []

        def backtrack(start: int, remaining: int):
            if remaining == 0:
                result.append(current[:])
                return
            for i in range(start, len(candidates)):
                if candidates[i] > remaining:
                    break  # sorted — everything after is too big
                if i > start and candidates[i] == candidates[i - 1]:
                    continue  # skip same-level duplicate
                current.append(candidates[i])
                backtrack(i + 1, remaining - candidates[i])  # i+1: no reuse
                current.pop()

        backtrack(0, target)
        return result


if __name__ == "__main__":
    sol = Solution()
    print(sol.combinationSum2([10,1,2,7,6,1,5], 8))   # [[1,1,6],[1,2,5],[1,7],[2,6]]
    print(sol.combinationSum2([2,5,2,1,2], 5))          # [[1,2,2],[5]]
