#
# @lc app=leetcode id=1029 lang=python3
#
# [1029] Two City Scheduling
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs) // 2
        costs.sort(key=lambda x: x[0] - x[1])
        return sum(cost[0] if i < n else cost[1] for i, cost in enumerate(costs))
# @lc code=end

sol = Solution()
print(sol.twoCitySchedCost([[10, 20], [30, 200], [400, 50], [30, 20]]))  # 110
