"""
Problem: Generate Parentheses
Link: https://leetcode.com/problems/generate-parentheses/
Topic: Recursion (backtracking)
Difficulty: Medium

=========================
Explanation
=========================
Build the string one character at a time via recursion, tracking two
counters: `open_count` (how many '(' placed so far) and `close_count` (how
many ')' placed so far). At each recursive step you have at most two
choices:

1. Place '(' if open_count < n (haven't used up all opens yet).
2. Place ')' if close_count < open_count (only close a paren that's
   actually open -- this is what guarantees well-formedness; you can never
   have more closes than opens at any prefix).

Base case: when the string length reaches 2*n, it's a complete, valid
combination -- add it to the result.

This is the canonical "backtracking with a validity constraint baked into
the recursion" pattern: instead of generating all 2^(2n) strings of parens
and filtering for validity afterward, the `close_count < open_count` guard
prunes invalid branches immediately, so you only ever recurse down paths
that can still become valid.

=========================
Complexity
=========================
Time:  O(4^n / sqrt(n)) -- here's the intuition:
       - Naive upper bound: 2 choices at each of 2n positions = 4^n strings.
       - Backtracking prunes invalid branches early; only valid strings reach
         the base case. It turns out the count of valid strings grows like
         4^n / n^1.5 (much smaller than 4^n -- for n=3: naive=64, valid=5).
       - Each valid string takes O(n) to build. Multiplying:
         O(n) * 4^n/n^1.5 = O(4^n / sqrt(n)).
       - Interview tip: just say "backtracking prunes most of the 4^n paths;
         the number of valid strings grows like 4^n/sqrt(n)."
Space: O(n) for working memory -- the recursion goes at most 2n levels deep
       (one character added per call), and at any moment only one root-to-leaf
       path is alive on the call stack (same DFS reasoning as combination sum).
       The `current` list also holds at most 2n characters. So working memory
       is O(n).
       Output storage is separate: storing all valid strings costs
       O(4^n/sqrt(n) * n), but by convention space complexity excludes the
       output itself.
"""

from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(current: List[str], open_count: int, close_count: int):
            if len(current) == 2 * n:
                result.append("".join(current))
                return
            if open_count < n:
                current.append("(")
                backtrack(current, open_count + 1, close_count)
                current.pop()
            if close_count < open_count:
                current.append(")")
                backtrack(current, open_count, close_count + 1)
                current.pop()

        backtrack([], 0, 0)
        return result


if __name__ == "__main__":
    sol = Solution()
    print(sol.generateParenthesis(3))
    # ['((()))', '(()())', '(())()', '()(())', '()()()']
    print(sol.generateParenthesis(1))
    # ['()']


"""
=========================
Google-asked variations (2-3)
=========================

1. Valid Parentheses (LeetCode 20, Easy)
   "Given a string of '()[]{}', determine if it's valid." This is the
   *verification* counterpart to this problem's *generation* -- solved with
   a stack instead of recursion. A common Google opener: ask Valid
   Parentheses first as a warm-up, then escalate to Generate Parentheses to
   see if you can flip from checking validity to constructing it.

2. Remove Invalid Parentheses (LeetCode 301, Hard)
   "Given a string with extra parens, remove the minimum number to make it
   valid, return all possible results." Same backtracking instinct, but now
   you're pruning *removals* via BFS/backtracking over an existing string
   rather than building from scratch -- tests whether you can adapt the
   open/close counting validity check to a different shape of problem.

3. Different Ways to Add Parentheses / Score of Parentheses (LeetCode 856)
   "Given a balanced parentheses string, compute a 'score'" (empty pair =
   1, AB = A+B, (A) = 2*A). Tests whether you understand the *structure*
   of nested valid parentheses (not just generating it) -- a common
   follow-up question to check if you actually understand the recursive
   structure or just memorized the open/close-counter trick.
"""
