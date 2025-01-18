#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
#
from preImport import *
# @lc code=start
class Solution:
    """
        Greedy
    """
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        ans = 0
        for i in range(1, n):
            ans += max(0, prices[i] - prices[i - 1])
        return ans
# @lc code=end

