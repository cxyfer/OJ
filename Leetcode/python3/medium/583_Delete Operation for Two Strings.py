#
# @lc app=leetcode id=583 lang=python3
# @lcpr version=30204
#
# [583] Delete Operation for Two Strings
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
    1. LCS
    2. 定義 dp[i][j] 為使得 s[:i] 和 t[:j] 相同所需的最少刪除次數
"""
# @lc code=start
class Solution1:
    def minDistance(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return m + n - 2 * dp[m][n]
    
class Solution2:
    def minDistance(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            dp[i][0] = i
        for j in range(1, n + 1):
            dp[0][j] = j
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == t[j - 1]: # 相同，不用刪除
                    dp[i][j] = dp[i - 1][j - 1]
                else: # 不同，刪除兩者之一，取最小
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + 1
        return dp[m][n]
    
# class Solution(Solution1):
class Solution(Solution2):
    pass

# @lc code=end

sol = Solution()
print(sol.minDistance("sea", "eat"))


#
# @lcpr case=start
# "sea"\n"eat"\n
# @lcpr case=end

# @lcpr case=start
# "leetcode"\n"etco"\n
# @lcpr case=end

#

