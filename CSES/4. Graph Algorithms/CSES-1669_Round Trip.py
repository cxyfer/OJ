import sys
sys.setrecursionlimit(1 << 20)

n, m = map(int, input().split())

g = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(lambda x: int(x) - 1, input().split())
    g[u].append(v)
    g[v].append(u)

fa = list(range(n))
vis = [False] * n
def dfs(u):
    for v in g[u]:
        if v == fa[u]:
            continue
        if vis[v]: # 找到環
            path = [u]
            while path[-1] != v:
                path.append(fa[path[-1]])
            path.append(u)
            print(len(path))
            print(" ".join(map(lambda x: str(x + 1), path)))
            exit()
        vis[v] = True
        fa[v] = u
        dfs(v)

for u in range(n):
    if vis[u]:
        continue
    vis[u] = True
    dfs(u)

print("IMPOSSIBLE")
