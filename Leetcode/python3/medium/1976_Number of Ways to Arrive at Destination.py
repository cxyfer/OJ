#
# @lc app=leetcode id=1976 lang=python3
#
# [1976] Number of Ways to Arrive at Destination
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = int(1e9 + 7)
        g = [[] for _ in range(n)]
        for u, v, w in roads:
            g[u].append((v, w))
            g[v].append((u, w))
        dist = [float("inf")] * n
        ans = [0] * n
        dist[0] = 0
        ans[0] = 1
        hp = [(0, 0)]  # (dist, node)
        while hp:
            d, u = heappop(hp)
            if dist[u] < d:
                continue
            for v, w in g[u]:
                nd = dist[u] + w
                if nd < dist[v]:
                    dist[v] = nd
                    ans[v] = ans[u]
                    heappush(hp, (nd, v))
                elif nd == dist[v]:
                    ans[v] = (ans[u] + ans[v]) % MOD
        return ans[n - 1]
# @lc code=end

