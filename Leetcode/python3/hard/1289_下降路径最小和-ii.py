#
# @lc app=leetcode.cn id=1289 lang=python3
#
# [1289] 下降路径最小和  II
#
from preImport import *
# @lc code=start
class Solution:
    """
        DP
    """
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dp = [[float('inf')] * n for _ in range(n)]
        for i in range(n):
            dp[0][i] = grid[0][i]
        for i in range(1, n):
            for j in range(n):
                dp[i][j] = min([dp[i-1][k] + grid[i][j] for k in range(n) if k != j])
        return min(dp[-1])
# @lc code=end

