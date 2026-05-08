"""
P2196 [NOIP 1996 提高组] 挖地雷
https://www.luogu.com.cn/problem/P2196
"""

from functools import cache


def solve1():
    n = int(input())
    A = list(map(int, input().split()))

    g = [[] for _ in range(n)]
    for u in range(n - 1):
        vs = list(map(int, input().split()))
        for v, s in enumerate(vs, start=u + 1):
            if s == 1:
                g[u].append(v)

    @cache
    def dfs(u: int) -> int:
        if u >= n:
            return 0
        res = 0
        for v in g[u]:
            res = max(res, dfs(v))
        return res + A[u]

    st = max(range(n), key=dfs)

    u = st
    path = []
    while u < n:
        path.append(u + 1)
        v = u + 1
        while v < n and dfs(v) + A[u] != dfs(u):
            v += 1
        u = v

    print(*path)
    print(dfs(st))


def solve2():
    n = int(input())
    A = list(map(int, input().split()))

    g = [[] for _ in range(n)]
    for u in range(n - 1):
        vs = list(map(int, input().split()))
        for v, s in enumerate(vs, start=u + 1):
            if s == 1:
                g[u].append(v)

    f = [0] * n
    for u in range(n - 1, -1, -1):
        f[u] = A[u]
        for v in g[u]:
            f[u] = max(f[u], f[v] + A[u])

    st = max(list(range(n)), key=lambda x: f[x])

    u = st
    path = []
    while u < n:
        path.append(u + 1)
        v = u + 1
        while v < n and f[v] + A[u] != f[u]:
            v += 1
        u = v

    print(*path)
    print(f[st])


solve = solve1
# solve = solve2

if __name__ == "__main__":
    solve()
