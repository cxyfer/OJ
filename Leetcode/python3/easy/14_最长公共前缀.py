#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#
from preImport import *
# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lcp = 0
        m, n = len(strs), len(strs[0])
        for i in range(n):
            ch = strs[0][i]
            for j in range(1, m):
                if i >= len(strs[j]) or strs[j][i] != ch:
                    return strs[0][:lcp]
            lcp += 1
        return strs[0][:lcp]
# @lc code=end

