import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *

from typing import List
import heapq
from math import inf

class Solution:
    def minTimeMaxPower(self, n: int, edges: List[List[int]], power: int, cost: List[int], source: int, target: int) -> List[int]:
        g = [[] for _ in range(n)]
        for u, v, w in edges:
            g[u].append((v, w))

        dist = [[inf] * (power + 1) for _ in range(n)]
        dist[source][0] = 0

        hp = [(0, 0, source)]
        while hp:
            d, e, u = heappop(hp)

            if u == target:
                return [d, power - e]

            ne = e + cost[u]
            if d > dist[u][e] or ne > power:
                continue

            for v, w in g[u]:
                nd = d + w
                if nd < dist[v][ne]:
                    dist[v][ne] = nd
                    heappush(hp, (nd, ne, v))

        return [-1, -1]

sol = Solution()
print(sol.minTimeMaxPower(5, [[0,1,1],[1,4,1],[0,2,1],[2,3,1],[3,4,1]], 4, [2,3,1,1,1], 0, 4))  # [3, 0]