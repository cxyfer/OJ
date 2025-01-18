# @algorithm @lc id=121 lang=python3 
# @title best-time-to-buy-and-sell-stock

from en.Python3.mod.preImport import *
# @test([7,1,5,3,6,4])=5
# @test([7,6,4,3,1])=0
class Solution:
    """
        1. Dynamic Programming
        Transfrom to max subarray problem
    """
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 1: # base case
            return 0
        diffs = [prices[i]-prices[i-1] for i in range(1, n)]
        ans = diffs[0]
        dp = [0] * (n-1)
        dp[0] = diffs[0]
        for i in range(1, n-1):
            # diffs[i-1] 或 diffs[i-1]，從diffs[i]開始重新計算
            dp[i] = max(diffs[i], dp[i-1] + diffs[i])
            ans = max(ans, dp[i])
        return ans if ans > 0 else 0