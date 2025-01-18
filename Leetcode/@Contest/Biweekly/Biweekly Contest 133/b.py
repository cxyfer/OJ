import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n - 2):
            if nums[i] == 0:
                nums[i] = 1
                nums[i + 1] ^= 1
                nums[i + 2] ^= 1
                ans += 1
        for i in range(n - 2, n):
            if nums[i] == 0:
                return -1
        return ans
