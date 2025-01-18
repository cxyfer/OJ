from heapq import heappush, heappop

n, m = map(int, input().split())

g = [[] for _ in range(n)]
for _ in range(m):
    u, v, w = map(int, input().split())
    g[u - 1].append((v - 1, w))


dist = [float('inf')] * n
dist[0] = 0
hp = [(0, 0)]

while hp:
    d, u = heappop(hp)
    if d > dist[u]:
        continue
    for v, w in g[u]:
        nd = d + w
        if nd < dist[v]:
            dist[v] = nd
            heappush(hp, (nd, v))

print(*dist)