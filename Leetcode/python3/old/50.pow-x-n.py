#
# @lc app=leetcode.cn id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == float(0):
            return float(0)
        if n < 0:
            x, n = 1 / x, -n
        ans = 1
        while n:
            if n % 2 == 1:
                ans *= x
            x *= x
            n //= 2
        return ans
# @lc code=end



