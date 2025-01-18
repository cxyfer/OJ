"""
Eulerian Circuit + FLoyd-Warshall + Bitmask DP
"""
from functools import cache

while True:
    n, *args = map(int, input().split())
    if n == 0:
        break
    m = args[0]
    g = [[float("inf")] * n for _ in range(n)]
    cnt = [0] * n
    tot = 0
    for i in range(n):
        g[i][i] = 0
    for _ in range(m):
        u, v, w = map(int, input().split())
        u -= 1
        v -= 1
        g[u][v] = min(g[u][v], w)
        g[v][u] = min(g[v][u], w)
        cnt[u] += 1
        cnt[v] += 1
        tot += w

    # Floyd-Warshall
    for k in range(n):
        for i in range(n):
            if i == k or g[i][k] == float("inf"):
                continue
            for j in range(n):
                if j == k or g[k][j] == float("inf"):
                    continue
                g[i][j] = min(g[i][j], g[i][k] + g[k][j])

    odds = [u for u in range(n) if cnt[u] & 1]
    t = len(odds)
    u = (1 << t) - 1

    @cache
    def dfs(s):
        if s == u:
            return 0
        res = float("inf")
        for i in range(t):
            if s & (1 << i):
                continue
            for j in range(i + 1, t):
                if s & (1 << j):
                    continue
                res = min(res, dfs(s | (1 << i) | (1 << j)) + g[odds[i]][odds[j]])
        return res

    print(tot + dfs(0))