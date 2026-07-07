"""
Problem: Pow(x, n)
Link: https://leetcode.com/problems/powx-n/
Topic: Recursion (divide & conquer)
Difficulty: Medium

=========================
Explanation
=========================
Naive approach: multiply x by itself n times -> O(n) time. Too slow for
n up to 2^31.

Key insight (binary/fast exponentiation): x^n can be halved recursively.
- If n is even:  x^n = (x^(n/2))^2
- If n is odd:   x^n = x * (x^(n/2))^2     (integer division drops the remainder)

Each recursive call halves n, so the recursion depth is O(log n) instead of
O(n). This "halve the exponent" trick is the single most reusable idea in
this file -- it generalizes far beyond floats (see Variations below).

Negative n: x^(-n) = 1 / x^n. Handle by flipping the sign of n and inverting
x once up front, then run the same positive-exponent logic.

Edge case to watch: n = -2^31 cannot simply become positive 2^31 in a
signed 32-bit int (overflow) -- in Python this isn't an issue since ints
are arbitrary precision, but call this out verbally in an interview, since
it's a classic gotcha in C++/Java.

=========================
Complexity
=========================
Time:  O(log n) -- the exponent halves each call.
Space: O(log n) -- recursion call stack depth. (An iterative version, see
       below, gets this down to O(1) space -- a natural follow-up to offer
       proactively.)
"""


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n
        return self._fast_pow(x, n)

    def _fast_pow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        half = self._fast_pow(x, n // 2)
        if n % 2 == 0:
            return half * half
        return half * half * x

    # Iterative version, O(1) space -- good to mention as a follow-up:
    # binary-expand n into bits, multiply in the bits of x^(2^k) that are
    # "on".
    def myPowIterative(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n
        result = 1.0
        base = x
        while n > 0:
            if n % 2 == 1:
                result *= base
            base *= base
            n //= 2
        return result


if __name__ == "__main__":
    sol = Solution()
    print(sol.myPow(2.0, 10))   # 1024.0
    print(sol.myPow(2.1, 3))    # 9.261
    print(sol.myPow(2.0, -2))   # 0.25
    print(sol.myPowIterative(2.0, 10))  # 1024.0


"""
=========================
Google-asked variations (2-3)
=========================

1. Sqrt(x) (LeetCode 69, Easy)
   "Implement integer square root without using x**0.5."
   Different technique on the surface (binary search over the answer space
   instead of halving the exponent), but tests the same underlying instinct
   Google probes here: can you compute a math function in sub-linear time
   instead of brute force? Often asked as a quick warm-up before Pow(x, n).

2. Super Pow (LeetCode 372, Medium)
   "Calculate a^b mod 1337, where b is given as a huge number represented
   as an array of digits (b can be far larger than a 32/64-bit int)."
   Direct extension of fast exponentiation: you can't materialize b as a
   normal int, so you process its digits left-to-right, using the identity
   pow(a, 10*x + d) = pow(pow(a, x), 10) * pow(a, d) (mod m). Tests whether
   you can adapt the halving trick when the "n" itself doesn't fit in a
   primitive type -- a common Google twist (assume the obvious type doesn't
   work, now what?).

3. Fast doubling Fibonacci / matrix exponentiation (no single canonical
   LeetCode # but a very common Google follow-up: "compute Fib(n) in
   O(log n)")
   Generalizes the *same* halving idea from scalars to 2x2 matrices:
   [[F(n+1), F(n)], [F(n), F(n-1)]] = [[1,1],[1,0]]^n, and matrix power
   uses the exact recursive halving structure as myPow. Great follow-up to
   pose yourself: "the trick I used for floats also works for matrices --
   here's why." Demonstrates pattern transfer, which is exactly what Google
   interviewers are listening for after you solve the base problem cleanly.
"""
