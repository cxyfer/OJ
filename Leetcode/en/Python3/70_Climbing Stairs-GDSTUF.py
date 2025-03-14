# @algorithm @lc id=70 lang=python3 
# @title climbing-stairs


from en.Python3.mod.preImport import *
# @test(2)=2
# @test(3)=3
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0 for _ in range(n+1)]
        dp[0] = 1
        dp[1] = 1
        for i in range(2,n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]