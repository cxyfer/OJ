# @algorithm @lc id=123 lang=python3 
# @title best-time-to-buy-and-sell-stock-iii


from en.Python3.mod.preImport import *
# @test([3,3,5,0,0,3,1,4])=6
# @test([1,2,3,4,5])=4
# @test([7,6,4,3,1])=0
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        n = len(prices)
        # dp[i][j][k] 表示第i天，第j次交易(賣出次數)，是否持有股票
        dp = [[[0, 0] for _ in range(3)] for _ in range(n)]
        dp[0][0][1] = -prices[0] # 第一天買入
        for j in range(1,3): # 第一天不可能賣出
            for k in range(2):
                dp[0][j][k] = float('-inf') 
        for i in range(1, n):
            # 未持股，未賣出過，說明從未進行過買賣
            # dp[i][0][0] = 0 
            # 未持股，賣出過1次，可能是之前賣的，可能是今天賣的(前一天之前賣過0次且持有股票)
            dp[i][1][0] = max(dp[i-1][1][0], dp[i-1][0][1] + prices[i])
            # 未持股，賣出過2次，可能是之前賣的，可能是今天賣的(前一天之前賣過1次且持有股票)
            dp[i][2][0] = max(dp[i-1][2][0], dp[i-1][1][1] + prices[i])
            # 持股，未賣出過，可能是之前買的，可能是今天買的
            dp[i][0][1] = max(dp[i-1][0][1], dp[i-1][0][0] - prices[i])
            # 持股，賣出過1次，可能是之前買的，可能是今天買的
            dp[i][1][1] = max(dp[i-1][1][1], dp[i-1][1][0] - prices[i])
            # 持股，賣出過2次，不可能
            # dp[i][2][1] = float('-inf')
        return max(dp[n-1][0][0], dp[n-1][1][0], dp[n-1][2][0])