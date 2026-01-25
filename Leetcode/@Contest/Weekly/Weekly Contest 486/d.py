import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *

class Solution:
    def nthSmallest(self, n: int, k: int) -> int:
        ans = 0
        for b in range(60, -1, -1):
            cnt = math.comb(b, k)
            if cnt < n:
                ans |= (1 << b)
                n -= cnt
                k -= 1
                if k == 0:
                    break
        return ans
    
sol = Solution()
print(sol.nthSmallest(4, 2))  # 9
print(sol.nthSmallest(3, 1))  # 4