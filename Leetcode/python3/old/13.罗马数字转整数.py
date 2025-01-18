#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#
from en.Python3.mod.preImport import *
# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        MAP = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        ans = 0
        for idx in range(1, len(s)):
            pre = MAP[s[idx-1]]
            cur = MAP[s[idx]]
            if pre < cur:
                ans -= pre
            else:
                ans += pre
        return ans + MAP[s[-1]]
# @lc code=end

