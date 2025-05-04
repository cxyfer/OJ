import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *

class Solution:
    def specialGrid(self, N: int) -> List[List[int]]:
        if N == 0:
            return [[0]]
        n, m = 2 ** N, 2 ** (N - 1)
        res = [[-1] * n for _ in range(n)]
        grid = self.specialGrid(N - 1)
        for i in range(n):
            for j in range(n):
                if i < m and j >= m:
                    res[i][j] = grid[i][j - m]
                elif i >= m and j >= m:
                    res[i][j] = grid[i - m][j - m] + m * m
                elif i >= m and j < m:
                    res[i][j] = grid[i - m][j] + 2 * m * m
                else:
                    res[i][j] = grid[i][j] + 3 * m * m
        return res

sol = Solution()
print(sol.specialGrid(2))
