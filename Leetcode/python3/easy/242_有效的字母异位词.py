#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#
from preImport import *
# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return sorted(s) == sorted(t)
        return Counter(s) == Counter(t)
# @lc code=end

