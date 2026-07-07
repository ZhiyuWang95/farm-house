"""
Problem: Combination Sum
Link: https://leetcode.com/problems/combination-sum/
Topic: DFS (backtracking with pruning)
Difficulty: Medium

=========================
Explanation
=========================
Contrast with Permutations (order matters, each element used once) and
Word Search (path-constrained on a grid): this problem's defining
features are (1) the SAME number can be reused unlimited times, and
(2) ORDER doesn't matter -- [2,2,3] and [2,3,2] are the same combination,
not two different answers.

Both of those features are handled by ONE trick: sort `candidates` first,
and in the recursion, only ever consider candidates at the current index
OR LATER (never go backward to an earlier index). This single rule:
  - Prevents counting [2,3] and [3,2] as separate results (order-
    independence), since you can never "go back" to pick 2 after having
    picked 3.
  - Still allows reuse of the same number, by recursing with the SAME
    start index (not index + 1) when you choose to include candidates[i]
    again.

Backtrack(start, remaining_target, current):
  - Base case: remaining_target == 0 -> append a copy of `current`.
  - Base case: remaining_target < 0 -> dead end, return (this is exactly
    why candidates are sorted: as soon as candidates[i] > remaining_target,
    EVERY later candidate is also too big, so you can `break` out of the
    loop entirely instead of just `continue`-ing -- a meaningful pruning
    optimization once sorted).
  - For i from start to len(candidates): append candidates[i], recurse
    with (i, remaining_target - candidates[i], current) -- note `i`, not
    `i + 1`, since reuse is allowed -- then pop (backtrack) before trying
    the next i.

=========================
Complexity
=========================
Time:  Exponential in the worst case (bounded by target / min(candidates)
       recursion depth, branching factor = number of candidates at each
       level) -- commonly stated loosely as O(n^(target/min_candidate)).
       Sorting + the `break`-on-overshoot pruning keeps this practical for
       the given constraints.
Space: O(target / min(candidates)) recursion depth, plus the output size.
"""

from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        current = []

        def backtrack(start: int, remaining: int):
            if remaining == 0:
                result.append(current[:])
                return
            for i in range(start, len(candidates)):
                if candidates[i] > remaining:
                    break  # sorted -> everything after is too big too
                current.append(candidates[i])
                backtrack(i, remaining - candidates[i])  # reuse: pass i, not i+1
                current.pop()

        backtrack(0, target)
        return result


class Solution2:
    """Iterative DFS: explicit stack replaces the call stack."""
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        # stack: (start_index, path, remaining)
        stack = [(0, [], target)]

        while stack:
            start, path, remaining = stack.pop()

            if remaining == 0:
                result.append(path)
                continue

            for i in range(start, len(candidates)):
                if candidates[i] > remaining:
                    break
                stack.append((i, path + [candidates[i]], remaining - candidates[i]))

        return result


if __name__ == "__main__":
    sol = Solution()
    print(sol.combinationSum([2, 3, 6, 7], 7))   # [[2,2,3],[7]]
    print(sol.combinationSum([2, 3, 5], 8))      # [[2,2,2,2],[2,3,3],[3,5]]
    print(sol.combinationSum([2], 1))            # []

    sol2 = Solution2()
    print(sol2.combinationSum([2, 3, 6, 7], 7))  # [[2,2,3],[7]]
    print(sol2.combinationSum([2, 3, 5], 8))     # [[2,2,2,2],[2,3,3],[3,5]]
    print(sol2.combinationSum([2], 1))           # []


"""
=========================
Google-asked variations (2-3)
=========================

1. Combination Sum II (LeetCode 40, Medium)
   "Candidates may contain duplicates, and each number can be used at
   most ONCE." Two changes from this problem: recurse with `i + 1` (no
   reuse) instead of `i`, AND add a dedup guard at each loop level
   (`if i > start and candidates[i] == candidates[i-1]: continue`) to
   avoid generating the same combination twice when duplicate values
   exist in the sorted input. A very commonly cited "almost the same
   problem, but the two small changes matter a lot" Google pairing.

2. Combination Sum III (LeetCode 216, Medium)
   "Find all combinations of exactly k numbers from 1-9 that sum to n,
   each number used at most once." Adds a second constraint (exact count
   k, not just sum) on top of the no-reuse version -- tests whether you
   can track an additional piece of state (remaining picks left) through
   the same backtracking skeleton.

3. Combination Sum IV (LeetCode 377, Medium) -- secretly Coin Change II
   "Count the NUMBER OF combinations (order matters here -- it's actually
   permutations) that sum to target, with unlimited reuse." This is
   deliberately NOT solved by backtracking -- the combination count
   explodes exponentially while overlapping subproblems repeat constantly,
   so it should be solved with the same unbounded-knapsack DP as Coin
   Change (see dp_coin_change.py in this folder). A sharp test of
   recognizing WHEN to abandon backtracking for DP: "count the ways"
   problems with overlapping subproblems usually want DP, not
   enumeration.
"""
