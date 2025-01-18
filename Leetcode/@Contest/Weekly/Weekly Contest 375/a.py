import math
from math import *
from typing import *
from collections import *
from functools import lru_cache
import heapq
from heapq import *
from bisect import *
from itertools import *

class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        ans = 0
        for i, x in enumerate(batteryPercentages):
            if x - ans > 0:
                ans += 1
        return ans

sol = Solution()
print(sol.countTestedDevices([1,1,2,1,3])) # 3
print(sol.countTestedDevices([0,1,2])) # 2