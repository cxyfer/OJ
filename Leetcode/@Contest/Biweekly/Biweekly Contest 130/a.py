import math
from typing import *
from collections import *
from functools import lru_cache, cache
from heapq import *
from bisect import *
from itertools import *

class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        ans = True
        for i in range(m):
            for j in range(n):
                if i + 1 < m and grid[i][j] != grid[i+1][j]:
                    ans = False
                if j + 1 < n and grid[i][j] == grid[i][j+1]:
                    ans = False
        return ans