import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *

class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        return min(need1 * cost1 + need2 * cost2, 
               min(need1, need2) * costBoth + (need1 - min(need1, need2)) * cost1 + (need2 - min(need1, need2)) * cost2,
               max(need1, need2) * costBoth)

sol = Solution()
print(sol.minimumCost(3, 2, 1, 3, 2))  # 3