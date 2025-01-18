#
# @lc app=leetcode.cn id=1768 lang=python3
#
# [1768] 交替合并字符串
#

# @lc code=start
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = j = 0
        res = ''
        while (i < len(word1) or j < len(word2)):
            if i < len(word1):
                res += word1[i]
            if j < len(word2):
                res += word2[j]
            i += 1
            j += 1
        return res
# @lc code=end

