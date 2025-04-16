"""
【华为】20230412_1_指令优先级
https://niumacode.com/problem/P1535
"""
from collections import deque

n, m = map(int, input().split())

g = [[] for _ in range(n + 1)]
ind = [0] * (n + 1)
for _ in range(m):
    u, v, w = map(int, input().split())
    g[v].append((u, w))
    ind[u] += 1

q = deque([u for u in range(1, n + 1) if ind[u] == 0])
dist = [0] * (n + 1)

while q:
    u = q.popleft()
    for v, w in g[u]:
        dist[v] = max(dist[v], dist[u] + w)
        ind[v] -= 1
        if ind[v] == 0:
            q.append(v)
print(*sorted(list(range(1, n + 1)), key=lambda x: (-dist[x], x)))