#
# @lc app=leetcode.cn id=1768 lang=python3
#
# [1768] 交替合并字符串
#

# @lc code=start
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m, n = len(word1), len(word2)
        ans = ""
        for i in range(max(m, n)):
            if i < m:
                ans += word1[i]
            if i < n:
                ans += word2[i]
        return ans
# @lc code=end

