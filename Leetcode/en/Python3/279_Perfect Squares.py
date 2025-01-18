# @algorithm @lc id=279 lang=python3 
# @title perfect-squares


from en.Python3.mod.preImport import *
# @test(12)=3
# @test(13)=2
class Solution:
    """
        Dynamic Programming
        dp[i] 表示和為i的完全平方數的最小個數
    """
    def numSquares(self, n: int) -> int:
        dp = [0] * (n+1)
        for i in range(1, n+1):
            dp[i] = i # i = (1^2) * i
            for j in range(1, math.isqrt(i)+1): # j*j <= i
                dp[i] = min(dp[i], dp[i-j*j]+1)
        return dp[n]