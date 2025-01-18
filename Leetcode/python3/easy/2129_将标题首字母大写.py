#
# @lc app=leetcode.cn id=2129 lang=python3
#
# [2129] 将标题首字母大写
#
from preImport import *
# @lc code=start
class Solution:
    def capitalizeTitle(self, title: str) -> str:
        words = title.split()
        for i, w in enumerate(words):
            if len(w) > 2:
                words[i] = w.title()
            else:
                words[i] = w.lower()
        return ' '.join(words)
# @lc code=end

