import math
from typing import *
from collections import *
from functools import lru_cache, cache
from heapq import *
from bisect import *
from itertools import *

class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        n = len(nums)
        @cache
        def dfs(target, i, j):
            if i >= j: # 區間內的數字小於2個
                return 0
            res = 0
            if nums[i] + nums[i+1] == target:
                res = max(res, 1 + dfs(target, i+2, j))
            if nums[j-1] + nums[j] == target:
                res = max(res, 1 + dfs(target, i, j-2))
            if nums[i] + nums[j] == target:
                res = max(res, 1 + dfs(target, i+1, j-1))
            return res
        res1 = dfs(nums[0]+nums[1], 2, n-1)
        res2 = dfs(nums[-2]+nums[-1], 0, n-3)
        res3 = dfs(nums[0]+nums[-1], 1, n-2)
        ans = 1 + max(res1, res2, res3)
        return ans

sol = Solution()
print(sol.maxOperations([3,2,1,2,3,4])) # 3
print(sol.maxOperations([3,2,6,1,4])) # 2
print(sol.maxOperations([3,3,7,3,2,4,2,3])) # 2