import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *

class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])

        @cache
        def dfs(i: int, j: int, c: int) -> int:
            if i < 0 or i >= m or j < 0 or j >= n:
                return float("-inf")
            c += (grid[i][j] > 0)
            if c > k:
                return float("-inf")
            if i == m - 1 and j == n - 1:
                return grid[i][j]
            return grid[i][j] + max(dfs(i + 1, j, c), dfs(i, j + 1, c))

        return max(dfs(0, 0, 0), -1)


sol = Solution()
print(sol.maxPathScore([[0, 1], [2, 0]], 1))  # 2
print(sol.maxPathScore([[0, 1],[1, 2]], 1))  # -1
