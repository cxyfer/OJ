"""
對於一個度數皆為 3 的連通分量，可以計算他相鄰的點中度數為 2 的點的數量 cnt
在這些度數為 2 的點中，任選兩個配對，即可滿足題目要求，故這個連通分量的貢獻為 cnt * (cnt - 1) // 2
可以用 BFS 或 DFS 找到所有度數皆為 3 的連通分量
"""
import sys
sys.setrecursionlimit(10**6)

N = int(input())
edges = [list(map(int, input().split())) for _ in range(N-1)]

g = [[] for _ in range(N + 1)]
deg = [0] * (N + 1)
for u, v in edges:
    g[u].append(v)
    g[v].append(u)
    deg[u] += 1
    deg[v] += 1

vis = [False] * (N + 1)
def dfs(u):
    if deg[u] != 3 or vis[u]:
        return 0
    vis[u] = True
    cnt = 0
    for v in g[u]:
        if deg[v] == 2:
            cnt += 1
        elif deg[v] == 3 and not vis[v]:
            cnt += dfs(v)
    return cnt

ans = 0
for x in range(1, N + 1):
    if deg[x] != 3 or vis[x]:
        continue
    cnt = dfs(x)
    ans += cnt * (cnt - 1) // 2
print(ans)