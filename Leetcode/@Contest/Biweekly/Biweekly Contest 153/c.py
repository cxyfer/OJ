import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *

class Solution:
    def minimumCost(self, nums: List[int], cost: List[int], k: int) -> int:
        n = len(nums)

        s1 = list(accumulate(nums, initial=0))
        s2 = list(accumulate(cost, initial=0))

        @cache
        def dfs(i: int) -> int:
            if i == n:
                return 0
            res = float('inf')
            for j in range(i, n):
                # res = min(res, dfs(x + 1, j + 1) + (s1[x + 1] + c * j) * (s2[x + 1] - s2[i]))
                res = min(res, dfs(j + 1) + s1[j + 1] * (s2[j + 1] - s2[i]) + k * (s2[n] - s2[i]))
            return res
        return dfs(0)
    
sol = Solution()
print(sol.minimumCost([3,1,4], [4,6,6], 1))  # 110
print(sol.minimumCost([4,8,5,1,14,2,2,12,1], [7,2,8,4,2,2,1,1,2], 7))  # 985