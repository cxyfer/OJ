# @algorithm @lc id=1224 lang=python3 
# @title minimum-falling-path-sum-ii


from en.Python3.mod.preImport import *
# @test([[1,2,3],[4,5,6],[7,8,9]])=13
# @test([[7]])=7
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