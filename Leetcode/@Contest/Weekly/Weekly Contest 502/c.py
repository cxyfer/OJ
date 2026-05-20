import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *

"""
Q3: ||Sparse Table||
||對於每個 row 維護一個 Sparse Table，那麼每個元素只需要查 O(n) 個 ST 表的區間最大值，注意邊界需要縮減一個元素||
||O(n^2m)||
"""

class SparseTable:
    def __init__(self, data, merge_func):
        n = len(data)
        self.data = data
        self.merge = merge_func
        k = n.bit_length() - 1
        self.st = [[None] * (k + 1) for _ in range(n)]
        for i in range(n):
            self.st[i][0] = data[i]
        
        for j in range(1, k + 1):
            for i in range(n):
                self.st[i][j] = self.merge(self.st[i][j - 1], self.st[min(n - 1, i + (1 << (j - 1)))][j - 1])
    
    def query(self, L, R):  # 0-indexed
        k = (R - L + 1).bit_length() - 1
        return self.merge(self.st[L][k], self.st[R - (1 << k) + 1][k])

class Solution:
    def countLocalMaximums(self, matrix: list[list[int]]) -> int:
        n, m = len(matrix), len(matrix[0])
        sts = [SparseTable(row, max) for row in matrix]

        ans = 0
        for i, row in enumerate(matrix):
            for j, x in enumerate(row):
                for idx in range(max(i - x, 0), min(i + x, n - 1) + 1):
                    l = max(j - x + (abs(idx - i) == x), 0)
                    r = min(j + x - (abs(idx - i) == x), m)
                    if sts[idx].query(l, r) > x:
                        break
                else:
                    ans += 1
        return ans