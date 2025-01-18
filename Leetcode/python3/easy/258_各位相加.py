#
# @lc app=leetcode.cn id=258 lang=python3
#
# [258] 各位相加
#

# @lc code=start
class Solution:
    def addDigits(self, num: int) -> int:
        while(num >= 10):
            tmp = 0
            while(num > 0):
                tmp += num % 10
                num //= 10
            num = tmp
        return num
# @lc code=end

