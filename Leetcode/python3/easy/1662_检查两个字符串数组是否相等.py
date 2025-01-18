#
# @lc app=leetcode.cn id=1662 lang=python3
#
# [1662] 检查两个字符串数组是否相等
#
from preImport import *
# @lc code=start
class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        # return "".join(word1) == "".join(word2)
        i = j = ii = jj = 0
        while i < len(word1) and j < len(word2):
            if word1[i][ii] != word2[j][jj]: # 檢查字元是否相等
                return False
            ii += 1
            jj += 1
            if ii == len(word1[i]): # 換word1的下一個字串
                ii = 0
                i += 1
            if jj == len(word2[j]): # 換word2的下一個字串
                jj = 0
                j += 1
        return i == len(word1) and j == len(word2) # 是否已經檢查完所有字串
# @lc code=end

