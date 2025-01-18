# @algorithm @lc id=122 lang=python3 
# @title best-time-to-buy-and-sell-stock-ii


from en.Python3.mod.preImport import *
# @test([7,1,5,3,6,4])=7
# @test([1,2,3,4,5])=4
# @test([7,6,4,3,1])=0
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