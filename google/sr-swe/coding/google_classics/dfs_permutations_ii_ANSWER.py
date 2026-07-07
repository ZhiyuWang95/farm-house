"""
Problem: Permutations II
Link: https://leetcode.com/problems/permutations-ii/
Topic: DFS (backtracking with deduplication)
Difficulty: Medium

=========================
Explanation
=========================
Extension of Permutations I (dfs_permutations.py). The base algorithm uses a
`used` boolean array and tries each unused index in sequence. Adding duplicates
requires one dedup guard: if nums[i] == nums[i-1] and used[i-1] is False,
skip nums[i].

Why this works: sorting ensures equal values are adjacent. At any recursion
level (fixed prefix), if we've already explored a branch starting with value V
(via nums[i-1]) and then backtracked, trying nums[i] (which also equals V)
would generate the exact same permutations again. The `not used[i-1]` condition
catches exactly this case: after backtracking from nums[i-1], used[i-1] is
False, so we skip nums[i]. If used[i-1] is True, nums[i-1] is already in the
current prefix at a different depth — different situation, don't skip.

The dedup logic is subtle: `if i > 0 and nums[i] == nums[i-1] and not used[i-1]: continue`
is the canonical guard for permutations with duplicates.

=========================
Complexity
=========================
Time:  O(n * n!) — n! permutations, each of length n to copy
Space: O(n) recursion depth + O(n) for `used` array
"""

from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        current = []
        used = [False] * len(nums)

        def backtrack():
            if len(current) == len(nums):
                result.append(current[:])
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue  # skip duplicate at this recursion level
                used[i] = True
                current.append(nums[i])
                backtrack()
                current.pop()
                used[i] = False

        backtrack()
        return result


if __name__ == "__main__":
    sol = Solution()
    print(sol.permuteUnique([1, 1, 2]))  # [[1,1,2],[1,2,1],[2,1,1]]
    print(len(sol.permuteUnique([1, 2, 3])))  # 6
