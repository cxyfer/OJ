#
# @lc app=leetcode.cn id=1154 lang=python3
#
# [1154] 一年中的第几天
#
from preImport import *
# @lc code=start
class Solution:
    DAYS = [31,28,31,30,31,30,31,31,30,31,30,31]
    S = list(accumulate(DAYS, initial=0)) # Prefix sum
    def dayOfYear(self, date: str) -> int:
        y, m, d = map(int, date.split('-'))
        isLeap = (y%4==0 and y%100!=0) or y%400==0 # 閏年
        return self.S[m-1] + d + (m>2 and isLeap)
# @lc code=end

