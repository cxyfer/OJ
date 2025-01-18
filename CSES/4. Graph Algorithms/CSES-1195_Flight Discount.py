"""
分別從起點和終點跑一次 Dijkstra，之後枚舉要在哪條邊上使用折價券
"""
import sys
input = lambda: sys.stdin.readline().strip()
print = lambda val: sys.stdout.write(str(val) + "\n")

from heapq import *

n, m = map(int, input().split())
edges = []
for _ in range(m):
    u, v, w = map(int, input().split())
    edges.append((u - 1, v - 1, w))

g1 = [[] for _ in range(n)]
g2 = [[] for _ in range(n)]
for u, v, w in edges:
    g1[u].append((v, w))
    g2[v].append((u, w))

def dijkstra(g, st):
    dist = [float('inf')] * n
    dist[st] = 0
    hp = [(0, st)]
    while hp:
        d, u = heappop(hp)
        if d > dist[u]:
            continue
        for v, w in g[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heappush(hp, (nd, v))
    return dist

dist1 = dijkstra(g1, 0)
dist2 = dijkstra(g2, n - 1)

# 枚舉要使用折價券的邊
ans = float('inf')
for u, v, w in edges:
    ans = min(ans, dist1[u] + w // 2 + dist2[v])
print(ans)