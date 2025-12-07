#
# @lc app=leetcode id=3772 lang=python3
#
# [3772] Maximum Subgraph Score in a Tree
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def maxSubgraphScore(self, n: int, edges: List[List[int]], good: List[int]) -> List[int]:
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        ans = [0] * n
        f = [0] * n
        def dfs(u: int, fa: int) -> None:
            f[u] = 1 if good[u] else -1
            for v in g[u]:
                if v == fa:
                    continue
                dfs(v, u)
                f[u] += max(0, f[v])
        dfs(0, -1)
        ans[0] = f[0]
        
        def reroot(u: int, fa: int) -> None:
            for v in g[u]:
                if v == fa:
                    continue
                ans[v] = f[v] + max(0, ans[u] - max(f[v], 0))
                reroot(v, u)
        reroot(0, -1)
        return ans
# @lc code=end

