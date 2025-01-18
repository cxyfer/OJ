import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        n = len(nums)

        @cache
        def dfs(i, k):
            if k < 0:
                return 0
            if i == n - 1:
                return 1
            res = 0
            for j in range(i+1, n):
                if nums[j] != nums[i]:
                    res = max(res, 1 + dfs(j, k-1))
                else:
                    res = max(res, 1 + dfs(j, k))
            return res
        ans = 0
        for i in range(n):
            ans = max(ans, dfs(i, k))
        return ans
    
sol = Solution()
print(sol.maximumLength([1,2,1,1,3], 2)) # 4
print(sol.maximumLength([1,2,3,4,5,1], 0)) # 2
print(sol.maximumLength([59,60,59,60,60,60], 0)) # 4
print(sol.maximumLength([68,69,68,69,69,68,68], 1)) # 5
