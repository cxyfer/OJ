#
# @lc app=leetcode id=1392 lang=python3
#
# [1392] Longest Happy Prefix
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def longestPrefix(self, s: str) -> str:
        n = len(s)
        pi = [0] * n
        ln = 0
        for i in range(1, n):
            while ln and s[i] != s[ln]:
                ln = pi[ln - 1]
            if s[i] == s[ln]:
                ln += 1
            pi[i] = ln
        return s[:pi[-1]]
# @lc code=end

sol = Solution()
print(sol.longestPrefix("bba")) # ""