from collections import deque
n = int(input())

g = [[] for _ in range(n)]
for _ in range(n - 1):
    u, v = map(lambda x: int(x) - 1, input().split())
    g[u].append(v)
    g[v].append(u)

def bfs(u, fa):
    q = deque([(u, fa)])
    dist = [float('inf')] * n
    dist[u] = 0
    while q:
        u, fa = q.popleft()
        for v in g[u]:
            if v == fa:
                continue
            dist[v] = dist[u] + 1
            q.append((v, u))
    return dist

d1 = bfs(0, -1)
u = d1.index(max(d1))
d2 = bfs(u, -1)
print(max(d2))