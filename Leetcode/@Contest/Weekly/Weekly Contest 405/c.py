import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *

class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        preX = [[0] * (m + 1) for _ in range(n + 1)]
        preY = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(n):
            for j in range(m):
                preX[i + 1][j + 1] = preX[i + 1][j] + preX[i][j + 1] - preX[i][j] + (grid[i][j] == "X")
                preY[i + 1][j + 1] = preY[i + 1][j] + preY[i][j + 1] - preY[i][j] + (grid[i][j] == "Y")
        ans = 0
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if preX[i][j] == 0:
                    continue
                if preX[i][j] == preY[i][j]:
                    # print(i, j, preX[i][j], preY[i][j])
                    ans += 1
        return ans

sol = Solution()
print(sol.numberOfSubmatrices([["X","Y","."],["Y",".","."]])) # 3
print(sol.numberOfSubmatrices([["X","X"],["X","Y"]])) # 0
print(sol.numberOfSubmatrices([[".","."],[".","."]])) # 0