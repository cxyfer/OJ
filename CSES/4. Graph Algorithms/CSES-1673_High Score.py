from typing import NamedTuple

class Edge(NamedTuple):
    st: int
    ed: int
    w: int

n, m = map(int, input().split())
edges = []
for _ in range(m):
    u, v, w = map(int, input().split())
    edges.append(Edge(u - 1, v - 1, w))

dist = [float('-inf')] * n
dist[0] = 0
for _ in range(n):
    for e in edges:
        if dist[e.st] != float('-inf'):
            dist[e.ed] = max(dist[e.ed], dist[e.st] + e.w)

for _ in range(n):
    for e in edges:
        if dist[e.st] == float('inf'):
            dist[e.ed] = float('inf')
            continue
        if (dist[e.st] != float('-inf') and dist[e.st] + e.w > dist[e.ed]):
            dist[e.ed] = float('inf')

print(-1 if dist[n-1] == float('inf') else dist[n-1])