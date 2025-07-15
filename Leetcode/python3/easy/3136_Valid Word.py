#
# @lc app=leetcode id=3136 lang=python3
#
# [3136] Valid Word
#
from preImport import *
# @lc code=start
class Solution:
    def isValid(self, word: str) -> bool:
        return len(w := word.lower()) >= 3 and w.isalnum() and any(c in "aeiou" for c in w) and any(c.isalpha() and c not in "aeiou" for c in w)
# @lc code=end