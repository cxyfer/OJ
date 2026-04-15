#
# @lc app=leetcode id=3896 lang=python3
#
# [3896] Minimum Operations to Transform Array into Alternating Prime
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
MAX_N = int(1e5 + 5)  # 第一個 > 1e5 的質數是 100003
is_prime = [True] * (MAX_N + 1)
is_prime[0] = is_prime[1] = False
for i in range(2, math.isqrt(MAX_N) + 1):
    if is_prime[i]:
        for j in range(i * i, MAX_N + 1, i):
            is_prime[j] = False
primes = [x for x in range(2, MAX_N) if is_prime[x]]

class Solution:
    def minOperations(self, nums: list[int]) -> int:
        ans = 0
        for i, x in enumerate(nums):
            if i & 1:
                while is_prime[x]:
                    ans += 1
                    x += 1
            else:
                if not is_prime[x]:
                    idx = bisect_left(primes, x)
                    ans += primes[idx] - x
        return ans
# @lc code=end

