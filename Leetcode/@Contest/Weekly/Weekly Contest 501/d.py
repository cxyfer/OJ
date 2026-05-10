import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *

"""
Q4: ||最短路||
本題簡化版: https://www.luogu.com.cn/problem/P1629

本題其實是在求在從 u 出發到其他點的最短路 + 從其他點到 u 的最短路，只是兩次最短路要取不同邊權。
而對於雙向圖而言，從 u 到 v 的最短距離，等於從 v 到 u 的最短距離。
因此兩個距離都能以從 u 開始的最短路表示。

枚舉每個點 u，對兩個圖分別做 dijkstra，根據結果求解即可。
O(n (n + m) log m)
"""

class Solution:
    def minCost(self, n: int, prices: List[int], roads: List[List[int]]) -> List[int]:
        max_prices = max(prices)

        g1 = [[] for _ in range(n)]
        g2 = [[] for _ in range(n)]
        for u, v, c, t in roads:
            if c < max_prices:
                g1[u].append((v, c))
                g1[v].append((u, c))
            if c * t < max_prices:
                g2[u].append((v, c * t))
                g2[v].append((u, c * t))

        def dijkstra(st: int, g: list[list[tuple[int, int]]], price: int) -> list[int]:
            dist = [price] * n
            dist[st] = 0

            hp = [(0, st)]
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
        
        ans = []
        for u in range(n):
            dist1 = dijkstra(u, g1, prices[u])
            dist2 = dijkstra(u, g2, prices[u])
            ans.append(min(prices[v] + dist1[v] + dist2[v] for v in range(n)))
        return ans

sol = Solution()
print(sol.minCost(2, [8,3], [[0,1,1,2]]))  # [6,3]
        