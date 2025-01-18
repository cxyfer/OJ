import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *

class Solution:
    def maxEnergyBoost(self, energyDrinkA: List[int], energyDrinkB: List[int]) -> int:
        n = len(energyDrinkA)

        @cache
        def dfs(i, state):
            if i >= n:
                return 0
            res1 = dfs(i + 1, state) + (energyDrinkA[i] if state == 0 else energyDrinkB[i])
            res2 = dfs(i + 2, state ^ 1) + (energyDrinkA[i] if state == 0 else energyDrinkB[i])
            return max(res1, res2)
        
        return max(dfs(0, 0), dfs(0, 1))

sol = Solution()
print(sol.maxEnergyBoost([1,3,1], [3,1,1])) # 5
print(sol.maxEnergyBoost([3,3,3], [3,4,6])) # 13