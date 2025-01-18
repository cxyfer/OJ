from collections import deque

n, m = map(int, input().split())

g = [[] for _ in range(n + 1)]
ind = [0] * (n + 1)
for _ in range(m):
    u, v = map(int, input().split())
    g[u].append(v)
    ind[v] += 1

ans = []
q = deque([u for u in range(1, n + 1) if ind[u] == 0])
while q:
    u = q.popleft()
    ans.append(u)
    for v in g[u]:
        ind[v] -= 1
        if ind[v] == 0:
            q.append(v)

if len(ans) == n:
    print(*ans)
else:
    print("IMPOSSIBLE")