import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import xor

class Solution:
    def minDifference(self, n: int, k: int) -> List[int]:
        ans = []
        path = []
        def dfs(i, x, pre):
            if i == k - 1:
                ans.append(path + [x])
                return
            for y in range(pre, math.isqrt(x) + 1):
                if x % y == 0:
                    path.append(y)
                    dfs(i + 1, x // y, y)
                    path.pop()
        dfs(0, n, 1)
        return min(ans, key = lambda x : x[-1] - x[0])
            

sol = Solution()
print(sol.minDifference(100, 2))  # [10,10]
print(sol.minDifference(18, 5))  # [1,1,2,3,3]