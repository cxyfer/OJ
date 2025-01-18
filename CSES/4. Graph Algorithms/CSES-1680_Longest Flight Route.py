from collections import deque

n, m = map(int, input().split())

g = [[] for _ in range(n)]
ind = [0] * n
for _ in range(m):
    u, v = map(lambda x: int(x) - 1, input().split())
    g[u].append(v)
    ind[v] += 1

dist = [-float('inf')] * n
prev = [-1] * n
dist[0] = 1
q = deque([u for u in range(n) if ind[u] == 0])
while q:
    u = q.popleft()
    for v in g[u]:
        if dist[v] < dist[u] + 1:
            dist[v] = dist[u] + 1
            prev[v] = u
        ind[v] -= 1
        if ind[v] == 0:
            q.append(v)

if dist[n - 1] == -float('inf'):
    print("IMPOSSIBLE")
    exit()

path = []
u = n - 1
while u != -1:
    path.append(u + 1)
    u = prev[u]

print(dist[n - 1])
print(*path[::-1])