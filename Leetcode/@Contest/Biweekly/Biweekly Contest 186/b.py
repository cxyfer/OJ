import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *
from math import inf

"""
### Q2. 枚舉右維護左
枚舉 j，為使 nums[i] + nums[j] 最大，可以維護滿足 i <= j - k 的 nums[i] 的最大值。
"""

class Solution:
    def maxValidPairSum(self, nums: list[int], k: int) -> int:
        ans = mx = -inf
        for i, x in enumerate(nums):
            if i >= k:
                mx = max(mx, nums[i - k])
            ans = max(ans, x + mx)
        return ans


sol = Solution()
print(sol.maxValidPairSum([1, 3, 5, 2, 8], 2))  # 13
print(sol.maxValidPairSum([5, 1, 9], 1))  # 14