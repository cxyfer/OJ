import math
from math import *
from typing import *
from collections import *
from functools import lru_cache
import heapq
from heapq import *
from bisect import *
from itertools import *

class Solution:
    """
        Floyd-Warshall
    """
    def numberOfSets(self, n: int, maxDistance: int, roads: List[List[int]]) -> int:
        ans = 0
        for mask in range(1 << n):
            g = [[float('inf')] * n for _ in range(n)]

            for i in range(n):
                g[i][i] = 0

            for u, v, w in roads:
                if(mask >> u) & 1 and (mask >> v) & 1 and w <= maxDistance:
                    g[u][v] = min(g[u][v], w)
                    g[v][u] = min(g[v][u], w)

            for k in range(n):
                for i in range(n):
                    for j in range(n):
                        if g[i][k] + g[k][j] < g[i][j]:
                            g[i][j] = g[i][k] + g[k][j]
            flag = True
            for i in range(n):
                if not (mask >> i) & 1:
                    continue
                for j in range(n):
                    if not (mask >> j) & 1:
                        continue
                    if g[i][j] > maxDistance:
                        flag = False
                        break
            if flag:
                ans += 1
        return ans


sol = Solution()
print(sol.numberOfSets(3, 5, [[0,1,2],[1,2,10],[0,2,10]])) # 5
print(sol.numberOfSets(3, 5, [[0,1,20],[0,1,10],[1,2,2],[0,2,2]])) # 7
print(sol.numberOfSets(1, 10, [])) # 2
print(sol.numberOfSets(3, 19, [[1,0,7],[0,2,18]])) # 6