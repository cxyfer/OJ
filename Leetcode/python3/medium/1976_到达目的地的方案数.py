#
# @lc app=leetcode.cn id=1976 lang=python3
#
# [1976] 到达目的地的方案数
#
from preImport import *
# @lc code=start
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        g = [[float("inf") for _ in range(n)] for _ in range(n)]
        adj = [[] for _ in range(n)]
        for u, v, w in roads:
            g[u][v] = g[v][u] = w
            adj[u].append(v)
            adj[v].append(u)
        for i in range(n):
            g[i][i] = 0
        dist = [float("inf")] * n
        dist[0] = 0
        ans = [0] * n # ans[i] 表示以最短路到達 i 的方案數
        ans[0] = 1
        hp = [(0, 0)] # dist, node
        while hp:
            d, u = heappop(hp)
            if d > dist[u]:
                continue
            for v in adj[u]:
                t = d + g[u][v]
                if t < dist[v]: # 長度更短，從來源轉移
                    dist[v] = t
                    ans[v] = ans[u]
                    heappush(hp, (t, v))
                elif t == dist[v]: # 長度相同，累加
                    ans[v] = (ans[u] + ans[v]) % MOD
        return ans[-1]
# @lc code=end
sol = Solution()
print(sol.countPaths(2,[[1,0,10]])) # 1
print(sol.countPaths(7,[[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]])) # 4


