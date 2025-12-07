#
# @lc app=leetcode id=3770 lang=python3
#
# [3770] Largest Prime from Consecutive Prime Sum
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
MAX_N = int(5e5 + 5)
is_prime = [True] * (MAX_N + 1)
is_prime[0] = is_prime[1] = False
for i in range(2, math.isqrt(MAX_N) + 1):
    if is_prime[i]:
        for j in range(i * i, MAX_N + 1, i):
            is_prime[j] = False
primes = [x for x in range(2, MAX_N) if is_prime[x]]

st = set(primes)
arr = [0]  # sentinel
arr.extend(x for x in accumulate(primes) if x in st)

class Solution:
    def largestPrime(self, n: int) -> int:
        return arr[bisect_right(arr, n) - 1]
# @lc code=end

