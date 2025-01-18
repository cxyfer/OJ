#
# @lc app=leetcode.cn id=1544 lang=python3
#
# [1544] 整理字符串
#
from preImport import *
# @lc code=start
class Solution:
    def makeGood(self, s: str) -> str:
        st = []
        for ch in s:
            if st and abs(ord(ch) - ord(st[-1])) == 32:
                st.pop()
            else:
                st.append(ch)
        return ''.join(st)
# @lc code=end

