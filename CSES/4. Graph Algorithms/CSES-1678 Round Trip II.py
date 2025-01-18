import sys
sys.setrecursionlimit(1 << 20)

n, m = map(int, input().split())

g = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    g[u].append(v)

vis = [0] * (n + 1) # 0: not visited, 1: visited, 2: visited and processed
fa = [-1] * (n + 1) 
def dfs(u):
    vis[u] = 1
    for v in g[u]:
        if vis[v] == 1:
            ans = [u]
            t = u
            while t != v:
                ans.append(fa[t])
                t = fa[t]
            ans.append(u)
            ans.reverse()
            print(len(ans))
            print(*ans)
            exit()
        if vis[v] == 2:
            continue
        fa[v] = u
        dfs(v)
    vis[u] = 2
    return

for u in range(1, n + 1):
    if vis[u]:
        continue
    dfs(u)
else:
    print("IMPOSSIBLE")
    exit()