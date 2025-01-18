#
# @lc app=leetcode.cn id=2828 lang=python3
#
# [2828] 判别首字母缩略词
#
from preImport import *
# @lc code=start
class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        # return len(words) == len(s) and all(word[0] == s[idx] for idx, word in enumerate(words))
        if len(words) != len(s):
            return False
        for idx, word in enumerate(words):
            if word[0] != s[idx]:
                return False
        return True

# @lc code=end

