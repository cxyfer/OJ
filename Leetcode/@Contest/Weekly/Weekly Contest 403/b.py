import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *

class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        u, d, l, r = 1e9, -1e9, 1e9, -1e9
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if cell:
                    u = min(u, i)
                    d = max(d, i)
                    l = min(l, j)
                    r = max(r, j)
        return (d - u + 1) * (r - l + 1)