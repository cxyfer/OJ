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
        ans = 1
        target = nums[0] + nums[1]
        for i in range(2, n, 2):
            if i + 1 < n and nums[i] + nums[i + 1] == target:
                ans += 1
            else:
                break
        return ans