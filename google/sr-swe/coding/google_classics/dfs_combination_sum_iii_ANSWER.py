"""
Problem: Combination Sum III
Link: https://leetcode.com/problems/combination-sum-iii/
Topic: DFS (backtracking, bounded candidates)
Difficulty: Medium

=========================
Explanation
=========================
Same backtracking skeleton as Combination Sum II, but the candidate pool is
fixed (digits 1-9, each used at most once) and we have TWO termination
conditions instead of one: remaining sum == 0 AND exactly k numbers chosen.

Backtrack(start, remaining_sum, remaining_count):
- Base case (success): remaining_sum == 0 AND remaining_count == 0.
- Base case (prune): remaining_count == 0 but sum not 0, OR remaining_sum < 0.
- For each digit d from start to 9: pick d, recurse with (d+1, remaining-d, count-1).

The candidate pool being small (1-9, known in advance) means no sort is needed.
Since candidates are naturally ascending, the early break (d > remaining_sum)
still applies.

This is a "have you internalized the backtracking template well enough to
add a second state variable (count) to the recursion?" problem.

=========================
Complexity
=========================
Time:  O(C(9,k)) — at most C(9,k) combinations to explore; for k=4, that's 126
Space: O(k) recursion depth (at most k levels deep)
"""

from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        current = []

        def backtrack(start: int, remaining: int, count: int):
            if count == 0 and remaining == 0:
                result.append(current[:])
                return
            if count == 0 or remaining <= 0:
                return
            for d in range(start, 10):
                if d > remaining:
                    break
                current.append(d)
                backtrack(d + 1, remaining - d, count - 1)
                current.pop()

        backtrack(1, n, k)
        return result


if __name__ == "__main__":
    sol = Solution()
    print(sol.combinationSum3(3, 7))   # [[1,2,4]]
    print(sol.combinationSum3(3, 9))   # [[1,2,6],[1,3,5],[2,3,4]]
    print(sol.combinationSum3(4, 1))   # []
