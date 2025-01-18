#
# @lc app=leetcode.cn id=1704 lang=python3
#
# [1704] 判断字符串的两半是否相似
#
from preImport import *
# @lc code=start
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s)
        def f(s: str) -> int:
            return sum([1 for ch in s if ch in "aeiouAEIOU"])
        return f(s[:n//2]) == f(s[n//2:])
# @lc code=end

