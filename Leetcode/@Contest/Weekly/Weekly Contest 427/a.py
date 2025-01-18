import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *

class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        for i, x in enumerate(nums):
            if x > 0:
                idx = (i + x) % n
                ans[i] = nums[idx]
            elif x < 0:
                idx = (i + n - abs(x)) % n
                ans[i] = nums[idx]
            else:
                ans[i] = 0
        return ans
    
sol = Solution()
print(sol.constructTransformedArray([3,-2,1,1])) # [1,1,1,3]
print(sol.constructTransformedArray([-1,4,-1])) # [-1,-1,4]
