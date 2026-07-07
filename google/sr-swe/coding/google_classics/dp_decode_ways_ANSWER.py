"""
Problem: Decode Ways
Link: https://leetcode.com/problems/decode-ways/
Topic: DP
Difficulty: Medium

=========================
Explanation
=========================
At each position we decide: decode one digit (s[i]), or decode two digits
(s[i-1:i+1]). Both choices reduce to smaller subproblems, and the number of
ways to decode s[0:i] is needed repeatedly — DP signal.

State: dp[i] = number of ways to decode s[0:i].
Recurrence:
  - One-digit decode: if s[i-1] != '0', dp[i] += dp[i-1]
    (s[i-1] maps to a valid letter A-Z only if it's 1-9)
  - Two-digit decode: if s[i-2:i] is between "10" and "26", dp[i] += dp[i-2]
    (leading zero "0x" is invalid; two-digit max is "26")
Base cases: dp[0] = 1 (empty string: one way to decode nothing), dp[1] = 1 if
s[0] != '0' else 0.

The '0' cases are the main gotcha: "0" alone is invalid, "00" is invalid,
"30"-"99" as two-digit is invalid (> 26).
=========================
Complexity
=========================
Time:  O(n) — one pass through the string.
Space: O(1) — only two previous values needed (like Fibonacci).
"""


class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        prev2, prev1 = 1, 1
        for i in range(1, len(s)):
            current = 0
            if s[i] != '0':
                current += prev1
            two_digit = int(s[i - 1:i + 1])
            if 10 <= two_digit <= 26:
                current += prev2
            prev2, prev1 = prev1, current
        return prev1


if __name__ == "__main__":
    sol = Solution()
    print(sol.numDecodings("12"))     # 2
    print(sol.numDecodings("226"))    # 3
    print(sol.numDecodings("06"))     # 0
    print(sol.numDecodings("10"))     # 1
    print(sol.numDecodings("2101"))   # 1


"""
=========================
Google-asked variations (2-3)
=========================

1. Decode Ways II (LeetCode 639, Hard)
   "The encoded message may contain '*', which can represent any digit 1-9."
   The same DP structure but the one-digit and two-digit counts multiply by up
   to 9 depending on what '*' can match. Tests whether you can handle
   multiplicative branching in the same recurrence.

2. Number of Ways to Decode a Message with Wildcards
   A generalization where certain positions can be any letter. Same DP, but the
   branching factor per position changes. The core insight — one-digit and
   two-digit validity checks — remains identical.

3. Climbing Stairs (LeetCode 70, Easy)
   "Count ways to reach step n taking 1 or 2 steps at a time." Structurally
   identical to Decode Ways but without the validity constraints. Decode Ways
   is Climbing Stairs plus the digit-validity guards. Always a good warm-up
   to recognize the Fibonacci-shaped DP before adding the constraints.
"""
