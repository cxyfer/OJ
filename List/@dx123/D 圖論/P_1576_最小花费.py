"""
P1576 最小花费
https://www.luogu.com.cn/problem/P1576

如果手續費為 x %，則需要支付 100 / (100 - x) 倍的金額才能收到想要的金額。
將倍率視為邊權，距離視為需要支付的金額，則可以將問題轉換為最短路問題。
"""

from heapq import heappop, heappush


def solve():
    n, m = map(int, input().split())
    g = [[] for _ in range(n)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        u, v = u - 1, v - 1
        w = 100 / (100 - w)
        g[u].append((v, w))
        g[v].append((u, w))

    st, ed = map(lambda x: int(x) - 1, input().split())
    dist = [float("inf")] * n
    dist[st] = 100.0
    hp = [(100.0, st)]
    while hp:
        d, u = heappop(hp)
        if d > dist[u]:
            continue
        for v, w in g[u]:
            nd = d * w
            if nd < dist[v]:
                dist[v] = nd
                heappush(hp, (nd, v))

    print(f"{dist[ed]:.8f}")


if __name__ == "__main__":
    solve()
