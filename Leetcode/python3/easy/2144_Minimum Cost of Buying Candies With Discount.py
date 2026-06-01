#
# @lc app=leetcode id=2144 lang=python3
#
# [2144] Minimum Cost of Buying Candies With Discount
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        n = len(cost)
        cost.sort(reverse=True)
        # return sum(cost) - sum(cost[2::3])
        ans = 0
        for i in range(0, ((n + 2) // 3) * 3, 3):  # ceil(n / 3) * 3
            ans += cost[i]
            if i + 1 < n:
                ans += cost[i + 1]
        return ans
# @lc code=end

