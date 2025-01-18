import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *

DEBUG = False

class Solution:
    def minimumSum(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        points = []
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if cell:
                    points.append((i, j))
        points.sort()


        

[[1,0,1],[1,1,1]]
[[1,0,1,0],[0,1,0,1]]

sol = Solution()
print(sol.minimumSum([[1,0,1],[1,1,1]])) # 5
print(sol.minimumSum([[1,0,1,0],[0,1,0,1]])) # 5