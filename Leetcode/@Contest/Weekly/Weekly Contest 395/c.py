import math
from typing import *
from collections import *
from functools import lru_cache, cache
from heapq import *
from bisect import *
from itertools import *

class Solution:
    def minEnd(self, n: int, x: int) -> int:
        n -= 1
        ans = x
        i = j = 0
        while n:
            if not x & (1 << i):
                if n & (1 << j):
                    ans |= (1 << i)
                    n -= (1 << j)
                j += 1
            i += 1
        return ans

    

sol = Solution()
print(sol.minEnd(3, 4)) # 6
print(sol.minEnd(2, 7)) # 15
print(bin(15)[2:].zfill(16))