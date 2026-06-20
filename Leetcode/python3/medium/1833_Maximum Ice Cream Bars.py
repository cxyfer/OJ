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
        costs.sort()
        ans = s = 0
        for i, c in enumerate(costs, start=1):
            s += c
            if s > coins:
                break
            ans = i
        return ans
# @lc code=end

