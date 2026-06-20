import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *

"""
Q1: 構造
只要讓 (1, 1) => (m, 1) => (m, n) 或 (1, 1) => (1, n) => (m, n) 的路徑上都是 "." 就行了。
"""

class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        grid = [["#"] * n for _ in range(m)]
        for i in range(m):
            grid[i][0] = "."
        for j in range(n):
            grid[m - 1][j] = "."
        return ["".join(row) for row in grid]
