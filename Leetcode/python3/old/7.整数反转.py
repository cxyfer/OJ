#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        if -10< x < 10:
            return x
        y = abs(x)
        ans = 0
        positive = (x > 0)
        # 则其数值范围为 [−2^31,  2^31 − 1]
        boundry = (1<<31) -1 if positive else 1<<31
        while y != 0:
            ans = ans*10 +y%10
            if ans > boundry :
                return 0
            y //= 10
        return ans if positive else -ans

# @lc code=end

