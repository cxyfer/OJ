import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *

"""
"""
class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        n = len(nums)
        res1 = sum(1 for x in nums if x & 1)
        res2 = sum(1 for x in nums if x & 1 == 0)

        dp = [[0, 0] for _ in range(n + 1)]
        for i, x in enumerate(nums, 1):
            if x & 1:
                dp[i][0] = dp[i - 1][0]
                dp[i][1] = dp[i - 1][0] + 1
            else:
                dp[i][0] = dp[i - 1][1] + 1
                dp[i][1] = dp[i - 1][1]
        return max(res1, res2, dp[-1][0], dp[-1][1])

sol = Solution()
print(sol.maximumLength([1,2,3,4])) # 4
print(sol.maximumLength([1,2,1,1,2,1,2])) # 6
print(sol.maximumLength([1,3])) # 2