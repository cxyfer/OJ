#
# @lc app=leetcode id=3652 lang=python3
#
# [3652] Best Time to Buy and Sell Stock using Strategy
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n = len(prices)
        sp = list(accumulate(prices, initial=0))
        ss = list(accumulate([s * p for s, p in zip(strategy, prices)], initial=0))
        ans = ss[n]
        for i in range(k, n + 1):
            origin = ss[n] - ss[i] + ss[i - k]
            # hold = sp[i - k // 2] - sp[i - k]
            sell = sp[i] - sp[i - k // 2]
            ans = max(ans, origin + sell)
        return ans
# @lc code=end

