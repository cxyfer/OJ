"""
P4017 最大食物链计数
https://www.luogu.com.cn/problem/P4017
拓樸排序DP / 記憶化搜索

有兩種定義方式：
1. 令 f[u] 表示從一個入度為0的點出發，到達u的路徑數
2. 令 f[u] 表示從u出發，到達一個出度為0的點的路徑數

正向建圖時分別可以使用 拓樸排序DP / 記憶化搜索 來解決，
反向建圖時分別改成使用 記憶化搜索 / 拓樸排序DP 即可。
"""

from collections import deque
from functools import cache

MOD = 80112002


def solve1():
    n, m = map(int, input().split())

    g = [[] for _ in range(n)]
    ideg = [0] * n
    odeg = [0] * n
    for _ in range(m):
        u, v = map(lambda x: int(x) - 1, input().split())
        g[u].append(v)
        odeg[u] += 1
        ideg[v] += 1

    # f[u] 表示從一個入度為0的點出發，到達u的路徑數
    f = [0] * n
    q = deque()
    for u in range(n):
        if ideg[u] == 0:
            f[u] = 1
            q.append(u)

    while q:
        u = q.popleft()
        for v in g[u]:
            ideg[v] -= 1
            f[v] = (f[v] + f[u]) % MOD
            if ideg[v] == 0:
                q.append(v)

    ans = 0
    for u in range(n):
        if odeg[u] == 0:
            ans = (ans + f[u]) % MOD
    print(ans)


def solve2():
    n, m = map(int, input().split())

    g = [[] for _ in range(n)]
    ideg = [0] * n
    odeg = [0] * n
    for _ in range(m):
        u, v = map(lambda x: int(x) - 1, input().split())
        g[u].append(v)
        odeg[u] += 1
        ideg[v] += 1

    # dfs(u) 表示從u出發，到達一個出度為0的點的路徑數
    @cache
    def dfs(u: int) -> int:
        if odeg[u] == 0:
            return 1
        res = 0
        for v in g[u]:
            res += dfs(v)
        return res

    ans = 0
    for u in range(n):
        if ideg[u] == 0:
            ans = (ans + dfs(u)) % MOD
    print(ans)


solve = solve1
# solve = solve2

if __name__ == "__main__":
    solve()
