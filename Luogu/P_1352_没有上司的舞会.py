import sys
sys.setrecursionlimit(1 << 20)

n = int(input())
W = [int(input()) for _ in range(n)]
indeg = [0] * n
g = [[] for _ in range(n)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    g[v - 1].append(u - 1)
    indeg[u - 1] += 1

def dfs(u, fa):
    f0, f1 = 0, W[u] # 不選 u / 選 u
    for v in g[u]:
        if v == fa:
            continue
        g0, g1 = dfs(v, u)
        f0 += max(g0, g1)
        f1 += g0
    return f0, f1

root = 0
for i in range(n):
    if indeg[i] == 0:
        root = i
        break
else:
    raise ValueError("No root found")

print(max(dfs(root, -1)))
