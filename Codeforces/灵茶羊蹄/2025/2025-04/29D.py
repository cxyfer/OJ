n = int(input())
g = [[] for _ in range(n+1)]
for _ in range(n-1):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)
leafs = list(map(int, input().split()))

mp = {u: i for i, u in enumerate(leafs, start=1)}

# f[u] 表示以 u 為根的子樹中最早出現的葉節點在目標序列中的順序
f = [float('inf')] * (n + 1)
def dfs1(u, fa):
    if u != 1 and len(g[u]) == 1: # 葉節點
        f[u] = mp[u]
        return
    for v in g[u]:
        if v == fa:
            continue
        dfs1(v, u)
        f[u] = min(f[u], f[v])
dfs1(1, 0)

# 構建答案，根據 f[u] 決定子樹的訪問順序
path = []
def dfs2(u, fa):
    path.append(u)
    for v in sorted([v for v in g[u] if v != fa], key=lambda v: f[v]):
        dfs2(v, u)
        path.append(u)
dfs2(1, 0)

# 檢查構建的答案是否符合題目要求
# 1. 路徑長度為 2 * n - 1
# 2. 由於葉節點在 DFS 過程中只會出現一次（不會重複），因此可以直接檢查順序
if len(path) != 2 * n - 1 or leafs != [u for u in path if u != 1 and len(g[u]) == 1]:
    exit(print(-1))

print(*path)