import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *

class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        n = len(nums)
        nums.sort()
        ans = float("inf")
        for i in range(n//2):
            ans = min(ans, (nums[i] + nums[n - 1 - i]) / 2)
        return ans

[7,8,3,4,15,13,4,1]
[1,9,8,3,10,5]
[1,2,3,7,8,9]
sol = Solution()
print(sol.minimumAverage([7,8,3,4,15,13,4,1])) # 5.5
print(sol.minimumAverage([1,9,8,3,10,5])) # 5.5
print(sol.minimumAverage([1,2,3,7,8,9])) # 5.0