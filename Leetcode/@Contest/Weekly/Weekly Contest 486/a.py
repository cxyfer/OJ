import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *

class Solution:
    def minimumPrefixLength(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n - 1, 0, -1):
            if nums[i] <= nums[i - 1]:
                return i
        return 0