#
# @lc app=leetcode.cn id=2864 lang=python3
#
# [2864] 最大二进制奇数
#
from preImport import *
# @lc code=start
class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        n = len(s)
        cnt_1 = s.count('1')
        return '1' * (cnt_1 - 1) + '0' * (n - cnt_1) + '1'
# @lc code=end

