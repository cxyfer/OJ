0#
# @lc app=leetcode.cn id=309 lang=python3
#
# [309] 买卖股票的最佳时机含冷冻期
#
from preImport import *
# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        # dp[i+1][j] 表示第i天交易後的狀態，j=0表示不持有股票，j=1表示持有股票
        dp = [[0, 0] for _ in range(n+2)]
        dp[1][1] = -float('inf') # 第0天不可能持有股票
        for i in range(1, n+1): # i=1,2,...,n
            # 今天不持有：前一天不持有股票繼續不持有 / 兩天前持有股票且今天賣出
            dp[i+1][0] = max(dp[i][0], dp[i][1] + prices[i-1]) 
            # 今天持有：前一天持有股票繼續持有 / 兩天前不持有股票且今天買入
            dp[i+1][1] = max(dp[i][1], dp[i-1][0] - prices[i-1]) 
        return dp[n+1][0]
# @lc code=end

