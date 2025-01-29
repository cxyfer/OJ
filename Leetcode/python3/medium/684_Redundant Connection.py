#
# @lc app=leetcode id=684 lang=python3
# @lcpr version=30204
#
# [684] Redundant Connection
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        pa = list(range(n + 1))
        sz = [1] * (n + 1)

        def find(x):
            while x != pa[x]:
                pa[x] = pa[pa[x]]
                x = pa[x]
            return x
        
        for x, y in edges:
            fx, fy = find(x), find(y)
            if fx == fy:
                return [x, y]
            if sz[fx] < sz[fy]:
                fx, fy = fy, fx
            pa[fy] = pa[fx]
            sz[fx] += sz[fy]
        return [-1, -1]
# @lc code=end



#
# @lcpr case=start
# [[1,2],[1,3],[2,3]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,2],[2,3],[3,4],[1,4],[1,5]]\n
# @lcpr case=end

#

