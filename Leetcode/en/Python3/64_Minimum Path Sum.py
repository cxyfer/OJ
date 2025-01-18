# @algorithm @lc id=64 lang=python3 
# @title minimum-path-sum


from en.Python3.mod.preImport import *
# @test([[1,3,1],[1,5,1],[4,2,1]])=7
# @test([[1,2,3],[4,5,6]])=12
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[-1])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(n):
            dp[0][i] = grid[0][i] + (dp[0][i-1] if i > 0 else 0) # 只能由左方到達
        for i in range(1, m):
            dp[i][0] = grid[i][0] + dp[i-1][0] # 只能由上方到達
            for j in range(1, n):
                dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1]) # 可由上方或左方到達，取最小
        return dp[m-1][n-1]