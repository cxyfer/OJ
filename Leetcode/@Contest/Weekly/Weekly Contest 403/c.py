import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *

class Solution:
    def maximumTotalCost(self, nums: List[int]) -> int:
        n = len(nums)
        s1, s2 = [0] * (n + 1), [0] * (n + 1)
        for i, x in enumerate(nums):
            s1[i + 1] = s1[i] + x * (1 if 1 & i else -1)
            s2[i + 1] = s2[i] + x * (-1 if 1 & i else 1)

        def cost(i: int, j: int) -> int:
            return s1[j+1] - s1[i] if i & 1 else s2[j+1] - s2[i]
        
        # @cache
        # def dfs(i):
        #     if i == n:
        #         return 0
        #     return max(cost(i, j) + dfs(j + 1) for j in range(i, n))
        # return dfs(0)

        dp = [-float("inf")] * (n + 1)
        dp[n] = 0
        mx = [(0, -1) for i in range(n + 1)]
        mx[n] = (0, n-1)
        for i in range(n - 1, -1, -1):
            f, j = mx[i + 1]
            dp[i] = cost(i, j) + dp[j + 1]
            if f < dp[i]:
                mx[i] = (dp[i], i-1)
            else:
                mx[i] = mx[i + 1]

        return dp[0]
    


sol = Solution()
print(sol.maximumTotalCost([1,-2,3,4])) # 10
print(sol.maximumTotalCost([1,-1,1,-1])) # 4
print(sol.maximumTotalCost([0])) # 0
print(sol.maximumTotalCost([1,-1])) #2
print(sol.maximumTotalCost([-937])) # -937