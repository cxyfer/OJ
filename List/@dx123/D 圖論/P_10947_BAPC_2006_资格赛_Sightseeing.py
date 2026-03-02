"""
P10947 [BAPC 2006 资格赛] Sightseeing
https://www.luogu.com.cn/problem/P10947

需要維護最短路和第二短路，以及最短路和第二短路的數量。
最後判斷第二短路和最短路是否相差 1，如果是則需要加上第二短路的數量。
"""

from heapq import heappop, heappush


def solve():
    n, m = map(int, input().split())
    g = [[] for _ in range(n)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        u, v = u - 1, v - 1
        g[u].append((v, w))
    st, ed = map(lambda x: int(x) - 1, input().split())

    dist = [[float("inf")] * 2 for _ in range(n)]
    cnt = [[0] * 2 for _ in range(n)]

    dist[st][0] = 0
    cnt[st][0] = 1
    hp = [(0, st, 0)]
    while hp:
        d, u, k = heappop(hp)
        if d > dist[u][k]:
            continue
        for v, w in g[u]:
            nd = d + w
            if nd < dist[v][0]:
                dist[v][0], dist[v][1] = nd, dist[v][0]
                cnt[v][0], cnt[v][1] = cnt[u][k], cnt[v][0]
                heappush(hp, (nd, v, 0))
                heappush(hp, (dist[v][1], v, 1))  # 注意第二短路也要重新入堆
            elif nd == dist[v][0]:
                cnt[v][0] += cnt[u][k]
            elif nd < dist[v][1]:
                dist[v][1] = nd
                cnt[v][1] = cnt[u][k]
                heappush(hp, (nd, v, 1))
            elif nd == dist[v][1]:
                cnt[v][1] += cnt[u][k]

    print(cnt[ed][0] + (dist[ed][1] == dist[ed][0] + 1) * cnt[ed][1])


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()
