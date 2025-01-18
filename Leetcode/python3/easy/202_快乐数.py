#
# @lc app=leetcode.cn id=202 lang=python3
#
# [202] 快乐数
#
from preImport import *
# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while (n != 1 and not n in seen):
            seen.add(n)
            n = sum([int(i) ** 2 for i in str(n)])
        return n == 1
# @lc code=end

