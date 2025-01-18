import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *

"""
    https://atcoder.jp/contests/abc347/tasks/abc347_f
"""

class Solution:
    def minimumSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        @cache
        def calc(x1, x2, y1, y2): # 區域內的最小矩形面積
            l, r, u, d = 1e9, -1e9, 1e9, -1e9
            for i in range(x1, x2 + 1):
                for j in range(y1, y2 + 1):
                    if grid[i][j]:
                        l = min(l, j)
                        r = max(r, j)
                        u = min(u, i)
                        d = max(d, i)
            return (r - l + 1) * (d - u + 1)

        ans = 1e18

        # 三橫，枚舉兩個分界線
        for i1 in range(m - 2):
            for i2 in range(i1 + 1, m - 1):
                ans = min(ans, calc(0, i1, 0, n - 1) + calc(i1 + 1, i2, 0, n - 1) + calc(i2 + 1, m - 1, 0, n - 1))
        # 三直，枚舉兩個分界線
        for j1 in range(n - 2):
            for j2 in range(j1 + 1, n - 1):
                ans = min(ans, calc(0, m - 1, 0, j1) + calc(0, m - 1, j1 + 1, j2) + calc(0, m - 1, j2 + 1, n - 1))
        # 用一直一橫兩條分界線，分成四個區域，再將其中兩個組合，變成三個區域
        for i in range(m - 1):
            for j in range(n - 1):
                # 上一橫下二直
                ans = min(ans, calc(0, i, 0, n - 1) + calc(i + 1, m - 1, 0, j) + calc(i + 1, m - 1, j + 1, n - 1))
                # 上二直下一橫
                ans = min(ans, calc(0, i, 0, j) + calc(0, i, j + 1, n - 1) + calc(i + 1, m - 1, 0, n - 1))
                # 左一直右二橫
                ans = min(ans, calc(0, m - 1, 0, j) + calc(0, i, j + 1, n - 1) + calc(i + 1, m - 1, j + 1, n - 1))
                # 左二橫右一直
                ans = min(ans, calc(0, i, 0, j) + calc(i + 1, m - 1, 0, j) + calc(0, m - 1, j + 1, n - 1))
        return ans