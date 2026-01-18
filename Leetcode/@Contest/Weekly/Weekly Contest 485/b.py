import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *

class Solution:
    def maxCapacity(self, costs: List[int], capacity: List[int], budget: int) -> int:
        arr = [(cost, cap) for cost, cap in zip(costs, capacity) if cost < budget]
        arr.sort()
        pre_mx = list(accumulate(arr, func=lambda mx, p: max(mx, p[1]), initial=0))
        ans = 0
        for i, (cost, cap) in enumerate(arr):
            j = bisect_left(range(i), budget - cost, key=lambda j: arr[j][0])
            # (j - 1) + 1 == j
            ans = max(ans, cap + pre_mx[j])
        return ans

sol = Solution()
print(sol.maxCapacity([4,8,5,3], [1,5,2,7], 8))  # 8
print(sol.maxCapacity([3,5,7,4], [2,4,3,6], 7))  # 6