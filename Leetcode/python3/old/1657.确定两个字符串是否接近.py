#
# @lc app=leetcode.cn id=1657 lang=python3
#
# [1657] 确定两个字符串是否接近
#
from en.Python3.mod.preImport import *
# @lc code=start
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        cnt1 = Counter(word1)
        cnt2 = Counter(word2)
        return sorted(cnt1.keys()) == sorted(cnt2.keys()) and sorted(cnt1.values()) == sorted(cnt2.values())
# @lc code=end

