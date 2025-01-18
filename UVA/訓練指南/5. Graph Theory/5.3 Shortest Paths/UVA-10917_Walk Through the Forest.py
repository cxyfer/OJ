from heapq import *
from functools import cache

while True:
    args = list(map(int, input().split()))
    if len(args) == 1 and args[0] == 0: break
    n, m = args[0], args[1]
    g = [[] for _ in range(n + 1)]
    edges = [list(map(int, input().split())) for _ in range(m)]
    for u, v, w in edges:
        g[u].append((v, w))
        g[v].append((u, w))

    # Dijkstra 求各個點到家(2)的最短距離
    dist = [float('inf')] * (n + 1) # 各個點到家(2)的最短距離
    dist[2] = 0
    hp = [(0, 2)] # (d, u)
    while hp:
        d, u = heappop(hp)
        if d > dist[u]: continue
        for v, w in g[u]:
            if d + w < dist[v]:
                dist[v] = d + w
                heappush(hp, (dist[v], v))

    # 根據題意，保留 dist[u] > dist[v] 的有向邊
    rg = [[] for _ in range(n + 1)] # 建反向圖
    for u, v, _ in edges:
        if dist[u] > dist[v]: # u -> v
            rg[v].append(u)
        elif dist[v] > dist[u]: # v -> u
            rg[u].append(v)

    # dfs(v) 表示從公司(1)出發，到達 v 的路徑數
    @cache
    def dfs(v: int) -> int: 
        if v == 1: return 1
        res = 0
        for u in rg[v]:
            res += dfs(u)
        return res
    print(dfs(2)) # 從公司(1)出發，到達家(2)的路徑數