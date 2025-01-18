from math import sqrt
from heapq import *

n = int(input())
P = [tuple(map(int, input().split())) for _ in range(n)]

def dist(a, b):
    return sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

g = [[] for _ in range(n)]
m = int(input())
for _ in range(m):
    u, v = map(lambda x: int(x) - 1, input().split())
    d = dist(P[u], P[v])
    g[u].append((v, d))
    g[v].append((u, d))

st, ed = map(lambda x: int(x) - 1, input().split())


hp = [(0, st)]
dist = [float('inf')] * n
dist[st] = 0
while hp:
    d, u = heappop(hp)
    if d > dist[u]:
        continue
    for v, w in g[u]:
        nd = d + w
        if nd < dist[v]:
            dist[v] = nd
            heappush(hp, (nd, v))

print(f"{dist[ed]:.2f}")