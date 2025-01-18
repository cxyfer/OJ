from collections import deque
 
n, m = map(int, input().split())
 
g = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(lambda x: int(x) - 1, input().split())
    g[u].append(v)
    g[v].append(u)
 
flag = True
colors = [0] * n
for u in range(n):
    if colors[u]:
        continue
    q = deque([u])
    colors[u] = 1
    while q:
        u = q.popleft()
        c = colors[u]
        for v in g[u]:
            if colors[v] == c:
                exit(print("IMPOSSIBLE"))
            if colors[v]:
                continue
            colors[v] = 3 - c
            q.append(v)
else:
    print(*colors)