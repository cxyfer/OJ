import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n, m = len(moveTime), len(moveTime[0])
        DIR = [(-1,0), (1,0), (0,-1), (0,1)]
        dist = [[float('inf') for _ in range(m)] for _ in range(n)]
        dist[0][0] = 0
        
        hp = [(0, 0, 0)] # (time, x, y)
        while hp:
            t, x, y = heappop(hp)
            if x == n - 1 and y == m - 1:
                return t
            if t > dist[x][y]:
                continue
            for dx, dy in DIR:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m:
                    nt = max(t, moveTime[nx][ny]) + 1
                    if nt < dist[nx][ny]:
                        dist[nx][ny] = nt
                        heappush(hp, (nt, nx, ny))
        return -1

sol = Solution()
print(sol.minTimeToReach([[0,4],[4,4]]))  # 6
print(sol.minTimeToReach([[0,0,0],[0,0,0]]))  # 3
print(sol.minTimeToReach([[0,1],[1,2]]))  # 3