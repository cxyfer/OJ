#
# @lc app=leetcode.cn id=1335 lang=python3
#
# [1335] 工作计划的最低难度
#
from preImport import *
# @lc code=start
class Solution:
    """
        DP
        將 jobDifficulty 分成 d 個子區間，求每個子區間的最大值，使得這些最大值的和最小
    """
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if n < d:
            return -1
        
        # 1:1 翻譯成 iterative
        dp = [[float('inf')]*(n+1) for _ in range(d+1)]
        for j in range(1, n+1):
            dp[1][j] = max(jobDifficulty[:j])
        for i in range(2, d+1):
            for j in range(i, n+1):
                mx = jobDifficulty[j-1]
                for k in range(j-1, i-2, -1):
                    mx = max(mx, jobDifficulty[k])
                    dp[i][j] = min(dp[i][j], dp[i-1][k] + mx)
        return dp[d][n]

        @cache # Memoization
        def dp(i, j): # 令 dp(i, j) 表示前i天完成j個工作的最小難度
            if i == 1: # 只有一天，則最小難度為這一天的最大難度
                return max(jobDifficulty[:j])
            mx = jobDifficulty[j-1] # 今日至少要完成 第j個 工作，所以最大難度初始化為 jobDifficulty[j-1]
            res = dp(i-1, j-1) + mx # 今日的最大難度，從 前i-1天完成j-1個工作的最小難度 轉移
            for k in range(j-2, i-2, -1): # 可以從 前i-1天完成k個工作的最小難度 轉移，而前 i-1 天最少要完成 i-1 個工作
                mx = max(mx, jobDifficulty[k]) # 今日任務又多了一個，所以最大難度要更新
                res = min(res, dp(i-1, k) + mx)
            return res
        return dp(d, n)
# @lc code=end
sol = Solution()
print(sol.minDifficulty([6,5,4,3,2,1],2)) # 7
print(sol.minDifficulty([9,9,9],4)) # -1
print(sol.minDifficulty([1,1,1],3)) # 3