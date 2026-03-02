"""
P4568 [JLOI2011] 飞行路线
https://www.luogu.com.cn/problem/P4568
分層圖最短路
Same as P2939 [USACO09FEB] Revamping Trails G
"""

from heapq import heappop, heappush


def solve():
    n, m, k = map(int, input().split())
    st, ed = map(lambda x: x - 1, map(int, input().split()))
    g = [[] for _ in range(n)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        u, v = u - 1, v - 1
        g[u].append((v, w))
        g[v].append((u, w))

    dist = [[float("inf")] * (k + 1) for _ in range(n)]
    dist[st][0] = 0
    hp = [(0, st, 0)]
    while hp:
        d, u, t = heappop(hp)
        if d > dist[u][t]:
            continue
        for v, w in g[u]:
            if t < k and d < dist[v][t + 1]:
                dist[v][t + 1] = d
                heappush(hp, (d, v, t + 1))
            nd = d + w
            if nd < dist[v][t]:
                dist[v][t] = nd
                heappush(hp, (nd, v, t))
    print(ans if (ans := min(dist[ed])) != float("inf") else -1)


if __name__ == "__main__":
    solve()
