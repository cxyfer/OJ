#
# @lc app=leetcode id=1768 lang=python3
#
# [1768] Merge Strings Alternately
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ln = min(len(word1), len(word2))
        ans = ""
        for i in range(ln):
            ans += word1[i] + word2[i]
        ans += word1[ln:] + word2[ln:]
        return ans
# @lc code=end

