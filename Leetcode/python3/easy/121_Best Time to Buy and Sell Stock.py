#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
1. 枚舉右維護左，維護 prices 的前綴最小值

2. Dynamic Programming
定義 D[i] = prices[i] - prices[i-1]，則問題轉化為求 D 的最大子陣列和 (53. Maximum Subarray)
- 前綴和 + 枚舉右維護左的做法等同於 1. 維護 prices 的前綴最小值。
"""
# @lc code=start
class Solution1:
    def maxProfit(self, prices: list[int]) -> int:
        ans = 0
        mn = inf
        for p in prices:
            ans = max(ans, p - mn)
            mn = min(mn, p)
        return ans


class Solution2:
    def maxProfit(self, prices: list[int]) -> int:
        D = [b - a for a, b in pairwise(prices)]
        ans = f = 0
        for d in D:
            f = max(f + d, d)
            ans = max(ans, f)
        return ans


# Solution = Solution1
Solution = Solution2
# @lc code=end
