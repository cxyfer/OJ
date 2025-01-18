# @algorithm @lc id=62 lang=python3 
# @title unique-paths


from en.Python3.mod.preImport import *
# @test(3,7)=28
# @test(3,2)=3
class Solution:
    """
        1. Combination
    """
    # def uniquePaths(self, m: int, n: int) -> int:
    #     factorial = [1 for _ in range(m+n-1)]
    #     for i in range(1, m+n-1):
    #         factorial[i] = factorial[i-1] * i
    #     return factorial[m+n-2] // (factorial[m-1] * factorial[n-1])
    """
        2. Dynamic Programming
    """
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1] # 可由上方或左方到達
        return dp[m-1][n-1]
        