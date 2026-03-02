"""
P1629 邮递员送信
https://www.luogu.com.cn/problem/P1629

在到達每個節點後，都需要返回起點一次。
因此需要求從起點到每個點的最短路，以及從每個點到起點的最短路。
對於第二種情況，只需要求出反圖的最短路即可。
"""

from heapq import heappop, heappush


def solve():
    n, m = map(int, input().split())
    g = [[] for _ in range(n)]
    rg = [[] for _ in range(n)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        u, v = u - 1, v - 1
        g[u].append((v, w))
        rg[v].append((u, w))

    def dijkstra(g):
        dist = [float("inf")] * n
        dist[0] = 0
        hp = [(0, 0)]
        while hp:
            d, u = heappop(hp)
            if d > dist[u]:
                continue
            for v, w in g[u]:
                nd = d + w
                if nd < dist[v]:
                    dist[v] = nd
                    heappush(hp, (nd, v))
        return dist

    dist1 = dijkstra(g)
    dist2 = dijkstra(rg)
    print(sum(dist1) + sum(dist2))


if __name__ == "__main__":
    solve()
