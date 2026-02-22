"""
U262078 昂贵的聘礼
https://www.luogu.com.cn/problem/U262078

先忽略等級限制，則可以將每個物品視為圖上的節點，物品之間的替代關係視為邊。
則直接購買物品 v ，相當於從虛擬源點 s 到目標節點 v 的一條邊，邊權為價格 P[v]。
如果擁有物品 u，可以用價格 w 購買物品 v，則相當於 (u, v, w) 的一條邊。

接著考慮等級限制，我們可以枚舉在等級限制範圍內的物品，將其視為一個子圖，然後在子圖上跑最短路。
由於等級的值範圍是 [1, n]，因此枚舉子圖的時間複雜度是 O(n^2)。
每個子圖需要跑 O(nlogn) 的最短路，因此總時間複雜度是 O(n^3logn)。
"""

from heapq import heappop, heappush


def solve():
    k, n = map(int, input().split())

    P, L = [], []
    alts = []
    for _ in range(n):
        p, l, x = map(int, input().split())
        P.append(p)
        L.append(l)
        alt = []
        for _ in range(x):
            t, v = map(int, input().split())
            alt.append((t - 1, v))
        alts.append(alt)

    ans = float("inf")
    s = n  # 虛擬源點

    for l in range(1, n + 1):
        for r in range(l, min(n, l + k) + 1):
            st = set(u for u in range(n) if l <= L[u] <= r)
            if 0 not in st:
                continue

            g = [[] for _ in range(n + 1)]
            for u in st:
                g[s].append((u, P[u]))
                for t, w in alts[u]:
                    if t in st:
                        g[t].append((u, w))

            dist = [float("inf")] * (n + 1)
            dist[s] = 0
            hp = [(0, s)]
            while hp:
                d, u = heappop(hp)
                if d > dist[u]:
                    continue
                for v, w in g[u]:
                    nd = d + w
                    if nd < dist[v]:
                        dist[v] = nd
                        heappush(hp, (nd, v))

            ans = min(ans, dist[0])

    print(ans)


if __name__ == "__main__":
    solve()
