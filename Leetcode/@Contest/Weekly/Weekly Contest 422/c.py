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
        
        dp = [[[float('inf')] * 2 for _ in range(m)] for _ in range(n)]
        dp[0][0][0] = 0
        hp = [(0, 0, 0, 0)] # (time, x, y, z)
        
        while hp:
            t, x, y, z = heappop(hp)
            if x == n - 1 and y == m - 1:
                return t
            if t > dp[x][y][z]:
                continue
            for dx, dy in DIR:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m:
                    nt = max(t, moveTime[nx][ny]) + (1 if z == 0 else 2)
                    nz = 1 - z
                    if nt < dp[nx][ny][nz]:
                        dp[nx][ny][nz] = nt
                        heappush(hp, (nt, nx, ny, nz))
        return -1


sol = Solution()
print(sol.minTimeToReach([[0,4],[4,4]])) # 7
print(sol.minTimeToReach([[0,0,0,0],[0,0,0,0]])) # 6
print(sol.minTimeToReach([[0,1],[1,2]])) # 4
