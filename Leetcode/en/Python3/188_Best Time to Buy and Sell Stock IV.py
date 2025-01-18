# @algorithm @lc id=188 lang=python3 
# @title best-time-to-buy-and-sell-stock-iv


from en.Python3.mod.preImport import *
# @test(2,[2,4,1])=2
# @test(2,[3,2,6,5,0,3])=7
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        dp = [[0, float('-inf')] for _ in range(k+1)]
        for price in prices:
            for i in range(1, k+1):
                dp[i][0] = max(dp[i][0], dp[i][1] + price)
                dp[i][1] = max(dp[i][1], dp[i-1][0] - price)
        return dp[k][0]