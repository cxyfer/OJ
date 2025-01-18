# @algorithm @lc id=1236 lang=python3 
# @title n-th-tribonacci-number


from en.Python3.mod.preImport import *
# @test(4)=4
# @test(25)=1389537
class Solution:
    def tribonacci(self, n: int) -> int:
        dp = [0 for _ in range(max(3,n+1))]
        dp[0], dp[1], dp[2] = 0, 1, 1
        for i in range(3,n+1):
            dp[i] = dp[i-3] + dp[i-2] + dp[i-1]
        return dp[n]