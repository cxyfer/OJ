"""
    解法：根號分治 / Bitset / 啟發式合併

    1. 啟發式合併
    Ref: https://www.bilibili.com/video/BV1TZ421H7xo/
    時間複雜度：O(n log n) ，每次合併會使大小至少增加一倍，因此對於每個點，最多只會有 log n 次合併
"""
import sys
sys.setrecursionlimit(10**6) 

MOD = 998244353
N, Q = map(int, input().split())

# Disjoint Set
pa = list(range(N+1)) 
sz = [1] * (N+1)
def find(x: int) -> int:
    if pa[x] != x:
        pa[x] = find(pa[x])
    return pa[x]

# Graph
fa = [0] * (N+1)
g = [[] for _ in range(N+1)]
def dfs(u: int) -> None: # 啟發式合併，讓 u 作為子樹的根節點
    for v in g[u]:
        if v == fa[u]:
            continue
        fa[v] = u
        dfs(v)

ans = 0
for _ in range(Q):
    a, b, c = map(int, input().split())
    op = 1 + a * (1 + ans) % MOD % 2
    x = 1 + b * (1 + ans) % MOD % N
    y = 1 + c * (1 + ans) % MOD % N
    if op == 1:
        if sz[find(x)] > sz[find(y)]:
            x, y = y, x
        sz[find(y)] += sz[find(x)]
        pa[find(x)] = find(y)
        g[x].append(y)
        g[y].append(x)
        fa[x] = y
        dfs(x)
    else: # 要滿足條件，x 和 y 的距離必須為 2，且只有三種情況滿足
        if fa[x] != 0 and fa[x] == fa[y]: # 1. x 和 y 有相同的父節點
            ans = fa[x]
        elif fa[fa[x]] == y: # 2. x 和 y 在同一條鏈上，且 y 是 x 的祖父
            ans = fa[x]
        elif fa[fa[y]] == x: # 3. x 和 y 在同一條鏈上，且 x 是 y 的祖父
            ans = fa[y]
        else: # 不滿足
            ans = 0
        print(ans)