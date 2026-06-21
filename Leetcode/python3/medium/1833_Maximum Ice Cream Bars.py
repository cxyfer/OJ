#
# @lc app=leetcode id=1833 lang=python3
#
# [1833] Maximum Ice Cream Bars
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        # return bisect_right(list(accumulate(sorted(costs))), coins)
        n = len(costs)
        costs.sort()
        s = 0
        for i, c in enumerate(costs):
            s += c
            if s > coins:
                return i
        return n
# @lc code=end

