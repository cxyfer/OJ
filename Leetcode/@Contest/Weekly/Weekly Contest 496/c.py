import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *

class Solution:
    def minIncrease(self, nums: List[int]) -> int:
        n = len(nums)

        def calc(i: int) -> int:
            return max(max(nums[i - 1], nums[i + 1]) + 1 - nums[i], 0)

        if n & 1:
            return sum(calc(i) for i in range(1, n - 1, 2))

        arr1 = [calc(i) for i in range(1, n - 1, 2)]
        arr2 = [calc(i) for i in range(2, n - 1, 2)]

        ans = suf = sum(arr2)
        pre = 0
        for a, b in zip(arr1, arr2):
            pre += a
            suf -= b
            ans = min(ans, pre + suf)
        return ans

sol = Solution()
print(sol.minIncrease([1,2,2]))  # 1
print(sol.minIncrease([2,1,1,3]))  # 2
print(sol.minIncrease([5,2,1,4,3]))  # 4
print(sol.minIncrease([12,23,13,17,21,3]))  # 0