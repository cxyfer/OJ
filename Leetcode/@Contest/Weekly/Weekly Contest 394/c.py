import math
from typing import *
from collections import *
from functools import lru_cache, cache
from heapq import *
from bisect import *
from itertools import *

class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        cols = [Counter() for _ in range(n)]
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                cols[j][x] += 1
        # print(cols)
        @cache
        def f(i, j): # 第 i col 的全部元素都變成 j
            cur = m - cols[i][j]
            if i == 0:
                return cur
            res = float('inf')
            for x in range(10):
                if x == j:
                    continue
                res = min(res, cur + f(i-1, x))
            return res

        ans = float('inf')
        for x in range(10):
            ans = min(ans, f(n-1, x))
        return ans

sol = Solution()
print(sol.minimumOperations([[1,0,2],[1,0,2]])) # 0