"""
2134D - Sliding Tree 
https://codeforces.com/contest/2134/problem/D
構造

首先想一下怎樣可以使操作次數最少：
觀察給定的操作，操作後可以一條鏈的長度 + 1，後文圖解。
而目標為一個長度為 n - 1 的鏈，且原樹中最長的鏈長為其直徑，故在直徑上操作即可。

如何操作使一條鏈的長度 + 1：
考慮鏈上的兩點 (a, b)，以及與 b 相鄰但不在鏈上的點 c，
o - o - a - b - d - o - o
            |
    o - o - c
操作 (a, b, c) 後可以把 c 加入到鏈中，故長度 + 1
o - o - a - b
            |
    o - o - c - d - o - o
"""
from collections import deque

def solve():
    n = int(input())
    g = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = map(int, input().split())
        g[u].append(v)
        g[v].append(u)

    # 兩次 BFS 找直徑
    pa = [0] * (n + 1)
    dist = [0] * (n + 1)
    def bfs(st, fa):
        dist[st] = 0
        q = deque([(st, fa)])
        while q:
            u, fa = q.popleft()
            for v in g[u]:
                if v == fa:
                    continue
                pa[v] = u
                dist[v] = dist[u] + 1
                q.append((v, u))
    bfs(1, 0)
    x = max(range(1, n + 1), key=lambda u: dist[u])
    pa[x] = 0
    bfs(x, 0)
    y = max(range(1, n + 1), key=lambda u: dist[u])

    # 已經是 Path Graph
    if dist[y] == n - 1:
        print(-1)
        return

    on_diameter = [False] * (n + 1)
    while y != x:
        on_diameter[y] = True
        y = pa[y]
    on_diameter[x] = True

    a = b = c = -1
    for u in range(1, n + 1):
        if not on_diameter[u]:
            continue
        for v in g[u]:
            if on_diameter[v]:
                continue
            a, b, c = pa[u], u, v
            break
    print(a, b, c)

t = int(input())
for _ in range(t):
    solve()