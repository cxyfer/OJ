import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *

from typing import List

class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        ans = 0
        m, n = len(grid), len(grid[0])

        for j in range(n):
            prev = -1
            for i in range(m):
                if grid[i][j] > prev:
                    prev = grid[i][j]
                else:
                    ans += (prev + 1) - grid[i][j]
                    prev = prev + 1
        return ans
