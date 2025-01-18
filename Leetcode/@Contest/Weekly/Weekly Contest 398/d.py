import math
from typing import *
from collections import *
from functools import lru_cache, cache
from heapq import *
from bisect import *
from itertools import *

class Solution:
    """
        Start at stair 1, then 
        若當前 x > k+1，則永遠無法走到
    """
    def waysToReachStair(self, k: int) -> int:
        @cache
        def f(x, pre, can_down):
            if x < 0: return 0
            if x > k + 1: return 0 # 無法走到
            res = 1 if x == k else 0
            if can_down:
                res += f(x-1, pre, False) # 下1
            res += f(x + 2**pre, pre+1, True)
            return res
        return f(1, 0, True)

sol = Solution()
print(sol.waysToReachStair(0)) # 2
print(sol.waysToReachStair(1)) # 4