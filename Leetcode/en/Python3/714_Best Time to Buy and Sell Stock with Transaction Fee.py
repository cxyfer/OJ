# @algorithm @lc id=714 lang=python3 
# @title best-time-to-buy-and-sell-stock-with-transaction-fee


from en.Python3.mod.preImport import *
# @test([1,3,2,8,4,9],2)=8
# @test([1,3,7,5,10,3],3)=6
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        # dp[i][j] 表示第i天交易後的狀態，j=0表示不持有股票，j=1表示持有股票
        dp = [[0,0] for _ in range(n+1)]
        dp[0][1] = -float('inf') # 第0天不可能持有股票
        for i in range(1, n+1):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i-1] - fee) # 前一天不持有股票繼續不持有 / 前一天持有股票且今天賣出
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i-1]) # 前一天持有股票繼續持有 / 前一天不持有股票且今天買入
        return dp[n][0]