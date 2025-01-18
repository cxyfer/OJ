import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *

"""
Q3. DP

每個元素最多有 5 種可能：不操作、操作1、操作2、先操作1後操作2、先操作2後操作1。
根據這五種可能寫出狀態轉移方程，並且用記憶化搜索實現即可。
"""

class Solution:
    def minArraySum(self, nums: List[int], k: int, op1: int, op2: int) -> int:
        n = len(nums)

        @cache
        def f(i: int, cnt1: int, cnt2: int) -> int:
            if i == n:
                return 0

            x = nums[i] 

            res = x + f(i + 1, cnt1, cnt2) # 不操作
            if cnt1 < op1:
                res = min(res, math.ceil(x / 2) + f(i + 1, cnt1 + 1, cnt2)) # 操作1

            if cnt2 < op2 and x >= k:
                res = min(res, x - k + f(i + 1, cnt1, cnt2 + 1)) # 操作2

            if cnt1 < op1 and cnt2 < op2:
                x1 = math.ceil(x / 2)
                if x1 >= k:
                    res = min(res, x1 - k + f(i + 1, cnt1 + 1, cnt2 + 1)) # 先操作1後操作2
                if x >= k:
                    x2 = x - k
                    res = min(res, math.ceil(x2 / 2) + f(i + 1, cnt1 + 1, cnt2 + 1)) # 先操作2後操作1
            return res
        return f(0, 0, 0)
    

sol = Solution()
print(sol.minArraySum([2,8,3,19,3], 3, 1, 1)) # 23
print(sol.minArraySum([823,623,761,979], 426, 3, 4)) # 628