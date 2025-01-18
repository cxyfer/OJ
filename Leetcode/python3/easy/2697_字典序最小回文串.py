#
# @lc app=leetcode.cn id=2697 lang=python3
#
# [2697] 字典序最小回文串
#

# @lc code=start
class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        n = len(s)
        res = list(s)
        for i in range((n+1)//2):
            if s[i] != s[n-1-i]:
                res[i] = res[n-1-i] = min(s[i], s[n-1-i])
        return ''.join(res)
# @lc code=end

