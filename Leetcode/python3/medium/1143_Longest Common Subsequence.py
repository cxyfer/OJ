#
# @lc app=leetcode id=1143 lang=python3
# @lcpr version=30204
#
# [1143] Longest Common Subsequence
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def longestCommonSubsequence(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == t[j - 1]: # 可由左上方轉移
                    dp[i][j] = dp[i - 1][j - 1] + 1 
                else: # 可由上方或左方轉移
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[m][n]
# @lc code=end

sol = Solution()
print(sol.longestCommonSubsequence("CGTTCGGAATG", "TCGAGTGC"))

#
# @lcpr case=start
# "abcde"\n"ace"\n
# @lcpr case=end

# @lcpr case=start
# "abc"\n"abc"\n
# @lcpr case=end

# @lcpr case=start
# "abc"\n"def"\n
# @lcpr case=end

#

