#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#
from preImport import *
# @lc code=start
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
# @lc code=end

