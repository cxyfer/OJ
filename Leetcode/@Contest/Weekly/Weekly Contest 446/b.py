import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *

class Solution:
    def maximumPossibleSize(self, nums: List[int]) -> int:
        pre = nums[0]
        ans = len(nums)
        for _, y in pairwise(nums):
            if y < pre:  # 需要刪除 y
                ans -= 1
            else:
                pre = y
        return ans

sol = Solution()
print(sol.maximumPossibleSize([1,2,3]))  # 3
print(sol.maximumPossibleSize([19,80,63,74]))  # 2