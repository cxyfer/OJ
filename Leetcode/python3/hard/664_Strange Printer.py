#
# @lc app=leetcode id=664 lang=python3
# @lcpr version=30204
#
# [664] Strange Printer
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution1:
    def strangePrinter(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1

        for ln in range(2, n + 1):
            for i in range(n - ln + 1):
                j = i + ln - 1
                dp[i][j] = 1 + dp[i + 1][j] # 只列印第一個字母
                for k in range(i + 1, j):
                    if s[i] == s[k]:
                        dp[i][j] = min(dp[i][j], dp[i][k - 1] + dp[k + 1][j])
                if s[i] == s[j]:
                    dp[i][j] = min(dp[i][j], dp[i][j - 1])
        return dp[0][n - 1]
    
class Solution2:
    def strangePrinter(self, s: str) -> int:
        n = len(s)
        
        @cache
        def dfs(i, j):
            if i == j:
                return 1
            if i > j:
                return 0
            ans = 1 + dfs(i + 1, j) # 只列印第一個字母
            for k in range(i + 1, j + 1):
                if s[i] == s[k]:
                    ans = min(ans, dfs(i, k-1) + dfs(k+1, j))
            return ans
        
        return dfs(0, n-1)
    
class Solution(Solution2):
    pass
# @lc code=end

sol = Solution()
print(sol.strangePrinter("aaabbb"))
print(sol.strangePrinter("aba"))

#
# @lcpr case=start
# "aaabbb"\n
# @lcpr case=end

# @lcpr case=start
# "aba"\n
# @lcpr case=end

#

