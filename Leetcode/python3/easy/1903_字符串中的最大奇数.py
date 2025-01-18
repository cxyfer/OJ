#
# @lc app=leetcode.cn id=1903 lang=python3
#
# [1903] 字符串中的最大奇数
#
from preImport import *
# @lc code=start
class Solution:
    """
        找到最後一個奇數，返回前面的數字
    """
    def largestOddNumber(self, num: str) -> str:
        n = len(num)
        for i in range(n-1, -1, -1):
            if int(num[i]) % 2 == 1:
                return num[:i+1]
        return ""
# @lc code=end

