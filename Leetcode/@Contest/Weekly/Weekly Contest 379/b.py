import math
from typing import *
from collections import *
from functools import lru_cache, cache
from heapq import *
from bisect import *
from itertools import *

class Solution:
    def minMovesToCaptureTheQueen(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:
        if a == e: # rook 和 queen 在同一行
            if a == c: # bishop 也在同一行且是障礙物
                if d in range(min(b,f), max(b,f)):
                    return 2
            return 1
        if b == f: # rook 和 queen 在同一列
            if b == d: # bishop 也在同一列且是障礙物
                if c in range(min(a,e), max(a,e)):
                    return 2
            return 1
        if c + d == e + f: # bishop 和 queen 在同一個左上到右下的斜線上
            if c + d == a + b: # rook 也在同一個左上到右下的斜線上且是障礙物
                if a in range(min(c,e), max(c,e)) or b in range(min(d,f), max(d,f)): 
                    return 2
            return 1
        if c - d == e - f: # bishop 和 queen 在同一個左下到右上的斜線上
            if c - d == a - b: # rook 也在同一個左下到右上的斜線上且是障礙物
                if a in range(min(c,e), max(c,e)) or b in range(min(d,f), max(d,f)):
                    return 2
            return 1
        return 2

sol = Solution()
print(sol.minMovesToCaptureTheQueen(4,3,3,4,5,2)) #2
print(sol.minMovesToCaptureTheQueen(1,6,3,3,5,6)) #1
print(sol.minMovesToCaptureTheQueen(1,1,1,4,1,8)) #2
print(sol.minMovesToCaptureTheQueen(8,5,2,4,5,7)) #1