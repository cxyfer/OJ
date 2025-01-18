import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *

class Solution:
    def maximumPoints(self, enemyEnergies: List[int], currentEnergy: int) -> int:
        n = len(enemyEnergies)
        ans = 0 # points
        enemyEnergies.sort()
        first = enemyEnergies[0]
        if currentEnergy < first:
            return 0
        i, j = 0, n - 1
        while i < j:
            if currentEnergy >= first:
                ans += currentEnergy // first
                currentEnergy %= first
            currentEnergy += enemyEnergies[j]
            j -= 1
        ans += currentEnergy // first
        return ans
   
sol = Solution()
print(sol.maximumPoints([3,2,2], 2)) # 3
print(sol.maximumPoints([2], 10)) # 5
print(sol.maximumPoints([1,2,3], 0)) # 0
