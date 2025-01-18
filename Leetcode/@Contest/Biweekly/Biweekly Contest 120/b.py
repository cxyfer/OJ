import math
from typing import *
from collections import *
from functools import lru_cache, cache
from heapq import *
from bisect import *
from itertools import *

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        # pre = list(accumulate(nums, initial=0))
        s = sum(nums)
        for i in range(n - 1, 1, -1):
            # if pre[i] > nums[i]:
            #     return pre[i] + nums[i]
            if s  > 2 * nums[i]: # s - nums[i] > nums[i]
                return s
            s -= nums[i]
        return -1

sol = Solution()
print(sol.largestPerimeter([5,5,5])) # 15
print(sol.largestPerimeter([1,12,1,2,5,50,3])) # 12
print(sol.largestPerimeter([5,5,50])) # -1