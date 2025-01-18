#
# @lc app=leetcode id=712 lang=python3
# @lcpr version=30204
#
# [712] Minimum ASCII Delete Sum for Two Strings
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
    1. LCS，定義 dp[i][j] 表示 s[:i] 和 t[:j] 的最大共同子序列 ASCII 總和
    2. 定義 dp[i][j] 表示 s[:i] 和 t[:j] 相同所需的最小 ASCII 刪除和
"""
# @lc code=start
class Solution1:
    def minimumDeleteSum(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        s_sum = sum(ord(c) for c in s)
        t_sum = sum(ord(c) for c in t)
        # dp[i][j] 表示 s[:i] 和 t[:j] 的最大共同子序列總和
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + ord(s[i - 1])
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return s_sum + t_sum - 2 * dp[m][n]
    
class Solution2:
    def minimumDeleteSum(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        # dp[i][j] 表示 s[:i] 和 t[:j] 相同所需的最小 ASCII 刪除和
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            dp[i][0] = dp[i - 1][0] + ord(s[i - 1])
        for j in range(1, n + 1):
            dp[0][j] = dp[0][j - 1] + ord(t[j - 1])
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == t[j - 1]: # 相同，不用刪除
                    dp[i][j] = dp[i - 1][j - 1]
                else: # 不同，刪除兩者之一，取最小
                    dp[i][j] = min(dp[i - 1][j] + ord(s[i - 1]), dp[i][j - 1] + ord(t[j - 1]))
        return dp[m][n]
    
# class Solution(Solution1):
class Solution(Solution2):
    pass
# @lc code=end



#
# @lcpr case=start
# "sea"\n"eat"\n
# @lcpr case=end

# @lcpr case=start
# "delete"\n"leet"\n
# @lcpr case=end

#

