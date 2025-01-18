#
# @lc app=leetcode id=2959 lang=python3
# @lcpr version=30204
#
# [2959] Number of Possible Sets of Closing Branches
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
"""
    狀態壓縮 + Floyd-Warshall
"""
class Solution:
    def numberOfSets(self, n: int, maxDistance: int, roads: List[List[int]]) -> int:
        # Build graph
        g = [[float('inf')] * n for _ in range(n)]
        for i in range(n):
            g[i][i] = 0
        for u, v, w in roads:
            g[u][v] = min(g[u][v], w)
            g[v][u] = min(g[v][u], w)
        
        ans = 0
        g2 = [[] for _ in range(n)] # subgraph
        for mask in range(1 << n): # 狀態壓縮
            for i in range(n):
                if mask >> i & 1:
                    g2[i] = g[i][:] # copy
            # Floyd-Warshall
            for k in range(n):
                if mask >> k & 1 == 0: continue
                for i in range(n):
                    if mask >> i & 1 == 0: continue
                    for j in range(n):
                        if g2[i][k] + g2[k][j] < g2[i][j]:
                            g2[i][j] = g2[i][k] + g2[k][j]
            # Check
            flag = True
            for i in range(n):
                if mask >> i & 1 == 0: continue
                for j in range(n):
                    if mask >> j & 1 == 0: continue
                    if g2[i][j] > maxDistance:
                        flag = False
                        break
                if not flag:
                    break
            ans += flag
        return ans
# @lc code=end



#
# @lcpr case=start
# 3\n5\n[[0,1,2],[1,2,10],[0,2,10]]\n
# @lcpr case=end

# @lcpr case=start
# 3\n5\n[[0,1,20],[0,1,10],[1,2,2],[0,2,2]]\n
# @lcpr case=end

# @lcpr case=start
# 1\n10\n[]\n
# @lcpr case=end

#

