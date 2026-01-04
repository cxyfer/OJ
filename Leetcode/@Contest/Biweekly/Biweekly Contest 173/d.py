import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *

"""
包含但不限於：
- 忘記取模
- 把歐幾里得距離看成曼哈頓距離
- 認為 750^3 是可以過的
"""

MOD = int(1e9 + 7)

max = lambda a, b : a if a > b else b
min = lambda a, b : a if a < b else b

class Solution:
    def numberOfRoutes(self, grid: List[str], d: int) -> int:
        n, m = len(grid), len(grid[0])
        d2 = math.isqrt(d * d - 1)
        
        f = [[0] * 2 for _ in range(m)]
        for j in range(m):
            if grid[n - 1][j] == '.':
                f[j][0] = 1
        
        s = list(accumulate([f[j][0] for j in range(m)], func=lambda x, y: (x + y) % MOD, initial=0))
        for j in range(m):
            if grid[n-1][j] == '.':
                f[j][1] = (s[min(m - 1, j + d)+1] - s[max(0, j - d)] - f[j][0]) % MOD
   
        for r in range(n - 2, -1, -1):
            nf = [[0] * 2 for _ in range(m)]

            s = list(accumulate([f[j][0] + f[j][1] for j in range(m)], func=lambda x, y: (x + y) % MOD, initial=0))
            for j in range(m):
                if grid[r][j] == '.':
                    nf[j][0] = (s[min(m - 1, j + d2) + 1] - s[max(0, j - d2)]) % MOD

            s = list(accumulate([nf[j][0] for j in range(m)], func=lambda x, y: (x + y) % MOD, initial=0))
            for j in range(m):
                if grid[r][j] == '.':
                    nf[j][1] = (s[min(m - 1, j + d) + 1] - s[max(0, j - d)] - nf[j][0]) % MOD
            
            f = nf

        return sum(f[j][0] + f[j][1] for j in range(m)) % MOD


sol = Solution()
print(sol.numberOfRoutes(["..","#."], 1))  # 2
print(sol.numberOfRoutes(["..","#."], 2))  # 4
print(sol.numberOfRoutes([".#"], 1))  # 1

with open("d.txt", "r") as f:
    grid = f.readlines()
    print(sol.numberOfRoutes(grid, 60))