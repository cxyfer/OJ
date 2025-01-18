#
# @lc app=leetcode id=2285 lang=python3
# @lcpr version=30204
#
# [2285] Maximum Total Importance of Roads
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        deg = [0] * n
        for u, v in roads:
            deg[u] += 1
            deg[v] += 1
        deg.sort()
        ans = 0
        for i, x in enumerate(deg, 1):
            ans += x * i
        return ans
# @lc code=end



#
# @lcpr case=start
# 5\n[[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]]\n
# @lcpr case=end

# @lcpr case=start
# 5\n[[0,3],[2,4],[1,3]]\n
# @lcpr case=end

#

