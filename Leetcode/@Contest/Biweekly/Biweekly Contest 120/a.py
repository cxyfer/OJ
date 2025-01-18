import math
from typing import *
from collections import *
from functools import lru_cache, cache
from heapq import *
from bisect import *
from itertools import *

class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        def check(i, j):
            cur = nums[:i] + nums[j + 1:]
            nn = len(cur)
            for k in range(nn - 1):
                if cur[k] >= cur[k + 1]:
                    return False
            return True
        n = len(nums)
        ans = 0
        for i in range(n):
            for j in range(i, n):
                if check(i, j):
                    ans += 1
        return ans

sol = Solution()
print(sol.incremovableSubarrayCount([1,2,3,4])) # 10
print(sol.incremovableSubarrayCount([6,5,7,8])) # 7
print(sol.incremovableSubarrayCount([8,7,6,6])) # 3