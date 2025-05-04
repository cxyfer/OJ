import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *

class Solution:
    def minTravelTime(self, l: int, n: int, k: int, position: List[int], time: List[int]) -> int:
        s = list(accumulate(time))
        @cache
        def f(i, j, pre):
            if i == n - 1:
                return 0 if j == 0 else float('inf')
            if j == 0:
                return float('inf')
            res = float('inf')
            for k in range(i + 1, n):
                res = min(res, f(k, j - 1, s[k] - s[i]) + (position[k] - position[i]) * pre)
            return res
        return f(0, n - k - 1, time[0])

sol = Solution()
print(sol.minTravelTime(10, 4, 1, [0,3,8,10], [5,8,3,6]))  # 62
