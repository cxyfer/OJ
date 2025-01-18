import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *

class Solution:
    def findMinimumTime(self, strength: list[int], K: int) -> int:
        n = len(strength)
        u = (1 << n) - 1
        @cache
        def dfs(s):
            if s == u:
                return 0
            X = 1 + s.bit_count() * K
            res = float('inf')
            for i in range(n):
                if s & (1 << i):
                    continue
                res = min(res, math.ceil(strength[i] / X) + dfs(s | (1 << i)))
            return res
        return dfs(0)

sol = Solution()
print(sol.findMinimumTime(strength = [3,4,1], K = 1)) # 4
print(sol.findMinimumTime(strength = [2,5,4], K = 2)) # 5
