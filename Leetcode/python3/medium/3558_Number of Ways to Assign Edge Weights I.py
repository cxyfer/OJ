#
# @lc app=leetcode id=3558 lang=python3
#
# [3558] Number of Ways to Assign Edge Weights I
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        MOD = int(1e9 + 7)
        g = defaultdict(list)
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
        
        max_depth = 0
        def dfs(u, fa, depth):
            nonlocal max_depth
            max_depth = max(max_depth, depth)
            for v in g[u]:
                if v == fa:
                    continue
                dfs(v, u, depth + 1)
        dfs(1, 0, 0)
        return pow(2, max_depth - 1, MOD)
# @lc code=end

