# @algorithm @lc id=747 lang=python3 
# @title min-cost-climbing-stairs


from en.Python3.mod.preImport import *
# @test([10,15,20])=15
# @test([1,100,1,1,1,100,1,1,100,1])=6
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0]*(n+1)
        dp[0], dp[1] = 0, 0
        for i in range(2, n+1):
            dp[i] = min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2])
        return dp[-1]