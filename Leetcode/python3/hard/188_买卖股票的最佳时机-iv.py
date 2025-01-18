88#
# @lc app=leetcode.cn id=188 lang=python3
#
# [188] 买卖股票的最佳时机 IV
#
from preImport import *
# @lc code=start
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        dp = [[0, float('-inf')] for _ in range(k+1)]
        for price in prices:
            for i in range(1, k+1):
                dp[i][0] = max(dp[i][0], dp[i][1] + price)
                dp[i][1] = max(dp[i][1], dp[i-1][0] - price)
        return dp[k][0]
# @lc code=end

