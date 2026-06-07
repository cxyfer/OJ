#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#


# @lcpr-template-start
from preImport import *

# @lcpr-template-end
"""
1. Dynamic Programming
定義 D[i] = prices[i] - prices[i-1]，則問題轉化為求 D 的最大子陣列和

2. 
"""


# @lc code=start
class Solution1:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 1:  # base case
            return 0
        D = [b - a for a, b in pairwise(prices)]
        f = [0] * (n - 1)
        f[0] = D[0]
        for i in range(1, n - 1):
            f[i] = max(D[i], f[i - 1] + D[i])
        return max(max(f), 0)


class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        mn = float("inf")
        for p in prices:
            ans = max(ans, p - mn)
            mn = min(mn, p)
        return ans


# Solution = Solution1
Solution = Solution2
# @lc code=end
