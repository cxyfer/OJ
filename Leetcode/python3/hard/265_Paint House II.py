#
# @lc app=leetcode id=265 lang=python3
# @lcpr version=30204
#
# [265] Paint House II
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        n, k = len(costs), len(costs[0])

        @cache
        def dfs(i, pre):
            if i == n:
                return 0
            res = float('inf')
            for j in range(k):
                if j == pre:
                    continue
                res = min(res, costs[i][j] + dfs(i + 1, j))
            return res

        return dfs(0, -1)
# @lc code=end



#
# @lcpr case=start
# [[1,5,3],[2,9,4]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,3],[2,4]]\n
# @lcpr case=end

#

