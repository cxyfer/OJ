from heapq import *

MOD = 100003

n, m = map(int, input().split())

g = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(lambda x: int(x) - 1, input().split())
    g[u].append(v)
    g[v].append(u)

ans = [0] * n
dist = [float('inf')] * n
dist[0] = 0
ans[0] = 1

hp = [(0, 0)] # (dist, node)

while hp:
    d, u = heappop(hp)
    if d > dist[u]:
        continue
    for v in g[u]:
        nd = d + 1
        if nd < dist[v]:
            dist[v] = nd
            ans[v] = ans[u]
            heappush(hp, (nd, v))
        elif nd == dist[v]:
            ans[v] += ans[u]
            ans[v] %= MOD

print(*ans, sep='\n')