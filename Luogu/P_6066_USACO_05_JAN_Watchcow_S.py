import sys
sys.setrecursionlimit(int(1e5))

n, m = map(int, input().split())
g = [[] for _ in range(n + 1)]
deg = [0] * (n + 1)
for idx in range(m):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)
    deg[u] += 1
    deg[v] += 1

path = []
def dfs(u):
    while g[u]:
        v = g[u].pop(0)
        dfs(v)
    path.append(u)
dfs(1)
print(*path[::-1], sep='\n')