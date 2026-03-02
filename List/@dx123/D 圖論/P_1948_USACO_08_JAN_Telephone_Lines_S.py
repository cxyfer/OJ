"""
P1948 [USACO08JAN] Telephone Lines S
https://www.luogu.com.cn/problem/P1948
1. 二分 + BFS最短路
從最小化最大值可以想到二分，檢查函數可以將邊權大於mid的邊視為1，小於等於mid的邊視為0，然後跑BFS最短路
2. 分層圖最短路
將 dist[u] 視為到達u點路徑上最大邊權的最小值，然後跑分層圖最短路即可
"""

from collections import deque
from heapq import heappop, heappush


def solve1():
    n, m, k = map(int, input().split())

    g = [[] for _ in range(n)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        u, v = u - 1, v - 1
        g[u].append((v, w))
        g[v].append((u, w))

    def check(mid: int) -> bool:
        dist = [float("inf")] * n
        dist[0] = 0
        q = deque([(0, 0)])
        while q:
            d, u = q.popleft()
            for v, w in g[u]:
                w = 0 if w <= mid else 1
                nd = d + w
                if nd < dist[v]:
                    dist[v] = nd
                    q.append((nd, v))
        return dist[n - 1] <= k

    mx = max(max(w for _, w in g[u]) for u in range(n) if g[u])
    left, right = 0, mx
    while left <= right:
        mid = (left + right) // 2
        if check(mid):
            right = mid - 1
        else:
            left = mid + 1
    print(left if left <= mx else -1)


def solve2():
    n, m, k = map(int, input().split())

    g = [[] for _ in range(n)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        u, v = u - 1, v - 1
        g[u].append((v, w))
        g[v].append((u, w))

    dist = [[float("inf")] * (k + 1) for _ in range(n)]
    dist[0][0] = 0
    hp = [(0, 0, 0)]
    while hp:
        d, u, t = heappop(hp)
        if d > dist[u][t]:
            continue
        for v, w in g[u]:
            if t < k and d < dist[v][t + 1]:
                dist[v][t + 1] = d
                heappush(hp, (d, v, t + 1))
            nd = max(d, w)
            if nd < dist[v][t]:
                dist[v][t] = nd
                heappush(hp, (nd, v, t))
    print(ans if (ans := min(dist[n - 1])) != float("inf") else -1)


solve = solve2

if __name__ == "__main__":
    solve()
