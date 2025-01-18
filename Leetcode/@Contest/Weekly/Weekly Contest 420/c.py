import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *

MAX = int(1e6) + 5
lpd = [1] * (MAX + 1)  # largest proper divisor
for i in range(2, MAX // 2 + 1):
    for j in range(2 * i, MAX + 1, i):
        if i > lpd[j]:
            lpd[j] = i

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        def helper(x):
            values = [x]
            while True:
                pd = lpd[x] # proper divisor
                if pd <= 1:
                    break
                x = x // pd
                values.append(x)
            return values[::-1]
        last = float('inf')
        ans = 0
        for x in reversed(nums):
            values = helper(x)
            idx = bisect_right(values, last) - 1
            if idx < 0:
                return -1
            x = values[idx]
            cur = values[::-1].index(x)
            last = x
            ans += cur
        return ans

sol = Solution()
print(sol.minOperations([25,7])) # 1
print(sol.minOperations([7,7,6])) # -1
print(sol.minOperations([1,1,1,1])) # 0
