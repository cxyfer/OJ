import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *

class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        g = [[] for _ in range(n)]
        for (u, v, w) in edges:
            g[u].append((v, w))
            g[v].append((u, w << 1))
        hp = [(0, 0)]
        dist = [float("inf")] * n
        dist[0] = 0
        while hp:
            d, u = heappop(hp)
            if d > dist[u]:
                continue
            if u == n - 1:
                return d
            for v, w in g[u]:
                nd = d + w
                if nd < dist[v]:
                    dist[v] = nd
                    heappush(hp, (nd, v))
        return -1

sol = Solution()
print(sol.minCost(4, [[0,1,3],[3,1,1],[2,3,4],[0,2,2]]))  # 5
print(sol.minCost(4, [[0,2,1],[2,1,1],[1,3,1],[2,3,3]]))  # 3