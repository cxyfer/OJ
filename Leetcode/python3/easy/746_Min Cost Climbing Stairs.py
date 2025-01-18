#
# @lc app=leetcode id=746 lang=python3
# @lcpr version=30201
#
# [746] Min Cost Climbing Stairs
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * (n+1)
        for i in range(2, n+1):
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
        return dp[n]
# @lc code=end



#
# @lcpr case=start
# [10,15,20]\n
# @lcpr case=end

# @lcpr case=start
# [1,100,1,1,1,100,1,1,100,1]\n
# @lcpr case=end

#

