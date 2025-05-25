#
# @lc app=leetcode id=3559 lang=python3
#
# [3559] Number of Ways to Assign Edge Weights II
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def assignEdgeWeights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        n = len(edges) + 1
        g = defaultdict(list)
        for u, v in edges:
            u, v = u - 1, v - 1
            g[u].append(v)
            g[v].append(u)
            
        m = n.bit_length()
        pa = [[-1] * m for _ in range(n)]
        depth = [0] * n
        def dfs(u: int, fa: int) -> None:
            pa[u][0] = fa
            for v in g[u]:
                if v == fa:
                    continue
                depth[v] = depth[u] + 1
                dfs(v, u)
        dfs(0, -1)

        for i in range(m - 1):
            for x in range(n):
                p = pa[x][i]
                if p != -1:
                    pa[x][i + 1] = pa[p][i]

        def lca(x: int, y: int) -> int:
            if depth[x] < depth[y]:
                x, y = y, x

            k = depth[x] - depth[y]
            for i in range(k.bit_length()):
                if (k >> i) & 1:
                    x = pa[x][i]

            if x == y:
                return x

            for i in range(m - 1, -1, -1):
                if pa[x][i] != pa[y][i]:
                    x, y = pa[x][i], pa[y][i]
            
            return pa[x][0]
        
        def get_distance(x: int, y: int) -> int:
            lca_node = lca(x, y)
            return depth[x] + depth[y] - 2 * depth[lca_node]

        ans = []
        for u, v in queries:
            u, v = u - 1, v - 1
            path_len = get_distance(u, v)
            ans.append(pow(2, path_len - 1, int(1e9 + 7)) if path_len > 0 else 0)
        return ans
# @lc code=end

