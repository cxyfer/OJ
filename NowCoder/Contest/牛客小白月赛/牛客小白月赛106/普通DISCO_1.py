from collections import deque
 
n = int(input())
g = [[] for _ in range(n)]
for _ in range(n - 1):
    u, v = map(lambda x: int(x) - 1, input().split())
    g[u].append(v)
    g[v].append(u)
 
fa = [-1] * n
dep = [0] * n
q = deque([(0, -1)])
while q:
    u, f = q.popleft()
    fa[u] = f
    dep[u] = dep[f] + 1 if f != -1 else 1
    for v in g[u]:
        if v == f:
            continue
        q.append((v, u))
# def dfs(u):
#     for v in g[u]:
#         if v == fa[u]:
#             continue
#         fa[v] = u
#         dep[v] = dep[u] + 1
#         dfs(v)
# dfs(0)

idx = 0
for u in range(n):
    if dep[u] > dep[idx]:
        idx = u
 
q = deque()
vis = [False] * n
t = idx
while t != -1:
    q.append((0, t))
    vis[t] = True
    t = fa[t]
 
ans = 1 # 這裡至少要是 1
while q:
    d, u = q.popleft()
    ans = max(ans, d)
    for v in g[u]:
        if vis[v]:
            continue
        vis[v] = True
        q.append((d + 1, v))
 
print(ans + dep[idx] - 1)