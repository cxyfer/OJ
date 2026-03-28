import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *

"""
## Q3: 值域DP
注意到值域只有 2^10，而 XOR 的結果不會超出值域範圍。
因此只要記錄到達每個位置時的所有可能 XOR 值 即可。
時空複雜度均為 O(nmV)，但用滾動的方式應該可以把空間複雜度優化到 O(mV)。
"""

class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        n, m = len(grid), len(grid[0])

        @cache
        def dfs(i: int, j: int) -> set:
            x = grid[i][j]
            if i == 0 and j == 0:
                return set([x])
            res = set()
            if i > 0:
                for y in dfs(i - 1, j):
                    res.add(x ^ y)
            if j > 0:
                for y in dfs(i, j - 1):
                    res.add(x ^ y)
            return res

        return min(dfs(n - 1, m - 1))