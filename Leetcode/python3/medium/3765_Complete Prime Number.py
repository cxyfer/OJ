#
# @lc app=leetcode id=3765 lang=python3
#
# [3765] Complete Prime Number
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
def is_prime(x):
    if x == 1:
        return False
    for p in range(2, math.isqrt(x) + 1):
        if x % p == 0:
            return False
    return True

class Solution:
    def completePrime(self, num: int) -> bool:
        digits = []
        while num:
            digits.append(num % 10)
            num //= 10
        digits.reverse()
        # 檢查前綴
        x = 0
        for d in digits:
            x = x * 10 + d
            if not is_prime(x):
                return False
        # 檢查後綴
        x = 0
        p = 1
        digits.reverse()
        for d in digits:
            x += d * p
            p *= 10
            if not is_prime(x):
                return False
        return True
# @lc code=end

