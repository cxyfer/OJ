from collections import deque
from functools import cache
import sys
sys.setrecursionlimit(int(2e5 + 100))

def solve1():
    n, m = map(int, input().split())
    g = [[] for _ in range(n)]
    deg = [0] * n
    for _ in range(m):
        u, v = map(lambda x: int(x) - 1, input().split())
        g[u].append(v)
        deg[v] += 1

    # f[u] 表示以 u 為終點的最長路徑長度
    f = [0] * n
    q = deque(u for u in range(n) if deg[u] == 0)
    while q:
        u = q.popleft()
        for v in g[u]:
            f[v] = max(f[v], f[u] + 1)
            deg[v] -= 1
            # 要確定 v 的所有前驅都已經被處理過了
            if deg[v] == 0:
                q.append(v)
    print(max(f))

def solve2():
    n, m = map(int, input().split())
    rg = [[] for _ in range(n)]   # 反圖
    for _ in range(m):
        u, v = map(lambda x: int(x) - 1, input().split())
        rg[v].append(u)

    # dfs(u) 表示以 u 為終點(在反圖上的起點)的最長路徑長度
    @cache
    def dfs(u: int) -> int:
        res = 0
        for v in rg[u]:
            res = max(res, dfs(v) + 1)
        return res
    print(max(dfs(u) for u in range(n)))

solve = solve2
if __name__ == "__main__":
    solve()