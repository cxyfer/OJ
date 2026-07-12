from bisect import *
from collections import *
from functools import *
from heapq import *
from itertools import *
from math import *
from operator import *
from random import *
from string import *
from typing import *

"""
### Q4. DP: LIS

> 感覺這題不該被評為 Hard

令 f[i] 表示以第 i 個 column 結尾的最大 consistent columns 的長度，則有遞迴式：
f[i] = max(f[j] + 1) for all j < i if i and j are consistent columns.
"""


class Solution:
    def maxConsistentColumns(self, grid: List[List[int]], limit: int) -> int:
        m, n = len(grid), len(grid[0])

        f = [[all(abs(grid[k][i] - grid[k][j]) <= limit for k in range(m)) for j in range(n)] for i in range(n)]

        @cache
        def dfs(i: int) -> int:
            res = 1
            for j in range(i):
                if f[i][j]:
                    res = max(res, dfs(j) + 1)
            return res

        return max(dfs(i) for i in range(n))


sol = Solution()
print(sol.maxConsistentColumns([[-2, 0, 3]], 2))  # 2
print(sol.maxConsistentColumns([[1, -1, 1], [2, 2, 2]], 1))  # 2
print(sol.maxConsistentColumns([[-5, 5]], 9))  # 1
