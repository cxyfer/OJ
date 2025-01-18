import math
from typing import *
from collections import *
from functools import lru_cache, cache
from heapq import *
from bisect import *
from itertools import *

class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        # return False if any(nums[i] & 1 == nums[i - 1] & 1 for i in range(1, len(nums))) else True
        n = len(nums)
        for i in range(1, n):
            if nums[i] & 1 == nums[i - 1] & 1:
                return False
        return True