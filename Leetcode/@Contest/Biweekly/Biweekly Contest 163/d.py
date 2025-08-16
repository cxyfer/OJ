import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
import heapq
from collections import defaultdict

class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        n, m = len(grid), len(grid[0])
        
        mp = defaultdict(list)
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                mp[x].append((i, j))
        mn = min(mp.keys())
        f = [defaultdict(lambda: float('inf')) for _ in range(k + 1)]

        g = [[[] for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if i + 1 < n:
                    g[i][j].append(((i + 1, j), grid[i + 1][j]))
                if j + 1 < m:
                    g[i][j].append(((i, j + 1), grid[i][j + 1]))

        dist = [[[float('inf')] * (k + 1) for _ in range(m)] for _ in range(n)]
        hp = [(0, (0, 0), 0)]
        dist[0][0][0] = 0
        while hp:
            d, (x, y), t = heappop(hp)
            if d > dist[x][y][t]:
                continue
            if (x, y) == (n - 1, m - 1):
                return d
            for (nx, ny), w in g[x][y]:
                nd = d + w
                if nd < dist[nx][ny][t]:
                    dist[nx][ny][t] = nd
                    heappush(hp, (nd, (nx, ny), t))

            if t < k:
                for v in range(grid[x][y], mn - 1, -1):
                    if d >= f[t + 1][v]:
                        break
                    f[t + 1][v] = d
                    for nx, ny in mp[v]:
                        if d < dist[nx][ny][t + 1]:
                            dist[nx][ny][t + 1] = d
                            heappush(hp, (d, (nx, ny), t + 1))
        return -1

sol = Solution()
print(sol.minCost([[1,3,3],[2,5,4],[4,3,5]], 2))  # 7
print(sol.minCost([[19,10],[23,13],[16,32],[38,41],[30,36],[53,31]], 1))  # 55