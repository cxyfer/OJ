import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *

class Solution:
    def countStableSubarrays(self, capacity: List[int]) -> int:
        ans = s = 0
        mp = defaultdict(int)
        for r, x in enumerate(capacity):
            s += x
            ans += mp[(s - x - x, x)]
            if r > 0:
                mp[(s - x, capacity[r - 1])] += 1
        return ans

sol = Solution()
print(sol.countStableSubarrays([9,3,3,3,9]))  # 2
print(sol.countStableSubarrays([1,2,3,4,5]))  # 0
print(sol.countStableSubarrays([-4,4,0,0,-8,-4]))  # 1
