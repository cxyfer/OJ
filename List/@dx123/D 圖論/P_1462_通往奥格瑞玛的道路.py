"""
P1462 通往奥格瑞玛的道路
https://www.luogu.com.cn/problem/P1462

從最小化最大值可以聯想到二分。
而二分函數需要判斷是否存在一條路徑的距離 <= b，且途經節點的 cost[u] 皆 <= mid。
這相當於在子圖上跑最短路，且子圖的節點的 cost[u] 皆 <= mid。
"""

from heapq import heappush, heappop


def solve():
    n, m, b = map(int, input().split())
    cost = [int(input()) for _ in range(n)]
    g = [[] for _ in range(n)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        u, v = u - 1, v - 1
        g[u].append((v, w))
        g[v].append((u, w))

    def check(mid):
        if cost[0] > mid:  # 注意起點的 cost 也要 <= mid
            return False
        dist = [float("inf")] * n
        dist[0] = 0
        hp = [(0, 0)]
        while hp:
            d, u = heappop(hp)
            if d > dist[u]:
                continue
            for v, w in g[u]:
                if cost[v] > mid:
                    continue
                nd = d + w
                if nd < dist[v]:
                    dist[v] = nd
                    heappush(hp, (nd, v))
        return dist[n - 1] <= b

    left, right = min(cost), max(cost)
    while left <= right:
        mid = (left + right) // 2
        if check(mid):
            right = mid - 1
        else:
            left = mid + 1
    print(left if left <= max(cost) else "AFK")


if __name__ == "__main__":
    solve()
